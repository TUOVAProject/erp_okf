---
type: API Entity
title: ProjectActivityRelations
description: Represents a relation between two project activities.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectActivityRelation.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectActivityRelation.html
  title: Monitor API — ProjectActivityRelation
module: Common
api_class: ProjectActivityRelation
doc_name: ProjectActivityRelations
endpoint: GET /api/v1/Common/ProjectActivityRelations
guid: 7c32d185-ae8e-4296-8902-8e0d8f4ec99b
permission: Show Activity list – Project
introduced_in: '2.50'
property_count: 5
references_out:
- /entities/Common/ProjectActivity.md
---

# ProjectActivityRelations

Represents a relation between two project activities.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ProjectActivityRelation`
- **Endpoint:** `GET /api/v1/Common/ProjectActivityRelations`
- **Required permission:** Show Activity list – Project
- **GUID:** `7c32d185-ae8e-4296-8902-8e0d8f4ec99b`
- **Introduced in:** 2.50

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project activity relation. |
| `ParentId` | `Int64` | no | [ProjectActivities](ProjectActivity.md) |  | The business key identifier of the activity that the relation belongs to. |
| `DependentOnEntityId` | `Int64` | no | [ProjectActivities](ProjectActivity.md) |  | The business key identifier of the activity that the relation depends on. |
| `Type` | `Int32` | no |  | enum | The type of activitity relation. |
| `RowIndex` | `Int32` | no |  |  | The row index of the activity relation. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `FinishedBeforeStart` | 0 |
| `StartedBeforeStart` | 1 |


## Example

```json
{
  "Id": 0,
  "ParentId": 0,
  "DependentOnEntityId": 0,
  "Type": 0,
  "RowIndex": 0
}
```
