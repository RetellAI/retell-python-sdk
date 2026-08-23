# Call

Types:

```python
from retell.types import (
    CallResponse,
    PhoneCallResponse,
    WebCallResponse,
    CallListResponse,
    CallUpdateLiveResponse,
)
```

Methods:

- <code title="get /v2/get-call/{call_id}">client.call.<a href="./src/retell/resources/call.py">retrieve</a>(call_id) -> <a href="./src/retell/types/call_response.py">CallResponse</a></code>
- <code title="patch /v2/update-call/{call_id}">client.call.<a href="./src/retell/resources/call.py">update</a>(call_id, \*\*<a href="src/retell/types/call_update_params.py">params</a>) -> <a href="./src/retell/types/call_response.py">CallResponse</a></code>
- <code title="post /v3/list-calls">client.call.<a href="./src/retell/resources/call.py">list</a>(\*\*<a href="src/retell/types/call_list_params.py">params</a>) -> <a href="./src/retell/types/call_list_response.py">CallListResponse</a></code>
- <code title="delete /v2/delete-call/{call_id}">client.call.<a href="./src/retell/resources/call.py">delete</a>(call_id) -> None</code>
- <code title="post /v2/create-phone-call">client.call.<a href="./src/retell/resources/call.py">create_phone_call</a>(\*\*<a href="src/retell/types/call_create_phone_call_params.py">params</a>) -> <a href="./src/retell/types/phone_call_response.py">PhoneCallResponse</a></code>
- <code title="post /v2/create-web-call">client.call.<a href="./src/retell/resources/call.py">create_web_call</a>(\*\*<a href="src/retell/types/call_create_web_call_params.py">params</a>) -> <a href="./src/retell/types/web_call_response.py">WebCallResponse</a></code>
- <code title="post /v2/register-phone-call">client.call.<a href="./src/retell/resources/call.py">register_phone_call</a>(\*\*<a href="src/retell/types/call_register_phone_call_params.py">params</a>) -> <a href="./src/retell/types/phone_call_response.py">PhoneCallResponse</a></code>
- <code title="put /rerun-call-analysis/{call_id}">client.call.<a href="./src/retell/resources/call.py">rerun_analysis</a>(call_id) -> <a href="./src/retell/types/call_response.py">CallResponse</a></code>
- <code title="post /v2/stop-call/{call_id}">client.call.<a href="./src/retell/resources/call.py">stop</a>(call_id) -> None</code>
- <code title="patch /v2/update-live-call/{call_id}">client.call.<a href="./src/retell/resources/call.py">update_live</a>(call_id, \*\*<a href="src/retell/types/call_update_live_params.py">params</a>) -> <a href="./src/retell/types/call_update_live_response.py">CallUpdateLiveResponse</a></code>

# Chat

Types:

```python
from retell.types import ChatResponse, ChatListResponse, ChatCreateChatCompletionResponse
```

Methods:

- <code title="post /create-chat">client.chat.<a href="./src/retell/resources/chat.py">create</a>(\*\*<a href="src/retell/types/chat_create_params.py">params</a>) -> <a href="./src/retell/types/chat_response.py">ChatResponse</a></code>
- <code title="get /get-chat/{chat_id}">client.chat.<a href="./src/retell/resources/chat.py">retrieve</a>(chat_id) -> <a href="./src/retell/types/chat_response.py">ChatResponse</a></code>
- <code title="patch /update-chat/{chat_id}">client.chat.<a href="./src/retell/resources/chat.py">update</a>(chat_id, \*\*<a href="src/retell/types/chat_update_params.py">params</a>) -> <a href="./src/retell/types/chat_response.py">ChatResponse</a></code>
- <code title="post /v3/list-chats">client.chat.<a href="./src/retell/resources/chat.py">list</a>(\*\*<a href="src/retell/types/chat_list_params.py">params</a>) -> <a href="./src/retell/types/chat_list_response.py">ChatListResponse</a></code>
- <code title="delete /delete-chat/{chat_id}">client.chat.<a href="./src/retell/resources/chat.py">delete</a>(chat_id) -> None</code>
- <code title="post /create-chat-completion">client.chat.<a href="./src/retell/resources/chat.py">create_chat_completion</a>(\*\*<a href="src/retell/types/chat_create_chat_completion_params.py">params</a>) -> <a href="./src/retell/types/chat_create_chat_completion_response.py">ChatCreateChatCompletionResponse</a></code>
- <code title="post /create-sms-chat">client.chat.<a href="./src/retell/resources/chat.py">create_sms_chat</a>(\*\*<a href="src/retell/types/chat_create_sms_chat_params.py">params</a>) -> <a href="./src/retell/types/chat_response.py">ChatResponse</a></code>
- <code title="patch /end-chat/{chat_id}">client.chat.<a href="./src/retell/resources/chat.py">end</a>(chat_id) -> None</code>
- <code title="put /rerun-chat-analysis/{chat_id}">client.chat.<a href="./src/retell/resources/chat.py">rerun_analysis</a>(chat_id) -> <a href="./src/retell/types/chat_response.py">ChatResponse</a></code>

