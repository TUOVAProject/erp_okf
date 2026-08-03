---
type: API Entity
title: ProjectGroups
description: Represents a project group.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectGroup.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectGroup.html
  title: Monitor API — ProjectGroup
module: Common
api_class: ProjectGroup
doc_name: ProjectGroups
endpoint: GET /api/v1/Common/ProjectGroups
guid: 7FDCA3A6-3736-40C6-BCAD-0CC97744F868
permission: Show basic data for project
introduced_in: '24.6'
property_count: 3
referenced_by:
- /entities/Common/Project.md
---

# ProjectGroups

Represents a project group.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ProjectGroup`
- **Endpoint:** `GET /api/v1/Common/ProjectGroups`
- **Required permission:** Show basic data for project
- **GUID:** `7FDCA3A6-3736-40C6-BCAD-0CC97744F868`
- **Introduced in:** 24.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project group. |
| `Number` | `Int64` | no |  | unique | The human readable identifier of the project group. |
| `Description` | `String` | no |  |  | The translated description of the project group. |

## Referenced by

**Common**

- [Projects](Project.md) — `ProjectGroup` (expand)
- [Projects](Project.md) — `ProjectGroupId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null
}
```
