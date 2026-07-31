---
type: API Entity
title: AbcCodes
description: Represents an ABC code.
resource: https://api.monitor.se/api/Monitor.API.Inventory.AbcCode.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.AbcCode.html
  title: Monitor API — AbcCode
module: Inventory
api_class: AbcCode
doc_name: AbcCodes
endpoint: GET /api/v1/Inventory/AbcCodes
guid: d39aa997-b375-4fa9-8eba-0a8ddeedea2c
permission: Show ABC codes
introduced_in: '2.31'
property_count: 3
referenced_by:
- /entities/Inventory/PartPlanningInformation.md
- /entities/Inventory/PartTemplate.md
---

# AbcCodes

Represents an ABC code.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `AbcCode`
- **Endpoint:** `GET /api/v1/Inventory/AbcCodes`
- **Required permission:** Show ABC codes
- **GUID:** `d39aa997-b375-4fa9-8eba-0a8ddeedea2c`
- **Introduced in:** 2.31

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the ABC code. |
| `Code` | `String` | no |  |  | The human readable identifier (single letter) of the ABC code. |
| `Description` | `String` | no |  |  | The description of the ABC code. |

## Referenced by

**Inventory**

- [PartPlanningInformation](/entities/Inventory/PartPlanningInformation.md) — `AbcCodeId` (FK)
- [PartTemplates](/entities/Inventory/PartTemplate.md) — `AbcCodeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null
}
```