# PhoneNumber

Types:

```python
from retell.types import PhoneNumberResponse, PhoneNumberListResponse
```

Methods:

- <code title="post /create-phone-number">client.phone_number.<a href="./src/retell/resources/phone_number.py">create</a>(\*\*<a href="src/retell/types/phone_number_create_params.py">params</a>) -> <a href="./src/retell/types/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="get /get-phone-number/{phone_number}">client.phone_number.<a href="./src/retell/resources/phone_number.py">retrieve</a>(phone_number) -> <a href="./src/retell/types/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="patch /update-phone-number/{phone_number}">client.phone_number.<a href="./src/retell/resources/phone_number.py">update</a>(phone_number, \*\*<a href="src/retell/types/phone_number_update_params.py">params</a>) -> <a href="./src/retell/types/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="get /v2/list-phone-numbers">client.phone_number.<a href="./src/retell/resources/phone_number.py">list</a>(\*\*<a href="src/retell/types/phone_number_list_params.py">params</a>) -> <a href="./src/retell/types/phone_number_list_response.py">PhoneNumberListResponse</a></code>
- <code title="delete /delete-phone-number/{phone_number}">client.phone_number.<a href="./src/retell/resources/phone_number.py">delete</a>(phone_number) -> None</code>
- <code title="post /import-phone-number">client.phone*number.<a href="./src/retell/resources/phone_number.py">import*</a>(\*\*<a href="src/retell/types/phone_number_import_params.py">params</a>) -> <a href="./src/retell/types/phone_number_response.py">PhoneNumberResponse</a></code>

# Agent

Types:

```python
from retell.types import (
    AgentResponse,
    AgentListResponse,
    AgentCreateVersionResponse,
    AgentGetVersionsResponse,
    AgentListVersionsResponse,
)
```

Methods:

- <code title="post /create-agent">client.agent.<a href="./src/retell/resources/agent.py">create</a>(\*\*<a href="src/retell/types/agent_create_params.py">params</a>) -> <a href="./src/retell/types/agent_response.py">AgentResponse</a></code>
- <code title="get /get-agent/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">retrieve</a>(agent_id, \*\*<a href="src/retell/types/agent_retrieve_params.py">params</a>) -> <a href="./src/retell/types/agent_response.py">AgentResponse</a></code>
- <code title="patch /update-agent/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">update</a>(agent_id, \*\*<a href="src/retell/types/agent_update_params.py">params</a>) -> <a href="./src/retell/types/agent_response.py">AgentResponse</a></code>
- <code title="post /v2/list-agents">client.agent.<a href="./src/retell/resources/agent.py">list</a>(\*\*<a href="src/retell/types/agent_list_params.py">params</a>) -> <a href="./src/retell/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /delete-agent/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">delete</a>(agent_id) -> None</code>
- <code title="post /create-agent-version/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">create_version</a>(agent_id, \*\*<a href="src/retell/types/agent_create_version_params.py">params</a>) -> <a href="./src/retell/types/agent_create_version_response.py">AgentCreateVersionResponse</a></code>
- <code title="delete /delete-agent-version/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">delete_version</a>(agent_id, \*\*<a href="src/retell/types/agent_delete_version_params.py">params</a>) -> None</code>
- <code title="get /get-agent-versions/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">get_versions</a>(agent_id) -> <a href="./src/retell/types/agent_get_versions_response.py">AgentGetVersionsResponse</a></code>
- <code title="get /list-agent-versions/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">list_versions</a>(agent_id, \*\*<a href="src/retell/types/agent_list_versions_params.py">params</a>) -> <a href="./src/retell/types/agent_list_versions_response.py">AgentListVersionsResponse</a></code>
- <code title="post /publish-agent-version/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">publish</a>(agent_id, \*\*<a href="src/retell/types/agent_publish_params.py">params</a>) -> None</code>

