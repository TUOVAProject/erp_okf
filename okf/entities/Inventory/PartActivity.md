---
type: API Entity
title: PartActivities
description: Represents an part activity.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartActivity.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartActivity.html
  title: Monitor API — PartActivity
module: Inventory
api_class: PartActivity
doc_name: PartActivities
endpoint: GET /api/v1/Inventory/PartActivities
guid: 020CE79F-716A-4879-93BA-0D26F1D3D88A
permission: Show part
introduced_in: '22.7'
property_count: 9
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartActivityType.md
referenced_by:
- /entities/Inventory/Part.md
---

# PartActivities

Represents an part activity.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PartActivity`
- **Endpoint:** `GET /api/v1/Inventory/PartActivities`
- **Required permission:** Show part
- **GUID:** `020CE79F-716A-4879-93BA-0D26F1D3D88A`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part activity. |
| `PartId` | `Int64` | no | [Parts](Part.md) |  | The business key identifier of the part that the activity belongs to. |
| `ActivityTypeId` | `Int64` | no | [PartActivityTypes](PartActivityType.md) |  | The business key identifier of the part activity type. |
| `Description` | `String` | no |  |  | The description of the activity. |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the user that is responsible for the activity. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the activity's comment. |
| `ReminderId` | `Int64` | no |  |  | The business key identifier of the reminder that is linked with the activity. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |  | The planned completion date of the activity. |
| `Status` | `Int32` | no |  | enum | The status of the the activity. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `InProgress` | 2 |
| `History` | 9 |


## Referenced by

**Inventory**

- [Parts](Part.md) — `PartActivities` (expand)


## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "ActivityTypeId": 0,
  "Description": null,
  "ResponsibleUserId": 0,
  "CommentId": null,
  "ReminderId": 0,
  "PlannedCompletionDate": "0001-01-01T00:00:00+00:00",
  "Status": 0
}
```
