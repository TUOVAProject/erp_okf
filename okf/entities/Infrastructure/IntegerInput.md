---
type: API Type
title: IntegerInput
description: Represents a nullable 32-bit integer input for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.IntegerInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.IntegerInput.html
  title: Monitor API — IntegerInput
module: Infrastructure
api_class: IntegerInput
doc_name: IntegerInput
introduced_in: '2.18'
property_count: 1
---

# IntegerInput

Represents a nullable 32-bit integer input for update commands.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `IntegerInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `Int32?` | yes |  |  | The nullable 32-bit integer value to update the property with. |

## Example

```json
{
  "Value": null
}
```
