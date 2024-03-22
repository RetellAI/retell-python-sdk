# RegisterCalls

Types:

```python
from retell_ai.types import RegisterCallCreateResponse
```

Methods:

- <code title="post /register-call">client.register_calls.<a href="./src/retell_ai/resources/register_calls.py">create</a>(\*\*<a href="src/retell_ai/types/register_call_create_params.py">params</a>) -> <a href="./src/retell_ai/types/register_call_create_response.py">RegisterCallCreateResponse</a></code>

# Calls

Types:

```python
from retell_ai.types import CallRetrieveResponse, CallListResponse
```

Methods:

- <code title="get /get-call/{call_id}">client.calls.<a href="./src/retell_ai/resources/calls.py">retrieve</a>(call_id) -> <a href="./src/retell_ai/types/call_retrieve_response.py">CallRetrieveResponse</a></code>
- <code title="get /list-calls">client.calls.<a href="./src/retell_ai/resources/calls.py">list</a>(\*\*<a href="src/retell_ai/types/call_list_params.py">params</a>) -> <a href="./src/retell_ai/types/call_list_response.py">CallListResponse</a></code>

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

# RetellLlms

Types:

```python
from retell_ai.types import (
    RetellLlmCreateResponse,
    RetellLlmRetrieveResponse,
    RetellLlmUpdateResponse,
    RetellLlmListResponse,
)
```

Methods:

- <code title="post /create-retell-llm">client.retell_llms.<a href="./src/retell_ai/resources/retell_llms.py">create</a>(\*\*<a href="src/retell_ai/types/retell_llm_create_params.py">params</a>) -> <a href="./src/retell_ai/types/retell_llm_create_response.py">RetellLlmCreateResponse</a></code>
- <code title="get /get-retell-llm/{llm_id}">client.retell_llms.<a href="./src/retell_ai/resources/retell_llms.py">retrieve</a>(llm_id) -> <a href="./src/retell_ai/types/retell_llm_retrieve_response.py">RetellLlmRetrieveResponse</a></code>
- <code title="patch /update-retell-llm/{llm_id}">client.retell_llms.<a href="./src/retell_ai/resources/retell_llms.py">update</a>(llm_id, \*\*<a href="src/retell_ai/types/retell_llm_update_params.py">params</a>) -> <a href="./src/retell_ai/types/retell_llm_update_response.py">RetellLlmUpdateResponse</a></code>
- <code title="get /list-retell-llm">client.retell_llms.<a href="./src/retell_ai/resources/retell_llms.py">list</a>() -> <a href="./src/retell_ai/types/retell_llm_list_response.py">RetellLlmListResponse</a></code>
- <code title="delete /delete-retell-llm/{llm_id}">client.retell_llms.<a href="./src/retell_ai/resources/retell_llms.py">delete</a>(llm_id) -> None</code>
