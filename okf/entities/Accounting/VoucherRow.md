---
type: API Entity
title: VoucherRows
description: Represents a voucher row.
resource: https://api.monitor.se/api/Monitor.API.Accounting.VoucherRow.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.VoucherRow.html
  title: Monitor API — VoucherRow
module: Accounting
api_class: VoucherRow
doc_name: VoucherRows
endpoint: GET /api/v1/Accounting/VoucherRows
guid: 6E23F23C-97C1-434F-97AB-ACB7BDF00C27
permission: Show voucher
introduced_in: '2.30'
property_count: 24
references_out:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/AccountsReceivable.md
- /entities/Accounting/AccrualAccounting.md
- /entities/Accounting/Balance.md
- /entities/Accounting/CodingEntry.md
- /entities/Accounting/Voucher.md
- /entities/Accounting/VoucherRow.md
- /entities/Common/Currency.md
- /entities/Common/VatRate.md
referenced_by:
- /entities/Accounting/Voucher.md
- /entities/Accounting/VoucherRow.md
---

# VoucherRows

Represents a voucher row.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `VoucherRow`
- **Endpoint:** `GET /api/v1/Accounting/VoucherRows`
- **Required permission:** Show voucher
- **GUID:** `6E23F23C-97C1-434F-97AB-ACB7BDF00C27`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the voucher row. |
| `EntryIdentifier` | `String` | no |  |  | The unique coding identifier of the voucher row's coding entry. |
| `VoucherId` | `Int64` | no | [Vouchers](Voucher.md) |  | The business key identifier of the voucher that the voucher row belongs to. |
| `ParentVoucherDate` | `DateTimeOffset` | no |  |  | The voucher date of the parent voucher. |
| `ParentIsPreliminary` | `Boolean` | no |  |  | Specifies if the parent voucher is preliminary. |
| `ExchangeRate` | `Decimal` | no |  |  | The exchange rate of the voucher row. |
| `VatRateId` | `Int64?` | yes | [VatRates](../Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `BalanceId` | `Int64?` | yes | [Balances](Balance.md) |  | The business key identifier of the row's balance. |
| `CodingMethodId` | `Int64?` | yes |  |  | The business key identifier of the row's coding method. References CodingMethod. |
| `AccrualAccountingId` | `Int64?` | yes | [AccrualAccountings](AccrualAccounting.md) |  | The business key identifier of the row's accrual accounting. |
| `OrderNumber` | `String` | no |  | max length 50 | The order number linked to the voucher row |
| `DebitInCompanyCurrency` | `Decimal` | no |  |  | Debit in the company currency. |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the debit in the company currency. |
| `CreditInCompanyCurrency` | `Decimal` | no |  |  | Credit in the company currency. |
| `CreditInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the credit in the company currency. |
| `Debit` | `Decimal` | no |  |  | Debit on the voucher row. |
| `DebitCurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the debit currency. |
| `Credit` | `Decimal` | no |  |  | Credit on the voucher row. |
| `CreditCurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the credit currency. |
| `Quantity` | `Decimal` | no |  |  | The quantity set on the voucher row. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](CodingEntry.md) |  | The business key identifier of the coding entry. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](AccountsPayable.md) | since 25.6 | The business key identifier of the accounts payable connected to the row. |
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](AccountsReceivable.md) | since 25.6 | The business key identifier of the accounts receivable connected to the row. |
| `NetAmountVoucherRowId` | `Int64?` | yes | [VoucherRows](VoucherRow.md) | since 25.6 | The business key identifier of the net amount row that the VAT row belongs to. |

## Referenced by

**Accounting**

- [VoucherRows](VoucherRow.md) — `NetAmountVoucherRowId` (FK)
- [Vouchers](Voucher.md) — `Rows` (expand)


## Example

```json
{
  "Id": 0,
  "EntryIdentifier": null,
  "VoucherId": 0,
  "ParentVoucherDate": "0001-01-01T00:00:00+00:00",
  "ParentIsPreliminary": false,
  "ExchangeRate": 0.0,
  "VatRateId": null,
  "BalanceId": null,
  "CodingMethodId": null,
  "AccrualAccountingId": null,
  "OrderNumber": null,
  "DebitInCompanyCurrency": 0.0,
  "DebitInCompanyCurrencyCurrencyId": 0,
  "CreditInCompanyCurrency": 0.0,
  "CreditInCompanyCurrencyCurrencyId": 0,
  "Debit": 0.0,
  "DebitCurrencyId": 0,
  "Credit": 0.0,
  "CreditCurrencyId": 0,
  "Quantity": 0.0,
  "CodingEntryId": 0,
  "AccountsPayableId": null,
  "AccountsReceivableId": null,
  "NetAmountVoucherRowId": null
}
```
