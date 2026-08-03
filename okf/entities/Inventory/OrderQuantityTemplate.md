---
type: API Entity
title: OrderQuantityTemplates
description: Represents a order quantity template on part that holds many partial
  quantities.
resource: https://api.monitor.se/api/Monitor.API.Inventory.OrderQuantityTemplate.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.OrderQuantityTemplate.html
  title: Monitor API — OrderQuantityTemplate
module: Inventory
api_class: OrderQuantityTemplate
doc_name: OrderQuantityTemplates
endpoint: GET /api/v1/Inventory/OrderQuantityTemplates
guid: E5B55563-A110-4B17-BFE0-3B20269ADE26
permission: Show part
introduced_in: '22.6'
property_count: 2
references_out:
- /entities/Common/PartialQuantity.md
referenced_by:
- /entities/Inventory/Part.md
---

# OrderQuantityTemplates

Represents a order quantity template on part that holds many partial quantities.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `OrderQuantityTemplate`
- **Endpoint:** `GET /api/v1/Inventory/OrderQuantityTemplates`
- **Required permission:** Show part
- **GUID:** `E5B55563-A110-4B17-BFE0-3B20269ADE26`
- **Introduced in:** 22.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](../Common/PartialQuantity.md) | expandable, collection | The partial quantities for the order quantity. |

## Referenced by

**Inventory**

- [Parts](Part.md) — `OrderQuantity` (expand)
- [Parts](Part.md) — `OrderQuantityId` (FK)


## Example

```json
{
  "Id": 0,
  "PartialQuantities": null
}
```
