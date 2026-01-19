# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TestListBatchTestsParams"]


class TestListBatchTestsParams(TypedDict, total=False):
    type: Required[Literal["retell-llm", "conversation-flow"]]
    """Type of response engine"""

    conversation_flow_id: str
    """Conversation flow ID (required when type is conversation-flow)"""

    llm_id: str
    """LLM ID (required when type is retell-llm)"""

    version: int
    """Version of the response engine (defaults to latest)"""
