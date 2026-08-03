---
type: API Type
title: StringInput
description: Represents a string input for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.StringInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.StringInput.html
  title: Monitor API — StringInput
module: Infrastructure
api_class: StringInput
doc_name: StringInput
introduced_in: '2.18'
property_count: 1
---

# StringInput

Represents a string input for update commands.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `StringInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `String` | no |  |  | The string value to update the property with. |

## Example

```json
{
  "Value": null
}
```
