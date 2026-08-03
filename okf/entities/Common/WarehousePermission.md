---
type: API Entity
title: WarehousePermissions
description: Represents an application user warehouse permission.
resource: https://api.monitor.se/api/Monitor.API.Common.WarehousePermission.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.WarehousePermission.html
  title: Monitor API — WarehousePermission
module: Common
api_class: WarehousePermission
doc_name: WarehousePermissions
endpoint: GET /api/v1/Common/WarehousePermissions
guid: 2869CE1E-C5E8-4DA7-9CEF-25680186D67F
permission: Show user rights groups
introduced_in: '22.3'
property_count: 6
references_out:
- /entities/Common/Permission.md
- /entities/Common/PermissionGroup.md
- /entities/Common/Role.md
referenced_by:
- /entities/Common/ApplicationUser.md
---

# WarehousePermissions

Represents an application user warehouse permission.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `WarehousePermission`
- **Endpoint:** `GET /api/v1/Common/WarehousePermissions`
- **Required permission:** Show user rights groups
- **GUID:** `2869CE1E-C5E8-4DA7-9CEF-25680186D67F`
- **Introduced in:** 22.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the warehouse permission. |
| `ApplicationUserId` | `Int64` | no |  |  | The business key identifier of the application user that the warehouse permission belongs to. |
| `WarehouseId` | `Int64` | no |  |  | The business key identifier of the warehouse that the warehouse permission applies to. |
| `PermissionGroups` | `PermissionGroups[]` | no | [PermissionGroups](PermissionGroup.md) | expandable, collection | The permission groups that apply to the warehouse permission. |
| `Roles` | `Roles[]` | no | [Roles](Role.md) | expandable, collection | The roles that apply to the warehouse permission. |
| `Permissions` | `Permissions[]` | no | [Permissions](Permission.md) | expandable, collection | The individual permissions that apply to the warehouse permission. |

## Referenced by

**Common**

- [ApplicationUsers](ApplicationUser.md) — `WarehousePermissions` (expand)


## Example

```json
{
  "Id": 0,
  "ApplicationUserId": 0,
  "WarehouseId": 0,
  "PermissionGroups": null,
  "Roles": null,
  "Permissions": null
}
```
