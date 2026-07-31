---
type: API Entity
title: OrderQuantityManufacturingOrders
description: Represents a order quantity template on part that holds many partial
  quantities.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.OrderQuantityManufacturingOrder.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.OrderQuantityManufacturingOrder.html
  title: Monitor API — OrderQuantityManufacturingOrder
module: Manufacturing
api_class: OrderQuantityManufacturingOrder
doc_name: OrderQuantityManufacturingOrders
endpoint: GET /api/v1/Manufacturing/OrderQuantityManufacturingOrders
guid: 69A87003-67FA-45B3-AD3E-6FF127B6B919
permission: Show manufacturing orders
introduced_in: '22.6'
property_count: 2
references_out:
- /entities/Common/PartialQuantity.md
referenced_by:
- /entities/Manufacturing/ManufacturingOrder.md
---

# OrderQuantityManufacturingOrders

Represents a order quantity template on part that holds many partial quantities.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `OrderQuantityManufacturingOrder`
- **Endpoint:** `GET /api/v1/Manufacturing/OrderQuantityManufacturingOrders`
- **Required permission:** Show manufacturing orders
- **GUID:** `69A87003-67FA-45B3-AD3E-6FF127B6B919`
- **Introduced in:** 22.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](/entities/Common/PartialQuantity.md) | expandable, collection | The partial quantities for the order quantity. |

## Referenced by

**Manufacturing**

- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `OrderQuantity` (expand)
- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `OrderQuantityId` (FK)


## Example

```json
{
  "Id": 0,
  "PartialQuantities": null
}
```
