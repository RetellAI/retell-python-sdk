# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TestListTestRunsParams"]


class TestListTestRunsParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return."""

    pagination_key: str
    """Pagination key for fetching the next page."""
