---
type: API Entity
title: CustomerPartLinks
description: Represents a customer part link.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerPartLink.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerPartLink.html
  title: Monitor API — CustomerPartLink
module: Sales
api_class: CustomerPartLink
doc_name: CustomerPartLinks
endpoint: GET /api/v1/Sales/CustomerPartLinks
guid: 41DF82F6-EC6E-4362-A780-91B00BDC8583
permission: Show customer
introduced_in: '2.18'
property_count: 28
references_out:
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/StaggeredPrice.md
- /entities/Common/Unit.md
- /entities/Inventory/Part.md
- /entities/Sales/Customer.md
referenced_by:
- /entities/Inventory/Part.md
- /entities/Sales/Customer.md
---

# CustomerPartLinks

Represents a customer part link.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerPartLink`
- **Endpoint:** `GET /api/v1/Sales/CustomerPartLinks`
- **Required permission:** Show customer
- **GUID:** `41DF82F6-EC6E-4362-A780-91B00BDC8583`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer part link. |
| `CustomerId` | `Int64` | no | [Customers](Customer.md) |  | The business key identifier of the customer part link customer. References Customers . |
| `CustomerPartNumber` | `String` | no |  |  | The part number that the customer uses to identify the part. |
| `PackagingPartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the customer part link packaging part. References Parts . |
| `Gs1Code` | `String` | no |  |  | The GS1 code of the customer part link. |
| `SalesCommentShowInForms` | `Int32` | no |  | bitmask, enum | Specifies which documents the sales comment of the part link will be shown on. |
| `QuantityForLeadTimeToCustomer` | `Decimal?` | yes |  |  | The quantity for lead time. |
| `PartId` | `Int64` | no | [Parts](../Inventory/Part.md) |  | The business key identifier of the customer part link's part. |
| `Price` | `Decimal?` | yes |  |  | The price of the customer part link. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the customer part link. |
| `LeadTime` | `TimeSpan?` | yes |  |  | The lead time of the customer part link. |
| `Discount` | `Decimal?` | yes |  |  | The discount percentage of the customer part link. |
| `PriceValidThrough` | `DateTimeOffset?` | yes |  |  | The date/time offset that the customer part link price is valid through. |
| `FuturePrice` | `Decimal?` | yes |  |  | The future price of the customer part link. |
| `FuturePriceValidThrough` | `DateTimeOffset?` | yes |  |  | The date/time offset that the future customer part link price is valid through. |
| `FutureSetupPrice` | `Decimal?` | yes |  |  | The future setup price of the customer part link. |
| `QuantityPerPackage` | `Decimal?` | yes |  |  | The quantity per package of the customer part link. |
| `PickingCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the customer part link picking comment. References Comments . |
| `PickingComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The customer part link picking comment. |
| `OverrideSalesCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the customer part link override sales comment. References Comments . |
| `OverrideSalesComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The customer part link override sales comment. |
| `UnitId` | `Int64` | no | [Units](../Common/Unit.md) |  | The business key identifier of the customer part link unit. References Units . |
| `Unit` | `Units` | no | [Units](../Common/Unit.md) | expandable | The customer part link unit. |
| `PriceCurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the customer part link price currency. References Currencies . |
| `PriceCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The customer part link price currency. |
| `PriceCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifer of the customer part link price comment. References Comments . |
| `PriceComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The customer part link price comment. |
| `StaggeredPrices` | `StaggeredPrices[]` | no | [StaggeredPrices](../Common/StaggeredPrice.md) | expandable, collection, since 24.3 | The staggered prices on the part link. |

## Enumerations

### SalesCommentShowInForms (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Quote` | 1 |
| `Acknowledgement` | 2 |
| `DeliveryNote` | 4 |
| `Invoice` | 8 |
| `ProFormaInvoice` | 16 |


## Referenced by

**Inventory**

- [Parts](../Inventory/Part.md) — `CustomerPartLinks` (expand)

**Sales**

- [Customers](Customer.md) — `CustomerPartLinks` (expand)


## Example

```json
{
  "Id": 0,
  "CustomerId": 0,
  "CustomerPartNumber": null,
  "PackagingPartId": null,
  "Gs1Code": null,
  "SalesCommentShowInForms": 0,
  "QuantityForLeadTimeToCustomer": null,
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
  "PickingCommentId": null,
  "PickingComment": null,
  "OverrideSalesCommentId": null,
  "OverrideSalesComment": null,
  "UnitId": 0,
  "Unit": null,
  "PriceCurrencyId": 0,
  "PriceCurrency": null,
  "PriceCommentId": null,
  "PriceComment": null,
  "StaggeredPrices": null
}
```
