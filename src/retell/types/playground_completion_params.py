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
    "MessageInjectedMessageBase",
    "MessageSMSMessageBase",
    "MessageSMSMessageBaseMultimedia",
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

    version: Union[str, int]
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


class MessageInjectedMessageBase(TypedDict, total=False):
    content: Required[str]
    """The injected context text."""

    role: Required[Literal["injected"]]
    """External context injected into the conversation via the update-live-call API.

    Not spoken by either party.
    """

    created_timestamp: int
    """Create timestamp of the message"""

    message_id: str
    """Unique id of the message"""


class MessageSMSMessageBaseMultimedia(TypedDict, total=False):
    url: Required[str]
    """URL of the multimedia attachment."""

    summary: str
    """Optional textual summary of the attachment."""


class MessageSMSMessageBase(TypedDict, total=False):
    content: Required[str]
    """Text content of the SMS message."""

    role: Required[Literal["sms"]]
    """SMS message exchanged during the call (for example received from the user).

    Woven into the transcript and shown to the agent, but not part of the spoken
    conversation.
    """

    created_timestamp: int
    """Create timestamp of the message"""

    message_id: str
    """Unique id of the message"""

    multimedia: Iterable[MessageSMSMessageBaseMultimedia]
    """Multimedia attachments (MMS).

    Display only; not relayed into the spoken conversation.
    """


Message: TypeAlias = Union[
    MessageMessageBase,
    MessageToolCallInvocationMessageBase,
    MessageToolCallResultMessageBase,
    MessageNodeTransitionMessageBase,
    MessageStateTransitionMessageBase,
    MessageInjectedMessageBase,
    MessageSMSMessageBase,
]


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
