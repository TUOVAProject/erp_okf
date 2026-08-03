---
type: API Entity
title: StandardAccounts
description: Represents a standard account.
resource: https://api.monitor.se/api/Monitor.API.Accounting.StandardAccount.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.StandardAccount.html
  title: Monitor API — StandardAccount
module: Accounting
api_class: StandardAccount
doc_name: StandardAccounts
endpoint: GET /api/v1/Accounting/StandardAccounts
guid: 0A03DEAE-320C-4079-84F4-56126CB61802
permission: Show chart of accounts
introduced_in: '22.7'
property_count: 5
references_out:
- /entities/Accounting/CodingEntry.md
referenced_by:
- /entities/Purchase/SupplierAccount.md
---

# StandardAccounts

Represents a standard account.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `StandardAccount`
- **Endpoint:** `GET /api/v1/Accounting/StandardAccounts`
- **Required permission:** Show chart of accounts
- **GUID:** `0A03DEAE-320C-4079-84F4-56126CB61802`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the standard account (mirrors AccountType). |
| `AccountType` | `Int32` | no |  | enum | The business key identifier of the standard account. |
| `Version` | `Int32` | no |  |  | The version of the account. |
| `CodingEntryId` | `Int64?` | yes | [CodingEntries](CodingEntry.md) |  | The business key identifier of the account's coding entry. |
| `StandardAccountCategory` | `Int32` | no |  | enum | The category of the account. |

## Enumerations

### AccountType

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `AccountsReceivable` | 1 |
| `AccountsPayable` | 2 |
| `InvoicingCharges` | 3 |
| `RoundOff` | 6 |
| `CustomerDiscounts` | 10 |
| `BadDebtLoss` | 11 |
| `ExchangeProfitAccountsReceivable` | 16 |
| `BankCharge` | 17 |
| `SupplierDiscounts` | 18 |
| `AccountsPayableWriteOffs` | 19 |
| `PreliminaryAccount` | 20 |
| `InsuranceCost` | 21 |
| `PreliminaryAccountsPayable` | 22 |
| `ReminderFee` | 23 |
| `RoundOffVat` | 27 |
| `VatClearingAccountToPay` | 28 |
| `ExchangeLossAccountsReceivable` | 32 |
| `ExchangeProfitAccountsPayable` | 33 |
| `ExchangeLossAccountsPayable` | 34 |
| `TransitionAccountFixedAssetSales` | 35 |
| `SuspenseAccountDuringPosteriorCoding` | 40 |
| `DebitAccountForInternalInvoices` | 43 |
| `AdditionalPartRowPurchase` | 50 |
| `AdditionalPartRowSales` | 51 |
| `PenaltyInterestExpenseForAccountsPayable` | 55 |
| `PaidAdvanceCustomer` | 63 |
| `UnrealizedExchangeProfitSales` | 96 |
| `UnrealizedExchangeLossSales` | 97 |
| `UnrealizedExchangeProfitPurchase` | 98 |
| `UnrealizedExchangeLossPurchase` | 99 |
| `OnAccountPurchase` | 101 |
| `ExchangeProfitOnPriceDifference` | 102 |
| `ExchangeLossOnPriceDifference` | 103 |
| `RoundOffPurchase` | 104 |
| `VatClearingAccountToReceive` | 105 |
| `OverDepreciations` | 106 |
| `AccountForRevaluationSales` | 124 |
| `AccountForRevaluationPurchase` | 125 |
| `PreliminaryAccrualAccountSuspendedVatForSalesAgreement` | 126 |
| `RecognizedIncomeNotInvoiced` | 135 |
| `RecognizedIncomeConsecutivePrice` | 136 |
| `RecognizedIncomeFixedPrice` | 137 |
| `AnticipatedLossIncomeFixedPrice` | 140 |
| `ReduceOfIncomeAnticipatedLoss` | 141 |
| `OffsetAccountForAdvancesBookedOnBalanceAccount` | 150 |
| `OnAccountSales` | 151 |
| `AccrualAccountForAgreements` | 152 |
| `ProjectMaterialCostCalculationWriteUp` | 153 |
| `ProjectMaterialCostCalculationOffset` | 154 |
| `FactoringFees` | 155 |
| `FactoringRecource` | 156 |
| `FactoringLoss` | 157 |
| `PaidInvoicesFromCustomer` | 158 |
| `AccrualAccountForSupplierAgreements` | 159 |

### StandardAccountCategory

| Name | Value |
| --- | ---: |
| `Sales` | 1 |
| `Purchase` | 2 |
| `Accounting` | 3 |


## Referenced by

**Purchase**

- [SupplierAccounts](../Purchase/SupplierAccount.md) — `StandardAccount` (expand)
- [SupplierAccounts](../Purchase/SupplierAccount.md) — `StandardAccountId` (FK)


## Example

```json
{
  "Id": 0,
  "AccountType": 0,
  "Version": 0,
  "CodingEntryId": null,
  "StandardAccountCategory": 0
}
```
