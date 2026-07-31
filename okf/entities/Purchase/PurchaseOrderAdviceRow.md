---
type: API Entity
title: PurchaseOrderAdviceRows
description: Represents a purchase order advice row.
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderAdviceRow.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderAdviceRow.html
  title: Monitor API — PurchaseOrderAdviceRow
module: Purchase
api_class: PurchaseOrderAdviceRow
doc_name: PurchaseOrderAdviceRows
endpoint: GET /api/v1/Purchase/PurchaseOrderAdviceRows
guid: F5EA8FD8-8301-4C1A-A6DF-C26D966E4DFC
permission: Show arrival
introduced_in: '22.2'
property_count: 12
references_out:
- /entities/Common/Unit.md
- /entities/Purchase/PurchaseOrderAdvice.md
- /entities/Purchase/PurchaseOrderAdviceRow.md
- /entities/Purchase/PurchaseOrderRow.md
referenced_by:
- /entities/Purchase/PurchaseOrderAdviceRow.md
- /entities/Purchase/PurchaseOrderAdviceRowProductRecord.md
---

# PurchaseOrderAdviceRows

Represents a purchase order advice row.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `PurchaseOrderAdviceRow`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderAdviceRows`
- **Required permission:** Show arrival
- **GUID:** `F5EA8FD8-8301-4C1A-A6DF-C26D966E4DFC`
- **Introduced in:** 22.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the purchase order advice row. |
| `PurchaseOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) |  | The business key identifier of the purchase order row for this row. |
| `ParentId` | `Int64?` | yes | [PurchaseOrderAdvices](/entities/Purchase/PurchaseOrderAdvice.md) |  | The business key identifier of the purchase order advice for this row. |
| `Status` | `Int32` | no |  | enum | The status for the row. |
| `Quantity` | `Decimal` | no |  |  | The quantity for the row. |
| `DeliveredQuantity` | `Decimal` | no |  |  | The delivered quantity for the row. |
| `RestQuantity` | `Decimal` | no |  |  | The rest quantity for the row. |
| `UnitId` | `Int64?` | yes | [Units](/entities/Common/Unit.md) |  | The business key identifier of the unit for the row. |
| `ConversionFactor` | `Decimal?` | yes |  |  | The conversion factor for the row. |
| `ParentRowId` | `Int64?` | yes | [PurchaseOrderAdviceRows](/entities/Purchase/PurchaseOrderAdviceRow.md) |  | The business key identifier of the purchase order advice row for the row. |
| `SupplierPackageNumber` | `String` | no |  | max length 80 | The supplier package number for the row. |
| `SupplierAgreementReference` | `String` | no |  | max length 80 | The supplier agreement reference tor the row. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `PartiallyDelivered` | 5 |
| `History` | 9 |


## Referenced by

**Purchase**

- [PurchaseOrderAdviceRowProductRecords](/entities/Purchase/PurchaseOrderAdviceRowProductRecord.md) — `ParentId` (FK)
- [PurchaseOrderAdviceRows](/entities/Purchase/PurchaseOrderAdviceRow.md) — `ParentRowId` (FK)


## Example

```json
{
  "Id": 0,
  "PurchaseOrderRowId": null,
  "ParentId": null,
  "Status": 0,
  "Quantity": 0.0,
  "DeliveredQuantity": 0.0,
  "RestQuantity": 0.0,
  "UnitId": null,
  "ConversionFactor": null,
  "ParentRowId": null,
  "SupplierPackageNumber": null,
  "SupplierAgreementReference": null
}
```
