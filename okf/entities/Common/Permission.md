---
type: API Entity
title: Permissions
description: Represents a permission node.
resource: https://api.monitor.se/api/Monitor.API.Common.Permission.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Permission.html
  title: Monitor API — Permission
module: Common
api_class: Permission
doc_name: Permissions
endpoint: GET /api/v1/Common/Permissions
guid: 1CCC4273-1533-40BE-8478-496F5D10DFD3
permission: Show user
introduced_in: '22.3'
property_count: 5
referenced_by:
- /entities/Common/PermissionGroup.md
- /entities/Common/WarehousePermission.md
---

# Permissions

Represents a permission node.

- **Module:** [Common](/modules/Common.md)
- **API class:** `Permission`
- **Endpoint:** `GET /api/v1/Common/Permissions`
- **Required permission:** Show user
- **GUID:** `1CCC4273-1533-40BE-8478-496F5D10DFD3`
- **Introduced in:** 22.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the permission. |
| `PermissionId` | `Guid` | no |  |  | The programmatic identifier of the permission node. |
| `IsDenied` | `Boolean` | no |  |  | Whether or not the permission is denied. |
| `ParentClass` | `Guid` | no |  |  | The GUID identifier of the type of entity that the permission belongs to. |
| `ParentId` | `Int64` | no |  |  | The business key identifier of the parent that the permission belongs to. |

## Referenced by

**Common**

- [PermissionGroups](/entities/Common/PermissionGroup.md) — `Permissions` (expand)
- [WarehousePermissions](/entities/Common/WarehousePermission.md) — `Permissions` (expand)


## Example

```json
{
  "Id": 0,
  "PermissionId": "00000000-0000-0000-0000-000000000000",
  "IsDenied": false,
  "ParentClass": "00000000-0000-0000-0000-000000000000",
  "ParentId": 0
}
```
