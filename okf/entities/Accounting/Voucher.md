---
type: API Entity
title: Vouchers
description: Represents a voucher.
resource: https://api.monitor.se/api/Monitor.API.Accounting.Voucher.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.Voucher.html
  title: Monitor API — Voucher
module: Accounting
api_class: Voucher
doc_name: Vouchers
endpoint: GET /api/v1/Accounting/Vouchers
guid: 7228033A-745C-43F0-9E0F-36AC9B65B761
permission: Show voucher
introduced_in: '2.30'
property_count: 41
references_out:
- /entities/Accounting/AccountingYear.md
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/AccrualAccountingRow.md
- /entities/Accounting/Voucher.md
- /entities/Accounting/VoucherRow.md
- /entities/Accounting/VoucherSeries.md
- /entities/Common/Comment.md
referenced_by:
- /entities/Accounting/FixedAsset.md
- /entities/Accounting/Voucher.md
- /entities/Accounting/VoucherRow.md
---

# Vouchers

Represents a voucher.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `Voucher`
- **Endpoint:** `GET /api/v1/Accounting/Vouchers`
- **Required permission:** Show voucher
- **GUID:** `7228033A-745C-43F0-9E0F-36AC9B65B761`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the voucher. |
| `Version` | `Int32` | no |  |  | The version of the voucher. |
| `SeriesId` | `Int64` | no | [VoucherSeries](VoucherSeries.md) |  | The business key identifier of the voucher series for the voucher. |
| `AccountingYearId` | `Int64` | no | [AccountingYears](AccountingYear.md) |  | The business key identifier of the accounting year for the voucher. |
| `Number` | `Int64` | no |  |  | The voucher number. |
| `Text` | `String` | no |  | max length 100 | The description of the voucher. |
| `VoucherDate` | `DateTimeOffset` | no |  |  | The date of the voucher. |
| `ConnectedVoucherId` | `Int64?` | yes | [Vouchers](Voucher.md) |  | The business key identifier of the voucher connected to the voucher. |
| `ConnectionType` | `Int32` | no |  | enum | The connection type to the connected voucher. |
| `ReverseConnectionVoucherId` | `Int64?` | yes | [Vouchers](Voucher.md) |  | The business key identifier of rectification/copy connected to the voucher. |
| `ReverseConnectionType` | `Int32` | no |  | enum | The connection type to the reverse connected voucher. |
| `IsPreliminary` | `Boolean` | no |  |  | Specifies if the voucher is preliminary. |
| `BundleNumber` | `Int64?` | yes |  |  | The bundle number of the voucher. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the voucher's comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The comment of the voucher. |
| `Rows` | `VoucherRows[]` | no | [VoucherRows](VoucherRow.md) | expandable, collection | The rows belonging to the voucher. |
| `AccountsReceivableLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's accounts receivable ledger. References AccountsReceivableLedger. |
| `CancelledAccountsReceivableLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's cancelled accounts receivable ledger. References CancelledAccountsReceivableLedger. |
| `AccountsPayableLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's accounts payable ledger. References AccountsPayableLedger. |
| `CancelledAccountsPayableLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's cancelled accounts payable ledger. References CancelledAccountsPayableLedger. |
| `PreliminaryAccountsPayableLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's preliminary accounts payable ledger. References PreliminaryAccountsPayableLedger. |
| `CancelledPreliminaryAccountsPayableLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's cancelled preliminary accounts payable ledger. References CancelledPreliminaryAccountsPayableLedger. |
| `IncomingPaymentLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's incoming payment ledger. References IncomingPaymentLedger. |
| `AccrualAccountingLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's accrual accounting ledger. References AccrualAccountingLedger. |
| `OutgoingPaymentLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's outgoing payment ledger. References OutgoingPaymentLedger. |
| `FixedAssetLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's fixed asset payment ledger. References FixedAssetLedger. |
| `UnplannedStockBalanceChangeLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's unplanned stock balance change ledger. References UnplannedStockBalanceChangeLedger. |
| `StockTransactionLogLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's stock transaction log ledger. References StockTransactionLogLedger. |
| `ManufacturingOrderLogLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's manufacturing order log ledger. References ManufacturingOrderLogLedger. |
| `InvoiceLogLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's invoice log ledger. References InvoiceLogLedger. |
| `PriceChangeLogLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's price change log ledger. References PriceChangeLogLedger. |
| `CalculationDifferenceLedgerId` | `Int64?` | yes |  |  | The business key identifier of the voucher's calculation difference ledger. References CalculationDifferenceLedger. |
| `UnplannedStockBalanceChangeTransactionId` | `Int64?` | yes |  |  | The business key identifier for the unplanned stock balance change transaction of the voucher. References UnplannedStockBalanceChangeTransaction. |
| `AccountsReceivableId` | `Int64?` | yes |  |  | The business key identifier for the accounts receivable linked to the voucher. References AccountsReceivable. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](AccountsPayable.md) |  | The business key identifier for the accounts payable linked to the voucher. |
| `AccountsPayable` | `AccountsPayables` | no | [AccountsPayables](AccountsPayable.md) | expandable | The accounts payable linked to the voucher. |
| `AccrualAccountingRowId` | `Int64?` | yes | [AccrualAccountingRows](AccrualAccountingRow.md) |  | The business key identifier for the accrual accounting row linked to the voucher. |
| `VatBookingId` | `Int64?` | yes |  |  | The business key identifier for the voucher's VAT booking. References VatBooking. |
| `CorrectionBookingId` | `Int64?` | yes |  |  | The business key identifier for the voucher's correction booking. References Booking. |
| `CNSeries` | `String` | no |  | since 25.6 | The CN series of the voucher. |
| `CNNumber` | `String` | no |  | since 25.6 | The CN number of the voucher. |

## Enumerations

### ConnectionType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Correction` | 1 |
| `Copy` | 2 |

