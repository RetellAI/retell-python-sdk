# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .conversation_flow_response import ConversationFlowResponse

__all__ = ["ConversationFlowListResponse"]


class ConversationFlowListResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[ConversationFlowResponse]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
