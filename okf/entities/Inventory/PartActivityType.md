---
type: API Entity
title: PartActivityTypes
description: Represents an part activity type.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartActivityType.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartActivityType.html
  title: Monitor API — PartActivityType
module: Inventory
api_class: PartActivityType
doc_name: PartActivityTypes
endpoint: GET /api/v1/Inventory/PartActivityTypes
guid: 355FF5E8-D570-4D73-BEEE-753E1FF0B080
permission: Show basic data for part
introduced_in: '22.7'
property_count: 3
referenced_by:
- /entities/Inventory/PartActivity.md
---

# PartActivityTypes

Represents an part activity type.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PartActivityType`
- **Endpoint:** `GET /api/v1/Inventory/PartActivityTypes`
- **Required permission:** Show basic data for part
- **GUID:** `355FF5E8-D570-4D73-BEEE-753E1FF0B080`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part activity type. |
| `Code` | `Int64` | no |  | unique | he human readable identifier of the activity type. |
| `Description` | `String` | no |  | max length 80 | The description of the activity type. |

## Referenced by

**Inventory**

- [PartActivities](PartActivity.md) — `ActivityTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null
}
```
