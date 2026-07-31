---
type: API Entity
title: PurchaseOrderInvoiceRows
description: Represents a purchase order invoice row entry
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderInvoiceRow.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderInvoiceRow.html
  title: Monitor API — PurchaseOrderInvoiceRow
module: Purchase
api_class: PurchaseOrderInvoiceRow
doc_name: PurchaseOrderInvoiceRows
endpoint: GET /api/v1/Purchase/PurchaseOrderInvoiceRows
guid: 1A17F9C3-677C-4E68-AA31-7720DE7355AB
permission: Show purchase orders
introduced_in: '2.27'
property_count: 21
references_out:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/Coding.md
- /entities/Accounting/CodingEntry.md
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/VatRate.md
- /entities/Purchase/PurchaseOrderDeliveryRow.md
referenced_by:
- /entities/Purchase/PurchaseOrderInvoice.md
---

# PurchaseOrderInvoiceRows

Represents a purchase order invoice row entry

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `PurchaseOrderInvoiceRow`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderInvoiceRows`
- **Required permission:** Show purchase orders
- **GUID:** `1A17F9C3-677C-4E68-AA31-7720DE7355AB`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the purchase order invoice row. |
| `PurchaseOrderDeliveryRowId` | `Int64` | no | [PurchaseOrderDeliveryRows](/entities/Purchase/PurchaseOrderDeliveryRow.md) |  | The business key identifier of the purchase order delivery row. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the purchase order's invoice row comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The internal comment of the purchase order invoice row. |
| `Price` | `Decimal?` | yes |  |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the row price currency. |
| `PriceLockedFromAutomaticChanges` | `Boolean` | no |  |  | Specifies if price is locked from automatic changes. |
| `PriceIsFuturePrice` | `Boolean` | no |  |  | Specifies if price is a future price. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The price of the row in company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency for the row price in the company currency. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency for the row setup price. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |  | The setup price of the row in company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency for row setup price in company currency. |
| `VatRateId` | `Int64` | no | [VatRates](/entities/Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `Discount` | `Decimal` | no |  |  | The discount in percent set for the row. |
| `StandardPrice` | `Decimal?` | yes |  |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency for the row standard price. |
| `CodingId` | `Int64?` | yes | [CodingEntries](/entities/Accounting/CodingEntry.md) | since 2.30 | The business key identifier of the row's coding. |
| `Coding` | `Codings` | no | [Codings](/entities/Accounting/Coding.md) | expandable, since 2.30 | The coding of the row. |
| `LedgerId` | `Int64?` | yes | [AccountsPayables](/entities/Accounting/AccountsPayable.md) | since 22.5 | The business key identifier of the invoice row's ledger. |

## Referenced by

**Purchase**

- [PurchaseOrderInvoices](/entities/Purchase/PurchaseOrderInvoice.md) — `Rows` (expand)


## Example

```json
{
  "Id": 0,
  "PurchaseOrderDeliveryRowId": 0,
  "CommentId": null,
  "Comment": null,
  "Price": null,
  "PriceCurrencyId": null,
  "PriceLockedFromAutomaticChanges": false,
  "PriceIsFuturePrice": false,
  "PriceInCompanyCurrency": null,
  "PriceInCompanyCurrencyCurrencyId": null,
  "SetupPrice": null,
  "SetupPriceCurrencyId": null,
  "SetupPriceInCompanyCurrency": null,
  "SetupPriceInCompanyCurrencyCurrencyId": null,
  "VatRateId": 0,
  "Discount": 0.0,
  "StandardPrice": null,
  "StandardPriceCurrencyId": null,
  "CodingId": null,
  "Coding": null,
  "LedgerId": null
}
```
