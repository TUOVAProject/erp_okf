---
type: API Entity
title: SalesPrices
description: Represents a sales price.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesPrice.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesPrice.html
  title: Monitor API — SalesPrice
module: Sales
api_class: SalesPrice
doc_name: SalesPrices
endpoint: GET /api/v1/Sales/SalesPrices
guid: D12C7407-B8AE-47EE-9285-953CC360A022
permission: Show part
introduced_in: '2.34'
property_count: 20
references_out:
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/PriceList.md
- /entities/Common/StaggeredPrice.md
- /entities/Inventory/Part.md
---

# SalesPrices

Represents a sales price.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `SalesPrice`
- **Endpoint:** `GET /api/v1/Sales/SalesPrices`
- **Required permission:** Show part
- **GUID:** `D12C7407-B8AE-47EE-9285-953CC360A022`
- **Introduced in:** 2.34

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the sales price. |
| `PartId` | `Int64` | no | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the part the sales price belongs to. |
| `PriceListId` | `Int64` | no | [PriceLists](/entities/Common/PriceList.md) |  | The business key identifier of the price list the sales price belongs to. |
| `Price` | `Decimal?` | yes |  |  | The price on the sales price. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency for the price on the sales price. |
| `PriceCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The currency for the price on the sales price. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price on the sales price. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency for the setup price on the sales price. |
| `SetupPriceCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The currency for the setup price on the sales price. |
| `ValidThrough` | `DateTimeOffset?` | yes |  |  | The valid through date on the sales price. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the sales price's comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the sales price. |
| `FuturePrice` | `Decimal?` | yes |  |  | The future price on the sales price. |
| `FuturePriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency for the future price on the sales price. |
| `FuturePriceCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The currency for the future price on the sales price. |
| `FutureSetupPrice` | `Decimal?` | yes |  |  | The future setup price on the sales price. |
| `FutureSetupPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency for the future setup price on the sales price. |
| `FutureSetupPriceCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The currency for the future setup price on the sales price. |
| `FuturePriceValidThrough` | `DateTimeOffset?` | yes |  |  | The future valid through date on the sales price. |
| `StaggeredPrices` | `StaggeredPrices[]` | no | [StaggeredPrices](/entities/Common/StaggeredPrice.md) | expandable, collection | The staggered prices on the sales price. |

## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "PriceListId": 0,
  "Price": null,
  "PriceCurrencyId": null,
  "PriceCurrency": null,
  "SetupPrice": null,
  "SetupPriceCurrencyId": null,
  "SetupPriceCurrency": null,
  "ValidThrough": null,
  "CommentId": null,
  "Comment": null,
  "FuturePrice": null,
  "FuturePriceCurrencyId": null,
  "FuturePriceCurrency": null,
  "FutureSetupPrice": null,
  "FutureSetupPriceCurrencyId": null,
  "FutureSetupPriceCurrency": null,
  "FuturePriceValidThrough": null,
  "StaggeredPrices": null
}
```
