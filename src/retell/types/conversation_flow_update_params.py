# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ConversationFlowUpdateParams",
    "BeginTagDisplayPosition",
    "Mcp",
    "ModelChoice",
    "Node",
    "NodeConversationNode",
    "NodeConversationNodeInstruction",
    "NodeConversationNodeInstructionNodeInstructionPrompt",
    "NodeConversationNodeInstructionNodeInstructionStaticText",
    "NodeConversationNodeDisplayPosition",
    "NodeConversationNodeEdge",
    "NodeConversationNodeEdgeTransitionCondition",
    "NodeConversationNodeEdgeTransitionConditionPromptCondition",
    "NodeConversationNodeEdgeTransitionConditionEquationCondition",
    "NodeConversationNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeConversationNodeFinetuneConversationExample",
    "NodeConversationNodeFinetuneConversationExampleTranscript",
    "NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember0",
    "NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember1",
    "NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember2",
    "NodeConversationNodeFinetuneTransitionExample",
    "NodeConversationNodeFinetuneTransitionExampleTranscript",
    "NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeConversationNodeGlobalNodeSetting",
    "NodeConversationNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeConversationNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeConversationNodeModelChoice",
    "NodeConversationNodeSkipResponseEdge",
    "NodeConversationNodeSkipResponseEdgeTransitionCondition",
    "NodeConversationNodeSkipResponseEdgeTransitionConditionPromptCondition",
    "NodeConversationNodeSkipResponseEdgeTransitionConditionEquationCondition",
    "NodeConversationNodeSkipResponseEdgeTransitionConditionEquationConditionEquation",
    "NodeConversationNodeSkipResponseEdgeTransitionConditionUnionMember2",
    "NodeEndNode",
    "NodeEndNodeDisplayPosition",
    "NodeEndNodeGlobalNodeSetting",
    "NodeEndNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeEndNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeFunctionNode",
    "NodeFunctionNodeDisplayPosition",
    "NodeFunctionNodeEdge",
    "NodeFunctionNodeEdgeTransitionCondition",
    "NodeFunctionNodeEdgeTransitionConditionPromptCondition",
    "NodeFunctionNodeEdgeTransitionConditionEquationCondition",
    "NodeFunctionNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeFunctionNodeFinetuneTransitionExample",
    "NodeFunctionNodeFinetuneTransitionExampleTranscript",
    "NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeFunctionNodeGlobalNodeSetting",
    "NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeFunctionNodeInstruction",
    "NodeFunctionNodeInstructionNodeInstructionPrompt",
    "NodeFunctionNodeInstructionNodeInstructionStaticText",
    "NodeFunctionNodeModelChoice",
    "NodeTransferCallNode",
    "NodeTransferCallNodeEdge",
    "NodeTransferCallNodeEdgeTransitionCondition",
    "NodeTransferCallNodeEdgeTransitionConditionPromptCondition",
    "NodeTransferCallNodeEdgeTransitionConditionEquationCondition",
    "NodeTransferCallNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeTransferCallNodeEdgeTransitionConditionUnionMember2",
    "NodeTransferCallNodeTransferDestination",
    "NodeTransferCallNodeTransferDestinationTransferDestinationPredefined",
    "NodeTransferCallNodeTransferDestinationTransferDestinationInferred",
    "NodeTransferCallNodeTransferOption",
    "NodeTransferCallNodeTransferOptionTransferOptionColdTransfer",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransfer",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "NodeTransferCallNodeDisplayPosition",
    "NodeTransferCallNodeGlobalNodeSetting",
    "NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeTransferCallNodeModelChoice",
    "NodePressDigitNode",
    "NodePressDigitNodeInstruction",
    "NodePressDigitNodeDisplayPosition",
    "NodePressDigitNodeEdge",
    "NodePressDigitNodeEdgeTransitionCondition",
    "NodePressDigitNodeEdgeTransitionConditionPromptCondition",
    "NodePressDigitNodeEdgeTransitionConditionEquationCondition",
    "NodePressDigitNodeEdgeTransitionConditionEquationConditionEquation",
    "NodePressDigitNodeFinetuneTransitionExample",
    "NodePressDigitNodeFinetuneTransitionExampleTranscript",
    "NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodePressDigitNodeGlobalNodeSetting",
    "NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodePressDigitNodeModelChoice",
    "NodeBranchNode",
    "NodeBranchNodeElseEdge",
    "NodeBranchNodeElseEdgeTransitionCondition",
    "NodeBranchNodeElseEdgeTransitionConditionPromptCondition",
    "NodeBranchNodeElseEdgeTransitionConditionEquationCondition",
    "NodeBranchNodeElseEdgeTransitionConditionEquationConditionEquation",
    "NodeBranchNodeElseEdgeTransitionConditionUnionMember2",
    "NodeBranchNodeDisplayPosition",
    "NodeBranchNodeEdge",
    "NodeBranchNodeEdgeTransitionCondition",
    "NodeBranchNodeEdgeTransitionConditionPromptCondition",
    "NodeBranchNodeEdgeTransitionConditionEquationCondition",
    "NodeBranchNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeBranchNodeFinetuneTransitionExample",
    "NodeBranchNodeFinetuneTransitionExampleTranscript",
    "NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeBranchNodeGlobalNodeSetting",
    "NodeBranchNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeBranchNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeSMSNode",
    "NodeSMSNodeFailedEdge",
    "NodeSMSNodeFailedEdgeTransitionCondition",
    "NodeSMSNodeFailedEdgeTransitionConditionPromptCondition",
    "NodeSMSNodeFailedEdgeTransitionConditionEquationCondition",
    "NodeSMSNodeFailedEdgeTransitionConditionEquationConditionEquation",
    "NodeSMSNodeFailedEdgeTransitionConditionUnionMember2",
    "NodeSMSNodeInstruction",
    "NodeSMSNodeInstructionNodeInstructionPrompt",
    "NodeSMSNodeInstructionNodeInstructionStaticText",
    "NodeSMSNodeSuccessEdge",
    "NodeSMSNodeSuccessEdgeTransitionCondition",
    "NodeSMSNodeSuccessEdgeTransitionConditionPromptCondition",
    "NodeSMSNodeSuccessEdgeTransitionConditionEquationCondition",
    "NodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation",
    "NodeSMSNodeSuccessEdgeTransitionConditionUnionMember2",
    "NodeSMSNodeDisplayPosition",
    "NodeSMSNodeGlobalNodeSetting",
    "NodeSMSNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeSMSNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeExtractDynamicVariablesNode",
    "NodeExtractDynamicVariablesNodeVariable",
    "NodeExtractDynamicVariablesNodeVariableStringAnalysisData",
    "NodeExtractDynamicVariablesNodeVariableEnumAnalysisData",
    "NodeExtractDynamicVariablesNodeVariableBooleanAnalysisData",
    "NodeExtractDynamicVariablesNodeVariableNumberAnalysisData",
    "NodeExtractDynamicVariablesNodeDisplayPosition",
    "NodeExtractDynamicVariablesNodeEdge",
    "NodeExtractDynamicVariablesNodeEdgeTransitionCondition",
    "NodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition",
    "NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationCondition",
    "NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeExtractDynamicVariablesNodeFinetuneTransitionExample",
    "NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript",
    "NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeExtractDynamicVariablesNodeGlobalNodeSetting",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeExtractDynamicVariablesNodeModelChoice",
    "NodeAgentSwapNode",
    "NodeAgentSwapNodeEdge",
    "NodeAgentSwapNodeEdgeTransitionCondition",
    "NodeAgentSwapNodeEdgeTransitionConditionPromptCondition",
    "NodeAgentSwapNodeEdgeTransitionConditionEquationCondition",
    "NodeAgentSwapNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeAgentSwapNodeEdgeTransitionConditionUnionMember2",
    "NodeAgentSwapNodeDisplayPosition",
    "NodeAgentSwapNodeGlobalNodeSetting",
    "NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeMcpNode",
    "NodeMcpNodeDisplayPosition",
    "NodeMcpNodeEdge",
    "NodeMcpNodeEdgeTransitionCondition",
    "NodeMcpNodeEdgeTransitionConditionPromptCondition",
    "NodeMcpNodeEdgeTransitionConditionEquationCondition",
    "NodeMcpNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeMcpNodeFinetuneTransitionExample",
    "NodeMcpNodeFinetuneTransitionExampleTranscript",
    "NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeMcpNodeGlobalNodeSetting",
    "NodeMcpNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeMcpNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeMcpNodeInstruction",
    "NodeMcpNodeInstructionNodeInstructionPrompt",
    "NodeMcpNodeInstructionNodeInstructionStaticText",
    "Tool",
    "ToolConversationFlowCustomTool",
    "ToolConversationFlowCustomToolParameters",
    "ToolCheckAvailabilityCalTool",
    "ToolBookAppointmentCalTool",
]


