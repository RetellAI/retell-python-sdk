# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .test_case_job_response import TestCaseJobResponse

__all__ = ["TestListTestRunsResponse"]


class TestListTestRunsResponse(BaseModel):
    __test__ = False
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[TestCaseJobResponse]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
