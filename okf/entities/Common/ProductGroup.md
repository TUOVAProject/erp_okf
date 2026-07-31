---
type: API Entity
title: ProductGroups
description: Represents a product group.
resource: https://api.monitor.se/api/Monitor.API.Common.ProductGroup.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProductGroup.html
  title: Monitor API — ProductGroup
module: Common
api_class: ProductGroup
doc_name: ProductGroups
endpoint: GET /api/v1/Common/ProductGroups
guid: BABF8E12-DF95-405E-A3A2-6ABDF39D9984
permission: Show posting matrix
introduced_in: '2.18'
property_count: 5
referenced_by:
- /entities/Common/DiscountCategoryRow.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartTemplate.md
---

# ProductGroups

Represents a product group.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ProductGroup`
- **Endpoint:** `GET /api/v1/Common/ProductGroups`
- **Required permission:** Show posting matrix
- **GUID:** `BABF8E12-DF95-405E-A3A2-6ABDF39D9984`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the product group. |
| `Number` | `String` | no |  | unique, max length 10 | The product group number. |
| `Description` | `String` | no |  |  | The translated description of the product group. |
| `Alias` | `String` | no |  | max length 10 | The product group alias. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the product group is the default. |

## Referenced by

**Common**

- [DiscountCategoryRows](/entities/Common/DiscountCategoryRow.md) — `ProductGroupId` (FK)

**Inventory**

- [PartTemplates](/entities/Inventory/PartTemplate.md) — `ProductGroupId` (FK)
- [Parts](/entities/Inventory/Part.md) — `ProductGroup` (expand)
- [Parts](/entities/Inventory/Part.md) — `ProductGroupId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": null,
  "Description": null,
  "Alias": null,
  "IsDefault": false
}
```
