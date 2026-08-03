---
type: API Entity
title: PriceLists
description: Represents a price list.
resource: https://api.monitor.se/api/Monitor.API.Common.PriceList.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PriceList.html
  title: Monitor API — PriceList
module: Common
api_class: PriceList
doc_name: PriceLists
endpoint: GET /api/v1/Common/PriceLists
guid: 860576DC-266D-4341-A268-04A3606E695C
permission: Show price lists
introduced_in: '2.18'
property_count: 8
references_out:
- /entities/Common/Currency.md
- /entities/Common/PriceList.md
referenced_by:
- /entities/Common/PriceList.md
- /entities/Inventory/PriceChangeLog.md
- /entities/Purchase/BlanketOrderPurchaseRow.md
- /entities/Sales/BlanketOrderSalesRow.md
- /entities/Sales/BlanketOrderSalesType.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrderType.md
- /entities/Sales/QuoteType.md
- /entities/Sales/SalesAgreementType.md
- /entities/Sales/SalesPrice.md
---

# PriceLists

Represents a price list.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `PriceList`
- **Endpoint:** `GET /api/v1/Common/PriceLists`
- **Required permission:** Show price lists
- **GUID:** `860576DC-266D-4341-A268-04A3606E695C`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the price list. |
| `Number` | `Int64` | no |  |  | The price list number. |
| `Description` | `String` | no |  |  | The translated description of the price list. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor of the price list. |
| `ParentPriceListId` | `Int64?` | yes | [PriceLists](PriceList.md) |  | The business key identifier of the price list's parent. References PriceLists . |
| `CurrencyId` | `Int64` | no | [Currencies](Currency.md) |  | The business key identifier of the price list's currency. References Currencies . |
| `PriceListBasis` | `Int32` | no |  | enum | Specifies the basis of the price list. |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |

## Enumerations

### PriceListBasis

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `ParentPriceList` | 1 |
| `StandardPrice` | 2 |


## Referenced by

**Common**

- [PriceLists](PriceList.md) — `ParentPriceListId` (FK)

**Inventory**

- [PriceChangeLogs](../Inventory/PriceChangeLog.md) — `PriceListId` (FK)

**Purchase**

- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `PriceOriginPriceListId` (FK)

**Sales**

- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `PriceOriginPriceListId` (FK)
- [BlanketOrderSalesTypes](../Sales/BlanketOrderSalesType.md) — `PriceListId` (FK)
- [CustomerOrderTypes](../Sales/CustomerOrderType.md) — `PriceListId` (FK)
- [Customers](../Sales/Customer.md) — `ConfigurationPriceListId` (FK)
- [Customers](../Sales/Customer.md) — `PriceListId` (FK)
- [QuoteTypes](../Sales/QuoteType.md) — `PriceListId` (FK)
- [SalesAgreementTypes](../Sales/SalesAgreementType.md) — `PriceListId` (FK)
- [SalesPrices](../Sales/SalesPrice.md) — `PriceListId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "ConversionFactor": 0.0,
  "ParentPriceListId": null,
  "CurrencyId": 0,
  "PriceListBasis": 0,
  "CompanyIds": null
}
```
