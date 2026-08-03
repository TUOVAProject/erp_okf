---
type: API Entity
title: Balances
description: Represents a balance.
resource: https://api.monitor.se/api/Monitor.API.Accounting.Balance.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.Balance.html
  title: Monitor API — Balance
module: Accounting
api_class: Balance
doc_name: Balances
endpoint: GET /api/v1/Accounting/Balances
guid: 5775FC3E-2115-4E45-A6E6-419743FA8960
permission: Show balance information
introduced_in: '22.5'
property_count: 7
references_out:
- /entities/Accounting/AccountingYear.md
- /entities/Accounting/CodingEntry.md
- /entities/Accounting/OpeningBalance.md
referenced_by:
- /entities/Accounting/AccountingBudget.md
- /entities/Accounting/BalanceRowDay.md
- /entities/Accounting/VoucherRow.md
---

# Balances

Represents a balance.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `Balance`
- **Endpoint:** `GET /api/v1/Accounting/Balances`
- **Required permission:** Show balance information
- **GUID:** `5775FC3E-2115-4E45-A6E6-419743FA8960`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the balance. |
| `AccountingYearId` | `Int64` | no | [AccountingYears](AccountingYear.md) |  | The business key identifier of the accounting year the balance belongs to. |
| `Amount` | `Decimal` | no |  |  | The balance amount in the account's currency. |
| `AmountInCompanyCurrency` | `Decimal` | no |  |  | The balance amount in company currency. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](CodingEntry.md) |  | The business key identifier of the coding entry the balance belongs to. |
| `OpeningBalanceId` | `Int64?` | yes | [OpeningBalances](OpeningBalance.md) |  | The business key identifier of the opening balance for the balance. |
| `Quantity` | `Decimal` | no |  |  | The recorded quantity of the balance. |

## Referenced by

**Accounting**

- [AccountingBudgets](AccountingBudget.md) — `BalanceId` (FK)
- [BalanceRowDays](BalanceRowDay.md) — `BalanceId` (FK)
- [VoucherRows](VoucherRow.md) — `BalanceId` (FK)


## Example

```json
{
  "Id": 0,
  "AccountingYearId": 0,
  "Amount": 0.0,
  "AmountInCompanyCurrency": 0.0,
  "CodingEntryId": 0,
  "OpeningBalanceId": null,
  "Quantity": 0.0
}
```
