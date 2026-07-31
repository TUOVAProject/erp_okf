---
type: API Entity
title: StaggeredPrices
description: Represents a staggered price.
resource: https://api.monitor.se/api/Monitor.API.Common.StaggeredPrice.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.StaggeredPrice.html
  title: Monitor API — StaggeredPrice
module: Common
api_class: StaggeredPrice
doc_name: StaggeredPrices
endpoint: GET /api/v1/Common/StaggeredPrices
guid: D18766FB-BF4B-431D-BDB2-2B47190D2935
permission: Show part
introduced_in: '2.34'
property_count: 8
references_out:
- /entities/Inventory/Part.md
referenced_by:
- /entities/Sales/CustomerPartLink.md
- /entities/Sales/SalesPrice.md
---

# StaggeredPrices

Represents a staggered price.

- **Module:** [Common](/modules/Common.md)
- **API class:** `StaggeredPrice`
- **Endpoint:** `GET /api/v1/Common/StaggeredPrices`
- **Required permission:** Show part
- **GUID:** `D18766FB-BF4B-431D-BDB2-2B47190D2935`
- **Introduced in:** 2.34

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the staggered price. |
| `PartId` | `Int64` | no | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the part the staggered price belongs to. |
| `Price` | `Decimal` | no |  |  | The price on the staggered price in the parent's currency. |
| `LowerBoundaryQuantity` | `Decimal` | no |  |  | The lower boundary quantity on the staggered price. |
| `FuturePrice` | `Decimal?` | yes |  |  | The future price on the staggered price in the parent's currency. |
| `ShippingPrice` | `Decimal` | no |  |  | The shipping price on the staggered price in the parent's currency. |
| `ParentClass` | `Guid` | no |  |  | The GUID of the staggered price's parent type. |
| `ParentId` | `Int64` | no |  |  | The business key identifier of the staggered price's parent. |

## Referenced by

**Sales**

- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `StaggeredPrices` (expand)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `StaggeredPrices` (expand)


## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "Price": 0.0,
  "LowerBoundaryQuantity": 0.0,
  "FuturePrice": null,
  "ShippingPrice": 0.0,
  "ParentClass": "00000000-0000-0000-0000-000000000000",
  "ParentId": 0
}
```
