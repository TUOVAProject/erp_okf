---
type: API Entity
title: SalesPickingListRowQuantities
description: Represents sales picking list row quantity information used by the web-client
  procedure.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesPickingListRowQuantity.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesPickingListRowQuantity.html
  title: Monitor API — SalesPickingListRowQuantity
module: Sales
api_class: SalesPickingListRowQuantity
doc_name: SalesPickingListRowQuantities
endpoint: GET /api/v1/Sales/SalesPickingListRowQuantities
guid: 68C563BF-D15B-439B-A71B-AB256A21A6C1
permission: Show customer orders
introduced_in: 22.1.5
property_count: 8
references_out:
- /entities/Inventory/Part.md
- /entities/Inventory/PartLocation.md
- /entities/Inventory/ProductRecord.md
- /entities/Sales/CustomerOrderDeliveryRow.md
---

# SalesPickingListRowQuantities

Represents sales picking list row quantity information used by the web-client procedure.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `SalesPickingListRowQuantity`
- **Endpoint:** `GET /api/v1/Sales/SalesPickingListRowQuantities`
- **Required permission:** Show customer orders
- **GUID:** `68C563BF-D15B-439B-A71B-AB256A21A6C1`
- **Introduced in:** 22.1.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the sales picking list row quantity. |
| `PickingListRowKey` | `String` | no |  | unique, max length 76 | The composite string key of the sales picking list row quantity. |
| `CustomerOrderDeliveryRowId` | `Int64` | no | [CustomerOrderDeliveryRows](CustomerOrderDeliveryRow.md) |  | The business key identifier of the customer order delivery row that the row quantity relates to. |
| `PartLocationId` | `Int64?` | yes | [PartLocations](../Inventory/PartLocation.md) |  | The business key identifier of the part location that the row quantity relates to. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](../Inventory/ProductRecord.md) |  | The business key identifier of the product record that the row quantity relates to. |
| `PartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the part that the row quantity relates to. |
| `Quantity` | `Decimal` | no |  |  | The quantity set for the row. |
| `Included` | `Boolean?` | yes |  |  | Null if the user has not specifically set the included state of the row, otherwise true or false depending on if the row is included or not. |

## Example

```json
{
  "Id": 0,
  "PickingListRowKey": null,
  "CustomerOrderDeliveryRowId": 0,
  "PartLocationId": null,
  "ProductRecordId": null,
  "PartId": null,
  "Quantity": 0.0,
  "Included": null
}
```
