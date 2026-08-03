---
type: API Entity
title: BusinessContactBankAccounts
description: Represents a business contact bank account.
resource: https://api.monitor.se/api/Monitor.API.Common.BusinessContactBankAccount.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.BusinessContactBankAccount.html
  title: Monitor API — BusinessContactBankAccount
module: Common
api_class: BusinessContactBankAccount
doc_name: BusinessContactBankAccounts
endpoint: GET /api/v1/Common/BusinessContactBankAccounts
guid: 2E25739E-28B0-4E9A-B1E0-E5F71BB65783
introduced_in: '2.28'
property_count: 14
references_out:
- /entities/Common/Address.md
- /entities/Common/CentralBankCode.md
- /entities/Common/Country.md
- /entities/Common/Currency.md
referenced_by:
- /entities/Accounting/OutgoingPayment.md
- /entities/Purchase/Supplier.md
---

# BusinessContactBankAccounts

Represents a business contact bank account.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `BusinessContactBankAccount`
- **Endpoint:** `GET /api/v1/Common/BusinessContactBankAccounts`
- **GUID:** `2E25739E-28B0-4E9A-B1E0-E5F71BB65783`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business contact bank account. |
| `ClearingNumber` | `String` | no |  |  | The clearing number of the business contact bank account. |
| `ClearingSystem` | `String` | no |  |  | The clearing system of the business contact bank account. |
| `CountryId` | `Int64` | no | [Countries](Country.md) |  | The business key identifier of the business contact bank account country. |
| `Country` | `Countries` | no | [Countries](Country.md) | expandable | The country of the business contact bank account. |
| `CentralBankCodeId` | `Int64?` | yes | [CentralBankCodes](CentralBankCode.md) |  | The business key identifier of the business contact bank account central bank code. |
| `CentralBankCode` | `CentralBankCodes` | no | [CentralBankCodes](CentralBankCode.md) | expandable | The central bank code of the business contact bank account. |
| `CurrencyId` | `Int64` | no | [Currencies](Currency.md) |  | The business key identifier of the business contact bank account currency. |
| `Currency` | `Currencies` | no | [Currencies](Currency.md) | expandable | The currency of the business contact bank account. |
| `Type` | `Int32` | no |  | enum | The type of the business contact bank account. |
| `Number` | `String` | no |  | max length 50 | The human readable identifier number of the business contact bank account. |
| `BankIdentifierCode` | `String` | no |  | max length 30 | The human readable identifier bank identifier code of the business contact bank account. |
| `BankAddressId` | `Int64?` | yes | [Addresses](Address.md) |  | The business key identifier of the business contact bank account bank address. |
| `BankAddress` | `Addresses` | no | [Addresses](Address.md) | expandable | The bank address of the business contact bank account. |

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

- [OutgoingPayments](../Accounting/OutgoingPayment.md) — `ReceivingBankAccountId` (FK)

**Purchase**

- [Suppliers](../Purchase/Supplier.md) — `AllBusinessContactBankAccountOfSupplier` (expand)
- [Suppliers](../Purchase/Supplier.md) — `DefaultBusinessContactBankAccount` (expand)
- [Suppliers](../Purchase/Supplier.md) — `DefaultBusinessContactBankAccountId` (FK)


## Example

```json
{
  "Id": 0,
  "ClearingNumber": null,
  "ClearingSystem": null,
  "CountryId": 0,
  "Country": null,
  "CentralBankCodeId": null,
  "CentralBankCode": null,
  "CurrencyId": 0,
  "Currency": null,
  "Type": 0,
  "Number": null,
  "BankIdentifierCode": null,
  "BankAddressId": null,
  "BankAddress": null
}
```
