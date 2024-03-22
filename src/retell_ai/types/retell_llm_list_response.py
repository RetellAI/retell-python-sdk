# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "RetellLlmListResponse",
    "RetellLlmListResponseItem",
    "RetellLlmListResponseItemGeneralTool",
    "RetellLlmListResponseItemGeneralToolEndCallTool",
    "RetellLlmListResponseItemGeneralToolTransferCallTool",
    "RetellLlmListResponseItemGeneralToolCustomTool",
    "RetellLlmListResponseItemGeneralToolCustomToolParameters",
    "RetellLlmListResponseItemState",
    "RetellLlmListResponseItemStateEdge",
    "RetellLlmListResponseItemStateEdgeParameters",
    "RetellLlmListResponseItemStateTool",
    "RetellLlmListResponseItemStateToolEndCallTool",
    "RetellLlmListResponseItemStateToolTransferCallTool",
    "RetellLlmListResponseItemStateToolCustomTool",
    "RetellLlmListResponseItemStateToolCustomToolParameters",
]


class RetellLlmListResponseItemGeneralToolEndCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["end_call"]] = None

    type: Optional[Literal["pre_defined"]] = None


class RetellLlmListResponseItemGeneralToolTransferCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["transfer_call"]] = None

    number: Optional[str] = None

    type: Optional[Literal["pre_defined"]] = None


class RetellLlmListResponseItemGeneralToolCustomToolParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class RetellLlmListResponseItemGeneralToolCustomTool(BaseModel):
    description: Optional[str] = None

    execution_message_description: Optional[str] = None

    execution_timing: Optional[Literal["immediate", "await_agent_turn"]] = None

    name: Optional[str] = None

    parameters: Optional[RetellLlmListResponseItemGeneralToolCustomToolParameters] = None

    speak_after_execution: Optional[bool] = None

    speak_during_execution: Optional[bool] = None

    type: Optional[Literal["custom"]] = None

    url: Optional[str] = None


RetellLlmListResponseItemGeneralTool = Union[
    RetellLlmListResponseItemGeneralToolEndCallTool,
    RetellLlmListResponseItemGeneralToolTransferCallTool,
    RetellLlmListResponseItemGeneralToolCustomTool,
]


class RetellLlmListResponseItemStateEdgeParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class RetellLlmListResponseItemStateEdge(BaseModel):
    description: Optional[str] = None

    destination_state_name: Optional[str] = FieldInfo(alias="destinationStateName", default=None)

    parameters: Optional[RetellLlmListResponseItemStateEdgeParameters] = None

    speak_during_transition: Optional[bool] = FieldInfo(alias="speakDuringTransition", default=None)


class RetellLlmListResponseItemStateToolEndCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["end_call"]] = None

    type: Optional[Literal["pre_defined"]] = None


class RetellLlmListResponseItemStateToolTransferCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["transfer_call"]] = None

    number: Optional[str] = None

    type: Optional[Literal["pre_defined"]] = None


class RetellLlmListResponseItemStateToolCustomToolParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class RetellLlmListResponseItemStateToolCustomTool(BaseModel):
    description: Optional[str] = None

    execution_message_description: Optional[str] = None

    execution_timing: Optional[Literal["immediate", "await_agent_turn"]] = None

    name: Optional[str] = None

    parameters: Optional[RetellLlmListResponseItemStateToolCustomToolParameters] = None

    speak_after_execution: Optional[bool] = None

    speak_during_execution: Optional[bool] = None

    type: Optional[Literal["custom"]] = None

    url: Optional[str] = None


RetellLlmListResponseItemStateTool = Union[
    RetellLlmListResponseItemStateToolEndCallTool,
    RetellLlmListResponseItemStateToolTransferCallTool,
    RetellLlmListResponseItemStateToolCustomTool,
]


class RetellLlmListResponseItemState(BaseModel):
    edges: Optional[List[RetellLlmListResponseItemStateEdge]] = None

    name: Optional[str] = None

    state_prompt: Optional[str] = None

    tools: Optional[List[RetellLlmListResponseItemStateTool]] = None


class RetellLlmListResponseItem(BaseModel):
    general_prompt: str
    """General prompt used in every state."""

    begin_message: Optional[str] = None
    """Optional first phrase said by the agent."""

    general_tools: Optional[List[RetellLlmListResponseItemGeneralTool]] = None
    """Optional array of tools used in every state."""

    last_modification_timestamp: Optional[int] = None
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    llm_id: Optional[str] = None
    """Unique id of Retell LLM."""

    starting_state: Optional[str] = None
    """Optional identifier of the starting state."""

    states: Optional[List[RetellLlmListResponseItemState]] = None
    """Optional array of states for the agent."""


RetellLlmListResponse = List[RetellLlmListResponseItem]
