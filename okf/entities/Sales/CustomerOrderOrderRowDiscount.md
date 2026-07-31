---
type: API Entity
title: CustomerOrderOrderRowDiscounts
description: Represents a discount row for a customer order row.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderOrderRowDiscount.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderOrderRowDiscount.html
  title: Monitor API — CustomerOrderOrderRowDiscount
module: Sales
api_class: CustomerOrderOrderRowDiscount
doc_name: CustomerOrderOrderRowDiscounts
endpoint: GET /api/v1/Sales/CustomerOrderOrderRowDiscounts
guid: 9280A5CE-3778-4C70-9238-8280AD77A8DB
permission: Show customer orders
introduced_in: '24.8'
property_count: 15
references_out:
- /entities/Common/Currency.md
- /entities/Common/Discount.md
- /entities/Sales/CustomerOrderRow.md
referenced_by:
- /entities/Sales/CustomerOrderRow.md
---

# CustomerOrderOrderRowDiscounts

Represents a discount row for a customer order row.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `CustomerOrderOrderRowDiscount`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderOrderRowDiscounts`
- **Required permission:** Show customer orders
- **GUID:** `9280A5CE-3778-4C70-9238-8280AD77A8DB`
- **Introduced in:** 24.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the discount row. |
| `OrderRowId` | `Int64` | no | [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) |  | The business key identifier of the discount row's customer order row. |
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

- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `DiscountRows` (expand)


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
