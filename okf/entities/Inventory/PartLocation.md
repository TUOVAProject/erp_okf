---
type: API Entity
title: PartLocations
description: Represents a part location.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartLocation.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartLocation.html
  title: Monitor API — PartLocation
module: Inventory
api_class: PartLocation
doc_name: PartLocations
endpoint: GET /api/v1/Inventory/PartLocations
guid: B24A64DD-4E57-4FD3-B8EA-B2206EF2E67A
permission: Show part
introduced_in: '2.28'
property_count: 22
references_out:
- /entities/Common/Revision.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartLocationProductRecord.md
referenced_by:
- /entities/Inventory/Part.md
- /entities/Inventory/PartLocationProductRecord.md
- /entities/Inventory/PhysicalInventoryRow.md
- /entities/Inventory/StockBalanceChange.md
- /entities/Inventory/StockTransaction.md
- /entities/Sales/PackageRowPartLocation.md
- /entities/Sales/SalesPickingListRowQuantity.md
- /entities/Sales/WithdrawalInformationLocation.md
---

# PartLocations

Represents a part location.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PartLocation`
- **Endpoint:** `GET /api/v1/Inventory/PartLocations`
- **Required permission:** Show part
- **GUID:** `B24A64DD-4E57-4FD3-B8EA-B2206EF2E67A`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the location. |
| `PartId` | `Int64` | no | [Parts](Part.md) |  | The business key identifier of the part to which the location belong. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse where the location is located. |
| `Warehouse` | `Warehouses` | no | [Warehouses](../Common/Warehouse.md) | expandable | The warehouse of the location. |
| `Name` | `String` | no |  | max length 35 | The name of the location. |
| `Balance` | `Decimal` | no |  |  | The balance in standard unit. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the location. |
| `LatestArrivalDate` | `DateTimeOffset` | no |  |  | Latest arrival date for the location. |
| `WorkCenterPickingLocation` | `Boolean` | no |  |  | Whether the location is a work center picking location. |
| `WorkCenterPickingLocationFillingQuantity` | `Decimal` | no |  |  | Specifies the filling quantity when the location is a work center picking location. |
| `OutgoingPickLocation` | `Boolean` | no |  |  | Specifies whether the location is of type pick location. |
| `ArrivalLocation` | `Boolean` | no |  |  | Specifies whether the location is of type arrival location. |
| `Priority` | `Int32?` | yes |  |  | Specifies the priority of the location. |
| `OutgoingPickLocationReorderPoint` | `Decimal` | no |  |  | Specifies the pick location reordering point, quantity used when filling pick location. |
| `BatchNumber` | `String` | no |  |  | Batch number when part has traceability of type batch. |
| `SerialNumber` | `String` | no |  |  | Serial number when part has traceability of type serial number. |
| `InventoryStatus` | `Int32` | no |  | enum | The inventory status of the location. |
| `IsOngoingRefill` | `Boolean` | no |  |  | Specifies if the location is currently being refilled. |
| `RevisionId` | `Int64?` | yes | [Revisions](../Common/Revision.md) |  | The business key identifier of the revision of the location. |
| `Revision` | `Revisions` | no | [Revisions](../Common/Revision.md) | expandable | The revision of the location. |
| `IgnoredBalance` | `Boolean` | no |  |  | Specifies if the balance of the location is to be ignored when calculating Net Requirement and CDT. |
| `PartLocationProductRecords` | `PartLocationProductRecords[]` | no | [PartLocationProductRecords](PartLocationProductRecord.md) | expandable, collection, since 2.29 | A collection of quantity items that holds the quantity of each batch/serial number. |

## Enumerations

### LifeCycleState

| Name | Value |
| --- | ---: |
| `Transient` | 1 |
| `Persistent` | 10 |
| `History` | 20 |
| `RemovableCandidate` | 99 |

### InventoryStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `UnderInventory` | 1 |
| `UnderInventoryWithBalanceCheckpoint` | 2 |


## Referenced by

**Inventory**

- [PartLocationProductRecords](PartLocationProductRecord.md) — `PartLocationId` (FK)
- [Parts](Part.md) — `PartLocations` (expand)
- [PhysicalInventoryRows](PhysicalInventoryRow.md) — `LocationId` (FK)
- [StockBalanceChanges](StockBalanceChange.md) — `PartLocationId` (FK)
- [StockTransactions](StockTransaction.md) — `PartLocationId` (FK)

**Sales**

- [PackageRowPartLocations](../Sales/PackageRowPartLocation.md) — `PartLocationId` (FK)
- [SalesPickingListRowQuantities](../Sales/SalesPickingListRowQuantity.md) — `PartLocationId` (FK)
- [WithdrawalInformationLocation](../Sales/WithdrawalInformationLocation.md) — `PartLocationId` (FK)
- [WithdrawalInformationLocation](../Sales/WithdrawalInformationLocation.md) — `ProductRecordId` (FK)


## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "WarehouseId": 0,
  "Warehouse": null,
  "Name": null,
  "Balance": 0.0,
  "LifeCycleState": 0,
  "LatestArrivalDate": "0001-01-01T00:00:00+00:00",
  "WorkCenterPickingLocation": false,
  "WorkCenterPickingLocationFillingQuantity": 0.0,
  "OutgoingPickLocation": false,
  "ArrivalLocation": false,
  "Priority": null,
  "OutgoingPickLocationReorderPoint": 0.0,
  "BatchNumber": null,
  "SerialNumber": null,
  "InventoryStatus": 0,
  "IsOngoingRefill": false,
  "RevisionId": null,
  "Revision": null,
  "IgnoredBalance": false,
  "PartLocationProductRecords": null
}
```
