---
type: API Entity
title: OrderQuantityManufacturingOrderOperations
description: Represents a order quantity template on part that holds many partial
  quantities.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.OrderQuantityManufacturingOrderOperation.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.OrderQuantityManufacturingOrderOperation.html
  title: Monitor API — OrderQuantityManufacturingOrderOperation
module: Manufacturing
api_class: OrderQuantityManufacturingOrderOperation
doc_name: OrderQuantityManufacturingOrderOperations
endpoint: GET /api/v1/Manufacturing/OrderQuantityManufacturingOrderOperations
guid: FA5AF8B1-A66C-4ACE-B29C-A9B1142CBE5D
permission: Show manufacturing orders
introduced_in: '22.6'
property_count: 2
references_out:
- /entities/Common/PartialQuantity.md
referenced_by:
- /entities/Manufacturing/ManufacturingOrderOperation.md
---

# OrderQuantityManufacturingOrderOperations

Represents a order quantity template on part that holds many partial quantities.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `OrderQuantityManufacturingOrderOperation`
- **Endpoint:** `GET /api/v1/Manufacturing/OrderQuantityManufacturingOrderOperations`
- **Required permission:** Show manufacturing orders
- **GUID:** `FA5AF8B1-A66C-4ACE-B29C-A9B1142CBE5D`
- **Introduced in:** 22.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](/entities/Common/PartialQuantity.md) | expandable, collection | The partial quantities for the order quantity. |

## Referenced by

**Manufacturing**

- [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) — `OrderQuantity` (expand)
- [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) — `OrderQuantityId` (FK)


## Example

```json
{
  "Id": 0,
  "PartialQuantities": null
}
```
