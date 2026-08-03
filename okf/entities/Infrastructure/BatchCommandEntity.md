---
type: API Type
title: BatchCommandEntity
description: A batch command entity is used to create command batches, allowing transactional
  continuity across multiple commands.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.BatchCommandEntity.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.BatchCommandEntity.html
  title: Monitor API — BatchCommandEntity
module: Infrastructure
api_class: BatchCommandEntity
doc_name: BatchCommandEntity
introduced_in: '2.18'
property_count: 4
---

# BatchCommandEntity

A batch command entity is used to create command batches, allowing transactional continuity across multiple commands.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `BatchCommandEntity`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Notes

- Property forwarding does not work for commands issued for a /Many path.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Path` | `String` | no |  |  | The API-local URL to the command that should be invoked. For example /Common/Commands/CreateComment . |
| `Body` | `Object` | no |  |  | The JSON-encoded instance of the command that should be invoked. |
| `ForwardPropertyName` | `String` | no |  |  | The name of the property to forward from the response of the command to the next command in the batch. |
| `ReceivingPropertyName` | `String` | no |  |  | The name of the property that should receive the forwarded property from the previous command in the batch. |

## Example

```json
{
  "Path": null,
  "Body": null,
  "ForwardPropertyName": null,
  "ReceivingPropertyName": null
}
```
