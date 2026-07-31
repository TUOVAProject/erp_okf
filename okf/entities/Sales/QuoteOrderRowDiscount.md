---
type: API Entity
title: QuoteOrderRowDiscounts
description: Represents a discount row for a quote row.
resource: https://api.monitor.se/api/Monitor.API.Sales.QuoteOrderRowDiscount.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.QuoteOrderRowDiscount.html
  title: Monitor API — QuoteOrderRowDiscount
module: Sales
api_class: QuoteOrderRowDiscount
doc_name: QuoteOrderRowDiscounts
endpoint: GET /api/v1/Sales/QuoteOrderRowDiscounts
guid: B95A981B-B37F-4B45-880B-9E6F5ADAB385
permission: Show quote
introduced_in: '24.8'
property_count: 15
references_out:
- /entities/Common/Currency.md
- /entities/Common/Discount.md
- /entities/Sales/QuoteRow.md
referenced_by:
- /entities/Sales/QuoteRow.md
---

# QuoteOrderRowDiscounts

Represents a discount row for a quote row.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `QuoteOrderRowDiscount`
- **Endpoint:** `GET /api/v1/Sales/QuoteOrderRowDiscounts`
- **Required permission:** Show quote
- **GUID:** `B95A981B-B37F-4B45-880B-9E6F5ADAB385`
- **Introduced in:** 24.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the discount row. |
| `OrderRowId` | `Int64` | no | [QuoteRows](/entities/Sales/QuoteRow.md) |  | The business key identifier of the discount row's quote row. |
| `DiscountId` | `Int64?` | yes | [Discounts](/entities/Common/Discount.md) |  | The business key identifier of the discount row's discount. |
| `AsPercent` | `Decimal?` | yes |  |  | The discount amount as percent of the discount row. |
| `DiscountLockedFromAutomaticChanges` | `Boolean` | no |  |  | Specifies if the discount is locked from automatic changes. |
| `AsAmount` | `Decimal?` | yes |  |  | The discount amount of the discount row. |
| `AsAmountCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the discount row's amount currency. |
| `DiscountType` | `Int32` | no |  | enum | The discount type of the discount row. |
| `GrossPrice` | `Decimal?` | yes |  |  | The gross price of the discount row. |
| `GrossPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the discount row's gross price currency. |
| `NetPrice` | `Decimal?` | yes |  |  | The net price of the discount row. |
| `NetPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the discount row's net price currency. |
| `DiscountCalculationType` | `Int32` | no |  | enum | The discount calculation type of the discount row. |
| `Priority` | `Int32` | no |  |  | The priority of the discount row. |
| `ReplacesDiscountFieldOnOrderRow` | `Boolean` | no |  |  | Specifies if this discount row represents the discount which could be applied to the discount field on the order row itself before order multiple discounts on order rows were introduced. |

## Enumerations

### DiscountType

| Name | Value |
| --- | ---: |
| `Discount` | 0 |
| `OrderDiscount` | 1 |
| `TotalRowDiscount` | 2 |
| `ProjectDiscount` | 3 |
| `CustomerDiscountOnDiscount` | 4 |
| `OrderTypeDiscount` | 5 |
| `ManualDiscount` | 99 |

### DiscountCalculationType

| Name | Value |
| --- | ---: |
| `Percent` | 1 |
| `Amount` | 2 |


## Referenced by

**Sales**

- [QuoteRows](/entities/Sales/QuoteRow.md) — `DiscountRows` (expand)


## Example

```json
{
  "Id": 0,
  "OrderRowId": 0,
  "DiscountId": null,
  "AsPercent": null,
  "DiscountLockedFromAutomaticChanges": false,
  "AsAmount": null,
  "AsAmountCurrencyId": null,
  "DiscountType": 0,
  "GrossPrice": null,
  "GrossPriceCurrencyId": null,
  "NetPrice": null,
  "NetPriceCurrencyId": null,
  "DiscountCalculationType": 0,
  "Priority": 0,
  "ReplacesDiscountFieldOnOrderRow": false
}
```
