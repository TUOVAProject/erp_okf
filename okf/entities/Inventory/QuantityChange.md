---
type: API Entity
title: QuantityChanges
description: Represents a quantity change.
resource: https://api.monitor.se/api/Monitor.API.Inventory.QuantityChange.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.QuantityChange.html
  title: Monitor API — QuantityChange
module: Inventory
api_class: QuantityChange
doc_name: QuantityChanges
endpoint: GET /api/v1/Inventory/QuantityChanges
guid: F2EFE17D-83DA-4250-B95C-C812EA6D2F81
permission: Show part
introduced_in: '2.48'
property_count: 21
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Person.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Inventory/StockBalanceChange.md
referenced_by:
- /entities/Inventory/StockBalanceChange.md
- /entities/Manufacturing/ManufacturingPickingListMaterial.md
- /entities/Purchase/PurchaseOrderDeliveryRowQuantity.md
---

# QuantityChanges

Represents a quantity change.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `QuantityChange`
- **Endpoint:** `GET /api/v1/Inventory/QuantityChanges`
- **Required permission:** Show part
- **GUID:** `F2EFE17D-83DA-4250-B95C-C812EA6D2F81`
- **Introduced in:** 2.48

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the quantity change. |
| `ActualDeliveryDate` | `DateTimeOffset` | no |  |  | The date that the delivery was performed. |
| `PartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The part that the quantity change was made for. |
| `BalanceChange` | `Decimal` | no |  |  | The total balance change. |
| `AvailableBalance` | `Decimal` | no |  |  | The total available balance in the warehouse before the quantity change was performed. Note that this only provides a value for quantity changes that have status "Cleared" and are created in the outgoing delivery planning. This property is not suitable for looking at the historical balance of a part. |
| `PickingByUserId` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The user that performed the picking. |
| `PickingByPersonId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The person that performed the picking. |
| `DeliveredByUserId` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The user that performed the delivery. |
| `DeliveredByPersonId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The person that performed the delivery. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The warehouse where the quantity change was performed. |
| `StockBalanceChanges` | `StockBalanceChanges[]` | no | [StockBalanceChanges](/entities/Inventory/StockBalanceChange.md) | collection | The stock balance changes that belong to the quantity change. |
| `Status` | `Int32` | no |  | enum | This determines which way the quantity change is going. |
| `ClearingTimeStamp` | `DateTimeOffset?` | yes |  |  | The date when clearing was performed. |
| `PickingTimeStamp` | `DateTimeOffset?` | yes |  |  | The date when picking was performed. |
| `IsOriginalReceivingInspectionQuantity` | `Boolean` | no |  |  | Tells if quantity change is original receiving inspection quantity. |
| `Price` | `Decimal?` | yes |  |  | Price of the row when the transaction was made. |
| `CanceledQuantity` | `Decimal` | no |  |  | The quantity that was cancelled. |
| `IsExportedToManagementAccounting` | `Boolean` | no |  |  | Is exported to management accounting |
| `CanceledTimestamp` | `DateTimeOffset?` | yes |  |  | The date when cancel was performed. |
| `UndoneTimestamp` | `DateTimeOffset?` | yes |  |  | The date when undo was performed. |
| `ReservationId` | `Int64?` | yes |  |  | The reservation that is linked to the quantity change. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Cleared` | 1 |
| `Picking` | 2 |
| `OutgoingDelivery` | 3 |
| `Adviced` | 4 |
| `ReceivingInspection` | 5 |
| `IncomingDelivery` | 6 |
| `CanceledOutgoingDelivery` | 7 |
| `CanceledIncomingDelivery` | 8 |
| `WithdrawInspection` | 9 |
| `InspectionCompleted` | 10 |
| `InspectionRejection` | 11 |


## Referenced by

**Inventory**

- [StockBalanceChanges](/entities/Inventory/StockBalanceChange.md) — `QuantityChangeId` (FK)

**Manufacturing**

- [ManufacturingPickingListMaterials](/entities/Manufacturing/ManufacturingPickingListMaterial.md) — `QuantityChange` (expand)
- [ManufacturingPickingListMaterials](/entities/Manufacturing/ManufacturingPickingListMaterial.md) — `QuantityChangeId` (FK)

**Purchase**

- [PurchaseOrderDeliveryRowQuantities](/entities/Purchase/PurchaseOrderDeliveryRowQuantity.md) — `QuantityChange` (expand)
- [PurchaseOrderDeliveryRowQuantities](/entities/Purchase/PurchaseOrderDeliveryRowQuantity.md) — `QuantityChangeId` (FK)


## Example

```json
{
  "Id": 0,
  "ActualDeliveryDate": "0001-01-01T00:00:00+00:00",
  "PartId": null,
  "BalanceChange": 0.0,
  "AvailableBalance": 0.0,
  "PickingByUserId": null,
  "PickingByPersonId": null,
  "DeliveredByUserId": null,
  "DeliveredByPersonId": null,
  "WarehouseId": 0,
  "StockBalanceChanges": null,
  "Status": 0,
  "ClearingTimeStamp": null,
  "PickingTimeStamp": null,
  "IsOriginalReceivingInspectionQuantity": false,
  "Price": null,
  "CanceledQuantity": 0.0,
  "IsExportedToManagementAccounting": false,
  "CanceledTimestamp": null,
  "UndoneTimestamp": null,
  "ReservationId": null
}
```
