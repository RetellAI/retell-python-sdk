# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes, SequenceNotStr

__all__ = ["VoiceCloneParams"]


class VoiceCloneParams(TypedDict, total=False):
    files: Required[SequenceNotStr[FileTypes]]
    """Audio files to use for voice cloning.

    Up to 25 files allowed. For Cartesia and MiniMax, only 1 file is supported. For
    Inworld, up to 3 files are supported.
    """

    voice_name: Required[str]
    """Name for the cloned voice"""

    voice_provider: Required[Literal["elevenlabs", "cartesia", "minimax", "fish_audio"]]
    """Voice provider to use for cloning."""
