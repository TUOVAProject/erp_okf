---
type: API Entity
title: CaseManagementPhases
description: Represents a case management phase.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementPhase.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementPhase.html
  title: Monitor API — CaseManagementPhase
module: Inventory
api_class: CaseManagementPhase
doc_name: CaseManagementPhases
endpoint: GET /api/v1/Inventory/CaseManagementPhases
guid: DE25A497-E2D5-4B6F-A7FC-9383B86DC1AC
permission: Show case
introduced_in: '2.45'
property_count: 3
referenced_by:
- /entities/Inventory/CaseEntryPhase.md
- /entities/Inventory/CaseManagementTemplateNode.md
---

# CaseManagementPhases

Represents a case management phase.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `CaseManagementPhase`
- **Endpoint:** `GET /api/v1/Inventory/CaseManagementPhases`
- **Required permission:** Show case
- **GUID:** `DE25A497-E2D5-4B6F-A7FC-9383B86DC1AC`
- **Introduced in:** 2.45

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case management phase. |
| `Number` | `Int32` | no |  |  | The human readable identifier of the case management phase. |
| `Description` | `String` | no |  |  | The description of the case management phase. |

## Referenced by

**Inventory**

- [CaseEntryPhases](CaseEntryPhase.md) — `CaseManagementPhase` (expand)
- [CaseManagementTemplateNodes](CaseManagementTemplateNode.md) — `PhaseId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null
}
```
