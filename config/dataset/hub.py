"""Size categories of the dataset card and the clip count each one stays below."""

from __future__ import annotations

SIZE_CATEGORY_BOUNDS = (
    (1_000, "n<1K"),
    (10_000, "1K<n<10K"),
    (100_000, "10K<n<100K"),
    (1_000_000, "100K<n<1M"),
)
