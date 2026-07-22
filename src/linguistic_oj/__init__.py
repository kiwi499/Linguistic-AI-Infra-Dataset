"""Core services for the Linguistic Online Judge."""

from .evaluation import (
    DependencyArc,
    DependencyScore,
    ExactMatchScore,
    SegmentationScore,
    TaggingScore,
    score_dependencies,
    score_exact_match,
    score_segmentation,
    score_tags,
)

__all__ = [
    "DependencyArc",
    "DependencyScore",
    "ExactMatchScore",
    "SegmentationScore",
    "TaggingScore",
    "score_dependencies",
    "score_exact_match",
    "score_segmentation",
    "score_tags",
]
