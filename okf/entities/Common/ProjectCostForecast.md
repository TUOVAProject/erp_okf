---
type: API Entity
title: ProjectCostForecasts
description: Represents a project cost forecast.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectCostForecast.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectCostForecast.html
  title: Monitor API — ProjectCostForecast
module: Common
api_class: ProjectCostForecast
doc_name: ProjectCostForecasts
endpoint: GET /api/v1/Common/ProjectCostForecasts
guid: ee72fff4-766b-4919-b621-acffc517c0e8
permission: Show projects
introduced_in: '2.46'
property_count: 8
references_out:
- /entities/Common/Comment.md
- /entities/Common/Project.md
- /entities/Common/ProjectCostType.md
referenced_by:
- /entities/Common/Project.md
---

# ProjectCostForecasts

Represents a project cost forecast.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ProjectCostForecast`
- **Endpoint:** `GET /api/v1/Common/ProjectCostForecasts`
- **Required permission:** Show projects
- **GUID:** `ee72fff4-766b-4919-b621-acffc517c0e8`
- **Introduced in:** 2.46

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project cost forecast. |
| `ProjectId` | `Int64?` | yes | [Projects](Project.md) |  | The business key identifier of the project this project cost forecast belongs to. |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](ProjectCostType.md) |  | The business key identifier of the project cost type this project cost forecast belongs to. |
| `Hours` | `Decimal` | no |  |  | The time in hours of the project cost forecast. |
| `Cost` | `Decimal` | no |  |  | The cost of the project cost forecast. |
| `Income` | `Decimal` | no |  |  | The income of the project cost forecast. |
| `CommentId` | `Int64?` | yes | [Comments](Comment.md) |  | The business key identifier of the project cost forecast's comment. |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The comment of the project cost forecast. |

## Referenced by

**Common**

- [Projects](Project.md) — `ProjectCostForecasts` (expand)


## Example

```json
{
  "Id": 0,
  "ProjectId": null,
  "CostTypeId": null,
  "Hours": 0.0,
  "Cost": 0.0,
  "Income": 0.0,
  "CommentId": null,
  "Comment": null
}
```
