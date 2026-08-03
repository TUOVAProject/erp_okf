---
type: API Type
title: NotNullDecimalInput
description: Represents a decimal input for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.NotNullDecimalInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.NotNullDecimalInput.html
  title: Monitor API — NotNullDecimalInput
module: Infrastructure
api_class: NotNullDecimalInput
doc_name: NotNullDecimalInput
introduced_in: '2.18'
property_count: 1
---

# NotNullDecimalInput

Represents a decimal input for update commands.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `NotNullDecimalInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `Decimal` | no |  |  | The decimal value to update the property with. |

## Example

```json
{
  "Value": 0.0
}
```
