---
type: API Entity
title: ManufacturingOrderMaterials
description: Represents a manufacturing order material.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderMaterial.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderMaterial.html
  title: Monitor API — ManufacturingOrderMaterial
module: Manufacturing
api_class: ManufacturingOrderMaterial
doc_name: ManufacturingOrderMaterials
endpoint: GET /api/v1/Manufacturing/ManufacturingOrderMaterials
guid: 34CE9D0E-1927-446E-B5A9-A40E9CC937B6
permission: Show manufacturing orders
introduced_in: '2.18'
property_count: 26
references_out:
- /entities/Common/Comment.md
- /entities/Inventory/Part.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Purchase/PurchaseOrderRow.md
referenced_by:
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Manufacturing/ManufacturingPickingListMaterial.md
---

# ManufacturingOrderMaterials

Represents a manufacturing order material.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `ManufacturingOrderMaterial`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderMaterials`
- **Required permission:** Show manufacturing orders
- **GUID:** `34CE9D0E-1927-446E-B5A9-A40E9CC937B6`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the manufacturing order material. |
| `ReportNumber` | `Int64` | no |  |  | The report number of the manufacturing order material. |
| `RowNumber` | `Int32` | no |  |  | The row number of the manufacturing order material. |
| `PartId` | `Int64` | no | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the manufacturing order material part. |
| `Part` | `Parts` | no | [Parts](/entities/Inventory/Part.md) | expandable | The manufacturing order material part. |
| `ToOperationNumber` | `Int32` | no |  |  | The manufacturing order operation number that the manufacturing order material belongs to. |
| `ReportedQuantity` | `Decimal` | no |  |  | The reported quantity of the manufacturing order material. |
| `RestQuantity` | `Decimal` | no |  |  | The remaining quantity of the manufacturing order material. |
| `PlannedQuantity` | `Decimal` | no |  |  | The planned quantity of the manufacturing order material. |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) |  | The business key identifier of the manufacturing order that the manufacturing order material belongs to. |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](/entities/Manufacturing/ManufacturingOrderNode.md) | since 2.30 | The business key identifier of the manufacturing order node that the manufacturing order material belongs to. |
| `PositionNumber` | `String` | no |  | since 2.49 | The position number of the material. |
| `InstructionCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) | since 2.49 | The business key identifier of the manufacturing order material's instruction comment. |
| `InstructionComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable, since 2.49 | The manufacturing order material's instruction comment. |
| `QuantityPerUnit` | `Decimal` | no |  | since 22.9 | Quantity per unit of the manufacturing order material. |
| `CycleTime` | `TimeSpan?` | yes |  | since 22.9 | Cycle time of the manufacturing order material. |
| `EditedStatus` | `Int32` | no |  | bitmask, enum, since 22.9 | Edited status of the manufacturing order material. |
| `ExtraQuantityProcent` | `Decimal` | no |  | since 22.9 | Extra quantity procent of the manufacturing order material. |
| `LinkedPurchaseOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) | since 22.9 | The business key identifier of the purchase order row that the manufacturing order material belongs to. |
| `LockedToBatchNo` | `String` | no |  | max length 35, since 22.9 | Locked To batch number of the manufacturing order material. |
| `QuantityPerCycle` | `Decimal?` | yes |  | since 22.9 | Quantity per cycle of the manufacturing order material. |
| `RejectedQuantity` | `Decimal` | no |  | since 22.9 | Rejected quantity of the manufacturing order material. |
| `ReportedSetupQuantity` | `Decimal` | no |  | since 22.9 | Reported setup quantity of the manufacturing order material. |
| `RestSetupQuantity` | `Decimal` | no |  | since 22.9 | Rest setup quantity of the manufacturing order material. |
| `SetupQuantity` | `Decimal` | no |  | since 22.9 | Setup quantity of the manufacturing order material. |
| `MaterialRowOriginId` | `Int64?` | yes |  | since 24.4 | Material row origin id of the manufacturing order material. |

## Enumerations

### EditedStatus (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `NotEdited` | 0 |
| `Edited` | 1 |
| `Synchronized` | 2 |


## Referenced by

**Manufacturing**

- [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) — `Materials` (expand)
- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `Materials` (expand)
- [ManufacturingPickingListMaterials](/entities/Manufacturing/ManufacturingPickingListMaterial.md) — `Material` (expand)
- [ManufacturingPickingListMaterials](/entities/Manufacturing/ManufacturingPickingListMaterial.md) — `MaterialId` (FK)


## Example

```json
{
  "Id": 0,
  "ReportNumber": 0,
  "RowNumber": 0,
  "PartId": 0,
  "Part": null,
  "ToOperationNumber": 0,
  "ReportedQuantity": 0.0,
  "RestQuantity": 0.0,
  "PlannedQuantity": 0.0,
  "ManufacturingOrderId": 0,
  "ManufacturingOrderNodeId": 0,
  "PositionNumber": null,
  "InstructionCommentId": null,
  "InstructionComment": null,
  "QuantityPerUnit": 0.0,
  "CycleTime": null,
  "EditedStatus": 0,
  "ExtraQuantityProcent": 0.0,
  "LinkedPurchaseOrderRowId": null,
  "LockedToBatchNo": null,
  "QuantityPerCycle": null,
  "RejectedQuantity": 0.0,
  "ReportedSetupQuantity": 0.0,
  "RestSetupQuantity": 0.0,
  "SetupQuantity": 0.0,
  "MaterialRowOriginId": null
}
```
