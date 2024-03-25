# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "LlmCreateParams",
    "GeneralTool",
    "GeneralToolEndCallTool",
    "GeneralToolTransferCallTool",
    "GeneralToolFormatDateTimeTool",
    "GeneralToolCheckAvailabilityCalTool",
    "GeneralToolBookAppointmentCalTool",
    "GeneralToolCustomTool",
    "GeneralToolCustomToolParameters",
    "State",
    "StateEdge",
    "StateEdgeParameters",
    "StateTool",
    "StateToolEndCallTool",
    "StateToolTransferCallTool",
    "StateToolFormatDateTimeTool",
    "StateToolCheckAvailabilityCalTool",
    "StateToolBookAppointmentCalTool",
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
    """Optional array of states."""


class GeneralToolEndCallTool(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["end_call"]]

    description: str


class GeneralToolTransferCallTool(TypedDict, total=False):
    name: Required[str]

    number: Required[str]

    type: Required[Literal["transfer_call"]]

    description: str


class GeneralToolFormatDateTimeTool(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["parse_relative_date_time"]]

    description: str

    timezone: str


class GeneralToolCheckAvailabilityCalTool(TypedDict, total=False):
    cal_api_key: Required[str]

    event_type_id: Required[int]

    name: Required[str]

    type: Required[Literal["check_availability_cal"]]

    description: str

    timezone: str


class GeneralToolBookAppointmentCalTool(TypedDict, total=False):
    cal_api_key: Required[str]

    event_type_id: Required[int]

    name: Required[str]

    type: Required[Literal["book_appointment_cal"]]

    description: str

    timezone: str


class GeneralToolCustomToolParameters(TypedDict, total=False):
    properties: Required[Dict[str, object]]

    type: Required[Literal["object"]]

    required: List[str]


class GeneralToolCustomTool(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    speak_after_execution: Required[bool]

    speak_during_execution: Required[bool]

    type: Required[Literal["custom"]]

    url: Required[str]

    execution_message_description: str

    parameters: GeneralToolCustomToolParameters


GeneralTool = Union[
    GeneralToolEndCallTool,
    GeneralToolTransferCallTool,
    GeneralToolFormatDateTimeTool,
    GeneralToolCheckAvailabilityCalTool,
    GeneralToolBookAppointmentCalTool,
    GeneralToolCustomTool,
]


class StateEdgeParameters(TypedDict, total=False):
    properties: Required[Dict[str, object]]

    type: Required[Literal["object"]]

    required: List[str]


class StateEdge(TypedDict, total=False):
    description: Required[str]

    destination_state_name: Required[str]

    parameters: StateEdgeParameters

    speak_during_transition: bool


class StateToolEndCallTool(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["end_call"]]

    description: str


class StateToolTransferCallTool(TypedDict, total=False):
    name: Required[str]

    number: Required[str]

    type: Required[Literal["transfer_call"]]

    description: str


class StateToolFormatDateTimeTool(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["parse_relative_date_time"]]

    description: str

    timezone: str


class StateToolCheckAvailabilityCalTool(TypedDict, total=False):
    cal_api_key: Required[str]

    event_type_id: Required[int]

    name: Required[str]

    type: Required[Literal["check_availability_cal"]]

    description: str

    timezone: str


class StateToolBookAppointmentCalTool(TypedDict, total=False):
    cal_api_key: Required[str]

    event_type_id: Required[int]

    name: Required[str]

    type: Required[Literal["book_appointment_cal"]]

    description: str

    timezone: str


class StateToolCustomToolParameters(TypedDict, total=False):
    properties: Required[Dict[str, object]]

    type: Required[Literal["object"]]

    required: List[str]


class StateToolCustomTool(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    speak_after_execution: Required[bool]

    speak_during_execution: Required[bool]

    type: Required[Literal["custom"]]

    url: Required[str]

    execution_message_description: str

    parameters: StateToolCustomToolParameters


StateTool = Union[
    StateToolEndCallTool,
    StateToolTransferCallTool,
    StateToolFormatDateTimeTool,
    StateToolCheckAvailabilityCalTool,
    StateToolBookAppointmentCalTool,
    StateToolCustomTool,
]


class State(TypedDict, total=False):
    name: Required[str]

    state_prompt: Required[str]

    edges: Iterable[StateEdge]

    tools: Iterable[StateTool]
