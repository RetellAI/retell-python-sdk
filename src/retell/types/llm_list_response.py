# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .llm_response import LlmResponse

__all__ = ["LlmListResponse"]


class LlmListResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[LlmResponse]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
