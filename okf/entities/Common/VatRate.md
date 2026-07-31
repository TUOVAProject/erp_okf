---
type: API Entity
title: VatRates
description: Represents a VAT rate.
resource: https://api.monitor.se/api/Monitor.API.Common.VatRate.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.VatRate.html
  title: Monitor API — VatRate
module: Common
api_class: VatRate
doc_name: VatRates
endpoint: GET /api/v1/Common/VatRates
guid: 5286db96-c5f6-4394-ba8c-1d67c406b68b
permission: Show VAT settings
introduced_in: '2.18'
property_count: 15
references_out:
- /entities/Accounting/Account.md
- /entities/Common/Comment.md
referenced_by:
- /entities/Accounting/AccountYearSetting.md
- /entities/Accounting/BookingRow.md
- /entities/Accounting/VoucherRow.md
- /entities/Common/DeliveryAddress.md
- /entities/Common/VatGroup.md
- /entities/Inventory/Part.md
- /entities/Purchase/BlanketOrderPurchaseRow.md
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/PurchaseOrderInvoiceRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/BlanketOrderSalesRow.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrderInvoiceRow.md
- /entities/Sales/CustomerOrderPaymentPlanRow.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/SalesAgreementBasisRow.md
- /entities/Sales/SalesAgreementRow.md
---

# VatRates

Represents a VAT rate.

- **Module:** [Common](/modules/Common.md)
- **API class:** `VatRate`
- **Endpoint:** `GET /api/v1/Common/VatRates`
- **Required permission:** Show VAT settings
- **GUID:** `5286db96-c5f6-4394-ba8c-1d67c406b68b`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the VAT rate. |
| `Number` | `Int64` | no |  | unique | The VAT rate number. |
| `Percentage` | `Decimal` | no |  |  | The VAT percentage of the rate. |
| `Description` | `String` | no |  |  | The translated description of the rate. |
| `ReversedTax` | `Boolean` | no |  |  | Specifies if reverse tax responsibility is applicable for the rate. |
| `OutputVatAccountId` | `Int64?` | yes | [Accounts](/entities/Accounting/Account.md) |  | The business key identifier of the output account for the rate. |
| `InputVatAccountId` | `Int64?` | yes | [Accounts](/entities/Accounting/Account.md) |  | The business key identifier of the input account for the rate. |
| `Active` | `Boolean` | no |  |  | Specifies if the rate is active. |
| `ReversedTaxPercentage` | `Decimal` | no |  |  | Specifies the reverse VAT percentage of the rate. |
| `ReferenceTextId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) | **deprecated since 24.5** | The business key identifier of the rate reference text. References Comments . _(Replaced by Reference.)_ |
| `ReferenceText` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable, **deprecated since 24.5** | The rate reference text. _(Replaced by Reference.)_ |
| `Reference` | `String` | no |  | since 24.5 | The translated reference text of the rate. |
| `EcSalesType` | `Int32?` | yes |  | enum | Specifies the European Commission sales type of the VAT rate. |
| `CodeType` | `Int32` | no |  | bitmask, enum, since 24.5 | Specifies the VAT code type of the VAT rate. |
| `DatevVatCode` | `Int64?` | yes |  | since 25.6 | The VAT code used in DATEV exports. |

## Enumerations

### EcSalesType

| Name | Value |
| --- | ---: |
| `Goods trade` | 1 |
| `Services` | 2 |
| `Third party trade` | 3 |
| `GoodsTrade` | 1 |
| `Services` | 2 |
| `ThirdPartyTrade` | 3 |

### CodeType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Sales` | 1 |
| `Purchase` | 2 |


## Referenced by

**Accounting**

- [AccountYearSettings](/entities/Accounting/AccountYearSetting.md) — `VatRateId` (FK)
- [BookingRows](/entities/Accounting/BookingRow.md) — `VatRateId` (FK)
- [VoucherRows](/entities/Accounting/VoucherRow.md) — `VatRateId` (FK)

**Common**

- [DeliveryAddresses](/entities/Common/DeliveryAddress.md) — `VatRateId` (FK)
- [VatGroups](/entities/Common/VatGroup.md) — `DefaultVatRateForPurchaseId` (FK)
- [VatGroups](/entities/Common/VatGroup.md) — `DefaultVatRateForSalesId` (FK)
- [VatGroups](/entities/Common/VatGroup.md) — `DefaultVatRateId` (FK)

**Inventory**

- [Parts](/entities/Inventory/Part.md) — `VatRate` (expand)
- [Parts](/entities/Inventory/Part.md) — `VatRateId` (FK)

**Purchase**

- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `VatRate` (expand)
- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `VatRateId` (FK)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `VatRateId` (FK)
- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `VatRateId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `VatRate` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `VatRateId` (FK)

**Sales**

- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `VatRate` (expand)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `VatRateId` (FK)
- [CustomerOrderInvoiceRows](/entities/Sales/CustomerOrderInvoiceRow.md) — `VatRateId` (FK)
- [CustomerOrderPaymentPlanRows](/entities/Sales/CustomerOrderPaymentPlanRow.md) — `VatRateId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `VatRateId` (FK)
- [Customers](/entities/Sales/Customer.md) — `VatRate` (expand)
- [Customers](/entities/Sales/Customer.md) — `VatRateId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `VatRateId` (FK)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `VatRateId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `VatRateId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Percentage": 0.0,
  "Description": null,
  "ReversedTax": false,
  "OutputVatAccountId": null,
  "InputVatAccountId": null,
  "Active": false,
  "ReversedTaxPercentage": 0.0,
  "ReferenceTextId": null,
  "ReferenceText": null,
  "Reference": null,
  "EcSalesType": null,
  "CodeType": 0,
  "DatevVatCode": null
}
```
