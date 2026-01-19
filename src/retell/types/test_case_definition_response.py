# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "TestCaseDefinitionResponse",
    "ResponseEngine",
    "ResponseEngineResponseEngineRetellLm",
    "ResponseEngineResponseEngineConversationFlow",
    "ToolMock",
    "ToolMockInputMatchRule",
    "ToolMockInputMatchRuleType",
    "ToolMockInputMatchRuleUnionMember1",
]


class ResponseEngineResponseEngineRetellLm(BaseModel):
    llm_id: str
    """id of the Retell LLM Response Engine."""

    type: Literal["retell-llm"]
    """type of the Response Engine."""

    version: Optional[float] = None
    """Version of the Retell LLM Response Engine."""


class ResponseEngineResponseEngineConversationFlow(BaseModel):
    conversation_flow_id: str
    """ID of the Conversation Flow Response Engine."""

    type: Literal["conversation-flow"]
    """type of the Response Engine."""

    version: Optional[float] = None
    """Version of the Conversation Flow Response Engine."""


ResponseEngine: TypeAlias = Union[ResponseEngineResponseEngineRetellLm, ResponseEngineResponseEngineConversationFlow]


class ToolMockInputMatchRuleType(BaseModel):
    type: Literal["any"]
    """Match any input of the tool"""


class ToolMockInputMatchRuleUnionMember1(BaseModel):
    args: Dict[str, object]
    """Arguments to match. Only provided fields will be checked"""

    type: Literal["partial_match"]
    """Match only calls with specific arguments"""


ToolMockInputMatchRule: TypeAlias = Union[ToolMockInputMatchRuleType, ToolMockInputMatchRuleUnionMember1]


class ToolMock(BaseModel):
    input_match_rule: ToolMockInputMatchRule
    """Rule for matching tool calls"""

    output: str
    """The output of the tool call that will be fed into the LLM.

    Should be a JSON string.
    """

    tool_name: str
    """Name of the tool to mock"""

    result: Optional[bool] = None
    """For tool calls like transfer_call that require a boolean result.

    Optional for most tools.
    """


class TestCaseDefinitionResponse(BaseModel):
    __test__ = False
    creation_timestamp: int
    """Timestamp when the test case definition was created (milliseconds since epoch)"""

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

    metrics: List[str]
    """Array of metric names to evaluate"""

    name: str
    """Name of the test case definition"""

    response_engine: ResponseEngine
    """Response engine to use for the test case. Custom LLM is not supported."""

    test_case_definition_id: str
    """Unique identifier for the test case definition"""

    tool_mocks: List[ToolMock]
    """Mock tool calls for testing"""

    type: Literal["simulation"]
    """Type of test case definition"""

    user_modified_timestamp: int
    """
    Timestamp when the test case definition was last modified (milliseconds since
    epoch)
    """

    user_prompt: str
    """User prompt to simulate in the test case"""
