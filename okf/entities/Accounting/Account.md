---
type: API Entity
title: Accounts
description: Represents a account.
resource: https://api.monitor.se/api/Monitor.API.Accounting.Account.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.Account.html
  title: Monitor API — Account
module: Accounting
api_class: Account
doc_name: Accounts
endpoint: GET /api/v1/Accounting/Accounts
guid: 6BA2B2FD-55E1-48FA-8735-11B3FD136552
permission: Show chart of accounts
introduced_in: '2.27'
property_count: 3
referenced_by:
- /entities/Accounting/AccountYearSetting.md
- /entities/Accounting/BankAccount.md
- /entities/Accounting/CodingEntry.md
- /entities/Common/VatRate.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/SalesAgreementBasis.md
---

# Accounts

Represents a account.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `Account`
- **Endpoint:** `GET /api/v1/Accounting/Accounts`
- **Required permission:** Show chart of accounts
- **GUID:** `6BA2B2FD-55E1-48FA-8735-11B3FD136552`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the Account. |
| `Number` | `String` | no |  | max length 10 | The human readable identifier of the account number. |
| `Type` | `Int32` | no |  | max length 10, enum | The type of account. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Assets` | 1 |
| `DebtAndOwnCapital` | 2 |
| `Incomes` | 3 |
| `Costs` | 4 |
| `Internal` | 5 |
| `BalanceSheet` | 6 |
| `OutsideBalanceSheet` | 7 |
| `Settlement` | 8 |
| `Wynikowe` | 9 |
| `FixedAssets` | 10 |
| `CurrentAssets` | 11 |
| `Equity` | 12 |
| `Liabilities` | 13 |
| `Other` | 14 |


## Referenced by

**Accounting**

- [AccountYearSettings](AccountYearSetting.md) — `Account` (expand)
- [AccountYearSettings](AccountYearSetting.md) — `AccountId` (FK)
- [BankAccounts](BankAccount.md) — `AccountingAccountId` (FK)
- [CodingEntries](CodingEntry.md) — `Account` (expand)
- [CodingEntries](CodingEntry.md) — `AccountId` (FK)

**Common**

- [VatRates](../Common/VatRate.md) — `InputVatAccountId` (FK)
- [VatRates](../Common/VatRate.md) — `OutputVatAccountId` (FK)

**Sales**

- [SalesAgreementBases](../Sales/SalesAgreementBasis.md) — `AccrualAccountId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `AccrualAccountId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": null,
  "Type": 0
}
```
