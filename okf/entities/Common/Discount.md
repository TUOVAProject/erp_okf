---
type: API Entity
title: Discounts
description: Represents a queryable discount.
resource: https://api.monitor.se/api/Monitor.API.Common.Discount.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Discount.html
  title: Monitor API — Discount
module: Common
api_class: Discount
doc_name: Discounts
endpoint: GET /api/v1/Common/Discounts
guid: 15E9F1CA-E360-4CBD-8293-D7737FB74959
permission: Show discounts
introduced_in: '24.8'
property_count: 9
referenced_by:
- /entities/Sales/CustomerOrderInvoiceOrderRowDiscount.md
- /entities/Sales/CustomerOrderOrderRowDiscount.md
- /entities/Sales/QuoteOrderRowDiscount.md
---

# Discounts

Represents a queryable discount.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `Discount`
- **Endpoint:** `GET /api/v1/Common/Discounts`
- **Required permission:** Show discounts
- **GUID:** `15E9F1CA-E360-4CBD-8293-D7737FB74959`
- **Introduced in:** 24.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the discount. |
| `Code` | `String` | no |  | max length 20 | The human readable identifier of the discount. |
| `Name` | `String` | no |  |  | The translated name of the discount. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the discount is active. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if this is the default discount for the discount type. |
| `DiscountForModule` | `Int32` | no |  | enum | The sales or purchase module of the discount. |
| `DiscountType` | `Int32` | no |  | enum | The type of the discount. |
| `Priority` | `Int32` | no |  |  | The priority of the discount. |
| `DiscountCalculationType` | `Int32` | no |  | enum | The calculation type of the discount. |

## Enumerations

### DiscountForModule

| Name | Value |
| --- | ---: |
| `Sales` | 0 |

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

- [CustomerOrderInvoiceOrderRowDiscounts](../Sales/CustomerOrderInvoiceOrderRowDiscount.md) — `DiscountId` (FK)
- [CustomerOrderOrderRowDiscounts](../Sales/CustomerOrderOrderRowDiscount.md) — `DiscountId` (FK)
- [QuoteOrderRowDiscounts](../Sales/QuoteOrderRowDiscount.md) — `DiscountId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Name": null,
  "IsActive": false,
  "IsDefault": false,
  "DiscountForModule": 0,
  "DiscountType": 0,
  "Priority": 0,
  "DiscountCalculationType": 0
}
```
