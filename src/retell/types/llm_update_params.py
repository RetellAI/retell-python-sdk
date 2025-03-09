# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "LlmUpdateParams",
    "GeneralTool",
    "GeneralToolEndCallTool",
    "GeneralToolTransferCallTool",
    "GeneralToolTransferCallToolTransferDestination",
    "GeneralToolTransferCallToolTransferDestinationTransferDestinationPredefined",
    "GeneralToolTransferCallToolTransferDestinationTransferDestinationInferred",
    "GeneralToolTransferCallToolWarmTransferOption",
    "GeneralToolTransferCallToolWarmTransferOptionWarmTransferPrompt",
    "GeneralToolTransferCallToolWarmTransferOptionWarmTransferStaticMessage",
    "GeneralToolCheckAvailabilityCalTool",
    "GeneralToolBookAppointmentCalTool",
    "GeneralToolPressDigitTool",
    "GeneralToolCustomTool",
    "GeneralToolCustomToolParameters",
    "State",
    "StateEdge",
    "StateEdgeParameters",
    "StateTool",
    "StateToolEndCallTool",
    "StateToolTransferCallTool",
    "StateToolTransferCallToolTransferDestination",
    "StateToolTransferCallToolTransferDestinationTransferDestinationPredefined",
    "StateToolTransferCallToolTransferDestinationTransferDestinationInferred",
    "StateToolTransferCallToolWarmTransferOption",
    "StateToolTransferCallToolWarmTransferOptionWarmTransferPrompt",
    "StateToolTransferCallToolWarmTransferOptionWarmTransferStaticMessage",
    "StateToolCheckAvailabilityCalTool",
    "StateToolBookAppointmentCalTool",
    "StateToolPressDigitTool",
    "StateToolCustomTool",
    "StateToolCustomToolParameters",
]


