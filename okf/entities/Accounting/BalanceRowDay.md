---
type: API Entity
title: BalanceRowDays
description: Represents a balance row day.
resource: https://api.monitor.se/api/Monitor.API.Accounting.BalanceRowDay.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.BalanceRowDay.html
  title: Monitor API — BalanceRowDay
module: Accounting
api_class: BalanceRowDay
doc_name: BalanceRowDays
endpoint: GET /api/v1/Accounting/BalanceRowDays
guid: A2C89FE1-34EC-4DA0-B61B-48B8AFD9151D
permission: Show balance information
introduced_in: '22.5'
property_count: 9
references_out:
- /entities/Accounting/Balance.md
---

# BalanceRowDays

Represents a balance row day.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `BalanceRowDay`
- **Endpoint:** `GET /api/v1/Accounting/BalanceRowDays`
- **Required permission:** Show balance information
- **GUID:** `A2C89FE1-34EC-4DA0-B61B-48B8AFD9151D`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the balance row day. |
| `BalanceId` | `Int64` | no | [Balances](/entities/Accounting/Balance.md) |  | The business key identifier of the balance the balance row day belongs to. |
| `Credit` | `Decimal` | no |  |  | The credit amount in the account's currency. |
| `CreditInCompanyCurrency` | `Decimal` | no |  |  | The credit amount in company currency. |
| `Date` | `DateTimeOffset` | no |  |  | The date of the balance row day. |
| `Debit` | `Decimal` | no |  |  | The debit amount in the account's currency. |
| `DebitInCompanyCurrency` | `Decimal` | no |  |  | The debit amount in company currency. |
| `PeriodNumber` | `Int32` | no |  |  | The period number for the balance row day's date. |
| `Quantity` | `Decimal` | no |  |  | The recorded quantity of the balance row day. |

## Example

```json
{
  "Id": 0,
  "BalanceId": 0,
  "Credit": 0.0,
  "CreditInCompanyCurrency": 0.0,
  "Date": "0001-01-01T00:00:00+00:00",
  "Debit": 0.0,
  "DebitInCompanyCurrency": 0.0,
  "PeriodNumber": 0,
  "Quantity": 0.0
}
```
