# Call

Types:

```python
from retell.types import CallResponse, PhoneCallResponse, WebCallResponse, CallListResponse
```

Methods:

- <code title="get /v2/get-call/{call_id}">client.call.<a href="./src/retell/resources/call.py">retrieve</a>(call_id) -> <a href="./src/retell/types/call_response.py">CallResponse</a></code>
- <code title="post /v2/list-calls">client.call.<a href="./src/retell/resources/call.py">list</a>(\*\*<a href="src/retell/types/call_list_params.py">params</a>) -> <a href="./src/retell/types/call_list_response.py">CallListResponse</a></code>
- <code title="post /v2/create-phone-call">client.call.<a href="./src/retell/resources/call.py">create_phone_call</a>(\*\*<a href="src/retell/types/call_create_phone_call_params.py">params</a>) -> <a href="./src/retell/types/phone_call_response.py">PhoneCallResponse</a></code>
- <code title="post /v2/create-web-call">client.call.<a href="./src/retell/resources/call.py">create_web_call</a>(\*\*<a href="src/retell/types/call_create_web_call_params.py">params</a>) -> <a href="./src/retell/types/web_call_response.py">WebCallResponse</a></code>
- <code title="post /v2/register-phone-call">client.call.<a href="./src/retell/resources/call.py">register_phone_call</a>(\*\*<a href="src/retell/types/call_register_phone_call_params.py">params</a>) -> <a href="./src/retell/types/phone_call_response.py">PhoneCallResponse</a></code>

# PhoneNumber

Types:

```python
from retell.types import PhoneNumberResponse, PhoneNumberListResponse
```

Methods:

- <code title="post /create-phone-number">client.phone_number.<a href="./src/retell/resources/phone_number.py">create</a>(\*\*<a href="src/retell/types/phone_number_create_params.py">params</a>) -> <a href="./src/retell/types/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="get /get-phone-number/{phone_number}">client.phone_number.<a href="./src/retell/resources/phone_number.py">retrieve</a>(phone_number) -> <a href="./src/retell/types/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="patch /update-phone-number/{phone_number}">client.phone_number.<a href="./src/retell/resources/phone_number.py">update</a>(phone_number, \*\*<a href="src/retell/types/phone_number_update_params.py">params</a>) -> <a href="./src/retell/types/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="get /list-phone-numbers">client.phone_number.<a href="./src/retell/resources/phone_number.py">list</a>() -> <a href="./src/retell/types/phone_number_list_response.py">PhoneNumberListResponse</a></code>
- <code title="delete /delete-phone-number/{phone_number}">client.phone_number.<a href="./src/retell/resources/phone_number.py">delete</a>(phone_number) -> None</code>
- <code title="post /import-phone-number">client.phone*number.<a href="./src/retell/resources/phone_number.py">import*</a>(\*\*<a href="src/retell/types/phone_number_import_params.py">params</a>) -> <a href="./src/retell/types/phone_number_response.py">PhoneNumberResponse</a></code>

# Agent

Types:

```python
from retell.types import AgentResponse, AgentListResponse
```

Methods:

- <code title="post /create-agent">client.agent.<a href="./src/retell/resources/agent.py">create</a>(\*\*<a href="src/retell/types/agent_create_params.py">params</a>) -> <a href="./src/retell/types/agent_response.py">AgentResponse</a></code>
- <code title="get /get-agent/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">retrieve</a>(agent_id) -> <a href="./src/retell/types/agent_response.py">AgentResponse</a></code>
- <code title="patch /update-agent/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">update</a>(agent_id, \*\*<a href="src/retell/types/agent_update_params.py">params</a>) -> <a href="./src/retell/types/agent_response.py">AgentResponse</a></code>
- <code title="get /list-agents">client.agent.<a href="./src/retell/resources/agent.py">list</a>() -> <a href="./src/retell/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /delete-agent/{agent_id}">client.agent.<a href="./src/retell/resources/agent.py">delete</a>(agent_id) -> None</code>

# Llm

Types:

```python
from retell.types import LlmResponse, LlmListResponse
```

Methods:

- <code title="post /create-retell-llm">client.llm.<a href="./src/retell/resources/llm.py">create</a>(\*\*<a href="src/retell/types/llm_create_params.py">params</a>) -> <a href="./src/retell/types/llm_response.py">LlmResponse</a></code>
- <code title="get /get-retell-llm/{llm_id}">client.llm.<a href="./src/retell/resources/llm.py">retrieve</a>(llm_id) -> <a href="./src/retell/types/llm_response.py">LlmResponse</a></code>
- <code title="patch /update-retell-llm/{llm_id}">client.llm.<a href="./src/retell/resources/llm.py">update</a>(llm_id, \*\*<a href="src/retell/types/llm_update_params.py">params</a>) -> <a href="./src/retell/types/llm_response.py">LlmResponse</a></code>
- <code title="get /list-retell-llms">client.llm.<a href="./src/retell/resources/llm.py">list</a>() -> <a href="./src/retell/types/llm_list_response.py">LlmListResponse</a></code>
- <code title="delete /delete-retell-llm/{llm_id}">client.llm.<a href="./src/retell/resources/llm.py">delete</a>(llm_id) -> None</code>

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

# Voice

Types:

```python
from retell.types import VoiceResponse, VoiceListResponse
```

Methods:

- <code title="get /get-voice/{voice_id}">client.voice.<a href="./src/retell/resources/voice.py">retrieve</a>(voice_id) -> <a href="./src/retell/types/voice_response.py">VoiceResponse</a></code>
- <code title="get /list-voices">client.voice.<a href="./src/retell/resources/voice.py">list</a>() -> <a href="./src/retell/types/voice_list_response.py">VoiceListResponse</a></code>

# Concurrency

Types:

```python
from retell.types import ConcurrencyRetrieveResponse
```

Methods:

- <code title="get /get-concurrency">client.concurrency.<a href="./src/retell/resources/concurrency.py">retrieve</a>() -> <a href="./src/retell/types/concurrency_retrieve_response.py">ConcurrencyRetrieveResponse</a></code>
