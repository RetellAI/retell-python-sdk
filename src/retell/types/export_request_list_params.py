# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExportRequestListParams"]


class ExportRequestListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return."""

    pagination_key: str
    """Pagination key for fetching the next page."""

    sort_order: Literal["ascending", "descending"]
    """Sort order for results."""
