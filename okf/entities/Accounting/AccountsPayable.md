---
type: API Entity
title: AccountsPayables
description: Represents a account's payable.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountsPayable.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountsPayable.html
  title: Monitor API — AccountsPayable
module: Accounting
api_class: AccountsPayable
doc_name: AccountsPayables
endpoint: GET /api/v1/Accounting/AccountsPayables
guid: 7C342374-541F-4841-ADF9-5925130FD07F
permission: Show accounts payable
introduced_in: '2.27'
property_count: 70
references_out:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/OutgoingPayment.md
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
- /entities/Common/Country.md
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/LanguageCode.md
- /entities/Common/PaymentMethod.md
- /entities/Common/PaymentTerm.md
- /entities/Common/VatGroup.md
- /entities/Common/Warehouse.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/Supplier.md
- /entities/Purchase/SupplierAccountGroup.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/AccountsPayableCashDiscountLevel.md
- /entities/Accounting/AccrualAccounting.md
- /entities/Accounting/FixedAsset.md
- /entities/Accounting/OutgoingPayment.md
- /entities/Accounting/SetOffDestination.md
- /entities/Accounting/Voucher.md
- /entities/Accounting/VoucherRow.md
- /entities/Inventory/CasePartLink.md
- /entities/Purchase/EimDocument.md
- /entities/Purchase/PurchaseOrderDeliveryRow.md
- /entities/Purchase/PurchaseOrderInvoiceRow.md
---

# AccountsPayables

