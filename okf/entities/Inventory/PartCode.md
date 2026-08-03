---
type: API Entity
title: PartCodes
description: Represents a part code.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartCode.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartCode.html
  title: Monitor API — PartCode
module: Inventory
api_class: PartCode
doc_name: PartCodes
endpoint: GET /api/v1/Inventory/PartCodes
guid: D8FF7E9E-0606-495A-958D-7045E23AAB93
permission: Show basic data for part
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Common/DiscountCategoryRow.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartTemplate.md
---

# PartCodes

Represents a part code.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PartCode`
- **Endpoint:** `GET /api/v1/Inventory/PartCodes`
- **Required permission:** Show basic data for part
- **GUID:** `D8FF7E9E-0606-495A-958D-7045E23AAB93`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part code. |
| `Code` | `String` | no |  | unique, max length 6 | The human readable identifier of the part code. |
| `Description` | `String` | no |  |  | The translated description of the part code. |
| `Alias` | `String` | no |  | max length 6 | The human readable alias code of the part code. |

## Referenced by

**Common**

- [DiscountCategoryRows](../Common/DiscountCategoryRow.md) — `PartCodeId` (FK)

**Inventory**

- [PartTemplates](PartTemplate.md) — `PartCodeId` (FK)
- [Parts](Part.md) — `PartCode` (expand)
- [Parts](Part.md) — `PartCodeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "Alias": null
}
```
