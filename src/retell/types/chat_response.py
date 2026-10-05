# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ChatResponse",
    "ChatAnalysis",
    "ChatCost",
    "ChatCostProductCost",
    "MessageWithToolCall",
    "MessageWithToolCallMessageBase",
    "MessageWithToolCallMessageBaseMultimedia",
    "MessageWithToolCallToolCallInvocationMessageBase",
    "MessageWithToolCallToolCallResultMessageBase",
    "MessageWithToolCallNodeTransitionMessageBase",
    "MessageWithToolCallStateTransitionMessageBase",
    "MessageWithToolCallInjectedMessageBase",
    "MessageWithToolCallSMSMessageBase",
    "MessageWithToolCallSMSMessageBaseMultimedia",
    "PostSessionMessageWithToolCall",
    "PostSessionMessageWithToolCallMessageBase",
    "PostSessionMessageWithToolCallMessageBaseMultimedia",
    "PostSessionMessageWithToolCallToolCallInvocationMessageBase",
    "PostSessionMessageWithToolCallToolCallResultMessageBase",
    "PostSessionMessageWithToolCallNodeTransitionMessageBase",
    "PostSessionMessageWithToolCallStateTransitionMessageBase",
    "PostSessionMessageWithToolCallInjectedMessageBase",
    "PostSessionMessageWithToolCallSMSMessageBase",
    "PostSessionMessageWithToolCallSMSMessageBaseMultimedia",
    "PreSessionMessageWithToolCall",
    "PreSessionMessageWithToolCallMessageBase",
    "PreSessionMessageWithToolCallMessageBaseMultimedia",
    "PreSessionMessageWithToolCallToolCallInvocationMessageBase",
    "PreSessionMessageWithToolCallToolCallResultMessageBase",
    "PreSessionMessageWithToolCallNodeTransitionMessageBase",
    "PreSessionMessageWithToolCallStateTransitionMessageBase",
    "PreSessionMessageWithToolCallInjectedMessageBase",
    "PreSessionMessageWithToolCallSMSMessageBase",
    "PreSessionMessageWithToolCallSMSMessageBaseMultimedia",
    "ScrubbedPostSessionMessageWithToolCall",
    "ScrubbedPostSessionMessageWithToolCallMessageBase",
    "ScrubbedPostSessionMessageWithToolCallMessageBaseMultimedia",
    "ScrubbedPostSessionMessageWithToolCallToolCallInvocationMessageBase",
    "ScrubbedPostSessionMessageWithToolCallToolCallResultMessageBase",
    "ScrubbedPostSessionMessageWithToolCallNodeTransitionMessageBase",
    "ScrubbedPostSessionMessageWithToolCallStateTransitionMessageBase",
    "ScrubbedPostSessionMessageWithToolCallInjectedMessageBase",
    "ScrubbedPostSessionMessageWithToolCallSMSMessageBase",
    "ScrubbedPostSessionMessageWithToolCallSMSMessageBaseMultimedia",
    "ScrubbedPreSessionMessageWithToolCall",
    "ScrubbedPreSessionMessageWithToolCallMessageBase",
    "ScrubbedPreSessionMessageWithToolCallMessageBaseMultimedia",
    "ScrubbedPreSessionMessageWithToolCallToolCallInvocationMessageBase",
    "ScrubbedPreSessionMessageWithToolCallToolCallResultMessageBase",
    "ScrubbedPreSessionMessageWithToolCallNodeTransitionMessageBase",
    "ScrubbedPreSessionMessageWithToolCallStateTransitionMessageBase",
    "ScrubbedPreSessionMessageWithToolCallInjectedMessageBase",
    "ScrubbedPreSessionMessageWithToolCallSMSMessageBase",
    "ScrubbedPreSessionMessageWithToolCallSMSMessageBaseMultimedia",
]


