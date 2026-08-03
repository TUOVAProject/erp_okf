---
type: API Entity
title: AccrualAccountingLedgers
description: Represents a accrual accounting ledger.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccrualAccountingLedger.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccrualAccountingLedger.html
  title: Monitor API — AccrualAccountingLedger
module: Accounting
api_class: AccrualAccountingLedger
doc_name: AccrualAccountingLedgers
endpoint: GET /api/v1/Accounting/AccrualAccountingLedgers
guid: 8789B96F-264D-4572-AE51-ADD470BA8CF2
permission: Show accrual
introduced_in: '2.27'
property_count: 3
referenced_by:
- /entities/Accounting/AccrualAccountingRow.md
---

# AccrualAccountingLedgers

Represents a accrual accounting ledger.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `AccrualAccountingLedger`
- **Endpoint:** `GET /api/v1/Accounting/AccrualAccountingLedgers`
- **Required permission:** Show accrual
- **GUID:** `8789B96F-264D-4572-AE51-ADD470BA8CF2`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the accrual accounting ledger. |
| `Number` | `Int64` | no |  |  | The number of the accrual accounting ledger. |
| `ApprovedDate` | `DateTimeOffset?` | yes |  |  | When the accrual accounting ledger was approved. |

## Referenced by

**Accounting**

- [AccrualAccountingRows](AccrualAccountingRow.md) — `Ledger` (expand)
- [AccrualAccountingRows](AccrualAccountingRow.md) — `LedgerId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "ApprovedDate": null
}
```
