---
type: API Entity
title: AlloyQuantities
description: Represents Alloy Quantities of an alloy.
resource: https://api.monitor.se/api/Monitor.API.Inventory.AlloyQuantity.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.AlloyQuantity.html
  title: Monitor API — AlloyQuantity
module: Inventory
api_class: AlloyQuantity
doc_name: AlloyQuantities
endpoint: GET /api/v1/Inventory/AlloyQuantities
guid: 030691D1-876B-44ED-8FEF-78C52E015953
permission: Create new alloy codes
introduced_in: '25.3'
property_count: 4
references_out:
- /entities/Inventory/Alloy.md
- /entities/Inventory/Part.md
---

# AlloyQuantities

Represents Alloy Quantities of an alloy.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `AlloyQuantity`
- **Endpoint:** `GET /api/v1/Inventory/AlloyQuantities`
- **Required permission:** Create new alloy codes
- **GUID:** `030691D1-876B-44ED-8FEF-78C52E015953`
- **Introduced in:** 25.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the alloy quantity. |
| `AlloyId` | `Int64` | no | [Alloys](/entities/Inventory/Alloy.md) |  | The business key identifier of the alloy quantity. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the alloy. |
| `PartId` | `Int64` | no | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the alloy part. |

## Example

```json
{
  "Id": 0,
  "AlloyId": 0,
  "Quantity": 0.0,
  "PartId": 0
}
```