class ChatAnalysis(BaseModel):
    """
    Post chat analysis that includes information such as sentiment, status, summary, and custom defined data to extract. Available after chat ends. Subscribe to `chat_analyzed` webhook event type to receive it once ready.
    """

    chat_successful: Optional[bool] = None
    """
    Whether the agent seems to have a successful chat with the user, where the agent
    finishes the task, and the call was complete without being cutoff.
    """

    chat_summary: Optional[str] = None
    """A high level summary of the chat."""

    custom_analysis_data: Optional[object] = None
    """
    Custom analysis data that was extracted based on the schema defined in chat
    agent post chat analysis data. Can be empty if nothing is specified.
    """

    user_sentiment: Optional[Literal["Negative", "Positive", "Neutral", "Unknown"]] = None
    """Sentiment of the user in the chat."""


class ChatCostProductCost(BaseModel):
    cost: float
    """Cost for the product in cents for the duration of the call."""

    product: str
    """Product name that has a cost associated with it."""

    is_transfer_leg_cost: Optional[bool] = None
    """True if this cost item is for a transfer segment."""

    unit_price: Optional[float] = None
    """Unit price of the product in cents per second."""


class ChatCost(BaseModel):
    combined_cost: Optional[float] = None
    """Combined cost of all individual costs in cents"""

    product_costs: Optional[List[ChatCostProductCost]] = None
    """List of products with their unit prices and costs in cents"""


class MessageWithToolCallMessageBaseMultimedia(BaseModel):
    url: str
    """URL of the multimedia attachment."""

    summary: Optional[str] = None
    """Optional textual summary of the attachment."""


class MessageWithToolCallMessageBase(BaseModel):
    content: str
    """Content of the message"""

    role: Literal["agent", "user"]
    """Documents whether this message is sent by agent or user."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    multimedia: Optional[List[MessageWithToolCallMessageBaseMultimedia]] = None
    """Multimedia attachments received with this message (MMS).

    Display only; a textual summary of each attachment is already included in
    content. Response only — supplying it in a request has no effect and is silently
    ignored. Omitted from PII-scrubbed messages.
    """


class MessageWithToolCallToolCallInvocationMessageBase(BaseModel):
    arguments: str
    """Arguments for this tool call, it's a stringified JSON object."""

    name: str
    """Name of the function in this tool call."""

    role: Literal["tool_call_invocation"]
    """This is a tool call invocation."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    thought_signature: Optional[str] = None
    """Optional thought signature from Google Gemini thinking models.

    This is used internally to maintain reasoning chain in multi-turn function
    calling.
    """


class MessageWithToolCallToolCallResultMessageBase(BaseModel):
    content: str
    """Result of the tool call, can be a string, a stringified json, etc."""

    role: Literal["tool_call_result"]
    """This is the result of a tool call."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    successful: Optional[bool] = None
    """Whether the tool call was successful."""


class MessageWithToolCallNodeTransitionMessageBase(BaseModel):
    role: Literal["node_transition"]
    """This is a node transition."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    former_node_id: Optional[str] = None
    """Former node id"""

    former_node_name: Optional[str] = None
    """Former node name"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    new_node_id: Optional[str] = None
    """New node id"""

    new_node_name: Optional[str] = None
    """New node name"""

    transition_type: Optional[Literal["global", "global_go_back", "interrupt_go_back", "normal"]] = None
    """How this node was reached.

    "global" means a global node transition, "global_go_back" means returning from a
    global node, "interrupt_go_back" means going back due to user interruption, and
    "normal" means a regular edge transition.
    """


class MessageWithToolCallStateTransitionMessageBase(BaseModel):
    role: Literal["state_transition"]
    """This is a state transition."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    former_state_name: Optional[str] = None
    """Former state name"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    new_state_name: Optional[str] = None
    """New state name"""


class MessageWithToolCallInjectedMessageBase(BaseModel):
    content: str
    """The injected context text."""

    role: Literal["injected"]
    """External context injected into the conversation via the update-live-call API.

    Not spoken by either party.
    """

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""


class MessageWithToolCallSMSMessageBaseMultimedia(BaseModel):
    url: str
    """URL of the multimedia attachment."""

    summary: Optional[str] = None
    """Optional textual summary of the attachment."""


