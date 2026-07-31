---
type: API Entity
title: SupplierPartLinks
description: Represents a supplier part link.
resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierPartLink.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierPartLink.html
  title: Monitor API — SupplierPartLink
module: Purchase
api_class: SupplierPartLink
doc_name: SupplierPartLinks
endpoint: GET /api/v1/Purchase/SupplierPartLinks
guid: EC4715C4-9F65-493C-8872-442DB47B7562
permission: Show supplier
introduced_in: '2.18'
property_count: 29
references_out:
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/Unit.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartPurchaseExpenseValues.md
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Inventory/Part.md
- /entities/Inventory/PartPlanningInformation.md
- /entities/Purchase/Supplier.md
---

# SupplierPartLinks

Represents a supplier part link.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `SupplierPartLink`
- **Endpoint:** `GET /api/v1/Purchase/SupplierPartLinks`
- **Required permission:** Show supplier
- **GUID:** `EC4715C4-9F65-493C-8872-442DB47B7562`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the supplier part link. |
| `SupplierId` | `Int64` | no | [Suppliers](/entities/Purchase/Supplier.md) |  | The business key identifier of the supplier part link supplier. |
| `SupplierPartNumber` | `String` | no |  |  | The supplier part link part number. |
| `PurchaseCommentShowInForms` | `Int32` | no |  | bitmask, enum | Specifies on which forms the purchase comment should be shown. |
| `IncludeAlloyCostOnPurchaseOrder` | `Boolean` | no |  |  | Include alloy cost on purchase orders for this supplier part link. |
| `PartId` | `Int64` | no | [Part](/entities/Inventory/Part.md) |  | The business key identifier of the supplier part link part. |
| `Price` | `Decimal?` | yes |  |  | The price of the supplier link part. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the supplier link part. |
| `LeadTime` | `TimeSpan?` | yes |  |  | The lead time of the supplier part link in work days. |
| `Discount` | `Decimal?` | yes |  |  | The discount of the supplier part link. |
| `PriceValidThrough` | `DateTimeOffset?` | yes |  |  | The valid through date of the supplier part link price. |
| `FuturePrice` | `Decimal?` | yes |  |  | The future price of the supplier part link. |
| `FuturePriceValidThrough` | `DateTimeOffset?` | yes |  |  | The valid through date of the supplier part link future price. |
| `FutureSetupPrice` | `Decimal?` | yes |  |  | The future setup price of the supplier part link. |
| `QuantityPerPackage` | `Decimal?` | yes |  |  | The quantity per package of the supplier part link. |
| `OverridePurchaseCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the supplier part link override purchase comment. |
| `OverridePurchaseComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The supplier part link override purchase comment. |
| `UnitId` | `Int64` | no | [Units](/entities/Common/Unit.md) |  | The business key identifier of the supplier part link unit. |
| `Unit` | `Units` | no | [Units](/entities/Common/Unit.md) | expandable | The supplier part link unit. |
| `PriceCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the supplier part link price currency. |
| `PriceCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The supplier part link price currency. |
| `PriceCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the supplier part link price comment. |
| `PriceComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The supplier part link price comment. |
| `Brand` | `String` | no |  | max length 80, since 2.47 | The brand of the supplier part link. |
| `Storage` | `String` | no |  | max length 35, since 2.47 | The storage of the supplier part link. |
| `Dock` | `String` | no |  | max length 35, since 2.47 | The dock of the supplier part link. |
| `IsRemoteConfigured` | `Boolean` | no |  | since 23.2 | Specifies if the part is remote configured via the transfer profile connected to the supplier. |
| `PartPurchaseExpenseValuesId` | `Int64?` | yes | [PartPurchaseExpenseValues](/entities/Inventory/PartPurchaseExpenseValues.md) | since 26.6 | The business key identitier of the supplier part link purchase expense values. |
| `PartPurchaseExpenseValues` | `PartPurchaseExpenseValues` | no | [PartPurchaseExpenseValues](/entities/Inventory/PartPurchaseExpenseValues.md) | expandable, since 26.6 | The supplier part link purchase expense values. |

## Enumerations

### PurchaseCommentShowInForms (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `Internal` | 0 |
| `Inquiry` | 1 |
| `Order` | 2 |
| `DeliverySchedule` | 4 |


## Referenced by

**Inventory**

- [PartPlanningInformation](/entities/Inventory/PartPlanningInformation.md) — `ActiveSupplierPartLink` (expand)
- [PartPlanningInformation](/entities/Inventory/PartPlanningInformation.md) — `ActiveSupplierPartLinkId` (FK)
- [Parts](/entities/Inventory/Part.md) — `SupplierPartLinks` (expand)

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `SupplierPartLinks` (expand)


## Example

```json
{
  "Id": 0,
  "SupplierId": 0,
  "SupplierPartNumber": null,
  "PurchaseCommentShowInForms": 0,
  "IncludeAlloyCostOnPurchaseOrder": false,
  "PartId": 0,
  "Price": null,
  "SetupPrice": null,
  "LeadTime": null,
  "Discount": null,
  "PriceValidThrough": null,
  "FuturePrice": null,
  "FuturePriceValidThrough": null,
  "FutureSetupPrice": null,
  "QuantityPerPackage": null,
  "OverridePurchaseCommentId": null,
  "OverridePurchaseComment": null,
  "UnitId": 0,
  "Unit": null,
  "PriceCurrencyId": 0,
  "PriceCurrency": null,
  "PriceCommentId": null,
  "PriceComment": null,
  "Brand": null,
  "Storage": null,
  "Dock": null,
  "IsRemoteConfigured": false,
  "PartPurchaseExpenseValuesId": null,
  "PartPurchaseExpenseValues": null
}
```
