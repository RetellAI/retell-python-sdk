# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VoiceSearchResponse", "Voice"]


class Voice(BaseModel):
    """Voices retrieved from the provider."""

    description: Optional[str] = None
    """Description of the voice."""

    name: Optional[str] = None
    """Name of the voice."""

    provider_voice_id: Optional[str] = None
    """id of the voice from the provider."""

    public_user_id: Optional[str] = None
    """For elevenlabs only. User id of the voice owner."""


class VoiceSearchResponse(BaseModel):
    voices: List[Voice]
