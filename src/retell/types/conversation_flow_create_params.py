# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ConversationFlowCreateParams",
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
    "Component",
    "ComponentNode",
    "ComponentNodeConversationNode",
    "ComponentNodeConversationNodeInstruction",
    "ComponentNodeConversationNodeInstructionNodeInstructionPrompt",
    "ComponentNodeConversationNodeInstructionNodeInstructionStaticText",
    "ComponentNodeConversationNodeDisplayPosition",
    "ComponentNodeConversationNodeEdge",
    "ComponentNodeConversationNodeEdgeTransitionCondition",
    "ComponentNodeConversationNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeConversationNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeConversationNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeConversationNodeFinetuneConversationExample",
    "ComponentNodeConversationNodeFinetuneConversationExampleTranscript",
    "ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember0",
    "ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember1",
    "ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember2",
    "ComponentNodeConversationNodeFinetuneTransitionExample",
    "ComponentNodeConversationNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeConversationNodeGlobalNodeSetting",
    "ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeConversationNodeModelChoice",
    "ComponentNodeConversationNodeSkipResponseEdge",
    "ComponentNodeConversationNodeSkipResponseEdgeTransitionCondition",
    "ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionPromptCondition",
    "ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionEquationCondition",
    "ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionUnionMember2",
    "ComponentNodeEndNode",
    "ComponentNodeEndNodeDisplayPosition",
    "ComponentNodeEndNodeGlobalNodeSetting",
    "ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeEndNodeInstruction",
    "ComponentNodeEndNodeInstructionNodeInstructionPrompt",
    "ComponentNodeEndNodeInstructionNodeInstructionStaticText",
    "ComponentNodeFunctionNode",
    "ComponentNodeFunctionNodeDisplayPosition",
    "ComponentNodeFunctionNodeEdge",
    "ComponentNodeFunctionNodeEdgeTransitionCondition",
    "ComponentNodeFunctionNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeFunctionNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeFunctionNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeFunctionNodeFinetuneTransitionExample",
    "ComponentNodeFunctionNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeFunctionNodeGlobalNodeSetting",
    "ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeFunctionNodeInstruction",
    "ComponentNodeFunctionNodeInstructionNodeInstructionPrompt",
    "ComponentNodeFunctionNodeInstructionNodeInstructionStaticText",
    "ComponentNodeFunctionNodeModelChoice",
    "ComponentNodeTransferCallNode",
    "ComponentNodeTransferCallNodeEdge",
    "ComponentNodeTransferCallNodeEdgeTransitionCondition",
    "ComponentNodeTransferCallNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeTransferCallNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeTransferCallNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeTransferCallNodeEdgeTransitionConditionUnionMember2",
    "ComponentNodeTransferCallNodeTransferDestination",
    "ComponentNodeTransferCallNodeTransferDestinationTransferDestinationPredefined",
    "ComponentNodeTransferCallNodeTransferDestinationTransferDestinationInferred",
    "ComponentNodeTransferCallNodeTransferOption",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionColdTransfer",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransfer",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferIvrOption",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransfer",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "ComponentNodeTransferCallNodeDisplayPosition",
    "ComponentNodeTransferCallNodeGlobalNodeSetting",
    "ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeTransferCallNodeInstruction",
    "ComponentNodeTransferCallNodeInstructionNodeInstructionPrompt",
    "ComponentNodeTransferCallNodeInstructionNodeInstructionStaticText",
    "ComponentNodeTransferCallNodeModelChoice",
    "ComponentNodePressDigitNode",
    "ComponentNodePressDigitNodeInstruction",
    "ComponentNodePressDigitNodeDisplayPosition",
    "ComponentNodePressDigitNodeEdge",
    "ComponentNodePressDigitNodeEdgeTransitionCondition",
    "ComponentNodePressDigitNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodePressDigitNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodePressDigitNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodePressDigitNodeFinetuneTransitionExample",
    "ComponentNodePressDigitNodeFinetuneTransitionExampleTranscript",
    "ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodePressDigitNodeGlobalNodeSetting",
    "ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodePressDigitNodeModelChoice",
    "ComponentNodeBranchNode",
    "ComponentNodeBranchNodeElseEdge",
    "ComponentNodeBranchNodeElseEdgeTransitionCondition",
    "ComponentNodeBranchNodeElseEdgeTransitionConditionPromptCondition",
    "ComponentNodeBranchNodeElseEdgeTransitionConditionEquationCondition",
    "ComponentNodeBranchNodeElseEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeBranchNodeElseEdgeTransitionConditionUnionMember2",
    "ComponentNodeBranchNodeDisplayPosition",
    "ComponentNodeBranchNodeEdge",
    "ComponentNodeBranchNodeEdgeTransitionCondition",
    "ComponentNodeBranchNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeBranchNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeBranchNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeBranchNodeFinetuneTransitionExample",
    "ComponentNodeBranchNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeBranchNodeGlobalNodeSetting",
    "ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeSMSNode",
    "ComponentNodeSMSNodeFailedEdge",
    "ComponentNodeSMSNodeFailedEdgeTransitionCondition",
    "ComponentNodeSMSNodeFailedEdgeTransitionConditionPromptCondition",
    "ComponentNodeSMSNodeFailedEdgeTransitionConditionEquationCondition",
    "ComponentNodeSMSNodeFailedEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeSMSNodeFailedEdgeTransitionConditionUnionMember2",
    "ComponentNodeSMSNodeInstruction",
    "ComponentNodeSMSNodeInstructionNodeInstructionPrompt",
    "ComponentNodeSMSNodeInstructionNodeInstructionStaticText",
    "ComponentNodeSMSNodeSuccessEdge",
    "ComponentNodeSMSNodeSuccessEdgeTransitionCondition",
    "ComponentNodeSMSNodeSuccessEdgeTransitionConditionPromptCondition",
    "ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationCondition",
    "ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeSMSNodeSuccessEdgeTransitionConditionUnionMember2",
    "ComponentNodeSMSNodeDisplayPosition",
    "ComponentNodeSMSNodeGlobalNodeSetting",
    "ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeExtractDynamicVariablesNode",
    "ComponentNodeExtractDynamicVariablesNodeVariable",
    "ComponentNodeExtractDynamicVariablesNodeVariableStringAnalysisData",
    "ComponentNodeExtractDynamicVariablesNodeVariableEnumAnalysisData",
    "ComponentNodeExtractDynamicVariablesNodeVariableBooleanAnalysisData",
    "ComponentNodeExtractDynamicVariablesNodeVariableNumberAnalysisData",
    "ComponentNodeExtractDynamicVariablesNodeDisplayPosition",
    "ComponentNodeExtractDynamicVariablesNodeEdge",
    "ComponentNodeExtractDynamicVariablesNodeEdgeTransitionCondition",
    "ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExample",
    "ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSetting",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeExtractDynamicVariablesNodeModelChoice",
    "ComponentNodeAgentSwapNode",
    "ComponentNodeAgentSwapNodeEdge",
    "ComponentNodeAgentSwapNodeEdgeTransitionCondition",
    "ComponentNodeAgentSwapNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeAgentSwapNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeAgentSwapNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeAgentSwapNodeEdgeTransitionConditionUnionMember2",
    "ComponentNodeAgentSwapNodeDisplayPosition",
    "ComponentNodeAgentSwapNodeGlobalNodeSetting",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeAgentSwapNodeInstruction",
    "ComponentNodeAgentSwapNodeInstructionNodeInstructionPrompt",
    "ComponentNodeAgentSwapNodeInstructionNodeInstructionStaticText",
    "ComponentNodeMcpNode",
    "ComponentNodeMcpNodeDisplayPosition",
    "ComponentNodeMcpNodeEdge",
    "ComponentNodeMcpNodeEdgeTransitionCondition",
    "ComponentNodeMcpNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeMcpNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeMcpNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeMcpNodeFinetuneTransitionExample",
    "ComponentNodeMcpNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeMcpNodeGlobalNodeSetting",
    "ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeMcpNodeInstruction",
    "ComponentNodeMcpNodeInstructionNodeInstructionPrompt",
    "ComponentNodeMcpNodeInstructionNodeInstructionStaticText",
    "ComponentNodeComponentNode",
    "ComponentNodeComponentNodeElseEdge",
    "ComponentNodeComponentNodeElseEdgeTransitionCondition",
    "ComponentNodeComponentNodeElseEdgeTransitionConditionPromptCondition",
    "ComponentNodeComponentNodeElseEdgeTransitionConditionEquationCondition",
    "ComponentNodeComponentNodeElseEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeComponentNodeElseEdgeTransitionConditionUnionMember2",
    "ComponentNodeComponentNodeDisplayPosition",
    "ComponentNodeComponentNodeEdge",
    "ComponentNodeComponentNodeEdgeTransitionCondition",
    "ComponentNodeComponentNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeComponentNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeComponentNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeComponentNodeGlobalNodeSetting",
    "ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeBridgeTransferNode",
    "ComponentNodeBridgeTransferNodeDisplayPosition",
    "ComponentNodeBridgeTransferNodeGlobalNodeSetting",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeCancelTransferNode",
    "ComponentNodeCancelTransferNodeDisplayPosition",
    "ComponentNodeCancelTransferNodeGlobalNodeSetting",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentBeginTagDisplayPosition",
    "ComponentMcp",
    "ComponentTool",
    "ComponentToolConversationFlowCustomTool",
    "ComponentToolConversationFlowCustomToolParameters",
    "ComponentToolCheckAvailabilityCalTool",
    "ComponentToolBookAppointmentCalTool",
    "KBConfig",
    "Mcp",
    "Tool",
    "ToolConversationFlowCustomTool",
    "ToolConversationFlowCustomToolParameters",
    "ToolCheckAvailabilityCalTool",
    "ToolBookAppointmentCalTool",
]


