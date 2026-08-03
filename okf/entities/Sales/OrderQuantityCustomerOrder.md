---
type: API Entity
title: OrderQuantityCustomerOrders
description: Represents a order quantity template on part that holds many partial
  quantities.
resource: https://api.monitor.se/api/Monitor.API.Sales.OrderQuantityCustomerOrder.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.OrderQuantityCustomerOrder.html
  title: Monitor API — OrderQuantityCustomerOrder
module: Sales
api_class: OrderQuantityCustomerOrder
doc_name: OrderQuantityCustomerOrders
endpoint: GET /api/v1/Sales/OrderQuantityCustomerOrders
guid: 90AE5E92-2966-41AA-9FB7-DA086D66EA0E
permission: Show purchase orders
introduced_in: '22.6'
property_count: 2
references_out:
- /entities/Common/PartialQuantity.md
referenced_by:
- /entities/Sales/CustomerOrderRow.md
---

# OrderQuantityCustomerOrders

Represents a order quantity template on part that holds many partial quantities.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `OrderQuantityCustomerOrder`
- **Endpoint:** `GET /api/v1/Sales/OrderQuantityCustomerOrders`
- **Required permission:** Show purchase orders
- **GUID:** `90AE5E92-2966-41AA-9FB7-DA086D66EA0E`
- **Introduced in:** 22.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](../Common/PartialQuantity.md) | expandable, collection | The partial quantities for the order quantity. |

## Referenced by

**Sales**

- [CustomerOrderRows](CustomerOrderRow.md) — `OrderQuantity` (expand)
- [CustomerOrderRows](CustomerOrderRow.md) — `OrderQuantityId` (FK)


## Example

```json
{
  "Id": 0,
  "PartialQuantities": null
}
```
