---
type: API Entity
title: SalesOverheadMarkups
description: Represents sales overhead markup.
resource: https://api.monitor.se/api/Monitor.API.Inventory.SalesOverheadMarkup.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.SalesOverheadMarkup.html
  title: Monitor API — SalesOverheadMarkup
module: Inventory
api_class: SalesOverheadMarkup
doc_name: SalesOverheadMarkups
endpoint: GET /api/v1/Inventory/SalesOverheadMarkups
guid: F386809E-2433-4823-B979-8221E8310428
permission: Show calculation mark-up
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Inventory/Part.md
- /entities/Inventory/PartTemplate.md
---

# SalesOverheadMarkups

Represents sales overhead markup.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `SalesOverheadMarkup`
- **Endpoint:** `GET /api/v1/Inventory/SalesOverheadMarkups`
- **Required permission:** Show calculation mark-up
- **GUID:** `F386809E-2433-4823-B979-8221E8310428`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the sales overhead markup. |
| `Number` | `Int32` | no |  |  | The human readable number of the sales overhead markup. |
| `Description` | `String` | no |  |  | The translated description of the sales overhead markup. |
| `Markup` | `Decimal` | no |  |  | The markup defined by the sales overhead markup. |

## Referenced by

**Inventory**

- [PartTemplates](/entities/Inventory/PartTemplate.md) — `SalesOverheadMarkupId` (FK)
- [Parts](/entities/Inventory/Part.md) — `SalesOverheadMarkup` (expand)
- [Parts](/entities/Inventory/Part.md) — `SalesOverheadMarkupId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "Markup": 0.0
}
```
