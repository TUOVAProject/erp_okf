---
type: API Entity
title: CustomerOrderInvoiceRows
description: Represents a customer order invoice row.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderInvoiceRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderInvoiceRow.html
  title: Monitor API — CustomerOrderInvoiceRow
module: Sales
api_class: CustomerOrderInvoiceRow
doc_name: CustomerOrderInvoiceRows
endpoint: GET /api/v1/Sales/CustomerOrderInvoiceRows
guid: 75EB28BB-44E7-4DBC-92AC-360F453A534C
permission: Show customer orders
introduced_in: '2.36'
property_count: 23
references_out:
- /entities/Common/Currency.md
- /entities/Common/VatRate.md
- /entities/Sales/CustomerOrderInvoiceOrderRowDiscount.md
referenced_by:
- /entities/Sales/CustomerOrderDeliveryRow.md
- /entities/Sales/CustomerOrderInvoiceOrderRowDiscount.md
---

# CustomerOrderInvoiceRows

Represents a customer order invoice row.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerOrderInvoiceRow`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderInvoiceRows`
- **Required permission:** Show customer orders
- **GUID:** `75EB28BB-44E7-4DBC-92AC-360F453A534C`
- **Introduced in:** 2.36

## Notes

- CustomerOrderInvoiceRows

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the row. |
| `CodingId` | `Int64?` | yes |  |  |  |
| `Discount` | `Decimal?` | yes |  |  | The discount specified on the row. |
| `InterestInvoiceBasisId` | `Int64?` | yes |  |  | The business key identifier of the interest invoice basis. |
| `LedgerId` | `Int64?` | yes |  |  | The business key identifier to the ledger's accounts receivable of the customer order invoice. |
| `OverrideStandardPrice` | `Decimal?` | yes |  |  | The value of the overridden standard price. |
| `OverrideStandardPriceCurrencyId` | `Int64?` | yes |  |  | The business key identifier of the override standard price currency |
| `Price` | `Decimal?` | yes |  |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's price currency. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The row's price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the company currency. |
| `PriceIsFuturePrice` | `Boolean?` | yes |  |  | Specifies if the price is a future price. |
| `PriceLockedFromAutomaticChanges` | `Boolean?` | yes |  |  | Specifies if price is locked from automatic changes. |
| `PriceOrigin` | `Int32?` | yes |  | enum | The price origin of the row. |
| `PriceOriginPriceListId` | `Int64?` | yes |  |  | The business key identifier of the row's original pricelist. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes |  |  | The business key identifier of the row's setup price currency. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |  | The row's setup price in the company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the company currency. |
| `StandardPrice` | `Decimal?` | yes |  |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's standard price currency. |
| `VatRateId` | `Int64?` | yes | [VatRates](../Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `DiscountRows` | `CustomerOrderInvoiceOrderRowDiscounts[]` | no | [CustomerOrderInvoiceOrderRowDiscounts](CustomerOrderInvoiceOrderRowDiscount.md) | expandable, collection, since 24.8 | The discount rows for the row. |

## Enumerations

### PriceOrigin

| Name | Value |
| --- | ---: |
| `Undefined` | 0 |
| `UserDefined` | 1 |
| `PriceList` | 2 |
| `PriceListStaggered` | 3 |
| `BusinessPartLink` | 4 |
| `BusinessPartLinkStaggered` | 5 |
| `StandardPrice` | 6 |
| `PartConfiguration` | 7 |
| `PostCalculatedAverage` | 8 |
| `BusinessPartLinkFuturePrice` | 9 |


## Referenced by

**Sales**

- [CustomerOrderDeliveryRows](CustomerOrderDeliveryRow.md) — `InvoiceRow` (expand)
- [CustomerOrderDeliveryRows](CustomerOrderDeliveryRow.md) — `InvoiceRowId` (FK)
- [CustomerOrderInvoiceOrderRowDiscounts](CustomerOrderInvoiceOrderRowDiscount.md) — `OrderRowId` (FK)


## Example

```json
{
  "Id": 0,
  "CodingId": null,
  "Discount": null,
  "InterestInvoiceBasisId": null,
  "LedgerId": null,
  "OverrideStandardPrice": null,
  "OverrideStandardPriceCurrencyId": null,
  "Price": null,
  "PriceCurrencyId": null,
  "PriceInCompanyCurrency": null,
  "PriceInCompanyCurrencyCurrencyId": null,
  "PriceIsFuturePrice": null,
  "PriceLockedFromAutomaticChanges": null,
  "PriceOrigin": null,
  "PriceOriginPriceListId": null,
  "SetupPrice": null,
  "SetupPriceCurrencyId": null,
  "SetupPriceInCompanyCurrency": null,
  "SetupPriceInCompanyCurrencyCurrencyId": null,
  "StandardPrice": null,
  "StandardPriceCurrencyId": null,
  "VatRateId": null,
  "DiscountRows": null
}
```