class LlmUpdateParams(TypedDict, total=False):
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

    knowledge_base_ids: Optional[List[str]]
    """A list of knowledge base ids to use for this resource.

    Set to null to remove all knowledge bases.
    """

    model: Optional[Literal["gpt-4o", "gpt-4o-mini", "claude-3.7-sonnet", "claude-3.5-haiku"]]
    """Select the underlying text LLM. If not set, would default to gpt-4o."""

    model_high_priority: bool
    """
    If set to true, will use high priority pool with more dedicated resource to
    ensure lower and more consistent latency, default to false. This feature usually
    comes with a higher cost.
    """

    model_temperature: float
    """If set, will control the randomness of the response.

    Value ranging from [0,1]. Lower value means more deterministic, while higher
    value means more random. If unset, default value 0 will apply. Note that for
    tool calling, a lower value is recommended.
    """

    s2s_model: Optional[Literal["gpt-4o-realtime", "gpt-4o-mini-realtime"]]
    """Select the underlying speech to speech model.

    Can only set this or model, not both.
    """

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

    tool_call_strict_mode: bool
    """Only applicable when model is gpt-4o or gpt-4o mini.

    If set to true, will use structured output to make sure tool call arguments
    follow the json schema. The time to save a new tool or change to a tool will be
    longer as additional processing is needed. Default to false.
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


class GeneralToolTransferCallToolTransferDestinationTransferDestinationPredefined(TypedDict, total=False):
    number: Required[str]
    """
    The number to transfer to in E.164 format or a dynamic variable like
    {{transfer_number}}.
    """

    type: Required[Literal["predefined"]]
    """The type of transfer destination."""


class GeneralToolTransferCallToolTransferDestinationTransferDestinationInferred(TypedDict, total=False):
    prompt: Required[str]
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Required[Literal["inferred"]]
    """The type of transfer destination."""


GeneralToolTransferCallToolTransferDestination: TypeAlias = Union[
    GeneralToolTransferCallToolTransferDestinationTransferDestinationPredefined,
    GeneralToolTransferCallToolTransferDestinationTransferDestinationInferred,
]


class GeneralToolTransferCallToolWarmTransferOptionWarmTransferPrompt(TypedDict, total=False):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class GeneralToolTransferCallToolWarmTransferOptionWarmTransferStaticMessage(TypedDict, total=False):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


GeneralToolTransferCallToolWarmTransferOption: TypeAlias = Union[
    GeneralToolTransferCallToolWarmTransferOptionWarmTransferPrompt,
    GeneralToolTransferCallToolWarmTransferOptionWarmTransferStaticMessage,
]


class GeneralToolTransferCallTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    type: Required[Literal["transfer_call"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    number: Optional[str]
    """
    The number to transfer to in E.164 format or a dynamic variable like
    {{transfer_number}}.
    """

    show_transferee_as_caller: Optional[bool]
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support SIP REFER to PSTN. This is
    only applicable for cold transfer, so if warm transfer option is specified, this
    field will be ignored. Default to false (default to show AI agent as caller).
    """

    transfer_destination: GeneralToolTransferCallToolTransferDestination

    warm_transfer_option: Optional[GeneralToolTransferCallToolWarmTransferOption]
    """If set, when transfer is successful, will perform a warm handoff.

    Can leave either a static message or a dynamic one based on prompt. Set to null
    to disable warm handoff.
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


class GeneralToolPressDigitTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["press_digit"]]

    delay_ms: int
    """
    Delay in milliseconds before pressing the digit, because a lot of IVR systems
    speak very slowly, and a delay can make sure the agent hears the full menu.
    Default to 1000 ms (1s). Valid range is 0 to 5000 ms (inclusive).
    """

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
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

    timeout_ms: int
    """The maximum time in milliseconds the tool can run before it's considered
    timeout.

    If the tool times out, the agent would have that info. The minimum value allowed
    is 1000 ms (1 s), and maximum value allowed is 600,000 ms (10 min). By default,
    this is set to 120,000 ms (2 min).
    """


GeneralTool: TypeAlias = Union[
    GeneralToolEndCallTool,
    GeneralToolTransferCallTool,
    GeneralToolCheckAvailabilityCalTool,
    GeneralToolBookAppointmentCalTool,
    GeneralToolPressDigitTool,
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


class StateToolTransferCallToolTransferDestinationTransferDestinationPredefined(TypedDict, total=False):
    number: Required[str]
    """
    The number to transfer to in E.164 format or a dynamic variable like
    {{transfer_number}}.
    """

    type: Required[Literal["predefined"]]
    """The type of transfer destination."""


class StateToolTransferCallToolTransferDestinationTransferDestinationInferred(TypedDict, total=False):
    prompt: Required[str]
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Required[Literal["inferred"]]
    """The type of transfer destination."""


StateToolTransferCallToolTransferDestination: TypeAlias = Union[
    StateToolTransferCallToolTransferDestinationTransferDestinationPredefined,
    StateToolTransferCallToolTransferDestinationTransferDestinationInferred,
]


class StateToolTransferCallToolWarmTransferOptionWarmTransferPrompt(TypedDict, total=False):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class StateToolTransferCallToolWarmTransferOptionWarmTransferStaticMessage(TypedDict, total=False):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


StateToolTransferCallToolWarmTransferOption: TypeAlias = Union[
    StateToolTransferCallToolWarmTransferOptionWarmTransferPrompt,
    StateToolTransferCallToolWarmTransferOptionWarmTransferStaticMessage,
]


class StateToolTransferCallTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    type: Required[Literal["transfer_call"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    number: Optional[str]
    """
    The number to transfer to in E.164 format or a dynamic variable like
    {{transfer_number}}.
    """

    show_transferee_as_caller: Optional[bool]
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support SIP REFER to PSTN. This is
    only applicable for cold transfer, so if warm transfer option is specified, this
    field will be ignored. Default to false (default to show AI agent as caller).
    """

    transfer_destination: StateToolTransferCallToolTransferDestination

    warm_transfer_option: Optional[StateToolTransferCallToolWarmTransferOption]
    """If set, when transfer is successful, will perform a warm handoff.

    Can leave either a static message or a dynamic one based on prompt. Set to null
    to disable warm handoff.
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


class StateToolPressDigitTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["press_digit"]]

    delay_ms: int
    """
    Delay in milliseconds before pressing the digit, because a lot of IVR systems
    speak very slowly, and a delay can make sure the agent hears the full menu.
    Default to 1000 ms (1s). Valid range is 0 to 5000 ms (inclusive).
    """

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
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

    timeout_ms: int
    """The maximum time in milliseconds the tool can run before it's considered
    timeout.

    If the tool times out, the agent would have that info. The minimum value allowed
    is 1000 ms (1 s), and maximum value allowed is 600,000 ms (10 min). By default,
    this is set to 120,000 ms (2 min).
    """


StateTool: TypeAlias = Union[
    StateToolEndCallTool,
    StateToolTransferCallTool,
    StateToolCheckAvailabilityCalTool,
    StateToolBookAppointmentCalTool,
    StateToolPressDigitTool,
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
