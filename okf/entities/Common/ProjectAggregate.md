---
type: API Entity
title: ProjectAggregates
description: Represents a project aggregate.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectAggregate.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectAggregate.html
  title: Monitor API — ProjectAggregate
module: Common
api_class: ProjectAggregate
doc_name: ProjectAggregates
endpoint: GET /api/v1/Common/ProjectAggregates
guid: F8DD9C91-ECF8-4AF1-AE67-794EED907060
permission: Show projects
introduced_in: '2.46'
property_count: 9
references_out:
- /entities/Common/Project.md
- /entities/Common/ProjectCostType.md
referenced_by:
- /entities/Common/Project.md
---

# ProjectAggregates

Represents a project aggregate.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ProjectAggregate`
- **Endpoint:** `GET /api/v1/Common/ProjectAggregates`
- **Required permission:** Show projects
- **GUID:** `F8DD9C91-ECF8-4AF1-AE67-794EED907060`
- **Introduced in:** 2.46

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project aggregate. |
| `ProjectId` | `Int64?` | yes | [Projects](/entities/Common/Project.md) |  | The business key identifier of the project the project aggregate belongs to. |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](/entities/Common/ProjectCostType.md) |  | The business key identifier of the project cost type the project aggregate belongs to. |
| `ExpectedResultCost` | `Decimal` | no |  |  | The expected result cost. |
| `ExpectedResultIncome` | `Decimal` | no |  |  | The expected result income. |
| `ExpectedResultTime` | `Decimal` | no |  |  | The expected result time in hours. |
| `ResultCost` | `Decimal` | no |  |  | The results cost. |
| `ResultIncome` | `Decimal` | no |  |  | The results income. |
| `ResultTime` | `Decimal` | no |  |  | The results time in hours. |

## Referenced by

**Common**

- [Projects](/entities/Common/Project.md) — `ProjectAggregates` (expand)


## Example

```json
{
  "Id": 0,
  "ProjectId": null,
  "CostTypeId": null,
  "ExpectedResultCost": 0.0,
  "ExpectedResultIncome": 0.0,
  "ExpectedResultTime": 0.0,
  "ResultCost": 0.0,
  "ResultIncome": 0.0,
  "ResultTime": 0.0
}
```
