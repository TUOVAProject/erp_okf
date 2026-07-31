---
type: API Entity
title: Locations
description: Represents a location (so called generated location) Can also represent
  a stock package)
resource: https://api.monitor.se/api/Monitor.API.Inventory.Location.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.Location.html
  title: Monitor API — Location
module: Inventory
api_class: Location
doc_name: Locations
endpoint: GET /api/v1/Inventory/Locations
guid: 11397529-3969-44E4-8142-B0CBAA05FD06
permission: Show locations
introduced_in: '24.4'
property_count: 31
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Location.md
- /entities/Inventory/Part.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Manufacturing/ManufacturingOrderOperationReporting.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Sales/CustomerOrder.md
referenced_by:
- /entities/Inventory/Location.md
---

# Locations

Represents a location (so called generated location) Can also represent a stock package)

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `Location`
- **Endpoint:** `GET /api/v1/Inventory/Locations`
- **Required permission:** Show locations
- **GUID:** `11397529-3969-44E4-8142-B0CBAA05FD06`
- **Introduced in:** 24.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the location. |
| `ParentId` | `Int64?` | yes | [Locations](/entities/Inventory/Location.md) |  | The business key identifier of the location's parent location. Applicable for locations that represents a stock package. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse where the location is located. |
| `Warehouse` | `Warehouses` | no | [Warehouses](/entities/Common/Warehouse.md) | expandable | The warehouse of the location. |
| `Name` | `String` | no |  | max length 35 | The name of the location or the package number. |
| `StorageType` | `Int32` | no |  | enum | The type of the location. (Single- or multipart storage) |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the comment |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the location. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the application user that blocked the entity. |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](/entities/Common/ApplicationUser.md) | expandable | The application user that blocked the location. |
| `BlockedStatus` | `Int32` | no |  | enum | The block status of the entity. |
| `BlockMessageId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The block message of the location. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |  | The date when the entity stops being blocked. |
| `SortingOrder` | `Int64?` | yes |  |  | The route sorting order. |
| `IsPackage` | `Boolean` | no |  |  | Whether this location represents a stock package |
| `MaxWidth` | `Decimal?` | yes |  |  | The max width of the location. |
| `MinWidth` | `Decimal?` | yes |  |  | The min width of the location. |
| `MaxLength` | `Decimal?` | yes |  |  | The max length of the location. |
| `MinLength` | `Decimal?` | yes |  |  | The min length of the location. |
| `MaxHeight` | `Decimal?` | yes |  |  | The max height of the location. |
| `MinHeight` | `Decimal?` | yes |  |  | The min height of the location. |
| `LoadCapacity` | `Decimal?` | yes |  |  | The max weight load capacity of the location. |
| `PackagingPartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the packaging part that defines the packaging type of this location. Applicable for locations that represents a stock package. |
| `PackagingPart` | `Parts` | no | [Parts](/entities/Inventory/Part.md) | expandable | The packaging part that defines the packaging type of this location. Applicable for locations that represents a stock package. |
| `ManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) | since 25.3 | The business key identifier of the manufacturing order that the package were created for. Applicable for locations that represents a stock package. |
| `ManufacturingOrderMaterialId` | `Int64?` | yes | [ManufacturingOrderOperationReportings](/entities/Manufacturing/ManufacturingOrderOperationReporting.md) | since 25.3 | The business key identifier of the reported material that is linked to the package. Applicable for locations that represents a stock package. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) | since 25.3 | The business key identifier of the purchase order that the package were created for. Applicable for locations that represents a stock package. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](/entities/Sales/CustomerOrder.md) | since 25.3 | The business key identifier of the customer order that the package were created for. Applicable for locations that represents a stock package. |
| `Rfid` | `String` | no |  | since 25.3 | The RFID of the package. Applicable for locations that represents a stock package. |

## Enumerations

### StorageType

| Name | Value |
| --- | ---: |
| `SinglePartStorage` | 0 |
| `MultiplePartStorage` | 1 |

### BlockedStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Message` | 1 |
| `Blocked` | 2 |


## Referenced by

**Inventory**

- [Locations](/entities/Inventory/Location.md) — `ParentId` (FK)


## Example

```json
{
  "Id": 0,
  "ParentId": null,
  "WarehouseId": 0,
  "Warehouse": null,
  "Name": null,
  "StorageType": 0,
  "CommentId": null,
  "Comment": null,
  "BlockedById": null,
  "BlockedBy": null,
  "BlockedStatus": 0,
  "BlockMessageId": null,
  "BlockMessage": null,
  "BlockedFromDate": null,
  "BlockedToDate": null,
  "SortingOrder": null,
  "IsPackage": false,
  "MaxWidth": null,
  "MinWidth": null,
  "MaxLength": null,
  "MinLength": null,
  "MaxHeight": null,
  "MinHeight": null,
  "LoadCapacity": null,
  "PackagingPartId": null,
  "PackagingPart": null,
  "ManufacturingOrderId": null,
  "ManufacturingOrderMaterialId": null,
  "PurchaseOrderId": null,
  "CustomerOrderId": null,
  "Rfid": null
}
```
