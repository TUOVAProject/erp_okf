---
type: API Entity
title: FixedAssetGroups
description: Represents a fixed assets group.
resource: https://api.monitor.se/api/Monitor.API.Accounting.FixedAssetGroup.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.FixedAssetGroup.html
  title: Monitor API — FixedAssetGroup
module: Accounting
api_class: FixedAssetGroup
doc_name: FixedAssetGroups
endpoint: GET /api/v1/Accounting/FixedAssetGroups
guid: 5b152e6b-530b-4ad2-8b5d-f457e05d0b90
permission: Show basic data for fixed assets register
introduced_in: '23.5'
property_count: 2
referenced_by:
- /entities/Accounting/FixedAsset.md
---

# FixedAssetGroups

Represents a fixed assets group.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `FixedAssetGroup`
- **Endpoint:** `GET /api/v1/Accounting/FixedAssetGroups`
- **Required permission:** Show basic data for fixed assets register
- **GUID:** `5b152e6b-530b-4ad2-8b5d-f457e05d0b90`
- **Introduced in:** 23.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the fixed assets group. |
| `Code` | `String` | no |  | unique, max length 8 | The human readable identifier of the fixed assets group. |

## Referenced by

**Accounting**

- [FixedAssets](/entities/Accounting/FixedAsset.md) — `Group` (expand)
- [FixedAssets](/entities/Accounting/FixedAsset.md) — `GroupId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null
}
```
