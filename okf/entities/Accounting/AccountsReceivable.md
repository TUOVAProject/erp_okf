---
type: API Entity
title: AccountsReceivables
description: Represents an accounts receivable.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountsReceivable.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountsReceivable.html
  title: Monitor API — AccountsReceivable
module: Accounting
api_class: AccountsReceivable
doc_name: AccountsReceivables
endpoint: GET /api/v1/Accounting/AccountsReceivables
guid: 93690592-6919-4221-822a-1f8bfbca9ce9
permission: Show accounts receivable
introduced_in: '2.44'
property_count: 66
references_out:
- /entities/Accounting/AccountsReceivable.md
- /entities/Accounting/Booking.md
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/PaymentTerm.md
- /entities/Common/VatGroup.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerAccountGroup.md
referenced_by:
- /entities/Accounting/AccountsReceivable.md
- /entities/Accounting/AccountsReceivableCashDiscountLevel.md
- /entities/Accounting/FixedAssetSale.md
- /entities/Accounting/IncomingPayment.md
- /entities/Accounting/SetOffDestination.md
- /entities/Accounting/VoucherRow.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CasePartLink.md
- /entities/Sales/InvoiceLog.md
---

# AccountsReceivables

Represents an accounts receivable.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `AccountsReceivable`
- **Endpoint:** `GET /api/v1/Accounting/AccountsReceivables`
- **Required permission:** Show accounts receivable
- **GUID:** `93690592-6919-4221-822a-1f8bfbca9ce9`
- **Introduced in:** 2.44

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the accounts receivable. |
| `Version` | `Int32` | no |  |  | The version of the accounts receivable. |
| `BookingId` | `Int64?` | yes | [Bookings](/entities/Accounting/Booking.md) |  | The business key identifier of the booking that the accounts receivable belongs to. |
| `Booking` | `Bookings` | no | [Bookings](/entities/Accounting/Booking.md) | expandable | The booking that the accounts receivable belongs to. |
| `InvoiceType` | `Int32` | no |  | enum | The invoice type of the accounts receivable. |
| `LatestReminderDate` | `DateTimeOffset?` | yes |  |  | The latest reminder date of the accounts receivable. |
| `PaymentReminder` | `Boolean` | no |  |  | Specifies if the accounts receivable has payment reminders. |
| `NumberOfPaymentReminders` | `Int32` | no |  |  | The number of payment reminders that are left for the accounts receivable. |
| `CollectionDate` | `DateTimeOffset?` | yes |  |  | The collection date of the accounts receivable. |
| `Collection` | `Boolean` | no |  |  | Specifies if the accounts receivable has been collected or not. |
| `InterestType` | `Int32` | no |  | enum | The interest type of the accounts receivable. |
| `IsComprehensive` | `Boolean` | no |  |  | Specifies if the accounts receivable is comprehensive or not. |
| `PartialInvoiceType` | `Int32` | no |  | enum | Specifies how partial invoicing works for the accounts receivable. |
| `CustomerAccountGroupId` | `Int64` | no | [CustomerAccountGroups](/entities/Sales/CustomerAccountGroup.md) |  | The business key identifier of the customer account group for the accounts receivable. |
| `CustomerAccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](/entities/Sales/CustomerAccountGroup.md) | expandable | The customer account group of the accounts receivable. |
| `DebitInvoiceId` | `Int64?` | yes | [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) |  | The business key identifier of the debit invoice that the accounts receivable belongs to. |
| `OnAccountIncomingPaymentLedgerId` | `Int64?` | yes |  |  | The business key identifier of the incoming payment ledger for the accounts receivable. |
| `OnAccountCancelledIncomingPaymentLedgerId` | `Int64?` | yes |  |  | The business key identifier of the cancelled incoming payment ledger for the accounts receivable. |
| `IsEInvoiceExported` | `Boolean` | no |  |  | Specifies if an e-invoice has been exported for the accounts receivable. |
| `AccountsReceivableLedgerId` | `Int64?` | yes |  |  | The business key identifier of the accounts receivable ledger. |
| `CancelledAccountsReceivableLedgerId` | `Int64?` | yes |  |  | The business key identifier of the cancelled accounts receivable ledger. |
| `Status` | `Int32` | no |  | enum | The status of the accounts receivable. |
| `LatePaymentFee` | `Decimal?` | yes |  |  | The late payment fee of the accounts receivable in percent. |
| `CancelCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the cancel comment of the accounts receivable. |
| `CancelComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The cancel comment of the accounts receivable. |
| `CancelDate` | `DateTimeOffset` | no |  |  | The cancel date of the accounts receivable. |
| `CancelBookingId` | `Int64?` | yes | [Bookings](/entities/Accounting/Booking.md) |  | The business key identifier of the cancel booking that the accounts receivable belongs to. |
| `CancelBooking` | `Bookings` | no | [Bookings](/entities/Accounting/Booking.md) | expandable | The cancel booking that the accounts receivable belongs to. |
| `BusinessContactId` | `Int64?` | yes | [Customers](/entities/Sales/Customer.md) |  | The business key identifier of the customer that the accounts receivable belongs to. |
| `InvoiceNumber` | `Int64` | no |  | unique | The human readable identifier of the accounts receivable. |
| `InvoiceDate` | `DateTimeOffset` | no |  |  | The invoice date of the accounts receivable. |
| `DueDate` | `DateTimeOffset` | no |  |  | The due date of the accounts receivable. |
| `IsCredit` | `Boolean` | no |  |  | Specifies if the accounts receivable is on credit or not. |
| `InvoiceAmount` | `Decimal` | no |  |  | The invoice amount of the accounts receivable. |
| `InvoiceAmountCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the accounts receivable’s invoice amount currency. |
| `InvoiceAmountInCompanyCurrency` | `Decimal` | no |  |  | The invoice amount of the accounts receivable in the company currency. |
| `InvoiceAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the accounts receivable’s invoice amount company currency. |
| `VatAmount` | `Decimal` | no |  |  | The VAT amount of the accounts receivable. |
| `VatAmountCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the accounts receivable’s VAT amount currency. |
| `VatAmountInCompanyCurrency` | `Decimal` | no |  |  | The VAT amount of the accounts receivable in the company currency. |
| `VatAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the accounts receivable’s VAT amount company currency. |
| `RestAmount` | `Decimal` | no |  |  | The rest amount of the accounts receivable. |
| `RestAmountCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the accounts receivable’s rest amount currency. |
| `RestAmountInCompanyCurrency` | `Decimal` | no |  |  | The rest amount of the accounts receivable in the company currency. |
| `RestAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the accounts receivable’s rest amount company currency. |
| `OrderedRestAmount` | `Decimal` | no |  |  | The ordered rest amount of the accounts receivable. |
| `OrderedRestAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the accounts receivable’s ordered rest amount currency. |
| `CurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the accounts receivable currency. |
| `ExchangeRate` | `Decimal` | no |  |  | The exchange rate applicable to the accounts receivable. |
| `PaidInFullDate` | `DateTimeOffset?` | yes |  |  | Specifies when the accounts receivable was paid in full. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the accounts receivable comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the accounts receivable. |
| `ReferenceNumber` | `String` | no |  |  | The reference number of the accounts receivable. |
| `UseFixedDueDate` | `Boolean` | no |  |  | Specifies if the accounts receivable uses a fixed due date. |
| `VatGroupId` | `Int64` | no | [VatGroups](/entities/Common/VatGroup.md) |  | The business key identifier of the VAT group that the accounts receivable belongs to. |
| `PaymentTermId` | `Int64` | no | [PaymentTerms](/entities/Common/PaymentTerm.md) |  | The business key identifier of the payment term that the accounts receivable belongs to. |
| `ChineseVatInvoiceNumber` | `String` | no |  |  | The Chinese VAT invoice number of the accounts receivable. |
| `ChineseVatInvoiceDate` | `DateTimeOffset?` | yes |  |  | The Chinese VAT invoice date of the accounts receivable. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the accounts receivable's currency exchange type. |
| `CTCReportingInvoiceNumber` | `String` | no |  | since 25.6 | The invoice number for accounts receivable from CTC reporting system. |
| `CTCReportingReasonForRejection` | `String` | no |  | since 25.6 | The reason for rejection accounts receivable in CTC reporting system. |
| `CTCReportingStatus` | `Int32?` | yes |  | enum, since 25.6 | The accounts receivable's status from CTC reporting system. |
| `CTCReportingInvoiceDate` | `DateTimeOffset?` | yes |  | since 25.6 | The accounts receivable's invoice date from CTC reporting system. |
| `CTCReportingIdentifier` | `String` | no |  | since 25.6 | The accounts receivable's identifier from CTC reporting system. |
| `CTCReportingElectronicConfirmationURL` | `String` | no |  | since 25.6 | The official electronic confirmation URL of receipt from CTC reporting system. |
| `CTCReportingElectronicConfirmationNumber` | `String` | no |  | since 25.6 | The official electronic confirmation number of receipt from CTC reporting system. |

## Enumerations

### InvoiceType

| Name | Value |
| --- | ---: |
| `Standard` | 1 |
| `Internal` | 2 |
| `CashReceipt` | 3 |
| `Interest` | 4 |
| `OnAccount` | 5 |
| `DebitNote` | 6 |
| `ServiceTax` | 7 |
| `CorrectionInvoice` | 8 |
| `CollectiveCorrectionInvoice` | 9 |

### InterestType

| Name | Value |
| --- | ---: |
| `InterestInvoice` | 0 |
| `NextRegularInvoice` | 1 |
| `None` | 2 |

### PartialInvoiceType

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `InAdvance` | 1 |
| `Delivery` | 2 |
| `InArrears` | 3 |
| `Text` | 4 |

### Status

| Name | Value |
| --- | ---: |
| `Approved` | 0 |
| `Printed` | 1 |
| `Cancelled` | 2 |

### CTCReportingStatus

| Name | Value |
| --- | ---: |
| `NotSent` | 0 |
| `SentForApproval` | 1 |
| `Approved` | 2 |
| `NotApproved` | 3 |
| `Cancelled` | 4 |


## Referenced by

**Accounting**

- [AccountsReceivableCashDiscountLevels](/entities/Accounting/AccountsReceivableCashDiscountLevel.md) — `ParentId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `DebitInvoiceId` (FK)
- [FixedAssetSales](/entities/Accounting/FixedAssetSale.md) — `AccountsReceivableId` (FK)
- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `ParentId` (FK)
- [SetOffDestination](/entities/Accounting/SetOffDestination.md) — `AccountsReceivableId` (FK)
- [VoucherRows](/entities/Accounting/VoucherRow.md) — `AccountsReceivableId` (FK)

