---
type: API Type
title: DecimalInput
description: Represents a nullable decimal input for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.DecimalInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.DecimalInput.html
  title: Monitor API — DecimalInput
module: Infrastructure
api_class: DecimalInput
doc_name: DecimalInput
introduced_in: '2.18'
property_count: 1
---

# DecimalInput

Represents a nullable decimal input for update commands.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `DecimalInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `Decimal?` | yes |  |  | The nullable decimal value to update the property with. |

## Example

```json
{
  "Value": null
}
```
