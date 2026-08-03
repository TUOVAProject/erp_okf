---
type: API Entity
title: BookingRows
description: Represents a booking row.
resource: https://api.monitor.se/api/Monitor.API.Accounting.BookingRow.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.BookingRow.html
  title: Monitor API — BookingRow
module: Accounting
api_class: BookingRow
doc_name: BookingRows
endpoint: GET /api/v1/Accounting/BookingRows
guid: 6C01AE3F-3CEA-4A92-899A-04E23F8FBD46
introduced_in: '2.27'
property_count: 20
references_out:
- /entities/Accounting/AccrualAccounting.md
- /entities/Accounting/Booking.md
- /entities/Accounting/BookingRow.md
- /entities/Accounting/CodingEntry.md
- /entities/Common/Currency.md
- /entities/Common/VatRate.md
- /entities/Purchase/PurchaseOrderDeliveryRow.md
referenced_by:
- /entities/Accounting/AccrualAccounting.md
- /entities/Accounting/AccrualAccountingRow.md
- /entities/Accounting/Booking.md
- /entities/Accounting/BookingRow.md
---

# BookingRows

Represents a booking row.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `BookingRow`
- **Endpoint:** `GET /api/v1/Accounting/BookingRows`
- **GUID:** `6C01AE3F-3CEA-4A92-899A-04E23F8FBD46`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the booking row. |
| `Type` | `Int32` | no |  | enum | The type of booking row. |
| `AuthorizedWhen` | `DateTimeOffset?` | yes |  | **deprecated since 2.49** | When the booking row was authorized. Property is obsolete, it gives last value from new list of row authorizations _(Now returns AuthorizedWhen from last row authorization)_ |
| `PurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](../Purchase/PurchaseOrderDeliveryRow.md) |  | The business key identifier of the booking rows purchase order delivery row. |
| `BookingId` | `Int64` | no | [Bookings](Booking.md) |  | The business key identifier of the booking. |
| `VatRateId` | `Int64?` | yes | [VatRates](../Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `AccrualAccountingId` | `Int64?` | yes | [AccrualAccountings](AccrualAccounting.md) |  | The business key identifier of the accrual accounting. |
| `OrderNumber` | `String` | no |  | max length 50 | The human readable identifier of the order number |
| `DebitInCompanyCurrency` | `Decimal` | no |  |  | Debit in the company currency. |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the debit in the company currency. |
| `CreditInCompanyCurrency` | `Decimal` | no |  |  | Credit in the company currency. |
| `CreditInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the credit in the company currency. |
| `Debit` | `Decimal` | no |  |  | Debit on the booking row. |
| `DebitCurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the debit currency. |
| `Credit` | `Decimal` | no |  |  | Credit on the booking row. |
| `CreditCurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the credit currency. |
| `Quantity` | `Decimal` | no |  |  | Quantity on the booking row. |
| `RowIndex` | `Int32` | no |  |  | Row index of the booking row. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](CodingEntry.md) |  | The business key identifier of the coding entry. |
| `NetAmountBookingRowId` | `Int64?` | yes | [BookingRows](BookingRow.md) | since 25.6 | The business key identifier of the net amount row that the VAT row belongs to. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `AccountsReceivable` | 1 |
| `OutputVat` | 2 |
| `AccountsPayable` | 3 |
| `PreliminaryAccountsPayable` | 4 |
| `PaymentIn` | 5 |
| `PaymentOut` | 6 |
| `Purchase` | 7 |
| `Sales` | 8 |
| `Miscellaneous` | 9 |
| `PurchaseWithoutOrder` | 10 |
| `InvoicingCharges` | 11 |
| `InsuranceCost` | 12 |
| `RoundOff` | 13 |
| `SetupPrice` | 14 |
| `Material` | 15 |
| `Inventory` | 16 |
| `PreliminaryAccount` | 17 |
| `InputVat` | 18 |
| `ExchangeRateAdjustment` | 19 |
| `InvoiceReminderFee` | 20 |
| `PriceDifference` | 21 |
| `PaymentInVat` | 22 |
| `PaymentOutVat` | 23 |
| `OtherPayment` | 24 |
| `InputVatNonDeductible` | 25 |
| `CurrencyDifference` | 26 |
| `WithholdingTax` | 27 |
| `ManualAccountsPayableFinalBookingFromG4` | 999 |


## Referenced by

**Accounting**

- [AccrualAccountingRows](AccrualAccountingRow.md) — `BookingRows` (expand)
- [AccrualAccountings](AccrualAccounting.md) — `AccountsPayableBookingRow` (expand)
- [AccrualAccountings](AccrualAccounting.md) — `BookingRows` (expand)
- [BookingRows](BookingRow.md) — `NetAmountBookingRowId` (FK)
- [Bookings](Booking.md) — `Rows` (expand)


## Example

```json
{
  "Id": 0,
  "Type": 0,
  "AuthorizedWhen": null,
  "PurchaseOrderDeliveryRowId": null,
  "BookingId": 0,
  "VatRateId": null,
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
  "RowIndex": 0,
  "CodingEntryId": 0,
  "NetAmountBookingRowId": null
}
```
