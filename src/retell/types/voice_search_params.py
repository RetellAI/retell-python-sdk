# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VoiceSearchParams"]


class VoiceSearchParams(TypedDict, total=False):
    search_query: Required[str]
    """Search query to find voices by name, description, or ID."""

    voice_provider: Literal["elevenlabs", "cartesia", "minimax"]
    """Voice provider to search."""
