---
type: API Type
title: LongInput
description: Represents a nullable 64-bit integer input for update commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.LongInput.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.LongInput.html
  title: Monitor API — LongInput
module: Infrastructure
api_class: LongInput
doc_name: LongInput
introduced_in: '2.18'
property_count: 1
---

# LongInput

Represents a nullable 64-bit integer input for update commands.

- **Module:** [Infrastructure](/modules/Infrastructure.md)
- **API class:** `LongInput`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- See Input types for more information.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Value` | `Int64?` | yes |  |  | The nullable 64-bit integer value to update the property with. |

## Example

```json
{
  "Value": null
}
```
