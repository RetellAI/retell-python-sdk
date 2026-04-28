# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ConversationFlowUpdateParams",
    "BeginTagDisplayPosition",
    "Component",
    "ComponentNode",
    "ComponentNodeConversationNode",
    "ComponentNodeConversationNodeInstruction",
    "ComponentNodeConversationNodeInstructionNodeInstructionPrompt",
    "ComponentNodeConversationNodeInstructionNodeInstructionStaticText",
    "ComponentNodeConversationNodeAlwaysEdge",
    "ComponentNodeConversationNodeAlwaysEdgeTransitionCondition",
    "ComponentNodeConversationNodeAlwaysEdgeTransitionConditionPromptCondition",
    "ComponentNodeConversationNodeAlwaysEdgeTransitionConditionEquationCondition",
    "ComponentNodeConversationNodeAlwaysEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeConversationNodeAlwaysEdgeTransitionConditionUnionMember2",
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
    "ComponentNodeConversationNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeSubagentNode",
    "ComponentNodeSubagentNodeInstruction",
    "ComponentNodeSubagentNodeAlwaysEdge",
    "ComponentNodeSubagentNodeAlwaysEdgeTransitionCondition",
    "ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionPromptCondition",
    "ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionEquationCondition",
    "ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionUnionMember2",
    "ComponentNodeSubagentNodeDisplayPosition",
    "ComponentNodeSubagentNodeEdge",
    "ComponentNodeSubagentNodeEdgeTransitionCondition",
    "ComponentNodeSubagentNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeSubagentNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeSubagentNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeSubagentNodeFinetuneConversationExample",
    "ComponentNodeSubagentNodeFinetuneConversationExampleTranscript",
    "ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember0",
    "ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember1",
    "ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember2",
    "ComponentNodeSubagentNodeFinetuneTransitionExample",
    "ComponentNodeSubagentNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeSubagentNodeGlobalNodeSetting",
    "ComponentNodeSubagentNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
    "ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeSubagentNodeModelChoice",
    "ComponentNodeSubagentNodeSkipResponseEdge",
    "ComponentNodeSubagentNodeSkipResponseEdgeTransitionCondition",
    "ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionPromptCondition",
    "ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionEquationCondition",
    "ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionUnionMember2",
    "ComponentNodeSubagentNodeTool",
    "ComponentNodeSubagentNodeToolEndCallTool",
    "ComponentNodeSubagentNodeToolTransferCallTool",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferDestination",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationPredefined",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationInferred",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOption",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionColdTransfer",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransfer",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "ComponentNodeSubagentNodeToolCheckAvailabilityCalTool",
    "ComponentNodeSubagentNodeToolBookAppointmentCalTool",
    "ComponentNodeSubagentNodeToolAgentSwapTool",
    "ComponentNodeSubagentNodeToolPressDigitTool",
    "ComponentNodeSubagentNodeToolSendSMSTool",
    "ComponentNodeSubagentNodeToolSendSMSToolSMSContent",
    "ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentPredefined",
    "ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentInferred",
    "ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentTemplate",
    "ComponentNodeSubagentNodeToolCustomTool",
    "ComponentNodeSubagentNodeToolCustomToolParameters",
    "ComponentNodeSubagentNodeToolCodeTool",
    "ComponentNodeSubagentNodeToolExtractDynamicVariableTool",
    "ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariable",
    "ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableStringAnalysisData",
    "ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableEnumAnalysisData",
    "ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableBooleanAnalysisData",
    "ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableNumberAnalysisData",
    "ComponentNodeSubagentNodeToolBridgeTransferTool",
    "ComponentNodeSubagentNodeToolCancelTransferTool",
    "ComponentNodeSubagentNodeToolMcpTool",
    "ComponentNodeEndNode",
    "ComponentNodeEndNodeDisplayPosition",
    "ComponentNodeEndNodeGlobalNodeSetting",
    "ComponentNodeEndNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeEndNodeModelChoice",
    "ComponentNodeFunctionNode",
    "ComponentNodeFunctionNodeDisplayPosition",
    "ComponentNodeFunctionNodeEdge",
    "ComponentNodeFunctionNodeEdgeTransitionCondition",
    "ComponentNodeFunctionNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeFunctionNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeFunctionNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeFunctionNodeElseEdge",
    "ComponentNodeFunctionNodeElseEdgeTransitionCondition",
    "ComponentNodeFunctionNodeElseEdgeTransitionConditionPromptCondition",
    "ComponentNodeFunctionNodeElseEdgeTransitionConditionEquationCondition",
    "ComponentNodeFunctionNodeElseEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeFunctionNodeElseEdgeTransitionConditionUnionMember2",
    "ComponentNodeFunctionNodeFinetuneTransitionExample",
    "ComponentNodeFunctionNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeFunctionNodeGlobalNodeSetting",
    "ComponentNodeFunctionNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeCodeNode",
    "ComponentNodeCodeNodeDisplayPosition",
    "ComponentNodeCodeNodeEdge",
    "ComponentNodeCodeNodeEdgeTransitionCondition",
    "ComponentNodeCodeNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeCodeNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeCodeNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeCodeNodeElseEdge",
    "ComponentNodeCodeNodeElseEdgeTransitionCondition",
    "ComponentNodeCodeNodeElseEdgeTransitionConditionPromptCondition",
    "ComponentNodeCodeNodeElseEdgeTransitionConditionEquationCondition",
    "ComponentNodeCodeNodeElseEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeCodeNodeElseEdgeTransitionConditionUnionMember2",
    "ComponentNodeCodeNodeFinetuneTransitionExample",
    "ComponentNodeCodeNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeCodeNodeGlobalNodeSetting",
    "ComponentNodeCodeNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
    "ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExample",
    "ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExample",
    "ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "ComponentNodeCodeNodeInstruction",
    "ComponentNodeCodeNodeInstructionNodeInstructionPrompt",
    "ComponentNodeCodeNodeInstructionNodeInstructionStaticText",
    "ComponentNodeCodeNodeModelChoice",
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
    "ComponentNodeTransferCallNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodePressDigitNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeBranchNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeBranchNodeModelChoice",
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
    "ComponentNodeSMSNodeInstructionSMSInstructionTemplate",
    "ComponentNodeSMSNodeSuccessEdge",
    "ComponentNodeSMSNodeSuccessEdgeTransitionCondition",
    "ComponentNodeSMSNodeSuccessEdgeTransitionConditionPromptCondition",
    "ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationCondition",
    "ComponentNodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeSMSNodeSuccessEdgeTransitionConditionUnionMember2",
    "ComponentNodeSMSNodeDisplayPosition",
    "ComponentNodeSMSNodeGlobalNodeSetting",
    "ComponentNodeSMSNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeSMSNodeModelChoice",
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
    "ComponentNodeExtractDynamicVariablesNodeElseEdge",
    "ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionCondition",
    "ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionPromptCondition",
    "ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationCondition",
    "ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionUnionMember2",
    "ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExample",
    "ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSetting",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeAgentSwapNodeModelChoice",
    "ComponentNodeMcpNode",
    "ComponentNodeMcpNodeDisplayPosition",
    "ComponentNodeMcpNodeEdge",
    "ComponentNodeMcpNodeEdgeTransitionCondition",
    "ComponentNodeMcpNodeEdgeTransitionConditionPromptCondition",
    "ComponentNodeMcpNodeEdgeTransitionConditionEquationCondition",
    "ComponentNodeMcpNodeEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeMcpNodeElseEdge",
    "ComponentNodeMcpNodeElseEdgeTransitionCondition",
    "ComponentNodeMcpNodeElseEdgeTransitionConditionPromptCondition",
    "ComponentNodeMcpNodeElseEdgeTransitionConditionEquationCondition",
    "ComponentNodeMcpNodeElseEdgeTransitionConditionEquationConditionEquation",
    "ComponentNodeMcpNodeElseEdgeTransitionConditionUnionMember2",
    "ComponentNodeMcpNodeFinetuneTransitionExample",
    "ComponentNodeMcpNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeMcpNodeGlobalNodeSetting",
    "ComponentNodeMcpNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeMcpNodeModelChoice",
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
    "ComponentNodeComponentNodeFinetuneTransitionExample",
    "ComponentNodeComponentNodeFinetuneTransitionExampleTranscript",
    "ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "ComponentNodeComponentNodeGlobalNodeSetting",
    "ComponentNodeComponentNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeBridgeTransferNodeInstruction",
    "ComponentNodeBridgeTransferNodeInstructionNodeInstructionPrompt",
    "ComponentNodeBridgeTransferNodeInstructionNodeInstructionStaticText",
    "ComponentNodeBridgeTransferNodeModelChoice",
    "ComponentNodeCancelTransferNode",
    "ComponentNodeCancelTransferNodeDisplayPosition",
    "ComponentNodeCancelTransferNodeGlobalNodeSetting",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackCondition",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "ComponentNodeCancelTransferNodeInstruction",
    "ComponentNodeCancelTransferNodeInstructionNodeInstructionPrompt",
    "ComponentNodeCancelTransferNodeInstructionNodeInstructionStaticText",
    "ComponentNodeCancelTransferNodeModelChoice",
    "ComponentBeginTagDisplayPosition",
    "ComponentMcp",
    "ComponentNote",
    "ComponentNoteDisplayPosition",
    "ComponentNoteSize",
    "ComponentTool",
    "ComponentToolCustomTool",
    "ComponentToolCustomToolParameters",
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
    "NodeConversationNodeAlwaysEdge",
    "NodeConversationNodeAlwaysEdgeTransitionCondition",
    "NodeConversationNodeAlwaysEdgeTransitionConditionPromptCondition",
    "NodeConversationNodeAlwaysEdgeTransitionConditionEquationCondition",
    "NodeConversationNodeAlwaysEdgeTransitionConditionEquationConditionEquation",
    "NodeConversationNodeAlwaysEdgeTransitionConditionUnionMember2",
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
    "NodeConversationNodeGlobalNodeSettingGoBackCondition",
    "NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeSubagentNode",
    "NodeSubagentNodeInstruction",
    "NodeSubagentNodeAlwaysEdge",
    "NodeSubagentNodeAlwaysEdgeTransitionCondition",
    "NodeSubagentNodeAlwaysEdgeTransitionConditionPromptCondition",
    "NodeSubagentNodeAlwaysEdgeTransitionConditionEquationCondition",
    "NodeSubagentNodeAlwaysEdgeTransitionConditionEquationConditionEquation",
    "NodeSubagentNodeAlwaysEdgeTransitionConditionUnionMember2",
    "NodeSubagentNodeDisplayPosition",
    "NodeSubagentNodeEdge",
    "NodeSubagentNodeEdgeTransitionCondition",
    "NodeSubagentNodeEdgeTransitionConditionPromptCondition",
    "NodeSubagentNodeEdgeTransitionConditionEquationCondition",
    "NodeSubagentNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeSubagentNodeFinetuneConversationExample",
    "NodeSubagentNodeFinetuneConversationExampleTranscript",
    "NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember0",
    "NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember1",
    "NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember2",
    "NodeSubagentNodeFinetuneTransitionExample",
    "NodeSubagentNodeFinetuneTransitionExampleTranscript",
    "NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeSubagentNodeGlobalNodeSetting",
    "NodeSubagentNodeGlobalNodeSettingGoBackCondition",
    "NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
    "NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeSubagentNodeModelChoice",
    "NodeSubagentNodeSkipResponseEdge",
    "NodeSubagentNodeSkipResponseEdgeTransitionCondition",
    "NodeSubagentNodeSkipResponseEdgeTransitionConditionPromptCondition",
    "NodeSubagentNodeSkipResponseEdgeTransitionConditionEquationCondition",
    "NodeSubagentNodeSkipResponseEdgeTransitionConditionEquationConditionEquation",
    "NodeSubagentNodeSkipResponseEdgeTransitionConditionUnionMember2",
    "NodeSubagentNodeTool",
    "NodeSubagentNodeToolEndCallTool",
    "NodeSubagentNodeToolTransferCallTool",
    "NodeSubagentNodeToolTransferCallToolTransferDestination",
    "NodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationPredefined",
    "NodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationInferred",
    "NodeSubagentNodeToolTransferCallToolTransferOption",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionColdTransfer",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransfer",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt",
    "NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage",
    "NodeSubagentNodeToolCheckAvailabilityCalTool",
    "NodeSubagentNodeToolBookAppointmentCalTool",
    "NodeSubagentNodeToolAgentSwapTool",
    "NodeSubagentNodeToolPressDigitTool",
    "NodeSubagentNodeToolSendSMSTool",
    "NodeSubagentNodeToolSendSMSToolSMSContent",
    "NodeSubagentNodeToolSendSMSToolSMSContentSMSContentPredefined",
    "NodeSubagentNodeToolSendSMSToolSMSContentSMSContentInferred",
    "NodeSubagentNodeToolSendSMSToolSMSContentSMSContentTemplate",
    "NodeSubagentNodeToolCustomTool",
    "NodeSubagentNodeToolCustomToolParameters",
    "NodeSubagentNodeToolCodeTool",
    "NodeSubagentNodeToolExtractDynamicVariableTool",
    "NodeSubagentNodeToolExtractDynamicVariableToolVariable",
    "NodeSubagentNodeToolExtractDynamicVariableToolVariableStringAnalysisData",
    "NodeSubagentNodeToolExtractDynamicVariableToolVariableEnumAnalysisData",
    "NodeSubagentNodeToolExtractDynamicVariableToolVariableBooleanAnalysisData",
    "NodeSubagentNodeToolExtractDynamicVariableToolVariableNumberAnalysisData",
    "NodeSubagentNodeToolBridgeTransferTool",
    "NodeSubagentNodeToolCancelTransferTool",
    "NodeSubagentNodeToolMcpTool",
    "NodeEndNode",
    "NodeEndNodeDisplayPosition",
    "NodeEndNodeGlobalNodeSetting",
    "NodeEndNodeGlobalNodeSettingGoBackCondition",
    "NodeEndNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeEndNodeModelChoice",
    "NodeFunctionNode",
    "NodeFunctionNodeDisplayPosition",
    "NodeFunctionNodeEdge",
    "NodeFunctionNodeEdgeTransitionCondition",
    "NodeFunctionNodeEdgeTransitionConditionPromptCondition",
    "NodeFunctionNodeEdgeTransitionConditionEquationCondition",
    "NodeFunctionNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeFunctionNodeElseEdge",
    "NodeFunctionNodeElseEdgeTransitionCondition",
    "NodeFunctionNodeElseEdgeTransitionConditionPromptCondition",
    "NodeFunctionNodeElseEdgeTransitionConditionEquationCondition",
    "NodeFunctionNodeElseEdgeTransitionConditionEquationConditionEquation",
    "NodeFunctionNodeElseEdgeTransitionConditionUnionMember2",
    "NodeFunctionNodeFinetuneTransitionExample",
    "NodeFunctionNodeFinetuneTransitionExampleTranscript",
    "NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeFunctionNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeFunctionNodeGlobalNodeSetting",
    "NodeFunctionNodeGlobalNodeSettingGoBackCondition",
    "NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeCodeNode",
    "NodeCodeNodeDisplayPosition",
    "NodeCodeNodeEdge",
    "NodeCodeNodeEdgeTransitionCondition",
    "NodeCodeNodeEdgeTransitionConditionPromptCondition",
    "NodeCodeNodeEdgeTransitionConditionEquationCondition",
    "NodeCodeNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeCodeNodeElseEdge",
    "NodeCodeNodeElseEdgeTransitionCondition",
    "NodeCodeNodeElseEdgeTransitionConditionPromptCondition",
    "NodeCodeNodeElseEdgeTransitionConditionEquationCondition",
    "NodeCodeNodeElseEdgeTransitionConditionEquationConditionEquation",
    "NodeCodeNodeElseEdgeTransitionConditionUnionMember2",
    "NodeCodeNodeFinetuneTransitionExample",
    "NodeCodeNodeFinetuneTransitionExampleTranscript",
    "NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeCodeNodeGlobalNodeSetting",
    "NodeCodeNodeGlobalNodeSettingGoBackCondition",
    "NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
    "NodeCodeNodeGlobalNodeSettingNegativeFinetuneExample",
    "NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscript",
    "NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0",
    "NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1",
    "NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2",
    "NodeCodeNodeGlobalNodeSettingPositiveFinetuneExample",
    "NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscript",
    "NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0",
    "NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1",
    "NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2",
    "NodeCodeNodeInstruction",
    "NodeCodeNodeInstructionNodeInstructionPrompt",
    "NodeCodeNodeInstructionNodeInstructionStaticText",
    "NodeCodeNodeModelChoice",
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
    "NodeTransferCallNodeGlobalNodeSettingGoBackCondition",
    "NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodePressDigitNodeGlobalNodeSettingGoBackCondition",
    "NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeBranchNodeGlobalNodeSettingGoBackCondition",
    "NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeBranchNodeModelChoice",
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
    "NodeSMSNodeInstructionSMSInstructionTemplate",
    "NodeSMSNodeSuccessEdge",
    "NodeSMSNodeSuccessEdgeTransitionCondition",
    "NodeSMSNodeSuccessEdgeTransitionConditionPromptCondition",
    "NodeSMSNodeSuccessEdgeTransitionConditionEquationCondition",
    "NodeSMSNodeSuccessEdgeTransitionConditionEquationConditionEquation",
    "NodeSMSNodeSuccessEdgeTransitionConditionUnionMember2",
    "NodeSMSNodeDisplayPosition",
    "NodeSMSNodeGlobalNodeSetting",
    "NodeSMSNodeGlobalNodeSettingGoBackCondition",
    "NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeSMSNodeModelChoice",
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
    "NodeExtractDynamicVariablesNodeElseEdge",
    "NodeExtractDynamicVariablesNodeElseEdgeTransitionCondition",
    "NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionPromptCondition",
    "NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationCondition",
    "NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationConditionEquation",
    "NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionUnionMember2",
    "NodeExtractDynamicVariablesNodeFinetuneTransitionExample",
    "NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscript",
    "NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeExtractDynamicVariablesNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeExtractDynamicVariablesNodeGlobalNodeSetting",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackCondition",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeAgentSwapNodeGlobalNodeSettingGoBackCondition",
    "NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeAgentSwapNodeModelChoice",
    "NodeMcpNode",
    "NodeMcpNodeDisplayPosition",
    "NodeMcpNodeEdge",
    "NodeMcpNodeEdgeTransitionCondition",
    "NodeMcpNodeEdgeTransitionConditionPromptCondition",
    "NodeMcpNodeEdgeTransitionConditionEquationCondition",
    "NodeMcpNodeEdgeTransitionConditionEquationConditionEquation",
    "NodeMcpNodeElseEdge",
    "NodeMcpNodeElseEdgeTransitionCondition",
    "NodeMcpNodeElseEdgeTransitionConditionPromptCondition",
    "NodeMcpNodeElseEdgeTransitionConditionEquationCondition",
    "NodeMcpNodeElseEdgeTransitionConditionEquationConditionEquation",
    "NodeMcpNodeElseEdgeTransitionConditionUnionMember2",
    "NodeMcpNodeFinetuneTransitionExample",
    "NodeMcpNodeFinetuneTransitionExampleTranscript",
    "NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeMcpNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeMcpNodeGlobalNodeSetting",
    "NodeMcpNodeGlobalNodeSettingGoBackCondition",
    "NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeMcpNodeModelChoice",
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
    "NodeComponentNodeFinetuneTransitionExample",
    "NodeComponentNodeFinetuneTransitionExampleTranscript",
    "NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember0",
    "NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember1",
    "NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember2",
    "NodeComponentNodeGlobalNodeSetting",
    "NodeComponentNodeGlobalNodeSettingGoBackCondition",
    "NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeBridgeTransferNodeGlobalNodeSettingGoBackCondition",
    "NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeBridgeTransferNodeInstruction",
    "NodeBridgeTransferNodeInstructionNodeInstructionPrompt",
    "NodeBridgeTransferNodeInstructionNodeInstructionStaticText",
    "NodeBridgeTransferNodeModelChoice",
    "NodeCancelTransferNode",
    "NodeCancelTransferNodeDisplayPosition",
    "NodeCancelTransferNodeGlobalNodeSetting",
    "NodeCancelTransferNodeGlobalNodeSettingGoBackCondition",
    "NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition",
    "NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition",
    "NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition",
    "NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation",
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
    "NodeCancelTransferNodeInstruction",
    "NodeCancelTransferNodeInstructionNodeInstructionPrompt",
    "NodeCancelTransferNodeInstructionNodeInstructionStaticText",
    "NodeCancelTransferNodeModelChoice",
    "Note",
    "NoteDisplayPosition",
    "NoteSize",
    "Tool",
    "ToolCustomTool",
    "ToolCustomToolParameters",
    "ToolCheckAvailabilityCalTool",
    "ToolBookAppointmentCalTool",
]