class ConversationFlowCreateParams(TypedDict, total=False):
    model_choice: Required[ModelChoice]
    """The model choice for the conversation flow."""

    nodes: Required[Iterable[Node]]
    """Array of nodes in the conversation flow."""

    start_speaker: Required[Literal["user", "agent"]]
    """Who starts the conversation - user or agent."""

    begin_after_user_silence_ms: Optional[int]
    """
    If set, the AI will begin the conversation after waiting for the user for the
    duration (in milliseconds) specified by this attribute. This only applies if the
    agent is configured to wait for the user to speak first. If not set, the agent
    will wait indefinitely for the user to speak.
    """

    begin_tag_display_position: Optional[BeginTagDisplayPosition]
    """Display position for the begin tag in the frontend."""

    components: Optional[Iterable[Component]]
    """Local components embedded within the conversation flow."""

    default_dynamic_variables: Optional[Dict[str, str]]
    """
    Default dynamic variables that can be referenced throughout the conversation
    flow.
    """

    global_prompt: Optional[str]
    """Global prompt used in every node of the conversation flow."""

    is_transfer_llm: Optional[bool]
    """Whether this conversation flow is used for transfer LLM."""

    kb_config: KBConfig
    """Knowledge base configuration for RAG retrieval."""

    knowledge_base_ids: Optional[SequenceNotStr[str]]
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    mcps: Optional[Iterable[Mcp]]
    """A list of MCP server configurations to use for this conversation flow."""

    model_temperature: Optional[float]
    """Controls the randomness of the model's responses.

    Lower values make responses more deterministic.
    """

    start_node_id: Optional[str]
    """ID of the start node in the conversation flow."""

    tool_call_strict_mode: Optional[bool]
    """Whether to use strict mode for tool calls.

    Only applicable when using certain supported models.
    """

    tools: Optional[Iterable[Tool]]
    """Tools available in the conversation flow."""