class MessageWithToolCallSMSMessageBase(BaseModel):
    content: str
    """Text content of the SMS message."""

    role: Literal["sms"]
    """SMS message exchanged during the call (for example received from the user).

    Woven into the transcript and shown to the agent, but not part of the spoken
    conversation.
    """

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    multimedia: Optional[List[MessageWithToolCallSMSMessageBaseMultimedia]] = None
    """Multimedia attachments (MMS).

    Display only; not relayed into the spoken conversation.
    """


MessageWithToolCall: TypeAlias = Union[
    MessageWithToolCallMessageBase,
    MessageWithToolCallToolCallInvocationMessageBase,
    MessageWithToolCallToolCallResultMessageBase,
    MessageWithToolCallNodeTransitionMessageBase,
    MessageWithToolCallStateTransitionMessageBase,
    MessageWithToolCallInjectedMessageBase,
    MessageWithToolCallSMSMessageBase,
]


class PostSessionMessageWithToolCallMessageBaseMultimedia(BaseModel):
    url: str
    """URL of the multimedia attachment."""

    summary: Optional[str] = None
    """Optional textual summary of the attachment."""


class PostSessionMessageWithToolCallMessageBase(BaseModel):
    content: str
    """Content of the message"""

    role: Literal["agent", "user"]
    """Documents whether this message is sent by agent or user."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    multimedia: Optional[List[PostSessionMessageWithToolCallMessageBaseMultimedia]] = None
    """Multimedia attachments received with this message (MMS).

    Display only; a textual summary of each attachment is already included in
    content. Response only — supplying it in a request has no effect and is silently
    ignored. Omitted from PII-scrubbed messages.
    """


class PostSessionMessageWithToolCallToolCallInvocationMessageBase(BaseModel):
    arguments: str
    """Arguments for this tool call, it's a stringified JSON object."""

    name: str
    """Name of the function in this tool call."""

    role: Literal["tool_call_invocation"]
    """This is a tool call invocation."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    thought_signature: Optional[str] = None
    """Optional thought signature from Google Gemini thinking models.

    This is used internally to maintain reasoning chain in multi-turn function
    calling.
    """


class PostSessionMessageWithToolCallToolCallResultMessageBase(BaseModel):
    content: str
    """Result of the tool call, can be a string, a stringified json, etc."""

    role: Literal["tool_call_result"]
    """This is the result of a tool call."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    successful: Optional[bool] = None
    """Whether the tool call was successful."""


class PostSessionMessageWithToolCallNodeTransitionMessageBase(BaseModel):
    role: Literal["node_transition"]
    """This is a node transition."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    former_node_id: Optional[str] = None
    """Former node id"""

    former_node_name: Optional[str] = None
    """Former node name"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    new_node_id: Optional[str] = None
    """New node id"""

    new_node_name: Optional[str] = None
    """New node name"""

    transition_type: Optional[Literal["global", "global_go_back", "interrupt_go_back", "normal"]] = None
    """How this node was reached.

    "global" means a global node transition, "global_go_back" means returning from a
    global node, "interrupt_go_back" means going back due to user interruption, and
    "normal" means a regular edge transition.
    """


class PostSessionMessageWithToolCallStateTransitionMessageBase(BaseModel):
    role: Literal["state_transition"]
    """This is a state transition."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    former_state_name: Optional[str] = None
    """Former state name"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    new_state_name: Optional[str] = None
    """New state name"""


class PostSessionMessageWithToolCallInjectedMessageBase(BaseModel):
    content: str
    """The injected context text."""

    role: Literal["injected"]
    """External context injected into the conversation via the update-live-call API.

    Not spoken by either party.
    """

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""


class PostSessionMessageWithToolCallSMSMessageBaseMultimedia(BaseModel):
    url: str
    """URL of the multimedia attachment."""

    summary: Optional[str] = None
    """Optional textual summary of the attachment."""


class PostSessionMessageWithToolCallSMSMessageBase(BaseModel):
    content: str
    """Text content of the SMS message."""

    role: Literal["sms"]
    """SMS message exchanged during the call (for example received from the user).

    Woven into the transcript and shown to the agent, but not part of the spoken
    conversation.
    """

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    multimedia: Optional[List[PostSessionMessageWithToolCallSMSMessageBaseMultimedia]] = None
    """Multimedia attachments (MMS).

    Display only; not relayed into the spoken conversation.
    """


