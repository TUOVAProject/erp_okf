---
type: API Type
title: ErrorCommandResponse
description: This is the response type returned if an error occurs when invoking a
  command.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.ErrorCommandResponse.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.ErrorCommandResponse.html
  title: Monitor API — ErrorCommandResponse
module: Infrastructure
api_class: ErrorCommandResponse
doc_name: ErrorCommandResponse
introduced_in: '2.18'
property_count: 1
---

# ErrorCommandResponse

This is the response type returned if an error occurs when invoking a command.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `ErrorCommandResponse`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `ErrorMessage` | `String` | no |  |  | The message of the error that caused the command to fail. |

## Example

```json
{
  "ErrorMessage": null
}
```
