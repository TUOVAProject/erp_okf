---
type: API Type
title: ApiValidationResult
description: Specifies a command validation result.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.ApiValidationResult.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.ApiValidationResult.html
  title: Monitor API — ApiValidationResult
module: Infrastructure
api_class: ApiValidationResult
doc_name: ApiValidationResult
introduced_in: '2.18'
property_count: 2
referenced_by:
- /entities/Infrastructure/ValidationCommandResponse.md
---

# ApiValidationResult

Specifies a command validation result.

- **Module:** [Infrastructure](/modules/Infrastructure.md)
- **API class:** `ApiValidationResult`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- Used by the ValidationCommandResponse type.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Kind` | `Int32` | no |  | enum | The validation kind of the result. |
| `Message` | `String` | no |  |  | The message returned by the validation. |

## Enumerations

### Kind

| Name | Value |
| --- | ---: |
| `Valid` | 0 |
| `Warning` | 1 |
| `Error` | 2 |


## Referenced by

**Infrastructure**

- [ValidationCommandResponse](/entities/Infrastructure/ValidationCommandResponse.md) — `Results` (expand)


## Example

```json
{
  "Kind": 0,
  "Message": null
}
```
