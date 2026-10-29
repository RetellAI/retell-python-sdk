# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AppListTemplatesParams"]


class AppListTemplatesParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return."""

    pagination_key: str
    """Pagination key for fetching the next page."""

    privacy_scope: Literal["standard", "pci"]
    """Only include functions with this scope and apps providing them.

    Omit to include all scopes.
    """
