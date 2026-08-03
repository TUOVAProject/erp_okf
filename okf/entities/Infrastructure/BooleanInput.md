---
type: API Type
title: BooleanInput
description: Represents a nullable boolean input for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.BooleanInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.BooleanInput.html
  title: Monitor API — BooleanInput
module: Infrastructure
api_class: BooleanInput
doc_name: BooleanInput
introduced_in: '2.18'
property_count: 1
---

# BooleanInput

Represents a nullable boolean input for update commands.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `BooleanInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `Boolean?` | yes |  |  | The nullable boolean value to update the property with. |

## Example

```json
{
  "Value": null
}
```
