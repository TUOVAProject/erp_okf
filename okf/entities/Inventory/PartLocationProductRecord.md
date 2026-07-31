---
type: API Entity
title: PartLocationProductRecords
description: Represents a location quantity item where the quantity and possible product
  record is to be found.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartLocationProductRecord.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartLocationProductRecord.html
  title: Monitor API — PartLocationProductRecord
module: Inventory
api_class: PartLocationProductRecord
doc_name: PartLocationProductRecords
endpoint: GET /api/v1/Inventory/PartLocationProductRecords
guid: EE339B91-B25D-4D1E-9343-1080E8BED931
permission: Show part
introduced_in: '2.29'
property_count: 4
references_out:
- /entities/Inventory/PartLocation.md
- /entities/Inventory/ProductRecord.md
referenced_by:
- /entities/Inventory/PartLocation.md
---

# PartLocationProductRecords

Represents a location quantity item where the quantity and possible product record is to be found.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `PartLocationProductRecord`
- **Endpoint:** `GET /api/v1/Inventory/PartLocationProductRecords`
- **Required permission:** Show part
- **GUID:** `EE339B91-B25D-4D1E-9343-1080E8BED931`
- **Introduced in:** 2.29

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the location quantity item. |
| `PartLocationId` | `Int64` | no | [PartLocations](/entities/Inventory/PartLocation.md) |  | The business key identifier of the location to which the location quantity item belong. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](/entities/Inventory/ProductRecord.md) |  | The business key identifier of the product record of the location quantity item. |
| `Quantity` | `Decimal` | no |  |  | The quantity in standard unit. |

## Referenced by

**Inventory**

- [PartLocations](/entities/Inventory/PartLocation.md) — `PartLocationProductRecords` (expand)


## Example

```json
{
  "Id": 0,
  "PartLocationId": 0,
  "ProductRecordId": null,
  "Quantity": 0.0
}
```
