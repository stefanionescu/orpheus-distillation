"""Conditional flow matching: the guided Euler sampler and the training loss."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast, override

import torch
from torch import nn
from pydantic import Field, BaseModel
from torch.nn import functional
import torch.func
import torch.nn.attention
from torch.nn.attention import SDPBackend

if TYPE_CHECKING:
    from contextlib import AbstractContextManager
    from collections.abc import Callable, Sequence

    from src.train.voxcpm_1_5.model.modules.locdit.local_dit import VoxCPMLocDit

SAMPLING_TEMPERATURE = 1.0
SWAY_SAMPLING_COEFFICIENT = 1.0
# CFG-Zero* zeroes the velocity for this fraction of the steps, at least one.
ZERO_STAR_INIT_FRACTION = 0.04
LOG_NORM_MEAN = -0.4
LOG_NORM_STD = 1.0
# Power zero turns off the adaptive loss weighting.
LOSS_WEIGHT_POWER = 0.0
LOSS_WEIGHT_EPSILON = 1e-3
# Keep the CFG-Zero* projection finite when the unconditional velocity is zero.
PROJECTION_EPSILON = 1e-8
# Forward-mode differentiation of attention works only with these kernels.
JVP_ATTENTION_BACKENDS = [SDPBackend.MATH, SDPBackend.CUDNN_ATTENTION]

_jvp = cast("Callable[..., tuple[torch.Tensor, torch.Tensor]]", torch.func.jvp)
_select_attention_backends = cast(
    "Callable[[Sequence[object]], AbstractContextManager[None]]", torch.nn.attention.sdpa_kernel
)


class CfmConfig(BaseModel):
    """Flow matching config, under `dit_config.cfm_config` in `config.json`.

    An alias names the `config.json` key of its field, so dump with `by_alias=True`.

    Attributes:
        sigma_min: Minimum noise level; nothing reads it.
        solver: ODE solver name; only `euler` exists.
        t_scheduler: Training timestep distribution, `log-norm` or `uniform`.
        condition_drop_rate: Chance to drop the condition in training, for classifier-free guidance.
        default_guidance_scale: Upstream default guidance scale; nothing reads it.
        reg_loss_type: Regression loss name; the loss ignores it and uses mean squared error.
        unequal_time_ratio_range: Fraction of mean-mode samples with two different times, at the start and
            end of training.
        noise_cond_prob_range: Chance to noise the previous patch, at the start and end of training.
        noise_cond_scale: Standard deviation of that noise.

    """

    sigma_min: float = 1e-6
    solver: str = "euler"
    t_scheduler: str = "log-norm"
    condition_drop_rate: float = Field(default=0.1, alias="training_cfg_rate")
    default_guidance_scale: float = Field(default=1.0, alias="inference_cfg_rate")
    reg_loss_type: str = "l1"
    unequal_time_ratio_range: tuple[float, float] = Field(default=(0.25, 0.75), alias="ratio_r_neq_t_range")
    noise_cond_prob_range: tuple[float, float] = (0.0, 0.0)
    noise_cond_scale: float = 0.0


class UnifiedCfm(nn.Module):
    """Flow matching around the diffusion estimator."""

    def __init__(
        self,
        in_channels: int,
        cfm_params: CfmConfig,
        estimator: VoxCPMLocDit,
        *,
        mean_mode: bool = False,
    ) -> None:
        """Store the flow matching settings and the estimator.

        Args:
            in_channels: Size of one latent frame.
            cfm_params: Flow matching config.
            estimator: Velocity estimator.
            mean_mode: Whether the estimator trains on the mean velocity between two times.

        """
        cast("Callable[[], None]", super().__init__)()
        self.t_scheduler = cfm_params.t_scheduler
        self.condition_drop_rate = cfm_params.condition_drop_rate
        self.unequal_time_ratio_range = cfm_params.unequal_time_ratio_range
        self.noise_cond_prob_range = cfm_params.noise_cond_prob_range
        self.noise_cond_scale = cfm_params.noise_cond_scale

        self.in_channels = in_channels
        self.mean_mode = mean_mode

        self.estimator = estimator

    @override
    @torch.inference_mode()
    def forward(
        self,
        mu: torch.Tensor,
        n_timesteps: int,
        patch_size: int,
        cond: torch.Tensor,
        guidance_scale: float = 1.0,
    ) -> torch.Tensor:
        """Sample one patch per sample from noise, with sway-sampled timesteps and guidance.

        Args:
            mu: Language model state that conditions each patch, shaped (batch, hidden_size).
            n_timesteps: Euler steps.
            patch_size: Latent frames per patch.
            cond: Previous patch, shaped (batch, in_channels, patch_size).
            guidance_scale: Classifier-free guidance scale.

        Returns:
            Patches, shaped (batch, in_channels, patch_size).

        """
        b, _ = mu.shape
        t = patch_size
        z = torch.randn((b, self.in_channels, t), device=mu.device, dtype=mu.dtype) * SAMPLING_TEMPERATURE

        t_span = torch.linspace(1, 0, n_timesteps + 1, device=mu.device, dtype=mu.dtype)
        t_span = t_span + SWAY_SAMPLING_COEFFICIENT * (torch.cos(torch.pi / 2 * t_span) - 1 + t_span)

        return self.solve_euler(x=z, t_span=t_span, mu=mu, cond=cond, guidance_scale=guidance_scale)

    def solve_euler(
        self,
        x: torch.Tensor,
        t_span: torch.Tensor,
        mu: torch.Tensor,
        cond: torch.Tensor,
        guidance_scale: float = 1.0,
    ) -> torch.Tensor:
        """Integrate the guided velocity from noise to a patch with Euler steps.

        CFG-Zero* zeroes the velocity of the first steps and scales the unconditional velocity by its projection
        onto the conditional one.

        Args:
            x: Noise, shaped (batch, in_channels, patch_size).
            t_span: Timesteps from one to zero.
            mu: Language model state that conditions each patch, shaped (batch, hidden_size).
            cond: Previous patch, shaped (batch, in_channels, prefix_length).
            guidance_scale: Classifier-free guidance scale.

        Returns:
            Patches, shaped like `x`.

        """
        t, dt = t_span[0], t_span[0] - t_span[1]

        zero_init_steps = max(1, int(len(t_span) * ZERO_STAR_INIT_FRACTION))
        for step in range(1, len(t_span)):
            if step <= zero_init_steps:
                velocity = torch.zeros_like(x)
            else:
                x_in, mu_in, t_in, cond_in, dt_in = self._build_guidance_inputs(x, mu, t, cond, dt)
                velocity = self.estimator(x_in, mu_in, t_in, cond_in, dt_in)
                velocity, unconditional_velocity = torch.split(velocity, [x.size(0), x.size(0)], dim=0)
                velocity = self._apply_zero_star_guidance(velocity, unconditional_velocity, guidance_scale)

            x = x - dt * velocity
            t = t - dt
            if step < len(t_span) - 1:
                dt = t - t_span[step + 1]

        return x

    def _build_guidance_inputs(
        self,
        x: torch.Tensor,
        mu: torch.Tensor,
        t: torch.Tensor,
        cond: torch.Tensor,
        dt: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        b = x.size(0)
        x_in = torch.zeros([2 * b, self.in_channels, x.size(2)], device=x.device, dtype=x.dtype)
        mu_in = torch.zeros([2 * b, mu.size(1)], device=x.device, dtype=x.dtype)
        t_in = torch.zeros([2 * b], device=x.device, dtype=x.dtype)
        dt_in = torch.zeros([2 * b], device=x.device, dtype=x.dtype)
        cond_in = torch.zeros([2 * b, self.in_channels, cond.size(2)], device=x.device, dtype=x.dtype)
        x_in[:b], x_in[b:] = x, x
        mu_in[:b] = mu
        t_in[:b], t_in[b:] = t.unsqueeze(0), t.unsqueeze(0)
        dt_in[:b], dt_in[b:] = dt.unsqueeze(0), dt.unsqueeze(0)
        # Only the mean mode conditions on the step size.
        if not self.mean_mode:
            dt_in = torch.zeros_like(dt_in)
        cond_in[:b], cond_in[b:] = cond, cond
        return x_in, mu_in, t_in, cond_in, dt_in

    def _apply_zero_star_guidance(
        self,
        velocity: torch.Tensor,
        unconditional_velocity: torch.Tensor,
        guidance_scale: float,
    ) -> torch.Tensor:
        b = velocity.size(0)
        positive_flat = velocity.view(b, -1)
        negative_flat = unconditional_velocity.view(b, -1)
        dot_product = torch.sum(positive_flat * negative_flat, dim=1, keepdim=True)
        squared_norm = torch.sum(negative_flat**2, dim=1, keepdim=True) + PROJECTION_EPSILON
        st_star = (dot_product / squared_norm).view(b, *([1] * (len(velocity.shape) - 1)))
        return unconditional_velocity * st_star + guidance_scale * (velocity - unconditional_velocity * st_star)

    def compute_loss(
        self,
        target: torch.Tensor,
        mu: torch.Tensor,
        cond: torch.Tensor | None = None,
        tgt_mask: torch.Tensor | None = None,
        progress: float = 0.0,
    ) -> torch.Tensor:
        """Compute the flow matching loss of a batch of target patches.

        Args:
            target: Target patches, shaped (patches, in_channels, patch_size).
            mu: Language model state that conditions each patch, shaped (patches, hidden_size).
            cond: Previous patches, shaped like `target`, or None for zeros.
            tgt_mask: Ones at the frames that count toward the loss, shaped (patches, 1, patch_size), or None
                to count every frame.
            progress: Fraction of training done; it schedules the condition noise and the mean-mode ratio.

        Returns:
            The scalar loss.

        """
        b, _, _ = target.shape

        if self.condition_drop_rate > 0:
            condition_mask = torch.rand(b, device=target.device) > self.condition_drop_rate
            mu = mu * condition_mask.view(-1, 1)

        if cond is None:
            cond = torch.zeros_like(target)

        cond = self._apply_cond_noise(cond, progress)
        unequal_time_ratio = self._compute_unequal_time_ratio(progress)

        r, t = self._sample_times(target, unequal_time_ratio)
        r_detached = r.detach().clone()
        t_detached = t.detach().clone()
        z = torch.randn_like(target)
        y = (1 - t_detached.view(-1, 1, 1)) * target + t_detached.view(-1, 1, 1) * z
        v = z - target

        def predict_velocity(z_sample: torch.Tensor, r_sample: torch.Tensor, t_sample: torch.Tensor) -> torch.Tensor:
            return cast("torch.Tensor", self.estimator(z_sample, mu, t_sample, cond, dt=t_sample - r_sample))

        if self.mean_mode:
            v_r = torch.zeros_like(r)
            v_t = torch.ones_like(t)
            with _select_attention_backends(JVP_ATTENTION_BACKENDS):
                u_pred, dudt = _jvp(predict_velocity, (y, r, t), (v, v_r, v_t))
            u_tgt = v - (t_detached - r_detached).view(-1, 1, 1) * dudt
        else:
            u_pred = predict_velocity(y, r, t)
            u_tgt = v

        losses = functional.mse_loss(u_pred, u_tgt.detach(), reduction="none").mean(dim=1)
        if tgt_mask is None:
            return losses.mean()
        weights = (1.0 / ((losses + LOSS_WEIGHT_EPSILON).pow(LOSS_WEIGHT_POWER)) * tgt_mask.squeeze(1)).detach()
        return (weights * losses).sum() / torch.sum(tgt_mask)

    def _apply_cond_noise(self, cond: torch.Tensor, progress: float) -> torch.Tensor:
        noise_prob = self.noise_cond_prob_range[0] + progress * (
            self.noise_cond_prob_range[1] - self.noise_cond_prob_range[0]
        )
        noisy_mask = torch.rand(cond.shape[0], device=cond.device) > (1.0 - noise_prob)
        return cond + noisy_mask.view(-1, 1, 1) * torch.randn_like(cond) * self.noise_cond_scale

    def _compute_unequal_time_ratio(self, progress: float) -> float:
        if not self.mean_mode:
            return 0.0
        low, high = self.unequal_time_ratio_range
        return low + progress * (high - low)

    def _sample_times(self, x: torch.Tensor, unequal_time_ratio: float) -> tuple[torch.Tensor, torch.Tensor]:
        batch_size = x.shape[0]
        if self.t_scheduler == "log-norm":
            s_r = torch.randn(batch_size, device=x.device, dtype=x.dtype) * LOG_NORM_STD + LOG_NORM_MEAN
            s_t = torch.randn(batch_size, device=x.device, dtype=x.dtype) * LOG_NORM_STD + LOG_NORM_MEAN
            r = torch.sigmoid(s_r)
            t = torch.sigmoid(s_t)
        elif self.t_scheduler == "uniform":
            r = torch.rand(batch_size, device=x.device, dtype=x.dtype)
            t = torch.rand(batch_size, device=x.device, dtype=x.dtype)
        else:
            message = f"Unsupported t_scheduler: {self.t_scheduler}"
            raise ValueError(message)

        mask = torch.rand(batch_size, device=x.device, dtype=x.dtype) < unequal_time_ratio
        r, t = torch.where(
            mask,
            torch.stack([torch.min(r, t), torch.max(r, t)], dim=0),
            torch.stack([t, t], dim=0),
        )

        return r.squeeze(), t.squeeze()
