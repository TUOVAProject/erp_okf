---
type: API Entity
title: AccountingYears
description: Represents a accounting year.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingYear.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingYear.html
  title: Monitor API — AccountingYear
module: Accounting
api_class: AccountingYear
doc_name: AccountingYears
endpoint: GET /api/v1/Accounting/AccountingYears
guid: A0F6E162-C4A2-4605-A79B-01F17DE6FC78
permission: Show accounting year
introduced_in: '2.26'
property_count: 5
referenced_by:
- /entities/Accounting/AccountYearSetting.md
- /entities/Accounting/AccountingBudget.md
- /entities/Accounting/AccountingYearPeriod.md
- /entities/Accounting/Balance.md
- /entities/Accounting/OpeningBalance.md
- /entities/Accounting/Voucher.md
---

# AccountingYears

Represents a accounting year.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `AccountingYear`
- **Endpoint:** `GET /api/v1/Accounting/AccountingYears`
- **Required permission:** Show accounting year
- **GUID:** `A0F6E162-C4A2-4605-A79B-01F17DE6FC78`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the accounting year. |
| `ActivePeriodId` | `Int64?` | yes |  |  | The business key identifier of the active period |
| `Description` | `String` | no |  |  | The description of the accounting year |
| `Status` | `Int32` | no |  | enum | Status of the accounting year |
| `OpeningBalanceLocked` | `Boolean` | no |  |  | True if the opening balance is locked |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Active` | 0 |
| `Previous` | 1 |
| `PeriodFinancialStatement` | 2 |
| `Historical` | 9 |
| `Future` | -1 |


## Referenced by

**Accounting**

- [AccountYearSettings](/entities/Accounting/AccountYearSetting.md) — `AccountingYearId` (FK)
- [AccountingBudgets](/entities/Accounting/AccountingBudget.md) — `AccountingYearId` (FK)
- [AccountingYearPeriods](/entities/Accounting/AccountingYearPeriod.md) — `AccountingYear` (expand)
- [AccountingYearPeriods](/entities/Accounting/AccountingYearPeriod.md) — `AccountingYearId` (FK)
- [Balances](/entities/Accounting/Balance.md) — `AccountingYearId` (FK)
- [OpeningBalances](/entities/Accounting/OpeningBalance.md) — `AccountingYearId` (FK)
- [Vouchers](/entities/Accounting/Voucher.md) — `AccountingYearId` (FK)


## Example

```json
{
  "Id": 0,
  "ActivePeriodId": null,
  "Description": null,
  "Status": 0,
  "OpeningBalanceLocked": false
}
```
