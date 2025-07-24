# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ConversationFlowResponse",
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


class BeginTagDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


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


class ModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeConversationNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeConversationNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


NodeConversationNodeInstruction: TypeAlias = Union[
    NodeConversationNodeInstructionNodeInstructionPrompt, NodeConversationNodeInstructionNodeInstructionStaticText
]


class NodeConversationNodeDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


class NodeConversationNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeConversationNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeConversationNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeConversationNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeConversationNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeConversationNodeEdgeTransitionConditionPromptCondition,
    NodeConversationNodeEdgeTransitionConditionEquationCondition,
]


class NodeConversationNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeConversationNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeConversationNodeFinetuneConversationExampleTranscript: TypeAlias = Union[
    NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember0,
    NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember1,
    NodeConversationNodeFinetuneConversationExampleTranscriptUnionMember2,
]


class NodeConversationNodeFinetuneConversationExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodeConversationNodeFinetuneConversationExampleTranscript]
    """The example transcript to finetune how the conversation should be."""


class NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeConversationNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeConversationNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodeConversationNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeConversationNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeConversationNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeConversationNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeConversationNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeConversationNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeConversationNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeConversationNodeSkipResponseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeConversationNodeSkipResponseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeConversationNodeSkipResponseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeConversationNodeSkipResponseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Skip response"]] = None
    """Must be "Skip response" for skip response edge"""


class NodeConversationNodeSkipResponseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Skip response"]
    """Must be "Skip response" for skip response edge"""

    type: Literal["prompt"]


NodeConversationNodeSkipResponseEdgeTransitionCondition: TypeAlias = Union[
    NodeConversationNodeSkipResponseEdgeTransitionConditionPromptCondition,
    NodeConversationNodeSkipResponseEdgeTransitionConditionEquationCondition,
    NodeConversationNodeSkipResponseEdgeTransitionConditionUnionMember2,
]


class NodeConversationNodeSkipResponseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeConversationNodeSkipResponseEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeConversationNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    instruction: NodeConversationNodeInstruction

    type: Literal["conversation"]
    """Type of the node"""

    display_position: Optional[NodeConversationNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[NodeConversationNodeEdge]] = None

    finetune_conversation_examples: Optional[List[NodeConversationNodeFinetuneConversationExample]] = None

    finetune_transition_examples: Optional[List[NodeConversationNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodeConversationNodeGlobalNodeSetting] = None

    interruption_sensitivity: Optional[float] = None

    api_model_choice: Optional[NodeConversationNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    skip_response_edge: Optional[NodeConversationNodeSkipResponseEdge] = None


class NodeEndNodeDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


class NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeEndNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeEndNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeEndNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeEndNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeEndNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeEndNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["end"]
    """Type of the node"""

    display_position: Optional[NodeEndNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[NodeEndNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodeFunctionNodeDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


class NodeFunctionNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeFunctionNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeFunctionNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeFunctionNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeFunctionNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeFunctionNodeEdgeTransitionConditionPromptCondition, NodeFunctionNodeEdgeTransitionConditionEquationCondition
]


class NodeFunctionNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeFunctionNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeFunctionNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeFunctionNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodeFunctionNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeFunctionNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeFunctionNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeFunctionNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeFunctionNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeFunctionNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


NodeFunctionNodeInstruction: TypeAlias = Union[
    NodeFunctionNodeInstructionNodeInstructionPrompt, NodeFunctionNodeInstructionNodeInstructionStaticText
]


class NodeFunctionNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeFunctionNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    tool_id: str
    """Tool ID for function nodes"""

    tool_type: Literal["local", "shared"]
    """Tool type for function nodes"""

    type: Literal["function"]
    """Type of the node"""

    wait_for_result: bool
    """Whether to wait for tool result"""

    display_position: Optional[NodeFunctionNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[NodeFunctionNodeEdge]] = None

    finetune_transition_examples: Optional[List[NodeFunctionNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodeFunctionNodeGlobalNodeSetting] = None

    instruction: Optional[NodeFunctionNodeInstruction] = None

    interruption_sensitivity: Optional[float] = None

    api_model_choice: Optional[NodeFunctionNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """Whether to speak during tool execution"""


class NodeTransferCallNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeTransferCallNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeTransferCallNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeTransferCallNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Transfer failed"]] = None
    """Must be "Transfer failed" for transfer failed edge"""


class NodeTransferCallNodeEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Transfer failed"]
    """Must be "Transfer failed" for transfer failed edge"""

    type: Literal["prompt"]


NodeTransferCallNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeTransferCallNodeEdgeTransitionConditionPromptCondition,
    NodeTransferCallNodeEdgeTransitionConditionEquationCondition,
    NodeTransferCallNodeEdgeTransitionConditionUnionMember2,
]


class NodeTransferCallNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeTransferCallNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeTransferCallNodeTransferDestinationTransferDestinationPredefined(BaseModel):
    number: str
    """
    The number to transfer to in E.164 format or a dynamic variable like
    {{transfer_number}}.
    """

    type: Literal["predefined"]
    """The type of transfer destination."""


class NodeTransferCallNodeTransferDestinationTransferDestinationInferred(BaseModel):
    prompt: str
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Literal["inferred"]
    """The type of transfer destination."""


NodeTransferCallNodeTransferDestination: TypeAlias = Union[
    NodeTransferCallNodeTransferDestinationTransferDestinationPredefined,
    NodeTransferCallNodeTransferDestinationTransferDestinationInferred,
]


class NodeTransferCallNodeTransferOptionTransferOptionColdTransfer(BaseModel):
    type: Literal["cold_transfer"]
    """The type of the transfer."""

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support SIP REFER to PSTN. This is
    only applicable for cold transfer, so if warm transfer option is specified, this
    field will be ignored. Default to false (default to show AI agent as caller).
    """


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt(BaseModel):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption: TypeAlias = Union[
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt,
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage,
]


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt(BaseModel):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption: TypeAlias = Union[
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt,
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransfer(BaseModel):
    type: Literal["warm_transfer"]
    """The type of the transfer."""

    agent_detection_timeout_ms: Optional[float] = None
    """The time to wait before considering transfer fails."""

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
        NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption
    ] = None
    """
    If set, when transfer is connected, will say the handoff message only to the
    agent receiving the transfer. Can leave either a static message or a dynamic one
    based on prompt. Set to null to disable warm handoff.
    """

    public_handoff_option: Optional[NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption] = (
        None
    )
    """
    If set, when transfer is successful, will say the handoff message to both the
    transferee and the agent receiving the transfer. Can leave either a static
    message or a dynamic one based on prompt. Set to null to disable warm handoff.
    """


NodeTransferCallNodeTransferOption: TypeAlias = Union[
    NodeTransferCallNodeTransferOptionTransferOptionColdTransfer,
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransfer,
]


class NodeTransferCallNodeDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


class NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeTransferCallNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeTransferCallNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeTransferCallNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    edge: NodeTransferCallNodeEdge

    transfer_destination: NodeTransferCallNodeTransferDestination

    transfer_option: NodeTransferCallNodeTransferOption

    type: Literal["transfer_call"]
    """Type of the node"""

    custom_sip_headers: Optional[Dict[str, str]] = None
    """Custom SIP headers for transfer calls"""

    display_position: Optional[NodeTransferCallNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[NodeTransferCallNodeGlobalNodeSetting] = None

    api_model_choice: Optional[NodeTransferCallNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodePressDigitNodeInstruction(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodePressDigitNodeDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


class NodePressDigitNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodePressDigitNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodePressDigitNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodePressDigitNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodePressDigitNodeEdgeTransitionCondition: TypeAlias = Union[
    NodePressDigitNodeEdgeTransitionConditionPromptCondition, NodePressDigitNodeEdgeTransitionConditionEquationCondition
]


class NodePressDigitNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodePressDigitNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodePressDigitNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodePressDigitNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodePressDigitNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodePressDigitNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodePressDigitNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodePressDigitNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodePressDigitNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodePressDigitNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    instruction: NodePressDigitNodeInstruction

    type: Literal["press_digit"]
    """Type of the node"""

    delay_ms: Optional[int] = None
    """Delay in milliseconds before pressing the digit"""

    display_position: Optional[NodePressDigitNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[NodePressDigitNodeEdge]] = None

    finetune_transition_examples: Optional[List[NodePressDigitNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodePressDigitNodeGlobalNodeSetting] = None

    api_model_choice: Optional[NodePressDigitNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodeBranchNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeBranchNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeBranchNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeBranchNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class NodeBranchNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


NodeBranchNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeBranchNodeElseEdgeTransitionConditionPromptCondition,
    NodeBranchNodeElseEdgeTransitionConditionEquationCondition,
    NodeBranchNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeBranchNodeElseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeBranchNodeElseEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeBranchNodeDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


class NodeBranchNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeBranchNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeBranchNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeBranchNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeBranchNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeBranchNodeEdgeTransitionConditionPromptCondition, NodeBranchNodeEdgeTransitionConditionEquationCondition
]


class NodeBranchNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeBranchNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeBranchNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeBranchNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodeBranchNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeBranchNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeBranchNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeBranchNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeBranchNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeBranchNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeBranchNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    else_edge: NodeBranchNodeElseEdge

    type: Literal["branch"]
    """Type of the node"""

    display_position: Optional[NodeBranchNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[NodeBranchNodeEdge]] = None

    finetune_transition_examples: Optional[List[NodeBranchNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodeBranchNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodeSMSNodeFailedEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeSMSNodeFailedEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeSMSNodeFailedEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeSMSNodeFailedEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Failed to send"]] = None
    """Must be "failed to send" for SMS failed edge"""


class NodeSMSNodeFailedEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Failed to send"]
    """Must be "failed to send" for SMS failed edge"""

    type: Literal["prompt"]


NodeSMSNodeFailedEdgeTransitionCondition: TypeAlias = Union[
    NodeSMSNodeFailedEdgeTransitionConditionPromptCondition,
    NodeSMSNodeFailedEdgeTransitionConditionEquationCondition,
    NodeSMSNodeFailedEdgeTransitionConditionUnionMember2,
]


class NodeSMSNodeFailedEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeSMSNodeFailedEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeSMSNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeSMSNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


NodeSMSNodeInstruction: TypeAlias = Union[
    NodeSMSNodeInstructionNodeInstructionPrompt, NodeSMSNodeInstructionNodeInstructionStaticText
]


class NodeSMSNodeSuccessEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeSMSNodeSuccessEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Sent successfully"]] = None
    """Must be "sent successfully" for SMS success edge"""


class NodeSMSNodeSuccessEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Sent successfully"]
    """Must be "sent successfully" for SMS success edge"""

    type: Literal["prompt"]


NodeSMSNodeSuccessEdgeTransitionCondition: TypeAlias = Union[
    NodeSMSNodeSuccessEdgeTransitionConditionPromptCondition,
    NodeSMSNodeSuccessEdgeTransitionConditionEquationCondition,
    NodeSMSNodeSuccessEdgeTransitionConditionUnionMember2,
]


class NodeSMSNodeSuccessEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeSMSNodeSuccessEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeSMSNodeDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


class NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeSMSNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeSMSNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeSMSNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeSMSNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeSMSNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeSMSNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    failed_edge: NodeSMSNodeFailedEdge

    instruction: NodeSMSNodeInstruction

    success_edge: NodeSMSNodeSuccessEdge

    type: Literal["sms"]
    """Type of the node"""

    display_position: Optional[NodeSMSNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[NodeSMSNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodeExtractDynamicVariablesNodeVariableStringAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["string"]
    """Type of the variable to extract."""

    examples: Optional[List[str]] = None
    """Examples of the variable value to teach model the style and syntax."""


class NodeExtractDynamicVariablesNodeVariableEnumAnalysisData(BaseModel):
    choices: List[str]
    """The possible values of the variable, must be non empty array."""

    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["enum"]
    """Type of the variable to extract."""


class NodeExtractDynamicVariablesNodeVariableBooleanAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["boolean"]
    """Type of the variable to extract."""


class NodeExtractDynamicVariablesNodeVariableNumberAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["number"]
    """Type of the variable to extract."""


NodeExtractDynamicVariablesNodeVariable: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeVariableStringAnalysisData,
    NodeExtractDynamicVariablesNodeVariableEnumAnalysisData,
    NodeExtractDynamicVariablesNodeVariableBooleanAnalysisData,
    NodeExtractDynamicVariablesNodeVariableNumberAnalysisData,
]


class NodeExtractDynamicVariablesNodeDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


class NodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeExtractDynamicVariablesNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition,
    NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationCondition,
]


class NodeExtractDynamicVariablesNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeExtractDynamicVariablesNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeExtractDynamicVariablesNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeExtractDynamicVariablesNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[
        List[NodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExample]
    ] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[
        List[NodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExample]
    ] = None
    """Transition to this node"""


class NodeExtractDynamicVariablesNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeExtractDynamicVariablesNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["extract_dynamic_variables"]
    """Type of the node"""

    variables: List[NodeExtractDynamicVariablesNodeVariable]

    display_position: Optional[NodeExtractDynamicVariablesNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[NodeExtractDynamicVariablesNodeEdge]] = None

    finetune_transition_examples: Optional[List[NodeExtractDynamicVariablesNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodeExtractDynamicVariablesNodeGlobalNodeSetting] = None

    api_model_choice: Optional[NodeExtractDynamicVariablesNodeModelChoice] = FieldInfo(
        alias="model_choice", default=None
    )

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodeAgentSwapNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeAgentSwapNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeAgentSwapNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeAgentSwapNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Transfer failed"]] = None
    """Must be "Transfer failed" for transfer failed edge"""


class NodeAgentSwapNodeEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Transfer failed"]
    """Must be "Transfer failed" for transfer failed edge"""

    type: Literal["prompt"]


NodeAgentSwapNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeAgentSwapNodeEdgeTransitionConditionPromptCondition,
    NodeAgentSwapNodeEdgeTransitionConditionEquationCondition,
    NodeAgentSwapNodeEdgeTransitionConditionUnionMember2,
]


class NodeAgentSwapNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeAgentSwapNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeAgentSwapNodeDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


class NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeAgentSwapNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeAgentSwapNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    agent_id: str
    """The ID of the agent to swap to"""

    edge: NodeAgentSwapNodeEdge
    """Edge to transition to if agent swap fails"""

    post_call_analysis_setting: Literal["both_agents", "only_destination_agent"]
    """Post call analysis setting for the agent swap"""

    type: Literal["agent_swap"]
    """Type of the node"""

    agent_version: Optional[float] = None
    """The version of the agent to swap to.

    If not specified, will use the latest version
    """

    display_position: Optional[NodeAgentSwapNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[NodeAgentSwapNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodeMcpNodeDisplayPosition(BaseModel):
    x: Optional[float] = None

    y: Optional[float] = None


class NodeMcpNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeMcpNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains"]

    right: str
    """Right side of the equation"""


class NodeMcpNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeMcpNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeMcpNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeMcpNodeEdgeTransitionConditionPromptCondition, NodeMcpNodeEdgeTransitionConditionEquationCondition
]


class NodeMcpNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeMcpNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeMcpNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeMcpNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodeMcpNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeMcpNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeMcpNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeMcpNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeMcpNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeMcpNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeMcpNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeMcpNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


NodeMcpNodeInstruction: TypeAlias = Union[
    NodeMcpNodeInstructionNodeInstructionPrompt, NodeMcpNodeInstructionNodeInstructionStaticText
]


class NodeMcpNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    mcp_id: str
    """Unique ID of the MCP server"""

    mcp_tool_name: str
    """Name of the MCP tool to call"""

    type: Literal["mcp"]
    """Type of the node"""

    wait_for_result: bool
    """If true, will wait for result before transitioning to next node"""

    display_position: Optional[NodeMcpNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[NodeMcpNodeEdge]] = None

    finetune_transition_examples: Optional[List[NodeMcpNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodeMcpNodeGlobalNodeSetting] = None

    instruction: Optional[NodeMcpNodeInstruction] = None
    """What to say when calling the function, only used when speak during execution"""

    interruption_sensitivity: Optional[float] = None

    name: Optional[str] = None
    """Optional name for display purposes"""

    response_variables: Optional[Dict[str, str]] = None
    """
    Response variables to add to dynamic variables, key is the variable name, value
    is the path to the variable in the response
    """

    speak_during_execution: Optional[bool] = None
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


class ToolConversationFlowCustomToolParameters(BaseModel):
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


class ToolConversationFlowCustomTool(BaseModel):
    name: str
    """Name of the tool"""

    type: Literal["custom"]
    """Type of the tool"""

    url: str
    """Server URL to call the tool. Dynamic variables can be used in the URL."""

    description: Optional[str] = None
    """Description of the tool"""

    headers: Optional[Dict[str, str]] = None
    """Headers to add to the request"""

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None
    """HTTP method to use for the request, defaults to POST"""

    parameters: Optional[ToolConversationFlowCustomToolParameters] = None
    """Tool parameters schema"""

    query_params: Optional[Dict[str, str]] = None
    """Query parameters to add to the request"""

    response_variables: Optional[Dict[str, str]] = None
    """
    Response variables to add to the dynamic variables, key is the variable name,
    value is the path to the variable in the response
    """

    timeout_ms: Optional[int] = None
    """Timeout in milliseconds for the function call, defaults to 2 min"""

    tool_id: Optional[str] = None
    """Unique identifier for the tool"""


class ToolCheckAvailabilityCalTool(BaseModel):
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

    tool_id: Optional[str] = None
    """Unique identifier for the tool"""


class ToolBookAppointmentCalTool(BaseModel):
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

    tool_id: Optional[str] = None
    """Unique identifier for the tool"""


Tool: TypeAlias = Union[ToolConversationFlowCustomTool, ToolCheckAvailabilityCalTool, ToolBookAppointmentCalTool]


class ConversationFlowResponse(BaseModel):
    conversation_flow_id: str
    """Unique identifier for the conversation flow"""

    version: int
    """Version number of the conversation flow"""

    begin_tag_display_position: Optional[BeginTagDisplayPosition] = None
    """Display position for the begin tag in the frontend."""

    default_dynamic_variables: Optional[Dict[str, str]] = None
    """
    Default dynamic variables that can be referenced throughout the conversation
    flow.
    """

    global_prompt: Optional[str] = None
    """Global prompt used in every node of the conversation flow."""

    knowledge_base_ids: Optional[List[str]] = None
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    mcps: Optional[List[Mcp]] = None
    """A list of MCP server configurations to use for this conversation flow."""

    api_model_choice: Optional[ModelChoice] = FieldInfo(alias="model_choice", default=None)
    """The model choice for the conversation flow."""

    api_model_temperature: Optional[float] = FieldInfo(alias="model_temperature", default=None)
    """Controls the randomness of the model's responses.

    Lower values make responses more deterministic.
    """

    nodes: Optional[List[Node]] = None
    """Array of nodes in the conversation flow."""

    start_node_id: Optional[str] = None
    """ID of the start node in the conversation flow."""

    start_speaker: Optional[Literal["user", "agent"]] = None
    """Who starts the conversation - user or agent."""

    tool_call_strict_mode: Optional[bool] = None
    """Whether to use strict mode for tool calls.

    Only applicable when using structured output models.
    """

    tools: Optional[List[Tool]] = None
    """Tools available in the conversation flow."""
