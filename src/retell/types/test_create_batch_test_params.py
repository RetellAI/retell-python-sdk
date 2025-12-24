# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "TestCreateBatchTestParams",
    "ResponseEngine",
    "ResponseEngineResponseEngineRetellLm",
    "ResponseEngineResponseEngineConversationFlow",
]


class TestCreateBatchTestParams(TypedDict, total=False):
    response_engine: Required[ResponseEngine]
    """Response engine to use for the test cases. Custom LLM is not supported."""

    test_case_definition_ids: Required[SequenceNotStr[str]]
    """Array of test case definition IDs to run"""

    reserved_concurrency: int
    """
    Number of concurrency reserved for all other calls that are not triggered by
    batch calls, such as inbound calls.
    """


class ResponseEngineResponseEngineRetellLm(TypedDict, total=False):
    llm_id: Required[str]
    """id of the Retell LLM Response Engine."""

    type: Required[Literal["retell-llm"]]
    """type of the Response Engine."""

    version: Optional[float]
    """Version of the Retell LLM Response Engine."""


class ResponseEngineResponseEngineConversationFlow(TypedDict, total=False):
    conversation_flow_id: Required[str]
    """ID of the Conversation Flow Response Engine."""

    type: Required[Literal["conversation-flow"]]
    """type of the Response Engine."""

    version: Optional[float]
    """Version of the Conversation Flow Response Engine."""


ResponseEngine: TypeAlias = Union[ResponseEngineResponseEngineRetellLm, ResponseEngineResponseEngineConversationFlow]
