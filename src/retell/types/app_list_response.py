# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .app_response import AppResponse

__all__ = ["AppListResponse"]


class AppListResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[AppResponse]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
