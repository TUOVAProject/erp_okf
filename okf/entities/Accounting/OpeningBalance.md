---
type: API Entity
title: OpeningBalances
description: Represents an opening balance.
resource: https://api.monitor.se/api/Monitor.API.Accounting.OpeningBalance.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.OpeningBalance.html
  title: Monitor API — OpeningBalance
module: Accounting
api_class: OpeningBalance
doc_name: OpeningBalances
endpoint: GET /api/v1/Accounting/OpeningBalances
guid: 6E0771C2-064F-4673-A7AA-087C1C401CE1
permission: Show opening balance
introduced_in: '22.5'
property_count: 13
references_out:
- /entities/Accounting/AccountingYear.md
- /entities/Accounting/CodingEntry.md
- /entities/Common/Currency.md
referenced_by:
- /entities/Accounting/Balance.md
---

# OpeningBalances

Represents an opening balance.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `OpeningBalance`
- **Endpoint:** `GET /api/v1/Accounting/OpeningBalances`
- **Required permission:** Show opening balance
- **GUID:** `6E0771C2-064F-4673-A7AA-087C1C401CE1`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the opening balance. |
| `AccountingYearId` | `Int64` | no | [AccountingYears](/entities/Accounting/AccountingYear.md) |  | The business key identifier of the accounting year the opening balance belongs to. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) |  | The business key identifier of the coding entry the opening balance belongs to. |
| `Credit` | `Decimal` | no |  |  | The credit amount of the opening balance. |
| `CreditCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency of the credit amount. |
| `CreditInCompanyCurrency` | `Decimal` | no |  |  | The credit amount in company currency of the opening balance. |
| `CreditInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency of the credit amount in company currency. |
| `Debit` | `Decimal` | no |  |  | The debit amount of the opening balance. |
| `DebitCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency of the debit amount. |
| `DebitInCompanyCurrency` | `Decimal` | no |  |  | The debit amount in company currency of the opening balance. |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency of the debit amount in company currency. |
| `ExchangeRate` | `Decimal` | no |  |  | The exchange rate on the opening balance. |
| `Quantity` | `Decimal` | no |  |  | The recorded quantity of the opening balance. |

## Referenced by

**Accounting**

- [Balances](/entities/Accounting/Balance.md) — `OpeningBalanceId` (FK)


## Example

```json
{
  "Id": 0,
  "AccountingYearId": 0,
  "CodingEntryId": 0,
  "Credit": 0.0,
  "CreditCurrencyId": 0,
  "CreditInCompanyCurrency": 0.0,
  "CreditInCompanyCurrencyCurrencyId": null,
  "Debit": 0.0,
  "DebitCurrencyId": 0,
  "DebitInCompanyCurrency": 0.0,
  "DebitInCompanyCurrencyCurrencyId": 0,
  "ExchangeRate": 0.0,
  "Quantity": 0.0
}
```
