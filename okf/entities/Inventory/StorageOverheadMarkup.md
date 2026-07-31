---
type: API Entity
title: StorageOverheadMarkups
description: Represents storage overhead markup.
resource: https://api.monitor.se/api/Monitor.API.Inventory.StorageOverheadMarkup.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.StorageOverheadMarkup.html
  title: Monitor API — StorageOverheadMarkup
module: Inventory
api_class: StorageOverheadMarkup
doc_name: StorageOverheadMarkups
endpoint: GET /api/v1/Inventory/StorageOverheadMarkups
guid: 08416125-9EC9-4C8C-883E-19D6656EB07B
permission: Show calculation mark-up
introduced_in: '2.18'
property_count: 5
referenced_by:
- /entities/Inventory/Part.md
---

# StorageOverheadMarkups

Represents storage overhead markup.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `StorageOverheadMarkup`
- **Endpoint:** `GET /api/v1/Inventory/StorageOverheadMarkups`
- **Required permission:** Show calculation mark-up
- **GUID:** `08416125-9EC9-4C8C-883E-19D6656EB07B`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the storage overhead markup. |
| `Number` | `Int32` | no |  |  | The human readable number of the storage overhead markup. |
| `Description` | `String` | no |  |  | The translated description of the storage overhead markup. |
| `Markup` | `Decimal` | no |  |  | The markup defined by the storage overhead markup. |
| `Type` | `Int32` | no |  | enum | The type of storage overhead markup. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `StorageOverhead` | 0 |
| `SubContract` | 1 |
| `Both` | 2 |


## Referenced by

**Inventory**

- [Parts](/entities/Inventory/Part.md) — `StorageOverheadMarkup` (expand)
- [Parts](/entities/Inventory/Part.md) — `StorageOverheadMarkupId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "Markup": 0.0,
  "Type": 0
}
```