# ChatAgent

Types:

```python
from retell.types import (
    ChatAgentResponse,
    ChatAgentListResponse,
    ChatAgentCreateVersionResponse,
    ChatAgentGetVersionsResponse,
)
```

Methods:

- <code title="post /create-chat-agent">client.chat_agent.<a href="./src/retell/resources/chat_agent.py">create</a>(\*\*<a href="src/retell/types/chat_agent_create_params.py">params</a>) -> <a href="./src/retell/types/chat_agent_response.py">ChatAgentResponse</a></code>
- <code title="get /get-chat-agent/{agent_id}">client.chat_agent.<a href="./src/retell/resources/chat_agent.py">retrieve</a>(agent_id, \*\*<a href="src/retell/types/chat_agent_retrieve_params.py">params</a>) -> <a href="./src/retell/types/chat_agent_response.py">ChatAgentResponse</a></code>
- <code title="patch /update-chat-agent/{agent_id}">client.chat_agent.<a href="./src/retell/resources/chat_agent.py">update</a>(agent_id, \*\*<a href="src/retell/types/chat_agent_update_params.py">params</a>) -> <a href="./src/retell/types/chat_agent_response.py">ChatAgentResponse</a></code>
- <code title="post /v2/list-agents">client.chat_agent.<a href="./src/retell/resources/chat_agent.py">list</a>(\*\*<a href="src/retell/types/chat_agent_list_params.py">params</a>) -> <a href="./src/retell/types/chat_agent_list_response.py">ChatAgentListResponse</a></code>
- <code title="delete /delete-chat-agent/{agent_id}">client.chat_agent.<a href="./src/retell/resources/chat_agent.py">delete</a>(agent_id) -> None</code>
- <code title="post /create-agent-version/{agent_id}">client.chat_agent.<a href="./src/retell/resources/chat_agent.py">create_version</a>(agent_id, \*\*<a href="src/retell/types/chat_agent_create_version_params.py">params</a>) -> <a href="./src/retell/types/chat_agent_create_version_response.py">ChatAgentCreateVersionResponse</a></code>
- <code title="delete /delete-agent-version/{agent_id}">client.chat_agent.<a href="./src/retell/resources/chat_agent.py">delete_version</a>(agent_id, \*\*<a href="src/retell/types/chat_agent_delete_version_params.py">params</a>) -> None</code>
- <code title="get /get-chat-agent-versions/{agent_id}">client.chat_agent.<a href="./src/retell/resources/chat_agent.py">get_versions</a>(agent_id) -> <a href="./src/retell/types/chat_agent_get_versions_response.py">ChatAgentGetVersionsResponse</a></code>
- <code title="post /publish-agent-version/{agent_id}">client.chat_agent.<a href="./src/retell/resources/chat_agent.py">publish</a>(agent_id, \*\*<a href="src/retell/types/chat_agent_publish_params.py">params</a>) -> None</code>

# Llm

Types:

```python
from retell.types import LlmResponse, LlmListResponse
```

Methods:

