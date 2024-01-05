<!-- Start SDK Example Usage [usage] -->
### Create a new voice AI agent

Create a new agent

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)

req = operations.CreateAgentRequestBody(
    agent_name='Jarvis',
    begin_message='Hello there, how can I help you?',
    enable_begin_message=True,
    enable_end_call=True,
    enable_end_message=False,
    end_message='Hope you have a good day, goodbye.',
    prompt='You are a marketing assistant. You help come up with creative content ideas and content like marketing emails, blog posts, tweets, ad copy and product descriptions. You respond concisely, with filler words in it.',
    voice_id='elevenlabs-xxcrwXReTKMHWjqi7Q27',
)

res = s.create_agent(req)

if res.agent is not None:
    # handle response
    pass
```

### Create an outbound phone call

Initiate an outbound phone call.

```python
import retellclient
from retellclient.models import components, operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)

req = operations.CreatePhoneCallRequestBody(
    agent_prompt_params=[
        components.AgentPromptParams(
            name='username',
            value='Adam',
        ),
    ],
    phone_number=operations.PhoneNumber(
        from_='+14159095857',
        to='+14159095858',
    ),
)

res = s.create_phone_call(req)

if res.object is not None:
    # handle response
    pass
```

### Create a new phone number

Create a new phone number

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)

req = operations.CreatePhoneNumberRequestBody(
    agent_id='oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD',
    area_code=415,
)

res = s.create_phone_number(req)

if res.phone_number is not None:
    # handle response
    pass
```

### Delete an existing agent

Delete an existing agent

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)


res = s.delete_agent(agent_id='oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD')

if res.status_code == 200:
    # handle response
    pass
```

### Delete a specific phone number

Delete a specific phone number

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)


res = s.delete_phone_number(phone_number='string')

if res.status_code == 200:
    # handle response
    pass
```

### Retrieve details of an agent

Retrieve details of a specific agent

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)


res = s.get_agent(agent_id='16b980523634a6dc504898cda492e939')

if res.agent is not None:
    # handle response
    pass
```

### Retrieve a on-going or finished call

Retrieve details of a specific call

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)


res = s.get_call(call_id='119c3f8e47135a29e65947eeb34cf12d')

if res.call_detail is not None:
    # handle response
    pass
```

### Retrieve info about a specific number

Retrieve info about a specific number

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)


res = s.get_phone_number(phone_number='+14159095857')

if res.phone_number is not None:
    # handle response
    pass
```

### List all agents

List all agents

```python
import retellclient

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)


res = s.list_agents()

if res.classes is not None:
    # handle response
    pass
```

### List all web or phone calls

Retrieve call details

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)


res = s.list_calls(filter_criteria=operations.FilterCriteria(
    after_end_timestamp=1703302428800,
    after_start_timestamp=1703302407300,
    agent_id=[
        'oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD',
    ],
    before_end_timestamp=1703302428899,
    before_start_timestamp=1703302407399,
    call_type=[
        operations.CallType.INBOUND_PHONE_CALL,
        operations.CallType.OUTBOUND_PHONE_CALL,
    ],
), limit=666195, sort_order=operations.SortOrder.DESCENDING)

if res.classes is not None:
    # handle response
    pass
```

### List all purchased and active phone numbers

List all purchased and active phone numbers

```python
import retellclient

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)


res = s.list_phone_numbers()

if res.classes is not None:
    # handle response
    pass
```

### Update an existing agent

Update an existing agent

```python
import retellclient
from retellclient.models import components, operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)


res = s.update_agent(agent_no_default_no_required=components.AgentNoDefaultNoRequired(
    agent_name='Jarvis',
    begin_message='Hello there, how can I help you.',
    enable_begin_message=True,
    enable_end_call=True,
    enable_end_message=False,
    end_message='Hope you have a good day, goodbye.',
    prompt='You are a marketing assistant. You help come up with creative content ideas and content like marketing emails, blog posts, tweets, ad copy and product descriptions. You respond concisely, with filler words in it.',
    voice_id='elevenlabs-xxcrwXReTKMHWjqi7Q27',
), agent_id='16b980523634a6dc504898cda492e939')

if res.agent is not None:
    # handle response
    pass
```

### Update an existing phone number

Update an existing phone number

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    api_key="YOUR_API_KEY",
)


res = s.update_phone_agent(request_body=operations.UpdatePhoneAgentRequestBody(
    agent_id='oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD',
), phone_number='+14159095857')

if res.phone_number is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->