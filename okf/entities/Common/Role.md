---
type: API Entity
title: Roles
description: Represents a user role.
resource: https://api.monitor.se/api/Monitor.API.Common.Role.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Role.html
  title: Monitor API — Role
module: Common
api_class: Role
doc_name: Roles
endpoint: GET /api/v1/Common/Roles
guid: 362CC578-5333-4E2C-B5D6-45C6C272B908
permission: Show user
introduced_in: '22.3'
property_count: 3
referenced_by:
- /entities/Common/WarehousePermission.md
---

# Roles

Represents a user role.

- **Module:** [Common](/modules/Common.md)
- **API class:** `Role`
- **Endpoint:** `GET /api/v1/Common/Roles`
- **Required permission:** Show user
- **GUID:** `362CC578-5333-4E2C-B5D6-45C6C272B908`
- **Introduced in:** 22.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the role. |
| `Description` | `String` | no |  |  | The translated description of the role. |
| `IsSuperUser` | `Boolean` | no |  |  | Whether or not application user's that belong to the role are considered super users. |

## Referenced by

**Common**

- [WarehousePermissions](/entities/Common/WarehousePermission.md) — `Roles` (expand)


## Example

```json
{
  "Id": 0,
  "Description": null,
  "IsSuperUser": false
}
```
