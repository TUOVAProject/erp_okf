---
type: API Entity
title: BlanketOrderPurchaseRows
description: Represents a blanket order row for purchase.
resource: https://api.monitor.se/api/Monitor.API.Purchase.BlanketOrderPurchaseRow.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.BlanketOrderPurchaseRow.html
  title: Monitor API — BlanketOrderPurchaseRow
module: Purchase
api_class: BlanketOrderPurchaseRow
doc_name: BlanketOrderPurchaseRows
endpoint: GET /api/v1/Purchase/BlanketOrderPurchaseRows
guid: F974CE48-5739-40B2-8356-0D4EAD667222
permission: Show blanket order
introduced_in: '23.8'
property_count: 38
references_out:
- /entities/Common/Currency.md
- /entities/Common/PriceList.md
- /entities/Common/Revision.md
- /entities/Common/Unit.md
- /entities/Common/VatRate.md
- /entities/Inventory/Part.md
- /entities/Purchase/BlanketOrderPurchase.md
- /entities/Purchase/BlanketOrderPurchaseRow.md
referenced_by:
- /entities/Purchase/BlanketOrderPurchase.md
- /entities/Purchase/BlanketOrderPurchaseRow.md
- /entities/Purchase/PurchaseOrderRow.md
---

# BlanketOrderPurchaseRows

Represents a blanket order row for purchase.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `BlanketOrderPurchaseRow`
- **Endpoint:** `GET /api/v1/Purchase/BlanketOrderPurchaseRows`
- **Required permission:** Show blanket order
- **GUID:** `F974CE48-5739-40B2-8356-0D4EAD667222`
- **Introduced in:** 23.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the blanket order row. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the row. |
| `ParentOrderId` | `Int64?` | yes | [BlanketOrderPurchases](BlanketOrderPurchase.md) |  | The business key identifier of the row's blanket order. |
| `ParentRowId` | `Int64?` | yes | [BlanketOrderPurchaseRows](BlanketOrderPurchaseRow.md) |  | The business key identifier of the row's parent row. |
| `SupplierPartNumber` | `String` | no |  | max length 50 | The supplier's part number of the row. |
| `Position` | `Int64?` | yes |  |  | The position of the row. |
| `OrderRowType` | `Int32` | no |  | enum | The order row type of the row. |
| `PartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the row's part. |
| `Part` | `Parts` | no | [Parts](../Inventory/Part.md) | expandable | The part of the row. |
| `PartRowType` | `Int32` | no |  | enum | The part row type of the row. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the row. |
| `UnitId` | `Int64?` | yes | [Units](../Common/Unit.md) |  | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](../Common/Unit.md) | expandable | The unit of the row. |
| `Price` | `Decimal?` | yes |  |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's price currency. |
| `PriceCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The price currency of the row. |
| `PriceOriginPriceListId` | `Int64?` | yes | [PriceLists](../Common/PriceList.md) |  | The business key identifier of the row's price origin price list. |
| `PriceLockedFromAutomaticChanges` | `Boolean?` | yes |  |  | Specifies if the row have price locked from automatic changes. |
| `PriceIsFuturePrice` | `Boolean?` | yes |  |  | Specifies if the row's price is future price. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The price in company currency of the row. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's company currency used in price in company currency. |
| `PriceInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The company currency used in price in company currency of the row. |
| `Discount` | `Decimal` | no |  |  | The discount of the row. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's setup price currency. |
| `SetupPriceCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The setup price currency of the row. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |  | The setup price in company currency of the row. |
| `VatRateId` | `Int64?` | yes | [VatRates](../Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `VatRate` | `VatRates` | no | [VatRates](../Common/VatRate.md) | expandable | The VAT rate of the row. |
| `ShowFreeTextIn` | `Int32` | no |  | bitmask, enum | Specifies where the row's free text should be visible. |
| `ValidThrough` | `DateTimeOffset?` | yes |  |  | The requirement date of the row. |
| `RevisionId` | `Int64?` | yes | [Revisions](../Common/Revision.md) |  | The business key identifier of the row's revision. |
| `Revision` | `Revisions` | no | [Revisions](../Common/Revision.md) | expandable | The revision of the row. |
| `FreeTextHtml` | `String` | no |  |  | The free text in HTML format of the row. |
| `FreeText` | `String` | no |  |  | The free text of the row. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor of the row. |
| `QuantityRatio` | `Decimal?` | yes |  |  | The quantity ratio of the row. |
| `AdditionalRowDescription` | `String` | no |  |  | The additional row description of the row. |

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
| `Internal` | 0 |
| `Inquiry` | 1 |
| `Order` | 2 |
| `DeliverySchedule` | 4 |


## Referenced by

**Purchase**

- [BlanketOrderPurchaseRows](BlanketOrderPurchaseRow.md) — `ParentRowId` (FK)
- [BlanketOrderPurchases](BlanketOrderPurchase.md) — `Rows` (expand)
- [PurchaseOrderRows](PurchaseOrderRow.md) — `BlanketOrderPurchaseRowId` (FK)


## Example

```json
{
  "Id": 0,
  "LifeCycleState": 0,
  "ParentOrderId": null,
  "ParentRowId": null,
  "SupplierPartNumber": null,
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
  "AdditionalRowDescription": null
}
```
