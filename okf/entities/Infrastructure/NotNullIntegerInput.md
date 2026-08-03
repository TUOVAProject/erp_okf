---
type: API Type
title: NotNullIntegerInput
description: Represents a 32-bit integer input for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.NotNullIntegerInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.NotNullIntegerInput.html
  title: Monitor API — NotNullIntegerInput
module: Infrastructure
api_class: NotNullIntegerInput
doc_name: NotNullIntegerInput
introduced_in: '2.18'
property_count: 1
---

# NotNullIntegerInput

Represents a 32-bit integer input for update commands.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `NotNullIntegerInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `Int32` | no |  |  | The 32-bit integer value to update the property with. |

## Example

```json
{
  "Value": 0
}
```
