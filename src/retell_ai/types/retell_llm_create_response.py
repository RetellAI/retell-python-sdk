# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "RetellLlmCreateResponse",
    "GeneralTool",
    "GeneralToolEndCallTool",
    "GeneralToolTransferCallTool",
    "GeneralToolCustomTool",
    "GeneralToolCustomToolParameters",
    "State",
    "StateEdge",
    "StateEdgeParameters",
    "StateTool",
    "StateToolEndCallTool",
    "StateToolTransferCallTool",
    "StateToolCustomTool",
    "StateToolCustomToolParameters",
]


class GeneralToolEndCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["end_call"]] = None

    type: Optional[Literal["pre_defined"]] = None


class GeneralToolTransferCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["transfer_call"]] = None

    number: Optional[str] = None

    type: Optional[Literal["pre_defined"]] = None


class GeneralToolCustomToolParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class GeneralToolCustomTool(BaseModel):
    description: Optional[str] = None

    execution_message_description: Optional[str] = None

    execution_timing: Optional[Literal["immediate", "await_agent_turn"]] = None

    name: Optional[str] = None

    parameters: Optional[GeneralToolCustomToolParameters] = None

    speak_after_execution: Optional[bool] = None

    speak_during_execution: Optional[bool] = None

    type: Optional[Literal["custom"]] = None

    url: Optional[str] = None


GeneralTool = Union[GeneralToolEndCallTool, GeneralToolTransferCallTool, GeneralToolCustomTool]


class StateEdgeParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class StateEdge(BaseModel):
    description: Optional[str] = None

    destination_state_name: Optional[str] = FieldInfo(alias="destinationStateName", default=None)

    parameters: Optional[StateEdgeParameters] = None

    speak_during_transition: Optional[bool] = FieldInfo(alias="speakDuringTransition", default=None)


class StateToolEndCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["end_call"]] = None

    type: Optional[Literal["pre_defined"]] = None


class StateToolTransferCallTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["transfer_call"]] = None

    number: Optional[str] = None

    type: Optional[Literal["pre_defined"]] = None


class StateToolCustomToolParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class StateToolCustomTool(BaseModel):
    description: Optional[str] = None

    execution_message_description: Optional[str] = None

    execution_timing: Optional[Literal["immediate", "await_agent_turn"]] = None

    name: Optional[str] = None

    parameters: Optional[StateToolCustomToolParameters] = None

    speak_after_execution: Optional[bool] = None

    speak_during_execution: Optional[bool] = None

    type: Optional[Literal["custom"]] = None

    url: Optional[str] = None


StateTool = Union[StateToolEndCallTool, StateToolTransferCallTool, StateToolCustomTool]


class State(BaseModel):
    edges: Optional[List[StateEdge]] = None

    name: Optional[str] = None

    state_prompt: Optional[str] = None

    tools: Optional[List[StateTool]] = None


class RetellLlmCreateResponse(BaseModel):
    general_prompt: str
    """General prompt used in every state."""

    begin_message: Optional[str] = None
    """Optional first phrase said by the agent."""

    general_tools: Optional[List[GeneralTool]] = None
    """Optional array of tools used in every state."""

    last_modification_timestamp: Optional[int] = None
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    llm_id: Optional[str] = None
    """Unique id of Retell LLM."""

    starting_state: Optional[str] = None
    """Optional identifier of the starting state."""

    states: Optional[List[State]] = None
    """Optional array of states for the agent."""
