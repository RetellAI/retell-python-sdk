# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ConversationFlowResponse",
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
    "Tool",
    "ToolConversationFlowCustomTool",
    "ToolConversationFlowCustomToolParameters",
    "ToolCheckAvailabilityCalTool",
    "ToolBookAppointmentCalTool",
]


class BeginTagDisplayPosition(BaseModel):
    """Display position for the begin tag in the frontend."""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeConversationNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeConversationNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


ComponentNodeConversationNodeInstruction: TypeAlias = Union[
    ComponentNodeConversationNodeInstructionNodeInstructionPrompt,
    ComponentNodeConversationNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeConversationNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeConversationNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeConversationNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeConversationNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeConversationNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeConversationNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeConversationNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeConversationNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeConversationNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeConversationNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeConversationNodeFinetuneConversationExampleTranscript: TypeAlias = Union[
    ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember0,
    ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember1,
    ComponentNodeConversationNodeFinetuneConversationExampleTranscriptUnionMember2,
]


class ComponentNodeConversationNodeFinetuneConversationExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodeConversationNodeFinetuneConversationExampleTranscript]
    """The example transcript to finetune how the conversation should be."""


class ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeConversationNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeConversationNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeConversationNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodeConversationNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeConversationNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[
        List[ComponentNodeConversationNodeGlobalNodeSettingNegativeFinetuneExample]
    ] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[
        List[ComponentNodeConversationNodeGlobalNodeSettingPositiveFinetuneExample]
    ] = None
    """Transition to this node"""


class ComponentNodeConversationNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Skip response"]] = None
    """Must be "Skip response" for skip response edge"""


class ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Skip response"]
    """Must be "Skip response" for skip response edge"""

    type: Literal["prompt"]


ComponentNodeConversationNodeSkipResponseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionPromptCondition,
    ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionEquationCondition,
    ComponentNodeConversationNodeSkipResponseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeConversationNodeSkipResponseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeConversationNodeSkipResponseEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeConversationNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    instruction: ComponentNodeConversationNodeInstruction

    type: Literal["conversation"]
    """Type of the node"""

    display_position: Optional[ComponentNodeConversationNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[ComponentNodeConversationNodeEdge]] = None

    finetune_conversation_examples: Optional[List[ComponentNodeConversationNodeFinetuneConversationExample]] = None

    finetune_transition_examples: Optional[List[ComponentNodeConversationNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[ComponentNodeConversationNodeGlobalNodeSetting] = None

    interruption_sensitivity: Optional[float] = None

    knowledge_base_ids: Optional[List[str]] = None
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    api_model_choice: Optional[ComponentNodeConversationNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    skip_response_edge: Optional[ComponentNodeConversationNodeSkipResponseEdge] = None


class ComponentNodeEndNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeEndNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[ComponentNodeEndNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeEndNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class ComponentNodeEndNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeEndNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


ComponentNodeEndNodeInstruction: TypeAlias = Union[
    ComponentNodeEndNodeInstructionNodeInstructionPrompt, ComponentNodeEndNodeInstructionNodeInstructionStaticText
]


class ComponentNodeEndNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["end"]
    """Type of the node"""

    display_position: Optional[ComponentNodeEndNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[ComponentNodeEndNodeGlobalNodeSetting] = None

    instruction: Optional[ComponentNodeEndNodeInstruction] = None
    """What to say when ending the call, only used when speak during execution"""

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution"""


class ComponentNodeFunctionNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeFunctionNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeFunctionNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeFunctionNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeFunctionNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeFunctionNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeFunctionNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeFunctionNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeFunctionNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeFunctionNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeFunctionNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeFunctionNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodeFunctionNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeFunctionNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[ComponentNodeFunctionNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeFunctionNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class ComponentNodeFunctionNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeFunctionNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


ComponentNodeFunctionNodeInstruction: TypeAlias = Union[
    ComponentNodeFunctionNodeInstructionNodeInstructionPrompt,
    ComponentNodeFunctionNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeFunctionNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeFunctionNode(BaseModel):
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

    display_position: Optional[ComponentNodeFunctionNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[ComponentNodeFunctionNodeEdge]] = None

    finetune_transition_examples: Optional[List[ComponentNodeFunctionNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[ComponentNodeFunctionNodeGlobalNodeSetting] = None

    instruction: Optional[ComponentNodeFunctionNodeInstruction] = None

    interruption_sensitivity: Optional[float] = None

    api_model_choice: Optional[ComponentNodeFunctionNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """Whether to speak during tool execution"""


class ComponentNodeTransferCallNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeTransferCallNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeTransferCallNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeTransferCallNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Transfer failed"]] = None
    """Must be "Transfer failed" for transfer failed edge"""


class ComponentNodeTransferCallNodeEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Transfer failed"]
    """Must be "Transfer failed" for transfer failed edge"""

    type: Literal["prompt"]


ComponentNodeTransferCallNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeTransferCallNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeTransferCallNodeEdgeTransitionConditionEquationCondition,
    ComponentNodeTransferCallNodeEdgeTransitionConditionUnionMember2,
]


class ComponentNodeTransferCallNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeTransferCallNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeTransferCallNodeTransferDestinationTransferDestinationPredefined(BaseModel):
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


class ComponentNodeTransferCallNodeTransferDestinationTransferDestinationInferred(BaseModel):
    prompt: str
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Literal["inferred"]
    """The type of transfer destination."""


ComponentNodeTransferCallNodeTransferDestination: TypeAlias = Union[
    ComponentNodeTransferCallNodeTransferDestinationTransferDestinationPredefined,
    ComponentNodeTransferCallNodeTransferDestinationTransferDestinationInferred,
]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionColdTransfer(BaseModel):
    type: Literal["cold_transfer"]
    """The type of the transfer."""

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferIvrOption(BaseModel):
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption: TypeAlias = Union[
    ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt,
    ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption: TypeAlias = Union[
    ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt,
    ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransfer(BaseModel):
    type: Literal["warm_transfer"]
    """The type of the transfer."""

    agent_detection_timeout_ms: Optional[float] = None
    """The time to wait before considering transfer fails."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    ivr_option: Optional[ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferIvrOption] = None
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
        ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPrivateHandoffOption
    ] = None
    """
    If set, when transfer is connected, will say the handoff message only to the
    agent receiving the transfer. Can leave either a static message or a dynamic one
    based on prompt. Set to null to disable warm handoff.
    """

    public_handoff_option: Optional[
        ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransferPublicHandoffOption
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


class ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent(
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


class ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig(BaseModel):
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    action_on_timeout: Optional[Literal["bridge_transfer", "cancel_transfer"]] = None
    """The action to take when the transfer agent times out without making a decision.

    Defaults to cancel_transfer.
    """

    transfer_agent: Optional[
        ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent
    ] = None
    """The agent that will mediate the transfer decision."""

    transfer_timeout_ms: Optional[float] = None
    """
    The maximum time to wait for the transfer agent to make a decision, in
    milliseconds. Defaults to 30000 (30 seconds).
    """


class ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption: TypeAlias = Union[
    ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt,
    ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransfer(BaseModel):
    agentic_transfer_config: (
        ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig
    )
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    type: Literal["agentic_warm_transfer"]
    """The type of the transfer."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    on_hold_music: Optional[Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]] = None
    """The music to play while the caller is being transferred."""

    public_handoff_option: Optional[
        ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption
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


ComponentNodeTransferCallNodeTransferOption: TypeAlias = Union[
    ComponentNodeTransferCallNodeTransferOptionTransferOptionColdTransfer,
    ComponentNodeTransferCallNodeTransferOptionTransferOptionWarmTransfer,
    ComponentNodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransfer,
]


class ComponentNodeTransferCallNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeTransferCallNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[
        List[ComponentNodeTransferCallNodeGlobalNodeSettingNegativeFinetuneExample]
    ] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[
        List[ComponentNodeTransferCallNodeGlobalNodeSettingPositiveFinetuneExample]
    ] = None
    """Transition to this node"""


class ComponentNodeTransferCallNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeTransferCallNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


ComponentNodeTransferCallNodeInstruction: TypeAlias = Union[
    ComponentNodeTransferCallNodeInstructionNodeInstructionPrompt,
    ComponentNodeTransferCallNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeTransferCallNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeTransferCallNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    edge: ComponentNodeTransferCallNodeEdge

    transfer_destination: ComponentNodeTransferCallNodeTransferDestination

    transfer_option: ComponentNodeTransferCallNodeTransferOption

    type: Literal["transfer_call"]
    """Type of the node"""

    custom_sip_headers: Optional[Dict[str, str]] = None
    """Custom SIP headers for transfer calls"""

    display_position: Optional[ComponentNodeTransferCallNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[ComponentNodeTransferCallNodeGlobalNodeSetting] = None

    ignore_e164_validation: Optional[bool] = None
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    instruction: Optional[ComponentNodeTransferCallNodeInstruction] = None
    """What to say when transferring the call, only used when speak during execution"""

    api_model_choice: Optional[ComponentNodeTransferCallNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution"""


class ComponentNodePressDigitNodeInstruction(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodePressDigitNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodePressDigitNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodePressDigitNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodePressDigitNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodePressDigitNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodePressDigitNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodePressDigitNodeEdgeTransitionConditionPromptCondition,
    ComponentNodePressDigitNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodePressDigitNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodePressDigitNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodePressDigitNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodePressDigitNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodePressDigitNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodePressDigitNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodePressDigitNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[ComponentNodePressDigitNodeGlobalNodeSettingNegativeFinetuneExample]] = (
        None
    )
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodePressDigitNodeGlobalNodeSettingPositiveFinetuneExample]] = (
        None
    )
    """Transition to this node"""


class ComponentNodePressDigitNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodePressDigitNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    instruction: ComponentNodePressDigitNodeInstruction

    type: Literal["press_digit"]
    """Type of the node"""

    delay_ms: Optional[int] = None
    """Delay in milliseconds before pressing the digit"""

    display_position: Optional[ComponentNodePressDigitNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[ComponentNodePressDigitNodeEdge]] = None

    finetune_transition_examples: Optional[List[ComponentNodePressDigitNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[ComponentNodePressDigitNodeGlobalNodeSetting] = None

    api_model_choice: Optional[ComponentNodePressDigitNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""


class ComponentNodeBranchNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeBranchNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeBranchNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeBranchNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class ComponentNodeBranchNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


ComponentNodeBranchNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeBranchNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeBranchNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeBranchNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeBranchNodeElseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeBranchNodeElseEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeBranchNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeBranchNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeBranchNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeBranchNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeBranchNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeBranchNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeBranchNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeBranchNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeBranchNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeBranchNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeBranchNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeBranchNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeBranchNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodeBranchNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeBranchNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class ComponentNodeBranchNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    else_edge: ComponentNodeBranchNodeElseEdge

    type: Literal["branch"]
    """Type of the node"""

    display_position: Optional[ComponentNodeBranchNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[ComponentNodeBranchNodeEdge]] = None

    finetune_transition_examples: Optional[List[ComponentNodeBranchNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[ComponentNodeBranchNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class ComponentNodeSMSNodeFailedEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeSMSNodeFailedEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSMSNodeFailedEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeSMSNodeFailedEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Failed to send"]] = None
    """Must be "failed to send" for SMS failed edge"""


class ComponentNodeSMSNodeFailedEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Failed to send"]
    """Must be "failed to send" for SMS failed edge"""

    type: Literal["prompt"]


ComponentNodeSMSNodeFailedEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeSMSNodeFailedEdgeTransitionConditionPromptCondition,
    ComponentNodeSMSNodeFailedEdgeTransitionConditionEquationCondition,
    ComponentNodeSMSNodeFailedEdgeTransitionConditionUnionMember2,
]


class ComponentNodeSMSNodeFailedEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeSMSNodeFailedEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeSMSNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeSMSNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


ComponentNodeSMSNodeInstruction: TypeAlias = Union[
    ComponentNodeSMSNodeInstructionNodeInstructionPrompt, ComponentNodeSMSNodeInstructionNodeInstructionStaticText
]


class ComponentNodeSMSNodeSuccessEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Sent successfully"]] = None
    """Must be "sent successfully" for SMS success edge"""


class ComponentNodeSMSNodeSuccessEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Sent successfully"]
    """Must be "sent successfully" for SMS success edge"""

    type: Literal["prompt"]


ComponentNodeSMSNodeSuccessEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeSMSNodeSuccessEdgeTransitionConditionPromptCondition,
    ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationCondition,
    ComponentNodeSMSNodeSuccessEdgeTransitionConditionUnionMember2,
]


class ComponentNodeSMSNodeSuccessEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeSMSNodeSuccessEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeSMSNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeSMSNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class ComponentNodeSMSNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    failed_edge: ComponentNodeSMSNodeFailedEdge

    instruction: ComponentNodeSMSNodeInstruction

    success_edge: ComponentNodeSMSNodeSuccessEdge

    type: Literal["sms"]
    """Type of the node"""

    display_position: Optional[ComponentNodeSMSNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[ComponentNodeSMSNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class ComponentNodeExtractDynamicVariablesNodeVariableStringAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["string"]
    """Type of the variable to extract."""

    examples: Optional[List[str]] = None
    """Examples of the variable value to teach model the style and syntax."""


class ComponentNodeExtractDynamicVariablesNodeVariableEnumAnalysisData(BaseModel):
    choices: List[str]
    """The possible values of the variable, must be non empty array."""

    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["enum"]
    """Type of the variable to extract."""


class ComponentNodeExtractDynamicVariablesNodeVariableBooleanAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["boolean"]
    """Type of the variable to extract."""


class ComponentNodeExtractDynamicVariablesNodeVariableNumberAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["number"]
    """Type of the variable to extract."""


ComponentNodeExtractDynamicVariablesNodeVariable: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeVariableStringAnalysisData,
    ComponentNodeExtractDynamicVariablesNodeVariableEnumAnalysisData,
    ComponentNodeExtractDynamicVariablesNodeVariableBooleanAnalysisData,
    ComponentNodeExtractDynamicVariablesNodeVariableNumberAnalysisData,
]


class ComponentNodeExtractDynamicVariablesNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeExtractDynamicVariablesNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeExtractDynamicVariablesNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeExtractDynamicVariablesNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[
        List[ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingNegativeFinetuneExample]
    ] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[
        List[ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingPositiveFinetuneExample]
    ] = None
    """Transition to this node"""


class ComponentNodeExtractDynamicVariablesNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeExtractDynamicVariablesNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["extract_dynamic_variables"]
    """Type of the node"""

    variables: List[ComponentNodeExtractDynamicVariablesNodeVariable]

    display_position: Optional[ComponentNodeExtractDynamicVariablesNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[ComponentNodeExtractDynamicVariablesNodeEdge]] = None

    finetune_transition_examples: Optional[List[ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExample]] = (
        None
    )

    global_node_setting: Optional[ComponentNodeExtractDynamicVariablesNodeGlobalNodeSetting] = None

    api_model_choice: Optional[ComponentNodeExtractDynamicVariablesNodeModelChoice] = FieldInfo(
        alias="model_choice", default=None
    )

    name: Optional[str] = None
    """Optional name for display purposes"""


class ComponentNodeAgentSwapNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeAgentSwapNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeAgentSwapNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeAgentSwapNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Transfer failed"]] = None
    """Must be "Transfer failed" for transfer failed edge"""


class ComponentNodeAgentSwapNodeEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Transfer failed"]
    """Must be "Transfer failed" for transfer failed edge"""

    type: Literal["prompt"]


ComponentNodeAgentSwapNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeAgentSwapNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeAgentSwapNodeEdgeTransitionConditionEquationCondition,
    ComponentNodeAgentSwapNodeEdgeTransitionConditionUnionMember2,
]


class ComponentNodeAgentSwapNodeEdge(BaseModel):
    """Edge to transition to if agent swap fails"""

    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeAgentSwapNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeAgentSwapNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeAgentSwapNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[ComponentNodeAgentSwapNodeGlobalNodeSettingNegativeFinetuneExample]] = (
        None
    )
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeAgentSwapNodeGlobalNodeSettingPositiveFinetuneExample]] = (
        None
    )
    """Transition to this node"""


class ComponentNodeAgentSwapNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeAgentSwapNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


ComponentNodeAgentSwapNodeInstruction: TypeAlias = Union[
    ComponentNodeAgentSwapNodeInstructionNodeInstructionPrompt,
    ComponentNodeAgentSwapNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeAgentSwapNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    agent_id: str
    """The ID of the agent to swap to"""

    edge: ComponentNodeAgentSwapNodeEdge
    """Edge to transition to if agent swap fails"""

    post_call_analysis_setting: Literal["both_agents", "only_destination_agent"]
    """Post call analysis setting for the agent swap"""

    type: Literal["agent_swap"]
    """Type of the node"""

    agent_version: Optional[float] = None
    """The version of the agent to swap to.

    If not specified, will use the latest version
    """

    display_position: Optional[ComponentNodeAgentSwapNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[ComponentNodeAgentSwapNodeGlobalNodeSetting] = None

    instruction: Optional[ComponentNodeAgentSwapNodeInstruction] = None
    """What to say when swapping agents, only used when speak during execution"""

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution"""

    webhook_setting: Optional[Literal["both_agents", "only_destination_agent", "only_source_agent"]] = None
    """Webhook setting for the agent swap, defaults to only source."""


class ComponentNodeMcpNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeMcpNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeMcpNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeMcpNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeMcpNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeMcpNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeMcpNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeMcpNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeMcpNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeMcpNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeMcpNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeMcpNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodeMcpNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeMcpNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[ComponentNodeMcpNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeMcpNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class ComponentNodeMcpNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeMcpNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


ComponentNodeMcpNodeInstruction: TypeAlias = Union[
    ComponentNodeMcpNodeInstructionNodeInstructionPrompt, ComponentNodeMcpNodeInstructionNodeInstructionStaticText
]


class ComponentNodeMcpNode(BaseModel):
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

    display_position: Optional[ComponentNodeMcpNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[ComponentNodeMcpNodeEdge]] = None

    finetune_transition_examples: Optional[List[ComponentNodeMcpNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[ComponentNodeMcpNodeGlobalNodeSetting] = None

    instruction: Optional[ComponentNodeMcpNodeInstruction] = None
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


class ComponentNodeComponentNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeComponentNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeComponentNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeComponentNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class ComponentNodeComponentNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


ComponentNodeComponentNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeComponentNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeComponentNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeComponentNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeComponentNodeElseEdge(BaseModel):
    """Default edge when no other conditions are met"""

    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeComponentNodeElseEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeComponentNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeComponentNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeComponentNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeComponentNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeComponentNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeComponentNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeComponentNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeComponentNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeComponentNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeComponentNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeComponentNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[ComponentNodeComponentNodeGlobalNodeSettingNegativeFinetuneExample]] = (
        None
    )
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeComponentNodeGlobalNodeSettingPositiveFinetuneExample]] = (
        None
    )
    """Transition to this node"""


class ComponentNodeComponentNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    component_id: str
    """The reference ID of the component"""

    component_type: Literal["local", "shared"]
    """Type of component:

    - local: stored in conversation flow's components array
    - shared: stored in stand-alone conversation-flow-component table
    """

    else_edge: ComponentNodeComponentNodeElseEdge
    """Default edge when no other conditions are met"""

    type: Literal["component"]
    """Type of the node"""

    display_position: Optional[ComponentNodeComponentNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[ComponentNodeComponentNodeEdge]] = None
    """Array of edges for conditional transitions"""

    global_node_setting: Optional[ComponentNodeComponentNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class ComponentNodeBridgeTransferNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeBridgeTransferNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[
        List[ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    ] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[
        List[ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    ] = None
    """Transition to this node"""


class ComponentNodeBridgeTransferNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["bridge_transfer"]
    """Type of the node - initiates a warm transfer by bridging the call"""

    display_position: Optional[ComponentNodeBridgeTransferNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[ComponentNodeBridgeTransferNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class ComponentNodeCancelTransferNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeCancelTransferNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[
        List[ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    ] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[
        List[ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    ] = None
    """Transition to this node"""


class ComponentNodeCancelTransferNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["cancel_transfer"]
    """Type of the node - cancels the warm transfer and ends the transfer agent call"""

    display_position: Optional[ComponentNodeCancelTransferNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[ComponentNodeCancelTransferNodeGlobalNodeSetting] = None

    name: Optional[str] = None
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


class ComponentBeginTagDisplayPosition(BaseModel):
    """Display position for the begin tag in the frontend"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentMcp(BaseModel):
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


class ComponentToolConversationFlowCustomToolParameters(BaseModel):
    """Tool parameters schema"""

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


class ComponentToolConversationFlowCustomTool(BaseModel):
    name: str
    """Name of the tool"""

    type: Literal["custom"]
    """Type of the tool"""

    url: str
    """Server URL to call the tool. Dynamic variables can be used in the URL."""

    args_at_root: Optional[bool] = None
    """If true, the tool arguments will be passed at the root level of the request
    body.

    If false, they will be nested under "args".
    """

    description: Optional[str] = None
    """Description of the tool"""

    headers: Optional[Dict[str, str]] = None
    """Headers to add to the request"""

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None
    """HTTP method to use for the request, defaults to POST"""

    parameters: Optional[ComponentToolConversationFlowCustomToolParameters] = None
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


class ComponentToolCheckAvailabilityCalTool(BaseModel):
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


class ComponentToolBookAppointmentCalTool(BaseModel):
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


ComponentTool: TypeAlias = Union[
    ComponentToolConversationFlowCustomTool, ComponentToolCheckAvailabilityCalTool, ComponentToolBookAppointmentCalTool
]


class Component(BaseModel):
    name: str
    """Name of the component"""

    nodes: List[ComponentNode]
    """Nodes that make up the component"""

    begin_tag_display_position: Optional[ComponentBeginTagDisplayPosition] = None
    """Display position for the begin tag in the frontend"""

    mcps: Optional[List[ComponentMcp]] = None
    """A list of MCP server configurations to use for this component"""

    start_node_id: Optional[str] = None
    """ID of the starting node"""

    tools: Optional[List[ComponentTool]] = None
    """Tools available within the component"""


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


class ModelChoice(BaseModel):
    """The model choice for the conversation flow."""

    model: Literal[
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
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeConversationNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeConversationNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    knowledge_base_ids: Optional[List[str]] = None
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    api_model_choice: Optional[NodeConversationNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    skip_response_edge: Optional[NodeConversationNodeSkipResponseEdge] = None


class NodeEndNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

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


class NodeEndNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeEndNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


NodeEndNodeInstruction: TypeAlias = Union[
    NodeEndNodeInstructionNodeInstructionPrompt, NodeEndNodeInstructionNodeInstructionStaticText
]


class NodeEndNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["end"]
    """Type of the node"""

    display_position: Optional[NodeEndNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[NodeEndNodeGlobalNodeSetting] = None

    instruction: Optional[NodeEndNodeInstruction] = None
    """What to say when ending the call, only used when speak during execution"""

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution"""


class NodeFunctionNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeFunctionNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeFunctionNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    extension: Optional[str] = None
    """Extension digits to dial after the main number connects.

    Sent via DTMF. Allow digits, '\\**', '#', or a dynamic variable like
    {{extension}}.
    """


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
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


class NodeTransferCallNodeTransferOptionTransferOptionWarmTransferIvrOption(BaseModel):
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


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

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    ivr_option: Optional[NodeTransferCallNodeTransferOptionTransferOptionWarmTransferIvrOption] = None
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

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring, requires the telephony side to support caller id override. Retell
    Twilio numbers support this option.
    """


class NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent(BaseModel):
    """The agent that will mediate the transfer decision."""

    agent_id: str
    """The agent ID of the transfer agent.

    This agent must have isTransferAgent set to true and should use bridge_transfer
    and cancel_transfer tools (for Retell LLM) or BridgeTransferNode and
    CancelTransferNode (for Conversation Flow).
    """

    agent_version: float
    """The version of the transfer agent to use."""


class NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig(BaseModel):
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    action_on_timeout: Optional[Literal["bridge_transfer", "cancel_transfer"]] = None
    """The action to take when the transfer agent times out without making a decision.

    Defaults to cancel_transfer.
    """

    transfer_agent: Optional[
        NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent
    ] = None
    """The agent that will mediate the transfer decision."""

    transfer_timeout_ms: Optional[float] = None
    """
    The maximum time to wait for the transfer agent to make a decision, in
    milliseconds. Defaults to 30000 (30 seconds).
    """


class NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption: TypeAlias = Union[
    NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt,
    NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransfer(BaseModel):
    agentic_transfer_config: NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    type: Literal["agentic_warm_transfer"]
    """The type of the transfer."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    on_hold_music: Optional[Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]] = None
    """The music to play while the caller is being transferred."""

    public_handoff_option: Optional[
        NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption
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


NodeTransferCallNodeTransferOption: TypeAlias = Union[
    NodeTransferCallNodeTransferOptionTransferOptionColdTransfer,
    NodeTransferCallNodeTransferOptionTransferOptionWarmTransfer,
    NodeTransferCallNodeTransferOptionTransferOptionAgenticWarmTransfer,
]


class NodeTransferCallNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

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


class NodeTransferCallNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeTransferCallNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


NodeTransferCallNodeInstruction: TypeAlias = Union[
    NodeTransferCallNodeInstructionNodeInstructionPrompt, NodeTransferCallNodeInstructionNodeInstructionStaticText
]


class NodeTransferCallNodeModelChoice(BaseModel):
    model: Literal[
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

    ignore_e164_validation: Optional[bool] = None
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    instruction: Optional[NodeTransferCallNodeInstruction] = None
    """What to say when transferring the call, only used when speak during execution"""

    api_model_choice: Optional[NodeTransferCallNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution"""


class NodePressDigitNodeInstruction(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodePressDigitNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodePressDigitNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodePressDigitNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeBranchNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeBranchNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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
    """Position for frontend display"""

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
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeExtractDynamicVariablesNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeExtractDynamicVariablesNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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
    """Edge to transition to if agent swap fails"""

    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeAgentSwapNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeAgentSwapNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

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


class NodeAgentSwapNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeAgentSwapNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


NodeAgentSwapNodeInstruction: TypeAlias = Union[
    NodeAgentSwapNodeInstructionNodeInstructionPrompt, NodeAgentSwapNodeInstructionNodeInstructionStaticText
]


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

    instruction: Optional[NodeAgentSwapNodeInstruction] = None
    """What to say when swapping agents, only used when speak during execution"""

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution"""

    webhook_setting: Optional[Literal["both_agents", "only_destination_agent", "only_source_agent"]] = None
    """Webhook setting for the agent swap, defaults to only source."""


class NodeMcpNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeMcpNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeMcpNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


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


class NodeComponentNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeComponentNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeComponentNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeComponentNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class NodeComponentNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


NodeComponentNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeComponentNodeElseEdgeTransitionConditionPromptCondition,
    NodeComponentNodeElseEdgeTransitionConditionEquationCondition,
    NodeComponentNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeComponentNodeElseEdge(BaseModel):
    """Default edge when no other conditions are met"""

    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeComponentNodeElseEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeComponentNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeComponentNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeComponentNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeComponentNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeComponentNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeComponentNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeComponentNodeEdgeTransitionConditionPromptCondition, NodeComponentNodeEdgeTransitionConditionEquationCondition
]


class NodeComponentNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeComponentNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeComponentNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeComponentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeComponentNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeComponentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeComponentNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeComponentNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeComponentNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeComponentNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    component_id: str
    """The reference ID of the component"""

    component_type: Literal["local", "shared"]
    """Type of component:

    - local: stored in conversation flow's components array
    - shared: stored in stand-alone conversation-flow-component table
    """

    else_edge: NodeComponentNodeElseEdge
    """Default edge when no other conditions are met"""

    type: Literal["component"]
    """Type of the node"""

    display_position: Optional[NodeComponentNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[NodeComponentNodeEdge]] = None
    """Array of edges for conditional transitions"""

    global_node_setting: Optional[NodeComponentNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodeBridgeTransferNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeBridgeTransferNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeBridgeTransferNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["bridge_transfer"]
    """Type of the node - initiates a warm transfer by bridging the call"""

    display_position: Optional[NodeBridgeTransferNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[NodeBridgeTransferNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodeCancelTransferNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeCancelTransferNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    negative_finetune_examples: Optional[List[NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeCancelTransferNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["cancel_transfer"]
    """Type of the node - cancels the warm transfer and ends the transfer agent call"""

    display_position: Optional[NodeCancelTransferNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[NodeCancelTransferNodeGlobalNodeSetting] = None

    name: Optional[str] = None
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


class ToolConversationFlowCustomToolParameters(BaseModel):
    """Tool parameters schema"""

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

    args_at_root: Optional[bool] = None
    """If true, the tool arguments will be passed at the root level of the request
    body.

    If false, they will be nested under "args".
    """

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

    begin_after_user_silence_ms: Optional[int] = None
    """
    If set, the AI will begin the conversation after waiting for the user for the
    duration (in milliseconds) specified by this attribute. This only applies if the
    agent is configured to wait for the user to speak first. If not set, the agent
    will wait indefinitely for the user to speak.
    """

    begin_tag_display_position: Optional[BeginTagDisplayPosition] = None
    """Display position for the begin tag in the frontend."""

    components: Optional[List[Component]] = None
    """Local components embedded within the conversation flow."""

    default_dynamic_variables: Optional[Dict[str, str]] = None
    """
    Default dynamic variables that can be referenced throughout the conversation
    flow.
    """

    global_prompt: Optional[str] = None
    """Global prompt used in every node of the conversation flow."""

    is_transfer_llm: Optional[bool] = None
    """Whether this conversation flow is used for transfer LLM."""

    kb_config: Optional[KBConfig] = None
    """Knowledge base configuration for RAG retrieval."""

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

    Only applicable when using certain supported models.
    """

    tools: Optional[List[Tool]] = None
    """Tools available in the conversation flow."""
