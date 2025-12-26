# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VoiceAddResourceParams"]


class VoiceAddResourceParams(TypedDict, total=False):
    provider_voice_id: Required[str]
    """Voice id assigned by the provider."""

    voice_name: Required[str]
    """A custom name for the voice."""

    public_user_id: str
    """Required for ElevenLabs only. User id of the voice owner."""

    voice_provider: Literal["elevenlabs", "cartesia", "minimax"]
    """Voice provider to add the voice from."""
