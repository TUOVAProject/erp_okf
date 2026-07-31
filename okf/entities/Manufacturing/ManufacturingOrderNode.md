---
type: API Entity
title: ManufacturingOrderNodes
description: Represents a manufacturing order node.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderNode.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderNode.html
  title: Monitor API — ManufacturingOrderNode
module: Manufacturing
api_class: ManufacturingOrderNode
doc_name: ManufacturingOrderNodes
endpoint: GET /api/v1/Manufacturing/ManufacturingOrderNodes
guid: CFFE1A38-0B7F-498B-9B9B-E5FEA2BB2E75
permission: Show manufacturing orders
introduced_in: '2.30'
property_count: 18
references_out:
- /entities/Common/Revision.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Inventory/ProductRecord.md
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Manufacturing/ManufacturingOrderNodeDrawing.md
referenced_by:
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Manufacturing/ManufacturingOrderMaterial.md
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Manufacturing/ManufacturingOrderNodeDrawing.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
---

# ManufacturingOrderNodes

Represents a manufacturing order node.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `ManufacturingOrderNode`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderNodes`
- **Required permission:** Show manufacturing orders
- **GUID:** `CFFE1A38-0B7F-498B-9B9B-E5FEA2BB2E75`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the manufacturing order node. |
| `IsMainNode` | `Boolean` | no |  |  | Specifies if the node is the main node on manufacturing order. Only one of the root nodes on order can be the main node. |
| `IsRootNode` | `Boolean` | no |  |  | Specifies if the node is a root node on manufacturing order. It can be several root nodes. For example when splitting from max quantity or when coordinated parts exists. Only one of the root nodes on order can be the main node. |
| `Level` | `Int32` | no |  |  | Level in the node hierarchy |
| `Number` | `Int32` | no |  |  | Node number, a sequence number in exploding sort order. |
| `PartId` | `Int64` | no | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the part that the manufacturing order node is to produce. |
| `ReportedQuantity` | `Decimal` | no |  |  | The reported quantity. |
| `PlannedQuantity` | `Decimal` | no |  |  | The planned quantity. |
| `RestQuantity` | `Decimal` | no |  |  | The rest quantity. |
| `StartDate` | `DateTimeOffset` | no |  |  | The start date of the manufacturing order node. |
| `EndDate` | `DateTimeOffset` | no |  |  | The finish date of the manufacturing order node. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse that the node belongs to. |
| `Status` | `Int32` | no |  | enum | The status of the manufacturing order node. |
| `ManufacturingOrderNodeId` | `Int64?` | yes | [ManufacturingOrderNodes](/entities/Manufacturing/ManufacturingOrderNode.md) |  | The business key identifier of the manufacturing order node that the manufacturing order node belongs to. If id is null, it's a root node. |
| `Drawings` | `ManufacturingOrderNodeDrawings[]` | no | [ManufacturingOrderNodeDrawings](/entities/Manufacturing/ManufacturingOrderNodeDrawing.md) | expandable, collection, since 24.2 | A collection of drawings that belong to the manufacturing order node. |
| `RevisionId` | `Int64?` | yes | [Revisions](/entities/Common/Revision.md) | since 24.2 | The business key identifier of the revision that the manufacturing order node has. |
| `Revision` | `Revisions` | no | [Revisions](/entities/Common/Revision.md) | expandable, since 24.2 | The revision that the manufacturing order node has. |
| `SerialNumberProductRecords` | `ProductRecords[]` | no | [ProductRecords](/entities/Inventory/ProductRecord.md) | expandable, collection, since 25.2 | A collection of product records with serial number traceability that belong to the manufacturing order node. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `Registrered` | 1 |
| `Printed` | 2 |
| `Started` | 3 |
| `Finished` | 4 |
| `PostCalculated` | 5 |
| `Delivered` | 6 |
| `Historical` | 9 |


## Referenced by

**Manufacturing**

- [ManufacturingOrderMaterials](/entities/Manufacturing/ManufacturingOrderMaterial.md) — `ManufacturingOrderNodeId` (FK)
- [ManufacturingOrderNodeDrawings](/entities/Manufacturing/ManufacturingOrderNodeDrawing.md) — `ManufacturingOrderNodeId` (FK)
- [ManufacturingOrderNodes](/entities/Manufacturing/ManufacturingOrderNode.md) — `ManufacturingOrderNodeId` (FK)
- [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) — `ManufacturingOrderNodeId` (FK)
- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `Nodes` (expand)


## Example

```json
{
  "Id": 0,
  "IsMainNode": false,
  "IsRootNode": false,
  "Level": 0,
  "Number": 0,
  "PartId": 0,
  "ReportedQuantity": 0.0,
  "PlannedQuantity": 0.0,
  "RestQuantity": 0.0,
  "StartDate": "0001-01-01T00:00:00+00:00",
  "EndDate": "0001-01-01T00:00:00+00:00",
  "WarehouseId": 0,
  "Status": 0,
  "ManufacturingOrderNodeId": null,
  "Drawings": null,
  "RevisionId": null,
  "Revision": null,
  "SerialNumberProductRecords": null
}
```
