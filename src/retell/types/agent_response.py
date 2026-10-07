# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "AgentResponse",
    "ResponseEngine",
    "ResponseEngineResponseEngineRetellLm",
    "ResponseEngineResponseEngineCustomLm",
    "ResponseEngineResponseEngineConversationFlow",
    "CallScreeningOption",
    "ContactMemoryConfig",
    "CustomSttConfig",
    "GuardrailConfig",
    "HandbookConfig",
    "IvrOption",
    "IvrOptionAction",
    "PiiConfig",
    "PostCallAnalysisData",
    "PostCallAnalysisDataStringAnalysisData",
    "PostCallAnalysisDataEnumAnalysisData",
    "PostCallAnalysisDataBooleanAnalysisData",
    "PostCallAnalysisDataNumberAnalysisData",
    "PostCallAnalysisDataCallPresetAnalysisData",
    "PostSessionTool",
    "PostSessionToolAppTool",
    "PostSessionToolAppToolCondition",
    "PostSessionToolAppToolConditionEquation",
    "PostSessionToolAppToolOutputSelection",
    "PostSessionToolAppToolOutputSelectionUnionMember0",
    "PostSessionToolAppToolOutputSelectionUnionMember1",
    "PostSessionToolAppToolParameter",
    "PostSessionToolCustomTool",
    "PostSessionToolCustomToolCondition",
    "PostSessionToolCustomToolConditionEquation",
    "PostSessionToolCustomToolParameters",
    "PostSessionToolCodeTool",
    "PostSessionToolCodeToolCondition",
    "PostSessionToolCodeToolConditionEquation",
    "PostSessionToolSendSMSTool",
    "PostSessionToolSendSMSToolSMSContent",
    "PostSessionToolSendSMSToolSMSContentSMSContentPredefined",
    "PostSessionToolSendSMSToolSMSContentSMSContentInferred",
    "PostSessionToolSendSMSToolSMSContentSMSContentTemplate",
    "PostSessionToolSendSMSToolCondition",
    "PostSessionToolSendSMSToolConditionEquation",
    "PreSessionTool",
    "PreSessionToolAppTool",
    "PreSessionToolAppToolOutputSelection",
    "PreSessionToolAppToolOutputSelectionUnionMember0",
    "PreSessionToolAppToolOutputSelectionUnionMember1",
    "PreSessionToolAppToolParameter",
    "PreSessionToolCustomTool",
    "PreSessionToolCustomToolParameters",
    "PreSessionToolCodeTool",
    "PronunciationDictionary",
    "UserDtmfOptions",
    "VoicemailOption",
    "VoicemailOptionAction",
    "VoicemailOptionActionVoicemailActionPrompt",
    "VoicemailOptionActionVoicemailActionStaticText",
    "VoicemailOptionActionVoicemailActionHangup",
    "VoicemailOptionActionVoicemailActionBridgeTransfer",
]


class ResponseEngineResponseEngineRetellLm(BaseModel):
    llm_id: str
    """id of the Retell LLM Response Engine."""

    type: Literal["retell-llm"]
    """type of the Response Engine."""

    version: Optional[float] = None
    """Version of the Retell LLM Response Engine."""


class ResponseEngineResponseEngineCustomLm(BaseModel):
    llm_websocket_url: str
    """LLM websocket url of the custom LLM."""

    type: Literal["custom-llm"]
    """type of the Response Engine."""


class ResponseEngineResponseEngineConversationFlow(BaseModel):
    conversation_flow_id: str
    """ID of the Conversation Flow Response Engine."""

    type: Literal["conversation-flow"]
    """type of the Response Engine."""

    version: Optional[float] = None
    """Version of the Conversation Flow Response Engine."""


ResponseEngine: TypeAlias = Union[
    ResponseEngineResponseEngineRetellLm,
    ResponseEngineResponseEngineCustomLm,
    ResponseEngineResponseEngineConversationFlow,
]


class CallScreeningOption(BaseModel):
    """
    If this option is set, the agent prompt will include call screen handling instructions for identity and call purpose questions. Set this to null to disable call screen prompt instructions.
    """

    agent_identity: str
    """Identity the agent should provide when a call screen asks who is calling.

    Dynamic variables are supported.
    """

    call_purpose: str
    """Purpose the agent should provide when a call screen asks why it is calling.

    Dynamic variables are supported.
    """


class ContactMemoryConfig(BaseModel):
    """Contact memory settings for phone calls and SMS chats.

    Creating an agent defaults enable_update to false and enable_read to true. Updates only change the supplied flags; omitted flags stay unchanged and an empty object has no effect. Set a flag to false to disable it. The configuration cannot be cleared. Existing agents without this configuration have both disabled.
    """

    enable_read: Optional[bool] = None
    """Automatically add saved contact memory to the agent prompt.

    Skippable nodes can use answers from the current conversation even when this
    setting is disabled. Contact dynamic variables, including contact_memory, remain
    available regardless of this setting.
    """

    enable_update: Optional[bool] = None
    """Rewrite the contact memory after each conversation.

    Requires storing conversation data. Chat agents must also have
    end_chat_after_silence_ms set.
    """


class CustomSttConfig(BaseModel):
    """Custom STT configuration. Only used when stt_mode is set to custom."""

    endpointing_ms: int
    """Endpointing timeout in milliseconds.

    Minimum is 100 for Azure, 10 for Deepgram, 500 for Soniox, 100 for AssemblyAI,
    100 for Muse. For AssemblyAI, this sets min_turn_silence (100-3000 ms).
    max_turn_silence adds half of this value, rounded to the nearest millisecond and
    bounded to 500-1000 ms, with a total cap of 3000 ms. Muse detects turn ends
    itself and ignores this value.
    """

    provider: Literal["azure", "deepgram", "soniox", "assemblyai", "muse"]
    """ASR provider name."""


class GuardrailConfig(BaseModel):
    """
    Configuration for guardrail checks to detect and prevent prohibited topics in agent output and user input.
    """

    input_topics: Optional[List[Literal["platform_integrity_jailbreaking"]]] = None
    """Selected prohibited user topic categories to check.

    When user messages contain these topics, the agent will respond with a
    placeholder message instead of processing the request.
    """

    output_topics: Optional[
        List[
            Literal[
                "harassment",
                "self_harm",
                "sexual_exploitation",
                "violence",
                "defense_and_national_security",
                "illicit_and_harmful_activity",
                "gambling",
                "regulated_professional_advice",
                "child_safety_and_exploitation",
            ]
        ]
    ] = None
    """Selected prohibited agent topic categories to check.

    When agent messages contain these topics, they will be replaced with a
    placeholder message.
    """


