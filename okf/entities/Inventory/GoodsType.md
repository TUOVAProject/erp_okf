---
type: API Entity
title: GoodsTypes
description: Represents a goods type.
resource: https://api.monitor.se/api/Monitor.API.Inventory.GoodsType.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.GoodsType.html
  title: Monitor API — GoodsType
module: Inventory
api_class: GoodsType
doc_name: GoodsTypes
endpoint: GET /api/v1/Inventory/GoodsTypes
guid: C6BDE56D-B1B8-4801-9976-F65F05228C3A
permission: Show package type/goods type
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Inventory/Part.md
- /entities/Sales/CustomerOrderShippingInformationRow.md
- /entities/Sales/ShipmentPackageInformation.md
---

# GoodsTypes

Represents a goods type.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `GoodsType`
- **Endpoint:** `GET /api/v1/Inventory/GoodsTypes`
- **Required permission:** Show package type/goods type
- **GUID:** `C6BDE56D-B1B8-4801-9976-F65F05228C3A`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the goods type. |
| `Number` | `Int64` | no |  | unique | The human readable identifier of the goods type. |
| `Description` | `String` | no |  | max length 35 | The translated description of the goods type. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the goods type is active in the system. |

## Referenced by

**Inventory**

- [Parts](/entities/Inventory/Part.md) — `ExpGoodsType` (expand)
- [Parts](/entities/Inventory/Part.md) — `GoodsTypeId` (FK)

**Sales**

- [CustomerOrderShippingInformationRows](/entities/Sales/CustomerOrderShippingInformationRow.md) — `GoodsType` (expand)
- [CustomerOrderShippingInformationRows](/entities/Sales/CustomerOrderShippingInformationRow.md) — `GoodsTypeId` (FK)
- [ShipmentPackageInformations](/entities/Sales/ShipmentPackageInformation.md) — `GoodsType` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "IsActive": false
}
```
