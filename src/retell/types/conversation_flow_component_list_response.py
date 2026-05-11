# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .conversation_flow_component_response import ConversationFlowComponentResponse

__all__ = ["ConversationFlowComponentListResponse"]


class ConversationFlowComponentListResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[ConversationFlowComponentResponse]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