- <code title="post /create-retell-llm">client.llm.<a href="./src/retell/resources/llm.py">create</a>(\*\*<a href="src/retell/types/llm_create_params.py">params</a>) -> <a href="./src/retell/types/llm_response.py">LlmResponse</a></code>
- <code title="get /get-retell-llm/{llm_id}">client.llm.<a href="./src/retell/resources/llm.py">retrieve</a>(llm_id, \*\*<a href="src/retell/types/llm_retrieve_params.py">params</a>) -> <a href="./src/retell/types/llm_response.py">LlmResponse</a></code>
- <code title="patch /update-retell-llm/{llm_id}">client.llm.<a href="./src/retell/resources/llm.py">update</a>(llm_id, \*\*<a href="src/retell/types/llm_update_params.py">params</a>) -> <a href="./src/retell/types/llm_response.py">LlmResponse</a></code>
- <code title="get /v2/list-retell-llms">client.llm.<a href="./src/retell/resources/llm.py">list</a>(\*\*<a href="src/retell/types/llm_list_params.py">params</a>) -> <a href="./src/retell/types/llm_list_response.py">LlmListResponse</a></code>
- <code title="delete /delete-retell-llm/{llm_id}">client.llm.<a href="./src/retell/resources/llm.py">delete</a>(llm_id, \*\*<a href="src/retell/types/llm_delete_params.py">params</a>) -> None</code>

# ConversationFlow

Types:

```python
from retell.types import ConversationFlowResponse, ConversationFlowListResponse
```

Methods:

- <code title="post /create-conversation-flow">client.conversation_flow.<a href="./src/retell/resources/conversation_flow.py">create</a>(\*\*<a href="src/retell/types/conversation_flow_create_params.py">params</a>) -> <a href="./src/retell/types/conversation_flow_response.py">ConversationFlowResponse</a></code>
- <code title="get /get-conversation-flow/{conversation_flow_id}">client.conversation_flow.<a href="./src/retell/resources/conversation_flow.py">retrieve</a>(conversation_flow_id, \*\*<a href="src/retell/types/conversation_flow_retrieve_params.py">params</a>) -> <a href="./src/retell/types/conversation_flow_response.py">ConversationFlowResponse</a></code>
- <code title="patch /update-conversation-flow/{conversation_flow_id}">client.conversation_flow.<a href="./src/retell/resources/conversation_flow.py">update</a>(conversation_flow_id, \*\*<a href="src/retell/types/conversation_flow_update_params.py">params</a>) -> <a href="./src/retell/types/conversation_flow_response.py">ConversationFlowResponse</a></code>
- <code title="get /v2/list-conversation-flows">client.conversation_flow.<a href="./src/retell/resources/conversation_flow.py">list</a>(\*\*<a href="src/retell/types/conversation_flow_list_params.py">params</a>) -> <a href="./src/retell/types/conversation_flow_list_response.py">ConversationFlowListResponse</a></code>
- <code title="delete /delete-conversation-flow/{conversation_flow_id}">client.conversation_flow.<a href="./src/retell/resources/conversation_flow.py">delete</a>(conversation_flow_id, \*\*<a href="src/retell/types/conversation_flow_delete_params.py">params</a>) -> None</code>

# ConversationFlowComponent

Types:

```python
from retell.types import ConversationFlowComponentResponse, ConversationFlowComponentListResponse
```

Methods:

