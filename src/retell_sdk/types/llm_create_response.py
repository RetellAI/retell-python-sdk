# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "LlmCreateResponse",
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


class GeneralToolEndCallTool(BaseModel):
    name: str

    type: Literal["end_call"]

    description: Optional[str] = None


class GeneralToolTransferCallTool(BaseModel):
    name: str

    number: str

    type: Literal["transfer_call"]

    description: Optional[str] = None


class GeneralToolFormatDateTimeTool(BaseModel):
    name: str

    type: Literal["parse_relative_date_time"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class GeneralToolCheckAvailabilityCalTool(BaseModel):
    cal_api_key: str

    event_type_id: int

    name: str

    type: Literal["check_availability_cal"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class GeneralToolBookAppointmentCalTool(BaseModel):
    cal_api_key: str

    event_type_id: int

    name: str

    type: Literal["book_appointment_cal"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class GeneralToolCustomToolParameters(BaseModel):
    properties: Dict[str, object]

    type: Literal["object"]

    required: Optional[List[str]] = None


class GeneralToolCustomTool(BaseModel):
    description: str

    name: str

    speak_after_execution: bool

    speak_during_execution: bool

    type: Literal["custom"]

    url: str

    execution_message_description: Optional[str] = None

    parameters: Optional[GeneralToolCustomToolParameters] = None


GeneralTool = Union[
    GeneralToolEndCallTool,
    GeneralToolTransferCallTool,
    GeneralToolFormatDateTimeTool,
    GeneralToolCheckAvailabilityCalTool,
    GeneralToolBookAppointmentCalTool,
    GeneralToolCustomTool,
]


class StateEdgeParameters(BaseModel):
    properties: Dict[str, object]

    type: Literal["object"]

    required: Optional[List[str]] = None


class StateEdge(BaseModel):
    description: str

    destination_state_name: str

    parameters: Optional[StateEdgeParameters] = None

    speak_during_transition: Optional[bool] = None


class StateToolEndCallTool(BaseModel):
    name: str

    type: Literal["end_call"]

    description: Optional[str] = None


class StateToolTransferCallTool(BaseModel):
    name: str

    number: str

    type: Literal["transfer_call"]

    description: Optional[str] = None


class StateToolFormatDateTimeTool(BaseModel):
    name: str

    type: Literal["parse_relative_date_time"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class StateToolCheckAvailabilityCalTool(BaseModel):
    cal_api_key: str

    event_type_id: int

    name: str

    type: Literal["check_availability_cal"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class StateToolBookAppointmentCalTool(BaseModel):
    cal_api_key: str

    event_type_id: int

    name: str

    type: Literal["book_appointment_cal"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class StateToolCustomToolParameters(BaseModel):
    properties: Dict[str, object]

    type: Literal["object"]

    required: Optional[List[str]] = None


class StateToolCustomTool(BaseModel):
    description: str

    name: str

    speak_after_execution: bool

    speak_during_execution: bool

    type: Literal["custom"]

    url: str

    execution_message_description: Optional[str] = None

    parameters: Optional[StateToolCustomToolParameters] = None


StateTool = Union[
    StateToolEndCallTool,
    StateToolTransferCallTool,
    StateToolFormatDateTimeTool,
    StateToolCheckAvailabilityCalTool,
    StateToolBookAppointmentCalTool,
    StateToolCustomTool,
]


class State(BaseModel):
    name: str

    state_prompt: str

    edges: Optional[List[StateEdge]] = None

    tools: Optional[List[StateTool]] = None


class LlmCreateResponse(BaseModel):
    begin_message: Optional[str] = None
    """Optional first phrase said by the agent."""

    general_prompt: Optional[str] = None
    """General prompt used in every state."""

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
    """Optional array of states."""
