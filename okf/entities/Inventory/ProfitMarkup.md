---
type: API Entity
title: ProfitMarkups
description: Represents profit markup.
resource: https://api.monitor.se/api/Monitor.API.Inventory.ProfitMarkup.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.ProfitMarkup.html
  title: Monitor API — ProfitMarkup
module: Inventory
api_class: ProfitMarkup
doc_name: ProfitMarkups
endpoint: GET /api/v1/Inventory/ProfitMarkups
guid: 82791BC5-491D-4D1A-8BDB-3F4A7ECB5907
permission: Show calculation mark-up
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Inventory/Part.md
- /entities/Inventory/PartTemplate.md
---

# ProfitMarkups

Represents profit markup.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `ProfitMarkup`
- **Endpoint:** `GET /api/v1/Inventory/ProfitMarkups`
- **Required permission:** Show calculation mark-up
- **GUID:** `82791BC5-491D-4D1A-8BDB-3F4A7ECB5907`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the profit markup. |
| `Number` | `Int32` | no |  |  | The human readable number of the profit markup. |
| `Description` | `String` | no |  |  | The translated description of the profit markup. |
| `Markup` | `Decimal` | no |  |  | The markup defined by the profit markup. |

## Referenced by

**Inventory**

- [PartTemplates](/entities/Inventory/PartTemplate.md) — `ProfitMarkupId` (FK)
- [Parts](/entities/Inventory/Part.md) — `ProfitMarkup` (expand)
- [Parts](/entities/Inventory/Part.md) — `ProfitMarkupId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "Markup": 0.0
}
```
