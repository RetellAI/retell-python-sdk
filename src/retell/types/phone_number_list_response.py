# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .phone_number_response import PhoneNumberResponse

__all__ = ["PhoneNumberListResponse"]


class PhoneNumberListResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[PhoneNumberResponse]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
