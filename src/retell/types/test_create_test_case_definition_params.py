# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "TestCreateTestCaseDefinitionParams",
    "ResponseEngine",
    "ResponseEngineResponseEngineRetellLm",
    "ResponseEngineResponseEngineConversationFlow",
    "ToolMock",
    "ToolMockInputMatchRule",
    "ToolMockInputMatchRuleType",
    "ToolMockInputMatchRuleUnionMember1",
]


class TestCreateTestCaseDefinitionParams(TypedDict, total=False):
    metrics: Required[SequenceNotStr[str]]
    """Array of metric names to evaluate"""

    name: Required[str]
    """Name of the test case definition"""

    response_engine: Required[ResponseEngine]
    """Response engine to use for the test case. Custom LLM is not supported."""

    user_prompt: Required[str]
    """User prompt to simulate in the test case"""

    dynamic_variables: Dict[str, str]
    """Dynamic variables to inject into the response engine"""

    llm_model: Literal[
        "gpt-4.1",
        "gpt-4.1-mini",
        "gpt-4.1-nano",
        "gpt-5",
        "gpt-5.1",
        "gpt-5.2",
        "gpt-5-mini",
        "gpt-5-nano",
        "claude-4.5-sonnet",
        "claude-4.5-haiku",
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        "gemini-3.0-flash",
    ]
    """LLM model to use for simulation"""

    tool_mocks: Iterable[ToolMock]
    """Mock tool calls for testing"""


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


class ToolMockInputMatchRuleType(TypedDict, total=False):
    type: Required[Literal["any"]]
    """Match any input of the tool"""


class ToolMockInputMatchRuleUnionMember1(TypedDict, total=False):
    args: Required[Dict[str, object]]
    """Arguments to match. Only provided fields will be checked"""

    type: Required[Literal["partial_match"]]
    """Match only calls with specific arguments"""


ToolMockInputMatchRule: TypeAlias = Union[ToolMockInputMatchRuleType, ToolMockInputMatchRuleUnionMember1]


class ToolMock(TypedDict, total=False):
    input_match_rule: Required[ToolMockInputMatchRule]
    """Rule for matching tool calls"""

    output: Required[str]
    """The output of the tool call that will be fed into the LLM.

    Should be a JSON string.
    """

    tool_name: Required[str]
    """Name of the tool to mock"""

    result: Optional[bool]
    """For tool calls like transfer_call that require a boolean result.

    Optional for most tools.
    """
