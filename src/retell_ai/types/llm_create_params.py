# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LlmCreateParams",
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


class LlmCreateParams(TypedDict, total=False):
    begin_message: str
    """Optional first phrase said by the agent."""

    general_prompt: str
    """General prompt used in every state."""

    general_tools: Iterable[GeneralTool]
    """Optional array of tools used in every state."""

    starting_state: str
    """Optional identifier of the starting state."""

    states: Iterable[State]
    """Optional array of states for the agent."""


class GeneralToolEndCallTool(TypedDict, total=False):
    description: Optional[str]

    name: Literal["end_call"]

    type: Literal["pre_defined"]


class GeneralToolTransferCallTool(TypedDict, total=False):
    description: Optional[str]

    name: Literal["transfer_call"]

    number: str

    type: Literal["pre_defined"]


class GeneralToolCustomToolParameters(TypedDict, total=False):
    properties: Dict[str, object]

    required: List[str]

    type: Literal["object"]


class GeneralToolCustomTool(TypedDict, total=False):
    description: str

    execution_message_description: Optional[str]

    execution_timing: Literal["immediate", "await_agent_turn"]

    name: str

    parameters: Optional[GeneralToolCustomToolParameters]

    speak_after_execution: bool

    speak_during_execution: bool

    type: Literal["custom"]

    url: str


GeneralTool = Union[GeneralToolEndCallTool, GeneralToolTransferCallTool, GeneralToolCustomTool]


class StateEdgeParameters(TypedDict, total=False):
    properties: Dict[str, object]

    required: List[str]

    type: Literal["object"]


class StateEdge(TypedDict, total=False):
    description: str

    destination_state_name: Annotated[str, PropertyInfo(alias="destinationStateName")]

    parameters: Optional[StateEdgeParameters]

    speak_during_transition: Annotated[bool, PropertyInfo(alias="speakDuringTransition")]


class StateToolEndCallTool(TypedDict, total=False):
    description: Optional[str]

    name: Literal["end_call"]

    type: Literal["pre_defined"]


class StateToolTransferCallTool(TypedDict, total=False):
    description: Optional[str]

    name: Literal["transfer_call"]

    number: str

    type: Literal["pre_defined"]


class StateToolCustomToolParameters(TypedDict, total=False):
    properties: Dict[str, object]

    required: List[str]

    type: Literal["object"]


class StateToolCustomTool(TypedDict, total=False):
    description: str

    execution_message_description: Optional[str]

    execution_timing: Literal["immediate", "await_agent_turn"]

    name: str

    parameters: Optional[StateToolCustomToolParameters]

    speak_after_execution: bool

    speak_during_execution: bool

    type: Literal["custom"]

    url: str


StateTool = Union[StateToolEndCallTool, StateToolTransferCallTool, StateToolCustomTool]


class State(TypedDict, total=False):
    edges: Optional[Iterable[StateEdge]]

    name: str

    state_prompt: str

    tools: Optional[Iterable[StateTool]]