- <code title="post /create-conversation-flow-component">client.conversation_flow_component.<a href="./src/retell/resources/conversation_flow_component.py">create</a>(\*\*<a href="src/retell/types/conversation_flow_component_create_params.py">params</a>) -> <a href="./src/retell/types/conversation_flow_component_response.py">ConversationFlowComponentResponse</a></code>
- <code title="get /get-conversation-flow-component/{conversation_flow_component_id}">client.conversation_flow_component.<a href="./src/retell/resources/conversation_flow_component.py">retrieve</a>(conversation_flow_component_id) -> <a href="./src/retell/types/conversation_flow_component_response.py">ConversationFlowComponentResponse</a></code>
- <code title="patch /update-conversation-flow-component/{conversation_flow_component_id}">client.conversation_flow_component.<a href="./src/retell/resources/conversation_flow_component.py">update</a>(conversation_flow_component_id, \*\*<a href="src/retell/types/conversation_flow_component_update_params.py">params</a>) -> <a href="./src/retell/types/conversation_flow_component_response.py">ConversationFlowComponentResponse</a></code>
- <code title="get /v2/list-conversation-flow-components">client.conversation_flow_component.<a href="./src/retell/resources/conversation_flow_component.py">list</a>(\*\*<a href="src/retell/types/conversation_flow_component_list_params.py">params</a>) -> <a href="./src/retell/types/conversation_flow_component_list_response.py">ConversationFlowComponentListResponse</a></code>
- <code title="delete /delete-conversation-flow-component/{conversation_flow_component_id}">client.conversation_flow_component.<a href="./src/retell/resources/conversation_flow_component.py">delete</a>(conversation_flow_component_id) -> None</code>

# KnowledgeBase

Types:

```python
from retell.types import KnowledgeBaseResponse, KnowledgeBaseListResponse
```

Methods:

- <code title="post /create-knowledge-base">client.knowledge_base.<a href="./src/retell/resources/knowledge_base.py">create</a>(\*\*<a href="src/retell/types/knowledge_base_create_params.py">params</a>) -> <a href="./src/retell/types/knowledge_base_response.py">KnowledgeBaseResponse</a></code>
- <code title="get /get-knowledge-base/{knowledge_base_id}">client.knowledge_base.<a href="./src/retell/resources/knowledge_base.py">retrieve</a>(knowledge_base_id) -> <a href="./src/retell/types/knowledge_base_response.py">KnowledgeBaseResponse</a></code>
- <code title="get /list-knowledge-bases">client.knowledge_base.<a href="./src/retell/resources/knowledge_base.py">list</a>() -> <a href="./src/retell/types/knowledge_base_list_response.py">KnowledgeBaseListResponse</a></code>
- <code title="delete /delete-knowledge-base/{knowledge_base_id}">client.knowledge_base.<a href="./src/retell/resources/knowledge_base.py">delete</a>(knowledge_base_id) -> None</code>
- <code title="post /add-knowledge-base-sources/{knowledge_base_id}">client.knowledge_base.<a href="./src/retell/resources/knowledge_base.py">add_sources</a>(knowledge_base_id, \*\*<a href="src/retell/types/knowledge_base_add_sources_params.py">params</a>) -> <a href="./src/retell/types/knowledge_base_response.py">KnowledgeBaseResponse</a></code>
- <code title="delete /delete-knowledge-base-source/{knowledge_base_id}/source/{source_id}">client.knowledge_base.<a href="./src/retell/resources/knowledge_base.py">delete_source</a>(source_id, \*, knowledge_base_id) -> <a href="./src/retell/types/knowledge_base_response.py">KnowledgeBaseResponse</a></code>

# Voice

Types:

```python
from retell.types import VoiceResponse, VoiceListResponse, VoiceSearchResponse
```

Methods:

- <code title="get /get-voice/{voice_id}">client.voice.<a href="./src/retell/resources/voice.py">retrieve</a>(voice_id) -> <a href="./src/retell/types/voice_response.py">VoiceResponse</a></code>
- <code title="get /list-voices">client.voice.<a href="./src/retell/resources/voice.py">list</a>() -> <a href="./src/retell/types/voice_list_response.py">VoiceListResponse</a></code>
- <code title="post /add-community-voice">client.voice.<a href="./src/retell/resources/voice.py">add_resource</a>(\*\*<a href="src/retell/types/voice_add_resource_params.py">params</a>) -> <a href="./src/retell/types/voice_response.py">VoiceResponse</a></code>
- <code title="post /clone-voice">client.voice.<a href="./src/retell/resources/voice.py">clone</a>(\*\*<a href="src/retell/types/voice_clone_params.py">params</a>) -> <a href="./src/retell/types/voice_response.py">VoiceResponse</a></code>
- <code title="post /search-community-voice">client.voice.<a href="./src/retell/resources/voice.py">search</a>(\*\*<a href="src/retell/types/voice_search_params.py">params</a>) -> <a href="./src/retell/types/voice_search_response.py">VoiceSearchResponse</a></code>

