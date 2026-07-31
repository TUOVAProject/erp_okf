---
type: API Entity
title: ProjectCostBudgets
description: Represents a project cost budget.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectCostBudget.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectCostBudget.html
  title: Monitor API — ProjectCostBudget
module: Common
api_class: ProjectCostBudget
doc_name: ProjectCostBudgets
endpoint: GET /api/v1/Common/ProjectCostBudgets
guid: c82183a9-3415-4079-8162-18b878592da0
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

# ProjectCostBudgets

Represents a project cost budget.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ProjectCostBudget`
- **Endpoint:** `GET /api/v1/Common/ProjectCostBudgets`
- **Required permission:** Show projects
- **GUID:** `c82183a9-3415-4079-8162-18b878592da0`
- **Introduced in:** 2.46

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project cost budget. |
| `ProjectId` | `Int64?` | yes | [Projects](/entities/Common/Project.md) |  | The business key identifier of the project this project cost budget belongs to. |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](/entities/Common/ProjectCostType.md) |  | The business key identifier of the project cost type this project cost budget belongs to. |
| `Hours` | `Decimal` | no |  |  | The time in hours of the project cost budget. |
| `Cost` | `Decimal` | no |  |  | The cost of the project cost budget. |
| `Income` | `Decimal` | no |  |  | The income of the project cost budget. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the project cost budget's comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the project cost budget. |

## Referenced by

**Common**

- [Projects](/entities/Common/Project.md) — `ProjectCostBudgets` (expand)


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
