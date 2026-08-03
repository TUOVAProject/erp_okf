---
type: API Entity
title: ProjectPhaseTypes
description: Represents a project phase type.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectPhaseType.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectPhaseType.html
  title: Monitor API — ProjectPhaseType
module: Common
api_class: ProjectPhaseType
doc_name: ProjectPhaseTypes
endpoint: GET /api/v1/Common/ProjectPhaseTypes
guid: FE62079E-AAE9-4E41-8C47-6BFEDD53A9CE
permission: Show basic data for project
introduced_in: '2.36'
property_count: 4
references_out:
- /entities/Common/ApplicationUser.md
referenced_by:
- /entities/Common/ProjectPhase.md
---

# ProjectPhaseTypes

Represents a project phase type.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ProjectPhaseType`
- **Endpoint:** `GET /api/v1/Common/ProjectPhaseTypes`
- **Required permission:** Show basic data for project
- **GUID:** `FE62079E-AAE9-4E41-8C47-6BFEDD53A9CE`
- **Introduced in:** 2.36

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the type. |
| `Number` | `Int32` | no |  |  | The number of the type. |
| `Description` | `String` | no |  |  | The translated description of the type. |
| `ManagerId` | `Int64?` | yes | [ApplicationUsers](ApplicationUser.md) |  | The business key identifier of the manager of the type. References ApplicationUsers . |

## Referenced by

**Common**

- [ProjectPhases](ProjectPhase.md) — `PhaseType` (expand)
- [ProjectPhases](ProjectPhase.md) — `PhaseTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "ManagerId": null
}
```