# Concurrency

Types:

```python
from retell.types import ConcurrencyRetrieveResponse
```

Methods:

- <code title="get /get-concurrency">client.concurrency.<a href="./src/retell/resources/concurrency.py">retrieve</a>() -> <a href="./src/retell/types/concurrency_retrieve_response.py">ConcurrencyRetrieveResponse</a></code>

# Identity

Types:

```python
from retell.types import IdentityRetrieveResponse
```

Methods:

- <code title="get /get-api-key-info">client.identity.<a href="./src/retell/resources/identity.py">retrieve</a>() -> <a href="./src/retell/types/identity_retrieve_response.py">IdentityRetrieveResponse</a></code>

# ExportRequest

Types:

```python
from retell.types import ExportRequestListResponse
```

Methods:

- <code title="get /v2/list-export-requests">client.export_request.<a href="./src/retell/resources/export_request.py">list</a>(\*\*<a href="src/retell/types/export_request_list_params.py">params</a>) -> <a href="./src/retell/types/export_request_list_response.py">ExportRequestListResponse</a></code>

# BatchCall

Types:

```python
from retell.types import BatchCallResponse
```

Methods:

- <code title="post /create-batch-call">client.batch_call.<a href="./src/retell/resources/batch_call.py">create_batch_call</a>(\*\*<a href="src/retell/types/batch_call_create_batch_call_params.py">params</a>) -> <a href="./src/retell/types/batch_call_response.py">BatchCallResponse</a></code>

# Tests

Types:

```python
from retell.types import (
    BatchTestResponse,
    TestCaseDefinitionResponse,
    TestCaseJobResponse,
    TestListBatchTestsResponse,
    TestListTestCaseDefinitionsResponse,
    TestListTestRunsResponse,
)
```

Methods:

- <code title="post /create-batch-test">client.tests.<a href="./src/retell/resources/tests.py">create_batch_test</a>(\*\*<a href="src/retell/types/test_create_batch_test_params.py">params</a>) -> <a href="./src/retell/types/batch_test_response.py">BatchTestResponse</a></code>
- <code title="post /create-test-case-definition">client.tests.<a href="./src/retell/resources/tests.py">create_test_case_definition</a>(\*\*<a href="src/retell/types/test_create_test_case_definition_params.py">params</a>) -> <a href="./src/retell/types/test_case_definition_response.py">TestCaseDefinitionResponse</a></code>
- <code title="delete /delete-test-case-definition/{test_case_definition_id}">client.tests.<a href="./src/retell/resources/tests.py">delete_test_case_definition</a>(test_case_definition_id) -> None</code>
- <code title="get /get-batch-test/{test_case_batch_job_id}">client.tests.<a href="./src/retell/resources/tests.py">get_batch_test</a>(test_case_batch_job_id) -> <a href="./src/retell/types/batch_test_response.py">BatchTestResponse</a></code>
- <code title="get /get-test-case-definition/{test_case_definition_id}">client.tests.<a href="./src/retell/resources/tests.py">get_test_case_definition</a>(test_case_definition_id) -> <a href="./src/retell/types/test_case_definition_response.py">TestCaseDefinitionResponse</a></code>
- <code title="get /get-test-run/{test_case_job_id}">client.tests.<a href="./src/retell/resources/tests.py">get_test_run</a>(test_case_job_id) -> <a href="./src/retell/types/test_case_job_response.py">TestCaseJobResponse</a></code>
- <code title="get /v2/list-batch-tests">client.tests.<a href="./src/retell/resources/tests.py">list_batch_tests</a>(\*\*<a href="src/retell/types/test_list_batch_tests_params.py">params</a>) -> <a href="./src/retell/types/test_list_batch_tests_response.py">TestListBatchTestsResponse</a></code>
- <code title="get /v2/list-test-case-definitions">client.tests.<a href="./src/retell/resources/tests.py">list_test_case_definitions</a>(\*\*<a href="src/retell/types/test_list_test_case_definitions_params.py">params</a>) -> <a href="./src/retell/types/test_list_test_case_definitions_response.py">TestListTestCaseDefinitionsResponse</a></code>
- <code title="get /v2/list-test-runs/{test_case_batch_job_id}">client.tests.<a href="./src/retell/resources/tests.py">list_test_runs</a>(test_case_batch_job_id, \*\*<a href="src/retell/types/test_list_test_runs_params.py">params</a>) -> <a href="./src/retell/types/test_list_test_runs_response.py">TestListTestRunsResponse</a></code>
- <code title="put /update-test-case-definition/{test_case_definition_id}">client.tests.<a href="./src/retell/resources/tests.py">update_test_case_definition</a>(test_case_definition_id, \*\*<a href="src/retell/types/test_update_test_case_definition_params.py">params</a>) -> <a href="./src/retell/types/test_case_definition_response.py">TestCaseDefinitionResponse</a></code>

