---
type: API Type
title: BatchResponse
description: The response object used by the batching system to return the complete
  result of an entire batch of commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.BatchResponse.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.BatchResponse.html
  title: Monitor API — BatchResponse
module: Infrastructure
api_class: BatchResponse
doc_name: BatchResponse
introduced_in: '2.18'
property_count: 4
references_out:
- /entities/Infrastructure/EntityCommandResponse.md
---

# BatchResponse

The response object used by the batching system to return the complete result of an entire batch of commands.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `BatchResponse`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `IsSuccessful` | `Boolean` | no |  |  | Specifies if the batch was successfully committed or not. |
| `Response` | `EntityCommandResponse[]` | no | [EntityCommandResponse](EntityCommandResponse.md) | collection | The individual commmand responses in the batch. When the batch command includes commands that uses the /Many tag the responses are flattened out. You still get one result per individual command, but to be able to match the responses, the batch command also needs to be flattened out. |
| `FailingIndex` | `Int32?` | yes |  |  | The index of the failing command in the batch. |
| `ErrorMessage` | `String` | no |  |  | The error message of the failure that caused the batch to be rolled back. |

## Example

```json
{
  "IsSuccessful": false,
  "Response": null,
  "FailingIndex": null,
  "ErrorMessage": null
}
```
