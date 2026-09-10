# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .contact_response import ContactResponse

__all__ = ["ContactListResponse"]


class ContactListResponse(BaseModel):
    has_more: bool
    """Whether more results are available."""

    items: List[ContactResponse]

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""

    total: Optional[float] = None
    """Total count of contacts matching the filter."""