**Inventory**

- [CaseEntry](/entities/Inventory/CaseEntry.md) — `AccountReciveableId` (FK)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `AccountsReceivable` (expand)
- [CaseEntryPartLinks](/entities/Inventory/CasePartLink.md) — `CompensationAccountsReceivableId` (FK)

**Sales**

- [InvoiceLogs](/entities/Sales/InvoiceLog.md) — `InvoiceId` (FK)


## Example

```json
{
  "Id": 0,
  "Version": 0,
  "BookingId": null,
  "Booking": null,
  "InvoiceType": 0,
  "LatestReminderDate": null,
  "PaymentReminder": false,
  "NumberOfPaymentReminders": 0,
  "CollectionDate": null,
  "Collection": false,
  "InterestType": 0,
  "IsComprehensive": false,
  "PartialInvoiceType": 0,
  "CustomerAccountGroupId": 0,
  "CustomerAccountGroup": null,
  "DebitInvoiceId": null,
  "OnAccountIncomingPaymentLedgerId": null,
  "OnAccountCancelledIncomingPaymentLedgerId": null,
  "IsEInvoiceExported": false,
  "AccountsReceivableLedgerId": null,
  "CancelledAccountsReceivableLedgerId": null,
  "Status": 0,
  "LatePaymentFee": null,
  "CancelCommentId": null,
  "CancelComment": null,
  "CancelDate": "0001-01-01T00:00:00+00:00",
  "CancelBookingId": null,
  "CancelBooking": null,
  "BusinessContactId": null,
  "InvoiceNumber": 0,
  "InvoiceDate": "0001-01-01T00:00:00+00:00",
  "DueDate": "0001-01-01T00:00:00+00:00",
  "IsCredit": false,
  "InvoiceAmount": 0.0,
  "InvoiceAmountCurrencyId": 0,
  "InvoiceAmountInCompanyCurrency": 0.0,
  "InvoiceAmountInCompanyCurrencyCurrencyId": 0,
  "VatAmount": 0.0,
  "VatAmountCurrencyId": 0,
  "VatAmountInCompanyCurrency": 0.0,
  "VatAmountInCompanyCurrencyCurrencyId": 0,
  "RestAmount": 0.0,
  "RestAmountCurrencyId": 0,
  "RestAmountInCompanyCurrency": 0.0,
  "RestAmountInCompanyCurrencyCurrencyId": 0,
  "OrderedRestAmount": 0.0,
  "OrderedRestAmountCurrencyId": null,
  "CurrencyId": 0,
  "ExchangeRate": 0.0,
  "PaidInFullDate": null,
  "CommentId": null,
  "Comment": null,
  "ReferenceNumber": null,
  "UseFixedDueDate": false,
  "VatGroupId": 0,
  "PaymentTermId": 0,
  "ChineseVatInvoiceNumber": null,
  "ChineseVatInvoiceDate": null,
  "CurrencyExchangeTypeId": 0,
  "CTCReportingInvoiceNumber": null,
  "CTCReportingReasonForRejection": null,
  "CTCReportingStatus": null,
  "CTCReportingInvoiceDate": null,
  "CTCReportingIdentifier": null,
  "CTCReportingElectronicConfirmationURL": null,
  "CTCReportingElectronicConfirmationNumber": null
}
```