class ConversationFlowUpdateParams(TypedDict, total=False):
    version: str
    """Version of the conversation flow to update"""

    begin_tag_display_position: Optional[BeginTagDisplayPosition]
    """Display position for the begin tag in the frontend."""

    default_dynamic_variables: Optional[Dict[str, str]]
    """
    Default dynamic variables that can be referenced throughout the conversation
    flow.
    """

    global_prompt: Optional[str]
    """Global prompt used in every node of the conversation flow."""

    knowledge_base_ids: Optional[List[str]]
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    mcps: Optional[Iterable[Mcp]]
    """A list of MCP server configurations to use for this conversation flow."""

    model_choice: ModelChoice
    """The model choice for the conversation flow."""

    model_temperature: Optional[float]
    """Controls the randomness of the model's responses.

    Lower values make responses more deterministic.
    """

    nodes: Iterable[Node]
    """Array of nodes in the conversation flow."""

    start_node_id: Optional[str]
    """ID of the start node in the conversation flow."""

    start_speaker: Literal["user", "agent"]
    """Who starts the conversation - user or agent."""

    tool_call_strict_mode: Optional[bool]
    """Whether to use strict mode for tool calls.

    Only applicable when using structured output models.
    """

    tools: Optional[Iterable[Tool]]
    """Tools available in the conversation flow."""


class BeginTagDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class Mcp(TypedDict, total=False):
    name: Required[str]

    url: Required[str]
    """The URL of the MCP server."""

    headers: Dict[str, str]
    """Headers to add to the MCP connection request."""

    query_params: Dict[str, str]
    """Query parameters to append to the MCP connection request URL."""

    timeout_ms: int
    """Maximum time to wait for a connection to be established (in milliseconds).

    Default to 120,000 ms (2 minutes).
    """


class ModelChoice(TypedDict, total=False):
    model: Required[
        Literal[
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "claude-3.7-sonnet",
            "claude-3.5-haiku",
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeConversationNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeConversationNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


NodeConversationNodeInstruction: TypeAlias = Union[
    NodeConversationNodeInstructionNodeInstructionPrompt, NodeConversationNodeInstructionNodeInstructionStaticText
]


class NodeConversationNodeDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class NodeConversationNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeConversationNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeConversationNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeConversationNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeConversationNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeConversationNodeEdgeTransitionConditionPromptCondition,
    NodeConversationNodeEdgeTransitionConditionEquationCondition,
]


class NodeConversationNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeConversationNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeConversationNodeFinetuneConversationExampleTranscript: TypeAlias = Union[
    NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember0,
    NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember1,
    NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember2,
]


class NodeConversationNodeFinetuneConversationExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodeConversationNodeFinetuneConversationExampleTranscript]]
    """The example transcript to finetune how the conversation should be."""


class NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeConversationNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeConversationNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodeConversationNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeConversationNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeConversationNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeConversationNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeConversationNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeConversationNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeConversationNodeModelChoice(TypedDict, total=False):
    model: Required[
        Literal[
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "claude-3.7-sonnet",
            "claude-3.5-haiku",
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeConversationNodeSkipResponseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeConversationNodeSkipResponseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeConversationNodeSkipResponseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeConversationNodeSkipResponseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Skip response"]
    """Must be "Skip response" for skip response edge"""


class NodeConversationNodeSkipResponseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Skip response"]]
    """Must be "Skip response" for skip response edge"""

    type: Required[Literal["prompt"]]


NodeConversationNodeSkipResponseEdgeTransitionCondition: TypeAlias = Union[
    NodeConversationNodeSkipResponseEdgeTransitionConditionPromptCondition,
    NodeConversationNodeSkipResponseEdgeTransitionConditionEquationCondition,
    NodeConversationNodeSkipResponseEdgeTransitionConditionUnionMember2,
]


class NodeConversationNodeSkipResponseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeConversationNodeSkipResponseEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeConversationNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    instruction: Required[NodeConversationNodeInstruction]

    type: Required[Literal["conversation"]]
    """Type of the node"""

    display_position: NodeConversationNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[NodeConversationNodeEdge]

    finetune_conversation_examples: Iterable[NodeConversationNodeFinetuneConversationExample]

    finetune_transition_examples: Iterable[NodeConversationNodeFinetuneTransitionExample]

    global_node_setting: NodeConversationNodeGlobalNodeSetting

    interruption_sensitivity: float

    model_choice: NodeConversationNodeModelChoice

    name: str
    """Optional name for display purposes"""

    skip_response_edge: NodeConversationNodeSkipResponseEdge


class NodeEndNodeDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeEndNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeEndNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeEndNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeEndNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeEndNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeEndNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["end"]]
    """Type of the node"""

    display_position: NodeEndNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: NodeEndNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class NodeFunctionNodeDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class NodeFunctionNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeFunctionNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeFunctionNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeFunctionNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeFunctionNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeFunctionNodeEdgeTransitionConditionPromptCondition, NodeFunctionNodeEdgeTransitionConditionEquationCondition
]


class NodeFunctionNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeFunctionNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeFunctionNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeFunctionNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodeFunctionNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeFunctionNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeFunctionNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeFunctionNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


NodeFunctionNodeInstruction: TypeAlias = Union[
    NodeFunctionNodeInstructionNodeInstructionPrompt, NodeFunctionNodeInstructionNodeInstructionStaticText
]


class NodeFunctionNodeModelChoice(TypedDict, total=False):
    model: Required[
        Literal[
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "claude-3.7-sonnet",
            "claude-3.5-haiku",
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeFunctionNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    tool_id: Required[str]
    """Tool ID for function nodes"""

    tool_type: Required[Literal["local", "shared"]]
    """Tool type for function nodes"""

    type: Required[Literal["function"]]
    """Type of the node"""

    wait_for_result: Required[bool]
    """Whether to wait for tool result"""

    display_position: NodeFunctionNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[NodeFunctionNodeEdge]

    finetune_transition_examples: Iterable[NodeFunctionNodeFinetuneTransitionExample]

    global_node_setting: NodeFunctionNodeGlobalNodeSetting

    instruction: NodeFunctionNodeInstruction

    interruption_sensitivity: float

    model_choice: NodeFunctionNodeModelChoice

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """Whether to speak during tool execution"""


class NodeTransferCallNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeTransferCallNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeTransferCallNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeTransferCallNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Transfer failed"]
    """Must be "Transfer failed" for transfer failed edge"""


class NodeTransferCallNodeEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Transfer failed"]]
    """Must be "Transfer failed" for transfer failed edge"""

    type: Required[Literal["prompt"]]


NodeTransferCallNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeTransferCallNodeEdgeTransitionConditionPromptCondition,
    NodeTransferCallNodeEdgeTransitionConditionEquationCondition,
    NodeTransferCallNodeEdgeTransitionConditionUnionMember2,
]


class NodeTransferCallNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeTransferCallNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeTransferCallNodeTransferDestinationTransferDestinationPredefined(TypedDict, total=False):
    number: Required[str]
    """
    The number to transfer to in E.164 format or a dynamic variable like
    {{transfer_number}}.
    """

    type: Required[Literal["predefined"]]
    """The type of transfer destination."""


class NodeTransferCallNodeTransferDestinationTransferDestinationInferred(TypedDict, total=False):
    prompt: Required[str]
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Required[Literal["inferred"]]
    """The type of transfer destination."""


NodeTransferCallNodeTransferDestination: TypeAlias = Union[
    NodeTransferCallNodeTransferDestinationTransferDestinationPredefined,
    NodeTransferCallNodeTransferDestinationTransferDestinationInferred,
]


class NodeTransferCallNodeTransferOptionTransferOptionColdTransfer(TypedDict, total=False):
    type: Required[Literal["cold_transfer"]]
    """The type of the transfer."""

    show_transferee_as_caller: bool
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support SIP REFER to PSTN. This is
    only applicable for cold transfer, so if warm transfer option is specified, this
    field will be ignored. Default to false (default to show AI agent as caller).
    """


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption: TypeAlias = Union[
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt,
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage,
]


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption: TypeAlias = Union[
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt,
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransfer(TypedDict, total=False):
    type: Required[Literal["warm_transfer"]]
    """The type of the transfer."""

    agent_detection_timeout_ms: float
    """The time to wait before considering transfer fails."""

    on_hold_music: Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]
    """The music to play while the caller is being transferred."""

    opt_out_human_detection: bool
    """If set to true, will not perform human detection for the transfer.

    Default to false.
    """

    opt_out_initial_message: bool
    """If set to true, AI will not say "Hello" after connecting the call.

    Default to false.
    """

    private_handoff_option: NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption
    """
    If set, when transfer is connected, will say the handoff message only to the
    agent receiving the transfer. Can leave either a static message or a dynamic one
    based on prompt. Set to null to disable warm handoff.
    """

    public_handoff_option: NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption
    """
    If set, when transfer is successful, will say the handoff message to both the
    transferee and the agent receiving the transfer. Can leave either a static
    message or a dynamic one based on prompt. Set to null to disable warm handoff.
    """


NodeTransferCallNodeTransferOption: TypeAlias = Union[
    NodeTransferCallNodeTransferOptionTransferOptionColdTransfer,
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransfer,
]


class NodeTransferCallNodeDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeTransferCallNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeTransferCallNodeModelChoice(TypedDict, total=False):
    model: Required[
        Literal[
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "claude-3.7-sonnet",
            "claude-3.5-haiku",
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeTransferCallNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    edge: Required[NodeTransferCallNodeEdge]

    transfer_destination: Required[NodeTransferCallNodeTransferDestination]

    transfer_option: Required[NodeTransferCallNodeTransferOption]

    type: Required[Literal["transfer_call"]]
    """Type of the node"""

    custom_sip_headers: Dict[str, str]
    """Custom SIP headers for transfer calls"""

    display_position: NodeTransferCallNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: NodeTransferCallNodeGlobalNodeSetting

    model_choice: NodeTransferCallNodeModelChoice

    name: str
    """Optional name for display purposes"""


class NodePressDigitNodeInstruction(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodePressDigitNodeDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class NodePressDigitNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodePressDigitNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodePressDigitNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodePressDigitNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodePressDigitNodeEdgeTransitionCondition: TypeAlias = Union[
    NodePressDigitNodeEdgeTransitionConditionPromptCondition, NodePressDigitNodeEdgeTransitionConditionEquationCondition
]


class NodePressDigitNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodePressDigitNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodePressDigitNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodePressDigitNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodePressDigitNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodePressDigitNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodePressDigitNodeModelChoice(TypedDict, total=False):
    model: Required[
        Literal[
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "claude-3.7-sonnet",
            "claude-3.5-haiku",
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodePressDigitNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    instruction: Required[NodePressDigitNodeInstruction]

    type: Required[Literal["press_digit"]]
    """Type of the node"""

    delay_ms: int
    """Delay in milliseconds before pressing the digit"""

    display_position: NodePressDigitNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[NodePressDigitNodeEdge]

    finetune_transition_examples: Iterable[NodePressDigitNodeFinetuneTransitionExample]

    global_node_setting: NodePressDigitNodeGlobalNodeSetting

    model_choice: NodePressDigitNodeModelChoice

    name: str
    """Optional name for display purposes"""


class NodeBranchNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeBranchNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeBranchNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeBranchNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class NodeBranchNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


NodeBranchNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeBranchNodeElseEdgeTransitionConditionPromptCondition,
    NodeBranchNodeElseEdgeTransitionConditionEquationCondition,
    NodeBranchNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeBranchNodeElseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeBranchNodeElseEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeBranchNodeDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class NodeBranchNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeBranchNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeBranchNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeBranchNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeBranchNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeBranchNodeEdgeTransitionConditionPromptCondition, NodeBranchNodeEdgeTransitionConditionEquationCondition
]


class NodeBranchNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeBranchNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeBranchNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeBranchNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodeBranchNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeBranchNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeBranchNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeBranchNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeBranchNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeBranchNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeBranchNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    else_edge: Required[NodeBranchNodeElseEdge]

    type: Required[Literal["branch"]]
    """Type of the node"""

    display_position: NodeBranchNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[NodeBranchNodeEdge]

    finetune_transition_examples: Iterable[NodeBranchNodeFinetuneTransitionExample]

    global_node_setting: NodeBranchNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class NodeSMSNodeFailedEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeSMSNodeFailedEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeSMSNodeFailedEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeSMSNodeFailedEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Failed to send"]
    """Must be "failed to send" for SMS failed edge"""


class NodeSMSNodeFailedEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Failed to send"]]
    """Must be "failed to send" for SMS failed edge"""

    type: Required[Literal["prompt"]]


NodeSMSNodeFailedEdgeTransitionCondition: TypeAlias = Union[
    NodeSMSNodeFailedEdgeTransitionConditionPromptCondition,
    NodeSMSNodeFailedEdgeTransitionConditionEquationCondition,
    NodeSMSNodeFailedEdgeTransitionConditionUnionMember2,
]


class NodeSMSNodeFailedEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeSMSNodeFailedEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeSMSNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeSMSNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


NodeSMSNodeInstruction: TypeAlias = Union[
    NodeSMSNodeInstructionNodeInstructionPrompt, NodeSMSNodeInstructionNodeInstructionStaticText
]


class NodeSMSNodeSuccessEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeSMSNodeSuccessEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Sent successfully"]
    """Must be "sent successfully" for SMS success edge"""


class NodeSMSNodeSuccessEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Sent successfully"]]
    """Must be "sent successfully" for SMS success edge"""

    type: Required[Literal["prompt"]]


NodeSMSNodeSuccessEdgeTransitionCondition: TypeAlias = Union[
    NodeSMSNodeSuccessEdgeTransitionConditionPromptCondition,
    NodeSMSNodeSuccessEdgeTransitionConditionEquationCondition,
    NodeSMSNodeSuccessEdgeTransitionConditionUnionMember2,
]


class NodeSMSNodeSuccessEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeSMSNodeSuccessEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeSMSNodeDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeSMSNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeSMSNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeSMSNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeSMSNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeSMSNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeSMSNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    failed_edge: Required[NodeSMSNodeFailedEdge]

    instruction: Required[NodeSMSNodeInstruction]

    success_edge: Required[NodeSMSNodeSuccessEdge]

    type: Required[Literal["sms"]]
    """Type of the node"""

    display_position: NodeSMSNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: NodeSMSNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class NodeExtractDynamicVariablesNodeVariableStringAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["string"]]
    """Type of the variable to extract."""

    examples: List[str]
    """Examples of the variable value to teach model the style and syntax."""


class NodeExtractDynamicVariablesNodeVariableEnumAnalysisData(TypedDict, total=False):
    choices: Required[List[str]]
    """The possible values of the variable, must be non empty array."""

    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["enum"]]
    """Type of the variable to extract."""


class NodeExtractDynamicVariablesNodeVariableBooleanAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["boolean"]]
    """Type of the variable to extract."""


class NodeExtractDynamicVariablesNodeVariableNumberAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["number"]]
    """Type of the variable to extract."""


NodeExtractDynamicVariablesNodeVariable: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeVariableStringAnalysisData,
    NodeExtractDynamicVariablesNodeVariableEnumAnalysisData,
    NodeExtractDynamicVariablesNodeVariableBooleanAnalysisData,
    NodeExtractDynamicVariablesNodeVariableNumberAnalysisData,
]


class NodeExtractDynamicVariablesNodeDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class NodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeExtractDynamicVariablesNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition,
    NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationCondition,
]


class NodeExtractDynamicVariablesNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeExtractDynamicVariablesNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeExtractDynamicVariablesNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeExtractDynamicVariablesNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeExtractDynamicVariablesNodeModelChoice(TypedDict, total=False):
    model: Required[
        Literal[
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "claude-3.7-sonnet",
            "claude-3.5-haiku",
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeExtractDynamicVariablesNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["extract_dynamic_variables"]]
    """Type of the node"""

    variables: Required[Iterable[NodeExtractDynamicVariablesNodeVariable]]

    display_position: NodeExtractDynamicVariablesNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[NodeExtractDynamicVariablesNodeEdge]

    finetune_transition_examples: Iterable[NodeExtractDynamicVariablesNodeFinetuneTransitionExample]

    global_node_setting: NodeExtractDynamicVariablesNodeGlobalNodeSetting

    model_choice: NodeExtractDynamicVariablesNodeModelChoice

    name: str
    """Optional name for display purposes"""


class NodeAgentSwapNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeAgentSwapNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeAgentSwapNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeAgentSwapNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Transfer failed"]
    """Must be "Transfer failed" for transfer failed edge"""


class NodeAgentSwapNodeEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Transfer failed"]]
    """Must be "Transfer failed" for transfer failed edge"""

    type: Required[Literal["prompt"]]


NodeAgentSwapNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeAgentSwapNodeEdgeTransitionConditionPromptCondition,
    NodeAgentSwapNodeEdgeTransitionConditionEquationCondition,
    NodeAgentSwapNodeEdgeTransitionConditionUnionMember2,
]


class NodeAgentSwapNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeAgentSwapNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeAgentSwapNodeDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeAgentSwapNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeAgentSwapNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    agent_id: Required[str]
    """The ID of the agent to swap to"""

    edge: Required[NodeAgentSwapNodeEdge]
    """Edge to transition to if agent swap fails"""

    post_call_analysis_setting: Required[Literal["both_agents", "only_destination_agent"]]
    """Post call analysis setting for the agent swap"""

    type: Required[Literal["agent_swap"]]
    """Type of the node"""

    agent_version: float
    """The version of the agent to swap to.

    If not specified, will use the latest version
    """

    display_position: NodeAgentSwapNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: NodeAgentSwapNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class NodeMcpNodeDisplayPosition(TypedDict, total=False):
    x: float

    y: float


class NodeMcpNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeMcpNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]]

    right: Required[str]
    """Right side of the equation"""


class NodeMcpNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeMcpNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeMcpNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeMcpNodeEdgeTransitionConditionPromptCondition, NodeMcpNodeEdgeTransitionConditionEquationCondition
]


class NodeMcpNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeMcpNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeMcpNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeMcpNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodeMcpNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeMcpNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeMcpNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeMcpNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeMcpNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeMcpNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeMcpNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeMcpNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


NodeMcpNodeInstruction: TypeAlias = Union[
    NodeMcpNodeInstructionNodeInstructionPrompt, NodeMcpNodeInstructionNodeInstructionStaticText
]


class NodeMcpNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    mcp_id: Required[str]
    """Unique ID of the MCP server"""

    mcp_tool_name: Required[str]
    """Name of the MCP tool to call"""

    type: Required[Literal["mcp"]]
    """Type of the node"""

    wait_for_result: Required[bool]
    """If true, will wait for result before transitioning to next node"""

    display_position: NodeMcpNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[NodeMcpNodeEdge]

    finetune_transition_examples: Iterable[NodeMcpNodeFinetuneTransitionExample]

    global_node_setting: NodeMcpNodeGlobalNodeSetting

    instruction: NodeMcpNodeInstruction
    """What to say when calling the function, only used when speak during execution"""

    interruption_sensitivity: float

    name: str
    """Optional name for display purposes"""

    response_variables: Dict[str, str]
    """
    Response variables to add to dynamic variables, key is the variable name, value
    is the path to the variable in the response
    """

    speak_during_execution: bool
    """If true, will speak during execution"""


Node: TypeAlias = Union[
    NodeConversationNode,
    NodeEndNode,
    NodeFunctionNode,
    NodeTransferCallNode,
    NodePressDigitNode,
    NodeBranchNode,
    NodeSMSNode,
    NodeExtractDynamicVariablesNode,
    NodeAgentSwapNode,
    NodeMcpNode,
]


class ToolConversationFlowCustomToolParameters(TypedDict, total=False):
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


class ToolConversationFlowCustomTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool"""

    type: Required[Literal["custom"]]
    """Type of the tool"""

    url: Required[str]
    """Server URL to call the tool. Dynamic variables can be used in the URL."""

    description: str
    """Description of the tool"""

    headers: Dict[str, str]
    """Headers to add to the request"""

    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
    """HTTP method to use for the request, defaults to POST"""

    parameters: ToolConversationFlowCustomToolParameters
    """Tool parameters schema"""

    query_params: Dict[str, str]
    """Query parameters to add to the request"""

    response_variables: Dict[str, str]
    """
    Response variables to add to the dynamic variables, key is the variable name,
    value is the path to the variable in the response
    """

    timeout_ms: int
    """Timeout in milliseconds for the function call, defaults to 2 min"""

    tool_id: str
    """Unique identifier for the tool"""


class ToolCheckAvailabilityCalTool(TypedDict, total=False):
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

    tool_id: str
    """Unique identifier for the tool"""


class ToolBookAppointmentCalTool(TypedDict, total=False):
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

    tool_id: str
    """Unique identifier for the tool"""


Tool: TypeAlias = Union[ToolConversationFlowCustomTool, ToolCheckAvailabilityCalTool, ToolBookAppointmentCalTool]
