# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VoiceResponse"]


class VoiceResponse(BaseModel):
    gender: Literal["male", "female"]
    """Gender of voice."""

    provider: Literal["elevenlabs", "openai", "deepgram"]
    """Indicates the provider of voice."""

    voice_id: str
    """Unique id for the voice."""

    voice_name: str
    """Name of the voice."""

    accent: Optional[str] = None
    """Accent annotation of the voice."""

    age: Optional[str] = None
    """Age annotation of the voice."""

    preview_audio_url: Optional[str] = None
    """URL to the preview audio of the voice."""
