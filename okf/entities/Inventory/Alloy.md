---
type: API Entity
title: Alloys
description: Represents an alloy.
resource: https://api.monitor.se/api/Monitor.API.Inventory.Alloy.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.Alloy.html
  title: Monitor API — Alloy
module: Inventory
api_class: Alloy
doc_name: Alloys
endpoint: GET /api/v1/Inventory/Alloys
guid: 2822fbbd-beff-4c1f-ae7f-3cd81413c0f4
permission: Show alloy codes
introduced_in: '2.18'
property_count: 7
references_out:
- /entities/Common/Currency.md
- /entities/Common/Unit.md
- /entities/Inventory/Part.md
referenced_by:
- /entities/Inventory/AlloyQuantity.md
- /entities/Inventory/Part.md
---

# Alloys

Represents an alloy.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `Alloy`
- **Endpoint:** `GET /api/v1/Inventory/Alloys`
- **Required permission:** Show alloy codes
- **GUID:** `2822fbbd-beff-4c1f-ae7f-3cd81413c0f4`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the alloy. |
| `Code` | `String` | no |  | unique, max length 10 | The human readable identifier of the alloy. |
| `Description` | `String` | no |  |  | The translated description of the alloy. |
| `Price` | `Decimal` | no |  |  | The price of the alloy. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the currency that the alloy price is specified in. |
| `UnitId` | `Int64` | no | [Units](../Common/Unit.md) |  | The business key identifier of the alloy unit. |
| `PartId` | `Int64` | no | [Parts](Part.md) |  | The business key identifier of the alloy part. |

## Referenced by

**Inventory**

- [AlloyQuantities](AlloyQuantity.md) — `AlloyId` (FK)
- [Parts](Part.md) — `CurrentAlloy` (expand)
- [Parts](Part.md) — `CurrentAlloyId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "Price": 0.0,
  "PriceCurrencyId": null,
  "UnitId": 0,
  "PartId": 0
}
```
