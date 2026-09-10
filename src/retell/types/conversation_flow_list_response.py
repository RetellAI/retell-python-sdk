# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .conversation_flow_response import ConversationFlowResponse

__all__ = ["ConversationFlowListResponse"]


class ConversationFlowListResponse(BaseModel):
    has_more: bool
    """Whether more results are available."""

    items: List[ConversationFlowResponse]

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
