---
type: API Entity
title: BankAccounts
description: Represents a bank account.
resource: https://api.monitor.se/api/Monitor.API.Accounting.BankAccount.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.BankAccount.html
  title: Monitor API — BankAccount
module: Accounting
api_class: BankAccount
doc_name: BankAccounts
endpoint: GET /api/v1/Accounting/BankAccounts
guid: 189F4F6B-16E0-4A8B-9DA6-F6D37DC4DA3C
permission: Show bank settings
introduced_in: '24.2'
property_count: 11
references_out:
- /entities/Accounting/Account.md
- /entities/Common/Address.md
- /entities/Common/Currency.md
referenced_by:
- /entities/Accounting/OutgoingPayment.md
---

# BankAccounts

Represents a bank account.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `BankAccount`
- **Endpoint:** `GET /api/v1/Accounting/BankAccounts`
- **Required permission:** Show bank settings
- **GUID:** `189F4F6B-16E0-4A8B-9DA6-F6D37DC4DA3C`
- **Introduced in:** 24.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the bank account. |
| `Code` | `String` | no |  | unique, max length 5 | The human readable identifier of the bank account. |
| `Description` | `String` | no |  |  | The translated description of the bank account. |
| `Type` | `Int32` | no |  | enum | The bank account's type. |
| `Number` | `String` | no |  | max length 50 | The bank account's number. |
| `BgNumber` | `String` | no |  | max length 9 | The bank account's bankgiro number. |
| `PgNumber` | `String` | no |  | max length 9 | The bank account's plusgiro number. |
| `BankIdentifierCode` | `String` | no |  | max length 20 | The bank account's bank identifier code. |
| `CurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the bank account's currency. |
| `AccountingAccountId` | `Int64` | no | [Accounts](Account.md) |  | The business key identifier of the bank account's accounting account. |
| `BankAddressId` | `Int64` | no | [Addresses](../Common/Address.md) |  | The business key identifier of the bank account's bank address. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Iban` | 1 |
| `Bban` | 2 |
| `Upic` | 3 |
| `Miscellaneous` | 4 |


## Referenced by

**Accounting**

- [OutgoingPayments](OutgoingPayment.md) — `SendingBankAccountId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "Type": 0,
  "Number": null,
  "BgNumber": null,
  "PgNumber": null,
  "BankIdentifierCode": null,
  "CurrencyId": 0,
  "AccountingAccountId": 0,
  "BankAddressId": 0
}
```
