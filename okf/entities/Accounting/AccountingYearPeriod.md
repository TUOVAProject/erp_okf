---
type: API Entity
title: AccountingYearPeriods
description: Represents a accounting year period.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingYearPeriod.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingYearPeriod.html
  title: Monitor API — AccountingYearPeriod
module: Accounting
api_class: AccountingYearPeriod
doc_name: AccountingYearPeriods
endpoint: GET /api/v1/Accounting/AccountingYearPeriods
guid: 67896436-2631-477C-A775-3B8C5C04A62A
permission: Show accounting year
introduced_in: '2.26'
property_count: 7
references_out:
- /entities/Accounting/AccountingYear.md
referenced_by:
- /entities/Accounting/AccountingBudgetPeriod.md
- /entities/Accounting/AccrualAccountingRow.md
---

# AccountingYearPeriods

Represents a accounting year period.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `AccountingYearPeriod`
- **Endpoint:** `GET /api/v1/Accounting/AccountingYearPeriods`
- **Required permission:** Show accounting year
- **GUID:** `67896436-2631-477C-A775-3B8C5C04A62A`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the accounting year period. |
| `FromDate` | `DateTimeOffset?` | yes |  |  | Period date, from |
| `ToDate` | `DateTimeOffset?` | yes |  |  | Period date, to |
| `Number` | `Int32?` | yes |  |  | Period number |
| `Status` | `Int32` | no |  | enum | Status of the period |
| `AccountingYearId` | `Int64` | no | [AccountingYears](/entities/Accounting/AccountingYear.md) |  | The business key identifier of the accounting year |
| `AccountingYear` | `AccountingYears` | no | [AccountingYears](/entities/Accounting/AccountingYear.md) | expandable | The accounting year of the period. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Undefined` | 0 |
| `Open` | 1 |
| `Closed` | 2 |
| `Locked` | 3 |


## Referenced by

**Accounting**

- [AccountingBudgetPeriods](/entities/Accounting/AccountingBudgetPeriod.md) — `PeriodId` (FK)
- [AccrualAccountingRows](/entities/Accounting/AccrualAccountingRow.md) — `Period` (expand)
- [AccrualAccountingRows](/entities/Accounting/AccrualAccountingRow.md) — `PeriodId` (FK)


## Example

```json
{
  "Id": 0,
  "FromDate": null,
  "ToDate": null,
  "Number": null,
  "Status": 0,
  "AccountingYearId": 0,
  "AccountingYear": null
}
```
