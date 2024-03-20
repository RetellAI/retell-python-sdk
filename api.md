# Calls

Types:

```python
from retell_ai.types import CallBase, CallBase, CallListResponse
```

Methods:

- <code title="get /get-call/{call_id}">client.calls.<a href="./src/retell_ai/resources/calls.py">retrieve</a>(call_id) -> <a href="./src/retell_ai/types/call_base.py">CallBase</a></code>
- <code title="get /list-calls">client.calls.<a href="./src/retell_ai/resources/calls.py">list</a>(\*\*<a href="src/retell_ai/types/call_list_params.py">params</a>) -> <a href="./src/retell_ai/types/call_list_response.py">CallListResponse</a></code>
- <code title="post /register-call">client.calls.<a href="./src/retell_ai/resources/calls.py">register</a>(\*\*<a href="src/retell_ai/types/call_register_params.py">params</a>) -> <a href="./src/retell_ai/types/call_base.py">CallBase</a></code>

# Agents

Types:

```python
from retell_ai.types import (
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentUpdateResponse,
    AgentListResponse,
)
```

Methods:

- <code title="post /create-agent">client.agents.<a href="./src/retell_ai/resources/agents.py">create</a>(\*\*<a href="src/retell_ai/types/agent_create_params.py">params</a>) -> <a href="./src/retell_ai/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /get-agent/{agent_id}">client.agents.<a href="./src/retell_ai/resources/agents.py">retrieve</a>(agent_id) -> <a href="./src/retell_ai/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="patch /update-agent/{agent_id}">client.agents.<a href="./src/retell_ai/resources/agents.py">update</a>(agent_id, \*\*<a href="src/retell_ai/types/agent_update_params.py">params</a>) -> <a href="./src/retell_ai/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /list-agents">client.agents.<a href="./src/retell_ai/resources/agents.py">list</a>() -> <a href="./src/retell_ai/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /delete-agent/{agent_id}">client.agents.<a href="./src/retell_ai/resources/agents.py">delete</a>(agent_id) -> None</code>

# Llm

Types:

```python
from retell_ai.types import (
    LlmCreateResponse,
    LlmRetrieveResponse,
    LlmUpdateResponse,
    LlmListResponse,
)
```

Methods:

- <code title="post /create-retell-llm">client.llm.<a href="./src/retell_ai/resources/llm.py">create</a>(\*\*<a href="src/retell_ai/types/llm_create_params.py">params</a>) -> <a href="./src/retell_ai/types/llm_create_response.py">LlmCreateResponse</a></code>
- <code title="get /get-retell-llm/{llm_id}">client.llm.<a href="./src/retell_ai/resources/llm.py">retrieve</a>(llm_id) -> <a href="./src/retell_ai/types/llm_retrieve_response.py">LlmRetrieveResponse</a></code>
- <code title="patch /update-retell-llm/{llm_id}">client.llm.<a href="./src/retell_ai/resources/llm.py">update</a>(llm_id, \*\*<a href="src/retell_ai/types/llm_update_params.py">params</a>) -> <a href="./src/retell_ai/types/llm_update_response.py">LlmUpdateResponse</a></code>
- <code title="get /list-retell-llm">client.llm.<a href="./src/retell_ai/resources/llm.py">list</a>() -> <a href="./src/retell_ai/types/llm_list_response.py">LlmListResponse</a></code>
- <code title="delete /delete-retell-llm/{llm_id}">client.llm.<a href="./src/retell_ai/resources/llm.py">delete</a>(llm_id) -> None</code>
