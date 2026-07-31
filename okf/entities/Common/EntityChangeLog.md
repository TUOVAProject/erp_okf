---
type: API Entity
title: EntityChangeLogs
description: Represents a queryable entity changelog entry.
resource: https://api.monitor.se/api/Monitor.API.Common.EntityChangeLog.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.EntityChangeLog.html
  title: Monitor API — EntityChangeLog
module: Common
api_class: EntityChangeLog
doc_name: EntityChangeLogs
endpoint: GET /api/v1/Common/EntityChangeLogs
guid: 408514C1-E8D8-47BB-9368-AE82AB2D9FB0
permission: Show changelog
introduced_in: '2.33'
property_count: 11
references_out:
- /entities/Common/EntityPropertyChange.md
---

# EntityChangeLogs

Represents a queryable entity changelog entry.

- **Module:** [Common](/modules/Common.md)
- **API class:** `EntityChangeLog`
- **Endpoint:** `GET /api/v1/Common/EntityChangeLogs`
- **Required permission:** Show changelog
- **GUID:** `408514C1-E8D8-47BB-9368-AE82AB2D9FB0`
- **Introduced in:** 2.33

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the changelog entry. |
| `ChangeType` | `Int32` | no |  | enum | The type of change that was made to the entity. |
| `EntityTypeId` | `Guid` | no |  |  | The GUID of the changed entity's type. |
| `EntityId` | `Int64` | no |  |  | The business key identifier of the changed entity. |
| `ModifiedBy` | `String` | no |  | max length 20 | The human readable identifier of the application user that performed the change. |
| `ModifiedTimestamp` | `DateTimeOffset` | no |  |  | The date when the change was made. |
| `AssociatedTypeId` | `Guid?` | yes |  |  | The GUID of the changed entity's parent type. |
| `AssociatedEntityId` | `Int64?` | yes |  |  | The business key identifier of the changed entity's parent. |
| `EntityCode` | `String` | no |  | max length 255 | The human readable identifier of the changed entity. |
| `Changes` | `EntityPropertyChanges[]` | no | [EntityPropertyChanges](/entities/Common/EntityPropertyChange.md) | collection | The property changes for this entity. |
| `Remark` | `String` | no |  | max length 100 | Holds extra information about the change. |

## Enumerations

### ChangeType

| Name | Value |
| --- | ---: |
| `Update` | 0 |
| `Create` | 1 |
| `Delete` | 2 |


## Example

```json
{
  "Id": 0,
  "ChangeType": 0,
  "EntityTypeId": "00000000-0000-0000-0000-000000000000",
  "EntityId": 0,
  "ModifiedBy": null,
  "ModifiedTimestamp": "0001-01-01T00:00:00+00:00",
  "AssociatedTypeId": null,
  "AssociatedEntityId": null,
  "EntityCode": null,
  "Changes": null,
  "Remark": null
}
```
