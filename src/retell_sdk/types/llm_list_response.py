# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "LlmListResponse",
    "LlmListResponseItem",
    "LlmListResponseItemGeneralTool",
    "LlmListResponseItemGeneralToolEndCallTool",
    "LlmListResponseItemGeneralToolTransferCallTool",
    "LlmListResponseItemGeneralToolFormatDateTimeTool",
    "LlmListResponseItemGeneralToolCheckAvailabilityCalTool",
    "LlmListResponseItemGeneralToolBookAppointmentCalTool",
    "LlmListResponseItemGeneralToolCustomTool",
    "LlmListResponseItemGeneralToolCustomToolParameters",
    "LlmListResponseItemState",
    "LlmListResponseItemStateEdge",
    "LlmListResponseItemStateEdgeParameters",
    "LlmListResponseItemStateTool",
    "LlmListResponseItemStateToolEndCallTool",
    "LlmListResponseItemStateToolTransferCallTool",
    "LlmListResponseItemStateToolFormatDateTimeTool",
    "LlmListResponseItemStateToolCheckAvailabilityCalTool",
    "LlmListResponseItemStateToolBookAppointmentCalTool",
    "LlmListResponseItemStateToolCustomTool",
    "LlmListResponseItemStateToolCustomToolParameters",
]


class LlmListResponseItemGeneralToolEndCallTool(BaseModel):
    name: str

    type: Literal["end_call"]

    description: Optional[str] = None


class LlmListResponseItemGeneralToolTransferCallTool(BaseModel):
    name: str

    number: str

    type: Literal["transfer_call"]

    description: Optional[str] = None


class LlmListResponseItemGeneralToolFormatDateTimeTool(BaseModel):
    name: str

    type: Literal["parse_relative_date_time"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class LlmListResponseItemGeneralToolCheckAvailabilityCalTool(BaseModel):
    cal_api_key: str

    event_type_id: int

    name: str

    type: Literal["check_availability_cal"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class LlmListResponseItemGeneralToolBookAppointmentCalTool(BaseModel):
    cal_api_key: str

    event_type_id: int

    name: str

    type: Literal["book_appointment_cal"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class LlmListResponseItemGeneralToolCustomToolParameters(BaseModel):
    properties: Dict[str, object]

    type: Literal["object"]

    required: Optional[List[str]] = None


class LlmListResponseItemGeneralToolCustomTool(BaseModel):
    description: str

    name: str

    speak_after_execution: bool

    speak_during_execution: bool

    type: Literal["custom"]

    url: str

    execution_message_description: Optional[str] = None

    parameters: Optional[LlmListResponseItemGeneralToolCustomToolParameters] = None


LlmListResponseItemGeneralTool = Union[
    LlmListResponseItemGeneralToolEndCallTool,
    LlmListResponseItemGeneralToolTransferCallTool,
    LlmListResponseItemGeneralToolFormatDateTimeTool,
    LlmListResponseItemGeneralToolCheckAvailabilityCalTool,
    LlmListResponseItemGeneralToolBookAppointmentCalTool,
    LlmListResponseItemGeneralToolCustomTool,
]


class LlmListResponseItemStateEdgeParameters(BaseModel):
    properties: Dict[str, object]

    type: Literal["object"]

    required: Optional[List[str]] = None


class LlmListResponseItemStateEdge(BaseModel):
    description: str

    destination_state_name: str

    parameters: Optional[LlmListResponseItemStateEdgeParameters] = None

    speak_during_transition: Optional[bool] = None


class LlmListResponseItemStateToolEndCallTool(BaseModel):
    name: str

    type: Literal["end_call"]

    description: Optional[str] = None


class LlmListResponseItemStateToolTransferCallTool(BaseModel):
    name: str

    number: str

    type: Literal["transfer_call"]

    description: Optional[str] = None


class LlmListResponseItemStateToolFormatDateTimeTool(BaseModel):
    name: str

    type: Literal["parse_relative_date_time"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class LlmListResponseItemStateToolCheckAvailabilityCalTool(BaseModel):
    cal_api_key: str

    event_type_id: int

    name: str

    type: Literal["check_availability_cal"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class LlmListResponseItemStateToolBookAppointmentCalTool(BaseModel):
    cal_api_key: str

    event_type_id: int

    name: str

    type: Literal["book_appointment_cal"]

    description: Optional[str] = None

    timezone: Optional[str] = None


class LlmListResponseItemStateToolCustomToolParameters(BaseModel):
    properties: Dict[str, object]

    type: Literal["object"]

    required: Optional[List[str]] = None


class LlmListResponseItemStateToolCustomTool(BaseModel):
    description: str

    name: str

    speak_after_execution: bool

    speak_during_execution: bool

    type: Literal["custom"]

    url: str

    execution_message_description: Optional[str] = None

    parameters: Optional[LlmListResponseItemStateToolCustomToolParameters] = None


LlmListResponseItemStateTool = Union[
    LlmListResponseItemStateToolEndCallTool,
    LlmListResponseItemStateToolTransferCallTool,
    LlmListResponseItemStateToolFormatDateTimeTool,
    LlmListResponseItemStateToolCheckAvailabilityCalTool,
    LlmListResponseItemStateToolBookAppointmentCalTool,
    LlmListResponseItemStateToolCustomTool,
]


class LlmListResponseItemState(BaseModel):
    name: str

    state_prompt: str

    edges: Optional[List[LlmListResponseItemStateEdge]] = None

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
    """Optional array of states."""


LlmListResponse = List[LlmListResponseItem]
