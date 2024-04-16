# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "LlmCreateParams",
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


class LlmCreateParams(TypedDict, total=False):
    begin_message: Optional[str]
    """First utterance said by the agent in the call.

    If not set, LLM will dynamically generate a message. If set to "", agent will
    wait for user to speak first.
    """

    general_prompt: Optional[str]
    """General prompt appended to system prompt no matter what state the agent is in.

    - System prompt (with state) = general prompt + state prompt.

    - System prompt (no state) = general prompt.
    """

    general_tools: Optional[Iterable[GeneralTool]]
    """A list of tools the model may call (to get external knowledge, call API, etc).

    You can select from some common predefined tools like end call, transfer call,
    etc; or you can create your own custom tool (last option) for the LLM to use.

    - Tools of LLM (with state) = general tools + state tools + state transitions

    - Tools of LLM (no state) = general tools
    """

    inbound_dynamic_variables_webhook_url: Optional[str]
    """
    For inbound phone calls with Retell numbers, if this webhook is set, will POST
    to it to retrieve dynamic variables to use for the call. Without this, there's
    no way to pass dynamic variables to inbound calls of Retell numbers.
    """

    model: Literal["gpt-3.5-turbo", "gpt-4-turbo"]
    """Select the underlying LLM. If not set, would default to gpt-3.5-turbo."""

    starting_state: Optional[str]
    """Name of the starting state. Required if states is not empty."""

    states: Optional[Iterable[State]]
    """States of the LLM.

    This is to help reduce prompt length and tool choices when the call can be
    broken into distinct states. With shorter prompts and less tools, the LLM can
    better focus and follow the rules, minimizing hallucination. If this field is
    not set, the agent would only have general prompt and general tools (essentially
    one state).
    """


class GeneralToolEndCallTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["end_call"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class GeneralToolTransferCallTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    number: Required[str]
    """
    The number to transfer to in E.164 format (a + and country code, then the phone
    number with no space or other special characters). For example, +16175551212.
    """

    type: Required[Literal["transfer_call"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class GeneralToolCheckAvailabilityCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: Required[float]
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for.
    """

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["check_availability_cal"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    timezone: str
    """
    Timezone to be used when checking availability, must be in
    [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    If not specified, will check if user specified timezone in call, and if not,
    will use the timezone of the Retell servers.
    """


class GeneralToolBookAppointmentCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: Required[float]
    """
    Cal.com event type id number for the cal.com event you want to book appointment.
    """

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["book_appointment_cal"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    timezone: str
    """
    Timezone to be used when booking appointment, must be in
    [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    If not specified, will check if user specified timezone in call, and if not,
    will use the timezone of the Retell servers.
    """


class GeneralToolCustomToolParameters(TypedDict, total=False):
    properties: Required[Dict[str, object]]
    """
    The value of properties is an object, where each key is the name of a property
    and each value is a schema used to validate that property.
    """

    type: Required[Literal["object"]]
    """Type must be "object" for a JSON Schema object."""

    required: List[str]
    """List of names of required property when generating this parameter.

    LLM will do its best to generate the required properties in its function
    arguments. Property must exist in properties.
    """


class GeneralToolCustomTool(TypedDict, total=False):
    description: Required[str]
    """Describes what this tool does and when to call this tool."""

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    speak_after_execution: Required[bool]
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: Required[bool]
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """

    type: Required[Literal["custom"]]

    url: Required[str]
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: str
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    parameters: GeneralToolCustomToolParameters
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


class StateEdgeParameters(TypedDict, total=False):
    properties: Required[Dict[str, object]]
    """
    The value of properties is an object, where each key is the name of a property
    and each value is a schema used to validate that property.
    """

    type: Required[Literal["object"]]
    """Type must be "object" for a JSON Schema object."""

    required: List[str]
    """List of names of required property when generating this parameter.

    LLM will do its best to generate the required properties in its function
    arguments. Property must exist in properties.
    """


class StateEdge(TypedDict, total=False):
    description: Required[str]
    """
    Describes what's the transition and at what time / criteria should this
    transition happen.
    """

    destination_state_name: Required[str]
    """The destination state name when going through transition of state via this edge.

    State transition internally is implemented as a tool call of LLM, and a tool
    call with name "transition*to*{destination_state_name}" will get created. Feel
    free to reference it inside the prompt.
    """

    parameters: StateEdgeParameters
    """Describes what parameters you want to extract out when the transition changes.

    The parameters extracted here can be referenced in prompts & function
    descriptions of later states via dynamic variables. The parameters the functions
    accepts, described as a JSON Schema object. See
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.
    """


class StateToolEndCallTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["end_call"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class StateToolTransferCallTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    number: Required[str]
    """
    The number to transfer to in E.164 format (a + and country code, then the phone
    number with no space or other special characters). For example, +16175551212.
    """

    type: Required[Literal["transfer_call"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class StateToolCheckAvailabilityCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: Required[float]
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for.
    """

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["check_availability_cal"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    timezone: str
    """
    Timezone to be used when checking availability, must be in
    [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    If not specified, will check if user specified timezone in call, and if not,
    will use the timezone of the Retell servers.
    """


class StateToolBookAppointmentCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: Required[float]
    """
    Cal.com event type id number for the cal.com event you want to book appointment.
    """

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["book_appointment_cal"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    timezone: str
    """
    Timezone to be used when booking appointment, must be in
    [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    If not specified, will check if user specified timezone in call, and if not,
    will use the timezone of the Retell servers.
    """


class StateToolCustomToolParameters(TypedDict, total=False):
    properties: Required[Dict[str, object]]
    """
    The value of properties is an object, where each key is the name of a property
    and each value is a schema used to validate that property.
    """

    type: Required[Literal["object"]]
    """Type must be "object" for a JSON Schema object."""

    required: List[str]
    """List of names of required property when generating this parameter.

    LLM will do its best to generate the required properties in its function
    arguments. Property must exist in properties.
    """


class StateToolCustomTool(TypedDict, total=False):
    description: Required[str]
    """Describes what this tool does and when to call this tool."""

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    speak_after_execution: Required[bool]
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: Required[bool]
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """

    type: Required[Literal["custom"]]

    url: Required[str]
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: str
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    parameters: StateToolCustomToolParameters
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


class State(TypedDict, total=False):
    name: Required[str]
    """Name of the state, must be unique for each state.

    Must be consisted of a-z, A-Z, 0-9, or contain underscores and dashes, with a
    maximum length of 64 (no space allowed).
    """

    edges: Iterable[StateEdge]
    """Edges of the state define how and what state can be reached from this state."""

    state_prompt: str
    """Prompt of the state, will be appended to the system prompt of LLM.

    - System prompt = general prompt + state prompt.
    """

    tools: Iterable[StateTool]
    """
    A list of tools specific to this state the model may call (to get external
    knowledge, call API, etc). You can select from some common predefined tools like
    end call, transfer call, etc; or you can create your own custom tool (last
    option) for the LLM to use.

    - Tools of LLM = general tools + state tools + state transitions
    """
