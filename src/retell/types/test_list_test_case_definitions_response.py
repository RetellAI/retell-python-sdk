# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .test_case_definition_response import TestCaseDefinitionResponse

__all__ = ["TestListTestCaseDefinitionsResponse"]


class TestListTestCaseDefinitionsResponse(BaseModel):
    __test__ = False
    has_more: bool
    """Whether more results are available."""

    items: List[TestCaseDefinitionResponse]

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
