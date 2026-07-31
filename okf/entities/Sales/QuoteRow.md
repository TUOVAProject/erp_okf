---
type: API Entity
title: QuoteRows
description: Represents a quote row.
resource: https://api.monitor.se/api/Monitor.API.Sales.QuoteRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.QuoteRow.html
  title: Monitor API — QuoteRow
module: Sales
api_class: QuoteRow
doc_name: QuoteRows
endpoint: GET /api/v1/Sales/QuoteRows
guid: CD5873CE-F08A-464A-BD0C-B60D21B56838
permission: Show quote
introduced_in: '2.18'
property_count: 52
references_out:
- /entities/Accounting/Coding.md
- /entities/Common/Currency.md
- /entities/Common/PartConfiguration.md
- /entities/Common/Revision.md
- /entities/Common/StatisticalGoodsCode.md
- /entities/Common/TransferProfile.md
- /entities/Common/Unit.md
- /entities/Common/VatRate.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/Quote.md
- /entities/Sales/QuoteOrderRowDiscount.md
- /entities/Sales/QuoteRow.md
referenced_by:
- /entities/Sales/Quote.md
- /entities/Sales/QuoteOrderRowDiscount.md
- /entities/Sales/QuoteRow.md
---

# QuoteRows

Represents a quote row.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `QuoteRow`
- **Endpoint:** `GET /api/v1/Sales/QuoteRows`
- **Required permission:** Show quote
- **GUID:** `CD5873CE-F08A-464A-BD0C-B60D21B56838`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the row. |
| `Position` | `Int64?` | yes |  |  | The position of the row. |
| `OrderRowType` | `Int32` | no |  | enum | The row type. |
| `PartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the row's part. |
| `EntityIdentityString` | `String` | no |  | max length 20 | The human readable identifier of the row's entity. |
| `AdditionalRowDescription` | `String` | no |  | max length 80 | The additional row description of the row. |
| `FreeTextHtml` | `String` | no |  | max length 0 | The free text row's rich text HTML data. |
| `FreeText` | `String` | no |  | max length 0 | The free text row's raw text data. |
| `ParentRowId` | `Int64?` | yes | [QuoteRows](/entities/Sales/QuoteRow.md) |  | The business key identifier of the row's parent. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |  | The delivery date of the row. |
| `RevisionId` | `Int64?` | yes | [Revisions](/entities/Common/Revision.md) |  | The business key identifier of the row's revision. |
| `Revision` | `Revisions` | no | [Revisions](/entities/Common/Revision.md) | expandable | The revision of the row. |
| `OrderedQuantity` | `Decimal` | no |  |  | The ordered quantity of the row. |
| `Price` | `Decimal?` | yes |  |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the row's price currency. |
| `Discount` | `Decimal` | no |  |  | The discount specified on the row. |
| `ToolId` | `Int64?` | yes |  | **deprecated since 2.48** | The business key identifier of the row's tool. _(Replaced by Part)_ |
| `UnitId` | `Int64?` | yes | [Units](/entities/Common/Unit.md) |  | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](/entities/Common/Unit.md) | expandable | The unit of the row. |
| `VatRateId` | `Int64` | no | [VatRates](/entities/Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the row's warehouse. |
| `WeightPerUnit` | `Decimal?` | yes |  |  | The weight per unit of the row. |
| `OrderDate` | `DateTimeOffset` | no |  |  | The order date of the row. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor of the row. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The row's price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the company currency. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |  | The row's setup price in the company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the company currency. |
| `StandardPrice` | `Decimal?` | yes |  |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the row's standard price currency. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes |  |  | The business key identifier of the row's setup price currency. |
| `ShowPrice` | `Boolean` | no |  |  | Specifies if price should be shown for the row. |
| `PartRowType` | `Int32` | no |  | enum | The part row type of the row. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the row. |
| `PartStatus` | `Int32?` | yes |  | enum | The part status of the row. |
| `OrderedQuantityInOrderUnit` | `Decimal` | no |  |  | The ordered quantity of the row in the order unit. |
| `AlternatePreparationCode` | `String` | no |  |  | The alternate preparation code of the row. |
| `ShowFreeTextIn` | `Int32` | no |  | bitmask, enum | Specifies which documents the free text data of the row should be projected on. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](/entities/Common/StatisticalGoodsCode.md) |  | The business key identifier of the row's statistical goods code. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrder](/entities/Sales/CustomerOrder.md) |  | The business key identifier of the customer order that was created as a result of the row. |
| `ExemptFromStatistics` | `Boolean` | no |  |  | Specifies if the row should be exempted from statistics. |
| `ParentOrderId` | `Int64` | no | [Quotes](/entities/Sales/Quote.md) | since 2.27 | The business key identifier of the rows parent quote. |
| `CodingId` | `Int64?` | yes |  | since 2.33 | The business key identifier of the rows coding. |
| `Coding` | `Codings` | no | [Codings](/entities/Accounting/Coding.md) | expandable, since 2.33 | The coding of the row. |
| `RowsGoodsLabel` | `String` | no |  | expandable, since 2.40 | The goods label of the row |
| `PartConfigurationId` | `Int64?` | yes |  | since 2.46 | The business key identifier of the row's part configuration. |
| `RowIndex` | `Int32?` | yes |  | since 2.54 | The index of the row. |
| `TransferProfileId` | `Int64?` | yes | [TransferProfiles](/entities/Common/TransferProfile.md) | since 23.2 | The business key identifier of the row's transfer profile. |
| `PartConfigurationIdInRemoteCompany` | `Int64?` | yes | [PartConfigurations](/entities/Common/PartConfiguration.md) | since 23.2 | The business key identifier of the row's part configuration in the remote company. |
| `CreateCustomerOrder` | `Boolean` | no |  | since 24.5 | The create customer order option for the row |
| `DiscountRows` | `QuoteOrderRowDiscounts[]` | no | [QuoteOrderRowDiscounts](/entities/Sales/QuoteOrderRowDiscount.md) | expandable, collection, since 24.8 | The discount rows for the row. |

## Enumerations

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

### LifeCycleState

| Name | Value |
| --- | ---: |
| `Transient` | 1 |
| `Persistent` | 10 |
| `History` | 20 |
| `RemovableCandidate` | 99 |

### PartStatus

| Name | Value |
| --- | ---: |
| `Quote` | 1 |
| `Prototype` | 2 |
| `New` | 3 |
| `Normal` | 4 |
| `NewRevision` | 5 |
| `PhasingOut` | 6 |
| `Expired` | 9 |
| `Inactive` | 99 |

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

- [QuoteOrderRowDiscounts](/entities/Sales/QuoteOrderRowDiscount.md) — `OrderRowId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `ParentRowId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `Rows` (expand)


## Example

```json
{
  "Id": 0,
  "Position": null,
  "OrderRowType": 0,
  "PartId": null,
  "EntityIdentityString": null,
  "AdditionalRowDescription": null,
  "FreeTextHtml": null,
  "FreeText": null,
  "ParentRowId": null,
  "DeliveryDate": null,
  "RevisionId": null,
  "Revision": null,
  "OrderedQuantity": 0.0,
  "Price": null,
  "PriceCurrencyId": null,
  "Discount": 0.0,
  "ToolId": null,
  "UnitId": null,
  "Unit": null,
  "VatRateId": 0,
  "WarehouseId": 0,
  "WeightPerUnit": null,
  "OrderDate": "0001-01-01T00:00:00+00:00",
  "ConversionFactor": 0.0,
  "PriceInCompanyCurrency": null,
  "PriceInCompanyCurrencyCurrencyId": null,
  "SetupPriceInCompanyCurrency": null,
  "SetupPriceInCompanyCurrencyCurrencyId": null,
  "StandardPrice": null,
  "StandardPriceCurrencyId": null,
  "SetupPrice": null,
  "SetupPriceCurrencyId": null,
  "ShowPrice": false,
  "PartRowType": 0,
  "LifeCycleState": 0,
  "PartStatus": null,
  "OrderedQuantityInOrderUnit": 0.0,
  "AlternatePreparationCode": null,
  "ShowFreeTextIn": 0,
  "StatisticalGoodsCodeId": null,
  "CustomerOrderId": null,
  "ExemptFromStatistics": false,
  "ParentOrderId": 0,
  "CodingId": null,
  "Coding": null,
  "RowsGoodsLabel": null,
  "PartConfigurationId": null,
  "RowIndex": null,
  "TransferProfileId": null,
  "PartConfigurationIdInRemoteCompany": null,
  "CreateCustomerOrder": false,
  "DiscountRows": null
}
```
