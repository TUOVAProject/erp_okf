---
type: API Entity
title: OutgoingPayments
description: Represents an outgoing payment.
resource: https://api.monitor.se/api/Monitor.API.Accounting.OutgoingPayment.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.OutgoingPayment.html
  title: Monitor API — OutgoingPayment
module: Accounting
api_class: OutgoingPayment
doc_name: OutgoingPayments
endpoint: GET /api/v1/Accounting/OutgoingPayments
guid: 8BB6D963-CDC3-45AF-9A21-4178D554EAD2
permission: Show accounts payable
introduced_in: '24.2'
property_count: 32
references_out:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/BankAccount.md
- /entities/Accounting/Booking.md
- /entities/Accounting/IncomingPayment.md
- /entities/Common/ApplicationUser.md
- /entities/Common/BusinessContactBankAccount.md
- /entities/Common/Currency.md
- /entities/Common/PaymentMethod.md
- /entities/Common/WriteOffCode.md
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
---

# OutgoingPayments

Represents an outgoing payment.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `OutgoingPayment`
- **Endpoint:** `GET /api/v1/Accounting/OutgoingPayments`
- **Required permission:** Show accounts payable
- **GUID:** `8BB6D963-CDC3-45AF-9A21-4178D554EAD2`
- **Introduced in:** 24.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the outgoing payment. |
| `AccountsPayableId` | `Int64` | no | [AccountsPayables](/entities/Accounting/AccountsPayable.md) |  | The business key identifier of the paid accounts payable. |
| `SupplierId` | `Int64` | no | [Suppliers](/entities/Purchase/Supplier.md) |  | The business key identifier of the paid supplier. |
| `CreationDate` | `DateTimeOffset` | no |  |  | The creation date of the outgoing payment. |
| `PaymentDate` | `DateTimeOffset` | no |  |  | The payment date of the outgoing payment. |
| `PaymentMethodId` | `Int64` | no | [PaymentMethods](/entities/Common/PaymentMethod.md) |  | The business key identifier of the payment's payment method. |
| `PaidAmount` | `Decimal` | no |  |  | The paid amount. |
| `PaidAmountCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the paid amount's currency. |
| `PaidAmountInCompanyCurrency` | `Decimal` | no |  |  | The paid amount in company currency. |
| `PaidAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the paid amount in company currency's currency. |
| `PaidVatAmount` | `Decimal?` | yes |  |  | The paid VAT amount. |
| `PaidVatAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the paid VAT amount's currency. |
| `BankChargeAmount` | `Decimal?` | yes |  |  | The bank charge amount. |
| `BankChargeAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the bank charge amount's currency. |
| `IsOrdered` | `Boolean` | no |  |  | Specifies if the outgoing payment is ordered for payment. |
| `IsCancelled` | `Boolean` | no |  |  | Specifies if the outgoing payment is cancelled. |
| `CancelledByUserId` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the user that cancelled the payment. |
| `CancelDate` | `DateTimeOffset?` | yes |  | **deprecated since 26.5** | The date at which the payment was cancelled. _(Replaced by CancelTimeStamp)_ |
| `CancelTimeStamp` | `DateTimeOffset?` | yes |  | since 26.5 | The timestamp when the payment was cancelled. |
| `ReceivingBankAccountId` | `Int64?` | yes | [BusinessContactBankAccounts](/entities/Common/BusinessContactBankAccount.md) |  | The business key identifier of the receiving bank account. |
| `SendingBankAccountId` | `Int64?` | yes | [BankAccounts](/entities/Accounting/BankAccount.md) |  | The business key identifier of the bank account the payment was sent from. |
| `SetOffIncomingPaymentId` | `Int64?` | yes | [IncomingPayments](/entities/Accounting/IncomingPayment.md) |  | The business key identifier of the incoming payment the payment was set off against. |
| `BookingId` | `Int64?` | yes | [Bookings](/entities/Accounting/Booking.md) |  | The business key identifier of the outgoing payment's booking. |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](/entities/Common/WriteOffCode.md) |  | The business key identifier of the outgoing payment's write off code. |
| `WriteOffAmount` | `Decimal?` | yes |  |  | The write off amount. |
| `WriteOffAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the write off amount's currency. |
| `WriteOffAmountInCompanyCurrency` | `Decimal?` | yes |  |  | The write off amount in company currency. |
| `WriteOffAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the write off amount in company currency's currency. |
| `BundleNumber` | `Int64` | no |  |  | The payment's bundle number. |
| `ChequeNumber` | `String` | no |  | max length 30 | The payment's cheque number. |
| `CurrencyExchangeRate` | `Decimal` | no |  |  | The payment's currency exchange rate. |
| `VoucherText` | `String` | no |  | max length 100 | The payment's voucher text. |

## Referenced by

**Accounting**

- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `Payments` (expand)


## Example

```json
{
  "Id": 0,
  "AccountsPayableId": 0,
  "SupplierId": 0,
  "CreationDate": "0001-01-01T00:00:00+00:00",
  "PaymentDate": "0001-01-01T00:00:00+00:00",
  "PaymentMethodId": 0,
  "PaidAmount": 0.0,
  "PaidAmountCurrencyId": 0,
  "PaidAmountInCompanyCurrency": 0.0,
  "PaidAmountInCompanyCurrencyCurrencyId": 0,
  "PaidVatAmount": null,
  "PaidVatAmountCurrencyId": null,
  "BankChargeAmount": null,
  "BankChargeAmountCurrencyId": null,
  "IsOrdered": false,
  "IsCancelled": false,
  "CancelledByUserId": null,
  "CancelDate": null,
  "CancelTimeStamp": null,
  "ReceivingBankAccountId": null,
  "SendingBankAccountId": null,
  "SetOffIncomingPaymentId": null,
  "BookingId": null,
  "WriteOffCodeId": null,
  "WriteOffAmount": null,
  "WriteOffAmountCurrencyId": null,
  "WriteOffAmountInCompanyCurrency": null,
  "WriteOffAmountInCompanyCurrencyCurrencyId": null,
  "BundleNumber": 0,
  "ChequeNumber": null,
  "CurrencyExchangeRate": 0.0,
  "VoucherText": null
}
```
