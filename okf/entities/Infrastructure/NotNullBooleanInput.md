---
type: API Type
title: NotNullBooleanInput
description: Represents a boolean input for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.NotNullBooleanInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.NotNullBooleanInput.html
  title: Monitor API — NotNullBooleanInput
module: Infrastructure
api_class: NotNullBooleanInput
doc_name: NotNullBooleanInput
introduced_in: '2.18'
property_count: 1
---

# NotNullBooleanInput

Represents a boolean input for update commands.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `NotNullBooleanInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `Boolean` | no |  |  | The boolean value to update the property with. |

## Example

```json
{
  "Value": false
}
```
