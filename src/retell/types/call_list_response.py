# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from .._models import BaseModel
from .web_call_response import WebCallResponse
from .phone_call_response import PhoneCallResponse

__all__ = ["CallListResponse", "ItemCallWebCallResponse", "ItemCallPhoneCallResponse"]


class ItemCallWebCallResponse(WebCallResponse):
    """V3 list calls response. Transcript fields are intentionally omitted."""

    pass


class ItemCallPhoneCallResponse(PhoneCallResponse):
    """V3 list calls response. Transcript fields are intentionally omitted."""

    pass


class CallListResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[Union[ItemCallWebCallResponse, ItemCallPhoneCallResponse]]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
