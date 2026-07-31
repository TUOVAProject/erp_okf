---
type: API Entity
title: ProjectTypes
description: Represents a project type.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectType.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectType.html
  title: Monitor API — ProjectType
module: Common
api_class: ProjectType
doc_name: ProjectTypes
endpoint: GET /api/v1/Common/ProjectTypes
guid: bcacaada-fbd4-43d4-97b6-cacc951f81fb
permission: Show basic data for project
introduced_in: '2.43'
property_count: 3
referenced_by:
- /entities/Common/Project.md
---

# ProjectTypes

Represents a project type.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ProjectType`
- **Endpoint:** `GET /api/v1/Common/ProjectTypes`
- **Required permission:** Show basic data for project
- **GUID:** `bcacaada-fbd4-43d4-97b6-cacc951f81fb`
- **Introduced in:** 2.43

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project type. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the project type. |
| `Description` | `String` | no |  |  | The translated description of the project type. |

## Referenced by

**Common**

- [Projects](/entities/Common/Project.md) — `ProjectType` (expand)
- [Projects](/entities/Common/Project.md) — `ProjectTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null
}
```
