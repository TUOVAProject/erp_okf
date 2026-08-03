---
type: API Entity
title: ProjectCostTypes
description: Represents a project cost type.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectCostType.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectCostType.html
  title: Monitor API — ProjectCostType
module: Common
api_class: ProjectCostType
doc_name: ProjectCostTypes
endpoint: GET /api/v1/Common/ProjectCostTypes
guid: C2F963E4-A7D2-499A-9A23-4AFAC99E2568
permission: Show projects
introduced_in: '2.46'
property_count: 4
referenced_by:
- /entities/Common/ProjectAggregate.md
- /entities/Common/ProjectCostBudget.md
- /entities/Common/ProjectCostForecast.md
- /entities/TimeRecording/AttendanceAddition.md
---

# ProjectCostTypes

Represents a project cost type.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ProjectCostType`
- **Endpoint:** `GET /api/v1/Common/ProjectCostTypes`
- **Required permission:** Show projects
- **GUID:** `C2F963E4-A7D2-499A-9A23-4AFAC99E2568`
- **Introduced in:** 2.46

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project cost type. |
| `Number` | `Int64` | no |  | unique | The human readable identifier of the project cost type. |
| `Description` | `String` | no |  |  | The translated description of the project cost type. |
| `Type` | `Int32` | no |  | enum | The type of the project cost type. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Cost` | 1 |
| `Income` | 2 |


## Referenced by

**Common**

- [ProjectAggregates](ProjectAggregate.md) — `CostTypeId` (FK)
- [ProjectCostBudgets](ProjectCostBudget.md) — `CostTypeId` (FK)
- [ProjectCostForecasts](ProjectCostForecast.md) — `CostTypeId` (FK)

**TimeRecording**

- [AttendanceAdditions](../TimeRecording/AttendanceAddition.md) — `CostType` (expand)
- [AttendanceAdditions](../TimeRecording/AttendanceAddition.md) — `CostTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "Type": 0
}
```
