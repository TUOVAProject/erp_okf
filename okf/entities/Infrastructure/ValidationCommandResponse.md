---
type: API Type
title: ValidationCommandResponse
description: This is the response type returned when adding /Validate after the command
  path.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.ValidationCommandResponse.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.ValidationCommandResponse.html
  title: Monitor API — ValidationCommandResponse
module: Infrastructure
api_class: ValidationCommandResponse
doc_name: ValidationCommandResponse
introduced_in: '2.18'
property_count: 3
references_out:
- /entities/Infrastructure/ApiValidationResult.md
---

# ValidationCommandResponse

This is the response type returned when adding /Validate after the command path.

- **Module:** [Infrastructure](/modules/Infrastructure.md)
- **API class:** `ValidationCommandResponse`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `IsValid` | `Boolean` | no |  |  | Specifies if the command was validated or not. |
| `ErrorMessage` | `String` | no |  |  | The error message thrown by the command if any. |
| `Results` | `ApiValidationResult[]` | no | [ApiValidationResult](/entities/Infrastructure/ApiValidationResult.md) | collection | The validation results of the command. |

## Example

```json
{
  "IsValid": false,
  "ErrorMessage": null,
  "Results": null
}
```