Represents a account's payable.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `AccountsPayable`
- **Endpoint:** `GET /api/v1/Accounting/AccountsPayables`
- **Required permission:** Show accounts payable
- **GUID:** `7C342374-541F-4841-ADF9-5925130FD07F`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the account's payable. |
| `Version` | `Int32` | no |  |  | The version of the account's payable. |
| `CancelCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the account payable's cancellation comment. |
| `CancelComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The cancellation comment of the account payable. |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](/entities/Common/PaymentMethod.md) |  | The business key identifier of the account payable's payment method. |
| `LanguageId` | `Int64` | no | [LanguageCodes](/entities/Common/LanguageCode.md) |  | The business key identifier of the account payable's language. |
| `Language` | `LanguageCodes` | no | [LanguageCodes](/entities/Common/LanguageCode.md) | expandable | The language of the account payable. |
| `SuppliersInvoiceNumber` | `String` | no |  | max length 30 | The human readable identifier of the supplier's invoice number. |
| `InvoiceType` | `Int32` | no |  | enum | The invoice type of the accounts payable. |
| `IsCredit` | `Boolean` | no |  |  | Specifies if the accounts payable is a credit or not. |
| `IsFinalBooked` | `Boolean` | no |  |  | Specifies if the accounts payable is final booked or not. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) |  | The business key identifier of the account payable's purchase order. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse that the accounts payable belongs to. |
| `PreliminaryBookingDate` | `DateTimeOffset?` | yes |  |  | The date of the preliminary booking. |
| `VoucherDate` | `DateTimeOffset?` | yes |  |  | The voucher date of the account payable. |
| `CancelVoucherDate` | `DateTimeOffset?` | yes |  |  | The voucher cancellation date of the account payable. |
| `SupplierAccountGroupId` | `Int64?` | yes | [SupplierAccountGroups](/entities/Purchase/SupplierAccountGroup.md) |  | The business key identifier of the supplier account group of the acounts payable. |
| `CountryId` | `Int64` | no | [Countries](/entities/Common/Country.md) |  | The business key identifier of the account payable's country. |
| `Status` | `Int32` | no |  | enum | The status of the accounts payable invoice. |
| `BlockMessageId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The block message of the account payable. |
| `OCRNumber` | `String` | no |  | max length 30 | The OCR number of the account payable. |
| `UseOCRNumber` | `Boolean` | no |  |  | Specifies if OCR number is used. |
| `CreditedAccountsPayableId` | `Int64?` | yes | [AccountsPayables](/entities/Accounting/AccountsPayable.md) |  | The business key identifier of the account payable's credit account payable. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the application user that blocked the entity. |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](/entities/Common/ApplicationUser.md) | expandable | The application user that blocked the account payable. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |  | The date when the entity stops being blocked. |
| `BlockedStatus` | `Int32` | no |  | enum | The block status of the entity. |
| `BlockedContextType` | `Int32` | no |  | bitmask, enum | Specifies which contexts the block applies for. |
| `HasEimInvoice` | `Boolean` | no |  |  | Specifies if the account payable has EIM invoice. |
| `HoldEimInvoice` | `Boolean` | no |  |  | Specifies if the EIM invoice is on hold. |
| `EimInvoiceStatus` | `Int32` | no |  | enum | Specifies the status of the EIM invoice. |
| `InvoiceNumber` | `Int64` | no |  |  | The invoice number of the accounts payable. |
| `InvoiceDate` | `DateTimeOffset` | no |  |  | The invoice date on the account payable. |
| `DueDate` | `DateTimeOffset` | no |  |  | The due date on the account payable. |
| `InvoiceAmount` | `Decimal` | no |  |  | The invoice amount on the account payable. |
| `InvoiceAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the invoice amount currency. |
| `InvoiceAmountInCompanyCurrency` | `Decimal` | no |  |  | The invoice amount in the company currency. |
| `InvoiceAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the company currency for the invoice amount. |
| `VatAmount` | `Decimal` | no |  |  | The VAT amount on the account payable. |
| `VatAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the invoice vat amount currency. |
| `VatAmountInCompanyCurrency` | `Decimal` | no |  |  | The VAT amount in company currency. |
| `VatAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the company currency for the invoice vat amount. |
| `RestAmount` | `Decimal` | no |  |  | The rest amount on the account payable. |
| `RestAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the invoice rest amount currency. |
| `RestAmountInCompanyCurrency` | `Decimal` | no |  |  | The rest amount in company currency. |
| `RestAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the company currency for the invoice rest amount. |
| `OrderedRestAmount` | `Decimal` | no |  |  | The ordered rest amount on the account payable. |
| `OrderedRestAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the invoice ordered rest amount currency. |
| `CurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency on the account payable. |
| `ExchangeRate` | `Decimal` | no |  |  | The exchange rate on the account payable. |
| `PaidInFullDate` | `DateTimeOffset?` | yes |  |  | Specifies the date when the account payable was paid in full. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the account payable's comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The internal comment of the account payable. |
| `ReferenceNumber` | `String` | no |  | max length 35 | The human readable reference number on the account payable. |
| `UseFixedDueDate` | `Boolean` | no |  |  | Specifies if a fixed due date is used. |
| `VatGroupId` | `Int64?` | yes | [VatGroups](/entities/Common/VatGroup.md) |  | The business key identifier of the VAT group that the account payable belongs to. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](/entities/Common/PaymentTerm.md) |  | The business key identifier of the payment term of the account payable. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](/entities/Common/PaymentTerm.md) | expandable | The payment term of the account payable. |
| `FinalBookingId` | `Int64?` | yes |  | since 2.41.1 | The business key identifier of the account payable's final booking. References Booking. |
| `BusinessContactId` | `Int64` | no | [Suppliers](/entities/Purchase/Supplier.md) | since 22.5 | The business key identifier of the supplier that the accounts payable belongs to. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the accounts payable's currency exchange type. |
| `Payments` | `OutgoingPayments[]` | no | [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) | expandable, collection, since 24.2 | The payments of the accounts payable. |
| `WithholdTaxAmount` | `Decimal?` | yes |  | since 25.6 | The withholding tax amount on the account payable. |
| `WithholdTaxAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) | since 25.6 | The business key identifier of the withholding tax amount currency. |
| `WithholdTaxAmountInCompanyCurrency` | `Decimal?` | yes |  | since 25.6 | The withholding tax in company currency amount on the account payable. |
| `WithholdTaxAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) | since 25.6 | The business key identifier of the withholding tax in company currency amount currency. |
| `InputVatDate` | `DateTimeOffset?` | yes |  | since 26.5 | The date used to assign the invoice's input VAT to the correct VAT period. Only used in the Polish and Hungarian country packages. |
| `OutputVatDate` | `DateTimeOffset?` | yes |  | since 26.5 | The date used to assign the invoice's output VAT to the correct VAT period. Only used in the Polish and Hungarian country packages. |

## Enumerations

### InvoiceType

| Name | Value |
| --- | ---: |
| `Standard` | 1 |
| `Interest` | 4 |
| `OnAccount` | 5 |
| `ForOrderingOnAccount` | 8 |
| `CorrectionInvoice` | 9 |

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 0 |
| `Preliminary` | 1 |
| `Final` | 2 |
| `Cancelled` | 6 |

### BlockedStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Message` | 1 |
| `Blocked` | 2 |

