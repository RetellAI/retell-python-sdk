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
        "gpt-5-mini",
        "gpt-5-nano",
        "gpt-5.1",
        "gpt-5.2",
        "gpt-5.4",
        "gpt-5.4-mini",
        "gpt-5.4-nano",
        "gpt-5.5",
        "claude-4.5-sonnet",
        "claude-4.6-sonnet",
        "claude-5-sonnet",
        "claude-4.5-haiku",
        "gemini-3.0-flash",
        "gemini-3.1-flash-lite",
        "gemini-3.5-flash",
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
    """Match every call to the tool, no matter what arguments were passed.

    Use this for a catch-all mock.
    """


class ToolMockInputMatchRuleUnionMember1(TypedDict, total=False):
    args: Required[object]
    """Argument values the call must have to match.

    Only the fields you list here are checked, and each must equal the value in the
    actual call. Extra fields in the call are ignored, so this is a subset match.
    """

    type: Required[Literal["partial_match"]]
    """Match only calls whose arguments contain the values listed in `args`."""


ToolMockInputMatchRule: TypeAlias = Union[ToolMockInputMatchRuleType, ToolMockInputMatchRuleUnionMember1]


class ToolMock(TypedDict, total=False):
    """A fake response for one tool.

    During a simulation, when the LLM calls a tool whose name matches `tool_name` and whose arguments satisfy `input_match_rule`, the real tool is not run; `output` is returned to the LLM instead. This keeps runs deterministic and avoids calling live integrations. A tool call that matches no mock falls through to the real tool.
    """

    input_match_rule: Required[ToolMockInputMatchRule]
    """Decides which calls to this tool the mock applies to."""

    output: Required[str]
    """The tool result fed back to the LLM in place of the real tool's output.

    Should be a JSON string, the same shape the real tool would return.
    """

    tool_name: Required[str]
    """The tool's function name, not the tool ID, i.e.

    the name the LLM uses when it calls the tool (for example
    `check_availability_cal`, `book_appointment_cal`, or the name you gave a custom
    function).
    """

    result: Optional[bool]
    """For tool calls like transfer_call that require a boolean result.

    Optional for most tools.
    """
