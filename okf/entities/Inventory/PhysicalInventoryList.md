---
type: API Entity
title: PhysicalInventoryLists
description: Represents a physical inventory list.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PhysicalInventoryList.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PhysicalInventoryList.html
  title: Monitor API — PhysicalInventoryList
module: Inventory
api_class: PhysicalInventoryList
doc_name: PhysicalInventoryLists
endpoint: GET /api/v1/Inventory/PhysicalInventoryLists
guid: 1ED2E7D1-7FAA-4E90-8523-8EE895680119
permission: Report stock count
introduced_in: '22.8'
property_count: 9
references_out:
- /entities/Common/Warehouse.md
referenced_by:
- /entities/Inventory/PhysicalInventoryRow.md
---

# PhysicalInventoryLists

Represents a physical inventory list.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PhysicalInventoryList`
- **Endpoint:** `GET /api/v1/Inventory/PhysicalInventoryLists`
- **Required permission:** Report stock count
- **GUID:** `1ED2E7D1-7FAA-4E90-8523-8EE895680119`
- **Introduced in:** 22.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the physical inventory list. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse for the physical inventory list. |
| `Number` | `Int64` | no |  | unique | The number of the physical inventory list. |
| `Version` | `Int32` | no |  |  | The version of the physical inventory list. |
| `Name` | `String` | no |  | max length 50 | The name of the physical inventory list. |
| `InventoryStatus` | `Int32` | no |  | enum | The status for the physical inventory list. |
| `State` | `Int32` | no |  | enum | The state for the physical inventory list. |
| `CreatedWhen` | `DateTimeOffset` | no |  |  | The date when the physical inventory list was created. |
| `PrintedWhen` | `DateTimeOffset?` | yes |  |  | The date when the physical inventory list was printed. |

## Enumerations

### InventoryStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `UnderInventory` | 1 |
| `UnderInventoryWithBalanceCheckpoint` | 2 |

### State

| Name | Value |
| --- | ---: |
| `NotStarted` | 0 |
| `Started` | 1 |
| `Paused` | 2 |
| `Finished` | 3 |
| `FinishedWithPendingApproval` | 4 |


## Referenced by

**Inventory**

- [PhysicalInventoryRows](PhysicalInventoryRow.md) — `PhysicalInventoryListId` (FK)


## Example

```json
{
  "Id": 0,
  "WarehouseId": 0,
  "Number": 0,
  "Version": 0,
  "Name": null,
  "InventoryStatus": 0,
  "State": 0,
  "CreatedWhen": "0001-01-01T00:00:00+00:00",
  "PrintedWhen": null
}
```
