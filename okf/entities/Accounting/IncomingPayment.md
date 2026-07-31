---
type: API Entity
title: IncomingPayments
description: Represents an incoming payment.
resource: https://api.monitor.se/api/Monitor.API.Accounting.IncomingPayment.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.IncomingPayment.html
  title: Monitor API — IncomingPayment
module: Accounting
api_class: IncomingPayment
doc_name: IncomingPayments
endpoint: GET /api/v1/Accounting/IncomingPayments
guid: 8FB6A6F5-9ADA-482D-8E00-6CE9F956701D
permission: Show accounts receivable
introduced_in: '22.8'
property_count: 31
references_out:
- /entities/Accounting/AccountsReceivable.md
- /entities/Accounting/Booking.md
- /entities/Common/ApplicationUser.md
- /entities/Common/Currency.md
- /entities/Common/PaymentMethod.md
- /entities/Common/WriteOffCode.md
referenced_by:
- /entities/Accounting/OutgoingPayment.md
---

# IncomingPayments

Represents an incoming payment.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `IncomingPayment`
- **Endpoint:** `GET /api/v1/Accounting/IncomingPayments`
- **Required permission:** Show accounts receivable
- **GUID:** `8FB6A6F5-9ADA-482D-8E00-6CE9F956701D`
- **Introduced in:** 22.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the incoming payment. |
| `BankChargeAmount` | `Decimal?` | yes |  |  | The bank charge amount of the incoming payment. |
| `BankChargeAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the bank charge amount's currency. |
| `BookingId` | `Int64?` | yes | [Bookings](/entities/Accounting/Booking.md) |  | The business key identifier of the incoming payment's booking. |
| `CancelDate` | `DateTimeOffset?` | yes |  | **deprecated since 26.5** | The date the payment was cancelled. _(Replaced by CancelTimeStamp)_ |
| `CancelTimeStamp` | `DateTimeOffset?` | yes |  | since 26.5 | The timestamp when the payment was cancelled. |
| `CancelledByUserId` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the user that cancelled the payment. |
| `CancelPaymentDate` | `DateTimeOffset` | no |  |  | The date the cancellation is booked. |
| `CreationDate` | `DateTimeOffset` | no |  |  | The date the incoming payment was created. |
| `CurrencyExchangeRate` | `Decimal` | no |  |  | The exchange rate of the incoming payment. |
| `InterestType` | `Int32` | no |  | enum | The interest type of the incoming payment. |
| `IsCancelled` | `Boolean` | no |  |  | Whether or not the payment is cancelled. |
| `PaidAmount` | `Decimal` | no |  |  | The paid amount. |
| `PaidAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the paid amount's currency. |
| `PaidAmountInCompanyCurrency` | `Decimal` | no |  |  | The paid amount in company currency. |
| `PaidAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the paid amount in company currency's currency. |
| `PaidVatAmount` | `Decimal?` | yes |  |  | The paid VAT amount. |
| `PaidVatAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the paid VAT amount's currency. |
| `ParentId` | `Int64` | no | [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) |  | The business key identifier of the paid accounts receivable. |
| `PaymentDate` | `DateTimeOffset` | no |  |  | The payment date. |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](/entities/Common/PaymentMethod.md) |  | The business key identifier of the payment method. |
| `VoucherText` | `String` | no |  | max length 100 | The voucher text of the incoming payment. |
| `WriteOffAmount` | `Decimal?` | yes |  |  | The amount written off for the incoming payment. |
| `WriteOffAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency of the amount written off. |
| `WriteOffAmountInCompanyCurrency` | `Decimal?` | yes |  |  | The amount written off in company currency for the incoming payment. |
| `WriteOffAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency of the amount written off in company currency for the incoming payment. |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](/entities/Common/WriteOffCode.md) |  | The business key identifier of the incoming payment's write off code. |
| `InterestInvoicingStatus` | `Int32` | no |  | enum | The interest invoicing status of the incoming payment. |
| `IsSetOffPayment` | `Boolean` | no |  |  | Specifies if the incoming payment is a set off payment. |
| `LedgerId` | `Int64?` | yes |  |  | The business key identifier of the incoming payment ledger. References IncomingPaymentLedger. |
| `ChequeNumber` | `String` | no |  | max length 30 | The cheque number of the incoming payment. |

## Enumerations

### InterestType

| Name | Value |
| --- | ---: |
| `InterestInvoice` | 0 |
| `NextRegularInvoice` | 1 |
| `None` | 2 |

### InterestInvoicingStatus

| Name | Value |
| --- | ---: |
| `NoInterest` | 0 |
| `Interest` | 1 |
| `InterestInvoiced` | 9 |


## Referenced by

**Accounting**

- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `SetOffIncomingPaymentId` (FK)


## Example

```json
{
  "Id": 0,
  "BankChargeAmount": null,
  "BankChargeAmountCurrencyId": null,
  "BookingId": null,
  "CancelDate": null,
  "CancelTimeStamp": null,
  "CancelledByUserId": null,
  "CancelPaymentDate": "0001-01-01T00:00:00+00:00",
  "CreationDate": "0001-01-01T00:00:00+00:00",
  "CurrencyExchangeRate": 0.0,
  "InterestType": 0,
  "IsCancelled": false,
  "PaidAmount": 0.0,
  "PaidAmountCurrencyId": null,
  "PaidAmountInCompanyCurrency": 0.0,
  "PaidAmountInCompanyCurrencyCurrencyId": null,
  "PaidVatAmount": null,
  "PaidVatAmountCurrencyId": null,
  "ParentId": 0,
  "PaymentDate": "0001-01-01T00:00:00+00:00",
  "PaymentMethodId": null,
  "VoucherText": null,
  "WriteOffAmount": null,
  "WriteOffAmountCurrencyId": null,
  "WriteOffAmountInCompanyCurrency": null,
  "WriteOffAmountInCompanyCurrencyCurrencyId": null,
  "WriteOffCodeId": null,
  "InterestInvoicingStatus": 0,
  "IsSetOffPayment": false,
  "LedgerId": null,
  "ChequeNumber": null
}
```
