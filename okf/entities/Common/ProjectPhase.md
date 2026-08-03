---
type: API Entity
title: ProjectPhases
description: Represents a project phase.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectPhase.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectPhase.html
  title: Monitor API — ProjectPhase
module: Common
api_class: ProjectPhase
doc_name: ProjectPhases
endpoint: GET /api/v1/Common/ProjectPhases
guid: 2A81071D-467A-4E01-823C-5508AEB554DC
permission: Show Activity list – Project
introduced_in: '2.36'
property_count: 10
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Project.md
- /entities/Common/ProjectActivity.md
- /entities/Common/ProjectPhaseType.md
referenced_by:
- /entities/Common/Project.md
- /entities/Common/ProjectActivity.md
---

# ProjectPhases

Represents a project phase.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ProjectPhase`
- **Endpoint:** `GET /api/v1/Common/ProjectPhases`
- **Required permission:** Show Activity list – Project
- **GUID:** `2A81071D-467A-4E01-823C-5508AEB554DC`
- **Introduced in:** 2.36

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project phase. |
| `Description` | `String` | no |  |  | The translated description of the project phase. |
| `Number` | `Int64` | no |  |  | The number of the project phase. |
| `PhaseTypeId` | `Int64` | no | [ProjectPhaseTypes](ProjectPhaseType.md) |  | The business key identifier of the type of the project phase. References ProjectPhaseTypes . |
| `PhaseType` | `ProjectPhaseTypes` | no | [ProjectPhaseTypes](ProjectPhaseType.md) | expandable | The type of the project phase. |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](ApplicationUser.md) |  | The business key identifier of the project phase's reponsible user. References ApplicationUsers . |
| `ParentId` | `Int64` | no | [Projects](Project.md) |  | The business key identifier of the phase's parent. References Projects . |
| `IsDummy` | `Boolean` | no |  |  | Specifies if the project phase is a dummy phase. |
| `RowIndex` | `Int32` | no |  |  | The row index of the project phase. |
| `Activities` | `ProjectActivities[]` | no | [ProjectActivities](ProjectActivity.md) | expandable, collection | The activities of the project phase. |

## Referenced by

**Common**

- [ProjectActivities](ProjectActivity.md) — `ParentId` (FK)
- [Projects](Project.md) — `Phases` (expand)


## Example

```json
{
  "Id": 0,
  "Description": null,
  "Number": 0,
  "PhaseTypeId": 0,
  "PhaseType": null,
  "ResponsibleUserId": 0,
  "ParentId": 0,
  "IsDummy": false,
  "RowIndex": 0,
  "Activities": null
}
```
