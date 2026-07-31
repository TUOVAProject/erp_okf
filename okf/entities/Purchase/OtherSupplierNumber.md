---
type: API Entity
title: OtherSupplierNumbers
description: Represents an alternative supplier code mainly used for EDI.
resource: https://api.monitor.se/api/Monitor.API.Purchase.OtherSupplierNumber.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.OtherSupplierNumber.html
  title: Monitor API — OtherSupplierNumber
module: Purchase
api_class: OtherSupplierNumber
doc_name: OtherSupplierNumbers
endpoint: GET /api/v1/Purchase/OtherSupplierNumbers
guid: 297E6E0A-F2BA-498D-B066-D8108EEE7E1A
permission: Show supplier
introduced_in: '2.32'
property_count: 4
references_out:
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Purchase/Supplier.md
---

# OtherSupplierNumbers

Represents an alternative supplier code mainly used for EDI.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `OtherSupplierNumber`
- **Endpoint:** `GET /api/v1/Purchase/OtherSupplierNumbers`
- **Required permission:** Show supplier
- **GUID:** `297E6E0A-F2BA-498D-B066-D8108EEE7E1A`
- **Introduced in:** 2.32

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the other supplier number. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if this is the default/active other supplier number. |
| `Number` | `String` | no |  | max length 25 | The human readable identifier of the other supplier number. |
| `SupplierId` | `Int64` | no | [Suppliers](/entities/Purchase/Supplier.md) |  | The business key identifier of the owning supplier. |

## Referenced by

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `OtherSupplierNumbers` (expand)


## Example

```json
{
  "Id": 0,
  "IsDefault": false,
  "Number": null,
  "SupplierId": 0
}
```
