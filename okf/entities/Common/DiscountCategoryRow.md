---
type: API Entity
title: DiscountCategoryRows
description: Represents a discount category row.
resource: https://api.monitor.se/api/Monitor.API.Common.DiscountCategoryRow.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.DiscountCategoryRow.html
  title: Monitor API — DiscountCategoryRow
module: Common
api_class: DiscountCategoryRow
doc_name: DiscountCategoryRows
endpoint: GET /api/v1/Common/DiscountCategoryRows
guid: A470E2F9-DB36-433A-8F23-FC0F0CED1947
permission: Show discount categories
introduced_in: '22.7'
property_count: 26
references_out:
- /entities/Common/DiscountCategory.md
- /entities/Common/ProductGroup.md
- /entities/Inventory/PartCode.md
referenced_by:
- /entities/Common/DiscountCategory.md
---

# DiscountCategoryRows

Represents a discount category row.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `DiscountCategoryRow`
- **Endpoint:** `GET /api/v1/Common/DiscountCategoryRows`
- **Required permission:** Show discount categories
- **GUID:** `A470E2F9-DB36-433A-8F23-FC0F0CED1947`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the row. |
| `DiscountCategoryId` | `Int64` | no | [DiscountCategories](DiscountCategory.md) |  | The business key identifier of the discount category this row belongs to. |
| `BoundaryType` | `Int32` | no |  | enum | The boundary type of the row. |
| `ProductGroupId` | `Int64?` | yes | [ProductGroups](ProductGroup.md) |  | The business key identifier of the product group for this row. |
| `PartCodeId` | `Int64?` | yes | [PartCodes](../Inventory/PartCode.md) |  | The business key identifier of the part code for this row. |
| `PartCategory` | `String` | no |  | max length 20 | The part category for this row. |
| `Boundary1` | `Decimal` | no |  |  | The first boundary of this row. |
| `Discount1` | `Decimal` | no |  |  | The discount for the first boundary of this row. |
| `Boundary2` | `Decimal` | no |  |  | The second boundary of this row. |
| `Discount2` | `Decimal` | no |  |  | The discount for the second boundary of this row. |
| `Boundary3` | `Decimal` | no |  |  | The third boundary of this row. |
| `Discount3` | `Decimal` | no |  |  | The discount for the third boundary of this row. |
| `Boundary4` | `Decimal` | no |  |  | The fourth boundary of this row. |
| `Discount4` | `Decimal` | no |  |  | The discount for the fourth boundary of this row. |
| `Boundary5` | `Decimal` | no |  |  | The fifth boundary of this row. |
| `Discount5` | `Decimal` | no |  |  | The discount for the fifth boundary of this row. |
| `Boundary6` | `Decimal` | no |  |  | The sixth boundary of this row. |
| `Discount6` | `Decimal` | no |  |  | The discount for the sixth boundary of this row. |
| `Boundary7` | `Decimal` | no |  |  | The seventh boundary of this row. |
| `Discount7` | `Decimal` | no |  |  | The discount for the seventh boundary of this row. |
| `Boundary8` | `Decimal` | no |  |  | The eighth boundary of this row. |
| `Discount8` | `Decimal` | no |  |  | The discount for the eighth boundary of this row. |
| `Boundary9` | `Decimal` | no |  |  | The ninth boundary of this row. |
| `Discount9` | `Decimal` | no |  |  | The discount for the ninth boundary of this row. |
| `Boundary10` | `Decimal` | no |  |  | The tenth boundary of this row. |
| `Discount10` | `Decimal` | no |  |  | The discount for the tenth boundary of this row. |

## Enumerations

### BoundaryType

| Name | Value |
| --- | ---: |
| `Quantity` | 0 |
| `Value` | 1 |


## Referenced by

**Common**

- [DiscountCategories](DiscountCategory.md) — `Rows` (expand)


## Example

```json
{
  "Id": 0,
  "DiscountCategoryId": 0,
  "BoundaryType": 0,
  "ProductGroupId": null,
  "PartCodeId": null,
  "PartCategory": null,
  "Boundary1": 0.0,
  "Discount1": 0.0,
  "Boundary2": 0.0,
  "Discount2": 0.0,
  "Boundary3": 0.0,
  "Discount3": 0.0,
  "Boundary4": 0.0,
  "Discount4": 0.0,
  "Boundary5": 0.0,
  "Discount5": 0.0,
  "Boundary6": 0.0,
  "Discount6": 0.0,
  "Boundary7": 0.0,
  "Discount7": 0.0,
  "Boundary8": 0.0,
  "Discount8": 0.0,
  "Boundary9": 0.0,
  "Discount9": 0.0,
  "Boundary10": 0.0,
  "Discount10": 0.0
}
```
