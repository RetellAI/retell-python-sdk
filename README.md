# openapi

<div align="left">
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start SDK Installation [installation] -->

## SDK Installation

```bash
pip install retell-sdk
```

<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->

## SDK Example Usage

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

<!-- Start Available Resources and Operations [operations] -->

## Available Resources and Operations

### [RetellClient SDK](docs/sdks/retellclient/README.md)

- [create_agent](docs/sdks/retellclient/README.md#create_agent) - Create a new agent
- [create_phone_call](docs/sdks/retellclient/README.md#create_phone_call) - Initiate an outbound phone call.
- [create_phone_number](docs/sdks/retellclient/README.md#create_phone_number) - Create a new phone number
- [delete_agent](docs/sdks/retellclient/README.md#delete_agent) - Delete an existing agent
- [delete_phone_number](docs/sdks/retellclient/README.md#delete_phone_number) - Delete a specific phone number
- [get_agent](docs/sdks/retellclient/README.md#get_agent) - Retrieve details of a specific agent
- [get_call](docs/sdks/retellclient/README.md#get_call) - Retrieve details of a specific call
- [get_phone_number](docs/sdks/retellclient/README.md#get_phone_number) - Retrieve info about a specific number
- [list_agents](docs/sdks/retellclient/README.md#list_agents) - List all agents
- [list_calls](docs/sdks/retellclient/README.md#list_calls) - Retrieve call details
- [list_phone_numbers](docs/sdks/retellclient/README.md#list_phone_numbers) - List all purchased and active phone numbers
- [update_agent](docs/sdks/retellclient/README.md#update_agent) - Update an existing agent
- [update_phone_agent](docs/sdks/retellclient/README.md#update_phone_agent) - Update an existing phone number
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->

## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an error. If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                              | Status Code | Content Type     |
| ----------------------------------------- | ----------- | ---------------- |
| errors.CreateAgentResponseBody            | 400         | application/json |
| errors.CreateAgentResponseResponseBody    | 401         | application/json |
| errors.CreateAgentResponse422ResponseBody | 422         | application/json |
| errors.CreateAgentResponse500ResponseBody | 500         | application/json |
| errors.SDKError                           | 400-600     | _/_              |

### Example

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

res = None
try:
    res = s.create_agent(req)
except errors.CreateAgentResponseBody as e:
    print(e)  # handle exception
    raise(e)
except errors.CreateAgentResponseResponseBody as e:
    print(e)  # handle exception
    raise(e)
except errors.CreateAgentResponse422ResponseBody as e:
    print(e)  # handle exception
    raise(e)
except errors.CreateAgentResponse500ResponseBody as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.agent is not None:
    # handle response
    pass
```

<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->

## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                   | Variables |
| --- | ------------------------ | --------- |
| 0   | `https://api.re-tell.ai` | None      |

#### Example

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    server_idx=0,
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

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import retellclient
from retellclient.models import operations

s = retellclient.RetellClient(
    server_url="https://api.re-tell.ai",
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

<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->

## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library. In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:

```python
import retellclient
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = retellclient.RetellClient(client: http_client)
```

<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->

## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type | Scheme      |
| --------- | ---- | ----------- |
| `api_key` | http | HTTP Bearer |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:

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

<!-- End Authentication [security] -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!