# Playground

Types:

```python
from retell.types import PlaygroundCompletionResponse
```

Methods:

- <code title="post /agent-playground-completion/{agent_id}">client.playground.<a href="./src/retell/resources/playground.py">completion</a>(agent_id, \*\*<a href="src/retell/types/playground_completion_params.py">params</a>) -> <a href="./src/retell/types/playground_completion_response.py">PlaygroundCompletionResponse</a></code>

# McpTool

Types:

```python
from retell.types import McpToolDefinition, McpToolGetMcpToolsResponse
```

Methods:

- <code title="get /get-mcp-tools/{agent_id}">client.mcp_tool.<a href="./src/retell/resources/mcp_tool.py">get_mcp_tools</a>(agent_id, \*\*<a href="src/retell/types/mcp_tool_get_mcp_tools_params.py">params</a>) -> <a href="./src/retell/types/mcp_tool_get_mcp_tools_response.py">McpToolGetMcpToolsResponse</a></code>

# Contact

Types:

```python
from retell.types import (
    ContactResponse,
    ContactListResponse,
    ContactBackfillAnalysisDataResponse,
    ContactGetBackfillJobStatusResponse,
    ContactListConversationsResponse,
)
```

Methods:

- <code title="post /create-contact">client.contact.<a href="./src/retell/resources/contact.py">create</a>(\*\*<a href="src/retell/types/contact_create_params.py">params</a>) -> <a href="./src/retell/types/contact_response.py">ContactResponse</a></code>
- <code title="patch /update-contact/{contact_id}">client.contact.<a href="./src/retell/resources/contact.py">update</a>(contact_id, \*\*<a href="src/retell/types/contact_update_params.py">params</a>) -> <a href="./src/retell/types/contact_response.py">ContactResponse</a></code>
- <code title="post /list-contacts">client.contact.<a href="./src/retell/resources/contact.py">list</a>(\*\*<a href="src/retell/types/contact_list_params.py">params</a>) -> <a href="./src/retell/types/contact_list_response.py">ContactListResponse</a></code>
- <code title="delete /delete-contact/{contact_id}">client.contact.<a href="./src/retell/resources/contact.py">delete</a>(contact_id) -> None</code>
- <code title="post /backfill-contact-analysis-data">client.contact.<a href="./src/retell/resources/contact.py">backfill_analysis_data</a>(\*\*<a href="src/retell/types/contact_backfill_analysis_data_params.py">params</a>) -> <a href="./src/retell/types/contact_backfill_analysis_data_response.py">ContactBackfillAnalysisDataResponse</a></code>
- <code title="get /get-contact/{contact_id}">client.contact.<a href="./src/retell/resources/contact.py">get</a>(contact_id) -> <a href="./src/retell/types/contact_response.py">ContactResponse</a></code>
- <code title="get /get-backfill-contact-job-status">client.contact.<a href="./src/retell/resources/contact.py">get_backfill_job_status</a>() -> <a href="./src/retell/types/contact_get_backfill_job_status_response.py">ContactGetBackfillJobStatusResponse</a></code>
- <code title="get /get-contact-by-phone/{phone_number}">client.contact.<a href="./src/retell/resources/contact.py">get_by_phone</a>(phone_number) -> <a href="./src/retell/types/contact_response.py">ContactResponse</a></code>
- <code title="get /list-contact-conversations/{contact_id}">client.contact.<a href="./src/retell/resources/contact.py">list_conversations</a>(contact_id, \*\*<a href="src/retell/types/contact_list_conversations_params.py">params</a>) -> <a href="./src/retell/types/contact_list_conversations_response.py">ContactListConversationsResponse</a></code>

