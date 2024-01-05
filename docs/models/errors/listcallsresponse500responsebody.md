# ListCallsResponse500ResponseBody

Internal Server Error


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | Raw HTTP response; suitable for custom response parsing                               |                                                                                       |
| `error_message`                                                                       | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   | An unexpected server error occurred.                                                  |