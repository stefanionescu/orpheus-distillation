"""Autoregressive decoding of audio latents, one patch per step."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast
from dataclasses import dataclass

from tqdm import tqdm
import torch
import einops

from src.train.voxcpm_1_5.model.base import VoxCPMBase

if TYPE_CHECKING:
    from collections.abc import Callable

    from schemas.voxcpm_1_5.inference import SamplerSettings
    from src.train.voxcpm_1_5.model.modules.minicpm4.cache import StaticKvCache

# Ignore the stop head for the first steps so every call yields some audio.
MIN_DECODE_STEPS = 2

_rearrange = cast("Callable[..., torch.Tensor]", einops.rearrange)


@dataclass(frozen=True)
class DecodeInputs:
    """Prompt of one decoding run, batched to one sample.

    Attributes:
        text_tokens: Text token ids and the audio start token, shaped (1, length).
        text_mask: Ones at text positions, shaped (1, length).
        audio_feats: Prompt audio patches, zero at text positions, shaped (1, length, patch_size, latent_dim).
        audio_mask: Ones at prompt audio positions, shaped (1, length).

    """

    text_tokens: torch.Tensor
    text_mask: torch.Tensor
    audio_feats: torch.Tensor
    audio_mask: torch.Tensor


class VoxCPMInferenceMixin(VoxCPMBase):
    """Decoding loop: prefill both language models, then predict one patch per step."""

    @torch.inference_mode()
    def _decode_until_stop(self, inputs: DecodeInputs, settings: SamplerSettings) -> torch.Tensor:
        batch_size = inputs.audio_feats.shape[0]
        feat_embed, input_embed, prefix_feat_cond = self._embed_prompt(inputs)
        lm_hidden, residual_hidden, caches = self._prefill(inputs, input_embed, feat_embed)
        pred_feat_seq: list[torch.Tensor] = []
        for step in tqdm(range(settings.max_patches)):
            pred_feat, curr_embed = self._predict_patch(lm_hidden, residual_hidden, prefix_feat_cond, settings)
            pred_feat_seq.append(pred_feat.unsqueeze(1))
            prefix_feat_cond = pred_feat

            stop_logits = self.stop_head(self.stop_actn(self.stop_proj(lm_hidden)))
            if step > MIN_DECODE_STEPS and stop_logits.argmax(dim=-1)[0].cpu().item() == 1:
                break
            lm_hidden, residual_hidden = self._run_decode_step(curr_embed, caches)

        pred_feat_tensor = torch.cat(pred_feat_seq, dim=1)
        return _rearrange(pred_feat_tensor, "b t p d -> b d (t p)", b=batch_size, p=self.patch_size)

    def _embed_prompt(self, inputs: DecodeInputs) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        feat_embed = self.feat_encoder(inputs.audio_feats)
        feat_embed = self.enc_to_lm_proj(feat_embed)

        scale_emb = self.config.lm_config.scale_emb if self.config.lm_config.use_mup else 1.0
        text_embed = self.base_lm.embed_tokens(inputs.text_tokens) * scale_emb
        input_embed = inputs.text_mask.unsqueeze(-1) * text_embed + inputs.audio_mask.unsqueeze(-1) * feat_embed
        prefix_feat_cond = inputs.audio_feats[:, -1, ...]
        return feat_embed, input_embed, prefix_feat_cond

    def _prefill(
        self,
        inputs: DecodeInputs,
        input_embed: torch.Tensor,
        feat_embed: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, tuple[StaticKvCache, StaticKvCache]]:
        enc_outputs, kv_cache_tuple = self.base_lm(inputs_embeds=input_embed, is_causal=True)
        base_cache = self.base_lm.kv_cache
        residual_cache = self.residual_lm.kv_cache
        if base_cache is None or residual_cache is None:
            message = "KV cache not initialized"
            raise RuntimeError(message)
        base_cache.fill_caches(kv_cache_tuple)

        feat_mask = inputs.audio_mask.unsqueeze(-1)
        enc_outputs = self.fsq_layer(enc_outputs) * feat_mask + enc_outputs * inputs.text_mask.unsqueeze(-1)
        lm_hidden = enc_outputs[:, -1, :]

        residual_enc_outputs, residual_kv_cache_tuple = self.residual_lm(
            inputs_embeds=enc_outputs + feat_mask * feat_embed,
            is_causal=True,
        )
        residual_cache.fill_caches(residual_kv_cache_tuple)
        residual_hidden = residual_enc_outputs[:, -1, :]
        return lm_hidden, residual_hidden, (base_cache, residual_cache)

    def _predict_patch(
        self,
        lm_hidden: torch.Tensor,
        residual_hidden: torch.Tensor,
        prefix_feat_cond: torch.Tensor,
        settings: SamplerSettings,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        dit_hidden = self.lm_to_dit_proj(lm_hidden) + self.res_to_dit_proj(residual_hidden)
        pred_feat = self.feat_decoder(
            mu=dit_hidden,
            patch_size=self.patch_size,
            cond=prefix_feat_cond.transpose(1, 2).contiguous(),
            n_timesteps=settings.timesteps,
            guidance_scale=settings.guidance_scale,
        ).transpose(1, 2)
        curr_embed = self.feat_encoder(pred_feat.unsqueeze(1))
        curr_embed = self.enc_to_lm_proj(curr_embed)
        return pred_feat, curr_embed

    def _run_decode_step(
        self,
        curr_embed: torch.Tensor,
        caches: tuple[StaticKvCache, StaticKvCache],
    ) -> tuple[torch.Tensor, torch.Tensor]:
        base_cache, residual_cache = caches
        lm_hidden = self.base_lm.forward_step(
            curr_embed[:, 0, :],
            torch.tensor([base_cache.step()], device=curr_embed.device),
        ).clone()

        lm_hidden = self.fsq_layer(lm_hidden)
        residual_hidden = self.residual_lm.forward_step(
            lm_hidden + curr_embed[:, 0, :],
            torch.tensor([residual_cache.step()], device=curr_embed.device),
        ).clone()
        return lm_hidden, residual_hidden
