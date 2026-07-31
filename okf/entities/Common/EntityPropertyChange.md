---
type: API Entity
title: EntityPropertyChanges
description: Represents a queryable entity property change entry.
resource: https://api.monitor.se/api/Monitor.API.Common.EntityPropertyChange.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.EntityPropertyChange.html
  title: Monitor API — EntityPropertyChange
module: Common
api_class: EntityPropertyChange
doc_name: EntityPropertyChanges
endpoint: GET /api/v1/Common/EntityPropertyChanges
guid: 0C275F3C-EF86-443D-A8D9-C32CC108DB85
permission: Show changelog
introduced_in: '2.33'
property_count: 6
referenced_by:
- /entities/Common/EntityChangeLog.md
---

# EntityPropertyChanges

Represents a queryable entity property change entry.

- **Module:** [Common](/modules/Common.md)
- **API class:** `EntityPropertyChange`
- **Endpoint:** `GET /api/v1/Common/EntityPropertyChanges`
- **Required permission:** Show changelog
- **GUID:** `0C275F3C-EF86-443D-A8D9-C32CC108DB85`
- **Introduced in:** 2.33

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the property change entry. |
| `MemberName` | `String` | no |  | max length 256 | The path to the property where the change occured. |
| `OldValue` | `String` | no |  | max length 256 | The value of the property before the change. |
| `NewValue` | `String` | no |  | max length 256 | The value of the property after the change. |
| `ChangeType` | `Int32` | no |  | enum | The type of change that was made to the property. |
| `EntityChangeLogId` | `Int64` | no |  | since 22.3 | The business key identifier of the property's change log |

## Enumerations

### ChangeType

| Name | Value |
| --- | ---: |
| `Update` | 0 |
| `Create` | 1 |
| `Delete` | 2 |


## Referenced by

**Common**

- [EntityChangeLogs](/entities/Common/EntityChangeLog.md) — `Changes` (expand)


## Example

```json
{
  "Id": 0,
  "MemberName": null,
  "OldValue": null,
  "NewValue": null,
  "ChangeType": 0,
  "EntityChangeLogId": 0
}
```
