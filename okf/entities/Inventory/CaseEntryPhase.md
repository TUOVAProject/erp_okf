---
type: API Entity
title: CaseEntryPhases
description: Represents a case entry phase.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseEntryPhase.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseEntryPhase.html
  title: Monitor API — CaseEntryPhase
module: Inventory
api_class: CaseEntryPhase
doc_name: CaseEntryPhases
endpoint: GET /api/v1/Inventory/CaseEntryPhases
guid: 4966A8CD-D216-4427-BD20-30295A95BA8C
permission: Show case
introduced_in: '2.45'
property_count: 8
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CaseEntryActivity.md
- /entities/Inventory/CaseManagementPhase.md
referenced_by:
- /entities/Inventory/CaseEntry.md
---

# CaseEntryPhases

Represents a case entry phase.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `CaseEntryPhase`
- **Endpoint:** `GET /api/v1/Inventory/CaseEntryPhases`
- **Required permission:** Show case
- **GUID:** `4966A8CD-D216-4427-BD20-30295A95BA8C`
- **Introduced in:** 2.45

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the phase. |
| `CaseManagementPhaseId` | `Int64` | no |  |  | The business key identifier of the case management phase that the phase is based on. |
| `CaseManagementPhase` | `CaseManagementPhases` | no | [CaseManagementPhases](/entities/Inventory/CaseManagementPhase.md) | expandable | The case management phase that the phase is based on. |
| `Description` | `String` | no |  |  | The description of the phase. |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the application user that is responsible for the phase. |
| `ParentId` | `Int64` | no | [CaseEntry](/entities/Inventory/CaseEntry.md) |  | The business key identifier of the parent of the phase. |
| `RowIndex` | `Int32` | no |  |  | Determines where the phase is placed in relation to the other phases belonging to the same parent. |
| `Activities` | `CaseEntryActivities[]` | no | [CaseEntryActivities](/entities/Inventory/CaseEntryActivity.md) | expandable, collection | The activities that are linked to the phase. |

## Referenced by

**Inventory**

- [CaseEntry](/entities/Inventory/CaseEntry.md) — `Phases` (expand)


## Example

```json
{
  "Id": 0,
  "CaseManagementPhaseId": 0,
  "CaseManagementPhase": null,
  "Description": null,
  "ResponsibleUserId": 0,
  "ParentId": 0,
  "RowIndex": 0,
  "Activities": null
}
```
