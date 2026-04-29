# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExportRequestListResponse", "Item"]


class Item(BaseModel):
    channel: Optional[Literal["call", "chat"]] = None

    created_timestamp: Optional[int] = None

    export_request_id: Optional[str] = None

    status: Optional[Literal["created", "processing", "completed", "error"]] = None

    timezone: Optional[str] = None

    url: Optional[str] = None


class ExportRequestListResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[Item]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