PostSessionMessageWithToolCall: TypeAlias = Union[
    PostSessionMessageWithToolCallMessageBase,
    PostSessionMessageWithToolCallToolCallInvocationMessageBase,
    PostSessionMessageWithToolCallToolCallResultMessageBase,
    PostSessionMessageWithToolCallNodeTransitionMessageBase,
    PostSessionMessageWithToolCallStateTransitionMessageBase,
    PostSessionMessageWithToolCallInjectedMessageBase,
    PostSessionMessageWithToolCallSMSMessageBase,
]


class PreSessionMessageWithToolCallMessageBaseMultimedia(BaseModel):
    url: str
    """URL of the multimedia attachment."""

    summary: Optional[str] = None
    """Optional textual summary of the attachment."""


class PreSessionMessageWithToolCallMessageBase(BaseModel):
    content: str
    """Content of the message"""

    role: Literal["agent", "user"]
    """Documents whether this message is sent by agent or user."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    multimedia: Optional[List[PreSessionMessageWithToolCallMessageBaseMultimedia]] = None
    """Multimedia attachments received with this message (MMS).

    Display only; a textual summary of each attachment is already included in
    content. Response only — supplying it in a request has no effect and is silently
    ignored. Omitted from PII-scrubbed messages.
    """


class PreSessionMessageWithToolCallToolCallInvocationMessageBase(BaseModel):
    arguments: str
    """Arguments for this tool call, it's a stringified JSON object."""

    name: str
    """Name of the function in this tool call."""

    role: Literal["tool_call_invocation"]
    """This is a tool call invocation."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    thought_signature: Optional[str] = None
    """Optional thought signature from Google Gemini thinking models.

    This is used internally to maintain reasoning chain in multi-turn function
    calling.
    """


class PreSessionMessageWithToolCallToolCallResultMessageBase(BaseModel):
    content: str
    """Result of the tool call, can be a string, a stringified json, etc."""

    role: Literal["tool_call_result"]
    """This is the result of a tool call."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    successful: Optional[bool] = None
    """Whether the tool call was successful."""


class PreSessionMessageWithToolCallNodeTransitionMessageBase(BaseModel):
    role: Literal["node_transition"]
    """This is a node transition."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    former_node_id: Optional[str] = None
    """Former node id"""

    former_node_name: Optional[str] = None
    """Former node name"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    new_node_id: Optional[str] = None
    """New node id"""

    new_node_name: Optional[str] = None
    """New node name"""

    transition_type: Optional[Literal["global", "global_go_back", "interrupt_go_back", "normal"]] = None
    """How this node was reached.

    "global" means a global node transition, "global_go_back" means returning from a
    global node, "interrupt_go_back" means going back due to user interruption, and
    "normal" means a regular edge transition.
    """


class PreSessionMessageWithToolCallStateTransitionMessageBase(BaseModel):
    role: Literal["state_transition"]
    """This is a state transition."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    former_state_name: Optional[str] = None
    """Former state name"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    new_state_name: Optional[str] = None
    """New state name"""


class PreSessionMessageWithToolCallInjectedMessageBase(BaseModel):
    content: str
    """The injected context text."""

    role: Literal["injected"]
    """External context injected into the conversation via the update-live-call API.

    Not spoken by either party.
    """

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""


class PreSessionMessageWithToolCallSMSMessageBaseMultimedia(BaseModel):
    url: str
    """URL of the multimedia attachment."""

    summary: Optional[str] = None
    """Optional textual summary of the attachment."""


class PreSessionMessageWithToolCallSMSMessageBase(BaseModel):
    content: str
    """Text content of the SMS message."""

    role: Literal["sms"]
    """SMS message exchanged during the call (for example received from the user).

    Woven into the transcript and shown to the agent, but not part of the spoken
    conversation.
    """

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    multimedia: Optional[List[PreSessionMessageWithToolCallSMSMessageBaseMultimedia]] = None
    """Multimedia attachments (MMS).

    Display only; not relayed into the spoken conversation.
    """


