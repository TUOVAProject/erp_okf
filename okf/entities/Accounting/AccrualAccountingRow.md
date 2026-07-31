---
type: API Entity
title: AccrualAccountingRows
description: Represents a accrual accounting row.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccrualAccountingRow.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccrualAccountingRow.html
  title: Monitor API — AccrualAccountingRow
module: Accounting
api_class: AccrualAccountingRow
doc_name: AccrualAccountingRows
endpoint: GET /api/v1/Accounting/AccrualAccountingRows
guid: C259D163-E6E4-4D28-8B53-AD0C1ECEBCBE
permission: Show accrual
introduced_in: '2.27'
property_count: 11
references_out:
- /entities/Accounting/AccountingYearPeriod.md
- /entities/Accounting/AccrualAccountingLedger.md
- /entities/Accounting/BookingRow.md
referenced_by:
- /entities/Accounting/AccrualAccounting.md
- /entities/Accounting/Voucher.md
---

# AccrualAccountingRows

Represents a accrual accounting row.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `AccrualAccountingRow`
- **Endpoint:** `GET /api/v1/Accounting/AccrualAccountingRows`
- **Required permission:** Show accrual
- **GUID:** `C259D163-E6E4-4D28-8B53-AD0C1ECEBCBE`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the accounting row. |
| `PeriodId` | `Int64` | no | [AccountingYearPeriods](/entities/Accounting/AccountingYearPeriod.md) |  | The business key identifier of the accrual accounting row's accounting year period. |
| `Period` | `AccountingYearPeriods` | no | [AccountingYearPeriods](/entities/Accounting/AccountingYearPeriod.md) | expandable | The accounting year period on the accrual accounting row. |
| `PeriodAmountInCompanyCurrency` | `Decimal` | no |  |  | Amount in company currency |
| `AccrualAccountingId` | `Int64` | no |  |  | The business key identifier of the accrual accounting. |
| `IsReleased` | `Boolean` | no |  |  | Specifies if the accrual accounting is released. |
| `LedgerId` | `Int64?` | yes | [AccrualAccountingLedgers](/entities/Accounting/AccrualAccountingLedger.md) |  | The business key identifier of the accrual accounting row's ledger. |
| `Ledger` | `AccrualAccountingLedgers` | no | [AccrualAccountingLedgers](/entities/Accounting/AccrualAccountingLedger.md) | expandable | The accrual accounting ledger. |
| `BookingId` | `Int64?` | yes |  |  | The business key identifier of the booking. |
| `RowIndex` | `Int32` | no |  |  | The row index of the accrual accounting. |
| `BookingRows` | `BookingRows[]` | no | [BookingRows](/entities/Accounting/BookingRow.md) | expandable, collection | Booking rows on the accrual accounting. |

## Referenced by

**Accounting**

- [AccrualAccountings](/entities/Accounting/AccrualAccounting.md) — `Rows` (expand)
- [Vouchers](/entities/Accounting/Voucher.md) — `AccrualAccountingRowId` (FK)


## Example

```json
{
  "Id": 0,
  "PeriodId": 0,
  "Period": null,
  "PeriodAmountInCompanyCurrency": 0.0,
  "AccrualAccountingId": 0,
  "IsReleased": false,
  "LedgerId": null,
  "Ledger": null,
  "BookingId": null,
  "RowIndex": 0,
  "BookingRows": null
}
```
