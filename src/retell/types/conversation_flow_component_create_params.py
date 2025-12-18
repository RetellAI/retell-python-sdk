# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ConversationFlowComponentCreateParams",
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
    "NodeEndNodeInstruction",
    "NodeEndNodeInstructionNodeInstructionPrompt",
    "NodeEndNodeInstructionNodeInstructionStaticText",
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
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferIvrOption",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "NodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransfer",
    "NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig",
    "NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent",
    "NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption",
    "NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
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
    "NodeTransferCallNodeInstruction",
    "NodeTransferCallNodeInstructionNodeInstructionPrompt",
    "NodeTransferCallNodeInstructionNodeInstructionStaticText",
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
    "NodeAgentSwapNodeInstruction",
    "NodeAgentSwapNodeInstructionNodeInstructionPrompt",
    "NodeAgentSwapNodeInstructionNodeInstructionStaticText",
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
    "NodeComponentNode",
    "NodeComponentNodeElseEdge",
    "NodeComponentNodeElseEdgeTransitionCondition",
    "NodeComponentNodeElseEdgeTransitionConditionPromptCondition",
    "NodeComponentNodeElseEdgeTransitionConditionEquationCondition",
    "NodeComponentNodeElseEdgeTransitionConditionEquationConditionEquation",
    "NodeComponentNodeElseEdgeTransitionConditionUnionMember2",
    "NodeComponentNodeDisplayPosition",
    "NodeComponentNodeEdge",
    "NodeComponentNodeEdgeTransitionCondition",
    "NodeComponentNodeEdgeTransitionConditionPromptCondition",
    "NodeComponentNodeEdgeTransitionConditionEquationCondition",
    "NodeComponentNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeComponentNodeGlobalNodeSetting",
    "NodeComponentNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeComponentNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeBridgeTransferNode",
    "NodeBridgeTransferNodeDisplayPosition",
    "NodeBridgeTransferNodeGlobalNodeSetting",
    "NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeCancelTransferNode",
    "NodeCancelTransferNodeDisplayPosition",
    "NodeCancelTransferNodeGlobalNodeSetting",
    "NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "BeginTagDisplayPosition",
    "Mcp",
    "Tool",
    "ToolConversationFlowCustomTool",
    "ToolConversationFlowCustomToolParameters",
    "ToolCheckAvailabilityCalTool",
    "ToolBookAppointmentCalTool",
]


class ConversationFlowComponentCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the component"""

    nodes: Required[Iterable[Node]]
    """Nodes that make up the component"""

    begin_tag_display_position: Optional[BeginTagDisplayPosition]
    """Display position for the begin tag in the frontend"""

    mcps: Optional[Iterable[Mcp]]
    """A list of MCP server configurations to use for this component"""

    start_node_id: Optional[str]
    """ID of the starting node"""

    tools: Optional[Iterable[Tool]]
    """Tools available within the component"""


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
    """Position for frontend display"""

    x: float

    y: float


class NodeConversationNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeConversationNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    interruption_sensitivity: Optional[float]

    knowledge_base_ids: Optional[SequenceNotStr[str]]
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    model_choice: NodeConversationNodeModelChoice

    name: str
    """Optional name for display purposes"""

    skip_response_edge: NodeConversationNodeSkipResponseEdge


class NodeEndNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

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


class NodeEndNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeEndNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


NodeEndNodeInstruction: TypeAlias = Union[
    NodeEndNodeInstructionNodeInstructionPrompt, NodeEndNodeInstructionNodeInstructionStaticText
]


class NodeEndNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["end"]]
    """Type of the node"""

    display_position: NodeEndNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: NodeEndNodeGlobalNodeSetting

    instruction: NodeEndNodeInstruction
    """What to say when ending the call, only used when speak during execution"""

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """If true, will speak during execution"""


class NodeFunctionNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodeFunctionNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeFunctionNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    interruption_sensitivity: Optional[float]

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

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    extension: str
    """Extension digits to dial after the main number connects.

    Sent via DTMF. Allow digits, '\\**', '#', or a dynamic variable like
    {{extension}}.
    """


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
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransferIvrOption(TypedDict, total=False):
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


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

    enable_bridge_audio_cue: bool
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    ivr_option: NodeTransferCallNodeTransferOptionTransferOptionWarmTransferIvrOption
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

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

    show_transferee_as_caller: bool
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


class NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent(
    TypedDict, total=False
):
    """The agent that will mediate the transfer decision."""

    agent_id: Required[str]
    """The agent ID of the transfer agent.

    This agent must have isTransferAgent set to true and should use bridge_transfer
    and cancel_transfer tools (for Retell LLM) or BridgeTransferNode and
    CancelTransferNode (for Conversation Flow).
    """

    agent_version: Required[float]
    """The version of the transfer agent to use."""


class NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig(TypedDict, total=False):
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    action_on_timeout: Literal["bridge_transfer", "cancel_transfer"]
    """The action to take when the transfer agent times out without making a decision.

    Defaults to cancel_transfer.
    """

    transfer_agent: (
        NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent
    )
    """The agent that will mediate the transfer decision."""

    transfer_timeout_ms: float
    """
    The maximum time to wait for the transfer agent to make a decision, in
    milliseconds. Defaults to 30000 (30 seconds).
    """


class NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption: TypeAlias = Union[
    NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt,
    NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransfer(TypedDict, total=False):
    agentic_transfer_config: Required[
        NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig
    ]
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    type: Required[Literal["agentic_warm_transfer"]]
    """The type of the transfer."""

    enable_bridge_audio_cue: bool
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    on_hold_music: Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]
    """The music to play while the caller is being transferred."""

    public_handoff_option: NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption
    """
    If set, when transfer is successful, will say the handoff message to both the
    transferee and the agent receiving the transfer. Can leave either a static
    message or a dynamic one based on prompt. Set to null to disable warm handoff.
    """

    show_transferee_as_caller: bool
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


NodeTransferCallNodeTransferOption: TypeAlias = Union[
    NodeTransferCallNodeTransferOptionTransferOptionColdTransfer,
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransfer,
    NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransfer,
]


class NodeTransferCallNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

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


class NodeTransferCallNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeTransferCallNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


NodeTransferCallNodeInstruction: TypeAlias = Union[
    NodeTransferCallNodeInstructionNodeInstructionPrompt, NodeTransferCallNodeInstructionNodeInstructionStaticText
]


class NodeTransferCallNodeModelChoice(TypedDict, total=False):
    model: Required[
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

    ignore_e164_validation: bool
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    instruction: NodeTransferCallNodeInstruction
    """What to say when transferring the call, only used when speak during execution"""

    model_choice: NodeTransferCallNodeModelChoice

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """If true, will speak during execution"""


class NodePressDigitNodeInstruction(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodePressDigitNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodePressDigitNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodePressDigitNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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
    """Position for frontend display"""

    x: float

    y: float


class NodeBranchNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeBranchNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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
    """Position for frontend display"""

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

    examples: SequenceNotStr[str]
    """Examples of the variable value to teach model the style and syntax."""


class NodeExtractDynamicVariablesNodeVariableEnumAnalysisData(TypedDict, total=False):
    choices: Required[SequenceNotStr[str]]
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
    """Position for frontend display"""

    x: float

    y: float


class NodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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
    """Edge to transition to if agent swap fails"""

    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeAgentSwapNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeAgentSwapNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

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


class NodeAgentSwapNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeAgentSwapNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


NodeAgentSwapNodeInstruction: TypeAlias = Union[
    NodeAgentSwapNodeInstructionNodeInstructionPrompt, NodeAgentSwapNodeInstructionNodeInstructionStaticText
]


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

    instruction: NodeAgentSwapNodeInstruction
    """What to say when swapping agents, only used when speak during execution"""

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """If true, will speak during execution"""

    webhook_setting: Literal["both_agents", "only_destination_agent", "only_source_agent"]
    """Webhook setting for the agent swap, defaults to only source."""


class NodeMcpNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodeMcpNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeMcpNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    interruption_sensitivity: Optional[float]

    name: str
    """Optional name for display purposes"""

    response_variables: Dict[str, str]
    """
    Response variables to add to dynamic variables, key is the variable name, value
    is the path to the variable in the response
    """

    speak_during_execution: bool
    """If true, will speak during execution"""


class NodeComponentNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeComponentNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeComponentNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeComponentNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class NodeComponentNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


NodeComponentNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeComponentNodeElseEdgeTransitionConditionPromptCondition,
    NodeComponentNodeElseEdgeTransitionConditionEquationCondition,
    NodeComponentNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeComponentNodeElseEdge(TypedDict, total=False):
    """Default edge when no other conditions are met"""

    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeComponentNodeElseEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeComponentNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodeComponentNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeComponentNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeComponentNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeComponentNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeComponentNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeComponentNodeEdgeTransitionConditionPromptCondition, NodeComponentNodeEdgeTransitionConditionEquationCondition
]


class NodeComponentNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeComponentNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeComponentNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeComponentNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeComponentNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeComponentNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeComponentNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeComponentNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    component_id: Required[str]
    """The reference ID of the component"""

    component_type: Required[Literal["local", "shared"]]
    """Type of component:

    - local: stored in conversation flow's components array
    - shared: stored in stand-alone conversation-flow-component table
    """

    else_edge: Required[NodeComponentNodeElseEdge]
    """Default edge when no other conditions are met"""

    type: Required[Literal["component"]]
    """Type of the node"""

    display_position: NodeComponentNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[NodeComponentNodeEdge]
    """Array of edges for conditional transitions"""

    global_node_setting: NodeComponentNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class NodeBridgeTransferNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeBridgeTransferNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeBridgeTransferNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["bridge_transfer"]]
    """Type of the node - initiates a warm transfer by bridging the call"""

    display_position: NodeBridgeTransferNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: NodeBridgeTransferNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class NodeCancelTransferNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeCancelTransferNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeCancelTransferNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["cancel_transfer"]]
    """Type of the node - cancels the warm transfer and ends the transfer agent call"""

    display_position: NodeCancelTransferNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: NodeCancelTransferNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


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
    NodeComponentNode,
    NodeBridgeTransferNode,
    NodeCancelTransferNode,
]


class BeginTagDisplayPosition(TypedDict, total=False):
    """Display position for the begin tag in the frontend"""

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


class ToolConversationFlowCustomToolParameters(TypedDict, total=False):
    """Tool parameters schema"""

    properties: Required[Dict[str, object]]
    """
    The value of properties is an object, where each key is the name of a property
    and each value is a schema used to validate that property.
    """

    type: Required[Literal["object"]]
    """Type must be "object" for a JSON Schema object."""

    required: SequenceNotStr[str]
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

    args_at_root: bool
    """If true, the tool arguments will be passed at the root level of the request
    body.

    If false, they will be nested under "args".
    """

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