PreSessionMessageWithToolCall: TypeAlias = Union[
    PreSessionMessageWithToolCallMessageBase,
    PreSessionMessageWithToolCallToolCallInvocationMessageBase,
    PreSessionMessageWithToolCallToolCallResultMessageBase,
    PreSessionMessageWithToolCallNodeTransitionMessageBase,
    PreSessionMessageWithToolCallStateTransitionMessageBase,
    PreSessionMessageWithToolCallInjectedMessageBase,
    PreSessionMessageWithToolCallSMSMessageBase,
]


class ScrubbedPostSessionMessageWithToolCallMessageBaseMultimedia(BaseModel):
    url: str
    """URL of the multimedia attachment."""

    summary: Optional[str] = None
    """Optional textual summary of the attachment."""


class ScrubbedPostSessionMessageWithToolCallMessageBase(BaseModel):
    content: str
    """Content of the message"""

    role: Literal["agent", "user"]
    """Documents whether this message is sent by agent or user."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    multimedia: Optional[List[ScrubbedPostSessionMessageWithToolCallMessageBaseMultimedia]] = None
    """Multimedia attachments received with this message (MMS).

    Display only; a textual summary of each attachment is already included in
    content. Response only — supplying it in a request has no effect and is silently
    ignored. Omitted from PII-scrubbed messages.
    """


class ScrubbedPostSessionMessageWithToolCallToolCallInvocationMessageBase(BaseModel):
    arguments: str
    """Arguments for this tool call, it's a stringified JSON object."""

    name: str
    """Name of the function in this tool call."""

    role: Literal["tool_call_invocation"]
    """This is a tool call invocation."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    thought_signature: Optional[str] = None
    """Optional thought signature from Google Gemini thinking models.

    This is used internally to maintain reasoning chain in multi-turn function
    calling.
    """


class ScrubbedPostSessionMessageWithToolCallToolCallResultMessageBase(BaseModel):
    content: str
    """Result of the tool call, can be a string, a stringified json, etc."""

    role: Literal["tool_call_result"]
    """This is the result of a tool call."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    successful: Optional[bool] = None
    """Whether the tool call was successful."""


class ScrubbedPostSessionMessageWithToolCallNodeTransitionMessageBase(BaseModel):
    role: Literal["node_transition"]
    """This is a node transition."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    former_node_id: Optional[str] = None
    """Former node id"""

    former_node_name: Optional[str] = None
    """Former node name"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    new_node_id: Optional[str] = None
    """New node id"""

    new_node_name: Optional[str] = None
    """New node name"""

    transition_type: Optional[Literal["global", "global_go_back", "interrupt_go_back", "normal"]] = None
    """How this node was reached.

    "global" means a global node transition, "global_go_back" means returning from a
    global node, "interrupt_go_back" means going back due to user interruption, and
    "normal" means a regular edge transition.
    """


class ScrubbedPostSessionMessageWithToolCallStateTransitionMessageBase(BaseModel):
    role: Literal["state_transition"]
    """This is a state transition."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    former_state_name: Optional[str] = None
    """Former state name"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    new_state_name: Optional[str] = None
    """New state name"""


class ScrubbedPostSessionMessageWithToolCallInjectedMessageBase(BaseModel):
    content: str
    """The injected context text."""

    role: Literal["injected"]
    """External context injected into the conversation via the update-live-call API.

    Not spoken by either party.
    """

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""


class ScrubbedPostSessionMessageWithToolCallSMSMessageBaseMultimedia(BaseModel):
    url: str
    """URL of the multimedia attachment."""

    summary: Optional[str] = None
    """Optional textual summary of the attachment."""


class ScrubbedPostSessionMessageWithToolCallSMSMessageBase(BaseModel):
    content: str
    """Text content of the SMS message."""

    role: Literal["sms"]
    """SMS message exchanged during the call (for example received from the user).

    Woven into the transcript and shown to the agent, but not part of the spoken
    conversation.
    """

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    multimedia: Optional[List[ScrubbedPostSessionMessageWithToolCallSMSMessageBaseMultimedia]] = None
    """Multimedia attachments (MMS).

    Display only; not relayed into the spoken conversation.
    """


