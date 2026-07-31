---
type: API Type
title: NotNullDateTimeInput
description: Represents a date/time value for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.NotNullDateTimeInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.NotNullDateTimeInput.html
  title: Monitor API — NotNullDateTimeInput
module: Infrastructure
api_class: NotNullDateTimeInput
doc_name: NotNullDateTimeInput
introduced_in: '2.18'
property_count: 1
---

# NotNullDateTimeInput

Represents a date/time value for update commands.

- **Module:** [Infrastructure](/modules/Infrastructure.md)
- **API class:** `NotNullDateTimeInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `DateTimeOffset` | no |  |  | The date/time value to update the property with. |

## Example

```json
{
  "Value": "0001-01-01T00:00:00+00:00"
}
```
