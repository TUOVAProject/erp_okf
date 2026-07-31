---
type: API Entity
title: PermissionGroups
description: Represents a permission group.
resource: https://api.monitor.se/api/Monitor.API.Common.PermissionGroup.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PermissionGroup.html
  title: Monitor API — PermissionGroup
module: Common
api_class: PermissionGroup
doc_name: PermissionGroups
endpoint: GET /api/v1/Common/PermissionGroups
guid: BC0D1D4D-E488-4DDD-B25D-C077E810F2A8
permission: Show user rights groups
introduced_in: '22.3'
property_count: 3
references_out:
- /entities/Common/Permission.md
referenced_by:
- /entities/Common/WarehousePermission.md
---

# PermissionGroups

Represents a permission group.

- **Module:** [Common](/modules/Common.md)
- **API class:** `PermissionGroup`
- **Endpoint:** `GET /api/v1/Common/PermissionGroups`
- **Required permission:** Show user rights groups
- **GUID:** `BC0D1D4D-E488-4DDD-B25D-C077E810F2A8`
- **Introduced in:** 22.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the permission group. |
| `Description` | `String` | no |  |  | The translated description of the permission group. |
| `Permissions` | `Permissions[]` | no | [Permissions](/entities/Common/Permission.md) | expandable, collection | The permissions that apply to the permission group. |

## Referenced by

**Common**

- [WarehousePermissions](/entities/Common/WarehousePermission.md) — `PermissionGroups` (expand)


## Example

```json
{
  "Id": 0,
  "Description": null,
  "Permissions": null
}
```
