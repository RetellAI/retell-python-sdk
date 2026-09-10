# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["AssetCreateParams"]


class AssetCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """Image or audio file to upload.

    Images support PNG, JPEG, GIF, WebP, and SVG. Audio supports MP3, WAV, WebM,
    OGG, M4A, AAC, and FLAC. Maximum size is 10 MB; audio is limited to 210 seconds.
    """
