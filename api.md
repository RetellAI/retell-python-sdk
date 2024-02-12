# Calls

Types:

```python
from toddlzt.types import CallBase, CallBase, CallListResponse
```

Methods:

- <code title="get /get-call/{call_id}">client.calls.<a href="./src/toddlzt/resources/calls.py">retrieve</a>(call_id) -> <a href="./src/toddlzt/types/call_base.py">CallBase</a></code>
- <code title="get /list-calls">client.calls.<a href="./src/toddlzt/resources/calls.py">list</a>(\*\*<a href="src/toddlzt/types/call_list_params.py">params</a>) -> <a href="./src/toddlzt/types/call_list_response.py">CallListResponse</a></code>
- <code title="post /register-call">client.calls.<a href="./src/toddlzt/resources/calls.py">register</a>(\*\*<a href="src/toddlzt/types/call_register_params.py">params</a>) -> <a href="./src/toddlzt/types/call_base.py">CallBase</a></code>

# Agents

Types:

```python
from toddlzt.types import (
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentUpdateResponse,
    AgentListResponse,
)
```

Methods:

- <code title="post /create-agent">client.agents.<a href="./src/toddlzt/resources/agents.py">create</a>(\*\*<a href="src/toddlzt/types/agent_create_params.py">params</a>) -> <a href="./src/toddlzt/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /get-agent/{agent_id}">client.agents.<a href="./src/toddlzt/resources/agents.py">retrieve</a>(agent_id) -> <a href="./src/toddlzt/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="patch /update-agent/{agent_id}">client.agents.<a href="./src/toddlzt/resources/agents.py">update</a>(agent_id, \*\*<a href="src/toddlzt/types/agent_update_params.py">params</a>) -> <a href="./src/toddlzt/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /list-agents">client.agents.<a href="./src/toddlzt/resources/agents.py">list</a>() -> <a href="./src/toddlzt/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /delete-agent/{agent_id}">client.agents.<a href="./src/toddlzt/resources/agents.py">delete</a>(agent_id) -> None</code>