### ReverseConnectionType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Correction` | 1 |
| `Copy` | 2 |


## Referenced by

**Accounting**

- [FixedAssets](FixedAsset.md) — `VoucherId` (FK)
- [VoucherRows](VoucherRow.md) — `VoucherId` (FK)
- [Vouchers](Voucher.md) — `ConnectedVoucherId` (FK)
- [Vouchers](Voucher.md) — `ReverseConnectionVoucherId` (FK)


## Example

```json
{
  "Id": 0,
  "Version": 0,
  "SeriesId": 0,
  "AccountingYearId": 0,
  "Number": 0,
  "Text": null,
  "VoucherDate": "0001-01-01T00:00:00+00:00",
  "ConnectedVoucherId": null,
  "ConnectionType": 0,
  "ReverseConnectionVoucherId": null,
  "ReverseConnectionType": 0,
  "IsPreliminary": false,
  "BundleNumber": null,
  "CommentId": null,
  "Comment": null,
  "Rows": null,
  "AccountsReceivableLedgerId": null,
  "CancelledAccountsReceivableLedgerId": null,
  "AccountsPayableLedgerId": null,
  "CancelledAccountsPayableLedgerId": null,
  "PreliminaryAccountsPayableLedgerId": null,
  "CancelledPreliminaryAccountsPayableLedgerId": null,
  "IncomingPaymentLedgerId": null,
  "AccrualAccountingLedgerId": null,
  "OutgoingPaymentLedgerId": null,
  "FixedAssetLedgerId": null,
  "UnplannedStockBalanceChangeLedgerId": null,
  "StockTransactionLogLedgerId": null,
  "ManufacturingOrderLogLedgerId": null,
  "InvoiceLogLedgerId": null,
  "PriceChangeLogLedgerId": null,
  "CalculationDifferenceLedgerId": null,
  "UnplannedStockBalanceChangeTransactionId": null,
  "AccountsReceivableId": null,
  "AccountsPayableId": null,
  "AccountsPayable": null,
  "AccrualAccountingRowId": null,
  "VatBookingId": null,
  "CorrectionBookingId": null,
  "CNSeries": null,
  "CNNumber": null
}
```
