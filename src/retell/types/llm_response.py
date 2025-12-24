# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "LlmResponse",
    "GeneralTool",
    "GeneralToolEndCallTool",
    "GeneralToolTransferCallTool",
    "GeneralToolTransferCallToolTransferDestination",
    "GeneralToolTransferCallToolTransferDestinationTransferDestinationPredefined",
    "GeneralToolTransferCallToolTransferDestinationTransferDestinationInferred",
    "GeneralToolTransferCallToolTransferOption",
    "GeneralToolTransferCallToolTransferOptionTransferOptionColdTransfer",
    "GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransfer",
    "GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption",
    "GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption",
    "GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt",
    "GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage",
    "GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption",
    "GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer",
    "GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig",
    "GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent",
    "GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption",
    "GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "GeneralToolCheckAvailabilityCalTool",
    "GeneralToolBookAppointmentCalTool",
    "GeneralToolAgentSwapTool",
    "GeneralToolPressDigitTool",
    "GeneralToolSendSMSTool",
    "GeneralToolSendSMSToolSMSContent",
    "GeneralToolSendSMSToolSMSContentSMSContentPredefined",
    "GeneralToolSendSMSToolSMSContentSMSContentInferred",
    "GeneralToolCustomTool",
    "GeneralToolCustomToolParameters",
    "GeneralToolExtractDynamicVariableTool",
    "GeneralToolExtractDynamicVariableToolVariable",
    "GeneralToolExtractDynamicVariableToolVariableStringAnalysisData",
    "GeneralToolExtractDynamicVariableToolVariableEnumAnalysisData",
    "GeneralToolExtractDynamicVariableToolVariableBooleanAnalysisData",
    "GeneralToolExtractDynamicVariableToolVariableNumberAnalysisData",
    "GeneralToolBridgeTransferTool",
    "GeneralToolCancelTransferTool",
    "GeneralToolMcpTool",
    "KBConfig",
    "Mcp",
    "State",
    "StateEdge",
    "StateEdgeParameters",
    "StateTool",
    "StateToolEndCallTool",
    "StateToolTransferCallTool",
    "StateToolTransferCallToolTransferDestination",
    "StateToolTransferCallToolTransferDestinationTransferDestinationPredefined",
    "StateToolTransferCallToolTransferDestinationTransferDestinationInferred",
    "StateToolTransferCallToolTransferOption",
    "StateToolTransferCallToolTransferOptionTransferOptionColdTransfer",
    "StateToolTransferCallToolTransferOptionTransferOptionWarmTransfer",
    "StateToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption",
    "StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption",
    "StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt",
    "StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage",
    "StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption",
    "StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer",
    "StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig",
    "StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent",
    "StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption",
    "StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "StateToolCheckAvailabilityCalTool",
    "StateToolBookAppointmentCalTool",
    "StateToolAgentSwapTool",
    "StateToolPressDigitTool",
    "StateToolSendSMSTool",
    "StateToolSendSMSToolSMSContent",
    "StateToolSendSMSToolSMSContentSMSContentPredefined",
    "StateToolSendSMSToolSMSContentSMSContentInferred",
    "StateToolCustomTool",
    "StateToolCustomToolParameters",
    "StateToolExtractDynamicVariableTool",
    "StateToolExtractDynamicVariableToolVariable",
    "StateToolExtractDynamicVariableToolVariableStringAnalysisData",
    "StateToolExtractDynamicVariableToolVariableEnumAnalysisData",
    "StateToolExtractDynamicVariableToolVariableBooleanAnalysisData",
    "StateToolExtractDynamicVariableToolVariableNumberAnalysisData",
    "StateToolBridgeTransferTool",
    "StateToolCancelTransferTool",
    "StateToolMcpTool",
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

    execution_message_description: Optional[str] = None
    """Describes what to say to user when ending the call.

    Only applicable when speak_during_execution is true.
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


class GeneralToolTransferCallToolTransferDestinationTransferDestinationPredefined(BaseModel):
    number: str
    """
    The number to transfer to in E.164 format or a dynamic variable like
    {{transfer_number}}.
    """

    type: Literal["predefined"]
    """The type of transfer destination."""

    extension: Optional[str] = None
    """Extension digits to dial after the main number connects.

    Sent via DTMF. Allow digits, '\\**', '#', or a dynamic variable like
    {{extension}}.
    """


class GeneralToolTransferCallToolTransferDestinationTransferDestinationInferred(BaseModel):
    prompt: str
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Literal["inferred"]
    """The type of transfer destination."""


GeneralToolTransferCallToolTransferDestination: TypeAlias = Union[
    GeneralToolTransferCallToolTransferDestinationTransferDestinationPredefined,
    GeneralToolTransferCallToolTransferDestinationTransferDestinationInferred,
]


class GeneralToolTransferCallToolTransferOptionTransferOptionColdTransfer(BaseModel):
    type: Literal["cold_transfer"]
    """The type of the transfer."""

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


class GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption(BaseModel):
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption: TypeAlias = Union[
    GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt,
    GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage,
]


class GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption: TypeAlias = Union[
    GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt,
    GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransfer(BaseModel):
    type: Literal["warm_transfer"]
    """The type of the transfer."""

    agent_detection_timeout_ms: Optional[float] = None
    """The time to wait before considering transfer fails."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    ivr_option: Optional[GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption] = None
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    on_hold_music: Optional[Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]] = None
    """The music to play while the caller is being transferred."""

    opt_out_human_detection: Optional[bool] = None
    """If set to true, will not perform human detection for the transfer.

    Default to false.
    """

    opt_out_initial_message: Optional[bool] = None
    """If set to true, AI will not say "Hello" after connecting the call.

    Default to false.
    """

    private_handoff_option: Optional[
        GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption
    ] = None
    """
    If set, when transfer is connected, will say the handoff message only to the
    agent receiving the transfer. Can leave either a static message or a dynamic one
    based on prompt. Set to null to disable warm handoff.
    """

    public_handoff_option: Optional[
        GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption
    ] = None
    """
    If set, when transfer is successful, will say the handoff message to both the
    transferee and the agent receiving the transfer. Can leave either a static
    message or a dynamic one based on prompt. Set to null to disable warm handoff.
    """

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


class GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent(
    BaseModel
):
    """The agent that will mediate the transfer decision."""

    agent_id: str
    """The agent ID of the transfer agent.

    This agent must have isTransferAgent set to true and should use bridge_transfer
    and cancel_transfer tools (for Retell LLM) or BridgeTransferNode and
    CancelTransferNode (for Conversation Flow).
    """

    agent_version: float
    """The version of the transfer agent to use."""


class GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig(BaseModel):
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    action_on_timeout: Optional[Literal["bridge_transfer", "cancel_transfer"]] = None
    """The action to take when the transfer agent times out without making a decision.

    Defaults to cancel_transfer.
    """

    transfer_agent: Optional[
        GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent
    ] = None
    """The agent that will mediate the transfer decision."""

    transfer_timeout_ms: Optional[float] = None
    """
    The maximum time to wait for the transfer agent to make a decision, in
    milliseconds. Defaults to 30000 (30 seconds).
    """


class GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption: TypeAlias = Union[
    GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt,
    GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer(BaseModel):
    agentic_transfer_config: (
        GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig
    )
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    type: Literal["agentic_warm_transfer"]
    """The type of the transfer."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    on_hold_music: Optional[Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]] = None
    """The music to play while the caller is being transferred."""

    public_handoff_option: Optional[
        GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption
    ] = None
    """
    If set, when transfer is successful, will say the handoff message to both the
    transferee and the agent receiving the transfer. Can leave either a static
    message or a dynamic one based on prompt. Set to null to disable warm handoff.
    """

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


GeneralToolTransferCallToolTransferOption: TypeAlias = Union[
    GeneralToolTransferCallToolTransferOptionTransferOptionColdTransfer,
    GeneralToolTransferCallToolTransferOptionTransferOptionWarmTransfer,
    GeneralToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer,
]


class GeneralToolTransferCallTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    transfer_destination: GeneralToolTransferCallToolTransferDestination

    transfer_option: GeneralToolTransferCallToolTransferOption

    type: Literal["transfer_call"]

    custom_sip_headers: Optional[Dict[str, str]] = None
    """Custom SIP headers to be added to the call."""

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: Optional[str] = None
    """Describes what to say to user when transferring the call.

    Only applicable when speak_during_execution is true.
    """

    ignore_e164_validation: Optional[bool] = None
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


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


class GeneralToolAgentSwapTool(BaseModel):
    agent_id: str
    """The id of the agent to swap to."""

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    post_call_analysis_setting: Literal["both_agents", "only_destination_agent"]
    """Post call analysis setting for the agent swap."""

    type: Literal["agent_swap"]

    agent_version: Optional[float] = None
    """The version of the agent to swap to.

    If not specified, will use the latest version.
    """

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: Optional[str] = None
    """The message for the agent to speak when executing agent swap."""

    speak_during_execution: Optional[bool] = None

    webhook_setting: Optional[Literal["both_agents", "only_destination_agent", "only_source_agent"]] = None
    """Webhook setting for the agent swap, defaults to only source."""


class GeneralToolPressDigitTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["press_digit"]

    delay_ms: Optional[int] = None
    """
    Delay in milliseconds before pressing the digit, because a lot of IVR systems
    speak very slowly, and a delay can make sure the agent hears the full menu.
    Default to 1000 ms (1s). Valid range is 0 to 5000 ms (inclusive).
    """

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class GeneralToolSendSMSToolSMSContentSMSContentPredefined(BaseModel):
    content: Optional[str] = None
    """The static message to be sent in the SMS. Can contain dynamic variables."""

    type: Optional[Literal["predefined"]] = None


class GeneralToolSendSMSToolSMSContentSMSContentInferred(BaseModel):
    prompt: Optional[str] = None
    """The prompt to be used to help infer the SMS content.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right message to send. Can contain dynamic variables.
    """

    type: Optional[Literal["inferred"]] = None


GeneralToolSendSMSToolSMSContent: TypeAlias = Union[
    GeneralToolSendSMSToolSMSContentSMSContentPredefined, GeneralToolSendSMSToolSMSContentSMSContentInferred
]


class GeneralToolSendSMSTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    sms_content: GeneralToolSendSMSToolSMSContent

    type: Literal["send_sms"]

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class GeneralToolCustomToolParameters(BaseModel):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

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

    type: Literal["custom"]

    url: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    args_at_root: Optional[bool] = None
    """
    If set to true, the parameters will be passed as root level JSON object instead
    of nested under "args".
    """

    execution_message_description: Optional[str] = None
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    headers: Optional[Dict[str, str]] = None
    """Headers to add to the request."""

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None
    """Method to use for the request, default to POST."""

    parameters: Optional[GeneralToolCustomToolParameters] = None
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format. Omitting parameters defines a function with
    an empty parameter list.
    """

    query_params: Optional[Dict[str, str]] = None
    """Query parameters to append to the request URL."""

    response_variables: Optional[Dict[str, str]] = None
    """A mapping of variable names to JSON paths in the response body.

    These values will be extracted from the response and made available as dynamic
    variables for use.
    """

    speak_during_execution: Optional[bool] = None
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """

    timeout_ms: Optional[int] = None
    """The maximum time in milliseconds the tool can run before it's considered
    timeout.

    If the tool times out, the agent would have that info. The minimum value allowed
    is 1000 ms (1 s), and maximum value allowed is 600,000 ms (10 min). By default,
    this is set to 120,000 ms (2 min).
    """


class GeneralToolExtractDynamicVariableToolVariableStringAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["string"]
    """Type of the variable to extract."""

    examples: Optional[List[str]] = None
    """Examples of the variable value to teach model the style and syntax."""


class GeneralToolExtractDynamicVariableToolVariableEnumAnalysisData(BaseModel):
    choices: List[str]
    """The possible values of the variable, must be non empty array."""

    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["enum"]
    """Type of the variable to extract."""


class GeneralToolExtractDynamicVariableToolVariableBooleanAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["boolean"]
    """Type of the variable to extract."""


class GeneralToolExtractDynamicVariableToolVariableNumberAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["number"]
    """Type of the variable to extract."""


GeneralToolExtractDynamicVariableToolVariable: TypeAlias = Union[
    GeneralToolExtractDynamicVariableToolVariableStringAnalysisData,
    GeneralToolExtractDynamicVariableToolVariableEnumAnalysisData,
    GeneralToolExtractDynamicVariableToolVariableBooleanAnalysisData,
    GeneralToolExtractDynamicVariableToolVariableNumberAnalysisData,
]


class GeneralToolExtractDynamicVariableTool(BaseModel):
    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["extract_dynamic_variable"]

    variables: List[GeneralToolExtractDynamicVariableToolVariable]
    """The variables to be extracted."""


class GeneralToolBridgeTransferTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["bridge_transfer"]

    description: Optional[str] = None
    """Describes what the tool does.

    This tool is only available to transfer agents (agents with isTransferAgent set
    to true) in agentic warm transfer mode. When invoked, it bridges the original
    caller to the transfer target and ends the transfer agent call.
    """


class GeneralToolCancelTransferTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["cancel_transfer"]

    description: Optional[str] = None
    """Describes what the tool does.

    This tool is only available to transfer agents (agents with isTransferAgent set
    to true) in agentic warm transfer mode. When invoked, it cancels the transfer,
    returns the original caller to the main agent, and ends the transfer agent call.
    """


class GeneralToolMcpTool(BaseModel):
    description: str
    """Description of the MCP tool."""

    name: str
    """Name of the MCP tool."""

    type: Literal["mcp"]

    execution_message_description: Optional[str] = None
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    input_schema: Optional[Dict[str, str]] = None
    """The input schema of the MCP tool."""

    mcp_id: Optional[str] = None
    """Unique id of the MCP."""

    response_variables: Optional[Dict[str, str]] = None
    """
    Response variables to add to dynamic variables, key is the variable name, value
    is the path to the variable in the response
    """

    speak_after_execution: Optional[bool] = None
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: Optional[bool] = None
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """


GeneralTool: TypeAlias = Union[
    GeneralToolEndCallTool,
    GeneralToolTransferCallTool,
    GeneralToolCheckAvailabilityCalTool,
    GeneralToolBookAppointmentCalTool,
    GeneralToolAgentSwapTool,
    GeneralToolPressDigitTool,
    GeneralToolSendSMSTool,
    GeneralToolCustomTool,
    GeneralToolExtractDynamicVariableTool,
    GeneralToolBridgeTransferTool,
    GeneralToolCancelTransferTool,
    GeneralToolMcpTool,
]


class KBConfig(BaseModel):
    """Knowledge base configuration for RAG retrieval."""

    filter_score: Optional[float] = None
    """Similarity threshold for filtering search results"""

    top_k: Optional[int] = None
    """Max number of knowledge base chunks to retrieve"""


class Mcp(BaseModel):
    name: str

    url: str
    """The URL of the MCP server."""

    headers: Optional[Dict[str, str]] = None
    """Headers to add to the MCP connection request."""

    query_params: Optional[Dict[str, str]] = None
    """Query parameters to append to the MCP connection request URL."""

    timeout_ms: Optional[int] = None
    """Maximum time to wait for a connection to be established (in milliseconds).

    Default to 120,000 ms (2 minutes).
    """


class StateEdgeParameters(BaseModel):
    """Describes what parameters you want to extract out when the transition changes.

    The parameters extracted here can be referenced in prompts & function descriptions of later states via dynamic variables. The parameters the functions accepts, described as a JSON Schema object. See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.
    """

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

    execution_message_description: Optional[str] = None
    """Describes what to say to user when ending the call.

    Only applicable when speak_during_execution is true.
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


class StateToolTransferCallToolTransferDestinationTransferDestinationPredefined(BaseModel):
    number: str
    """
    The number to transfer to in E.164 format or a dynamic variable like
    {{transfer_number}}.
    """

    type: Literal["predefined"]
    """The type of transfer destination."""

    extension: Optional[str] = None
    """Extension digits to dial after the main number connects.

    Sent via DTMF. Allow digits, '\\**', '#', or a dynamic variable like
    {{extension}}.
    """


class StateToolTransferCallToolTransferDestinationTransferDestinationInferred(BaseModel):
    prompt: str
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Literal["inferred"]
    """The type of transfer destination."""


StateToolTransferCallToolTransferDestination: TypeAlias = Union[
    StateToolTransferCallToolTransferDestinationTransferDestinationPredefined,
    StateToolTransferCallToolTransferDestinationTransferDestinationInferred,
]


class StateToolTransferCallToolTransferOptionTransferOptionColdTransfer(BaseModel):
    type: Literal["cold_transfer"]
    """The type of the transfer."""

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


class StateToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption(BaseModel):
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption: TypeAlias = Union[
    StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt,
    StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage,
]


class StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt(BaseModel):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption: TypeAlias = Union[
    StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt,
    StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class StateToolTransferCallToolTransferOptionTransferOptionWarmTransfer(BaseModel):
    type: Literal["warm_transfer"]
    """The type of the transfer."""

    agent_detection_timeout_ms: Optional[float] = None
    """The time to wait before considering transfer fails."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    ivr_option: Optional[StateToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption] = None
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    on_hold_music: Optional[Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]] = None
    """The music to play while the caller is being transferred."""

    opt_out_human_detection: Optional[bool] = None
    """If set to true, will not perform human detection for the transfer.

    Default to false.
    """

    opt_out_initial_message: Optional[bool] = None
    """If set to true, AI will not say "Hello" after connecting the call.

    Default to false.
    """

    private_handoff_option: Optional[
        StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption
    ] = None
    """
    If set, when transfer is connected, will say the handoff message only to the
    agent receiving the transfer. Can leave either a static message or a dynamic one
    based on prompt. Set to null to disable warm handoff.
    """

    public_handoff_option: Optional[
        StateToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption
    ] = None
    """
    If set, when transfer is successful, will say the handoff message to both the
    transferee and the agent receiving the transfer. Can leave either a static
    message or a dynamic one based on prompt. Set to null to disable warm handoff.
    """

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


class StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent(
    BaseModel
):
    """The agent that will mediate the transfer decision."""

    agent_id: str
    """The agent ID of the transfer agent.

    This agent must have isTransferAgent set to true and should use bridge_transfer
    and cancel_transfer tools (for Retell LLM) or BridgeTransferNode and
    CancelTransferNode (for Conversation Flow).
    """

    agent_version: float
    """The version of the transfer agent to use."""


class StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig(BaseModel):
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    action_on_timeout: Optional[Literal["bridge_transfer", "cancel_transfer"]] = None
    """The action to take when the transfer agent times out without making a decision.

    Defaults to cancel_transfer.
    """

    transfer_agent: Optional[
        StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent
    ] = None
    """The agent that will mediate the transfer decision."""

    transfer_timeout_ms: Optional[float] = None
    """
    The maximum time to wait for the transfer agent to make a decision, in
    milliseconds. Defaults to 30000 (30 seconds).
    """


class StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption: TypeAlias = Union[
    StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt,
    StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer(BaseModel):
    agentic_transfer_config: (
        StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig
    )
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    type: Literal["agentic_warm_transfer"]
    """The type of the transfer."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    on_hold_music: Optional[Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]] = None
    """The music to play while the caller is being transferred."""

    public_handoff_option: Optional[
        StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption
    ] = None
    """
    If set, when transfer is successful, will say the handoff message to both the
    transferee and the agent receiving the transfer. Can leave either a static
    message or a dynamic one based on prompt. Set to null to disable warm handoff.
    """

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


StateToolTransferCallToolTransferOption: TypeAlias = Union[
    StateToolTransferCallToolTransferOptionTransferOptionColdTransfer,
    StateToolTransferCallToolTransferOptionTransferOptionWarmTransfer,
    StateToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer,
]


class StateToolTransferCallTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    transfer_destination: StateToolTransferCallToolTransferDestination

    transfer_option: StateToolTransferCallToolTransferOption

    type: Literal["transfer_call"]

    custom_sip_headers: Optional[Dict[str, str]] = None
    """Custom SIP headers to be added to the call."""

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: Optional[str] = None
    """Describes what to say to user when transferring the call.

    Only applicable when speak_during_execution is true.
    """

    ignore_e164_validation: Optional[bool] = None
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


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


class StateToolAgentSwapTool(BaseModel):
    agent_id: str
    """The id of the agent to swap to."""

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    post_call_analysis_setting: Literal["both_agents", "only_destination_agent"]
    """Post call analysis setting for the agent swap."""

    type: Literal["agent_swap"]

    agent_version: Optional[float] = None
    """The version of the agent to swap to.

    If not specified, will use the latest version.
    """

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: Optional[str] = None
    """The message for the agent to speak when executing agent swap."""

    speak_during_execution: Optional[bool] = None

    webhook_setting: Optional[Literal["both_agents", "only_destination_agent", "only_source_agent"]] = None
    """Webhook setting for the agent swap, defaults to only source."""


class StateToolPressDigitTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["press_digit"]

    delay_ms: Optional[int] = None
    """
    Delay in milliseconds before pressing the digit, because a lot of IVR systems
    speak very slowly, and a delay can make sure the agent hears the full menu.
    Default to 1000 ms (1s). Valid range is 0 to 5000 ms (inclusive).
    """

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class StateToolSendSMSToolSMSContentSMSContentPredefined(BaseModel):
    content: Optional[str] = None
    """The static message to be sent in the SMS. Can contain dynamic variables."""

    type: Optional[Literal["predefined"]] = None


class StateToolSendSMSToolSMSContentSMSContentInferred(BaseModel):
    prompt: Optional[str] = None
    """The prompt to be used to help infer the SMS content.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right message to send. Can contain dynamic variables.
    """

    type: Optional[Literal["inferred"]] = None


StateToolSendSMSToolSMSContent: TypeAlias = Union[
    StateToolSendSMSToolSMSContentSMSContentPredefined, StateToolSendSMSToolSMSContentSMSContentInferred
]


class StateToolSendSMSTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    sms_content: StateToolSendSMSToolSMSContent

    type: Literal["send_sms"]

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """


class StateToolCustomToolParameters(BaseModel):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

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

    type: Literal["custom"]

    url: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    args_at_root: Optional[bool] = None
    """
    If set to true, the parameters will be passed as root level JSON object instead
    of nested under "args".
    """

    execution_message_description: Optional[str] = None
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    headers: Optional[Dict[str, str]] = None
    """Headers to add to the request."""

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None
    """Method to use for the request, default to POST."""

    parameters: Optional[StateToolCustomToolParameters] = None
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format. Omitting parameters defines a function with
    an empty parameter list.
    """

    query_params: Optional[Dict[str, str]] = None
    """Query parameters to append to the request URL."""

    response_variables: Optional[Dict[str, str]] = None
    """A mapping of variable names to JSON paths in the response body.

    These values will be extracted from the response and made available as dynamic
    variables for use.
    """

    speak_during_execution: Optional[bool] = None
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """

    timeout_ms: Optional[int] = None
    """The maximum time in milliseconds the tool can run before it's considered
    timeout.

    If the tool times out, the agent would have that info. The minimum value allowed
    is 1000 ms (1 s), and maximum value allowed is 600,000 ms (10 min). By default,
    this is set to 120,000 ms (2 min).
    """


class StateToolExtractDynamicVariableToolVariableStringAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["string"]
    """Type of the variable to extract."""

    examples: Optional[List[str]] = None
    """Examples of the variable value to teach model the style and syntax."""


class StateToolExtractDynamicVariableToolVariableEnumAnalysisData(BaseModel):
    choices: List[str]
    """The possible values of the variable, must be non empty array."""

    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["enum"]
    """Type of the variable to extract."""


class StateToolExtractDynamicVariableToolVariableBooleanAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["boolean"]
    """Type of the variable to extract."""


class StateToolExtractDynamicVariableToolVariableNumberAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["number"]
    """Type of the variable to extract."""


StateToolExtractDynamicVariableToolVariable: TypeAlias = Union[
    StateToolExtractDynamicVariableToolVariableStringAnalysisData,
    StateToolExtractDynamicVariableToolVariableEnumAnalysisData,
    StateToolExtractDynamicVariableToolVariableBooleanAnalysisData,
    StateToolExtractDynamicVariableToolVariableNumberAnalysisData,
]


class StateToolExtractDynamicVariableTool(BaseModel):
    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["extract_dynamic_variable"]

    variables: List[StateToolExtractDynamicVariableToolVariable]
    """The variables to be extracted."""


class StateToolBridgeTransferTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["bridge_transfer"]

    description: Optional[str] = None
    """Describes what the tool does.

    This tool is only available to transfer agents (agents with isTransferAgent set
    to true) in agentic warm transfer mode. When invoked, it bridges the original
    caller to the transfer target and ends the transfer agent call.
    """


class StateToolCancelTransferTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["cancel_transfer"]

    description: Optional[str] = None
    """Describes what the tool does.

    This tool is only available to transfer agents (agents with isTransferAgent set
    to true) in agentic warm transfer mode. When invoked, it cancels the transfer,
    returns the original caller to the main agent, and ends the transfer agent call.
    """


class StateToolMcpTool(BaseModel):
    description: str
    """Description of the MCP tool."""

    name: str
    """Name of the MCP tool."""

    type: Literal["mcp"]

    execution_message_description: Optional[str] = None
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    input_schema: Optional[Dict[str, str]] = None
    """The input schema of the MCP tool."""

    mcp_id: Optional[str] = None
    """Unique id of the MCP."""

    response_variables: Optional[Dict[str, str]] = None
    """
    Response variables to add to dynamic variables, key is the variable name, value
    is the path to the variable in the response
    """

    speak_after_execution: Optional[bool] = None
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: Optional[bool] = None
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """


StateTool: TypeAlias = Union[
    StateToolEndCallTool,
    StateToolTransferCallTool,
    StateToolCheckAvailabilityCalTool,
    StateToolBookAppointmentCalTool,
    StateToolAgentSwapTool,
    StateToolPressDigitTool,
    StateToolSendSMSTool,
    StateToolCustomTool,
    StateToolExtractDynamicVariableTool,
    StateToolBridgeTransferTool,
    StateToolCancelTransferTool,
    StateToolMcpTool,
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
    end call, transfer call, etc; or you can create your own custom tool for the LLM
    to use.

    - Tools of LLM = general tools + state tools + state transitions
    """


class LlmResponse(BaseModel):
    last_modification_timestamp: int
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    llm_id: str
    """Unique id of Retell LLM Response Engine."""

    begin_after_user_silence_ms: Optional[int] = None
    """
    If set, the AI will begin the conversation after waiting for the user for the
    duration (in milliseconds) specified by this attribute. This only applies if the
    agent is configured to wait for the user to speak first. If not set, the agent
    will wait indefinitely for the user to speak.
    """

    begin_message: Optional[str] = None
    """First utterance said by the agent in the call.

    If not set, LLM will dynamically generate a message. If set to "", agent will
    wait for user to speak first.
    """

    default_dynamic_variables: Optional[Dict[str, str]] = None
    """Default dynamic variables represented as key-value pairs of strings.

    These are injected into your Retell LLM prompt and tool description when
    specific values are not provided in a request. Only applicable for Retell LLM.
    """

    general_prompt: Optional[str] = None
    """General prompt appended to system prompt no matter what state the agent is in.

    - System prompt (with state) = general prompt + state prompt.
    - System prompt (no state) = general prompt.
    """

    general_tools: Optional[List[GeneralTool]] = None
    """A list of tools the model may call (to get external knowledge, call API, etc).

    You can select from some common predefined tools like end call, transfer call,
    etc; or you can create your own custom tool for the LLM to use.

    - Tools of LLM (with state) = general tools + state tools + state transitions
    - Tools of LLM (no state) = general tools
    """

    is_published: Optional[bool] = None
    """Whether the Retell LLM Response Engine is published."""

    kb_config: Optional[KBConfig] = None
    """Knowledge base configuration for RAG retrieval."""

    knowledge_base_ids: Optional[List[str]] = None
    """A list of knowledge base ids to use for this resource."""

    mcps: Optional[List[Mcp]] = None
    """A list of MCPs to use for this LLM."""

    model: Optional[
        Literal[
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "gpt-5",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5-mini",
            "gpt-5-nano",
            "claude-4.5-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
        ]
    ] = None
    """Select the underlying text LLM. If not set, would default to gpt-4.1."""

    api_model_high_priority: Optional[bool] = FieldInfo(alias="model_high_priority", default=None)
    """
    If set to true, will use high priority pool with more dedicated resource to
    ensure lower and more consistent latency, default to false. This feature usually
    comes with a higher cost.
    """

    api_model_temperature: Optional[float] = FieldInfo(alias="model_temperature", default=None)
    """If set, will control the randomness of the response.

    Value ranging from [0,1]. Lower value means more deterministic, while higher
    value means more random. If unset, default value 0 will apply. Note that for
    tool calling, a lower value is recommended.
    """

    s2s_model: Optional[Literal["gpt-4o-realtime", "gpt-4o-mini-realtime", "gpt-realtime", "gpt-realtime-mini"]] = None
    """Select the underlying speech to speech model.

    Can only set this or model, not both.
    """

    start_speaker: Optional[Literal["user", "agent"]] = None
    """The speaker who starts the conversation.

    Required. Must be either 'user' or 'agent'.
    """

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

    tool_call_strict_mode: Optional[bool] = None
    """Whether to use strict mode for tool calls.

    Only applicable when using certain supported models.
    """

    version: Optional[int] = None
    """The version of the LLM."""