ScrubbedPostSessionMessageWithToolCall: TypeAlias = Union[
    ScrubbedPostSessionMessageWithToolCallMessageBase,
    ScrubbedPostSessionMessageWithToolCallToolCallInvocationMessageBase,
    ScrubbedPostSessionMessageWithToolCallToolCallResultMessageBase,
    ScrubbedPostSessionMessageWithToolCallNodeTransitionMessageBase,
    ScrubbedPostSessionMessageWithToolCallStateTransitionMessageBase,
    ScrubbedPostSessionMessageWithToolCallInjectedMessageBase,
    ScrubbedPostSessionMessageWithToolCallSMSMessageBase,
]


class ScrubbedPreSessionMessageWithToolCallMessageBaseMultimedia(BaseModel):
    url: str
    """URL of the multimedia attachment."""

    summary: Optional[str] = None
    """Optional textual summary of the attachment."""


class ScrubbedPreSessionMessageWithToolCallMessageBase(BaseModel):
    content: str
    """Content of the message"""

    role: Literal["agent", "user"]
    """Documents whether this message is sent by agent or user."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    multimedia: Optional[List[ScrubbedPreSessionMessageWithToolCallMessageBaseMultimedia]] = None
    """Multimedia attachments received with this message (MMS).

    Display only; a textual summary of each attachment is already included in
    content. Response only — supplying it in a request has no effect and is silently
    ignored. Omitted from PII-scrubbed messages.
    """


class ScrubbedPreSessionMessageWithToolCallToolCallInvocationMessageBase(BaseModel):
    arguments: str
    """Arguments for this tool call, it's a stringified JSON object."""

    name: str
    """Name of the function in this tool call."""

    role: Literal["tool_call_invocation"]
    """This is a tool call invocation."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    thought_signature: Optional[str] = None
    """Optional thought signature from Google Gemini thinking models.

    This is used internally to maintain reasoning chain in multi-turn function
    calling.
    """


class ScrubbedPreSessionMessageWithToolCallToolCallResultMessageBase(BaseModel):
    content: str
    """Result of the tool call, can be a string, a stringified json, etc."""

    role: Literal["tool_call_result"]
    """This is the result of a tool call."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    successful: Optional[bool] = None
    """Whether the tool call was successful."""


class ScrubbedPreSessionMessageWithToolCallNodeTransitionMessageBase(BaseModel):
    role: Literal["node_transition"]
    """This is a node transition."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    former_node_id: Optional[str] = None
    """Former node id"""

    former_node_name: Optional[str] = None
    """Former node name"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    new_node_id: Optional[str] = None
    """New node id"""

    new_node_name: Optional[str] = None
    """New node name"""

    transition_type: Optional[Literal["global", "global_go_back", "interrupt_go_back", "normal"]] = None
    """How this node was reached.

    "global" means a global node transition, "global_go_back" means returning from a
    global node, "interrupt_go_back" means going back due to user interruption, and
    "normal" means a regular edge transition.
    """


class ScrubbedPreSessionMessageWithToolCallStateTransitionMessageBase(BaseModel):
    role: Literal["state_transition"]
    """This is a state transition."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    former_state_name: Optional[str] = None
    """Former state name"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    new_state_name: Optional[str] = None
    """New state name"""


class ScrubbedPreSessionMessageWithToolCallInjectedMessageBase(BaseModel):
    content: str
    """The injected context text."""

    role: Literal["injected"]
    """External context injected into the conversation via the update-live-call API.

    Not spoken by either party.
    """

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""


class ScrubbedPreSessionMessageWithToolCallSMSMessageBaseMultimedia(BaseModel):
    url: str
    """URL of the multimedia attachment."""

    summary: Optional[str] = None
    """Optional textual summary of the attachment."""


class ScrubbedPreSessionMessageWithToolCallSMSMessageBase(BaseModel):
    content: str
    """Text content of the SMS message."""

    role: Literal["sms"]
    """SMS message exchanged during the call (for example received from the user).

    Woven into the transcript and shown to the agent, but not part of the spoken
    conversation.
    """

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""

    message_id: Optional[str] = None
    """Unique id of the message"""

    multimedia: Optional[List[ScrubbedPreSessionMessageWithToolCallSMSMessageBaseMultimedia]] = None
    """Multimedia attachments (MMS).

    Display only; not relayed into the spoken conversation.
    """


