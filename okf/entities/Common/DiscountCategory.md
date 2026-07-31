---
type: API Entity
title: DiscountCategories
description: Represents a queryable discount category.
resource: https://api.monitor.se/api/Monitor.API.Common.DiscountCategory.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.DiscountCategory.html
  title: Monitor API — DiscountCategory
module: Common
api_class: DiscountCategory
doc_name: DiscountCategories
endpoint: GET /api/v1/Common/DiscountCategories
guid: 83F9058E-F78C-49FB-958E-75747687E0B0
permission: Show discount categories
introduced_in: '2.18'
property_count: 5
references_out:
- /entities/Common/DiscountCategoryRow.md
referenced_by:
- /entities/Common/DiscountCategoryRow.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
---

# DiscountCategories

Represents a queryable discount category.

- **Module:** [Common](/modules/Common.md)
- **API class:** `DiscountCategory`
- **Endpoint:** `GET /api/v1/Common/DiscountCategories`
- **Required permission:** Show discount categories
- **GUID:** `83F9058E-F78C-49FB-958E-75747687E0B0`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the discount category. |
| `Number` | `String` | no |  | unique, max length 10 | The discount category number. |
| `Description` | `String` | no |  |  | The translated description of the discount category. |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |
| `Rows` | `DiscountCategoryRows[]` | no | [DiscountCategoryRows](/entities/Common/DiscountCategoryRow.md) | expandable, collection, since 22.7 | The rows for the discount category. |

## Referenced by

**Common**

- [DiscountCategoryRows](/entities/Common/DiscountCategoryRow.md) — `DiscountCategoryId` (FK)

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `DiscountCategory` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `DiscountCategoryId` (FK)

**Sales**

- [Customers](/entities/Sales/Customer.md) — `DiscountCategory` (expand)
- [Customers](/entities/Sales/Customer.md) — `DiscountCategoryId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": null,
  "Description": null,
  "CompanyIds": null,
  "Rows": null
}
```
