---
type: API Entity
title: CustomerOrderShippingInformationRows
description: Represents a customer order shipping information row.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderShippingInformationRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderShippingInformationRow.html
  title: Monitor API — CustomerOrderShippingInformationRow
module: Sales
api_class: CustomerOrderShippingInformationRow
doc_name: CustomerOrderShippingInformationRows
endpoint: GET /api/v1/Sales/CustomerOrderShippingInformationRows
guid: E71AD50F-4B83-429F-8DF1-AF17922EDDE3
permission: Show customer orders
introduced_in: '2.30'
property_count: 16
references_out:
- /entities/Inventory/GoodsType.md
- /entities/Inventory/PackageType.md
- /entities/Inventory/Part.md
referenced_by:
- /entities/Sales/CustomerOrder.md
---

# CustomerOrderShippingInformationRows

Represents a customer order shipping information row.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `CustomerOrderShippingInformationRow`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderShippingInformationRows`
- **Required permission:** Show customer orders
- **GUID:** `E71AD50F-4B83-429F-8DF1-AF17922EDDE3`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer order shipping information row. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the customer order shipping information row. |
| `NetWeight` | `Decimal` | no |  | since 26.3 | The net weight of the customer order shipping information row. |
| `Weight` | `Decimal` | no |  |  | The weight of the customer order shipping information row. |
| `Volume` | `Decimal` | no |  |  | The volume of the customer order shipping information row. |
| `LoadingMeters` | `Decimal` | no |  |  | The loading meters of the customer order shipping information row. |
| `Length` | `Decimal` | no |  |  | The length of the customer order shipping information row. |
| `Width` | `Decimal` | no |  |  | The width of the customer order shipping information row. |
| `Height` | `Decimal` | no |  |  | The height of the customer order shipping information row. |
| `PackageTypeId` | `Int64` | no | [PackageTypes](/entities/Inventory/PackageType.md) |  | The business key identifier of the customer order shipping information row's package type. |
| `PackageType` | `PackageTypes` | no | [PackageTypes](/entities/Inventory/PackageType.md) | expandable | The package type of the customer order shipping information row. |
| `GoodsTypeId` | `Int64` | no | [GoodsTypes](/entities/Inventory/GoodsType.md) |  | The business key identifier of the customer order shipping information row's goods type. |
| `GoodsType` | `GoodsTypes` | no | [GoodsTypes](/entities/Inventory/GoodsType.md) | expandable | The goods type of the customer order shipping information row. |
| `PackagingPartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the customer order shipping information row's packaging part. |
| `PackagingPart` | `Parts` | no | [Parts](/entities/Inventory/Part.md) | expandable | The packaging part of the customer order shipping information row. |
| `ParentId` | `Int64?` | yes |  |  | The business key identifier of the customer order shipping information row's parent. |

## Referenced by

**Sales**

- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `ShippingInformationRows` (expand)


## Example

```json
{
  "Id": 0,
  "Quantity": 0.0,
  "NetWeight": 0.0,
  "Weight": 0.0,
  "Volume": 0.0,
  "LoadingMeters": 0.0,
  "Length": 0.0,
  "Width": 0.0,
  "Height": 0.0,
  "PackageTypeId": 0,
  "PackageType": null,
  "GoodsTypeId": 0,
  "GoodsType": null,
  "PackagingPartId": null,
  "PackagingPart": null,
  "ParentId": null
}
```
