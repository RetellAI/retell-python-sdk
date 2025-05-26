# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ChatResponse",
    "ChatAnalysis",
    "ChatCost",
    "ChatCostProductCost",
    "MessageWithToolCall",
    "MessageWithToolCallMessage",
    "MessageWithToolCallToolCallInvocationMessage",
    "MessageWithToolCallToolCallResultMessage",
    "MessageWithToolCallNodeTransitionMessage",
    "MessageWithToolCallStateTransitionMessage",
]


class ChatAnalysis(BaseModel):
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

    unit_price: float = FieldInfo(alias="unitPrice")
    """Unit price of the product in cents per second."""


class ChatCost(BaseModel):
    combined_cost: Optional[float] = None
    """Combined cost of all individual costs in cents"""

    product_costs: Optional[List[ChatCostProductCost]] = None
    """List of products with their unit prices and costs in cents"""


class MessageWithToolCallMessage(BaseModel):
    content: str
    """Content of the message"""

    created_timestamp: int
    """Create timestamp of the message"""

    message_id: str
    """Unique id ot the message"""

    role: Literal["agent", "user"]
    """Documents whether this message is sent by agent or user."""


class MessageWithToolCallToolCallInvocationMessage(BaseModel):
    arguments: str
    """Arguments for this tool call, it's a stringified JSON object."""

    message_id: str
    """Unique id ot the message"""

    name: str
    """Name of the function in this tool call."""

    role: Literal["tool_call_invocation"]
    """This is a tool call invocation."""

    tool_call_id: str
    """Tool call id, globally unique."""

    created_timestamp: Optional[int] = None
    """Create timestamp of the message"""


class MessageWithToolCallToolCallResultMessage(BaseModel):
    content: str
    """Result of the tool call, can be a string, a stringified json, etc."""

    created_timestamp: int
    """Create timestamp of the message"""

    message_id: str
    """Unique id ot the message"""

    role: Literal["tool_call_result"]
    """This is result of a tool call."""

    tool_call_id: str
    """Tool call id, globally unique."""


class MessageWithToolCallNodeTransitionMessage(BaseModel):
    created_timestamp: int
    """Create timestamp of the message"""

    message_id: str
    """Unique id ot the message"""

    role: Literal["node_transition"]
    """This is node transition."""

    former_node_id: Optional[str] = None
    """Former node id"""

    former_node_name: Optional[str] = None
    """Former node name"""

    new_node_id: Optional[str] = None
    """New node id"""

    new_node_name: Optional[str] = None
    """New node name"""


class MessageWithToolCallStateTransitionMessage(BaseModel):
    created_timestamp: int
    """Create timestamp of the message"""

    message_id: str
    """Unique id ot the message"""

    role: Literal["state_transition"]
    """This is state transition for ."""

    former_state_name: Optional[str] = None
    """Former state name"""

    new_state_name: Optional[str] = None
    """New state name"""


MessageWithToolCall: TypeAlias = Union[
    MessageWithToolCallMessage,
    MessageWithToolCallToolCallInvocationMessage,
    MessageWithToolCallToolCallResultMessage,
    MessageWithToolCallNodeTransitionMessage,
    MessageWithToolCallStateTransitionMessage,
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

    - `ended`: Chat session has ended can not generate new response.

    - `error`: Chat encountered error.
    """

    chat_analysis: Optional[ChatAnalysis] = None
    """
    Post chat analysis that includes information such as sentiment, status, summary,
    and custom defined data to extract. Available after chat ends. Subscribe to
    `chat_analyzed` webhook event type to receive it once ready.
    """

    chat_cost: Optional[ChatCost] = None

    collected_dynamic_variables: Optional[Dict[str, object]] = None
    """Dynamic variables collected from the chat. Only available after the chat ends."""

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

    retell_llm_dynamic_variables: Optional[Dict[str, object]] = None
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Response Engine prompt and tool description. Only applicable for Response
    Engine.
    """

    start_timestamp: Optional[int] = None
    """Begin timestamp (milliseconds since epoch) of the chat.

    Available after chat starts.
    """

    transcript: Optional[str] = None
    """Transcription of the chat."""
