---
type: API Entity
title: BlanketOrderSalesRows
description: Represents a blanket order row for sales.
resource: https://api.monitor.se/api/Monitor.API.Sales.BlanketOrderSalesRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BlanketOrderSalesRow.html
  title: Monitor API — BlanketOrderSalesRow
module: Sales
api_class: BlanketOrderSalesRow
doc_name: BlanketOrderSalesRows
endpoint: GET /api/v1/Sales/BlanketOrderSalesRows
guid: 2BDCA8BD-7785-42BF-9D35-6B9A60E0CCC0
permission: Show blanket order
introduced_in: '23.4'
property_count: 40
references_out:
- /entities/Common/Currency.md
- /entities/Common/PriceList.md
- /entities/Common/Revision.md
- /entities/Common/Unit.md
- /entities/Common/VatRate.md
- /entities/Inventory/Part.md
- /entities/Sales/BlanketOrderSales.md
- /entities/Sales/BlanketOrderSalesRow.md
referenced_by:
- /entities/Sales/BlanketOrderSales.md
- /entities/Sales/BlanketOrderSalesRow.md
- /entities/Sales/CustomerOrderRow.md
---

# BlanketOrderSalesRows

Represents a blanket order row for sales.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `BlanketOrderSalesRow`
- **Endpoint:** `GET /api/v1/Sales/BlanketOrderSalesRows`
- **Required permission:** Show blanket order
- **GUID:** `2BDCA8BD-7785-42BF-9D35-6B9A60E0CCC0`
- **Introduced in:** 23.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the blanket order row. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the row. |
| `ParentOrderId` | `Int64?` | yes | [BlanketOrderSales](/entities/Sales/BlanketOrderSales.md) |  | The business key identifier of the row's blanket order. |
| `ParentRowId` | `Int64?` | yes | [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) |  | The business key identifier of the row's parent row. |
| `CustomerPartNumber` | `String` | no |  | max length 50 | The customer's part number of the row. |
| `Position` | `Int64?` | yes |  |  | The position of the row. |
| `OrderRowType` | `Int32` | no |  | enum | The order row type of the row. |
| `PartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the row's part. |
| `Part` | `Parts` | no | [Parts](/entities/Inventory/Part.md) | expandable | The part of the row. |
| `PartRowType` | `Int32` | no |  | enum | The part row type of the row. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the row. |
| `UnitId` | `Int64?` | yes | [Units](/entities/Common/Unit.md) |  | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](/entities/Common/Unit.md) | expandable | The unit of the row. |
| `Price` | `Decimal?` | yes |  |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the row's price currency. |
| `PriceCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The price currency of the row. |
| `PriceOriginPriceListId` | `Int64?` | yes | [PriceLists](/entities/Common/PriceList.md) |  | The business key identifier of the row's price origin price list. |
| `PriceLockedFromAutomaticChanges` | `Boolean?` | yes |  |  | Specifies if the row have price locked from automatic changes. |
| `PriceIsFuturePrice` | `Boolean?` | yes |  |  | Specifies if the row's price is future price. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The price in company currency of the row. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the row's company currency used in price in company currency. |
| `PriceInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The company currency used in price in company currency of the row. |
| `Discount` | `Decimal` | no |  |  | The discount of the row. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the row's setup price currency. |
| `SetupPriceCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The setup price currency of the row. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |  | The setup price in company currency of the row. |
| `VatRateId` | `Int64?` | yes | [VatRates](/entities/Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `VatRate` | `VatRates` | no | [VatRates](/entities/Common/VatRate.md) | expandable | The VAT rate of the row. |
| `ShowFreeTextIn` | `Int32` | no |  | bitmask, enum | Specifies where the row's free text should be visible. |
| `ValidThrough` | `DateTimeOffset?` | yes |  |  | The requirement date of the row. |
| `RevisionId` | `Int64?` | yes | [Revisions](/entities/Common/Revision.md) |  | The business key identifier of the row's revision. |
| `Revision` | `Revisions` | no | [Revisions](/entities/Common/Revision.md) | expandable | The revision of the row. |
| `FreeTextHtml` | `String` | no |  |  | The free text in HTML format of the row. |
| `FreeText` | `String` | no |  |  | The free text of the row. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor of the row. |
| `QuantityRatio` | `Decimal?` | yes |  |  | The quantity ratio of the row. |
| `AdditionalRowDescription` | `String` | no |  |  | The additional row description of the row. |
| `AlternatePreparationCode` | `String` | no |  | max length 200, since 26.2 | The alternate preparation code of the row. |
| `RowsGoodsLabel` | `String` | no |  | max length 80, since 26.2 | The goods label of the row. |

## Enumerations

### LifeCycleState

| Name | Value |
| --- | ---: |
| `Transient` | 1 |
| `Persistent` | 10 |
| `History` | 20 |
| `RemovableCandidate` | 99 |

### OrderRowType

| Name | Value |
| --- | ---: |
| `Part` | 1 |
| `Additional` | 2 |
| `Sum` | 3 |
| `FreeText` | 4 |

### PartRowType

| Name | Value |
| --- | ---: |
| `NotPartRow` | 0 |
| `RegularRow` | 1 |
| `SubPartRow` | 2 |
| `SetupPriceRow` | 3 |
| `AlloyCostRow` | 4 |
| `PaymentPlanRow` | 5 |
| `PackagingRow` | 6 |

### ShowFreeTextIn (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Quote` | 1 |
| `Acknowledgement` | 2 |
| `DeliveryNote` | 4 |
| `Invoice` | 8 |
| `ProFormaInvoice` | 16 |


## Referenced by

**Sales**

- [BlanketOrderSales](/entities/Sales/BlanketOrderSales.md) — `Rows` (expand)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `ParentRowId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `BlanketOrderSalesRowId` (FK)


## Example

```json
{
  "Id": 0,
  "LifeCycleState": 0,
  "ParentOrderId": null,
  "ParentRowId": null,
  "CustomerPartNumber": null,
  "Position": null,
  "OrderRowType": 0,
  "PartId": null,
  "Part": null,
  "PartRowType": 0,
  "Quantity": 0.0,
  "UnitId": null,
  "Unit": null,
  "Price": null,
  "PriceCurrencyId": null,
  "PriceCurrency": null,
  "PriceOriginPriceListId": null,
  "PriceLockedFromAutomaticChanges": null,
  "PriceIsFuturePrice": null,
  "PriceInCompanyCurrency": null,
  "PriceInCompanyCurrencyCurrencyId": null,
  "PriceInCompanyCurrencyCurrency": null,
  "Discount": 0.0,
  "SetupPrice": null,
  "SetupPriceCurrencyId": null,
  "SetupPriceCurrency": null,
  "SetupPriceInCompanyCurrency": null,
  "VatRateId": null,
  "VatRate": null,
  "ShowFreeTextIn": 0,
  "ValidThrough": null,
  "RevisionId": null,
  "Revision": null,
  "FreeTextHtml": null,
  "FreeText": null,
  "ConversionFactor": 0.0,
  "QuantityRatio": null,
  "AdditionalRowDescription": null,
  "AlternatePreparationCode": null,
  "RowsGoodsLabel": null
}
```
