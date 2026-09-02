# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .phone_number_response import PhoneNumberResponse

__all__ = ["PhoneNumberListResponse"]


class PhoneNumberListResponse(BaseModel):
    has_more: bool
    """Whether more results are available."""

    items: List[PhoneNumberResponse]

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
