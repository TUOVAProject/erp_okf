---
type: API Entity
title: AccountYearSettings
description: Represents a account setting on a specific year.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountYearSetting.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountYearSetting.html
  title: Monitor API — AccountYearSetting
module: Accounting
api_class: AccountYearSetting
doc_name: AccountYearSettings
endpoint: GET /api/v1/Accounting/AccountYearSettings
guid: 016F1042-749D-4D51-8B79-C597C16E7A47
permission: Show accounting year
introduced_in: '2.27'
property_count: 17
references_out:
- /entities/Accounting/Account.md
- /entities/Accounting/AccountYearSettingCodingDimensionAvailability.md
- /entities/Accounting/AccountingYear.md
- /entities/Common/Currency.md
- /entities/Common/VatRate.md
referenced_by:
- /entities/Accounting/AccountYearSettingCodingDimensionAvailability.md
- /entities/Accounting/AccountingBudget.md
---

# AccountYearSettings

Represents a account setting on a specific year.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `AccountYearSetting`
- **Endpoint:** `GET /api/v1/Accounting/AccountYearSettings`
- **Required permission:** Show accounting year
- **GUID:** `016F1042-749D-4D51-8B79-C597C16E7A47`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the account year setting. |
| `AccountingYearId` | `Int64` | no | [AccountingYears](AccountingYear.md) |  | The business key identifier of accounting year. |
| `Description` | `String` | no |  |  | The description of the account year setting. |
| `AllowSpecification` | `Boolean` | no |  |  | Specifies if the account year setting allows specification to be used. |
| `AllowQuantity` | `Boolean` | no |  |  | Specifies if the account year setting allows quantity to be used. |
| `IsCurrencyAccount` | `Boolean` | no |  |  | Specifies if the account year setting is a currency account. |
| `CurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the currency if used. |
| `IsAccrual` | `Boolean` | no |  |  | Specifies if the account year setting is accrual. |
| `DebitOrCreditType` | `Int32` | no |  | enum | Specifies if the account year setting is of debit or credit type. |
| `VatType` | `Int32` | no |  | enum | The vat type on the account year setting. |
| `VatRateId` | `Int64?` | yes | [VatRates](../Common/VatRate.md) |  | The business key identifier of the vat rate. |
| `BlockedForManualCoding` | `Boolean` | no |  |  | Specifies if the account year setting is block for manual coding. |
| `IsFixedAssetAccount` | `Boolean` | no |  |  | Specifies if the account year setting is a fixed asset account. |
| `IncludeOrderNumberInCoding` | `Boolean` | no |  |  | Specifies if the account year setting should include ordernumber in coding. |
| `AccountId` | `Int64` | no | [Accounts](Account.md) |  | The business key identifier of the account. |
| `Account` | `Accounts` | no | [Accounts](Account.md) | expandable | The account of the account year setting. |
| `AccountCodingDimensions` | `AccountYearSettingCodingDimensionAvailabilities[]` | no | [AccountYearSettingCodingDimensionAvailabilities](AccountYearSettingCodingDimensionAvailability.md) | expandable, collection | The account coding dimensions of the account year setting. |

## Enumerations

### DebitOrCreditType

| Name | Value |
| --- | ---: |
| `Debit` | 0 |
| `Credit` | 1 |

### VatType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Sales` | 1 |
| `Purchase` | 2 |
| `InputVat` | 3 |
| `OutputVat` | 4 |


## Referenced by

**Accounting**

- [AccountYearSettingCodingDimensionAvailabilities](AccountYearSettingCodingDimensionAvailability.md) — `AccountYearSettingId` (FK)
- [AccountingBudgets](AccountingBudget.md) — `AccountYearSettingId` (FK)


## Example

```json
{
  "Id": 0,
  "AccountingYearId": 0,
  "Description": null,
  "AllowSpecification": false,
  "AllowQuantity": false,
  "IsCurrencyAccount": false,
  "CurrencyId": null,
  "IsAccrual": false,
  "DebitOrCreditType": 0,
  "VatType": 0,
  "VatRateId": null,
  "BlockedForManualCoding": false,
  "IsFixedAssetAccount": false,
  "IncludeOrderNumberInCoding": false,
  "AccountId": 0,
  "Account": null,
  "AccountCodingDimensions": null
}
```
