# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VoiceResponse"]


class VoiceResponse(BaseModel):
    gender: Literal["male", "female"]
    """Gender of voice."""

    provider: Literal["elevenlabs", "openai", "cartesia", "minimax", "fish_audio", "inworld", "platform", "xai"]
    """Indicates the provider of voice.

    `xai` voices can only be used with the `grok-voice-3.0` speech-to-speech model.
    """

    voice_id: str
    """Unique id for the voice."""

    voice_name: str
    """Name of the voice."""

    accent: Optional[str] = None
    """Accent annotation of the voice."""

    age: Optional[str] = None
    """Age annotation of the voice."""

    avatar_url: Optional[str] = None
    """URL to the avatar image of the voice."""

    preview_audio_url: Optional[str] = None
    """URL to the preview audio of the voice."""