class ModelChoice(TypedDict, total=False):
    """The model choice for the conversation flow."""

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
    """Display position for the begin tag in the frontend."""

    x: float

    y: float


class ComponentNodeConversationNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeConversationNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


ComponentNodeConversationNodeInstruction: TypeAlias = Union[
    ComponentNodeConversationNodeInstructionNodeInstructionPrompt,
    ComponentNodeConversationNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeConversationNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeConversationNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeConversationNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeConversationNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeConversationNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeConversationNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeConversationNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeConversationNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeConversationNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeConversationNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeConversationNodeFinetuneConversationExampleTranscript: TypeAlias = Union[
    ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember0,
    ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember1,
    ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember2,
]


class ComponentNodeConversationNodeFinetuneConversationExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodeConversationNodeFinetuneConversationExampleTranscript]]
    """The example transcript to finetune how the conversation should be."""


class ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeConversationNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeConversationNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodeConversationNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeConversationNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeConversationNodeModelChoice(TypedDict, total=False):
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


class ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Skip response"]
    """Must be "Skip response" for skip response edge"""


class ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Skip response"]]
    """Must be "Skip response" for skip response edge"""

    type: Required[Literal["prompt"]]


ComponentNodeConversationNodeSkipResponseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionPromptCondition,
    ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionEquationCondition,
    ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeConversationNodeSkipResponseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeConversationNodeSkipResponseEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeConversationNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    instruction: Required[ComponentNodeConversationNodeInstruction]

    type: Required[Literal["conversation"]]
    """Type of the node"""

    display_position: ComponentNodeConversationNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[ComponentNodeConversationNodeEdge]

    finetune_conversation_examples: Iterable[ComponentNodeConversationNodeFinetuneConversationExample]

    finetune_transition_examples: Iterable[ComponentNodeConversationNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodeConversationNodeGlobalNodeSetting

    interruption_sensitivity: Optional[float]

    knowledge_base_ids: Optional[SequenceNotStr[str]]
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    model_choice: ComponentNodeConversationNodeModelChoice

    name: str
    """Optional name for display purposes"""

    skip_response_edge: ComponentNodeConversationNodeSkipResponseEdge


class ComponentNodeEndNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeEndNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeEndNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeEndNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


ComponentNodeEndNodeInstruction: TypeAlias = Union[
    ComponentNodeEndNodeInstructionNodeInstructionPrompt, ComponentNodeEndNodeInstructionNodeInstructionStaticText
]


class ComponentNodeEndNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["end"]]
    """Type of the node"""

    display_position: ComponentNodeEndNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: ComponentNodeEndNodeGlobalNodeSetting

    instruction: ComponentNodeEndNodeInstruction
    """What to say when ending the call, only used when speak during execution"""

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """If true, will speak during execution"""


class ComponentNodeFunctionNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeFunctionNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeFunctionNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeFunctionNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeFunctionNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeFunctionNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeFunctionNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeFunctionNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeFunctionNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeFunctionNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeFunctionNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeFunctionNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodeFunctionNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeFunctionNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeFunctionNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeFunctionNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


ComponentNodeFunctionNodeInstruction: TypeAlias = Union[
    ComponentNodeFunctionNodeInstructionNodeInstructionPrompt,
    ComponentNodeFunctionNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeFunctionNodeModelChoice(TypedDict, total=False):
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


class ComponentNodeFunctionNode(TypedDict, total=False):
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

    display_position: ComponentNodeFunctionNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[ComponentNodeFunctionNodeEdge]

    finetune_transition_examples: Iterable[ComponentNodeFunctionNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodeFunctionNodeGlobalNodeSetting

    instruction: ComponentNodeFunctionNodeInstruction

    interruption_sensitivity: Optional[float]

    model_choice: ComponentNodeFunctionNodeModelChoice

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """Whether to speak during tool execution"""


class ComponentNodeTransferCallNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeTransferCallNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeTransferCallNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeTransferCallNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Transfer failed"]
    """Must be "Transfer failed" for transfer failed edge"""


class ComponentNodeTransferCallNodeEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Transfer failed"]]
    """Must be "Transfer failed" for transfer failed edge"""

    type: Required[Literal["prompt"]]


ComponentNodeTransferCallNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeTransferCallNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeTransferCallNodeEdgeTransitionConditionEquationCondition,
    ComponentNodeTransferCallNodeEdgeTransitionConditionUnionMember2,
]


class ComponentNodeTransferCallNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeTransferCallNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeTransferCallNodeTransferDestinationTransferDestinationPredefined(TypedDict, total=False):
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


class ComponentNodeTransferCallNodeTransferDestinationTransferDestinationInferred(TypedDict, total=False):
    prompt: Required[str]
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Required[Literal["inferred"]]
    """The type of transfer destination."""


ComponentNodeTransferCallNodeTransferDestination: TypeAlias = Union[
    ComponentNodeTransferCallNodeTransferDestinationTransferDestinationPredefined,
    ComponentNodeTransferCallNodeTransferDestinationTransferDestinationInferred,
]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionColdTransfer(TypedDict, total=False):
    type: Required[Literal["cold_transfer"]]
    """The type of the transfer."""

    show_transferee_as_caller: bool
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferIvrOption(TypedDict, total=False):
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption: TypeAlias = Union[
    ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt,
    ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption: TypeAlias = Union[
    ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt,
    ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransfer(TypedDict, total=False):
    type: Required[Literal["warm_transfer"]]
    """The type of the transfer."""

    agent_detection_timeout_ms: float
    """The time to wait before considering transfer fails."""

    enable_bridge_audio_cue: bool
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    ivr_option: ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferIvrOption
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

    private_handoff_option: ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption
    """
    If set, when transfer is connected, will say the handoff message only to the
    agent receiving the transfer. Can leave either a static message or a dynamic one
    based on prompt. Set to null to disable warm handoff.
    """

    public_handoff_option: ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption
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


class ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent(
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


class ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig(
    TypedDict, total=False
):
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    action_on_timeout: Literal["bridge_transfer", "cancel_transfer"]
    """The action to take when the transfer agent times out without making a decision.

    Defaults to cancel_transfer.
    """

    transfer_agent: (
        ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent
    )
    """The agent that will mediate the transfer decision."""

    transfer_timeout_ms: float
    """
    The maximum time to wait for the transfer agent to make a decision, in
    milliseconds. Defaults to 30000 (30 seconds).
    """


class ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption: TypeAlias = Union[
    ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt,
    ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransfer(TypedDict, total=False):
    agentic_transfer_config: Required[
        ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig
    ]
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    type: Required[Literal["agentic_warm_transfer"]]
    """The type of the transfer."""

    enable_bridge_audio_cue: bool
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    on_hold_music: Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]
    """The music to play while the caller is being transferred."""

    public_handoff_option: (
        ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption
    )
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


ComponentNodeTransferCallNodeTransferOption: TypeAlias = Union[
    ComponentNodeTransferCallNodeTransferOptionTransferOptionColdTransfer,
    ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransfer,
    ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransfer,
]


class ComponentNodeTransferCallNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeTransferCallNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeTransferCallNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeTransferCallNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


ComponentNodeTransferCallNodeInstruction: TypeAlias = Union[
    ComponentNodeTransferCallNodeInstructionNodeInstructionPrompt,
    ComponentNodeTransferCallNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeTransferCallNodeModelChoice(TypedDict, total=False):
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


class ComponentNodeTransferCallNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    edge: Required[ComponentNodeTransferCallNodeEdge]

    transfer_destination: Required[ComponentNodeTransferCallNodeTransferDestination]

    transfer_option: Required[ComponentNodeTransferCallNodeTransferOption]

    type: Required[Literal["transfer_call"]]
    """Type of the node"""

    custom_sip_headers: Dict[str, str]
    """Custom SIP headers for transfer calls"""

    display_position: ComponentNodeTransferCallNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: ComponentNodeTransferCallNodeGlobalNodeSetting

    ignore_e164_validation: bool
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    instruction: ComponentNodeTransferCallNodeInstruction
    """What to say when transferring the call, only used when speak during execution"""

    model_choice: ComponentNodeTransferCallNodeModelChoice

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """If true, will speak during execution"""


class ComponentNodePressDigitNodeInstruction(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodePressDigitNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodePressDigitNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodePressDigitNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodePressDigitNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodePressDigitNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodePressDigitNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodePressDigitNodeEdgeTransitionConditionPromptCondition,
    ComponentNodePressDigitNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodePressDigitNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodePressDigitNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodePressDigitNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodePressDigitNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodePressDigitNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodePressDigitNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodePressDigitNodeModelChoice(TypedDict, total=False):
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


class ComponentNodePressDigitNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    instruction: Required[ComponentNodePressDigitNodeInstruction]

    type: Required[Literal["press_digit"]]
    """Type of the node"""

    delay_ms: int
    """Delay in milliseconds before pressing the digit"""

    display_position: ComponentNodePressDigitNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[ComponentNodePressDigitNodeEdge]

    finetune_transition_examples: Iterable[ComponentNodePressDigitNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodePressDigitNodeGlobalNodeSetting

    model_choice: ComponentNodePressDigitNodeModelChoice

    name: str
    """Optional name for display purposes"""


class ComponentNodeBranchNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeBranchNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeBranchNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeBranchNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class ComponentNodeBranchNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


ComponentNodeBranchNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeBranchNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeBranchNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeBranchNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeBranchNodeElseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeBranchNodeElseEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeBranchNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeBranchNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeBranchNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeBranchNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeBranchNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeBranchNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeBranchNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeBranchNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeBranchNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeBranchNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeBranchNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeBranchNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodeBranchNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeBranchNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeBranchNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    else_edge: Required[ComponentNodeBranchNodeElseEdge]

    type: Required[Literal["branch"]]
    """Type of the node"""

    display_position: ComponentNodeBranchNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[ComponentNodeBranchNodeEdge]

    finetune_transition_examples: Iterable[ComponentNodeBranchNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodeBranchNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class ComponentNodeSMSNodeFailedEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeSMSNodeFailedEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSMSNodeFailedEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeSMSNodeFailedEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Failed to send"]
    """Must be "failed to send" for SMS failed edge"""


class ComponentNodeSMSNodeFailedEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Failed to send"]]
    """Must be "failed to send" for SMS failed edge"""

    type: Required[Literal["prompt"]]


ComponentNodeSMSNodeFailedEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeSMSNodeFailedEdgeTransitionConditionPromptCondition,
    ComponentNodeSMSNodeFailedEdgeTransitionConditionEquationCondition,
    ComponentNodeSMSNodeFailedEdgeTransitionConditionUnionMember2,
]


class ComponentNodeSMSNodeFailedEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeSMSNodeFailedEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeSMSNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeSMSNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


ComponentNodeSMSNodeInstruction: TypeAlias = Union[
    ComponentNodeSMSNodeInstructionNodeInstructionPrompt, ComponentNodeSMSNodeInstructionNodeInstructionStaticText
]


class ComponentNodeSMSNodeSuccessEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Sent successfully"]
    """Must be "sent successfully" for SMS success edge"""


class ComponentNodeSMSNodeSuccessEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Sent successfully"]]
    """Must be "sent successfully" for SMS success edge"""

    type: Required[Literal["prompt"]]


ComponentNodeSMSNodeSuccessEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeSMSNodeSuccessEdgeTransitionConditionPromptCondition,
    ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationCondition,
    ComponentNodeSMSNodeSuccessEdgeTransitionConditionUnionMember2,
]


class ComponentNodeSMSNodeSuccessEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeSMSNodeSuccessEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeSMSNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeSMSNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeSMSNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    failed_edge: Required[ComponentNodeSMSNodeFailedEdge]

    instruction: Required[ComponentNodeSMSNodeInstruction]

    success_edge: Required[ComponentNodeSMSNodeSuccessEdge]

    type: Required[Literal["sms"]]
    """Type of the node"""

    display_position: ComponentNodeSMSNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: ComponentNodeSMSNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class ComponentNodeExtractDynamicVariablesNodeVariableStringAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["string"]]
    """Type of the variable to extract."""

    examples: SequenceNotStr[str]
    """Examples of the variable value to teach model the style and syntax."""


class ComponentNodeExtractDynamicVariablesNodeVariableEnumAnalysisData(TypedDict, total=False):
    choices: Required[SequenceNotStr[str]]
    """The possible values of the variable, must be non empty array."""

    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["enum"]]
    """Type of the variable to extract."""


class ComponentNodeExtractDynamicVariablesNodeVariableBooleanAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["boolean"]]
    """Type of the variable to extract."""


class ComponentNodeExtractDynamicVariablesNodeVariableNumberAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["number"]]
    """Type of the variable to extract."""


ComponentNodeExtractDynamicVariablesNodeVariable: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeVariableStringAnalysisData,
    ComponentNodeExtractDynamicVariablesNodeVariableEnumAnalysisData,
    ComponentNodeExtractDynamicVariablesNodeVariableBooleanAnalysisData,
    ComponentNodeExtractDynamicVariablesNodeVariableNumberAnalysisData,
]


class ComponentNodeExtractDynamicVariablesNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeExtractDynamicVariablesNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeExtractDynamicVariablesNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeExtractDynamicVariablesNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[
        Iterable[ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    ]
    """Find tune the transition condition to this global node"""


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[
        Iterable[ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    ]
    """Find tune the transition condition to this global node"""


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[
        ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExample
    ]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[
        ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExample
    ]
    """Transition to this node"""


class ComponentNodeExtractDynamicVariablesNodeModelChoice(TypedDict, total=False):
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


class ComponentNodeExtractDynamicVariablesNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["extract_dynamic_variables"]]
    """Type of the node"""

    variables: Required[Iterable[ComponentNodeExtractDynamicVariablesNodeVariable]]

    display_position: ComponentNodeExtractDynamicVariablesNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[ComponentNodeExtractDynamicVariablesNodeEdge]

    finetune_transition_examples: Iterable[ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodeExtractDynamicVariablesNodeGlobalNodeSetting

    model_choice: ComponentNodeExtractDynamicVariablesNodeModelChoice

    name: str
    """Optional name for display purposes"""


class ComponentNodeAgentSwapNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeAgentSwapNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeAgentSwapNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeAgentSwapNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Transfer failed"]
    """Must be "Transfer failed" for transfer failed edge"""


class ComponentNodeAgentSwapNodeEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Transfer failed"]]
    """Must be "Transfer failed" for transfer failed edge"""

    type: Required[Literal["prompt"]]


ComponentNodeAgentSwapNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeAgentSwapNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeAgentSwapNodeEdgeTransitionConditionEquationCondition,
    ComponentNodeAgentSwapNodeEdgeTransitionConditionUnionMember2,
]


class ComponentNodeAgentSwapNodeEdge(TypedDict, total=False):
    """Edge to transition to if agent swap fails"""

    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeAgentSwapNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeAgentSwapNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeAgentSwapNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeAgentSwapNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeAgentSwapNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


ComponentNodeAgentSwapNodeInstruction: TypeAlias = Union[
    ComponentNodeAgentSwapNodeInstructionNodeInstructionPrompt,
    ComponentNodeAgentSwapNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeAgentSwapNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    agent_id: Required[str]
    """The ID of the agent to swap to"""

    edge: Required[ComponentNodeAgentSwapNodeEdge]
    """Edge to transition to if agent swap fails"""

    post_call_analysis_setting: Required[Literal["both_agents", "only_destination_agent"]]
    """Post call analysis setting for the agent swap"""

    type: Required[Literal["agent_swap"]]
    """Type of the node"""

    agent_version: float
    """The version of the agent to swap to.

    If not specified, will use the latest version
    """

    display_position: ComponentNodeAgentSwapNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: ComponentNodeAgentSwapNodeGlobalNodeSetting

    instruction: ComponentNodeAgentSwapNodeInstruction
    """What to say when swapping agents, only used when speak during execution"""

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """If true, will speak during execution"""

    webhook_setting: Literal["both_agents", "only_destination_agent", "only_source_agent"]
    """Webhook setting for the agent swap, defaults to only source."""


class ComponentNodeMcpNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeMcpNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeMcpNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeMcpNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeMcpNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeMcpNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeMcpNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeMcpNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeMcpNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeMcpNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeMcpNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeMcpNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodeMcpNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeMcpNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeMcpNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeMcpNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


ComponentNodeMcpNodeInstruction: TypeAlias = Union[
    ComponentNodeMcpNodeInstructionNodeInstructionPrompt, ComponentNodeMcpNodeInstructionNodeInstructionStaticText
]


class ComponentNodeMcpNode(TypedDict, total=False):
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

    display_position: ComponentNodeMcpNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[ComponentNodeMcpNodeEdge]

    finetune_transition_examples: Iterable[ComponentNodeMcpNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodeMcpNodeGlobalNodeSetting

    instruction: ComponentNodeMcpNodeInstruction
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


class ComponentNodeComponentNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeComponentNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeComponentNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeComponentNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class ComponentNodeComponentNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


ComponentNodeComponentNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeComponentNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeComponentNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeComponentNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeComponentNodeElseEdge(TypedDict, total=False):
    """Default edge when no other conditions are met"""

    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeComponentNodeElseEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeComponentNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeComponentNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeComponentNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeComponentNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeComponentNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeComponentNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeComponentNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeComponentNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeComponentNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeComponentNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeComponentNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeComponentNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    component_id: Required[str]
    """The reference ID of the component"""

    component_type: Required[Literal["local", "shared"]]
    """Type of component:

    - local: stored in conversation flow's components array
    - shared: stored in stand-alone conversation-flow-component table
    """

    else_edge: Required[ComponentNodeComponentNodeElseEdge]
    """Default edge when no other conditions are met"""

    type: Required[Literal["component"]]
    """Type of the node"""

    display_position: ComponentNodeComponentNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[ComponentNodeComponentNodeEdge]
    """Array of edges for conditional transitions"""

    global_node_setting: ComponentNodeComponentNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class ComponentNodeBridgeTransferNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeBridgeTransferNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeBridgeTransferNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["bridge_transfer"]]
    """Type of the node - initiates a warm transfer by bridging the call"""

    display_position: ComponentNodeBridgeTransferNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: ComponentNodeBridgeTransferNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class ComponentNodeCancelTransferNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(
    TypedDict, total=False
):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(
    TypedDict, total=False
):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeCancelTransferNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Iterable[ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeCancelTransferNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["cancel_transfer"]]
    """Type of the node - cancels the warm transfer and ends the transfer agent call"""

    display_position: ComponentNodeCancelTransferNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: ComponentNodeCancelTransferNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


ComponentNode: TypeAlias = Union[
    ComponentNodeConversationNode,
    ComponentNodeEndNode,
    ComponentNodeFunctionNode,
    ComponentNodeTransferCallNode,
    ComponentNodePressDigitNode,
    ComponentNodeBranchNode,
    ComponentNodeSMSNode,
    ComponentNodeExtractDynamicVariablesNode,
    ComponentNodeAgentSwapNode,
    ComponentNodeMcpNode,
    ComponentNodeComponentNode,
    ComponentNodeBridgeTransferNode,
    ComponentNodeCancelTransferNode,
]


class ComponentBeginTagDisplayPosition(TypedDict, total=False):
    """Display position for the begin tag in the frontend"""

    x: float

    y: float


class ComponentMcp(TypedDict, total=False):
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


class ComponentToolConversationFlowCustomToolParameters(TypedDict, total=False):
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


class ComponentToolConversationFlowCustomTool(TypedDict, total=False):
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

    parameters: ComponentToolConversationFlowCustomToolParameters
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


class ComponentToolCheckAvailabilityCalTool(TypedDict, total=False):
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


class ComponentToolBookAppointmentCalTool(TypedDict, total=False):
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


ComponentTool: TypeAlias = Union[
    ComponentToolConversationFlowCustomTool, ComponentToolCheckAvailabilityCalTool, ComponentToolBookAppointmentCalTool
]


class Component(TypedDict, total=False):
    name: Required[str]
    """Name of the component"""

    nodes: Required[Iterable[ComponentNode]]
    """Nodes that make up the component"""

    begin_tag_display_position: Optional[ComponentBeginTagDisplayPosition]
    """Display position for the begin tag in the frontend"""

    mcps: Optional[Iterable[ComponentMcp]]
    """A list of MCP server configurations to use for this component"""

    start_node_id: Optional[str]
    """ID of the starting node"""

    tools: Optional[Iterable[ComponentTool]]
    """Tools available within the component"""


class KBConfig(TypedDict, total=False):
    """Knowledge base configuration for RAG retrieval."""

    filter_score: float
    """Similarity threshold for filtering search results"""

    top_k: int
    """Max number of knowledge base chunks to retrieve"""


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
