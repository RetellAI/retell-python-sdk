# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ChatAgentResponse",
    "ResponseEngine",
    "ResponseEngineResponseEngineRetellLm",
    "ResponseEngineResponseEngineCustomLm",
    "ResponseEngineResponseEngineConversationFlow",
    "ContactMemoryConfig",
    "GuardrailConfig",
    "HandbookConfig",
    "PiiConfig",
    "PostChatAnalysisData",
    "PostChatAnalysisDataStringAnalysisData",
    "PostChatAnalysisDataEnumAnalysisData",
    "PostChatAnalysisDataBooleanAnalysisData",
    "PostChatAnalysisDataNumberAnalysisData",
    "PostChatAnalysisDataChatPresetAnalysisData",
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
    """Toggle behavior presets on/off to influence agent response style and behaviors.

    Voice-only presets are not available for chat agents.
    """

    ai_disclosure: Optional[bool] = None
    """When asked, acknowledge being a virtual assistant."""

    default_personality: Optional[bool] = None
    """Professional call center rep baseline."""

    high_empathy: Optional[bool] = None
    """Warm acknowledgment of caller concerns."""

    scope_boundaries: Optional[bool] = None
    """Stay within prompt/context scope, don't invent details."""


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


class PostChatAnalysisDataStringAnalysisData(BaseModel):
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


class PostChatAnalysisDataEnumAnalysisData(BaseModel):
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


class PostChatAnalysisDataBooleanAnalysisData(BaseModel):
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


class PostChatAnalysisDataNumberAnalysisData(BaseModel):
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


class PostChatAnalysisDataChatPresetAnalysisData(BaseModel):
    """System preset for post-chat analysis (chat agents).

    Use in post_chat_analysis_data to override prompts or mark fields optional.
    """

    name: Literal["chat_summary", "chat_successful", "user_sentiment"]
    """Preset identifier for chat agent analysis."""

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


PostChatAnalysisData: TypeAlias = Union[
    PostChatAnalysisDataStringAnalysisData,
    PostChatAnalysisDataEnumAnalysisData,
    PostChatAnalysisDataBooleanAnalysisData,
    PostChatAnalysisDataNumberAnalysisData,
    PostChatAnalysisDataChatPresetAnalysisData,
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


class ChatAgentResponse(BaseModel):
    agent_id: str
    """Unique id of chat agent."""

    last_modification_timestamp: int
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    response_engine: ResponseEngine
    """The Response Engine to attach to the agent.

    It is used to generate responses for the agent. You need to create a Response
    Engine first before attaching it to an agent.
    """

    agent_name: Optional[str] = None
    """The name of the chat agent. Only used for your own reference."""

    assigned_tags: Optional[List[str]] = None
    """Tags assigned to this chat agent version. Preferred tag is listed first."""

    auto_close_message: Optional[str] = None
    """Message to display when the chat is automatically closed."""

    base_version: Optional[int] = None
    """Version that this draft was based on. Null for initial versions."""

    contact_memory_config: Optional[ContactMemoryConfig] = None
    """Contact memory settings for phone calls and SMS chats.

    Creating an agent defaults enable_update to false and enable_read to true.
    Updates only change the supplied flags; omitted flags stay unchanged and an
    empty object has no effect. Set a flag to false to disable it. The configuration
    cannot be cleared. Existing agents without this configuration have both
    disabled.
    """

    data_storage_retention_days: Optional[int] = None
    """Number of days to retain call/chat data before automatic deletion.

    Must be between 1 and 730 days. If not set, data is retained forever (no
    automatic deletion).
    """

    data_storage_setting: Optional[Literal["everything", "everything_except_pii", "basic_attributes_only"]] = None
    """Controls what data is stored for this agent.

    "everything" stores all data including transcripts and recordings.
    "everything_except_pii" stores data but excludes PII when possible based on PII
    configuration. "basic_attributes_only" stores only basic metadata. If not set,
    defaults to "everything".
    """

    end_chat_after_silence_ms: Optional[int] = None
    """If users stay silent for a period after agent speech, end the chat.

    The minimum value allowed is 120,000 ms (2 minutes). The maximum value allowed
    is 259,200,000 ms (72 hours). By default, this is set to 3,600,000 (1 hour).
    """

    guardrail_config: Optional[GuardrailConfig] = None
    """
    Configuration for guardrail checks to detect and prevent prohibited topics in
    agent output and user input.
    """

    handbook_config: Optional[HandbookConfig] = None
    """Toggle behavior presets on/off to influence agent response style and behaviors.

    Voice-only presets are not available for chat agents.
    """

    is_published: Optional[bool] = None
    """Whether the chat agent is published."""

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

    opt_in_signed_url: Optional[bool] = None
    """Whether this agent opts in to signed url for public log.

    If not set, default value of false will apply.
    """

    pii_config: Optional[PiiConfig] = None
    """Configuration for PII scrubbing from transcripts and recordings."""

    post_chat_analysis_data: Optional[List[PostChatAnalysisData]] = None
    """Post chat analysis data to extract from the chat.

    This data will augment the pre-defined variables extracted in the chat analysis.
    This will be available after the chat ends.
    """

    post_chat_analysis_model: Optional[
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
    """The model to use for post chat analysis. Default to gpt-5.6-terra."""

    post_session_tools: Optional[List[PostSessionTool]] = None
    """
    Integration (Agent Functions) tools run as a dependency graph at chat end, after
    post-chat analysis. Each tool can be gated by a condition. Set to null to clear.
    """

    pre_session_tools: Optional[List[PreSessionTool]] = None
    """
    Integration (Agent Functions) tools run as a dependency graph before the chat's
    first message. Outputs are injected as dynamic variables. Set to null to clear.
    """

    signed_url_expiration_ms: Optional[int] = None
    """The expiration time for the signed url in milliseconds.

    Only applicable when opt_in_signed_url is true. If not set, default value of
    86400000 (24 hours) will apply.
    """

    timezone: Optional[str] = None
    """IANA timezone for the agent (e.g.

    America/New_York). Defaults to America/Los_Angeles if not set.
    """

    version: Optional[int] = None
    """The version of the chat agent."""

    version_title: Optional[str] = None
    """Optional title of the chat agent version. Used for your own reference."""

    webhook_events: Optional[List[Literal["chat_started", "chat_ended", "chat_analyzed", "transcript_updated"]]] = None
    """Which webhook events this agent should receive.

    If not set, defaults to chat_started, chat_ended, chat_analyzed.
    """

    webhook_timeout_ms: Optional[int] = None
    """The timeout for the webhook in milliseconds.

    If not set, default value of 10000 will apply.
    """

    webhook_url: Optional[str] = None
    """The webhook for agent to listen to chat events.

    See what events it would get at [webhook doc](/features/webhook). If set, will
    binds webhook events for this agent to the specified url, and will ignore the
    account level webhook for this agent. Set to `null` to remove webhook url from
    this agent.
    """
