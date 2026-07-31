---
type: API Entity
title: OrderQuantityPurchaseOrders
description: Represents a order quantity template on part that holds many partial
  quantities.
resource: https://api.monitor.se/api/Monitor.API.Purchase.OrderQuantityPurchaseOrder.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.OrderQuantityPurchaseOrder.html
  title: Monitor API — OrderQuantityPurchaseOrder
module: Purchase
api_class: OrderQuantityPurchaseOrder
doc_name: OrderQuantityPurchaseOrders
endpoint: GET /api/v1/Purchase/OrderQuantityPurchaseOrders
guid: A8337BAA-D7FF-4BF3-AB2E-F22D423DCBE3
permission: Show purchase orders
introduced_in: '22.6'
property_count: 2
references_out:
- /entities/Common/PartialQuantity.md
referenced_by:
- /entities/Purchase/PurchaseOrderRow.md
---

# OrderQuantityPurchaseOrders

Represents a order quantity template on part that holds many partial quantities.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `OrderQuantityPurchaseOrder`
- **Endpoint:** `GET /api/v1/Purchase/OrderQuantityPurchaseOrders`
- **Required permission:** Show purchase orders
- **GUID:** `A8337BAA-D7FF-4BF3-AB2E-F22D423DCBE3`
- **Introduced in:** 22.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](/entities/Common/PartialQuantity.md) | expandable, collection | The partial quantities for the order quantity. |

## Referenced by

**Purchase**

- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `OrderQuantity` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `OrderQuantityId` (FK)


## Example

```json
{
  "Id": 0,
  "PartialQuantities": null
}
```