### BlockedContextType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Payment` | 1 |

### EimInvoiceStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Hold` | 1 |
| `ForAuthorization` | 2 |
| `Approved` | 3 |
| `Rejected` | 4 |
| `FinalBooked` | 5 |


## Referenced by

**Accounting**

- [AccountsPayableCashDiscountLevels](/entities/Accounting/AccountsPayableCashDiscountLevel.md) — `ParentId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `CreditedAccountsPayableId` (FK)
- [AccrualAccountings](/entities/Accounting/AccrualAccounting.md) — `AccountsPayableId` (FK)
- [FixedAssets](/entities/Accounting/FixedAsset.md) — `AccountsPayableId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `AccountsPayableId` (FK)
- [SetOffDestination](/entities/Accounting/SetOffDestination.md) — `AccountsPayableId` (FK)
- [VoucherRows](/entities/Accounting/VoucherRow.md) — `AccountsPayableId` (FK)
- [Vouchers](/entities/Accounting/Voucher.md) — `AccountsPayable` (expand)
- [Vouchers](/entities/Accounting/Voucher.md) — `AccountsPayableId` (FK)

**Inventory**

- [CaseEntryPartLinks](/entities/Inventory/CasePartLink.md) — `CompensationAccountsPayableId` (FK)

**Purchase**

- [EimDocuments](/entities/Purchase/EimDocument.md) — `AccountsPayableId` (FK)
- [PurchaseOrderDeliveryRows](/entities/Purchase/PurchaseOrderDeliveryRow.md) — `AccountsPayableId` (FK)
- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `LedgerId` (FK)


## Example

```json
{
  "Id": 0,
  "Version": 0,
  "CancelCommentId": null,
  "CancelComment": null,
  "PaymentMethodId": null,
  "LanguageId": 0,
  "Language": null,
  "SuppliersInvoiceNumber": null,
  "InvoiceType": 0,
  "IsCredit": false,
  "IsFinalBooked": false,
  "PurchaseOrderId": null,
  "WarehouseId": 0,
  "PreliminaryBookingDate": null,
  "VoucherDate": null,
  "CancelVoucherDate": null,
  "SupplierAccountGroupId": null,
  "CountryId": 0,
  "Status": 0,
  "BlockMessageId": null,
  "BlockMessage": null,
  "OCRNumber": null,
  "UseOCRNumber": false,
  "CreditedAccountsPayableId": null,
  "BlockedById": null,
  "BlockedBy": null,
  "BlockedFromDate": null,
  "BlockedToDate": null,
  "BlockedStatus": 0,
  "BlockedContextType": 0,
  "HasEimInvoice": false,
  "HoldEimInvoice": false,
  "EimInvoiceStatus": 0,
  "InvoiceNumber": 0,
  "InvoiceDate": "0001-01-01T00:00:00+00:00",
  "DueDate": "0001-01-01T00:00:00+00:00",
  "InvoiceAmount": 0.0,
  "InvoiceAmountCurrencyId": null,
  "InvoiceAmountInCompanyCurrency": 0.0,
  "InvoiceAmountInCompanyCurrencyCurrencyId": null,
  "VatAmount": 0.0,
  "VatAmountCurrencyId": null,
  "VatAmountInCompanyCurrency": 0.0,
  "VatAmountInCompanyCurrencyCurrencyId": null,
  "RestAmount": 0.0,
  "RestAmountCurrencyId": null,
  "RestAmountInCompanyCurrency": 0.0,
  "RestAmountInCompanyCurrencyCurrencyId": null,
  "OrderedRestAmount": 0.0,
  "OrderedRestAmountCurrencyId": null,
  "CurrencyId": null,
  "ExchangeRate": 0.0,
  "PaidInFullDate": null,
  "CommentId": null,
  "Comment": null,
  "ReferenceNumber": null,
  "UseFixedDueDate": false,
  "VatGroupId": null,
  "PaymentTermId": null,
  "PaymentTerm": null,
  "FinalBookingId": null,
  "BusinessContactId": 0,
  "CurrencyExchangeTypeId": 0,
  "Payments": null,
  "WithholdTaxAmount": null,
  "WithholdTaxAmountCurrencyId": null,
  "WithholdTaxAmountInCompanyCurrency": null,
  "WithholdTaxAmountInCompanyCurrencyCurrencyId": null,
  "InputVatDate": null,
  "OutputVatDate": null
}
```
