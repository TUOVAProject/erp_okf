---
type: API Entity
title: InquiryRows
description: Represents an inquiry row.
resource: https://api.monitor.se/api/Monitor.API.Purchase.InquiryRow.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.InquiryRow.html
  title: Monitor API — InquiryRow
module: Purchase
api_class: InquiryRow
doc_name: InquiryRows
endpoint: GET /api/v1/Purchase/InquiryRows
guid: 1C7BE577-33A8-4CAF-9F52-16595EF161EB
permission: Show inquiry
introduced_in: '2.30'
property_count: 45
references_out:
- /entities/Accounting/Coding.md
- /entities/Common/Currency.md
- /entities/Common/Revision.md
- /entities/Common/StatisticalGoodsCode.md
- /entities/Common/Unit.md
- /entities/Common/VatRate.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/PurchaseOrder.md
referenced_by:
- /entities/Purchase/Inquiry.md
- /entities/Purchase/InquiryRow.md
---

# InquiryRows

Represents an inquiry row.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `InquiryRow`
- **Endpoint:** `GET /api/v1/Purchase/InquiryRows`
- **Required permission:** Show inquiry
- **GUID:** `1C7BE577-33A8-4CAF-9F52-16595EF161EB`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the row. |
| `Position` | `Int64?` | yes |  |  | The position of the row. |
| `OrderRowType` | `Int32` | no |  | enum | The row type. |
| `PartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the row's part. |
| `EntityIdentityString` | `String` | no |  | max length 20 | The human readable identifier of the row's entity. |
| `AdditionalRowDescription` | `String` | no |  | max length 80 | The additional row description of the row. |
| `FreeTextHtml` | `String` | no |  | max length 0 | The free text row's rich text HTML data. |
| `FreeText` | `String` | no |  | max length 0 | The free text row's raw text data. |
| `ParentRowId` | `Int64?` | yes | [InquiryRows](InquiryRow.md) |  | The business key identifier of the row's parent. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |  | The delivery date of the row. |
| `RevisionId` | `Int64?` | yes | [Revisions](../Common/Revision.md) |  | The business key identifier of the row's revision. |
| `Revision` | `Revisions` | no | [Revisions](../Common/Revision.md) | expandable | The revision of the row. |
| `OrderedQuantity` | `Decimal` | no |  |  | The ordered quantity of the row. |
| `Price` | `Decimal?` | yes |  |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's price currency. |
| `Discount` | `Decimal` | no |  |  | The discount specified on the row. |
| `ToolId` | `Int64?` | yes |  | **deprecated since 2.48** | The business key identifier of the row's tool. _(Replaced by Part)_ |
| `UnitId` | `Int64?` | yes | [Units](../Common/Unit.md) |  | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](../Common/Unit.md) | expandable | The unit of the row. |
| `VatRateId` | `Int64` | no | [VatRates](../Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the row's warehouse. |
| `WeightPerUnit` | `Decimal?` | yes |  |  | The weight per unit of the row. |
| `OrderDate` | `DateTimeOffset` | no |  |  | The order date of the row. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor of the row. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The row's price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the company currency. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |  | The row's setup price in the company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the company currency. |
| `StandardPrice` | `Decimal?` | yes |  |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's standard price currency. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes |  |  | The business key identifier of the row's setup price currency. |
| `ShowPrice` | `Boolean` | no |  |  | Specifies if price should be shown for the row. |
| `PartRowType` | `Int32` | no |  | enum | The part row type of the row. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the row. |
| `PartStatus` | `Int32?` | yes |  | enum | The part status of the row. |
| `OrderedQuantityInOrderUnit` | `Decimal` | no |  |  | The ordered quantity of the row in the order unit. |
| `ShowFreeTextIn` | `Int32` | no |  | bitmask, enum | Specifies which documents the free text data of the row should be projected on. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](../Common/StatisticalGoodsCode.md) |  | The business key identifier of the row's statistical goods code. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrder](PurchaseOrder.md) |  | The business key identifier of the purchase order that was created as a result of the row. |
| `ExemptFromStatistics` | `Boolean` | no |  |  | Specifies if the row should be exempted from statistics. |
| `ParentOrderId` | `Int64` | no | [Inquiries](Inquiry.md) | since 2.30 | The business key identifier of the rows parent inquiry. |
| `CodingId` | `Int64?` | yes | [Codings](../Accounting/Coding.md) | since 2.33 | The business key identifier of the rows coding. |
| `Coding` | `Codings` | no | [Codings](../Accounting/Coding.md) | expandable, since 2.33 | The coding of the row. |
| `RowIndex` | `Int32?` | yes |  | since 2.54 | The index of the row. |

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
| `Internal` | 0 |
| `Inquiry` | 1 |
| `Order` | 2 |
| `DeliverySchedule` | 4 |


## Referenced by

**Purchase**

- [Inquiries](Inquiry.md) — `Rows` (expand)
- [InquiryRows](InquiryRow.md) — `ParentRowId` (FK)


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
  "ShowFreeTextIn": 0,
  "StatisticalGoodsCodeId": null,
  "PurchaseOrderId": null,
  "ExemptFromStatistics": false,
  "ParentOrderId": 0,
  "CodingId": null,
  "Coding": null,
  "RowIndex": null
}
```
