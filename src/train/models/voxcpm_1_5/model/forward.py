"""Training forward pass and the keys of its loss dict."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast, override

import torch
import einops

from src.train.models.voxcpm_1_5.model.base import VoxCPMBase

if TYPE_CHECKING:
    from collections.abc import Callable

    from schemas.models.voxcpm_1_5.batch import PackedBatch

_rearrange = cast("Callable[..., torch.Tensor]", einops.rearrange)

LOSS_DIFF_KEY = "loss/diff"
LOSS_STOP_KEY = "loss/stop"


class VoxCPMForwardMixin(VoxCPMBase):
    """Training forward pass: diffusion loss per patch and stop loss per position."""

    @override
    def forward(
        self,
        batch: PackedBatch,
        *,
        progress: float = 0.0,
    ) -> dict[str, torch.Tensor]:
        """Compute the training losses of one packed batch.

        Args:
            batch: Packed tensors of one step. The pass ignores `position_ids`.
            progress: Fraction of training done, from 0 to 1; it schedules the condition noise.

        Returns:
            Diffusion loss under `LOSS_DIFF_KEY`, stop loss under `LOSS_STOP_KEY`, and target features
            of shape (batch, feat_dim, positions * patch_size) under `feat_gt`.

        """
        prepared = self._prepare_inputs(batch)
        text_tokens, text_mask, audio_feats, audio_mask, loss_mask, labels, batch_size = prepared

        lm_hidden, feat_embed, enc_outputs = self._compute_lm_hidden(text_tokens, text_mask, audio_feats, audio_mask)
        residual_hidden = self._compute_residual_hidden(enc_outputs, audio_mask, feat_embed)
        dit_hidden, feat_gt, feat_cond, loss_seq_mask = self._build_diffusion_inputs(
            lm_hidden,
            residual_hidden,
            audio_feats,
            loss_mask,
        )

        diff_loss = self.feat_decoder.compute_loss(
            feat_gt.transpose(1, 2).contiguous(),
            dit_hidden,
            cond=feat_cond.transpose(1, 2).contiguous(),
            tgt_mask=loss_seq_mask.transpose(1, 2).contiguous(),
            progress=progress,
        )
        stop_loss = self._compute_stop_loss(lm_hidden, labels, loss_mask)

        feat_gt_tensor = _rearrange(feat_gt, "(b t) p d -> b d (t p)", b=batch_size, p=self.patch_size)

        return {
            LOSS_DIFF_KEY: diff_loss,
            LOSS_STOP_KEY: stop_loss,
            "feat_gt": feat_gt_tensor,
        }

    def _prepare_inputs(
        self,
        batch: PackedBatch,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, int]:
        text_tokens = batch.text_tokens.to(self.device, dtype=torch.long)
        text_mask = batch.text_mask.to(self.device, dtype=self._get_dtype())
        audio_feats = batch.audio_feats.to(self.device, dtype=self._get_dtype())
        audio_mask = batch.audio_mask.to(self.device, dtype=self._get_dtype())
        loss_mask = batch.loss_mask.to(self.device, dtype=self._get_dtype())
        labels = batch.labels.to(self.device, dtype=torch.long)
        batch_size = audio_feats.shape[0]
        return text_tokens, text_mask, audio_feats, audio_mask, loss_mask, labels, batch_size

    def _compute_lm_hidden(
        self,
        text_tokens: torch.Tensor,
        text_mask: torch.Tensor,
        audio_feats: torch.Tensor,
        audio_mask: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        feat_embed = self.feat_encoder(audio_feats)
        feat_embed = self.enc_to_lm_proj(feat_embed)

        scale_emb = self.config.lm_config.scale_emb if self.config.lm_config.use_mup else 1.0
        text_embed = self.base_lm.embed_tokens(text_tokens) * scale_emb
        input_embed = text_mask.unsqueeze(-1) * text_embed + audio_mask.unsqueeze(-1) * feat_embed

        enc_outputs, _ = self.base_lm(inputs_embeds=input_embed, is_causal=True)
        enc_outputs = enc_outputs.to(self._get_dtype())
        enc_outputs = self.fsq_layer(enc_outputs) * audio_mask.unsqueeze(-1) + enc_outputs * text_mask.unsqueeze(-1)
        lm_hidden = torch.cat((torch.zeros_like(enc_outputs[:, 0:1, :]), enc_outputs[:, :-1, :]), dim=1)
        return lm_hidden, feat_embed, enc_outputs

    def _compute_residual_hidden(
        self,
        enc_outputs: torch.Tensor,
        audio_mask: torch.Tensor,
        feat_embed: torch.Tensor,
    ) -> torch.Tensor:
        residual_inputs = enc_outputs + audio_mask.unsqueeze(-1) * feat_embed
        residual_outputs, _ = self.residual_lm(inputs_embeds=residual_inputs, is_causal=True)
        residual_outputs = residual_outputs.to(self._get_dtype())
        return torch.cat((torch.zeros_like(residual_outputs[:, 0:1, :]), residual_outputs[:, :-1, :]), dim=1)

    def _build_diffusion_inputs(
        self,
        lm_hidden: torch.Tensor,
        residual_hidden: torch.Tensor,
        audio_feats: torch.Tensor,
        loss_mask: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        dit_hidden = self.lm_to_dit_proj(lm_hidden) + self.res_to_dit_proj(residual_hidden)
        dit_hidden = _rearrange(dit_hidden, "b t c -> (b t) c")

        target_dtype = self._get_dtype()
        feat_gt = _rearrange(audio_feats.to(target_dtype), "b t p d -> (b t) p d")
        feat_cond = torch.cat((torch.zeros_like(audio_feats[:, 0:1, ...]), audio_feats[:, :-1, ...]), dim=1)
        feat_cond = _rearrange(feat_cond.to(target_dtype), "b t p d -> (b t) p d")
        loss_seq_mask = loss_mask.unsqueeze(-1).repeat(1, 1, self.patch_size)
        loss_seq_mask = _rearrange(loss_seq_mask, "b t p -> (b t) p 1").to(target_dtype)
        return dit_hidden, feat_gt, feat_cond, loss_seq_mask

    def _compute_stop_loss(
        self,
        lm_hidden: torch.Tensor,
        labels: torch.Tensor,
        loss_mask: torch.Tensor,
    ) -> torch.Tensor:
        stop_logits = self.stop_head(self.stop_actn(self.stop_proj(lm_hidden)))
        stop_losses = self.stop_loss(stop_logits.transpose(1, 2), labels)
        denom = torch.clamp(loss_mask.sum(), min=1.0)
        return cast("torch.Tensor", (stop_losses * loss_mask).sum() / denom)
