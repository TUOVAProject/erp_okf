---
type: API Type
title: EntityCommandResponse
description: This is the response type of all state commands available in the system.
  As long as a command uses this return-type, it can be used with the command batching
  system.
resource: https://api.monitor.se/api/Monitor.API.Infrastructure.EntityCommandResponse.html
tags:
- Infrastructure
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Infrastructure.EntityCommandResponse.html
  title: Monitor API — EntityCommandResponse
module: Infrastructure
api_class: EntityCommandResponse
doc_name: EntityCommandResponse
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Infrastructure/BatchResponse.md
---

# EntityCommandResponse

This is the response type of all state commands available in the system. As long as a command uses this return-type, it can be used with the command batching system.

- **Module:** [Infrastructure](../../modules/Infrastructure.md)
- **API class:** `EntityCommandResponse`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `RootEntityId` | `Int64` | no |  |  | The business key identifier of the root entity in the context of the command. This is usually the parent entity of the parent that has been changed. |
| `EntityId` | `Int64` | no |  |  | The business key identifier of the main entity in the context of the command. This is always the entity that has been changed by the command. |
| `CommandName` | `String` | no |  |  | The name of the command that was invoked. |
| `Data` | `String` | no |  |  | Extended return-data of the command encoded as JSON. |

## Referenced by

**Infrastructure**

- [BatchResponse](BatchResponse.md) — `Response` (expand)


## Example

```json
{
  "RootEntityId": 0,
  "EntityId": 0,
  "CommandName": null,
  "Data": null
}
```
