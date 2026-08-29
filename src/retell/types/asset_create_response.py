# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AssetCreateResponse"]


class AssetCreateResponse(BaseModel):
    asset_id: Optional[str] = None
    """Unique identifier for the asset."""

    content_type: Optional[str] = None
    """MIME type of the asset."""

    created_timestamp: Optional[float] = None
    """Unix timestamp of when the asset was created."""

    file_name: Optional[str] = None
    """Stored file name.

    Uploaded audio is normalized to headerless PCM and uses a `.pcm` extension.
    """

    file_size: Optional[float] = None
    """File size in bytes."""

    url: Optional[str] = None
    """CDN URL to access the asset."""
