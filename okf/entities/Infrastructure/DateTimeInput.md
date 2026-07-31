---
type: API Type
title: DateTimeInput
description: Represents a nullable date/time input for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.DateTimeInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.DateTimeInput.html
  title: Monitor API — DateTimeInput
module: Infrastructure
api_class: DateTimeInput
doc_name: DateTimeInput
introduced_in: '2.18'
property_count: 1
---

# DateTimeInput

Represents a nullable date/time input for update commands.

- **Module:** [Infrastructure](/modules/Infrastructure.md)
- **API class:** `DateTimeInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `DateTimeOffset?` | yes |  |  | The nullable date/time value to update the property with. |

## Example

```json
{
  "Value": null
}
```
