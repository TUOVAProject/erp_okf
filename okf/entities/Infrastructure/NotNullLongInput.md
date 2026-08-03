---
type: API Type
title: NotNullLongInput
description: Represents a 64-bit integer input for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.NotNullLongInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.NotNullLongInput.html
  title: Monitor API — NotNullLongInput
module: Infrastructure
api_class: NotNullLongInput
doc_name: NotNullLongInput
introduced_in: '2.18'
property_count: 1
---

# NotNullLongInput

Represents a 64-bit integer input for update commands.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `NotNullLongInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `Int64` | no |  |  | The 64-bit integer value to update the property with. |

## Example

```json
{
  "Value": 0
}
```