# App

Types:

```python
from retell.types import AppResponse, AppListResponse, AppListUsagesResponse, AppTestAuthResponse
```

Methods:

- <code title="post /create-app">client.app.<a href="./src/retell/resources/app.py">create</a>(\*\*<a href="src/retell/types/app_create_params.py">params</a>) -> <a href="./src/retell/types/app_response.py">AppResponse</a></code>
- <code title="patch /update-app/{app_id}">client.app.<a href="./src/retell/resources/app.py">update</a>(app_id, \*\*<a href="src/retell/types/app_update_params.py">params</a>) -> <a href="./src/retell/types/app_response.py">AppResponse</a></code>
- <code title="get /list-apps">client.app.<a href="./src/retell/resources/app.py">list</a>(\*\*<a href="src/retell/types/app_list_params.py">params</a>) -> <a href="./src/retell/types/app_list_response.py">AppListResponse</a></code>
- <code title="delete /delete-app/{app_id}">client.app.<a href="./src/retell/resources/app.py">delete</a>(app_id, \*\*<a href="src/retell/types/app_delete_params.py">params</a>) -> None</code>
- <code title="get /get-app/{app_id}">client.app.<a href="./src/retell/resources/app.py">get</a>(app_id) -> <a href="./src/retell/types/app_response.py">AppResponse</a></code>
- <code title="get /list-app-usages/{app_id}">client.app.<a href="./src/retell/resources/app.py">list_usages</a>(app_id, \*\*<a href="src/retell/types/app_list_usages_params.py">params</a>) -> <a href="./src/retell/types/app_list_usages_response.py">AppListUsagesResponse</a></code>
- <code title="post /test-app-auth/{app_id}">client.app.<a href="./src/retell/resources/app.py">test_auth</a>(app_id) -> <a href="./src/retell/types/app_test_auth_response.py">AppTestAuthResponse</a></code>

# CRM

Types:

```python
from retell.types import (
    CRMConfig,
    CRMGetSchemaResponse,
    CRMGetSyncJobStatusResponse,
    CRMRunSyncJobResponse,
)
```

Methods:

- <code title="get /get-crm-config">client.crm.<a href="./src/retell/resources/crm.py">get_config</a>() -> <a href="./src/retell/types/crm_config.py">CRMConfig</a></code>
- <code title="get /get-crm-schema">client.crm.<a href="./src/retell/resources/crm.py">get_schema</a>(\*\*<a href="src/retell/types/crm_get_schema_params.py">params</a>) -> <a href="./src/retell/types/crm_get_schema_response.py">CRMGetSchemaResponse</a></code>
- <code title="get /get-sync-job-status">client.crm.<a href="./src/retell/resources/crm.py">get_sync_job_status</a>() -> <a href="./src/retell/types/crm_get_sync_job_status_response.py">CRMGetSyncJobStatusResponse</a></code>
- <code title="post /run-sync-job">client.crm.<a href="./src/retell/resources/crm.py">run_sync_job</a>() -> <a href="./src/retell/types/crm_run_sync_job_response.py">CRMRunSyncJobResponse</a></code>
- <code title="post /update-crm-config">client.crm.<a href="./src/retell/resources/crm.py">update_config</a>(\*\*<a href="src/retell/types/crm_update_config_params.py">params</a>) -> <a href="./src/retell/types/crm_config.py">CRMConfig</a></code>
