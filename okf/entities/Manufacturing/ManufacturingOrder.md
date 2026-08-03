---
type: API Entity
title: ManufacturingOrders
description: Represents a manufacturing order.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrder.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrder.html
  title: Monitor API — ManufacturingOrder
module: Manufacturing
api_class: ManufacturingOrder
doc_name: ManufacturingOrders
endpoint: GET /api/v1/Manufacturing/ManufacturingOrders
guid: 68181D89-48D6-4A70-949B-3EACE0A00B70
permission: Show manufacturing orders
introduced_in: '2.18'
property_count: 30
references_out:
- /entities/Common/Comment.md
- /entities/Common/PartConfiguration.md
- /entities/Common/Project.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Manufacturing/ManufacturingOrderMaterial.md
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Manufacturing/ManufacturingOrderType.md
- /entities/Manufacturing/OrderQuantityManufacturingOrder.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
referenced_by:
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/Location.md
- /entities/Inventory/ProductRecord.md
- /entities/Manufacturing/MaintenanceReporting.md
- /entities/Manufacturing/ManufacturingOrderMaterial.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Sales/CustomerOrderRow.md
---

# ManufacturingOrders

Represents a manufacturing order.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `ManufacturingOrder`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrders`
- **Required permission:** Show manufacturing orders
- **GUID:** `68181D89-48D6-4A70-949B-3EACE0A00B70`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the manufacturing order. |
| `OrderNumber` | `String` | no |  | unique, max length 20 | The order number of the manufacturing order. |
| `Status` | `Int32` | no |  | enum | The status of the manufacturing order. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse that the manufacturing order belongs to. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the comment that belongs to the manufacturing order. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The comment that belongs to the manufacturing order. |
| `PartId` | `Int64` | no | [Parts](../Inventory/Part.md) |  | The business key identifier of the part that the manufacturing order is to produce. |
| `Part` | `Parts` | no | [Parts](../Inventory/Part.md) | expandable | The part that the manufacturing order is to produce. |
| `ReportedQuantity` | `Decimal` | no |  |  | The reported quantity of the main manufacturing order node. |
| `PlannedQuantity` | `Decimal` | no |  |  | The planned quantity of the main manufacturing order node. |
| `RestQuantity` | `Decimal` | no |  |  | The rest quantity of the main manufacturing order node. |
| `StartDate` | `DateTimeOffset` | no |  |  | The start date of the manufacturing order. |
| `FinishDate` | `DateTimeOffset` | no |  |  | The finish date of the manufacturing order. |
| `Priority` | `Int32` | no |  |  | The priority of the manufacturing order. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](../Sales/CustomerOrder.md) |  | The business key identifier of the customer order that produced the manufacturing order. |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](../Sales/CustomerOrder.md) | expandable | The customer order that produced the manufacturing order. |
| `Operations` | `ManufacturingOrderOperations[]` | no | [ManufacturingOrderOperations](ManufacturingOrderOperation.md) | expandable, collection | The manufacturing order operations that belong to the manufacturing order. |
| `Materials` | `ManufacturingOrderMaterials[]` | no | [ManufacturingOrderMaterials](ManufacturingOrderMaterial.md) | expandable, collection | The manufacturing order materials that belong to the manufacturing order. |
| `Nodes` | `ManufacturingOrderNodes[]` | no | [ManufacturingOrderNodes](ManufacturingOrderNode.md) | expandable, collection, since 2.30 | The manufacturing order nodes that belong to the manufacturing order. It is flattened, not a structure. |
| `ProjectId` | `Int64?` | yes | [Projects](../Common/Project.md) | since 2.31 | The business key identifier of the project that belongs to the manufacturing order. |
| `Project` | `Projects` | no | [Projects](../Common/Project.md) | expandable, since 2.31 | The project that belongs to the manufacturing order. Can be null. |
| `CategoryString` | `String` | no |  | max length 15, since 2.41 | The category string of the manufacturing order. |
| `VariantCode` | `String` | no |  | max length 200, since 2.53 | The variant code on the manufacturing order. |
| `CustomerId` | `Int64?` | yes | [Customers](../Sales/Customer.md) | since 2.53 | The business key identifier of the customer on the manufacturing order. |
| `InitialFinishDate` | `DateTimeOffset` | no |  | since 2.53 | The initial finish date for the manufacturing order. |
| `PartConfigurationId` | `Int64?` | yes | [PartConfigurations](../Common/PartConfiguration.md) | since 2.55 | The business key identifier of the manufacturing order's part configuration. |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityManufacturingOrders](OrderQuantityManufacturingOrder.md) | since 22.6 | The business key identifier of order quantity. |
| `OrderQuantity` | `OrderQuantityManufacturingOrders` | no | [OrderQuantityManufacturingOrders](OrderQuantityManufacturingOrder.md) | expandable, since 22.6 | Order quantity that holds the partial quantities. |
| `OrderTypeId` | `Int64?` | yes | [ManufacturingOrderTypes](ManufacturingOrderType.md) | since 24.3 | The business key identifier of order type. |
| `OrderType` | `ManufacturingOrderTypes` | no | [ManufacturingOrderTypes](ManufacturingOrderType.md) | expandable, since 24.3 | Order type of the Manufacturing Order. |

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

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `ManufacturingOrder` (expand)
- [CaseEntry](../Inventory/CaseEntry.md) — `ManufacturingOrderId` (FK)
- [Locations](../Inventory/Location.md) — `ManufacturingOrderId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `ManufacturingOrder` (expand)
- [ProductRecords](../Inventory/ProductRecord.md) — `ManufacturingOrderId` (FK)

**Manufacturing**

- [MaintenanceReportings](MaintenanceReporting.md) — `ManufacturingOrder` (expand)
- [MaintenanceReportings](MaintenanceReporting.md) — `ManufacturingOrderId` (FK)
- [ManufacturingOrderMaterials](ManufacturingOrderMaterial.md) — `ManufacturingOrderId` (FK)
- [ManufacturingOrderOperations](ManufacturingOrderOperation.md) — `ManufacturingOrderId` (FK)

**Sales**

- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `LinkedManufacturingOrderId` (FK)


## Example

```json
{
  "Id": 0,
  "OrderNumber": null,
  "Status": 0,
  "WarehouseId": 0,
  "CommentId": null,
  "Comment": null,
  "PartId": 0,
  "Part": null,
  "ReportedQuantity": 0.0,
  "PlannedQuantity": 0.0,
  "RestQuantity": 0.0,
  "StartDate": "0001-01-01T00:00:00+00:00",
  "FinishDate": "0001-01-01T00:00:00+00:00",
  "Priority": 0,
  "CustomerOrderId": null,
  "CustomerOrder": null,
  "Operations": null,
  "Materials": null,
  "Nodes": null,
  "ProjectId": null,
  "Project": null,
  "CategoryString": null,
  "VariantCode": null,
  "CustomerId": null,
  "InitialFinishDate": "0001-01-01T00:00:00+00:00",
  "PartConfigurationId": null,
  "OrderQuantityId": null,
  "OrderQuantity": null,
  "OrderTypeId": null,
  "OrderType": null
}
```
