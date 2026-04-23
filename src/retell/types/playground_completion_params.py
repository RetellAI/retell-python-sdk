# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "PlaygroundCompletionParams",
    "Message",
    "MessageMessageBase",
    "MessageToolCallInvocationMessageBase",
    "MessageToolCallResultMessageBase",
    "MessageNodeTransitionMessageBase",
    "MessageStateTransitionMessageBase",
    "ToolMock",
    "ToolMockInputMatchRule",
    "ToolMockInputMatchRuleType",
    "ToolMockInputMatchRuleUnionMember1",
]


class PlaygroundCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """Full conversation history, same shape as chat completion messages.

    message_id and created_timestamp are optional — server generates them if
    omitted.
    """

    version: int
    """Agent version to use. Defaults to latest."""

    component_id: str
    """Conversation flow component id.

    Required when current_node_id refers to a node within a component.
    """

    current_node_id: str
    """Current node id for conversation-flow agents.

    Used to resume from a specific node. Must be provided together with component_id
    when testing components.
    """

    current_state: str
    """Current state name for retell-llm agents. Used to resume from a specific state."""

    dynamic_variables: Dict[str, str]
    """Key-value pairs for dynamic variable substitution."""

    tool_mocks: Iterable[ToolMock]
    """Optional mock responses for tools.

    When provided, the agent uses these instead of executing real tool calls.
    """


class MessageMessageBase(TypedDict, total=False):
    content: Required[str]
    """Content of the message"""

    role: Required[Literal["agent", "user"]]
    """Documents whether this message is sent by agent or user."""

    created_timestamp: int
    """Create timestamp of the message"""

    message_id: str
    """Unique id of the message"""


class MessageToolCallInvocationMessageBase(TypedDict, total=False):
    arguments: Required[str]
    """Arguments for this tool call, it's a stringified JSON object."""

    name: Required[str]
    """Name of the function in this tool call."""

    role: Required[Literal["tool_call_invocation"]]
    """This is a tool call invocation."""

    tool_call_id: Required[str]
    """Tool call id, globally unique."""

    created_timestamp: int
    """Create timestamp of the message"""

    message_id: str
    """Unique id of the message"""

    thought_signature: str
    """Optional thought signature from Google Gemini thinking models.

    This is used internally to maintain reasoning chain in multi-turn function
    calling.
    """


class MessageToolCallResultMessageBase(TypedDict, total=False):
    content: Required[str]
    """Result of the tool call, can be a string, a stringified json, etc."""

    role: Required[Literal["tool_call_result"]]
    """This is the result of a tool call."""

    tool_call_id: Required[str]
    """Tool call id, globally unique."""

    created_timestamp: int
    """Create timestamp of the message"""

    message_id: str
    """Unique id of the message"""

    successful: bool
    """Whether the tool call was successful."""


class MessageNodeTransitionMessageBase(TypedDict, total=False):
    role: Required[Literal["node_transition"]]
    """This is a node transition."""

    created_timestamp: int
    """Create timestamp of the message"""

    former_node_id: str
    """Former node id"""

    former_node_name: str
    """Former node name"""

    message_id: str
    """Unique id of the message"""

    new_node_id: str
    """New node id"""

    new_node_name: str
    """New node name"""

    transition_type: Literal["global", "global_go_back", "interrupt_go_back", "normal"]
    """How this node was reached.

    "global" means a global node transition, "global_go_back" means returning from a
    global node, "interrupt_go_back" means going back due to user interruption, and
    "normal" means a regular edge transition.
    """


class MessageStateTransitionMessageBase(TypedDict, total=False):
    role: Required[Literal["state_transition"]]
    """This is a state transition."""

    created_timestamp: int
    """Create timestamp of the message"""

    former_state_name: str
    """Former state name"""

    message_id: str
    """Unique id of the message"""

    new_state_name: str
    """New state name"""


Message: TypeAlias = Union[
    MessageMessageBase,
    MessageToolCallInvocationMessageBase,
    MessageToolCallResultMessageBase,
    MessageNodeTransitionMessageBase,
    MessageStateTransitionMessageBase,
]


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
