# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .batch_test_response import BatchTestResponse

__all__ = ["TestListBatchTestsResponse"]


class TestListBatchTestsResponse(BaseModel):
    __test__ = False
    has_more: bool
    """Whether more results are available."""

    items: List[BatchTestResponse]

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
