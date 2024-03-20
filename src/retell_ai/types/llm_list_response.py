# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "LlmListResponse",
    "LlmListResponseItem",
    "LlmListResponseItemGeneralTool",
    "LlmListResponseItemGeneralToolEndCallTool",
    "LlmListResponseItemGeneralToolTransferCallTool",
    "LlmListResponseItemGeneralToolCustomTool",
    "LlmListResponseItemGeneralToolCustomToolParameters",
    "LlmListResponseItemState",
    "LlmListResponseItemStateEdge",
    "LlmListResponseItemStateEdgeParameters",
    "LlmListResponseItemStateTool",
    "LlmListResponseItemStateToolEndCallTool",
    "LlmListResponseItemStateToolTransferCallTool",
    "LlmListResponseItemStateToolCustomTool",
    "LlmListResponseItemStateToolCustomToolParameters",
]


class LlmListResponseItemGeneralToolEndCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["end_call"]] = None

    type: Optional[Literal["pre_defined"]] = None


class LlmListResponseItemGeneralToolTransferCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["transfer_call"]] = None

    number: Optional[str] = None

    type: Optional[Literal["pre_defined"]] = None


class LlmListResponseItemGeneralToolCustomToolParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class LlmListResponseItemGeneralToolCustomTool(BaseModel):
    description: Optional[str] = None

    execution_message_description: Optional[str] = None

    execution_timing: Optional[Literal["immediate", "await_agent_turn"]] = None

    name: Optional[str] = None

    parameters: Optional[LlmListResponseItemGeneralToolCustomToolParameters] = None

    speak_after_execution: Optional[bool] = None

    speak_during_execution: Optional[bool] = None

    type: Optional[Literal["custom"]] = None

    url: Optional[str] = None


LlmListResponseItemGeneralTool = Union[
    LlmListResponseItemGeneralToolEndCallTool,
    LlmListResponseItemGeneralToolTransferCallTool,
    LlmListResponseItemGeneralToolCustomTool,
]


class LlmListResponseItemStateEdgeParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class LlmListResponseItemStateEdge(BaseModel):
    description: Optional[str] = None

    destination_state_name: Optional[str] = FieldInfo(alias="destinationStateName", default=None)

    parameters: Optional[LlmListResponseItemStateEdgeParameters] = None

    speak_during_transition: Optional[bool] = FieldInfo(alias="speakDuringTransition", default=None)


class LlmListResponseItemStateToolEndCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["end_call"]] = None

    type: Optional[Literal["pre_defined"]] = None


class LlmListResponseItemStateToolTransferCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["transfer_call"]] = None

    number: Optional[str] = None

    type: Optional[Literal["pre_defined"]] = None


class LlmListResponseItemStateToolCustomToolParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class LlmListResponseItemStateToolCustomTool(BaseModel):
    description: Optional[str] = None

    execution_message_description: Optional[str] = None

    execution_timing: Optional[Literal["immediate", "await_agent_turn"]] = None

    name: Optional[str] = None

    parameters: Optional[LlmListResponseItemStateToolCustomToolParameters] = None

    speak_after_execution: Optional[bool] = None

    speak_during_execution: Optional[bool] = None

    type: Optional[Literal["custom"]] = None

    url: Optional[str] = None


LlmListResponseItemStateTool = Union[
    LlmListResponseItemStateToolEndCallTool,
    LlmListResponseItemStateToolTransferCallTool,
    LlmListResponseItemStateToolCustomTool,
]


class LlmListResponseItemState(BaseModel):
    edges: Optional[List[LlmListResponseItemStateEdge]] = None

    name: Optional[str] = None

    state_prompt: Optional[str] = None

    tools: Optional[List[LlmListResponseItemStateTool]] = None


class LlmListResponseItem(BaseModel):
    begin_message: Optional[str] = None
    """Optional first phrase said by the agent."""

    general_prompt: Optional[str] = None
    """General prompt used in every state."""

    general_tools: Optional[List[LlmListResponseItemGeneralTool]] = None
    """Optional array of tools used in every state."""

    last_modification_timestamp: Optional[int] = None
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    llm_id: Optional[str] = None
    """Unique id of Retell LLM."""

    starting_state: Optional[str] = None
    """Optional identifier of the starting state."""

    states: Optional[List[LlmListResponseItemState]] = None
    """Optional array of states for the agent."""


LlmListResponse = List[LlmListResponseItem]
