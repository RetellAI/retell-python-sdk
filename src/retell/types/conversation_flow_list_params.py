# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationFlowListParams"]


class ConversationFlowListParams(TypedDict, total=False):
    limit: int

    pagination_key: str

    pagination_key_version: int