class ConversationFlowUpdateParams(TypedDict, total=False):
    version: int
    """Optional version of the conversation flow to update. Default to latest version."""

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

    model_choice: ModelChoice
    """The model choice for the conversation flow."""

    model_temperature: Optional[float]
    """Controls the randomness of the model's responses.

    Lower values make responses more deterministic.
    """

    nodes: Iterable[Node]
    """Array of nodes in the conversation flow."""

    notes: Optional[Iterable[Note]]
    """Visual annotations displayed on the flow canvas."""

    start_node_id: Optional[str]
    """ID of the start node in the conversation flow."""

    start_speaker: Literal["user", "agent"]
    """Who starts the conversation - user or agent."""

    tool_call_strict_mode: Optional[bool]
    """Whether to use strict mode for tool calls.

    Only applicable when using certain supported models.
    """

    tools: Optional[Iterable[Tool]]
    """Tools available in the conversation flow."""


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


class ComponentNodeConversationNodeAlwaysEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeConversationNodeAlwaysEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeConversationNodeAlwaysEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeConversationNodeAlwaysEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Always"]
    """Must be "Always" for always edge"""


class ComponentNodeConversationNodeAlwaysEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Always"]]
    """Must be "Always" for always edge"""

    type: Required[Literal["prompt"]]


ComponentNodeConversationNodeAlwaysEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeConversationNodeAlwaysEdgeTransitionConditionPromptCondition,
    ComponentNodeConversationNodeAlwaysEdgeTransitionConditionEquationCondition,
    ComponentNodeConversationNodeAlwaysEdgeTransitionConditionUnionMember2,
]


class ComponentNodeConversationNodeAlwaysEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeConversationNodeAlwaysEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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


class ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[
            ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
        ]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeConversationNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeConversationNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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

    always_edge: ComponentNodeConversationNodeAlwaysEdge

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

    responsiveness: Optional[float]

    skip_response_edge: ComponentNodeConversationNodeSkipResponseEdge

    voice_speed: Optional[float]


class ComponentNodeSubagentNodeInstruction(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Always"]
    """Must be "Always" for always edge"""


class ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Always"]]
    """Must be "Always" for always edge"""

    type: Required[Literal["prompt"]]


ComponentNodeSubagentNodeAlwaysEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionPromptCondition,
    ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionEquationCondition,
    ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionUnionMember2,
]


class ComponentNodeSubagentNodeAlwaysEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeSubagentNodeAlwaysEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeSubagentNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeSubagentNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeSubagentNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSubagentNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeSubagentNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeSubagentNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeSubagentNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeSubagentNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeSubagentNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeSubagentNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeSubagentNodeFinetuneConversationExampleTranscript: TypeAlias = Union[
    ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember0,
    ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember1,
    ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember2,
]


class ComponentNodeSubagentNodeFinetuneConversationExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodeSubagentNodeFinetuneConversationExampleTranscript]]
    """The example transcript to finetune how the conversation should be."""


class ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeSubagentNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeSubagentNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodeSubagentNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeSubagentNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeSubagentNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeSubagentNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeSubagentNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Skip response"]
    """Must be "Skip response" for skip response edge"""


class ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Skip response"]]
    """Must be "Skip response" for skip response edge"""

    type: Required[Literal["prompt"]]


ComponentNodeSubagentNodeSkipResponseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionPromptCondition,
    ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionEquationCondition,
    ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeSubagentNodeSkipResponseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeSubagentNodeSkipResponseEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeSubagentNodeToolEndCallTool(TypedDict, total=False):
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

    execution_message_description: str
    """Describes what to say to user when ending the call.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: bool
    """If true, will speak during execution."""


class ComponentNodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationPredefined(
    TypedDict, total=False
):
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


class ComponentNodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationInferred(
    TypedDict, total=False
):
    prompt: Required[str]
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Required[Literal["inferred"]]
    """The type of transfer destination."""


ComponentNodeSubagentNodeToolTransferCallToolTransferDestination: TypeAlias = Union[
    ComponentNodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationPredefined,
    ComponentNodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationInferred,
]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionColdTransfer(TypedDict, total=False):
    type: Required[Literal["cold_transfer"]]
    """The type of the transfer."""

    cold_transfer_mode: Literal["sip_refer", "sip_invite"]
    """The mode of the cold transfer.

    If set to `sip_refer`, will use SIP REFER to transfer the call. If set to
    `sip_invite`, will use SIP INVITE to transfer the call.
    """

    show_transferee_as_caller: bool
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring. Requires the telephony side to support caller id override. Retell
    Twilio numbers support this option. This parameter takes effect only when
    `cold_transfer_mode` is set to `sip_invite`. When using `sip_refer`, this option
    is not available. Retell Twilio numbers always use user's number as the caller
    id when using `sip refer` cold transfer mode.
    """

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption(
    TypedDict, total=False
):
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption: TypeAlias = Union[
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt,
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption: TypeAlias = Union[
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt,
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransfer(TypedDict, total=False):
    type: Required[Literal["warm_transfer"]]
    """The type of the transfer."""

    agent_detection_timeout_ms: float
    """The time to wait before considering transfer fails."""

    enable_bridge_audio_cue: bool
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    ivr_option: ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    on_hold_music: Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]
    """The music to play while the caller is being transferred."""

    opt_out_human_detection: bool
    """If set to true, will not perform human detection for the transfer.

    Default to false.
    """

    private_handoff_option: (
        ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption
    )
    """
    If set, when transfer is connected, will say the handoff message only to the
    agent receiving the transfer. Can leave either a static message or a dynamic one
    based on prompt. Set to null to disable warm handoff.
    """

    public_handoff_option: (
        ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption
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

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent(
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


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig(
    TypedDict, total=False
):
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    action_on_timeout: Literal["bridge_transfer", "cancel_transfer"]
    """The action to take when the transfer agent times out without making a decision.

    Defaults to cancel_transfer.
    """

    transfer_agent: ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent
    """The agent that will mediate the transfer decision."""

    transfer_timeout_ms: float
    """
    The maximum time to wait for the transfer agent to make a decision, in
    milliseconds. Defaults to 30000 (30 seconds).
    """


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption: TypeAlias = Union[
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt,
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer(
    TypedDict, total=False
):
    agentic_transfer_config: Required[
        ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig
    ]
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    type: Required[Literal["agentic_warm_transfer"]]
    """The type of the transfer."""

    enable_bridge_audio_cue: bool
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    on_hold_music: Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]
    """The music to play while the caller is being transferred."""

    public_handoff_option: (
        ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption
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

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


ComponentNodeSubagentNodeToolTransferCallToolTransferOption: TypeAlias = Union[
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionColdTransfer,
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransfer,
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer,
]


class ComponentNodeSubagentNodeToolTransferCallTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    transfer_destination: Required[ComponentNodeSubagentNodeToolTransferCallToolTransferDestination]

    transfer_option: Required[ComponentNodeSubagentNodeToolTransferCallToolTransferOption]

    type: Required[Literal["transfer_call"]]

    custom_sip_headers: Dict[str, str]
    """Custom SIP headers to be added to the call."""

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: str
    """Describes what to say to user when transferring the call.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    ignore_e164_validation: bool
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    speak_during_execution: bool
    """If true, will speak during execution."""


class ComponentNodeSubagentNodeToolCheckAvailabilityCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: Required[Union[float, str]]
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for. Can be a number or a dynamic variable in the format
    `{{variable_name}}` that will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """


class ComponentNodeSubagentNodeToolBookAppointmentCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: Required[Union[float, str]]
    """Cal.com event type id number for the cal.com event you want to book appointment.

    Can be a number or a dynamic variable in the format `{{variable_name}}` that
    will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """


class ComponentNodeSubagentNodeToolAgentSwapTool(TypedDict, total=False):
    agent_id: Required[str]
    """The id of the agent to swap to."""

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    post_call_analysis_setting: Required[Literal["both_agents", "only_destination_agent"]]
    """Post call analysis setting for the agent swap."""

    type: Required[Literal["agent_swap"]]

    agent_version: float
    """The version of the agent to swap to.

    If not specified, will use the latest version.
    """

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: str
    """The message for the agent to speak when executing agent swap."""

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    keep_current_language: bool
    """If true, keep the current language when swapping agents. Defaults to false."""

    keep_current_voice: bool
    """If true, keep the current voice when swapping agents. Defaults to false."""

    speak_during_execution: bool

    webhook_setting: Literal["both_agents", "only_destination_agent", "only_source_agent"]
    """Webhook setting for the agent swap, defaults to only source."""


class ComponentNodeSubagentNodeToolPressDigitTool(TypedDict, total=False):
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


class ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentPredefined(TypedDict, total=False):
    content: str
    """The static message to be sent in the SMS. Can contain dynamic variables."""

    type: Literal["predefined"]


class ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentInferred(TypedDict, total=False):
    prompt: str
    """The prompt to be used to help infer the SMS content.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right message to send. Can contain dynamic variables.
    """

    type: Literal["inferred"]


class ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentTemplate(TypedDict, total=False):
    template: Required[Literal["info_collection"]]
    """The template to use for the SMS content.

    "info_collection" sends a predefined message requesting information from the
    user.
    """

    type: Required[Literal["template"]]


ComponentNodeSubagentNodeToolSendSMSToolSMSContent: TypeAlias = Union[
    ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentPredefined,
    ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentInferred,
    ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentTemplate,
]


class ComponentNodeSubagentNodeToolSendSMSTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    sms_content: Required[ComponentNodeSubagentNodeToolSendSMSToolSMSContent]

    type: Required[Literal["send_sms"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: str
    """Describes what to say before sending the SMS.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: bool
    """If true, the agent will speak a short line before sending the SMS.

    If omitted, defaults to true (same as end_call / transfer_call tools).
    """


class ComponentNodeSubagentNodeToolCustomToolParameters(TypedDict, total=False):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

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


class ComponentNodeSubagentNodeToolCustomTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["custom"]]

    url: Required[str]
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    args_at_root: bool
    """
    If set to true, the parameters will be passed as root level JSON object instead
    of nested under "args".
    """

    description: str
    """Describes what this tool does and when to call this tool."""

    enable_typing_sound: bool
    """
    If true, play a typing sound on the agent audio track while this tool is
    executing. Useful when the tool takes a noticeable amount of time to prevent
    silence on the call.
    """

    execution_message_description: str
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    headers: Dict[str, str]
    """Headers to add to the request."""

    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
    """Method to use for the request, default to POST."""

    parameters: ComponentNodeSubagentNodeToolCustomToolParameters
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format. Omitting parameters defines a function with
    an empty parameter list.
    """

    query_params: Dict[str, str]
    """Query parameters to append to the request URL."""

    response_variables: Dict[str, str]
    """A mapping of variable names to JSON paths in the response body.

    These values will be extracted from the response and made available as dynamic
    variables for use.
    """

    speak_after_execution: bool
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: bool
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """

    timeout_ms: int
    """The maximum time in milliseconds the tool can run before it's considered
    timeout.

    If the tool times out, the agent would have that info. The minimum value allowed
    is 1000 ms (1 s), and maximum value allowed is 600,000 ms (10 min). By default,
    this is set to 120,000 ms (2 min).
    """


class ComponentNodeSubagentNodeToolCodeTool(TypedDict, total=False):
    code: Required[str]
    """JavaScript code to execute in the sandbox."""

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["code"]]

    description: str
    """Describes what this tool does and when to call this tool."""

    enable_typing_sound: bool
    """
    If true, play a typing sound on the agent audio track while this tool is
    executing.
    """

    execution_message_description: str
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    response_variables: Dict[str, str]
    """A mapping of variable names to JSON paths in the code execution result.

    These mapped values will be extracted and added as dynamic variables.
    """

    speak_after_execution: bool
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained.
    """

    speak_during_execution: bool
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the tool.
    """

    timeout_ms: int
    """The maximum time in milliseconds the code can run before it's considered
    timeout.

    Defaults to 30,000 ms (30 s).
    """


class ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableStringAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["string"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    examples: SequenceNotStr[str]
    """Examples of the variable value to teach model the style and syntax."""

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableEnumAnalysisData(TypedDict, total=False):
    choices: Required[SequenceNotStr[str]]
    """The possible values of the variable, must be non empty array."""

    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["enum"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableBooleanAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["boolean"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableNumberAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["number"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariable: TypeAlias = Union[
    ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableStringAnalysisData,
    ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableEnumAnalysisData,
    ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableBooleanAnalysisData,
    ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableNumberAnalysisData,
]


class ComponentNodeSubagentNodeToolExtractDynamicVariableTool(TypedDict, total=False):
    description: Required[str]
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["extract_dynamic_variable"]]

    variables: Required[Iterable[ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariable]]
    """The variables to be extracted."""


class ComponentNodeSubagentNodeToolBridgeTransferTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["bridge_transfer"]]

    description: str
    """Describes what the tool does.

    This tool is only available to transfer agents (agents with isTransferAgent set
    to true) in agentic warm transfer mode. When invoked, it bridges the original
    caller to the transfer target and ends the transfer agent call.
    """

    execution_message_description: str
    """Describes what to say to user when bridging the transfer.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: bool
    """If true, will speak during execution."""


class ComponentNodeSubagentNodeToolCancelTransferTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["cancel_transfer"]]

    description: str
    """Describes what the tool does.

    This tool is only available to transfer agents (agents with isTransferAgent set
    to true) in agentic warm transfer mode. When invoked, it cancels the transfer,
    returns the original caller to the main agent, and ends the transfer agent call.
    """

    execution_message_description: str
    """Describes what to say to user when cancelling the transfer.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: bool
    """If true, will speak during execution."""


class ComponentNodeSubagentNodeToolMcpTool(TypedDict, total=False):
    description: Required[str]
    """Description of the MCP tool."""

    name: Required[str]
    """Name of the MCP tool."""

    type: Required[Literal["mcp"]]

    enable_typing_sound: bool
    """
    If true, play a typing sound on the agent audio track while this MCP tool is
    executing.
    """

    execution_message_description: str
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    input_schema: Dict[str, str]
    """The input schema of the MCP tool."""

    mcp_id: str
    """Unique id of the MCP."""

    response_variables: Dict[str, str]
    """
    Response variables to add to dynamic variables, key is the variable name, value
    is the path to the variable in the response
    """

    speak_after_execution: bool
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: bool
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """


ComponentNodeSubagentNodeTool: TypeAlias = Union[
    ComponentNodeSubagentNodeToolEndCallTool,
    ComponentNodeSubagentNodeToolTransferCallTool,
    ComponentNodeSubagentNodeToolCheckAvailabilityCalTool,
    ComponentNodeSubagentNodeToolBookAppointmentCalTool,
    ComponentNodeSubagentNodeToolAgentSwapTool,
    ComponentNodeSubagentNodeToolPressDigitTool,
    ComponentNodeSubagentNodeToolSendSMSTool,
    ComponentNodeSubagentNodeToolCustomTool,
    ComponentNodeSubagentNodeToolCodeTool,
    ComponentNodeSubagentNodeToolExtractDynamicVariableTool,
    ComponentNodeSubagentNodeToolBridgeTransferTool,
    ComponentNodeSubagentNodeToolCancelTransferTool,
    ComponentNodeSubagentNodeToolMcpTool,
]


class ComponentNodeSubagentNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    instruction: Required[ComponentNodeSubagentNodeInstruction]

    type: Required[Literal["subagent"]]
    """Type of the node"""

    always_edge: ComponentNodeSubagentNodeAlwaysEdge

    display_position: ComponentNodeSubagentNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[ComponentNodeSubagentNodeEdge]

    finetune_conversation_examples: Iterable[ComponentNodeSubagentNodeFinetuneConversationExample]

    finetune_transition_examples: Iterable[ComponentNodeSubagentNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodeSubagentNodeGlobalNodeSetting

    interruption_sensitivity: Optional[float]

    knowledge_base_ids: Optional[SequenceNotStr[str]]
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    model_choice: ComponentNodeSubagentNodeModelChoice

    name: str
    """Optional name for display purposes"""

    responsiveness: Optional[float]

    skip_response_edge: ComponentNodeSubagentNodeSkipResponseEdge

    tool_ids: Optional[SequenceNotStr[str]]
    """
    The tool ids of the tools defined in main conversation flow or component that
    can be used in this subagent node.
    """

    tools: Optional[Iterable[ComponentNodeSubagentNodeTool]]
    """The tools owned by this subagent node.

    This includes other tool types like transfer_call, agent_swap, etc.
    """

    voice_speed: Optional[float]


class ComponentNodeEndNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeEndNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeEndNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class ComponentNodeEndNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    model_choice: ComponentNodeEndNodeModelChoice

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


class ComponentNodeFunctionNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeFunctionNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeFunctionNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeFunctionNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class ComponentNodeFunctionNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


ComponentNodeFunctionNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeFunctionNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeFunctionNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeFunctionNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeFunctionNodeElseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeFunctionNodeElseEdgeTransitionCondition]

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


class ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeFunctionNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeFunctionNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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

    else_edge: ComponentNodeFunctionNodeElseEdge

    enable_typing_sound: bool
    """If true, play a typing sound while this function executes."""

    finetune_transition_examples: Iterable[ComponentNodeFunctionNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodeFunctionNodeGlobalNodeSetting

    instruction: ComponentNodeFunctionNodeInstruction

    model_choice: ComponentNodeFunctionNodeModelChoice

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """Whether to speak during tool execution"""


class ComponentNodeCodeNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeCodeNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeCodeNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeCodeNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeCodeNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeCodeNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeCodeNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeCodeNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeCodeNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeCodeNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeCodeNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeCodeNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeCodeNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeCodeNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class ComponentNodeCodeNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


ComponentNodeCodeNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeCodeNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeCodeNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeCodeNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeCodeNodeElseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeCodeNodeElseEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeCodeNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeCodeNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodeCodeNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeCodeNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class ComponentNodeCodeNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeCodeNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeCodeNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeCodeNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


ComponentNodeCodeNodeInstruction: TypeAlias = Union[
    ComponentNodeCodeNodeInstructionNodeInstructionPrompt, ComponentNodeCodeNodeInstructionNodeInstructionStaticText
]


class ComponentNodeCodeNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeCodeNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    code: Required[str]
    """JavaScript code to execute in the sandbox."""

    type: Required[Literal["code"]]
    """Type of the node"""

    wait_for_result: Required[bool]
    """Whether to wait for code execution result"""

    display_position: ComponentNodeCodeNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[ComponentNodeCodeNodeEdge]

    else_edge: ComponentNodeCodeNodeElseEdge

    enable_typing_sound: bool
    """If true, play a typing sound while code executes."""

    finetune_transition_examples: Iterable[ComponentNodeCodeNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodeCodeNodeGlobalNodeSetting

    instruction: ComponentNodeCodeNodeInstruction

    model_choice: ComponentNodeCodeNodeModelChoice

    name: str
    """Optional name for display purposes"""

    response_variables: Dict[str, str]
    """A mapping of variable names to JSON paths in the code execution result.

    These mapped values will be extracted and added as dynamic variables.
    """

    speak_during_execution: bool
    """Whether to speak during code execution"""

    timeout_ms: int
    """The maximum time in milliseconds the code can run before it's considered
    timeout.

    Defaults to 30,000 ms (30 s).
    """


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

    cold_transfer_mode: Literal["sip_refer", "sip_invite"]
    """The mode of the cold transfer.

    If set to `sip_refer`, will use SIP REFER to transfer the call. If set to
    `sip_invite`, will use SIP INVITE to transfer the call.
    """

    show_transferee_as_caller: bool
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring. Requires the telephony side to support caller id override. Retell
    Twilio numbers support this option. This parameter takes effect only when
    `cold_transfer_mode` is set to `sip_invite`. When using `sip_refer`, this option
    is not available. Retell Twilio numbers always use user's number as the caller
    id when using `sip refer` cold transfer mode.
    """

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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


class ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[
            ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
        ]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeTransferCallNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeTransferCallNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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


class ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[
            ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
        ]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodePressDigitNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodePressDigitNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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


class ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeBranchNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeBranchNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeBranchNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    model_choice: ComponentNodeBranchNodeModelChoice

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


class ComponentNodeSMSNodeInstructionSMSInstructionTemplate(TypedDict, total=False):
    template: Required[Literal["info_collection"]]
    """The template to use for the instruction.

    "info_collection" sends a predefined message requesting information from the
    user.
    """

    type: Required[Literal["template"]]
    """Type of instruction"""


ComponentNodeSMSNodeInstruction: TypeAlias = Union[
    ComponentNodeSMSNodeInstructionNodeInstructionPrompt,
    ComponentNodeSMSNodeInstructionNodeInstructionStaticText,
    ComponentNodeSMSNodeInstructionSMSInstructionTemplate,
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


class ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeSMSNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeSMSNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeSMSNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    model_choice: ComponentNodeSMSNodeModelChoice

    name: str
    """Optional name for display purposes"""


class ComponentNodeExtractDynamicVariablesNodeVariableStringAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["string"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    examples: SequenceNotStr[str]
    """Examples of the variable value to teach model the style and syntax."""

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class ComponentNodeExtractDynamicVariablesNodeVariableEnumAnalysisData(TypedDict, total=False):
    choices: Required[SequenceNotStr[str]]
    """The possible values of the variable, must be non empty array."""

    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["enum"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class ComponentNodeExtractDynamicVariablesNodeVariableBooleanAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["boolean"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class ComponentNodeExtractDynamicVariablesNodeVariableNumberAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["number"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


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


class ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeExtractDynamicVariablesNodeElseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionCondition]

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


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[
            ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
        ]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[
        ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionCondition
    ]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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

    else_edge: ComponentNodeExtractDynamicVariablesNodeElseEdge

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


class ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class ComponentNodeAgentSwapNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    keep_current_language: bool
    """If true, keep the current language when swapping agents. Defaults to false."""

    keep_current_voice: bool
    """If true, keep the current voice when swapping agents. Defaults to false."""

    model_choice: ComponentNodeAgentSwapNodeModelChoice

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


class ComponentNodeMcpNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeMcpNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeMcpNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[ComponentNodeMcpNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class ComponentNodeMcpNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


ComponentNodeMcpNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeMcpNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeMcpNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeMcpNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeMcpNodeElseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeMcpNodeElseEdgeTransitionCondition]

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


class ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeMcpNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeMcpNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class ComponentNodeMcpNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    else_edge: ComponentNodeMcpNodeElseEdge

    enable_typing_sound: bool
    """If true, play a typing sound while MCP tool executes."""

    finetune_transition_examples: Iterable[ComponentNodeMcpNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodeMcpNodeGlobalNodeSetting

    instruction: ComponentNodeMcpNodeInstruction
    """What to say when calling the function, only used when speak during execution"""

    model_choice: ComponentNodeMcpNodeModelChoice

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


class ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


ComponentNodeComponentNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeComponentNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[ComponentNodeComponentNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeComponentNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionCondition]

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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeComponentNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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

    finetune_transition_examples: Iterable[ComponentNodeComponentNodeFinetuneTransitionExample]

    global_node_setting: ComponentNodeComponentNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class ComponentNodeBridgeTransferNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[
            ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
        ]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeBridgeTransferNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeBridgeTransferNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


ComponentNodeBridgeTransferNodeInstruction: TypeAlias = Union[
    ComponentNodeBridgeTransferNodeInstructionNodeInstructionPrompt,
    ComponentNodeBridgeTransferNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeBridgeTransferNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeBridgeTransferNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["bridge_transfer"]]
    """Type of the node - initiates a warm transfer by bridging the call"""

    display_position: ComponentNodeBridgeTransferNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: ComponentNodeBridgeTransferNodeGlobalNodeSetting

    instruction: ComponentNodeBridgeTransferNodeInstruction
    """Describes what to say to user when bridging the transfer.

    Only applicable when speak_during_execution is true.
    """

    model_choice: ComponentNodeBridgeTransferNodeModelChoice

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """If true, will speak during execution"""


class ComponentNodeCancelTransferNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[
            ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
        ]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class ComponentNodeCancelTransferNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class ComponentNodeCancelTransferNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


ComponentNodeCancelTransferNodeInstruction: TypeAlias = Union[
    ComponentNodeCancelTransferNodeInstructionNodeInstructionPrompt,
    ComponentNodeCancelTransferNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeCancelTransferNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeCancelTransferNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["cancel_transfer"]]
    """Type of the node - cancels the warm transfer and ends the transfer agent call"""

    display_position: ComponentNodeCancelTransferNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: ComponentNodeCancelTransferNodeGlobalNodeSetting

    instruction: ComponentNodeCancelTransferNodeInstruction
    """Describes what to say to user when cancelling the transfer.

    Only applicable when speak_during_execution is true.
    """

    model_choice: ComponentNodeCancelTransferNodeModelChoice

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """If true, will speak during execution"""


ComponentNode: TypeAlias = Union[
    ComponentNodeConversationNode,
    ComponentNodeSubagentNode,
    ComponentNodeEndNode,
    ComponentNodeFunctionNode,
    ComponentNodeCodeNode,
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


class ComponentNoteDisplayPosition(TypedDict, total=False):
    """Position of the note on the canvas."""

    x: float

    y: float


class ComponentNoteSize(TypedDict, total=False):
    """Dimensions of the note on the canvas."""

    height: float

    width: float


class ComponentNote(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the note."""

    content: Required[str]
    """
    Text content of the note, can contain refs to images in the format
    "<image:asset_id>"
    """

    display_position: Required[ComponentNoteDisplayPosition]
    """Position of the note on the canvas."""

    size: Required[ComponentNoteSize]
    """Dimensions of the note on the canvas."""


class ComponentToolCustomToolParameters(TypedDict, total=False):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

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


class ComponentToolCustomTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["custom"]]

    url: Required[str]
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    args_at_root: bool
    """
    If set to true, the parameters will be passed as root level JSON object instead
    of nested under "args".
    """

    description: str
    """Describes what this tool does and when to call this tool."""

    enable_typing_sound: bool
    """
    If true, play a typing sound on the agent audio track while this tool is
    executing. Useful when the tool takes a noticeable amount of time to prevent
    silence on the call.
    """

    execution_message_description: str
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    headers: Dict[str, str]
    """Headers to add to the request."""

    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
    """Method to use for the request, default to POST."""

    parameters: ComponentToolCustomToolParameters
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format. Omitting parameters defines a function with
    an empty parameter list.
    """

    query_params: Dict[str, str]
    """Query parameters to append to the request URL."""

    response_variables: Dict[str, str]
    """A mapping of variable names to JSON paths in the response body.

    These values will be extracted from the response and made available as dynamic
    variables for use.
    """

    speak_after_execution: bool
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: bool
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """

    timeout_ms: int
    """The maximum time in milliseconds the tool can run before it's considered
    timeout.

    If the tool times out, the agent would have that info. The minimum value allowed
    is 1000 ms (1 s), and maximum value allowed is 600,000 ms (10 min). By default,
    this is set to 120,000 ms (2 min).
    """

    tool_id: str
    """Unique identifier for the tool"""


class ComponentToolCheckAvailabilityCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: Required[Union[float, str]]
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for. Can be a number or a dynamic variable in the format
    `{{variable_name}}` that will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """

    tool_id: str
    """Unique identifier for the tool"""


class ComponentToolBookAppointmentCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: Required[Union[float, str]]
    """Cal.com event type id number for the cal.com event you want to book appointment.

    Can be a number or a dynamic variable in the format `{{variable_name}}` that
    will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """

    tool_id: str
    """Unique identifier for the tool"""


ComponentTool: TypeAlias = Union[
    ComponentToolCustomTool, ComponentToolCheckAvailabilityCalTool, ComponentToolBookAppointmentCalTool
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

    notes: Optional[Iterable[ComponentNote]]
    """Visual annotations displayed on the flow canvas."""

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


class ModelChoice(TypedDict, total=False):
    """The model choice for the conversation flow."""

    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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


class NodeConversationNodeAlwaysEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeConversationNodeAlwaysEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeConversationNodeAlwaysEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeConversationNodeAlwaysEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Always"]
    """Must be "Always" for always edge"""


class NodeConversationNodeAlwaysEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Always"]]
    """Must be "Always" for always edge"""

    type: Required[Literal["prompt"]]


NodeConversationNodeAlwaysEdgeTransitionCondition: TypeAlias = Union[
    NodeConversationNodeAlwaysEdgeTransitionConditionPromptCondition,
    NodeConversationNodeAlwaysEdgeTransitionConditionEquationCondition,
    NodeConversationNodeAlwaysEdgeTransitionConditionUnionMember2,
]


class NodeConversationNodeAlwaysEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeConversationNodeAlwaysEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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


class NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeConversationNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeConversationNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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

    always_edge: NodeConversationNodeAlwaysEdge

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

    responsiveness: Optional[float]

    skip_response_edge: NodeConversationNodeSkipResponseEdge

    voice_speed: Optional[float]


class NodeSubagentNodeInstruction(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeSubagentNodeAlwaysEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeSubagentNodeAlwaysEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeSubagentNodeAlwaysEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeSubagentNodeAlwaysEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Always"]
    """Must be "Always" for always edge"""


class NodeSubagentNodeAlwaysEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Always"]]
    """Must be "Always" for always edge"""

    type: Required[Literal["prompt"]]


NodeSubagentNodeAlwaysEdgeTransitionCondition: TypeAlias = Union[
    NodeSubagentNodeAlwaysEdgeTransitionConditionPromptCondition,
    NodeSubagentNodeAlwaysEdgeTransitionConditionEquationCondition,
    NodeSubagentNodeAlwaysEdgeTransitionConditionUnionMember2,
]


class NodeSubagentNodeAlwaysEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeSubagentNodeAlwaysEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeSubagentNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodeSubagentNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeSubagentNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeSubagentNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeSubagentNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeSubagentNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeSubagentNodeEdgeTransitionConditionPromptCondition, NodeSubagentNodeEdgeTransitionConditionEquationCondition
]


class NodeSubagentNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeSubagentNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeSubagentNodeFinetuneConversationExampleTranscript: TypeAlias = Union[
    NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember0,
    NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember1,
    NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember2,
]


class NodeSubagentNodeFinetuneConversationExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodeSubagentNodeFinetuneConversationExampleTranscript]]
    """The example transcript to finetune how the conversation should be."""


class NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeSubagentNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeSubagentNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodeSubagentNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeSubagentNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeSubagentNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeSubagentNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeSubagentNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeSubagentNodeSkipResponseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeSubagentNodeSkipResponseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeSubagentNodeSkipResponseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeSubagentNodeSkipResponseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Skip response"]
    """Must be "Skip response" for skip response edge"""


class NodeSubagentNodeSkipResponseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Skip response"]]
    """Must be "Skip response" for skip response edge"""

    type: Required[Literal["prompt"]]


NodeSubagentNodeSkipResponseEdgeTransitionCondition: TypeAlias = Union[
    NodeSubagentNodeSkipResponseEdgeTransitionConditionPromptCondition,
    NodeSubagentNodeSkipResponseEdgeTransitionConditionEquationCondition,
    NodeSubagentNodeSkipResponseEdgeTransitionConditionUnionMember2,
]


class NodeSubagentNodeSkipResponseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeSubagentNodeSkipResponseEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeSubagentNodeToolEndCallTool(TypedDict, total=False):
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

    execution_message_description: str
    """Describes what to say to user when ending the call.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: bool
    """If true, will speak during execution."""


class NodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationPredefined(TypedDict, total=False):
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


class NodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationInferred(TypedDict, total=False):
    prompt: Required[str]
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Required[Literal["inferred"]]
    """The type of transfer destination."""


NodeSubagentNodeToolTransferCallToolTransferDestination: TypeAlias = Union[
    NodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationPredefined,
    NodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationInferred,
]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionColdTransfer(TypedDict, total=False):
    type: Required[Literal["cold_transfer"]]
    """The type of the transfer."""

    cold_transfer_mode: Literal["sip_refer", "sip_invite"]
    """The mode of the cold transfer.

    If set to `sip_refer`, will use SIP REFER to transfer the call. If set to
    `sip_invite`, will use SIP INVITE to transfer the call.
    """

    show_transferee_as_caller: bool
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring. Requires the telephony side to support caller id override. Retell
    Twilio numbers support this option. This parameter takes effect only when
    `cold_transfer_mode` is set to `sip_invite`. When using `sip_refer`, this option
    is not available. Retell Twilio numbers always use user's number as the caller
    id when using `sip refer` cold transfer mode.
    """

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption(TypedDict, total=False):
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption: TypeAlias = Union[
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt,
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage,
]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption: TypeAlias = Union[
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt,
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransfer(TypedDict, total=False):
    type: Required[Literal["warm_transfer"]]
    """The type of the transfer."""

    agent_detection_timeout_ms: float
    """The time to wait before considering transfer fails."""

    enable_bridge_audio_cue: bool
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    ivr_option: NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    on_hold_music: Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]
    """The music to play while the caller is being transferred."""

    opt_out_human_detection: bool
    """If set to true, will not perform human detection for the transfer.

    Default to false.
    """

    private_handoff_option: (
        NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption
    )
    """
    If set, when transfer is connected, will say the handoff message only to the
    agent receiving the transfer. Can leave either a static message or a dynamic one
    based on prompt. Set to null to disable warm handoff.
    """

    public_handoff_option: (
        NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption
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

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent(
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


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig(
    TypedDict, total=False
):
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    action_on_timeout: Literal["bridge_transfer", "cancel_transfer"]
    """The action to take when the transfer agent times out without making a decision.

    Defaults to cancel_transfer.
    """

    transfer_agent: NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent
    """The agent that will mediate the transfer decision."""

    transfer_timeout_ms: float
    """
    The maximum time to wait for the transfer agent to make a decision, in
    milliseconds. Defaults to 30000 (30 seconds).
    """


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt(
    TypedDict, total=False
):
    prompt: str
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["prompt"]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    TypedDict, total=False
):
    message: str
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Literal["static_message"]


NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption: TypeAlias = Union[
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt,
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer(TypedDict, total=False):
    agentic_transfer_config: Required[
        NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig
    ]
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    type: Required[Literal["agentic_warm_transfer"]]
    """The type of the transfer."""

    enable_bridge_audio_cue: bool
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    on_hold_music: Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]
    """The music to play while the caller is being transferred."""

    public_handoff_option: (
        NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption
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

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


NodeSubagentNodeToolTransferCallToolTransferOption: TypeAlias = Union[
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionColdTransfer,
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransfer,
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer,
]


class NodeSubagentNodeToolTransferCallTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    transfer_destination: Required[NodeSubagentNodeToolTransferCallToolTransferDestination]

    transfer_option: Required[NodeSubagentNodeToolTransferCallToolTransferOption]

    type: Required[Literal["transfer_call"]]

    custom_sip_headers: Dict[str, str]
    """Custom SIP headers to be added to the call."""

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: str
    """Describes what to say to user when transferring the call.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    ignore_e164_validation: bool
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    speak_during_execution: bool
    """If true, will speak during execution."""


class NodeSubagentNodeToolCheckAvailabilityCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: Required[Union[float, str]]
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for. Can be a number or a dynamic variable in the format
    `{{variable_name}}` that will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """


class NodeSubagentNodeToolBookAppointmentCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: Required[Union[float, str]]
    """Cal.com event type id number for the cal.com event you want to book appointment.

    Can be a number or a dynamic variable in the format `{{variable_name}}` that
    will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """


class NodeSubagentNodeToolAgentSwapTool(TypedDict, total=False):
    agent_id: Required[str]
    """The id of the agent to swap to."""

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    post_call_analysis_setting: Required[Literal["both_agents", "only_destination_agent"]]
    """Post call analysis setting for the agent swap."""

    type: Required[Literal["agent_swap"]]

    agent_version: float
    """The version of the agent to swap to.

    If not specified, will use the latest version.
    """

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: str
    """The message for the agent to speak when executing agent swap."""

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    keep_current_language: bool
    """If true, keep the current language when swapping agents. Defaults to false."""

    keep_current_voice: bool
    """If true, keep the current voice when swapping agents. Defaults to false."""

    speak_during_execution: bool

    webhook_setting: Literal["both_agents", "only_destination_agent", "only_source_agent"]
    """Webhook setting for the agent swap, defaults to only source."""


class NodeSubagentNodeToolPressDigitTool(TypedDict, total=False):
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


class NodeSubagentNodeToolSendSMSToolSMSContentSMSContentPredefined(TypedDict, total=False):
    content: str
    """The static message to be sent in the SMS. Can contain dynamic variables."""

    type: Literal["predefined"]


class NodeSubagentNodeToolSendSMSToolSMSContentSMSContentInferred(TypedDict, total=False):
    prompt: str
    """The prompt to be used to help infer the SMS content.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right message to send. Can contain dynamic variables.
    """

    type: Literal["inferred"]


class NodeSubagentNodeToolSendSMSToolSMSContentSMSContentTemplate(TypedDict, total=False):
    template: Required[Literal["info_collection"]]
    """The template to use for the SMS content.

    "info_collection" sends a predefined message requesting information from the
    user.
    """

    type: Required[Literal["template"]]


NodeSubagentNodeToolSendSMSToolSMSContent: TypeAlias = Union[
    NodeSubagentNodeToolSendSMSToolSMSContentSMSContentPredefined,
    NodeSubagentNodeToolSendSMSToolSMSContentSMSContentInferred,
    NodeSubagentNodeToolSendSMSToolSMSContentSMSContentTemplate,
]


class NodeSubagentNodeToolSendSMSTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    sms_content: Required[NodeSubagentNodeToolSendSMSToolSMSContent]

    type: Required[Literal["send_sms"]]

    description: str
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    execution_message_description: str
    """Describes what to say before sending the SMS.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: bool
    """If true, the agent will speak a short line before sending the SMS.

    If omitted, defaults to true (same as end_call / transfer_call tools).
    """


class NodeSubagentNodeToolCustomToolParameters(TypedDict, total=False):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

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


class NodeSubagentNodeToolCustomTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["custom"]]

    url: Required[str]
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    args_at_root: bool
    """
    If set to true, the parameters will be passed as root level JSON object instead
    of nested under "args".
    """

    description: str
    """Describes what this tool does and when to call this tool."""

    enable_typing_sound: bool
    """
    If true, play a typing sound on the agent audio track while this tool is
    executing. Useful when the tool takes a noticeable amount of time to prevent
    silence on the call.
    """

    execution_message_description: str
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    headers: Dict[str, str]
    """Headers to add to the request."""

    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
    """Method to use for the request, default to POST."""

    parameters: NodeSubagentNodeToolCustomToolParameters
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format. Omitting parameters defines a function with
    an empty parameter list.
    """

    query_params: Dict[str, str]
    """Query parameters to append to the request URL."""

    response_variables: Dict[str, str]
    """A mapping of variable names to JSON paths in the response body.

    These values will be extracted from the response and made available as dynamic
    variables for use.
    """

    speak_after_execution: bool
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: bool
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """

    timeout_ms: int
    """The maximum time in milliseconds the tool can run before it's considered
    timeout.

    If the tool times out, the agent would have that info. The minimum value allowed
    is 1000 ms (1 s), and maximum value allowed is 600,000 ms (10 min). By default,
    this is set to 120,000 ms (2 min).
    """


class NodeSubagentNodeToolCodeTool(TypedDict, total=False):
    code: Required[str]
    """JavaScript code to execute in the sandbox."""

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["code"]]

    description: str
    """Describes what this tool does and when to call this tool."""

    enable_typing_sound: bool
    """
    If true, play a typing sound on the agent audio track while this tool is
    executing.
    """

    execution_message_description: str
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    response_variables: Dict[str, str]
    """A mapping of variable names to JSON paths in the code execution result.

    These mapped values will be extracted and added as dynamic variables.
    """

    speak_after_execution: bool
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained.
    """

    speak_during_execution: bool
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the tool.
    """

    timeout_ms: int
    """The maximum time in milliseconds the code can run before it's considered
    timeout.

    Defaults to 30,000 ms (30 s).
    """


class NodeSubagentNodeToolExtractDynamicVariableToolVariableStringAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["string"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    examples: SequenceNotStr[str]
    """Examples of the variable value to teach model the style and syntax."""

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class NodeSubagentNodeToolExtractDynamicVariableToolVariableEnumAnalysisData(TypedDict, total=False):
    choices: Required[SequenceNotStr[str]]
    """The possible values of the variable, must be non empty array."""

    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["enum"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class NodeSubagentNodeToolExtractDynamicVariableToolVariableBooleanAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["boolean"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class NodeSubagentNodeToolExtractDynamicVariableToolVariableNumberAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["number"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


NodeSubagentNodeToolExtractDynamicVariableToolVariable: TypeAlias = Union[
    NodeSubagentNodeToolExtractDynamicVariableToolVariableStringAnalysisData,
    NodeSubagentNodeToolExtractDynamicVariableToolVariableEnumAnalysisData,
    NodeSubagentNodeToolExtractDynamicVariableToolVariableBooleanAnalysisData,
    NodeSubagentNodeToolExtractDynamicVariableToolVariableNumberAnalysisData,
]


class NodeSubagentNodeToolExtractDynamicVariableTool(TypedDict, total=False):
    description: Required[str]
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["extract_dynamic_variable"]]

    variables: Required[Iterable[NodeSubagentNodeToolExtractDynamicVariableToolVariable]]
    """The variables to be extracted."""


class NodeSubagentNodeToolBridgeTransferTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["bridge_transfer"]]

    description: str
    """Describes what the tool does.

    This tool is only available to transfer agents (agents with isTransferAgent set
    to true) in agentic warm transfer mode. When invoked, it bridges the original
    caller to the transfer target and ends the transfer agent call.
    """

    execution_message_description: str
    """Describes what to say to user when bridging the transfer.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: bool
    """If true, will speak during execution."""


class NodeSubagentNodeToolCancelTransferTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state transitions). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["cancel_transfer"]]

    description: str
    """Describes what the tool does.

    This tool is only available to transfer agents (agents with isTransferAgent set
    to true) in agentic warm transfer mode. When invoked, it cancels the transfer,
    returns the original caller to the main agent, and ends the transfer agent call.
    """

    execution_message_description: str
    """Describes what to say to user when cancelling the transfer.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: bool
    """If true, will speak during execution."""


class NodeSubagentNodeToolMcpTool(TypedDict, total=False):
    description: Required[str]
    """Description of the MCP tool."""

    name: Required[str]
    """Name of the MCP tool."""

    type: Required[Literal["mcp"]]

    enable_typing_sound: bool
    """
    If true, play a typing sound on the agent audio track while this MCP tool is
    executing.
    """

    execution_message_description: str
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    input_schema: Dict[str, str]
    """The input schema of the MCP tool."""

    mcp_id: str
    """Unique id of the MCP."""

    response_variables: Dict[str, str]
    """
    Response variables to add to dynamic variables, key is the variable name, value
    is the path to the variable in the response
    """

    speak_after_execution: bool
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: bool
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """


NodeSubagentNodeTool: TypeAlias = Union[
    NodeSubagentNodeToolEndCallTool,
    NodeSubagentNodeToolTransferCallTool,
    NodeSubagentNodeToolCheckAvailabilityCalTool,
    NodeSubagentNodeToolBookAppointmentCalTool,
    NodeSubagentNodeToolAgentSwapTool,
    NodeSubagentNodeToolPressDigitTool,
    NodeSubagentNodeToolSendSMSTool,
    NodeSubagentNodeToolCustomTool,
    NodeSubagentNodeToolCodeTool,
    NodeSubagentNodeToolExtractDynamicVariableTool,
    NodeSubagentNodeToolBridgeTransferTool,
    NodeSubagentNodeToolCancelTransferTool,
    NodeSubagentNodeToolMcpTool,
]


class NodeSubagentNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    instruction: Required[NodeSubagentNodeInstruction]

    type: Required[Literal["subagent"]]
    """Type of the node"""

    always_edge: NodeSubagentNodeAlwaysEdge

    display_position: NodeSubagentNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[NodeSubagentNodeEdge]

    finetune_conversation_examples: Iterable[NodeSubagentNodeFinetuneConversationExample]

    finetune_transition_examples: Iterable[NodeSubagentNodeFinetuneTransitionExample]

    global_node_setting: NodeSubagentNodeGlobalNodeSetting

    interruption_sensitivity: Optional[float]

    knowledge_base_ids: Optional[SequenceNotStr[str]]
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    model_choice: NodeSubagentNodeModelChoice

    name: str
    """Optional name for display purposes"""

    responsiveness: Optional[float]

    skip_response_edge: NodeSubagentNodeSkipResponseEdge

    tool_ids: Optional[SequenceNotStr[str]]
    """
    The tool ids of the tools defined in main conversation flow or component that
    can be used in this subagent node.
    """

    tools: Optional[Iterable[NodeSubagentNodeTool]]
    """The tools owned by this subagent node.

    This includes other tool types like transfer_call, agent_swap, etc.
    """

    voice_speed: Optional[float]


class NodeEndNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeEndNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeEndNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeEndNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeEndNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class NodeEndNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    model_choice: NodeEndNodeModelChoice

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


class NodeFunctionNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeFunctionNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeFunctionNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeFunctionNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class NodeFunctionNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


NodeFunctionNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeFunctionNodeElseEdgeTransitionConditionPromptCondition,
    NodeFunctionNodeElseEdgeTransitionConditionEquationCondition,
    NodeFunctionNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeFunctionNodeElseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeFunctionNodeElseEdgeTransitionCondition]

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


class NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeFunctionNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeFunctionNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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

    else_edge: NodeFunctionNodeElseEdge

    enable_typing_sound: bool
    """If true, play a typing sound while this function executes."""

    finetune_transition_examples: Iterable[NodeFunctionNodeFinetuneTransitionExample]

    global_node_setting: NodeFunctionNodeGlobalNodeSetting

    instruction: NodeFunctionNodeInstruction

    model_choice: NodeFunctionNodeModelChoice

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """Whether to speak during tool execution"""


class NodeCodeNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodeCodeNodeEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeCodeNodeEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeCodeNodeEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeCodeNodeEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeCodeNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeCodeNodeEdgeTransitionConditionPromptCondition, NodeCodeNodeEdgeTransitionConditionEquationCondition
]


class NodeCodeNodeEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeCodeNodeEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeCodeNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeCodeNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeCodeNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeCodeNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class NodeCodeNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


NodeCodeNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeCodeNodeElseEdgeTransitionConditionPromptCondition,
    NodeCodeNodeElseEdgeTransitionConditionEquationCondition,
    NodeCodeNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeCodeNodeElseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeCodeNodeElseEdgeTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeCodeNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeCodeNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodeCodeNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeCodeNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


class NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeCodeNodeGlobalNodeSettingNegativeFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeCodeNodeGlobalNodeSettingPositiveFinetuneExample(TypedDict, total=False):
    transcript: Required[Iterable[NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]]
    """Find tune the transition condition to this global node"""


class NodeCodeNodeGlobalNodeSetting(TypedDict, total=False):
    condition: Required[str]
    """Condition for global node activation, cannot be empty"""

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeCodeNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[NodeCodeNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeCodeNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeCodeNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeCodeNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


NodeCodeNodeInstruction: TypeAlias = Union[
    NodeCodeNodeInstructionNodeInstructionPrompt, NodeCodeNodeInstructionNodeInstructionStaticText
]


class NodeCodeNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeCodeNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    code: Required[str]
    """JavaScript code to execute in the sandbox."""

    type: Required[Literal["code"]]
    """Type of the node"""

    wait_for_result: Required[bool]
    """Whether to wait for code execution result"""

    display_position: NodeCodeNodeDisplayPosition
    """Position for frontend display"""

    edges: Iterable[NodeCodeNodeEdge]

    else_edge: NodeCodeNodeElseEdge

    enable_typing_sound: bool
    """If true, play a typing sound while code executes."""

    finetune_transition_examples: Iterable[NodeCodeNodeFinetuneTransitionExample]

    global_node_setting: NodeCodeNodeGlobalNodeSetting

    instruction: NodeCodeNodeInstruction

    model_choice: NodeCodeNodeModelChoice

    name: str
    """Optional name for display purposes"""

    response_variables: Dict[str, str]
    """A mapping of variable names to JSON paths in the code execution result.

    These mapped values will be extracted and added as dynamic variables.
    """

    speak_during_execution: bool
    """Whether to speak during code execution"""

    timeout_ms: int
    """The maximum time in milliseconds the code can run before it's considered
    timeout.

    Defaults to 30,000 ms (30 s).
    """


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

    cold_transfer_mode: Literal["sip_refer", "sip_invite"]
    """The mode of the cold transfer.

    If set to `sip_refer`, will use SIP REFER to transfer the call. If set to
    `sip_invite`, will use SIP INVITE to transfer the call.
    """

    show_transferee_as_caller: bool
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring. Requires the telephony side to support caller id override. Retell
    Twilio numbers support this option. This parameter takes effect only when
    `cold_transfer_mode` is set to `sip_invite`. When using `sip_refer`, this option
    is not available. Retell Twilio numbers always use user's number as the caller
    id when using `sip refer` cold transfer mode.
    """

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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

    transfer_ring_duration_ms: int
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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


class NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeTransferCallNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeTransferCallNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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


class NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodePressDigitNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodePressDigitNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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


class NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeBranchNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeBranchNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[NodeBranchNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeBranchNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeBranchNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    model_choice: NodeBranchNodeModelChoice

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


class NodeSMSNodeInstructionSMSInstructionTemplate(TypedDict, total=False):
    template: Required[Literal["info_collection"]]
    """The template to use for the instruction.

    "info_collection" sends a predefined message requesting information from the
    user.
    """

    type: Required[Literal["template"]]
    """Type of instruction"""


NodeSMSNodeInstruction: TypeAlias = Union[
    NodeSMSNodeInstructionNodeInstructionPrompt,
    NodeSMSNodeInstructionNodeInstructionStaticText,
    NodeSMSNodeInstructionSMSInstructionTemplate,
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


class NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeSMSNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeSMSNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[NodeSMSNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeSMSNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeSMSNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    model_choice: NodeSMSNodeModelChoice

    name: str
    """Optional name for display purposes"""


class NodeExtractDynamicVariablesNodeVariableStringAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["string"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    examples: SequenceNotStr[str]
    """Examples of the variable value to teach model the style and syntax."""

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class NodeExtractDynamicVariablesNodeVariableEnumAnalysisData(TypedDict, total=False):
    choices: Required[SequenceNotStr[str]]
    """The possible values of the variable, must be non empty array."""

    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["enum"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class NodeExtractDynamicVariablesNodeVariableBooleanAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["boolean"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


class NodeExtractDynamicVariablesNodeVariableNumberAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["number"]]
    """Type of the variable to extract."""

    conditional_prompt: str
    """
    Optional instruction to help decide whether this field needs to be populated in
    the analysis. If not set, the field is always included. If required is true,
    this is ignored.
    """

    required: bool
    """Whether this data is required.

    If true and the data is not extracted, the call will be marked as unsuccessful.
    """


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


class NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


NodeExtractDynamicVariablesNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionPromptCondition,
    NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationCondition,
    NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeExtractDynamicVariablesNodeElseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeExtractDynamicVariablesNodeElseEdgeTransitionCondition]

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


class NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    TypedDict, total=False
):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[
            NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
        ]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
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

    else_edge: NodeExtractDynamicVariablesNodeElseEdge

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


class NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeAgentSwapNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeAgentSwapNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class NodeAgentSwapNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    keep_current_language: bool
    """If true, keep the current language when swapping agents. Defaults to false."""

    keep_current_voice: bool
    """If true, keep the current voice when swapping agents. Defaults to false."""

    model_choice: NodeAgentSwapNodeModelChoice

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


class NodeMcpNodeElseEdgeTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeMcpNodeElseEdgeTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeMcpNodeElseEdgeTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[Iterable[NodeMcpNodeElseEdgeTransitionConditionEquationConditionEquation]]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]

    prompt: Literal["Else"]
    """Must be "Else" for else edge"""


class NodeMcpNodeElseEdgeTransitionConditionUnionMember2(TypedDict, total=False):
    prompt: Required[Literal["Else"]]
    """Must be "Else" for else edge"""

    type: Required[Literal["prompt"]]


NodeMcpNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeMcpNodeElseEdgeTransitionConditionPromptCondition,
    NodeMcpNodeElseEdgeTransitionConditionEquationCondition,
    NodeMcpNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeMcpNodeElseEdge(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeMcpNodeElseEdgeTransitionCondition]

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


class NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(TypedDict, total=False):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeMcpNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeMcpNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class NodeMcpNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    else_edge: NodeMcpNodeElseEdge

    enable_typing_sound: bool
    """If true, play a typing sound while MCP tool executes."""

    finetune_transition_examples: Iterable[NodeMcpNodeFinetuneTransitionExample]

    global_node_setting: NodeMcpNodeGlobalNodeSetting

    instruction: NodeMcpNodeInstruction
    """What to say when calling the function, only used when speak during execution"""

    model_choice: NodeMcpNodeModelChoice

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


class NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember0(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["agent", "user"]]


class NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember1(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]

    role: Required[Literal["tool_call_invocation"]]

    tool_call_id: Required[str]


class NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember2(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["tool_call_result"]]

    tool_call_id: Required[str]


NodeComponentNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeComponentNodeFinetuneTransitionExample(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the example"""

    transcript: Required[Iterable[NodeComponentNodeFinetuneTransitionExampleTranscript]]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: str
    """Optional destination node ID"""


class NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(TypedDict, total=False):
    equations: Required[
        Iterable[NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeComponentNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionCondition]

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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeComponentNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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

    finetune_transition_examples: Iterable[NodeComponentNodeFinetuneTransitionExample]

    global_node_setting: NodeComponentNodeGlobalNodeSetting

    name: str
    """Optional name for display purposes"""


class NodeBridgeTransferNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeBridgeTransferNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeBridgeTransferNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeBridgeTransferNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeBridgeTransferNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


NodeBridgeTransferNodeInstruction: TypeAlias = Union[
    NodeBridgeTransferNodeInstructionNodeInstructionPrompt, NodeBridgeTransferNodeInstructionNodeInstructionStaticText
]


class NodeBridgeTransferNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeBridgeTransferNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["bridge_transfer"]]
    """Type of the node - initiates a warm transfer by bridging the call"""

    display_position: NodeBridgeTransferNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: NodeBridgeTransferNodeGlobalNodeSetting

    instruction: NodeBridgeTransferNodeInstruction
    """Describes what to say to user when bridging the transfer.

    Only applicable when speak_during_execution is true.
    """

    model_choice: NodeBridgeTransferNodeModelChoice

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """If true, will speak during execution"""


class NodeCancelTransferNodeDisplayPosition(TypedDict, total=False):
    """Position for frontend display"""

    x: float

    y: float


class NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(TypedDict, total=False):
    prompt: Required[str]
    """Prompt condition text"""

    type: Required[Literal["prompt"]]


class NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    TypedDict, total=False
):
    left: Required[str]
    """Left side of the equation"""

    operator: Required[Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]]

    right: str
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    TypedDict, total=False
):
    equations: Required[
        Iterable[NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]
    ]

    operator: Required[Literal["||", "&&"]]

    type: Required[Literal["equation"]]


NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeCancelTransferNodeGlobalNodeSettingGoBackCondition(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the edge"""

    transition_condition: Required[NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition]

    destination_node_id: str
    """ID of the destination node"""


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

    cool_down: float
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Iterable[NodeCancelTransferNodeGlobalNodeSettingGoBackCondition]
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Iterable[NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    """Don't transition to this node"""

    positive_finetune_examples: Iterable[NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    """Transition to this node"""


class NodeCancelTransferNodeInstructionNodeInstructionPrompt(TypedDict, total=False):
    text: Required[str]
    """The prompt text for the instruction"""

    type: Required[Literal["prompt"]]
    """Type of instruction"""


class NodeCancelTransferNodeInstructionNodeInstructionStaticText(TypedDict, total=False):
    text: Required[str]
    """The static text for the instruction"""

    type: Required[Literal["static_text"]]
    """Type of instruction"""


NodeCancelTransferNodeInstruction: TypeAlias = Union[
    NodeCancelTransferNodeInstructionNodeInstructionPrompt, NodeCancelTransferNodeInstructionNodeInstructionStaticText
]


class NodeCancelTransferNodeModelChoice(TypedDict, total=False):
    model: Required[
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
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
            "gemini-3.1-flash-lite",
        ]
    ]
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeCancelTransferNode(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the node"""

    type: Required[Literal["cancel_transfer"]]
    """Type of the node - cancels the warm transfer and ends the transfer agent call"""

    display_position: NodeCancelTransferNodeDisplayPosition
    """Position for frontend display"""

    global_node_setting: NodeCancelTransferNodeGlobalNodeSetting

    instruction: NodeCancelTransferNodeInstruction
    """Describes what to say to user when cancelling the transfer.

    Only applicable when speak_during_execution is true.
    """

    model_choice: NodeCancelTransferNodeModelChoice

    name: str
    """Optional name for display purposes"""

    speak_during_execution: bool
    """If true, will speak during execution"""


Node: TypeAlias = Union[
    NodeConversationNode,
    NodeSubagentNode,
    NodeEndNode,
    NodeFunctionNode,
    NodeCodeNode,
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


class NoteDisplayPosition(TypedDict, total=False):
    """Position of the note on the canvas."""

    x: float

    y: float


class NoteSize(TypedDict, total=False):
    """Dimensions of the note on the canvas."""

    height: float

    width: float


class Note(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the note."""

    content: Required[str]
    """
    Text content of the note, can contain refs to images in the format
    "<image:asset_id>"
    """

    display_position: Required[NoteDisplayPosition]
    """Position of the note on the canvas."""

    size: Required[NoteSize]
    """Dimensions of the note on the canvas."""


class ToolCustomToolParameters(TypedDict, total=False):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

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


class ToolCustomTool(TypedDict, total=False):
    name: Required[str]
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Required[Literal["custom"]]

    url: Required[str]
    """
    Describes what the tool does, sometimes can also include information about when
    to call the tool.
    """

    args_at_root: bool
    """
    If set to true, the parameters will be passed as root level JSON object instead
    of nested under "args".
    """

    description: str
    """Describes what this tool does and when to call this tool."""

    enable_typing_sound: bool
    """
    If true, play a typing sound on the agent audio track while this tool is
    executing. Useful when the tool takes a noticeable amount of time to prevent
    silence on the call.
    """

    execution_message_description: str
    """The description for the sentence agent say during execution.

    Only applicable when speak_during_execution is true. Can write what to say or
    even provide examples. The default is "The message you will say to callee when
    calling this tool. Make sure it fits into the conversation smoothly.".
    """

    execution_message_type: Literal["prompt", "static_text"]
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    headers: Dict[str, str]
    """Headers to add to the request."""

    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
    """Method to use for the request, default to POST."""

    parameters: ToolCustomToolParameters
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format. Omitting parameters defines a function with
    an empty parameter list.
    """

    query_params: Dict[str, str]
    """Query parameters to append to the request URL."""

    response_variables: Dict[str, str]
    """A mapping of variable names to JSON paths in the response body.

    These values will be extracted from the response and made available as dynamic
    variables for use.
    """

    speak_after_execution: bool
    """
    Determines whether the agent would call LLM another time and speak when the
    result of function is obtained. Usually this needs to get turned on so user can
    get update for the function call.
    """

    speak_during_execution: bool
    """
    Determines whether the agent would say sentence like "One moment, let me check
    that." when executing the function. Recommend to turn on if your function call
    takes over 1s (including network) to complete, so that your agent remains
    responsive.
    """

    timeout_ms: int
    """The maximum time in milliseconds the tool can run before it's considered
    timeout.

    If the tool times out, the agent would have that info. The minimum value allowed
    is 1000 ms (1 s), and maximum value allowed is 600,000 ms (10 min). By default,
    this is set to 120,000 ms (2 min).
    """

    tool_id: str
    """Unique identifier for the tool"""


class ToolCheckAvailabilityCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: Required[Union[float, str]]
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for. Can be a number or a dynamic variable in the format
    `{{variable_name}}` that will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """

    tool_id: str
    """Unique identifier for the tool"""


class ToolBookAppointmentCalTool(TypedDict, total=False):
    cal_api_key: Required[str]
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: Required[Union[float, str]]
    """Cal.com event type id number for the cal.com event you want to book appointment.

    Can be a number or a dynamic variable in the format `{{variable_name}}` that
    will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """

    tool_id: str
    """Unique identifier for the tool"""


Tool: TypeAlias = Union[ToolCustomTool, ToolCheckAvailabilityCalTool, ToolBookAppointmentCalTool]
