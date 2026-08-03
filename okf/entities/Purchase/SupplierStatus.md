---
type: API Entity
title: SupplierStatuses
description: Represents a supplier status.
resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierStatus.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierStatus.html
  title: Monitor API — SupplierStatus
module: Purchase
api_class: SupplierStatus
doc_name: SupplierStatuses
endpoint: GET /api/v1/Purchase/SupplierStatuses
guid: F1137340-D5E3-4C75-BE64-30D9637F797C
permission: Show supplier
introduced_in: '2.28'
property_count: 3
referenced_by:
- /entities/Purchase/Supplier.md
---

# SupplierStatuses

Represents a supplier status.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `SupplierStatus`
- **Endpoint:** `GET /api/v1/Purchase/SupplierStatuses`
- **Required permission:** Show supplier
- **GUID:** `F1137340-D5E3-4C75-BE64-30D9637F797C`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the supplier status. |
| `Code` | `Int64` | no |  | unique | The human readable identifier of the supplier status. |
| `Description` | `String` | no |  |  | The description of the supplier status. |

## Referenced by

**Purchase**

- [Suppliers](Supplier.md) — `Status` (expand)
- [Suppliers](Supplier.md) — `StatusId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null
}
```
