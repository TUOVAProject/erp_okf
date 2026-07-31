---
type: API Entity
title: SupplierDistricts
description: Represents a supplier district.
resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierDistrict.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierDistrict.html
  title: Monitor API — SupplierDistrict
module: Purchase
api_class: SupplierDistrict
doc_name: SupplierDistricts
endpoint: GET /api/v1/Purchase/SupplierDistricts
guid: 89D36BE4-F1EF-42B4-8685-BA1BCB9C6E3E
permission: Show supplier
introduced_in: '2.28'
property_count: 3
referenced_by:
- /entities/Purchase/Supplier.md
---

# SupplierDistricts

Represents a supplier district.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `SupplierDistrict`
- **Endpoint:** `GET /api/v1/Purchase/SupplierDistricts`
- **Required permission:** Show supplier
- **GUID:** `89D36BE4-F1EF-42B4-8685-BA1BCB9C6E3E`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the supplier district. |
| `Code` | `Int64` | no |  | unique | The human readable identifier of the supplier district. |
| `Description` | `String` | no |  |  | The description of the supplier district. |

## Referenced by

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `District` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `DistrictId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null
}
```
