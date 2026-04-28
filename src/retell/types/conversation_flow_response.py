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


class ComponentNodeConversationNodeAlwaysEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeConversationNodeAlwaysEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeConversationNodeAlwaysEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeConversationNodeAlwaysEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Always"]] = None
    """Must be "Always" for always edge"""


class ComponentNodeConversationNodeAlwaysEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Always"]
    """Must be "Always" for always edge"""

    type: Literal["prompt"]


ComponentNodeConversationNodeAlwaysEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeConversationNodeAlwaysEdgeTransitionConditionPromptCondition,
    ComponentNodeConversationNodeAlwaysEdgeTransitionConditionEquationCondition,
    ComponentNodeConversationNodeAlwaysEdgeTransitionConditionUnionMember2,
]


class ComponentNodeConversationNodeAlwaysEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeConversationNodeAlwaysEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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


class ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    BaseModel
):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[
        ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeConversationNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeConversationNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeConversationNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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

    always_edge: Optional[ComponentNodeConversationNodeAlwaysEdge] = None

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

    responsiveness: Optional[float] = None

    skip_response_edge: Optional[ComponentNodeConversationNodeSkipResponseEdge] = None

    voice_speed: Optional[float] = None


class ComponentNodeSubagentNodeInstruction(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Always"]] = None
    """Must be "Always" for always edge"""


class ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Always"]
    """Must be "Always" for always edge"""

    type: Literal["prompt"]


ComponentNodeSubagentNodeAlwaysEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionPromptCondition,
    ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionEquationCondition,
    ComponentNodeSubagentNodeAlwaysEdgeTransitionConditionUnionMember2,
]


class ComponentNodeSubagentNodeAlwaysEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeSubagentNodeAlwaysEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeSubagentNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeSubagentNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeSubagentNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSubagentNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeSubagentNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeSubagentNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeSubagentNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeSubagentNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeSubagentNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeSubagentNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeSubagentNodeFinetuneConversationExampleTranscript: TypeAlias = Union[
    ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember0,
    ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember1,
    ComponentNodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember2,
]


class ComponentNodeSubagentNodeFinetuneConversationExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodeSubagentNodeFinetuneConversationExampleTranscript]
    """The example transcript to finetune how the conversation should be."""


class ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeSubagentNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeSubagentNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodeSubagentNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[
        ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeSubagentNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeSubagentNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeSubagentNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[List[ComponentNodeSubagentNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeSubagentNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class ComponentNodeSubagentNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Skip response"]] = None
    """Must be "Skip response" for skip response edge"""


class ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Skip response"]
    """Must be "Skip response" for skip response edge"""

    type: Literal["prompt"]


ComponentNodeSubagentNodeSkipResponseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionPromptCondition,
    ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionEquationCondition,
    ComponentNodeSubagentNodeSkipResponseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeSubagentNodeSkipResponseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeSubagentNodeSkipResponseEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeSubagentNodeToolEndCallTool(BaseModel):
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

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


class ComponentNodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationPredefined(BaseModel):
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


class ComponentNodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationInferred(BaseModel):
    prompt: str
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Literal["inferred"]
    """The type of transfer destination."""


ComponentNodeSubagentNodeToolTransferCallToolTransferDestination: TypeAlias = Union[
    ComponentNodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationPredefined,
    ComponentNodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationInferred,
]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionColdTransfer(BaseModel):
    type: Literal["cold_transfer"]
    """The type of the transfer."""

    cold_transfer_mode: Optional[Literal["sip_refer", "sip_invite"]] = None
    """The mode of the cold transfer.

    If set to `sip_refer`, will use SIP REFER to transfer the call. If set to
    `sip_invite`, will use SIP INVITE to transfer the call.
    """

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring. Requires the telephony side to support caller id override. Retell
    Twilio numbers support this option. This parameter takes effect only when
    `cold_transfer_mode` is set to `sip_invite`. When using `sip_refer`, this option
    is not available. Retell Twilio numbers always use user's number as the caller
    id when using `sip refer` cold transfer mode.
    """

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption(BaseModel):
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption: TypeAlias = Union[
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt,
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption: TypeAlias = Union[
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt,
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransfer(BaseModel):
    type: Literal["warm_transfer"]
    """The type of the transfer."""

    agent_detection_timeout_ms: Optional[float] = None
    """The time to wait before considering transfer fails."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    ivr_option: Optional[
        ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption
    ] = None
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    on_hold_music: Optional[Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]] = None
    """The music to play while the caller is being transferred."""

    opt_out_human_detection: Optional[bool] = None
    """If set to true, will not perform human detection for the transfer.

    Default to false.
    """

    private_handoff_option: Optional[
        ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption
    ] = None
    """
    If set, when transfer is connected, will say the handoff message only to the
    agent receiving the transfer. Can leave either a static message or a dynamic one
    based on prompt. Set to null to disable warm handoff.
    """

    public_handoff_option: Optional[
        ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption
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

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent(
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


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig(
    BaseModel
):
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    action_on_timeout: Optional[Literal["bridge_transfer", "cancel_transfer"]] = None
    """The action to take when the transfer agent times out without making a decision.

    Defaults to cancel_transfer.
    """

    transfer_agent: Optional[
        ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent
    ] = None
    """The agent that will mediate the transfer decision."""

    transfer_timeout_ms: Optional[float] = None
    """
    The maximum time to wait for the transfer agent to make a decision, in
    milliseconds. Defaults to 30000 (30 seconds).
    """


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption: TypeAlias = Union[
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt,
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer(BaseModel):
    agentic_transfer_config: ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    type: Literal["agentic_warm_transfer"]
    """The type of the transfer."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    on_hold_music: Optional[Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]] = None
    """The music to play while the caller is being transferred."""

    public_handoff_option: Optional[
        ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption
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

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


ComponentNodeSubagentNodeToolTransferCallToolTransferOption: TypeAlias = Union[
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionColdTransfer,
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransfer,
    ComponentNodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer,
]


class ComponentNodeSubagentNodeToolTransferCallTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    transfer_destination: ComponentNodeSubagentNodeToolTransferCallToolTransferDestination

    transfer_option: ComponentNodeSubagentNodeToolTransferCallToolTransferOption

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

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    ignore_e164_validation: Optional[bool] = None
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


class ComponentNodeSubagentNodeToolCheckAvailabilityCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: Union[float, str]
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for. Can be a number or a dynamic variable in the format
    `{{variable_name}}` that will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """


class ComponentNodeSubagentNodeToolBookAppointmentCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: Union[float, str]
    """Cal.com event type id number for the cal.com event you want to book appointment.

    Can be a number or a dynamic variable in the format `{{variable_name}}` that
    will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """


class ComponentNodeSubagentNodeToolAgentSwapTool(BaseModel):
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

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    keep_current_language: Optional[bool] = None
    """If true, keep the current language when swapping agents. Defaults to false."""

    keep_current_voice: Optional[bool] = None
    """If true, keep the current voice when swapping agents. Defaults to false."""

    speak_during_execution: Optional[bool] = None

    webhook_setting: Optional[Literal["both_agents", "only_destination_agent", "only_source_agent"]] = None
    """Webhook setting for the agent swap, defaults to only source."""


class ComponentNodeSubagentNodeToolPressDigitTool(BaseModel):
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


class ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentPredefined(BaseModel):
    content: Optional[str] = None
    """The static message to be sent in the SMS. Can contain dynamic variables."""

    type: Optional[Literal["predefined"]] = None


class ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentInferred(BaseModel):
    prompt: Optional[str] = None
    """The prompt to be used to help infer the SMS content.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right message to send. Can contain dynamic variables.
    """

    type: Optional[Literal["inferred"]] = None


class ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentTemplate(BaseModel):
    template: Literal["info_collection"]
    """The template to use for the SMS content.

    "info_collection" sends a predefined message requesting information from the
    user.
    """

    type: Literal["template"]


ComponentNodeSubagentNodeToolSendSMSToolSMSContent: TypeAlias = Union[
    ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentPredefined,
    ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentInferred,
    ComponentNodeSubagentNodeToolSendSMSToolSMSContentSMSContentTemplate,
]


class ComponentNodeSubagentNodeToolSendSMSTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    sms_content: ComponentNodeSubagentNodeToolSendSMSToolSMSContent

    type: Literal["send_sms"]

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


class ComponentNodeSubagentNodeToolCustomToolParameters(BaseModel):
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


class ComponentNodeSubagentNodeToolCustomTool(BaseModel):
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

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None
    """Method to use for the request, default to POST."""

    parameters: Optional[ComponentNodeSubagentNodeToolCustomToolParameters] = None
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


class ComponentNodeSubagentNodeToolCodeTool(BaseModel):
    code: str
    """JavaScript code to execute in the sandbox."""

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["code"]

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


class ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableStringAnalysisData(BaseModel):
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


class ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableEnumAnalysisData(BaseModel):
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


class ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableBooleanAnalysisData(BaseModel):
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


class ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableNumberAnalysisData(BaseModel):
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


ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariable: TypeAlias = Union[
    ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableStringAnalysisData,
    ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableEnumAnalysisData,
    ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableBooleanAnalysisData,
    ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariableNumberAnalysisData,
]


class ComponentNodeSubagentNodeToolExtractDynamicVariableTool(BaseModel):
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

    variables: List[ComponentNodeSubagentNodeToolExtractDynamicVariableToolVariable]
    """The variables to be extracted."""


class ComponentNodeSubagentNodeToolBridgeTransferTool(BaseModel):
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

    execution_message_description: Optional[str] = None
    """Describes what to say to user when bridging the transfer.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


class ComponentNodeSubagentNodeToolCancelTransferTool(BaseModel):
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

    execution_message_description: Optional[str] = None
    """Describes what to say to user when cancelling the transfer.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


class ComponentNodeSubagentNodeToolMcpTool(BaseModel):
    description: str
    """Description of the MCP tool."""

    name: str
    """Name of the MCP tool."""

    type: Literal["mcp"]

    enable_typing_sound: Optional[bool] = None
    """
    If true, play a typing sound on the agent audio track while this MCP tool is
    executing.
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


class ComponentNodeSubagentNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    instruction: ComponentNodeSubagentNodeInstruction

    type: Literal["subagent"]
    """Type of the node"""

    always_edge: Optional[ComponentNodeSubagentNodeAlwaysEdge] = None

    display_position: Optional[ComponentNodeSubagentNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[ComponentNodeSubagentNodeEdge]] = None

    finetune_conversation_examples: Optional[List[ComponentNodeSubagentNodeFinetuneConversationExample]] = None

    finetune_transition_examples: Optional[List[ComponentNodeSubagentNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[ComponentNodeSubagentNodeGlobalNodeSetting] = None

    interruption_sensitivity: Optional[float] = None

    knowledge_base_ids: Optional[List[str]] = None
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    api_model_choice: Optional[ComponentNodeSubagentNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    responsiveness: Optional[float] = None

    skip_response_edge: Optional[ComponentNodeSubagentNodeSkipResponseEdge] = None

    tool_ids: Optional[List[str]] = None
    """
    The tool ids of the tools defined in main conversation flow or component that
    can be used in this subagent node.
    """

    tools: Optional[List[ComponentNodeSubagentNodeTool]] = None
    """The tools owned by this subagent node.

    This includes other tool types like transfer_call, agent_swap, etc.
    """

    voice_speed: Optional[float] = None


class ComponentNodeEndNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeEndNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeEndNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeEndNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class ComponentNodeEndNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    api_model_choice: Optional[ComponentNodeEndNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

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


class ComponentNodeFunctionNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeFunctionNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeFunctionNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeFunctionNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class ComponentNodeFunctionNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


ComponentNodeFunctionNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeFunctionNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeFunctionNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeFunctionNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeFunctionNodeElseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeFunctionNodeElseEdgeTransitionCondition

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


class ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[
        ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeFunctionNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeFunctionNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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

    else_edge: Optional[ComponentNodeFunctionNodeElseEdge] = None

    enable_typing_sound: Optional[bool] = None
    """If true, play a typing sound while this function executes."""

    finetune_transition_examples: Optional[List[ComponentNodeFunctionNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[ComponentNodeFunctionNodeGlobalNodeSetting] = None

    instruction: Optional[ComponentNodeFunctionNodeInstruction] = None

    api_model_choice: Optional[ComponentNodeFunctionNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """Whether to speak during tool execution"""


class ComponentNodeCodeNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeCodeNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeCodeNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeCodeNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeCodeNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeCodeNodeEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeCodeNodeEdgeTransitionConditionPromptCondition,
    ComponentNodeCodeNodeEdgeTransitionConditionEquationCondition,
]


class ComponentNodeCodeNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeCodeNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeCodeNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeCodeNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeCodeNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeCodeNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class ComponentNodeCodeNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


ComponentNodeCodeNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeCodeNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeCodeNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeCodeNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeCodeNodeElseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeCodeNodeElseEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeCodeNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeCodeNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodeCodeNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeCodeNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeCodeNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class ComponentNodeCodeNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeCodeNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[List[ComponentNodeCodeNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeCodeNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class ComponentNodeCodeNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeCodeNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


ComponentNodeCodeNodeInstruction: TypeAlias = Union[
    ComponentNodeCodeNodeInstructionNodeInstructionPrompt, ComponentNodeCodeNodeInstructionNodeInstructionStaticText
]


class ComponentNodeCodeNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeCodeNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    code: str
    """JavaScript code to execute in the sandbox."""

    type: Literal["code"]
    """Type of the node"""

    wait_for_result: bool
    """Whether to wait for code execution result"""

    display_position: Optional[ComponentNodeCodeNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[ComponentNodeCodeNodeEdge]] = None

    else_edge: Optional[ComponentNodeCodeNodeElseEdge] = None

    enable_typing_sound: Optional[bool] = None
    """If true, play a typing sound while code executes."""

    finetune_transition_examples: Optional[List[ComponentNodeCodeNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[ComponentNodeCodeNodeGlobalNodeSetting] = None

    instruction: Optional[ComponentNodeCodeNodeInstruction] = None

    api_model_choice: Optional[ComponentNodeCodeNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    response_variables: Optional[Dict[str, str]] = None
    """A mapping of variable names to JSON paths in the code execution result.

    These mapped values will be extracted and added as dynamic variables.
    """

    speak_during_execution: Optional[bool] = None
    """Whether to speak during code execution"""

    timeout_ms: Optional[int] = None
    """The maximum time in milliseconds the code can run before it's considered
    timeout.

    Defaults to 30,000 ms (30 s).
    """


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

    cold_transfer_mode: Optional[Literal["sip_refer", "sip_invite"]] = None
    """The mode of the cold transfer.

    If set to `sip_refer`, will use SIP REFER to transfer the call. If set to
    `sip_invite`, will use SIP INVITE to transfer the call.
    """

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring. Requires the telephony side to support caller id override. Retell
    Twilio numbers support this option. This parameter takes effect only when
    `cold_transfer_mode` is set to `sip_invite`. When using `sip_refer`, this option
    is not available. Retell Twilio numbers always use user's number as the caller
    id when using `sip refer` cold transfer mode.
    """

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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


class ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    BaseModel
):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[
        ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeTransferCallNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeTransferCallNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    BaseModel
):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[
        ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodePressDigitNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodePressDigitNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeBranchNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeBranchNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeBranchNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[List[ComponentNodeBranchNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeBranchNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class ComponentNodeBranchNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    api_model_choice: Optional[ComponentNodeBranchNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

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


class ComponentNodeSMSNodeInstructionSMSInstructionTemplate(BaseModel):
    template: Literal["info_collection"]
    """The template to use for the instruction.

    "info_collection" sends a predefined message requesting information from the
    user.
    """

    type: Literal["template"]
    """Type of instruction"""


ComponentNodeSMSNodeInstruction: TypeAlias = Union[
    ComponentNodeSMSNodeInstructionNodeInstructionPrompt,
    ComponentNodeSMSNodeInstructionNodeInstructionStaticText,
    ComponentNodeSMSNodeInstructionSMSInstructionTemplate,
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


class ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeSMSNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeSMSNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeSMSNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[List[ComponentNodeSMSNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[ComponentNodeSMSNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class ComponentNodeSMSNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    api_model_choice: Optional[ComponentNodeSMSNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""


class ComponentNodeExtractDynamicVariablesNodeVariableStringAnalysisData(BaseModel):
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


class ComponentNodeExtractDynamicVariablesNodeVariableEnumAnalysisData(BaseModel):
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


class ComponentNodeExtractDynamicVariablesNodeVariableBooleanAnalysisData(BaseModel):
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


class ComponentNodeExtractDynamicVariablesNodeVariableNumberAnalysisData(BaseModel):
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


class ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeExtractDynamicVariablesNodeElseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeExtractDynamicVariablesNodeElseEdgeTransitionCondition

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


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(
    BaseModel
):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    BaseModel
):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(
    BaseModel
):
    equations: List[
        ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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

    else_edge: Optional[ComponentNodeExtractDynamicVariablesNodeElseEdge] = None

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


class ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[
        ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeAgentSwapNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class ComponentNodeAgentSwapNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    keep_current_language: Optional[bool] = None
    """If true, keep the current language when swapping agents. Defaults to false."""

    keep_current_voice: Optional[bool] = None
    """If true, keep the current voice when swapping agents. Defaults to false."""

    api_model_choice: Optional[ComponentNodeAgentSwapNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

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


class ComponentNodeMcpNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeMcpNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeMcpNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeMcpNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class ComponentNodeMcpNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


ComponentNodeMcpNodeElseEdgeTransitionCondition: TypeAlias = Union[
    ComponentNodeMcpNodeElseEdgeTransitionConditionPromptCondition,
    ComponentNodeMcpNodeElseEdgeTransitionConditionEquationCondition,
    ComponentNodeMcpNodeElseEdgeTransitionConditionUnionMember2,
]


class ComponentNodeMcpNodeElseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeMcpNodeElseEdgeTransitionCondition

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


class ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeMcpNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeMcpNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeMcpNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class ComponentNodeMcpNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    else_edge: Optional[ComponentNodeMcpNodeElseEdge] = None

    enable_typing_sound: Optional[bool] = None
    """If true, play a typing sound while MCP tool executes."""

    finetune_transition_examples: Optional[List[ComponentNodeMcpNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[ComponentNodeMcpNodeGlobalNodeSetting] = None

    instruction: Optional[ComponentNodeMcpNodeInstruction] = None
    """What to say when calling the function, only used when speak during execution"""

    api_model_choice: Optional[ComponentNodeMcpNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

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


class ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


ComponentNodeComponentNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember0,
    ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember1,
    ComponentNodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class ComponentNodeComponentNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[ComponentNodeComponentNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[
        ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeComponentNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeComponentNodeGlobalNodeSettingGoBackConditionTransitionCondition

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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeComponentNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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

    finetune_transition_examples: Optional[List[ComponentNodeComponentNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[ComponentNodeComponentNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class ComponentNodeBridgeTransferNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    BaseModel
):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[
        ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeBridgeTransferNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[
        List[ComponentNodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    ] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[
        List[ComponentNodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    ] = None
    """Transition to this node"""


class ComponentNodeBridgeTransferNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeBridgeTransferNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


ComponentNodeBridgeTransferNodeInstruction: TypeAlias = Union[
    ComponentNodeBridgeTransferNodeInstructionNodeInstructionPrompt,
    ComponentNodeBridgeTransferNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeBridgeTransferNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeBridgeTransferNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["bridge_transfer"]
    """Type of the node - initiates a warm transfer by bridging the call"""

    display_position: Optional[ComponentNodeBridgeTransferNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[ComponentNodeBridgeTransferNodeGlobalNodeSetting] = None

    instruction: Optional[ComponentNodeBridgeTransferNodeInstruction] = None
    """Describes what to say to user when bridging the transfer.

    Only applicable when speak_during_execution is true.
    """

    api_model_choice: Optional[ComponentNodeBridgeTransferNodeModelChoice] = FieldInfo(
        alias="model_choice", default=None
    )

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution"""


class ComponentNodeCancelTransferNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    BaseModel
):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[
        ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[ComponentNodeCancelTransferNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[
        List[ComponentNodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample]
    ] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[
        List[ComponentNodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample]
    ] = None
    """Transition to this node"""


class ComponentNodeCancelTransferNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class ComponentNodeCancelTransferNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


ComponentNodeCancelTransferNodeInstruction: TypeAlias = Union[
    ComponentNodeCancelTransferNodeInstructionNodeInstructionPrompt,
    ComponentNodeCancelTransferNodeInstructionNodeInstructionStaticText,
]


class ComponentNodeCancelTransferNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class ComponentNodeCancelTransferNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["cancel_transfer"]
    """Type of the node - cancels the warm transfer and ends the transfer agent call"""

    display_position: Optional[ComponentNodeCancelTransferNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[ComponentNodeCancelTransferNodeGlobalNodeSetting] = None

    instruction: Optional[ComponentNodeCancelTransferNodeInstruction] = None
    """Describes what to say to user when cancelling the transfer.

    Only applicable when speak_during_execution is true.
    """

    api_model_choice: Optional[ComponentNodeCancelTransferNodeModelChoice] = FieldInfo(
        alias="model_choice", default=None
    )

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
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


class ComponentNoteDisplayPosition(BaseModel):
    """Position of the note on the canvas."""

    x: Optional[float] = None

    y: Optional[float] = None


class ComponentNoteSize(BaseModel):
    """Dimensions of the note on the canvas."""

    height: Optional[float] = None

    width: Optional[float] = None


class ComponentNote(BaseModel):
    id: str
    """Unique identifier for the note."""

    content: str
    """
    Text content of the note, can contain refs to images in the format
    "<image:asset_id>"
    """

    display_position: ComponentNoteDisplayPosition
    """Position of the note on the canvas."""

    size: ComponentNoteSize
    """Dimensions of the note on the canvas."""


class ComponentToolCustomToolParameters(BaseModel):
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


class ComponentToolCustomTool(BaseModel):
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

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None
    """Method to use for the request, default to POST."""

    parameters: Optional[ComponentToolCustomToolParameters] = None
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

    tool_id: Optional[str] = None
    """Unique identifier for the tool"""


class ComponentToolCheckAvailabilityCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: Union[float, str]
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for. Can be a number or a dynamic variable in the format
    `{{variable_name}}` that will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """

    tool_id: Optional[str] = None
    """Unique identifier for the tool"""


class ComponentToolBookAppointmentCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: Union[float, str]
    """Cal.com event type id number for the cal.com event you want to book appointment.

    Can be a number or a dynamic variable in the format `{{variable_name}}` that
    will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """

    tool_id: Optional[str] = None
    """Unique identifier for the tool"""


ComponentTool: TypeAlias = Union[
    ComponentToolCustomTool, ComponentToolCheckAvailabilityCalTool, ComponentToolBookAppointmentCalTool
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

    notes: Optional[List[ComponentNote]] = None
    """Visual annotations displayed on the flow canvas."""

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


class NodeConversationNodeAlwaysEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeConversationNodeAlwaysEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeConversationNodeAlwaysEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeConversationNodeAlwaysEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Always"]] = None
    """Must be "Always" for always edge"""


class NodeConversationNodeAlwaysEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Always"]
    """Must be "Always" for always edge"""

    type: Literal["prompt"]


NodeConversationNodeAlwaysEdgeTransitionCondition: TypeAlias = Union[
    NodeConversationNodeAlwaysEdgeTransitionConditionPromptCondition,
    NodeConversationNodeAlwaysEdgeTransitionConditionEquationCondition,
    NodeConversationNodeAlwaysEdgeTransitionConditionUnionMember2,
]


class NodeConversationNodeAlwaysEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeConversationNodeAlwaysEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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


class NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeConversationNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeConversationNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeConversationNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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

    always_edge: Optional[NodeConversationNodeAlwaysEdge] = None

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

    responsiveness: Optional[float] = None

    skip_response_edge: Optional[NodeConversationNodeSkipResponseEdge] = None

    voice_speed: Optional[float] = None


class NodeSubagentNodeInstruction(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeSubagentNodeAlwaysEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeSubagentNodeAlwaysEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeSubagentNodeAlwaysEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeSubagentNodeAlwaysEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Always"]] = None
    """Must be "Always" for always edge"""


class NodeSubagentNodeAlwaysEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Always"]
    """Must be "Always" for always edge"""

    type: Literal["prompt"]


NodeSubagentNodeAlwaysEdgeTransitionCondition: TypeAlias = Union[
    NodeSubagentNodeAlwaysEdgeTransitionConditionPromptCondition,
    NodeSubagentNodeAlwaysEdgeTransitionConditionEquationCondition,
    NodeSubagentNodeAlwaysEdgeTransitionConditionUnionMember2,
]


class NodeSubagentNodeAlwaysEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeSubagentNodeAlwaysEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeSubagentNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeSubagentNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeSubagentNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeSubagentNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeSubagentNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeSubagentNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeSubagentNodeEdgeTransitionConditionPromptCondition, NodeSubagentNodeEdgeTransitionConditionEquationCondition
]


class NodeSubagentNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeSubagentNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeSubagentNodeFinetuneConversationExampleTranscript: TypeAlias = Union[
    NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember0,
    NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember1,
    NodeSubagentNodeFinetuneConversationExampleTranscriptUnionMember2,
]


class NodeSubagentNodeFinetuneConversationExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodeSubagentNodeFinetuneConversationExampleTranscript]
    """The example transcript to finetune how the conversation should be."""


class NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeSubagentNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeSubagentNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeSubagentNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodeSubagentNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeSubagentNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeSubagentNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeSubagentNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeSubagentNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[List[NodeSubagentNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeSubagentNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeSubagentNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeSubagentNodeSkipResponseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeSubagentNodeSkipResponseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeSubagentNodeSkipResponseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeSubagentNodeSkipResponseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Skip response"]] = None
    """Must be "Skip response" for skip response edge"""


class NodeSubagentNodeSkipResponseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Skip response"]
    """Must be "Skip response" for skip response edge"""

    type: Literal["prompt"]


NodeSubagentNodeSkipResponseEdgeTransitionCondition: TypeAlias = Union[
    NodeSubagentNodeSkipResponseEdgeTransitionConditionPromptCondition,
    NodeSubagentNodeSkipResponseEdgeTransitionConditionEquationCondition,
    NodeSubagentNodeSkipResponseEdgeTransitionConditionUnionMember2,
]


class NodeSubagentNodeSkipResponseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeSubagentNodeSkipResponseEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeSubagentNodeToolEndCallTool(BaseModel):
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

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


class NodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationPredefined(BaseModel):
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


class NodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationInferred(BaseModel):
    prompt: str
    """The prompt to be used to help infer the transfer destination.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right number to transfer to. Can contain dynamic
    variables.
    """

    type: Literal["inferred"]
    """The type of transfer destination."""


NodeSubagentNodeToolTransferCallToolTransferDestination: TypeAlias = Union[
    NodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationPredefined,
    NodeSubagentNodeToolTransferCallToolTransferDestinationTransferDestinationInferred,
]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionColdTransfer(BaseModel):
    type: Literal["cold_transfer"]
    """The type of the transfer."""

    cold_transfer_mode: Optional[Literal["sip_refer", "sip_invite"]] = None
    """The mode of the cold transfer.

    If set to `sip_refer`, will use SIP REFER to transfer the call. If set to
    `sip_invite`, will use SIP INVITE to transfer the call.
    """

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring. Requires the telephony side to support caller id override. Retell
    Twilio numbers support this option. This parameter takes effect only when
    `cold_transfer_mode` is set to `sip_invite`. When using `sip_refer`, this option
    is not available. Retell Twilio numbers always use user's number as the caller
    id when using `sip refer` cold transfer mode.
    """

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption(BaseModel):
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption: TypeAlias = Union[
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferPrompt,
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOptionWarmTransferStaticMessage,
]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption: TypeAlias = Union[
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferPrompt,
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransfer(BaseModel):
    type: Literal["warm_transfer"]
    """The type of the transfer."""

    agent_detection_timeout_ms: Optional[float] = None
    """The time to wait before considering transfer fails."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    ivr_option: Optional[NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferIvrOption] = None
    """IVR navigation option to run when doing human detection.

    This prompt will guide the AI on how to navigate the IVR system.
    """

    on_hold_music: Optional[Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]] = None
    """The music to play while the caller is being transferred."""

    opt_out_human_detection: Optional[bool] = None
    """If set to true, will not perform human detection for the transfer.

    Default to false.
    """

    private_handoff_option: Optional[
        NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPrivateHandoffOption
    ] = None
    """
    If set, when transfer is connected, will say the handoff message only to the
    agent receiving the transfer. Can leave either a static message or a dynamic one
    based on prompt. Set to null to disable warm handoff.
    """

    public_handoff_option: Optional[
        NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransferPublicHandoffOption
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

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent(
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


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig(
    BaseModel
):
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    action_on_timeout: Optional[Literal["bridge_transfer", "cancel_transfer"]] = None
    """The action to take when the transfer agent times out without making a decision.

    Defaults to cancel_transfer.
    """

    transfer_agent: Optional[
        NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfigTransferAgent
    ] = None
    """The agent that will mediate the transfer decision."""

    transfer_timeout_ms: Optional[float] = None
    """
    The maximum time to wait for the transfer agent to make a decision, in
    milliseconds. Defaults to 30000 (30 seconds).
    """


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt(
    BaseModel
):
    prompt: Optional[str] = None
    """The prompt to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["prompt"]] = None


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage(
    BaseModel
):
    message: Optional[str] = None
    """The static message to be used for warm handoff. Can contain dynamic variables."""

    type: Optional[Literal["static_message"]] = None


NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption: TypeAlias = Union[
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferPrompt,
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOptionWarmTransferStaticMessage,
]


class NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer(BaseModel):
    agentic_transfer_config: (
        NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferAgenticTransferConfig
    )
    """Configuration for agentic warm transfer. Required for agentic warm transfer."""

    type: Literal["agentic_warm_transfer"]
    """The type of the transfer."""

    enable_bridge_audio_cue: Optional[bool] = None
    """Whether to play an audio cue when bridging the call. Defaults to true."""

    on_hold_music: Optional[Literal["none", "relaxing_sound", "uplifting_beats", "ringtone"]] = None
    """The music to play while the caller is being transferred."""

    public_handoff_option: Optional[
        NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransferPublicHandoffOption
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

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
    """


NodeSubagentNodeToolTransferCallToolTransferOption: TypeAlias = Union[
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionColdTransfer,
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionWarmTransfer,
    NodeSubagentNodeToolTransferCallToolTransferOptionTransferOptionAgenticWarmTransfer,
]


class NodeSubagentNodeToolTransferCallTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    transfer_destination: NodeSubagentNodeToolTransferCallToolTransferDestination

    transfer_option: NodeSubagentNodeToolTransferCallToolTransferOption

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

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    ignore_e164_validation: Optional[bool] = None
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


class NodeSubagentNodeToolCheckAvailabilityCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: Union[float, str]
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for. Can be a number or a dynamic variable in the format
    `{{variable_name}}` that will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """


class NodeSubagentNodeToolBookAppointmentCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: Union[float, str]
    """Cal.com event type id number for the cal.com event you want to book appointment.

    Can be a number or a dynamic variable in the format `{{variable_name}}` that
    will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """


class NodeSubagentNodeToolAgentSwapTool(BaseModel):
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

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    keep_current_language: Optional[bool] = None
    """If true, keep the current language when swapping agents. Defaults to false."""

    keep_current_voice: Optional[bool] = None
    """If true, keep the current voice when swapping agents. Defaults to false."""

    speak_during_execution: Optional[bool] = None

    webhook_setting: Optional[Literal["both_agents", "only_destination_agent", "only_source_agent"]] = None
    """Webhook setting for the agent swap, defaults to only source."""


class NodeSubagentNodeToolPressDigitTool(BaseModel):
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


class NodeSubagentNodeToolSendSMSToolSMSContentSMSContentPredefined(BaseModel):
    content: Optional[str] = None
    """The static message to be sent in the SMS. Can contain dynamic variables."""

    type: Optional[Literal["predefined"]] = None


class NodeSubagentNodeToolSendSMSToolSMSContentSMSContentInferred(BaseModel):
    prompt: Optional[str] = None
    """The prompt to be used to help infer the SMS content.

    The model will take the global prompt, the call transcript, and this prompt
    together to deduce the right message to send. Can contain dynamic variables.
    """

    type: Optional[Literal["inferred"]] = None


class NodeSubagentNodeToolSendSMSToolSMSContentSMSContentTemplate(BaseModel):
    template: Literal["info_collection"]
    """The template to use for the SMS content.

    "info_collection" sends a predefined message requesting information from the
    user.
    """

    type: Literal["template"]


NodeSubagentNodeToolSendSMSToolSMSContent: TypeAlias = Union[
    NodeSubagentNodeToolSendSMSToolSMSContentSMSContentPredefined,
    NodeSubagentNodeToolSendSMSToolSMSContentSMSContentInferred,
    NodeSubagentNodeToolSendSMSToolSMSContentSMSContentTemplate,
]


class NodeSubagentNodeToolSendSMSTool(BaseModel):
    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges).
    """

    sms_content: NodeSubagentNodeToolSendSMSToolSMSContent

    type: Literal["send_sms"]

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


class NodeSubagentNodeToolCustomToolParameters(BaseModel):
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


class NodeSubagentNodeToolCustomTool(BaseModel):
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

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None
    """Method to use for the request, default to POST."""

    parameters: Optional[NodeSubagentNodeToolCustomToolParameters] = None
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


class NodeSubagentNodeToolCodeTool(BaseModel):
    code: str
    """JavaScript code to execute in the sandbox."""

    name: str
    """Name of the tool.

    Must be unique within all tools available to LLM at any given time (general
    tools + state tools + state edges). Must be consisted of a-z, A-Z, 0-9, or
    contain underscores and dashes, with a maximum length of 64 (no space allowed).
    """

    type: Literal["code"]

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


class NodeSubagentNodeToolExtractDynamicVariableToolVariableStringAnalysisData(BaseModel):
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


class NodeSubagentNodeToolExtractDynamicVariableToolVariableEnumAnalysisData(BaseModel):
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


class NodeSubagentNodeToolExtractDynamicVariableToolVariableBooleanAnalysisData(BaseModel):
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


class NodeSubagentNodeToolExtractDynamicVariableToolVariableNumberAnalysisData(BaseModel):
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


NodeSubagentNodeToolExtractDynamicVariableToolVariable: TypeAlias = Union[
    NodeSubagentNodeToolExtractDynamicVariableToolVariableStringAnalysisData,
    NodeSubagentNodeToolExtractDynamicVariableToolVariableEnumAnalysisData,
    NodeSubagentNodeToolExtractDynamicVariableToolVariableBooleanAnalysisData,
    NodeSubagentNodeToolExtractDynamicVariableToolVariableNumberAnalysisData,
]


class NodeSubagentNodeToolExtractDynamicVariableTool(BaseModel):
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

    variables: List[NodeSubagentNodeToolExtractDynamicVariableToolVariable]
    """The variables to be extracted."""


class NodeSubagentNodeToolBridgeTransferTool(BaseModel):
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

    execution_message_description: Optional[str] = None
    """Describes what to say to user when bridging the transfer.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


class NodeSubagentNodeToolCancelTransferTool(BaseModel):
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

    execution_message_description: Optional[str] = None
    """Describes what to say to user when cancelling the transfer.

    Only applicable when speak_during_execution is true.
    """

    execution_message_type: Optional[Literal["prompt", "static_text"]] = None
    """Type of execution message.

    "prompt" means the agent will use execution_message_description as a prompt to
    generate the message. "static_text" means the agent will speak the
    execution_message_description directly. Defaults to "prompt".
    """

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution."""


class NodeSubagentNodeToolMcpTool(BaseModel):
    description: str
    """Description of the MCP tool."""

    name: str
    """Name of the MCP tool."""

    type: Literal["mcp"]

    enable_typing_sound: Optional[bool] = None
    """
    If true, play a typing sound on the agent audio track while this MCP tool is
    executing.
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


class NodeSubagentNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    instruction: NodeSubagentNodeInstruction

    type: Literal["subagent"]
    """Type of the node"""

    always_edge: Optional[NodeSubagentNodeAlwaysEdge] = None

    display_position: Optional[NodeSubagentNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[NodeSubagentNodeEdge]] = None

    finetune_conversation_examples: Optional[List[NodeSubagentNodeFinetuneConversationExample]] = None

    finetune_transition_examples: Optional[List[NodeSubagentNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodeSubagentNodeGlobalNodeSetting] = None

    interruption_sensitivity: Optional[float] = None

    knowledge_base_ids: Optional[List[str]] = None
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    api_model_choice: Optional[NodeSubagentNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    responsiveness: Optional[float] = None

    skip_response_edge: Optional[NodeSubagentNodeSkipResponseEdge] = None

    tool_ids: Optional[List[str]] = None
    """
    The tool ids of the tools defined in main conversation flow or component that
    can be used in this subagent node.
    """

    tools: Optional[List[NodeSubagentNodeTool]] = None
    """The tools owned by this subagent node.

    This includes other tool types like transfer_call, agent_swap, etc.
    """

    voice_speed: Optional[float] = None


class NodeEndNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeEndNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeEndNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeEndNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeEndNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeEndNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class NodeEndNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    api_model_choice: Optional[NodeEndNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

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


class NodeFunctionNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeFunctionNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeFunctionNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeFunctionNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class NodeFunctionNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


NodeFunctionNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeFunctionNodeElseEdgeTransitionConditionPromptCondition,
    NodeFunctionNodeElseEdgeTransitionConditionEquationCondition,
    NodeFunctionNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeFunctionNodeElseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeFunctionNodeElseEdgeTransitionCondition

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


class NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeFunctionNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeFunctionNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeFunctionNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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

    else_edge: Optional[NodeFunctionNodeElseEdge] = None

    enable_typing_sound: Optional[bool] = None
    """If true, play a typing sound while this function executes."""

    finetune_transition_examples: Optional[List[NodeFunctionNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodeFunctionNodeGlobalNodeSetting] = None

    instruction: Optional[NodeFunctionNodeInstruction] = None

    api_model_choice: Optional[NodeFunctionNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """Whether to speak during tool execution"""


class NodeCodeNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeCodeNodeEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeCodeNodeEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeCodeNodeEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeCodeNodeEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeCodeNodeEdgeTransitionCondition: TypeAlias = Union[
    NodeCodeNodeEdgeTransitionConditionPromptCondition, NodeCodeNodeEdgeTransitionConditionEquationCondition
]


class NodeCodeNodeEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeCodeNodeEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeCodeNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeCodeNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeCodeNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeCodeNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class NodeCodeNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


NodeCodeNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeCodeNodeElseEdgeTransitionConditionPromptCondition,
    NodeCodeNodeElseEdgeTransitionConditionEquationCondition,
    NodeCodeNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeCodeNodeElseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeCodeNodeElseEdgeTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeCodeNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeCodeNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeCodeNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodeCodeNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeCodeNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeCodeNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


class NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscript: TypeAlias = Union[
    NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember0,
    NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember1,
    NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscriptUnionMember2,
]


class NodeCodeNodeGlobalNodeSettingNegativeFinetuneExample(BaseModel):
    transcript: List[NodeCodeNodeGlobalNodeSettingNegativeFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscript: TypeAlias = Union[
    NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember0,
    NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember1,
    NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscriptUnionMember2,
]


class NodeCodeNodeGlobalNodeSettingPositiveFinetuneExample(BaseModel):
    transcript: List[NodeCodeNodeGlobalNodeSettingPositiveFinetuneExampleTranscript]
    """Find tune the transition condition to this global node"""


class NodeCodeNodeGlobalNodeSetting(BaseModel):
    condition: str
    """Condition for global node activation, cannot be empty"""

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeCodeNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[List[NodeCodeNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeCodeNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeCodeNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeCodeNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


NodeCodeNodeInstruction: TypeAlias = Union[
    NodeCodeNodeInstructionNodeInstructionPrompt, NodeCodeNodeInstructionNodeInstructionStaticText
]


class NodeCodeNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeCodeNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    code: str
    """JavaScript code to execute in the sandbox."""

    type: Literal["code"]
    """Type of the node"""

    wait_for_result: bool
    """Whether to wait for code execution result"""

    display_position: Optional[NodeCodeNodeDisplayPosition] = None
    """Position for frontend display"""

    edges: Optional[List[NodeCodeNodeEdge]] = None

    else_edge: Optional[NodeCodeNodeElseEdge] = None

    enable_typing_sound: Optional[bool] = None
    """If true, play a typing sound while code executes."""

    finetune_transition_examples: Optional[List[NodeCodeNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodeCodeNodeGlobalNodeSetting] = None

    instruction: Optional[NodeCodeNodeInstruction] = None

    api_model_choice: Optional[NodeCodeNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    response_variables: Optional[Dict[str, str]] = None
    """A mapping of variable names to JSON paths in the code execution result.

    These mapped values will be extracted and added as dynamic variables.
    """

    speak_during_execution: Optional[bool] = None
    """Whether to speak during code execution"""

    timeout_ms: Optional[int] = None
    """The maximum time in milliseconds the code can run before it's considered
    timeout.

    Defaults to 30,000 ms (30 s).
    """


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

    cold_transfer_mode: Optional[Literal["sip_refer", "sip_invite"]] = None
    """The mode of the cold transfer.

    If set to `sip_refer`, will use SIP REFER to transfer the call. If set to
    `sip_invite`, will use SIP INVITE to transfer the call.
    """

    show_transferee_as_caller: Optional[bool] = None
    """
    If set to true, will show transferee (the user, not the AI agent) as caller when
    transferring. Requires the telephony side to support caller id override. Retell
    Twilio numbers support this option. This parameter takes effect only when
    `cold_transfer_mode` is set to `sip_invite`. When using `sip_refer`, this option
    is not available. Retell Twilio numbers always use user's number as the caller
    id when using `sip refer` cold transfer mode.
    """

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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

    transfer_ring_duration_ms: Optional[int] = None
    """Override the ring duration for this specific transfer, in milliseconds.

    If not set, falls back to the agent-level `ring_duration_ms`.
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


class NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeTransferCallNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeTransferCallNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeTransferCallNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodePressDigitNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodePressDigitNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodePressDigitNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeBranchNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeBranchNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeBranchNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[List[NodeBranchNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeBranchNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeBranchNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    api_model_choice: Optional[NodeBranchNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

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


class NodeSMSNodeInstructionSMSInstructionTemplate(BaseModel):
    template: Literal["info_collection"]
    """The template to use for the instruction.

    "info_collection" sends a predefined message requesting information from the
    user.
    """

    type: Literal["template"]
    """Type of instruction"""


NodeSMSNodeInstruction: TypeAlias = Union[
    NodeSMSNodeInstructionNodeInstructionPrompt,
    NodeSMSNodeInstructionNodeInstructionStaticText,
    NodeSMSNodeInstructionSMSInstructionTemplate,
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


class NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeSMSNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeSMSNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeSMSNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[List[NodeSMSNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeSMSNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeSMSNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    api_model_choice: Optional[NodeSMSNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodeExtractDynamicVariablesNodeVariableStringAnalysisData(BaseModel):
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


class NodeExtractDynamicVariablesNodeVariableEnumAnalysisData(BaseModel):
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


class NodeExtractDynamicVariablesNodeVariableBooleanAnalysisData(BaseModel):
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


class NodeExtractDynamicVariablesNodeVariableNumberAnalysisData(BaseModel):
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


class NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


NodeExtractDynamicVariablesNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionPromptCondition,
    NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionEquationCondition,
    NodeExtractDynamicVariablesNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeExtractDynamicVariablesNodeElseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeExtractDynamicVariablesNodeElseEdgeTransitionCondition

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


class NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(
    BaseModel
):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[
        NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation
    ]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeExtractDynamicVariablesNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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

    else_edge: Optional[NodeExtractDynamicVariablesNodeElseEdge] = None

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


class NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeAgentSwapNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeAgentSwapNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeAgentSwapNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class NodeAgentSwapNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    keep_current_language: Optional[bool] = None
    """If true, keep the current language when swapping agents. Defaults to false."""

    keep_current_voice: Optional[bool] = None
    """If true, keep the current voice when swapping agents. Defaults to false."""

    api_model_choice: Optional[NodeAgentSwapNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

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


class NodeMcpNodeElseEdgeTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeMcpNodeElseEdgeTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeMcpNodeElseEdgeTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeMcpNodeElseEdgeTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]

    prompt: Optional[Literal["Else"]] = None
    """Must be "Else" for else edge"""


class NodeMcpNodeElseEdgeTransitionConditionUnionMember2(BaseModel):
    prompt: Literal["Else"]
    """Must be "Else" for else edge"""

    type: Literal["prompt"]


NodeMcpNodeElseEdgeTransitionCondition: TypeAlias = Union[
    NodeMcpNodeElseEdgeTransitionConditionPromptCondition,
    NodeMcpNodeElseEdgeTransitionConditionEquationCondition,
    NodeMcpNodeElseEdgeTransitionConditionUnionMember2,
]


class NodeMcpNodeElseEdge(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeMcpNodeElseEdgeTransitionCondition

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


class NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeMcpNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeMcpNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeMcpNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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


class NodeMcpNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


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

    else_edge: Optional[NodeMcpNodeElseEdge] = None

    enable_typing_sound: Optional[bool] = None
    """If true, play a typing sound while MCP tool executes."""

    finetune_transition_examples: Optional[List[NodeMcpNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodeMcpNodeGlobalNodeSetting] = None

    instruction: Optional[NodeMcpNodeInstruction] = None
    """What to say when calling the function, only used when speak during execution"""

    api_model_choice: Optional[NodeMcpNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

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


class NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember0(BaseModel):
    content: str

    role: Literal["agent", "user"]


class NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember1(BaseModel):
    arguments: str

    name: str

    role: Literal["tool_call_invocation"]

    tool_call_id: str


class NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember2(BaseModel):
    content: str

    role: Literal["tool_call_result"]

    tool_call_id: str


NodeComponentNodeFinetuneTransitionExampleTranscript: TypeAlias = Union[
    NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember0,
    NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember1,
    NodeComponentNodeFinetuneTransitionExampleTranscriptUnionMember2,
]


class NodeComponentNodeFinetuneTransitionExample(BaseModel):
    id: str
    """Unique identifier for the example"""

    transcript: List[NodeComponentNodeFinetuneTransitionExampleTranscript]
    """The example transcript to finetune how the node should transition."""

    destination_node_id: Optional[str] = None
    """Optional destination node ID"""


class NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeComponentNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeComponentNodeGlobalNodeSettingGoBackConditionTransitionCondition

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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeComponentNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

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

    finetune_transition_examples: Optional[List[NodeComponentNodeFinetuneTransitionExample]] = None

    global_node_setting: Optional[NodeComponentNodeGlobalNodeSetting] = None

    name: Optional[str] = None
    """Optional name for display purposes"""


class NodeBridgeTransferNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeBridgeTransferNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeBridgeTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeBridgeTransferNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[List[NodeBridgeTransferNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeBridgeTransferNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeBridgeTransferNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeBridgeTransferNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


NodeBridgeTransferNodeInstruction: TypeAlias = Union[
    NodeBridgeTransferNodeInstructionNodeInstructionPrompt, NodeBridgeTransferNodeInstructionNodeInstructionStaticText
]


class NodeBridgeTransferNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeBridgeTransferNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["bridge_transfer"]
    """Type of the node - initiates a warm transfer by bridging the call"""

    display_position: Optional[NodeBridgeTransferNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[NodeBridgeTransferNodeGlobalNodeSetting] = None

    instruction: Optional[NodeBridgeTransferNodeInstruction] = None
    """Describes what to say to user when bridging the transfer.

    Only applicable when speak_during_execution is true.
    """

    api_model_choice: Optional[NodeBridgeTransferNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
    """If true, will speak during execution"""


class NodeCancelTransferNodeDisplayPosition(BaseModel):
    """Position for frontend display"""

    x: Optional[float] = None

    y: Optional[float] = None


class NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition(BaseModel):
    prompt: str
    """Prompt condition text"""

    type: Literal["prompt"]


class NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation(BaseModel):
    left: str
    """Left side of the equation"""

    operator: Literal["==", "!=", ">", ">=", "<", "<=", "contains", "not_contains", "exists", "not_exist"]

    right: Optional[str] = None
    """Right side of the equation.

    The right side of the equation not required when "exists" or "not_exist" are
    selected.
    """


class NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition(BaseModel):
    equations: List[NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationConditionEquation]

    operator: Literal["||", "&&"]

    type: Literal["equation"]


NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition: TypeAlias = Union[
    NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionPromptCondition,
    NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionConditionEquationCondition,
]


class NodeCancelTransferNodeGlobalNodeSettingGoBackCondition(BaseModel):
    id: str
    """Unique identifier for the edge"""

    transition_condition: NodeCancelTransferNodeGlobalNodeSettingGoBackConditionTransitionCondition

    destination_node_id: Optional[str] = None
    """ID of the destination node"""


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

    cool_down: Optional[float] = None
    """
    The same global node won't be triggered again within the next N node
    transitions.
    """

    go_back_conditions: Optional[List[NodeCancelTransferNodeGlobalNodeSettingGoBackCondition]] = None
    """The conditions for global node go back.

    There would be no destination_node_id for these edges.
    """

    negative_finetune_examples: Optional[List[NodeCancelTransferNodeGlobalNodeSettingNegativeFinetuneExample]] = None
    """Don't transition to this node"""

    positive_finetune_examples: Optional[List[NodeCancelTransferNodeGlobalNodeSettingPositiveFinetuneExample]] = None
    """Transition to this node"""


class NodeCancelTransferNodeInstructionNodeInstructionPrompt(BaseModel):
    text: str
    """The prompt text for the instruction"""

    type: Literal["prompt"]
    """Type of instruction"""


class NodeCancelTransferNodeInstructionNodeInstructionStaticText(BaseModel):
    text: str
    """The static text for the instruction"""

    type: Literal["static_text"]
    """Type of instruction"""


NodeCancelTransferNodeInstruction: TypeAlias = Union[
    NodeCancelTransferNodeInstructionNodeInstructionPrompt, NodeCancelTransferNodeInstructionNodeInstructionStaticText
]


class NodeCancelTransferNodeModelChoice(BaseModel):
    model: Literal[
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
    """The LLM model to use"""

    type: Literal["cascading"]
    """Type of model choice"""

    high_priority: Optional[bool] = None
    """Whether to use high priority pool with more dedicated resource, default false"""


class NodeCancelTransferNode(BaseModel):
    id: str
    """Unique identifier for the node"""

    type: Literal["cancel_transfer"]
    """Type of the node - cancels the warm transfer and ends the transfer agent call"""

    display_position: Optional[NodeCancelTransferNodeDisplayPosition] = None
    """Position for frontend display"""

    global_node_setting: Optional[NodeCancelTransferNodeGlobalNodeSetting] = None

    instruction: Optional[NodeCancelTransferNodeInstruction] = None
    """Describes what to say to user when cancelling the transfer.

    Only applicable when speak_during_execution is true.
    """

    api_model_choice: Optional[NodeCancelTransferNodeModelChoice] = FieldInfo(alias="model_choice", default=None)

    name: Optional[str] = None
    """Optional name for display purposes"""

    speak_during_execution: Optional[bool] = None
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


class NoteDisplayPosition(BaseModel):
    """Position of the note on the canvas."""

    x: Optional[float] = None

    y: Optional[float] = None


class NoteSize(BaseModel):
    """Dimensions of the note on the canvas."""

    height: Optional[float] = None

    width: Optional[float] = None


class Note(BaseModel):
    id: str
    """Unique identifier for the note."""

    content: str
    """
    Text content of the note, can contain refs to images in the format
    "<image:asset_id>"
    """

    display_position: NoteDisplayPosition
    """Position of the note on the canvas."""

    size: NoteSize
    """Dimensions of the note on the canvas."""


class ToolCustomToolParameters(BaseModel):
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


class ToolCustomTool(BaseModel):
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

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None
    """Method to use for the request, default to POST."""

    parameters: Optional[ToolCustomToolParameters] = None
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

    tool_id: Optional[str] = None
    """Unique identifier for the tool"""


class ToolCheckAvailabilityCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to check
    availability for.
    """

    event_type_id: Union[float, str]
    """
    Cal.com event type id number for the cal.com event you want to check
    availability for. Can be a number or a dynamic variable in the format
    `{{variable_name}}` that will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """

    tool_id: Optional[str] = None
    """Unique identifier for the tool"""


class ToolBookAppointmentCalTool(BaseModel):
    cal_api_key: str
    """
    Cal.com Api key that have access to the cal.com event you want to book
    appointment.
    """

    event_type_id: Union[float, str]
    """Cal.com event type id number for the cal.com event you want to book appointment.

    Can be a number or a dynamic variable in the format `{{variable_name}}` that
    will be resolved at runtime.
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
    Can also be a dynamic variable in the format `{{variable_name}}` that will be
    resolved at runtime. If not specified, will check if user specified timezone in
    call, and if not, will use the timezone of the Retell servers.
    """

    tool_id: Optional[str] = None
    """Unique identifier for the tool"""


Tool: TypeAlias = Union[ToolCustomTool, ToolCheckAvailabilityCalTool, ToolBookAppointmentCalTool]


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

    notes: Optional[List[Note]] = None
    """Visual annotations displayed on the flow canvas."""

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