class HandbookConfig(BaseModel):
    """Toggle behavior presets on/off to influence agent response style and behaviors."""

    ai_disclosure: Optional[bool] = None
    """When asked, acknowledge being a virtual assistant."""

    conversational_personality: Optional[bool] = None
    """Enables Conversational Personality.

    When true, the agent uses the Conversational Personality handbook preset, skips
    Professional Rep Personality during prompt assembly, and enables internal
    colloquial rewrite behavior.
    """

    default_personality: Optional[bool] = None
    """Professional call center rep baseline."""

    echo_verification: Optional[bool] = None
    """Repeat back and confirm important details (voice only)."""

    high_empathy: Optional[bool] = None
    """Warm acknowledgment of caller concerns."""

    nato_phonetic_alphabet: Optional[bool] = None
    """Spell using NATO phonetic alphabet style (voice only)."""

    natural_filler_words: Optional[bool] = None
    """
    Sprinkle natural speech fillers like "um", "you know" for a more human,
    conversational tone.
    """

    scope_boundaries: Optional[bool] = None
    """Stay within prompt/context scope, don't invent details."""

    smart_matching: Optional[bool] = None
    """
    Treat near-match similar words as same entity to reduce impact of transcription
    error (voice only).
    """

    speech_normalization: Optional[bool] = None
    """Convert numbers/dates/currency to spoken forms (voice only)."""


class IvrOptionAction(BaseModel):
    type: Literal["hangup"]


class IvrOption(BaseModel):
    """
    If this option is set, the call will try to detect IVR in the first 3 minutes of the call. Actions defined will be applied when the IVR is detected. Set this to null to disable IVR detection.
    """

    action: IvrOptionAction

    detection_prompt: Optional[str] = None
    """Optionally describe what should be treated as an IVR.

    Leave as null to use the default definition.
    """


class PiiConfig(BaseModel):
    """Configuration for PII scrubbing from transcripts and recordings."""

    categories: List[
        Literal[
            "person_name",
            "address",
            "email",
            "phone_number",
            "ssn",
            "passport",
            "driver_license",
            "credit_card",
            "bank_account",
            "password",
            "pin",
            "medical_id",
            "date_of_birth",
            "customer_account_number",
        ]
    ]
    """List of PII categories to scrub from transcripts and recordings.

    PII redaction is only active when this list is non-empty; an empty array means
    no PII scrubbing is performed.
    """

    mode: Literal["post_call"]
    """The processing mode for PII scrubbing. Currently only post-call is supported."""


class PostCallAnalysisDataStringAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["string"]
    """Type of the variable to extract."""

    conditional_prompt: Optional[str] = None
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    examples: Optional[List[str]] = None
    """Examples of the variable value to teach model the style and syntax."""

    required: Optional[bool] = None
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class PostCallAnalysisDataEnumAnalysisData(BaseModel):
    choices: List[str]
    """The possible values of the variable, must be non empty array."""

    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["enum"]
    """Type of the variable to extract."""

    conditional_prompt: Optional[str] = None
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: Optional[bool] = None
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class PostCallAnalysisDataBooleanAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["boolean"]
    """Type of the variable to extract."""

    conditional_prompt: Optional[str] = None
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: Optional[bool] = None
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class PostCallAnalysisDataNumberAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["number"]
    """Type of the variable to extract."""

    conditional_prompt: Optional[str] = None
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: Optional[bool] = None
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class PostCallAnalysisDataCallPresetAnalysisData(BaseModel):
    """System preset for post-call analysis (voice agents).

    Use in post_call_analysis_data to override prompts or mark fields optional.
    """

    name: Literal["call_summary", "call_successful", "user_sentiment"]
    """Preset identifier for voice agent analysis."""

    type: Literal["system-presets"]
    """Identifies this item as a system preset."""

    conditional_prompt: Optional[str] = None
    """Optional instruction to help decide whether this field needs to be populated.

    If not set, the field is always included.
    """

    description: Optional[str] = None
    """Prompt or description for this preset."""

    required: Optional[bool] = None
    """If false, this field is optional in the analysis.

    If true or unset, the field is required.
    """


PostCallAnalysisData: TypeAlias = Union[
    PostCallAnalysisDataStringAnalysisData,
    PostCallAnalysisDataEnumAnalysisData,
    PostCallAnalysisDataBooleanAnalysisData,
    PostCallAnalysisDataNumberAnalysisData,
    PostCallAnalysisDataCallPresetAnalysisData,
]


class PostSessionToolAppToolConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class PostSessionToolAppToolCondition(BaseModel):
    """Optional gate; the step only runs when the condition holds.

    Defaults to always running.
    """

    equations: List[PostSessionToolAppToolConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


class PostSessionToolAppToolOutputSelectionUnionMember0(BaseModel):
    mode: Literal["all"]

    fields: Optional[List[str]] = None
    """Not used at runtime; stored and returned as-is for the UI."""


class PostSessionToolAppToolOutputSelectionUnionMember1(BaseModel):
    fields: List[str]
    """
    The only response fields the agent and the transcript see, as dot-paths into the
    response schema returned by get-app-tool-schema. Everything else is dropped.
    Selecting a parent keeps its whole subtree. A plain segment traverses arrays
    element-wise (deals.properties.amount keeps that field on every deal), while
    key[n] selects one element (deals[0].id keeps only the first deal's id); paths
    that match nothing contribute nothing.
    """

    mode: Literal["subset"]


PostSessionToolAppToolOutputSelection: TypeAlias = Union[
    PostSessionToolAppToolOutputSelectionUnionMember0, PostSessionToolAppToolOutputSelectionUnionMember1
]


class PostSessionToolAppToolParameter(BaseModel):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

    properties: object
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


class PostSessionToolAppTool(BaseModel):
    app_id: str
    """The connection (App) this tool runs against.

    Must be a connection in the organization whose provider matches this tool's
    provider.
    """

    app_tool_template_name: str
    """
    Name of the catalog template within the provider, as listed by
    list-app-templates.
    """

    name: str
    """Name of the tool.

    Must be unique within the phase's tools; referenced by depends_on.
    """

    provider: str
    """Provider of the connection.

    Must match the connection's provider; supported providers are listed by
    list-app-templates.
    """

    type: Literal["integration_app"]

    condition: Optional[PostSessionToolAppToolCondition] = None
    """Optional gate; the step only runs when the condition holds.

    Defaults to always running.
    """

    depends_on: Optional[List[str]] = None
    """Names of tools that must run before this one."""

    description: Optional[str] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. Overrides the catalog template's LLM-facing description.
    """

    enable_typing_sound: Optional[bool] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. If true, play a typing sound on the agent audio track while this
    tool is executing. Useful when the tool takes a noticeable amount of time to
    prevent silence on the call.
    """

    execution_message_description: Optional[str] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. The message for the agent to speak when executing the tool. Only
    applicable when speak_during_execution is true.
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. Type of execution message. "prompt" means the agent will use
    execution_message_description as a prompt to generate the message. "static_text"
    means the agent will speak the execution_message_description directly. Defaults
    to "prompt".
    """

    output_selection: Optional[PostSessionToolAppToolOutputSelection] = None
    """What the agent and the transcript see of the tool's response.

    Omit to send the full response. Does not affect response_variables, which are
    always extracted from the raw response.
    """

    parameters: Optional[List[PostSessionToolAppToolParameter]] = None
    """The resolved input parameters, in order.

    Properties may pin a value with const (including {{variable}} references) or
    provide a description for LLM inference. Each property may also record
    selected*input_mode, the editor mode the user selected ("const_enum",
    "const_boolean", "const_value", "description_custom", or "description_preset");
    it is stored and returned as-is, used only by the tool config UI. Omit the key
    when no mode is recorded; when set, const*_ modes require a non-empty const, and
    description\\___ modes must omit const entirely. Each parameter's required list
    must match the schema returned by the corresponding step of the
    get-app-tool-schema loop.
    """

    response_variables: Optional[Dict[str, str]] = None
    """
    Mapping of a dynamic-variable name to the response field (dot-path) it is
    populated from. Missing paths are ignored.
    """

    speak_after_execution: Optional[bool] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. Determines whether the agent would call LLM another time and speak
    when the result of the tool is obtained.
    """

    speak_during_execution: Optional[bool] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. If true, will speak during execution.
    """


class PostSessionToolCustomToolConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class PostSessionToolCustomToolCondition(BaseModel):
    """Optional gate; the step only runs when the condition holds.

    Defaults to always running.
    """

    equations: List[PostSessionToolCustomToolConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


class PostSessionToolCustomToolParameters(BaseModel):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

    properties: object
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


class PostSessionToolCustomTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
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

    condition: Optional[PostSessionToolCustomToolCondition] = None
    """Optional gate; the step only runs when the condition holds.

    Defaults to always running.
    """

    depends_on: Optional[List[str]] = None
    """Names of tools that must run before this one."""

    description: Optional[str] = None
    """Describes what this tool does and when to call this tool."""

    enable_typing_sound: Optional[bool] = None
    """
    If true, play a typing sound on the agent audio track while this tool is
    executing. Useful when the tool takes a noticeable amount of time to prevent
    silence on the call.
    """

    execution_message_description: Optional[str] = None
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    headers: Optional[Dict[str, str]] = None
    """Headers to add to the request."""

    max_retry: Optional[int] = None
    """
    Maximum number of times to retry the request after a failed attempt, from 0 (no
    retry) to 5. Retries happen on any failure, with exponential backoff between
    attempts; the backoff delay is not configurable. `timeout_ms` applies per
    attempt rather than as a budget across all attempts, so an attempt that times
    out is still retried and the worst-case total duration is `timeout_ms`
    multiplied by (`max_retry` + 1) as well as any latency incurred by the
    exponential backoff + jitter between each retry. Only the final attempt's result
    is reported to the agent. Because retries repeat the request, only set this
    above 0 if your endpoint is idempotent — a retried request may be processed more
    than once. Defaults to 0 (no retry).
    """

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None
    """Method to use for the request, default to POST."""

    parameter_type: Optional[Literal["json", "form"]] = None
    """
    How the tool's `parameters` are authored and shown in the dashboard editor —
    "form" for the visual parameter builder, "json" for a raw JSON Schema. Both
    produce the same `parameters` schema; this does not change how the request body
    is encoded (see `args_at_root`).
    """

    parameters: Optional[PostSessionToolCustomToolParameters] = None
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

    timeout_ms: Optional[int] = None
    """The maximum time in milliseconds the tool can run before it's considered
    timeout.

    If the tool times out, the agent would have that info. The minimum value allowed
    is 1000 ms (1 s), and maximum value allowed is 600,000 ms (10 min). By default,
    this is set to 120,000 ms (2 min).
    """


class PostSessionToolCodeToolConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class PostSessionToolCodeToolCondition(BaseModel):
    """Optional gate; the step only runs when the condition holds.

    Defaults to always running.
    """

    equations: List[PostSessionToolCodeToolConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


class PostSessionToolCodeTool(BaseModel):
    code: str
    """JavaScript code to execute in the sandbox."""

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["code"]

    condition: Optional[PostSessionToolCodeToolCondition] = None
    """Optional gate; the step only runs when the condition holds.

    Defaults to always running.
    """

    depends_on: Optional[List[str]] = None
    """Names of tools that must run before this one."""

    description: Optional[str] = None
    """Describes what this tool does and when to call this tool."""

    enable_typing_sound: Optional[bool] = None
    """
    If true, play a typing sound on the agent audio track while this tool is
    executing.
    """

    execution_message_description: Optional[str] = None
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    response_variables: Optional[Dict[str, str]] = None
    """A mapping of variable names to JSON paths in the code execution result.

    These mapped values will be extracted and added as dynamic variables.
    """

    speak_after_execution: Optional[bool] = None
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained.
    """

    speak_during_execution: Optional[bool] = None
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the tool.
    """

    timeout_ms: Optional[int] = None
    """The maximum time in milliseconds the code can run before it's considered
    timeout.

    Defaults to 30,000 ms (30 s).
    """


class PostSessionToolSendSMSToolSMSContentSMSContentPredefined(BaseModel):
    text: Optional[str] = None
    """The static message to be sent in the SMS. Can contain dynamic variables."""

    type: Optional[Literal["predefined"]] = None


class PostSessionToolSendSMSToolSMSContentSMSContentInferred(BaseModel):
    prompt: Optional[str] = None
    """The prompt to be used to help infer the SMS content.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right message to send. Can contain dynamic variables.
    """

    type: Optional[Literal["inferred"]] = None


class PostSessionToolSendSMSToolSMSContentSMSContentTemplate(BaseModel):
    template: Literal["info_collection"]
    """The template to use for the SMS content.

    "info_collection" sends a predefined message requesting information from the
    user.
    """

    type: Literal["template"]


PostSessionToolSendSMSToolSMSContent: TypeAlias = Union[
    PostSessionToolSendSMSToolSMSContentSMSContentPredefined,
    PostSessionToolSendSMSToolSMSContentSMSContentInferred,
    PostSessionToolSendSMSToolSMSContentSMSContentTemplate,
]


class PostSessionToolSendSMSToolConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class PostSessionToolSendSMSToolCondition(BaseModel):
    """Optional gate; the step only runs when the condition holds.

    Defaults to always running.
    """

    equations: List[PostSessionToolSendSMSToolConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


class PostSessionToolSendSMSTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    sms_content: PostSessionToolSendSMSToolSMSContent

    type: Literal["send_sms"]

    condition: Optional[PostSessionToolSendSMSToolCondition] = None
    """Optional gate; the step only runs when the condition holds.

    Defaults to always running.
    """

    depends_on: Optional[List[str]] = None
    """Names of tools that must run before this one."""

    description: Optional[str] = None
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: Optional[str] = None
    """Describes what to say before sending the SMS.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: Optional[bool] = None
    """If true, the agent will speak a short line before sending the SMS.

    If omitted, defaults to true (same as end_call / transfer_call tools).
    """


PostSessionTool: TypeAlias = Union[
    PostSessionToolAppTool, PostSessionToolCustomTool, PostSessionToolCodeTool, PostSessionToolSendSMSTool
]


class PreSessionToolAppToolOutputSelectionUnionMember0(BaseModel):
    mode: Literal["all"]

    fields: Optional[List[str]] = None
    """Not used at runtime; stored and returned as-is for the UI."""


class PreSessionToolAppToolOutputSelectionUnionMember1(BaseModel):
    fields: List[str]
    """
    The only response fields the agent and the transcript see, as dot-paths into the
    response schema returned by get-app-tool-schema. Everything else is dropped.
    Selecting a parent keeps its whole subtree. A plain segment traverses arrays
    element-wise (deals.properties.amount keeps that field on every deal), while
    key[n] selects one element (deals[0].id keeps only the first deal's id); paths
    that match nothing contribute nothing.
    """

    mode: Literal["subset"]


PreSessionToolAppToolOutputSelection: TypeAlias = Union[
    PreSessionToolAppToolOutputSelectionUnionMember0, PreSessionToolAppToolOutputSelectionUnionMember1
]


class PreSessionToolAppToolParameter(BaseModel):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

    properties: object
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


class PreSessionToolAppTool(BaseModel):
    app_id: str
    """The connection (App) this tool runs against.

    Must be a connection in the organization whose provider matches this tool's
    provider.
    """

    app_tool_template_name: str
    """
    Name of the catalog template within the provider, as listed by
    list-app-templates.
    """

    name: str
    """Name of the tool.

    Must be unique within the phase's tools; referenced by depends_on.
    """

    provider: str
    """Provider of the connection.

    Must match the connection's provider; supported providers are listed by
    list-app-templates.
    """

    type: Literal["integration_app"]

    depends_on: Optional[List[str]] = None
    """Names of tools that must run before this one."""

    description: Optional[str] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. Overrides the catalog template's LLM-facing description.
    """

    enable_typing_sound: Optional[bool] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. If true, play a typing sound on the agent audio track while this
    tool is executing. Useful when the tool takes a noticeable amount of time to
    prevent silence on the call.
    """

    execution_message_description: Optional[str] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. The message for the agent to speak when executing the tool. Only
    applicable when speak_during_execution is true.
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. Type of execution message. "prompt" means the agent will use
    execution_message_description as a prompt to generate the message. "static_text"
    means the agent will speak the execution_message_description directly. Defaults
    to "prompt".
    """

    output_selection: Optional[PreSessionToolAppToolOutputSelection] = None
    """What the agent and the transcript see of the tool's response.

    Omit to send the full response. Does not affect response_variables, which are
    always extracted from the raw response.
    """

    parameters: Optional[List[PreSessionToolAppToolParameter]] = None
    """The resolved input parameters, in order.

    Properties may pin a value with const (including {{variable}} references) or
    provide a description for LLM inference. Each property may also record
    selected*input_mode, the editor mode the user selected ("const_enum",
    "const_boolean", "const_value", "description_custom", or "description_preset");
    it is stored and returned as-is, used only by the tool config UI. Omit the key
    when no mode is recorded; when set, const*_ modes require a non-empty const, and
    description\\___ modes must omit const entirely. Each parameter's required list
    must match the schema returned by the corresponding step of the
    get-app-tool-schema loop.
    """

    response_variables: Optional[Dict[str, str]] = None
    """
    Mapping of a dynamic-variable name to the response field (dot-path) it is
    populated from. Missing paths are ignored.
    """

    speak_after_execution: Optional[bool] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. Determines whether the agent would call LLM another time and speak
    when the result of the tool is obtained.
    """

    speak_during_execution: Optional[bool] = None
    """
    Only applies to during conversation functions; ignored by the pre/post
    conversation. If true, will speak during execution.
    """


class PreSessionToolCustomToolParameters(BaseModel):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

    properties: object
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


class PreSessionToolCustomTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
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

    depends_on: Optional[List[str]] = None
    """Names of tools that must run before this one."""

    description: Optional[str] = None
    """Describes what this tool does and when to call this tool."""

    enable_typing_sound: Optional[bool] = None
    """
    If true, play a typing sound on the agent audio track while this tool is
    executing. Useful when the tool takes a noticeable amount of time to prevent
    silence on the call.
    """

    execution_message_description: Optional[str] = None
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    headers: Optional[Dict[str, str]] = None
    """Headers to add to the request."""

    max_retry: Optional[int] = None
    """
    Maximum number of times to retry the request after a failed attempt, from 0 (no
    retry) to 5. Retries happen on any failure, with exponential backoff between
    attempts; the backoff delay is not configurable. `timeout_ms` applies per
    attempt rather than as a budget across all attempts, so an attempt that times
    out is still retried and the worst-case total duration is `timeout_ms`
    multiplied by (`max_retry` + 1) as well as any latency incurred by the
    exponential backoff + jitter between each retry. Only the final attempt's result
    is reported to the agent. Because retries repeat the request, only set this
    above 0 if your endpoint is idempotent — a retried request may be processed more
    than once. Defaults to 0 (no retry).
    """

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None
    """Method to use for the request, default to POST."""

    parameter_type: Optional[Literal["json", "form"]] = None
    """
    How the tool's `parameters` are authored and shown in the dashboard editor —
    "form" for the visual parameter builder, "json" for a raw JSON Schema. Both
    produce the same `parameters` schema; this does not change how the request body
    is encoded (see `args_at_root`).
    """

    parameters: Optional[PreSessionToolCustomToolParameters] = None
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

    timeout_ms: Optional[int] = None
    """The maximum time in milliseconds the tool can run before it's considered
    timeout.

    If the tool times out, the agent would have that info. The minimum value allowed
    is 1000 ms (1 s), and maximum value allowed is 600,000 ms (10 min). By default,
    this is set to 120,000 ms (2 min).
    """


class PreSessionToolCodeTool(BaseModel):
    code: str
    """JavaScript code to execute in the sandbox."""

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["code"]

    depends_on: Optional[List[str]] = None
    """Names of tools that must run before this one."""

    description: Optional[str] = None
    """Describes what this tool does and when to call this tool."""

    enable_typing_sound: Optional[bool] = None
    """
    If true, play a typing sound on the agent audio track while this tool is
    executing.
    """

    execution_message_description: Optional[str] = None
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    response_variables: Optional[Dict[str, str]] = None
    """A mapping of variable names to JSON paths in the code execution result.

    These mapped values will be extracted and added as dynamic variables.
    """

    speak_after_execution: Optional[bool] = None
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained.
    """

    speak_during_execution: Optional[bool] = None
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the tool.
    """

    timeout_ms: Optional[int] = None
    """The maximum time in milliseconds the code can run before it's considered
    timeout.

    Defaults to 30,000 ms (30 s).
    """


PreSessionTool: TypeAlias = Union[PreSessionToolAppTool, PreSessionToolCustomTool, PreSessionToolCodeTool]


class PronunciationDictionary(BaseModel):
    alphabet: Literal["ipa", "cmu", "pinyin", "jyutping"]
    """The phonetic alphabet to use.

    MiniMax speech-02-turbo supports IPA and Pinyin. MiniMax speech-2.8-turbo also
    supports Jyutping. Support for other alphabets depends on the selected voice
    provider and model.
    """

    phoneme: str
    """Pronunciation of the word in the format of the selected phonetic alphabet."""

    word: str
    """The string of word / phrase to be annotated with pronunciation."""


class UserDtmfOptions(BaseModel):
    digit_limit: Optional[float] = None
    """
    The maximum number of digits allowed in the user's DTMF (Dual-Tone
    Multi-Frequency) input per turn. Once this limit is reached, the input is
    considered complete and a response will be generated immediately.
    """

    termination_key: Optional[str] = None
    """A single key that signals the end of DTMF input.

    Acceptable values include any digit (0-9), the pound/hash symbol (#), or the
    asterisk (\\**).
    """

    timeout_ms: Optional[int] = None
    """The time (in milliseconds) to wait for user DTMF input before timing out.

    The timer resets with each digit received.
    """


class VoicemailOptionActionVoicemailActionPrompt(BaseModel):
    text: str
    """
    The prompt used to generate the text to be spoken when the call is detected to
    be in voicemail.
    """

    type: Literal["prompt"]


class VoicemailOptionActionVoicemailActionStaticText(BaseModel):
    text: str
    """The text to be spoken when the call is detected to be in voicemail."""

    type: Literal["static_text"]


class VoicemailOptionActionVoicemailActionHangup(BaseModel):
    type: Literal["hangup"]


class VoicemailOptionActionVoicemailActionBridgeTransfer(BaseModel):
    type: Literal["bridge_transfer"]


VoicemailOptionAction: TypeAlias = Union[
    VoicemailOptionActionVoicemailActionPrompt,
    VoicemailOptionActionVoicemailActionStaticText,
    VoicemailOptionActionVoicemailActionHangup,
    VoicemailOptionActionVoicemailActionBridgeTransfer,
]


class VoicemailOption(BaseModel):
    """
    If this option is set, the call will try to detect voicemail in the first 3 minutes of the call. Actions defined (hangup, or leave a message) will be applied when the voicemail is detected. Set this to null to disable voicemail detection.
    """

    action: VoicemailOptionAction

    detection_prompt: Optional[str] = None
    """Optionally describe what should be treated as voicemail.

    Leave as null to use the default definition.
    """


class AgentResponse(BaseModel):
    agent_id: str
    """Unique id of agent."""

    last_modification_timestamp: int
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    response_engine: ResponseEngine
    """The Response Engine to attach to the agent.

    It is used to generate responses for the agent. You need to create a Response
    Engine first before attaching it to an agent.
    """

    version: int
    """Version of the agent."""

    voice_id: str
    """Unique voice id used for the agent.

    Find list of available voices and their preview in Dashboard.
    """

    agent_name: Optional[str] = None
    """The name of the agent. Only used for your own reference."""

    allow_dtmf_interruption: Optional[bool] = None
    """
    If set to true, DTMF input will interrupt the agent even when
    interruption_sensitivity is 0. Can be overridden per conversation or subagent
    node. Default to false.
    """

    allow_user_dtmf: Optional[bool] = None
    """If set to true, DTMF input will be accepted and processed.

    If false, any DTMF input will be ignored. Default to true.
    """

    ambient_sound: Optional[
        Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise", "call-center"]
    ] = None
    """
    If set, will add ambient environment sound to the call to make experience more
    realistic. Currently supports the following options:

    - `coffee-shop`: Coffee shop ambience with people chatting in background.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/coffee-shop.wav)
    - `convention-hall`: Convention hall ambience, with some echo and people
      chatting in background.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/convention-hall.wav)
    - `summer-outdoor`: Summer outdoor ambience with cicada chirping.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/summer-outdoor.wav)
    - `mountain-outdoor`: Mountain outdoor ambience with birds singing.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/mountain-outdoor.wav)
    - `static-noise`: Constant static noise.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/static-noise.wav)
    - `call-center`: Call center work noise.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/call-center.wav)
      Set to `null` to remove ambient sound from this agent.
    """

    ambient_sound_volume: Optional[float] = None
    """If set, will control the volume of the ambient sound.

    Value ranging from [0,2]. Lower value means quieter ambient sound, while higher
    value means louder ambient sound. If unset, default value 1 will apply.
    """

    assigned_tags: Optional[List[str]] = None
    """Tags assigned to this agent version. Preferred tag is listed first."""

    backchannel_frequency: Optional[float] = None
    """Only applicable when enable_backchannel is true.

    Controls how often the agent would backchannel when a backchannel is possible.
    Value ranging from [0,1]. Lower value means less frequent backchannel, while
    higher value means more frequent backchannel. If unset, default value 0.8 will
    apply.
    """

    backchannel_words: Optional[List[str]] = None
    """Only applicable when enable_backchannel is true.

    A list of words that the agent would use as backchannel. If not set, default
    backchannel words will apply. Check out
    [backchannel default words](/agent/interaction-configuration#backchannel) for
    more details. Note that certain voices do not work too well with certain words,
    so it's recommended to experiment before adding any words.
    """

    base_version: Optional[int] = None
    """Version that this draft was based on. Null for initial versions."""

    begin_message_delay_ms: Optional[int] = None
    """
    If set, will delay the first message by the specified amount of milliseconds, so
    that it gives user more time to prepare to take the call. Valid range is [0,
    5000]. If not set or set to 0, agent will speak immediately. Only applicable
    when agent speaks first.
    """

    boosted_keywords: Optional[List[str]] = None
    """
    Provide a customized list of keywords to bias the transcriber model, so that
    these words are more likely to get transcribed. Commonly used for names, brands,
    street, etc. Entries may reference dynamic variables with `{{variable}}` syntax.
    """

    call_screening_option: Optional[CallScreeningOption] = None
    """
    If this option is set, the agent prompt will include call screen handling
    instructions for identity and call purpose questions. Set this to null to
    disable call screen prompt instructions.
    """

    contact_memory_config: Optional[ContactMemoryConfig] = None
    """Contact memory settings for phone calls and SMS chats.

    Creating an agent defaults enable_update to false and enable_read to true.
    Updates only change the supplied flags; omitted flags stay unchanged and an
    empty object has no effect. Set a flag to false to disable it. The configuration
    cannot be cleared. Existing agents without this configuration have both
    disabled.
    """

    custom_stt_config: Optional[CustomSttConfig] = None
    """Custom STT configuration. Only used when stt_mode is set to custom."""

    data_storage_retention_days: Optional[int] = None
    """Number of days to retain call/chat data before automatic deletion.

    Must be between 1 and 730 days. If not set, data is retained forever (no
    automatic deletion).
    """

    data_storage_setting: Optional[Literal["everything", "everything_except_pii", "basic_attributes_only"]] = None
    """
    Granular setting to manage how Retell stores sensitive data (transcripts,
    recordings, logs, etc.). This replaces the deprecated
    `opt_out_sensitive_data_storage` field.

    - `everything`: Store all data including transcripts, recordings, and logs.
    - `everything_except_pii`: Store data without PII when PII is detected.
    - `basic_attributes_only`: Store only basic attributes; no
      transcripts/recordings/logs. If not set, default value of "everything" will
      apply.
    """

    denoising_enhancement_level: Optional[float] = None
    """Controls the enhancement level for background voice cancellation.

    Set to 0 to bypass background voice cancellation without BVC charges. Value
    ranging from [0,1]. Only applicable when denoising_mode is
    noise-and-background-speech-cancellation. Defaults to 0.8 if no value is
    configured. Set to null to clear the configured value. Omitting this field
    preserves the existing value.
    """

    denoising_mode: Optional[
        Literal["no-denoise", "noise-cancellation", "noise-and-background-speech-cancellation"]
    ] = None
    """If set, determines what denoising mode to use.

    Use "no-denoise" to bypass all audio denoising. Default to noise-cancellation.
    """

    enable_backchannel: Optional[bool] = None
    """
    Controls whether the agent would backchannel (agent interjects the speaker with
    phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
    when enabled tends to show up more in longer user utterances. If not set, agent
    will not backchannel.
    """

    enable_dnc_detection: Optional[bool] = None
    """
    If set to true, the agent recognizes requests to stop calling or contacting the
    user, confirms once, and on a clear yes ends the call with disconnection reason
    user_requested_dnc and sets do_not_call to true on the contact for the user's
    phone number. If unset, default value false will apply.
    """

    enable_dynamic_responsiveness: Optional[bool] = None
    """
    If set to true, the agent will dynamically adjust how quickly it responds based
    on the user's speech rate and past turn-taking behavior in the call. If unset,
    default value false will apply.
    """

    enable_dynamic_voice_speed: Optional[bool] = None
    """
    If set to true, will enable dynamic voice speed adjustment based on the user's
    speech rate and conversation context. If unset, default value false will apply.
    """

    enable_expressive_mode: Optional[bool] = None
    """Master toggle for expressive mode.

    When true, the agent may add expressive voice tags to the audio it generates.
    Only applicable for platform voices. If unset, defaults to false.
    """

    end_call_after_silence_ms: Optional[int] = None
    """If users stay silent for a period after agent speech, end the call.

    The minimum value allowed is 10,000 ms (10 s). By default, this is set to 600000
    (10 min).
    """

    expressive_emotion_tags: Optional[
        List[
            Literal[
                "empathetic",
                "excited",
                "happy",
                "curious",
                "surprised",
                "sigh",
                "clear throat",
                "pause",
                "long pause",
                "emphasis",
            ]
        ]
    ] = None
    """
    The expressive voice tags Retell pre-teaches the model to use when
    enable_expressive_mode is true. Custom tags defined in the system prompt are
    still allowed. If empty, the agent follows general expressive guidance without a
    fixed tag set.
    """

    expressive_mode_prompt: Optional[str] = None
    """
    Custom expressive voice guidance to use instead of the default Retell expressive
    prompt when enable_expressive_mode is true. If omitted or blank, the default
    expressive prompt will be used.
    """

    fallback_voice_ids: Optional[List[str]] = None
    """
    When TTS provider for the selected voice is experiencing outages, we would use
    fallback voices listed here for the agent. Voice id and the fallback voice ids
    must be from different TTS providers. The system would go through the list in
    order, if the first one in the list is also having outage, it would use the next
    one. Set to null to remove voice fallback for the agent.
    """

    guardrail_config: Optional[GuardrailConfig] = None
    """
    Configuration for guardrail checks to detect and prevent prohibited topics in
    agent output and user input.
    """

    handbook_config: Optional[HandbookConfig] = None
    """Toggle behavior presets on/off to influence agent response style and behaviors."""

    interruption_sensitivity: Optional[float] = None
    """Controls how sensitive the agent is to user interruptions.

    Value ranging from [0,1]. Lower value means it will take longer / more words for
    user to interrupt agent, while higher value means it's easier for user to
    interrupt agent. If unset, default value 1 will apply. When this is set to 0,
    agent would never be interrupted.
    """

    is_published: Optional[bool] = None
    """Whether the agent is published."""

    ivr_option: Optional[IvrOption] = None
    """
    If this option is set, the call will try to detect IVR in the first 3 minutes of
    the call. Actions defined will be applied when the IVR is detected. Set this to
    null to disable IVR detection.
    """

    language: Union[
        Literal[
            "en-US",
            "en-IN",
            "en-GB",
            "en-AU",
            "en-NZ",
            "de-DE",
            "es-ES",
            "es-419",
            "hi-IN",
            "fr-FR",
            "fr-CA",
            "ja-JP",
            "pt-PT",
            "pt-BR",
            "zh-CN",
            "ru-RU",
            "it-IT",
            "ko-KR",
            "nl-NL",
            "nl-BE",
            "pl-PL",
            "tr-TR",
            "vi-VN",
            "ro-RO",
            "bg-BG",
            "ca-ES",
            "th-TH",
            "da-DK",
            "fi-FI",
            "el-GR",
            "hu-HU",
            "id-ID",
            "no-NO",
            "sk-SK",
            "sv-SE",
            "lt-LT",
            "lv-LV",
            "cs-CZ",
            "ms-MY",
            "af-ZA",
            "ar-SA",
            "az-AZ",
            "bs-BA",
            "cy-GB",
            "fa-IR",
            "fil-PH",
            "gl-ES",
            "he-IL",
            "hr-HR",
            "hy-AM",
            "is-IS",
            "kk-KZ",
            "kn-IN",
            "mk-MK",
            "mr-IN",
            "ne-NP",
            "sl-SI",
            "sr-RS",
            "sw-KE",
            "ta-IN",
            "ur-IN",
            "yue-CN",
            "uk-UA",
            "multi",
        ],
        List[
            Literal[
                "en-US",
                "en-IN",
                "en-GB",
                "en-AU",
                "en-NZ",
                "de-DE",
                "es-ES",
                "es-419",
                "hi-IN",
                "fr-FR",
                "fr-CA",
                "ja-JP",
                "pt-PT",
                "pt-BR",
                "zh-CN",
                "ru-RU",
                "it-IT",
                "ko-KR",
                "nl-NL",
                "nl-BE",
                "pl-PL",
                "tr-TR",
                "vi-VN",
                "ro-RO",
                "bg-BG",
                "ca-ES",
                "th-TH",
                "da-DK",
                "fi-FI",
                "el-GR",
                "hu-HU",
                "id-ID",
                "no-NO",
                "sk-SK",
                "sv-SE",
                "lt-LT",
                "lv-LV",
                "cs-CZ",
                "ms-MY",
                "af-ZA",
                "ar-SA",
                "az-AZ",
                "bs-BA",
                "cy-GB",
                "fa-IR",
                "fil-PH",
                "gl-ES",
                "he-IL",
                "hr-HR",
                "hy-AM",
                "is-IS",
                "kk-KZ",
                "kn-IN",
                "mk-MK",
                "mr-IN",
                "ne-NP",
                "sl-SI",
                "sr-RS",
                "sw-KE",
                "ta-IN",
                "ur-IN",
                "yue-CN",
                "uk-UA",
            ]
        ],
        None,
    ] = None
    """Specifies what language(s) the agent will operate in.

    Accepts either a single locale (e.g. `en-US`) or an array of locales for
    multilingual agents (e.g. `["en-US","es-ES"]`). The scalar value `multi` is
    deprecated but still accepted as a scalar, and is stored and returned as the ten
    locales it used to mean. It must not appear inside the array form. Send an
    explicit locale array instead. If unset, defaults to `en-US`.
    """

    max_call_duration_ms: Optional[int] = None
    """Maximum allowed length for the call, will force end the call if reached.

    The minimum value allowed is 60,000 ms (1 min), and maximum value allowed is
    7,200,000 (2 hours). By default, this is set to 3,600,000 (1 hour).
    """

    opt_in_signed_url: Optional[bool] = None
    """Whether this agent opts in for signed URLs for public logs and recordings.

    When enabled, the generated URLs will include security signatures that restrict
    access and automatically expire after 24 hours.
    """

    pii_config: Optional[PiiConfig] = None
    """Configuration for PII scrubbing from transcripts and recordings."""

    post_call_analysis_data: Optional[List[PostCallAnalysisData]] = None
    """Post call analysis data to extract from the call.

    This data will augment the pre-defined variables extracted in the call analysis.
    This will be available after the call ends.
    """

    post_call_analysis_model: Optional[
        Literal[
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "gpt-5",
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "gpt-5.6-terra",
            "gpt-5.6-luna",
            "gpt-6-astra",
            "gpt-6-sol",
            "gpt-6.1-sol",
            "gpt-6-luna",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-5-opus",
            "claude-5.5-opus",
            "claude-5-sonnet",
            "claude-5.5-sonnet",
            "claude-4.5-haiku",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
            "gemini-3.5-flash",
            "gemini-3.5-flash-lite",
            "gemini-3.6-flash",
            "gemini-3.7-flash",
            "gemini-3.8-flash",
        ]
    ] = None
    """The model to use for post call analysis. Default to gpt-5.6-terra."""

    post_session_tools: Optional[List[PostSessionTool]] = None
    """
    Integration (Agent Functions) tools run as a dependency graph during teardown,
    after post-call analysis. Each tool can be gated by a condition. On calls the
    graph is stopped after five minutes so teardown can finish. Set to null to
    clear.
    """

    pre_session_tools: Optional[List[PreSessionTool]] = None
    """
    Integration (Agent Functions) tools run as a dependency graph during session
    setup, before the agent's first message. Outputs are injected as dynamic
    variables. On calls the graph gets one minute unless an outbound caller will be
    dialed after setup, in which case it gets five minutes. Past that session
    initialization continues and any remaining tools finish in the background, so
    their outputs no longer reach the agent's prompt. Set to null to clear.
    """

    pronunciation_dictionary: Optional[List[PronunciationDictionary]] = None
    """
    A list of words / phrases and their pronunciation to be used to guide the audio
    synthesize for consistent pronunciation. Check the dashboard to see what
    provider supports this feature. Set to null to remove pronunciation dictionary
    from this agent.
    """

    reminder_max_count: Optional[int] = None
    """
    If set, controls how many times agent would remind user when user is
    unresponsive. Must be a non negative integer. If unset, default value of 1 will
    apply (remind once). Set to 0 to disable agent from reminding.
    """

    reminder_trigger_ms: Optional[float] = None
    """
    If set (in milliseconds), will trigger a reminder to the agent to speak if the
    user has been silent for the specified duration after some agent speech. Must be
    a positive number. If unset, default value of 10000 ms (10 s) will apply.
    """

    responsiveness: Optional[float] = None
    """Controls how responsive is the agent.

    Value ranging from [0,1]. Lower value means less responsive agent (wait more,
    respond slower), while higher value means faster exchanges (respond when it
    can). If unset, default value 1 will apply.
    """

    ring_duration_ms: Optional[int] = None
    """If set, the phone ringing will last for the specified amount of milliseconds.

    This applies for both outbound call ringtime, and call transfer ringtime.
    Default to 30000 (30 s). Valid range is [5000, 300000].
    """

    signed_url_expiration_ms: Optional[int] = None
    """The expiration time for the signed url in milliseconds.

    Only applicable when opt_in_signed_url is true. If not set, default value of
    86400000 (24 hours) will apply.
    """

    stt_mode: Optional[Literal["fast", "accurate", "custom"]] = None
    """If set, determines whether speech to text should focus on latency or accuracy.

    Default to fast mode. When set to custom, custom_stt_config must be provided.
    """

    timezone: Optional[str] = None
    """IANA timezone for the agent (e.g.

    America/New_York). Defaults to America/Los_Angeles if not set.
    """

    user_dtmf_options: Optional[UserDtmfOptions] = None

    version_description: Optional[str] = None
    """Optional description of the agent version.

    Used for your own reference and documentation.
    """

    version_title: Optional[str] = None
    """Optional title of the agent version. Used for your own reference."""

    vocab_specialization: Optional[Literal["general", "medical"]] = None
    """If set, determines the vocabulary set to use for transcription.

    This setting only applies for English agents, for non English agent, this
    setting is a no-op. Default to general.
    """

    voice_model: Optional[
        Literal[
            "eleven_flash_v2",
            "eleven_flash_v2_5",
            "eleven_multilingual_v2",
            "eleven_v3",
            "eleven_v3_conversational",
            "eleven_v4",
            "eleven_v4_turbo",
            "sonic-3",
            "sonic-3-latest",
            "sonic-3.5",
            "sonic-3.6",
            "tts-1",
            "gpt-4o-mini-tts",
            "speech-02-turbo",
            "speech-2.8-turbo",
            "s1",
            "s2-pro",
            "s2.1-pro",
            "inworld-tts-2",
            "inworld-tts-2-flash",
        ]
    ] = None
    """Select the voice model used for the selected voice.

    Each provider has a set of available voice models. Set to null to remove voice
    model selection, and default ones will apply. Check out dashboard for more
    details of each voice model.
    """

    voice_speed: Optional[float] = None
    """Controls speed of voice.

    Value ranging from [0.5,2]. Lower value means slower speech, while higher value
    means faster speech rate. If unset, default value 1 will apply.
    """

    voice_temperature: Optional[float] = None
    """Controls how stable the voice is.

    Value ranging from [0,2]. Lower value means more stable, and higher value means
    more variant speech generation. Check the dashboard to see what provider
    supports this feature. If unset, default value 1 will apply.
    """

    voicemail_option: Optional[VoicemailOption] = None
    """
    If this option is set, the call will try to detect voicemail in the first 3
    minutes of the call. Actions defined (hangup, or leave a message) will be
    applied when the voicemail is detected. Set this to null to disable voicemail
    detection.
    """

    volume: Optional[float] = None
    """If set, will control the volume of the agent.

    Value ranging from [0,2]. Lower value means quieter agent speech, while higher
    value means louder agent speech. If unset, default value 1 will apply.
    """

    webhook_events: Optional[
        List[
            Literal[
                "call_started",
                "call_ended",
                "call_analyzed",
                "transcript_updated",
                "transfer_started",
                "transfer_bridged",
                "transfer_cancelled",
                "transfer_ended",
            ]
        ]
    ] = None
    """Which webhook events this agent should receive.

    If not set, defaults to call_started, call_ended, call_analyzed.
    """

    webhook_timeout_ms: Optional[int] = None
    """The timeout for the webhook in milliseconds.

    If not set, default value of 10000 will apply.
    """

    webhook_url: Optional[str] = None
    """The webhook for agent to listen to call events.

    See what events it would get at [webhook doc](/features/webhook). If set, will
    binds webhook events for this agent to the specified url, and will ignore the
    account level webhook for this agent. Set to `null` to remove webhook url from
    this agent.
    """
