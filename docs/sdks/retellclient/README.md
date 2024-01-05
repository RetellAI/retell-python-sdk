# RetellClient SDK


## Overview

### Available Operations

* [create_agent](#create_agent) - Create a new agent
* [create_phone_call](#create_phone_call) - Initiate an outbound phone call.
* [create_phone_number](#create_phone_number) - Create a new phone number
* [delete_agent](#delete_agent) - Delete an existing agent
* [delete_phone_number](#delete_phone_number) - Delete a specific phone number
* [get_agent](#get_agent) - Retrieve details of a specific agent
* [get_call](#get_call) - Retrieve details of a specific call
* [get_phone_number](#get_phone_number) - Retrieve info about a specific number
* [list_agents](#list_agents) - List all agents
* [list_calls](#list_calls) - Retrieve call details
* [list_phone_numbers](#list_phone_numbers) - List all purchased and active phone numbers
* [update_agent](#update_agent) - Update an existing agent
* [update_phone_agent](#update_phone_agent) - Update an existing phone number

## create_agent

Create a new agent

### Example Usage

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

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateAgentRequestBody](../../models/operations/createagentrequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateAgentResponse](../../models/operations/createagentresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.CreateAgentResponseBody            | 400                                       | application/json                          |
| errors.CreateAgentResponseResponseBody    | 401                                       | application/json                          |
| errors.CreateAgentResponse422ResponseBody | 422                                       | application/json                          |
| errors.CreateAgentResponse500ResponseBody | 500                                       | application/json                          |
| errors.SDKError                           | 400-600                                   | */*                                       |

## create_phone_call

Initiate an outbound phone call.

### Example Usage

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

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreatePhoneCallRequestBody](../../models/operations/createphonecallrequestbody.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.CreatePhoneCallResponse](../../models/operations/createphonecallresponse.md)**
### Errors

| Error Object                                  | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| errors.CreatePhoneCallResponseBody            | 400                                           | application/json                              |
| errors.CreatePhoneCallResponseResponseBody    | 401                                           | application/json                              |
| errors.CreatePhoneCallResponse402ResponseBody | 402                                           | application/json                              |
| errors.CreatePhoneCallResponse422ResponseBody | 422                                           | application/json                              |
| errors.CreatePhoneCallResponse429ResponseBody | 429                                           | application/json                              |
| errors.CreatePhoneCallResponse500ResponseBody | 500                                           | application/json                              |
| errors.SDKError                               | 400-600                                       | */*                                           |

## create_phone_number

Create a new phone number

### Example Usage

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

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreatePhoneNumberRequestBody](../../models/operations/createphonenumberrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.CreatePhoneNumberResponse](../../models/operations/createphonenumberresponse.md)**
### Errors

| Error Object                                    | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| errors.CreatePhoneNumberResponseBody            | 400                                             | application/json                                |
| errors.CreatePhoneNumberResponseResponseBody    | 401                                             | application/json                                |
| errors.CreatePhoneNumberResponse402ResponseBody | 402                                             | application/json                                |
| errors.CreatePhoneNumberResponse422ResponseBody | 422                                             | application/json                                |
| errors.CreatePhoneNumberResponse500ResponseBody | 500                                             | application/json                                |
| errors.SDKError                                 | 400-600                                         | */*                                             |

## delete_agent

Delete an existing agent

### Example Usage

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

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `agent_id`                            | *str*                                 | :heavy_check_mark:                    | Unique id of the agent to be deleted. | oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD      |


### Response

**[operations.DeleteAgentResponse](../../models/operations/deleteagentresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.DeleteAgentResponseBody            | 400                                       | application/json                          |
| errors.DeleteAgentResponseResponseBody    | 401                                       | application/json                          |
| errors.DeleteAgentResponse422ResponseBody | 422                                       | application/json                          |
| errors.DeleteAgentResponse500ResponseBody | 500                                       | application/json                          |
| errors.SDKError                           | 400-600                                   | */*                                       |

## delete_phone_number

Delete a specific phone number

### Example Usage

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

### Parameters

| Parameter                               | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `phone_number`                          | *str*                                   | :heavy_check_mark:                      | Phone number to delete in E.164 format. |


### Response

**[operations.DeletePhoneNumberResponse](../../models/operations/deletephonenumberresponse.md)**
### Errors

| Error Object                                    | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| errors.DeletePhoneNumberResponseBody            | 400                                             | application/json                                |
| errors.DeletePhoneNumberResponseResponseBody    | 401                                             | application/json                                |
| errors.DeletePhoneNumberResponse422ResponseBody | 422                                             | application/json                                |
| errors.DeletePhoneNumberResponse500ResponseBody | 500                                             | application/json                                |
| errors.SDKError                                 | 400-600                                         | */*                                             |

## get_agent

Retrieve details of a specific agent

### Example Usage

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

### Parameters

| Parameter                               | Type                                    | Required                                | Description                             | Example                                 |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `agent_id`                              | *str*                                   | :heavy_check_mark:                      | Unique id of the agent to be retrieved. | 16b980523634a6dc504898cda492e939        |


### Response

**[operations.GetAgentResponse](../../models/operations/getagentresponse.md)**
### Errors

| Error Object                           | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GetAgentResponseBody            | 400                                    | application/json                       |
| errors.GetAgentResponseResponseBody    | 401                                    | application/json                       |
| errors.GetAgentResponse422ResponseBody | 422                                    | application/json                       |
| errors.GetAgentResponse500ResponseBody | 500                                    | application/json                       |
| errors.SDKError                        | 400-600                                | */*                                    |

## get_call

Retrieve details of a specific call

### Example Usage

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

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `call_id`                                 | *str*                                     | :heavy_check_mark:                        | The call id to retrieve call history for. | 119c3f8e47135a29e65947eeb34cf12d          |


### Response

**[operations.GetCallResponse](../../models/operations/getcallresponse.md)**
### Errors

| Error Object                          | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.GetCallResponseBody            | 400                                   | application/json                      |
| errors.GetCallResponseResponseBody    | 401                                   | application/json                      |
| errors.GetCallResponse422ResponseBody | 422                                   | application/json                      |
| errors.GetCallResponse500ResponseBody | 500                                   | application/json                      |
| errors.SDKError                       | 400-600                               | */*                                   |

## get_phone_number

Retrieve info about a specific number

### Example Usage

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

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `phone_number`                                             | *str*                                                      | :heavy_check_mark:                                         | Phone number in E.164 format to retreive more information. | +14159095857                                               |


### Response

**[operations.GetPhoneNumberResponse](../../models/operations/getphonenumberresponse.md)**
### Errors

| Error Object                                 | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| errors.GetPhoneNumberResponseBody            | 400                                          | application/json                             |
| errors.GetPhoneNumberResponseResponseBody    | 401                                          | application/json                             |
| errors.GetPhoneNumberResponse422ResponseBody | 422                                          | application/json                             |
| errors.GetPhoneNumberResponse500ResponseBody | 500                                          | application/json                             |
| errors.SDKError                              | 400-600                                      | */*                                          |

## list_agents

List all agents

### Example Usage

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


### Response

**[operations.ListAgentsResponse](../../models/operations/listagentsresponse.md)**
### Errors

| Error Object                          | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.ListAgentsResponseBody         | 401                                   | application/json                      |
| errors.ListAgentsResponseResponseBody | 500                                   | application/json                      |
| errors.SDKError                       | 400-600                               | */*                                   |

## list_calls

Retrieve call details

### Example Usage

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

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `filter_criteria`                                                                                            | [Optional[operations.FilterCriteria]](../../models/operations/filtercriteria.md)                             | :heavy_minus_sign:                                                                                           | N/A                                                                                                          |
| `limit`                                                                                                      | *Optional[int]*                                                                                              | :heavy_minus_sign:                                                                                           | Limit the number of calls returned.                                                                          |
| `sort_order`                                                                                                 | [Optional[operations.SortOrder]](../../models/operations/sortorder.md)                                       | :heavy_minus_sign:                                                                                           | The calls will be sorted by `start_timestamp`, whether to return the calls in ascending or descending order. |


### Response

**[operations.ListCallsResponse](../../models/operations/listcallsresponse.md)**
### Errors

| Error Object                            | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.ListCallsResponseBody            | 400                                     | application/json                        |
| errors.ListCallsResponseResponseBody    | 401                                     | application/json                        |
| errors.ListCallsResponse500ResponseBody | 500                                     | application/json                        |
| errors.SDKError                         | 400-600                                 | */*                                     |

## list_phone_numbers

List all purchased and active phone numbers

### Example Usage

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


### Response

**[operations.ListPhoneNumbersResponse](../../models/operations/listphonenumbersresponse.md)**
### Errors

| Error Object                                   | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| errors.ListPhoneNumbersResponseBody            | 400                                            | application/json                               |
| errors.ListPhoneNumbersResponseResponseBody    | 401                                            | application/json                               |
| errors.ListPhoneNumbersResponse500ResponseBody | 500                                            | application/json                               |
| errors.SDKError                                | 400-600                                        | */*                                            |

## update_agent

Update an existing agent

### Example Usage

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

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `agent_no_default_no_required`                                                             | [components.AgentNoDefaultNoRequired](../../models/components/agentnodefaultnorequired.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |                                                                                            |
| `agent_id`                                                                                 | *str*                                                                                      | :heavy_check_mark:                                                                         | Unique id of the agent to be updated.                                                      | 16b980523634a6dc504898cda492e939                                                           |


### Response

**[operations.UpdateAgentResponse](../../models/operations/updateagentresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.UpdateAgentResponseBody            | 400                                       | application/json                          |
| errors.UpdateAgentResponseResponseBody    | 401                                       | application/json                          |
| errors.UpdateAgentResponse422ResponseBody | 422                                       | application/json                          |
| errors.UpdateAgentResponse500ResponseBody | 500                                       | application/json                          |
| errors.SDKError                           | 400-600                                   | */*                                       |

## update_phone_agent

Update an existing phone number

### Example Usage

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

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request_body`                                                                                   | [operations.UpdatePhoneAgentRequestBody](../../models/operations/updatephoneagentrequestbody.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |                                                                                                  |
| `phone_number`                                                                                   | *str*                                                                                            | :heavy_check_mark:                                                                               | Phone number in E.164 format that require agent update.                                          | +14159095857                                                                                     |


### Response

**[operations.UpdatePhoneAgentResponse](../../models/operations/updatephoneagentresponse.md)**
### Errors

| Error Object                                   | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| errors.UpdatePhoneAgentResponseBody            | 400                                            | application/json                               |
| errors.UpdatePhoneAgentResponseResponseBody    | 401                                            | application/json                               |
| errors.UpdatePhoneAgentResponse422ResponseBody | 422                                            | application/json                               |
| errors.UpdatePhoneAgentResponse500ResponseBody | 500                                            | application/json                               |
| errors.SDKError                                | 400-600                                        | */*                                            |
