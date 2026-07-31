---
type: API Entity
title: SupplierTypes
description: Represents a supplier type.
resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierType.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierType.html
  title: Monitor API — SupplierType
module: Purchase
api_class: SupplierType
doc_name: SupplierTypes
endpoint: GET /api/v1/Purchase/SupplierTypes
guid: BA03AB91-4D07-4B15-B524-22796ABC769C
permission: Show supplier
introduced_in: '2.28'
property_count: 3
referenced_by:
- /entities/Purchase/Supplier.md
---

# SupplierTypes

Represents a supplier type.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `SupplierType`
- **Endpoint:** `GET /api/v1/Purchase/SupplierTypes`
- **Required permission:** Show supplier
- **GUID:** `BA03AB91-4D07-4B15-B524-22796ABC769C`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the supplier type. |
| `Code` | `Int64` | no |  | unique | The human readable identifier of the supplier type. |
| `Description` | `String` | no |  |  | The description of the supplier type. |

## Referenced by

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `Type` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `TypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null
}
```
