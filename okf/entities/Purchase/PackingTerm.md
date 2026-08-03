---
type: API Entity
title: PackingTerms
description: Represents a packing term.
resource: https://api.monitor.se/api/Monitor.API.Purchase.PackingTerm.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PackingTerm.html
  title: Monitor API — PackingTerm
module: Purchase
api_class: PackingTerm
doc_name: PackingTerms
endpoint: GET /api/v1/Purchase/PackingTerms
guid: b785bcb1-b0f8-4f6f-bcc7-79e99dde9305
permission: Show terms
introduced_in: '2.28'
property_count: 4
referenced_by:
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/Supplier.md
---

# PackingTerms

Represents a packing term.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `PackingTerm`
- **Endpoint:** `GET /api/v1/Purchase/PackingTerms`
- **Required permission:** Show terms
- **GUID:** `b785bcb1-b0f8-4f6f-bcc7-79e99dde9305`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the packing term. |
| `Description` | `String` | no |  |  | The description of the packing term. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the packing term. |
| `IsDefault` | `Boolean` | no |  |  | The is default of the packing term. |

## Referenced by

**Purchase**

- [PurchaseOrders](PurchaseOrder.md) — `PackingTerm` (expand)
- [PurchaseOrders](PurchaseOrder.md) — `PackingTermId` (FK)
- [Suppliers](Supplier.md) — `PackingTerm` (expand)
- [Suppliers](Supplier.md) — `PackingTermId` (FK)


## Example

```json
{
  "Id": 0,
  "Description": null,
  "Number": 0,
  "IsDefault": false
}
```