ScrubbedPreSessionMessageWithToolCall: TypeAlias = Union[
    ScrubbedPreSessionMessageWithToolCallMessageBase,
    ScrubbedPreSessionMessageWithToolCallToolCallInvocationMessageBase,
    ScrubbedPreSessionMessageWithToolCallToolCallResultMessageBase,
    ScrubbedPreSessionMessageWithToolCallNodeTransitionMessageBase,
    ScrubbedPreSessionMessageWithToolCallStateTransitionMessageBase,
    ScrubbedPreSessionMessageWithToolCallInjectedMessageBase,
    ScrubbedPreSessionMessageWithToolCallSMSMessageBase,
]


class ChatResponse(BaseModel):
    agent_id: str
    """Corresponding chat agent id of this chat."""

    chat_id: str
    """Unique id of the chat."""

    chat_status: Literal["ongoing", "ended", "error"]
    """Status of chat.

    - `ongoing`: Chat session is ongoing, chat agent can receive new message and
      generate response.
    - `ended`: Chat session has ended, and no longer can generate new response.
    - `error`: Chat encountered error.
    """

    agent_tag: Optional[str] = None
    """Tag pointing at the agent version used for this chat"""

    chat_analysis: Optional[ChatAnalysis] = None
    """
    Post chat analysis that includes information such as sentiment, status, summary,
    and custom defined data to extract. Available after chat ends. Subscribe to
    `chat_analyzed` webhook event type to receive it once ready.
    """

    chat_cost: Optional[ChatCost] = None

    chat_type: Optional[Literal["api_chat", "sms_chat"]] = None
    """Type of the chat"""

    collected_dynamic_variables: Optional[Dict[str, str]] = None
    """Dynamic variables collected from the chat. Only available after the chat ends."""

    custom_attributes: Optional[Dict[str, Union[str, float, bool]]] = None
    """Custom attributes for the chat"""

    end_timestamp: Optional[int] = None
    """End timestamp (milliseconds since epoch) of the chat.

    Available after chat ends.
    """

    message_with_tool_calls: Optional[List[MessageWithToolCall]] = None
    """Transcript of the chat weaved with tool call invocation and results."""

    metadata: Optional[object] = None
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    chat. Not used for processing. You can later get this field from the chat
    object.
    """

    post_session_message_with_tool_calls: Optional[List[PostSessionMessageWithToolCall]] = None
    """
    Tool call invocations and results of integration tools run after post-chat
    analysis (post-session). Stored separately from the main transcript. Available
    after chat ends if post-session integration tools ran.
    """

    pre_session_message_with_tool_calls: Optional[List[PreSessionMessageWithToolCall]] = None
    """
    Tool call invocations and results of integration tools run before the chat's
    first message (pre-session). Stored separately from the main transcript.
    Available once pre-session integration tools have run (from the chat's first
    turn).
    """

    retell_llm_dynamic_variables: Optional[Dict[str, str]] = None
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Response Engine prompt and tool description. Only applicable for Response
    Engine.
    """

    scrubbed_post_session_message_with_tool_calls: Optional[List[ScrubbedPostSessionMessageWithToolCall]] = None
    """Post-session integration tool call invocations and results, without PII.

    Available after chat ends if post-session integration tools ran and PII
    scrubbing is enabled.
    """

    scrubbed_pre_session_message_with_tool_calls: Optional[List[ScrubbedPreSessionMessageWithToolCall]] = None
    """Pre-session integration tool call invocations and results, without PII.

    Available after chat ends if pre-session integration tools ran and PII scrubbing
    is enabled.
    """

    start_timestamp: Optional[int] = None
    """Begin timestamp (milliseconds since epoch) of the chat.

    Available after chat starts.
    """

    transcript: Optional[str] = None
    """Transcription of the chat."""

    version: Optional[int] = None
    """The version of the agent"""
