---
type: API Entity
title: CustomerOrderInvoiceOrderRowDiscounts
description: Represents a discount row for a customer order invoice row.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderInvoiceOrderRowDiscount.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderInvoiceOrderRowDiscount.html
  title: Monitor API — CustomerOrderInvoiceOrderRowDiscount
module: Sales
api_class: CustomerOrderInvoiceOrderRowDiscount
doc_name: CustomerOrderInvoiceOrderRowDiscounts
endpoint: GET /api/v1/Sales/CustomerOrderInvoiceOrderRowDiscounts
guid: F8067DA0-958B-4AF5-8481-2F49EA16F4D8
permission: Show customer orders
introduced_in: '24.8'
property_count: 15
references_out:
- /entities/Common/Currency.md
- /entities/Common/Discount.md
- /entities/Sales/CustomerOrderInvoiceRow.md
referenced_by:
- /entities/Sales/CustomerOrderInvoiceRow.md
---

# CustomerOrderInvoiceOrderRowDiscounts

Represents a discount row for a customer order invoice row.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerOrderInvoiceOrderRowDiscount`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderInvoiceOrderRowDiscounts`
- **Required permission:** Show customer orders
- **GUID:** `F8067DA0-958B-4AF5-8481-2F49EA16F4D8`
- **Introduced in:** 24.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the discount row. |
| `OrderRowId` | `Int64` | no | [CustomerOrderInvoiceRows](CustomerOrderInvoiceRow.md) |  | The business key identifier of the discount row's invoice row. |
| `DiscountId` | `Int64?` | yes | [Discounts](../Common/Discount.md) |  | The business key identifier of the discount row's discount. |
| `AsPercent` | `Decimal?` | yes |  |  | The discount amount as percent of the discount row. |
| `DiscountLockedFromAutomaticChanges` | `Boolean` | no |  |  | Specifies if the discount is locked from automatic changes. |
| `AsAmount` | `Decimal?` | yes |  |  | The discount amount of the discount row. |
| `AsAmountCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the discount row's amount currency. |
| `DiscountType` | `Int32` | no |  | enum | The discount type of the discount row. |
| `GrossPrice` | `Decimal?` | yes |  |  | The gross price of the discount row. |
| `GrossPriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the discount row's gross price currency. |
| `NetPrice` | `Decimal?` | yes |  |  | The net price of the discount row. |
| `NetPriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the discount row's net price currency. |
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

- [CustomerOrderInvoiceRows](CustomerOrderInvoiceRow.md) — `DiscountRows` (expand)


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
