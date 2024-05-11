# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "LlmResponse",
    "GeneralTool",
    "GeneralToolEndCallTool",
    "GeneralToolTransferCallTool",
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
    "StateToolCheckAvailabilityCalTool",
    "StateToolBookAppointmentCalTool",
    "StateToolCustomTool",
    "StateToolCustomToolParameters",
]


class GeneralToolEndCallTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["end_call"]

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class GeneralToolTransferCallTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    number: str
    """
    The number to transfer to in E.164 format (a + and country code, then the phone
    number with no space or other special characters). For example, +16175551212.
    """

    type: Literal["transfer_call"]

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class GeneralToolCheckAvailabilityCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: float
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for.
    """

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["check_availability_cal"]

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    timezone: Optional[str] = None
    """
    Timezone to be used when checking availability, must be in
    [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    If not specified, will check if user specified timezone in call, and if not,
    will use the timezone of the Retell servers.
    """


class GeneralToolBookAppointmentCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: float
    """
    Cal.com event type id number for the cal.com event you want to book appointment.
    """

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["book_appointment_cal"]

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    timezone: Optional[str] = None
    """
    Timezone to be used when booking appointment, must be in
    [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    If not specified, will check if user specified timezone in call, and if not,
    will use the timezone of the Retell servers.
    """


class GeneralToolCustomToolParameters(BaseModel):
    properties: Dict[str, object]
    """
    The value of properties is an object, where each key is the name of a property
    and each value is a schema used to validate that property.
    """

    type: Literal["object"]
    """Type must be "object" for a JSON Schema object."""

    required: Optional[List[str]] = None
    """List of names of required property when generating this parameter.

    LLM will do its best to generate the required properties in its function
    arguments. Property must exist in properties.
    """


class GeneralToolCustomTool(BaseModel):
    description: str
    """Describes what this tool does and when to call this tool."""

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    speak_after_execution: bool
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: bool
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """

    type: Literal["custom"]

    url: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: Optional[str] = None
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    parameters: Optional[GeneralToolCustomToolParameters] = None
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format. Omitting parameters defines a function with
    an empty parameter list.
    """


GeneralTool = Union[
    GeneralToolEndCallTool,
    GeneralToolTransferCallTool,
    GeneralToolCheckAvailabilityCalTool,
    GeneralToolBookAppointmentCalTool,
    GeneralToolCustomTool,
]


class StateEdgeParameters(BaseModel):
    properties: Dict[str, object]
    """
    The value of properties is an object, where each key is the name of a property
    and each value is a schema used to validate that property.
    """

    type: Literal["object"]
    """Type must be "object" for a JSON Schema object."""

    required: Optional[List[str]] = None
    """List of names of required property when generating this parameter.

    LLM will do its best to generate the required properties in its function
    arguments. Property must exist in properties.
    """


class StateEdge(BaseModel):
    description: str
    """
    Describes what's the transition and at what time / criteria should this
    transition happen.
    """

    destination_state_name: str
    """The destination state name when going through transition of state via this edge.

    State transition internally is implemented as a tool call of LLM, and a tool
    call with name "transition*to*{destination_state_name}" will get created. Feel
    free to reference it inside the prompt.
    """

    parameters: Optional[StateEdgeParameters] = None
    """Describes what parameters you want to extract out when the transition changes.

    The parameters extracted here can be referenced in prompts & function
    descriptions of later states via dynamic variables. The parameters the functions
    accepts, described as a JSON Schema object. See
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.
    """


class StateToolEndCallTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["end_call"]

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class StateToolTransferCallTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    number: str
    """
    The number to transfer to in E.164 format (a + and country code, then the phone
    number with no space or other special characters). For example, +16175551212.
    """

    type: Literal["transfer_call"]

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class StateToolCheckAvailabilityCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: float
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for.
    """

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["check_availability_cal"]

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    timezone: Optional[str] = None
    """
    Timezone to be used when checking availability, must be in
    [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    If not specified, will check if user specified timezone in call, and if not,
    will use the timezone of the Retell servers.
    """


class StateToolBookAppointmentCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: float
    """
    Cal.com event type id number for the cal.com event you want to book appointment.
    """

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["book_appointment_cal"]

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    timezone: Optional[str] = None
    """
    Timezone to be used when booking appointment, must be in
    [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    If not specified, will check if user specified timezone in call, and if not,
    will use the timezone of the Retell servers.
    """


class StateToolCustomToolParameters(BaseModel):
    properties: Dict[str, object]
    """
    The value of properties is an object, where each key is the name of a property
    and each value is a schema used to validate that property.
    """

    type: Literal["object"]
    """Type must be "object" for a JSON Schema object."""

    required: Optional[List[str]] = None
    """List of names of required property when generating this parameter.

    LLM will do its best to generate the required properties in its function
    arguments. Property must exist in properties.
    """


class StateToolCustomTool(BaseModel):
    description: str
    """Describes what this tool does and when to call this tool."""

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    speak_after_execution: bool
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: bool
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """

    type: Literal["custom"]

    url: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: Optional[str] = None
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    parameters: Optional[StateToolCustomToolParameters] = None
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format. Omitting parameters defines a function with
    an empty parameter list.
    """


StateTool = Union[
    StateToolEndCallTool,
    StateToolTransferCallTool,
    StateToolCheckAvailabilityCalTool,
    StateToolBookAppointmentCalTool,
    StateToolCustomTool,
]


class State(BaseModel):
    name: str
    """Name of the state, must be unique for each state.

    Must be consisted of a-z, A-Z, 0-9, or contain underscores and dashes, with a
    maximum length of 64 (no space allowed).
    """

    edges: Optional[List[StateEdge]] = None
    """Edges of the state define how and what state can be reached from this state."""

    state_prompt: Optional[str] = None
    """Prompt of the state, will be appended to the system prompt of LLM.

    - System prompt = general prompt + state prompt.
    """

    tools: Optional[List[StateTool]] = None
    """
    A list of tools specific to this state the model may call (to get external
    knowledge, call API, etc). You can select from some common predefined tools like
    end call, transfer call, etc; or you can create your own custom tool (last
    option) for the LLM to use.

    - Tools of LLM = general tools + state tools + state transitions
    """


class LlmResponse(BaseModel):
    last_modification_timestamp: int
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    llm_id: str
    """Unique id of Retell LLM."""

    llm_websocket_url: str
    """The LLM Websocket URL constructed from unique id of Retell LLM.

    Used in agent API to create / update agent.
    """

    begin_message: Optional[str] = None
    """First utterance said by the agent in the call.

    If not set, LLM will dynamically generate a message. If set to "", agent will
    wait for user to speak first.
    """

    general_prompt: Optional[str] = None
    """General prompt appended to system prompt no matter what state the agent is in.

    - System prompt (with state) = general prompt + state prompt.

    - System prompt (no state) = general prompt.
    """

    general_tools: Optional[List[GeneralTool]] = None
    """A list of tools the model may call (to get external knowledge, call API, etc).

    You can select from some common predefined tools like end call, transfer call,
    etc; or you can create your own custom tool (last option) for the LLM to use.

    - Tools of LLM (with state) = general tools + state tools + state transitions

    - Tools of LLM (no state) = general tools
    """

    inbound_dynamic_variables_webhook_url: Optional[str] = None
    """
    For inbound phone calls with Retell numbers, if this webhook is set, will POST
    to it to retrieve dynamic variables to use for the call. Without this, there's
    no way to pass dynamic variables to inbound calls of Retell numbers.
    """

    model: Optional[Literal["gpt-3.5-turbo", "gpt-4-turbo", "claude-3-sonnet", "claude-3-haiku"]] = None
    """Select the underlying LLM. If not set, would default to gpt-3.5-turbo."""

    starting_state: Optional[str] = None
    """Name of the starting state. Required if states is not empty."""

    states: Optional[List[State]] = None
    """States of the LLM.

    This is to help reduce prompt length and tool choices when the call can be
    broken into distinct states. With shorter prompts and less tools, the LLM can
    better focus and follow the rules, minimizing hallucination. If this field is
    not set, the agent would only have general prompt and general tools (essentially
    one state).
    """
