---
type: API Entity
title: PartialQuantities
description: Represents a partial quantity.
resource: https://api.monitor.se/api/Monitor.API.Common.PartialQuantity.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PartialQuantity.html
  title: Monitor API — PartialQuantity
module: Common
api_class: PartialQuantity
doc_name: PartialQuantities
endpoint: GET /api/v1/Common/PartialQuantities
guid: 5B9F4E40-CD73-4F03-AB24-90409BF48FA0
introduced_in: '22.6'
property_count: 5
references_out:
- /entities/Inventory/Part.md
referenced_by:
- /entities/Inventory/OrderQuantityTemplate.md
- /entities/Manufacturing/OrderQuantityManufacturingOrder.md
- /entities/Manufacturing/OrderQuantityManufacturingOrderOperation.md
- /entities/Purchase/OrderQuantityPurchaseOrder.md
- /entities/Sales/OrderQuantityCustomerOrder.md
---

# PartialQuantities

Represents a partial quantity.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `PartialQuantity`
- **Endpoint:** `GET /api/v1/Common/PartialQuantities`
- **GUID:** `5B9F4E40-CD73-4F03-AB24-90409BF48FA0`
- **Introduced in:** 22.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the partial quantity. |
| `Quantity` | `Decimal` | no |  |  | Quantity, can be a length or weight. |
| `NumberOf` | `Decimal` | no |  |  | Number of Quantity. Total amount of quantities is NumberOf * Quantity |
| `PackagePartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the package part id for this partial quantity. |
| `RowIndex` | `Int32` | no |  |  | The ordered row index of the partial quantity. |

## Referenced by

**Inventory**

- [OrderQuantityTemplates](../Inventory/OrderQuantityTemplate.md) — `PartialQuantities` (expand)

**Manufacturing**

- [OrderQuantityManufacturingOrderOperations](../Manufacturing/OrderQuantityManufacturingOrderOperation.md) — `PartialQuantities` (expand)
- [OrderQuantityManufacturingOrders](../Manufacturing/OrderQuantityManufacturingOrder.md) — `PartialQuantities` (expand)

**Purchase**

- [OrderQuantityPurchaseOrders](../Purchase/OrderQuantityPurchaseOrder.md) — `PartialQuantities` (expand)

**Sales**

- [OrderQuantityCustomerOrders](../Sales/OrderQuantityCustomerOrder.md) — `PartialQuantities` (expand)


## Example

```json
{
  "Id": 0,
  "Quantity": 0.0,
  "NumberOf": 0.0,
  "PackagePartId": null,
  "RowIndex": 0
}
```
