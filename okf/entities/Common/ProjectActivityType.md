---
type: API Entity
title: ProjectActivityTypes
description: Represents a project activity type.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectActivityType.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectActivityType.html
  title: Monitor API — ProjectActivityType
module: Common
api_class: ProjectActivityType
doc_name: ProjectActivityTypes
endpoint: GET /api/v1/Common/ProjectActivityTypes
guid: F186D8EE-B5D4-417D-80A4-95623A82A462
permission: Show basic data for project
introduced_in: '2.36'
property_count: 14
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
referenced_by:
- /entities/Common/ProjectActivity.md
---

# ProjectActivityTypes

Represents a project activity type.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ProjectActivityType`
- **Endpoint:** `GET /api/v1/Common/ProjectActivityTypes`
- **Required permission:** Show basic data for project
- **GUID:** `F186D8EE-B5D4-417D-80A4-95623A82A462`
- **Introduced in:** 2.36

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the type. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](ApplicationUser.md) |  | The business key identifier of the type's responsible user. References ApplicationUsers . |
| `PlannedTimeInHours` | `Decimal` | no |  |  | The planned time in hours of the type. |
| `LeadTimeInDays` | `Int32` | no |  |  | The lead time in days of the type. |
| `QueueTimeInDays` | `Int32` | no |  |  | The queue time in days of the type. |
| `CostTypeId` | `Int64` | no |  |  | The business key identifier of type's project cost type. References ProjectCostType. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the project activity type is active. |
| `CommentId` | `Int64?` | yes | [Comments](Comment.md) |  | The business key identifier of type's comment. |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The comment of the type. |
| `UseReminder` | `Boolean` | no |  |  | Specifies if the project activity type should use reminder. |
| `ShowInProjectReport` | `Boolean` | no |  |  | Specifies if the project activity type be shown in the project report. |
| `Code` | `Int64` | no |  | unique | The code of the activity type. |
| `Description` | `String` | no |  |  | The description of the activity type. |
| `IsReportedAsDirectTime` | `Boolean` | no |  | since 2.50 | Whether or not activities of this type should be reported as direct time. |

## Referenced by

**Common**

- [ProjectActivities](ProjectActivity.md) — `ActivityType` (expand)
- [ProjectActivities](ProjectActivity.md) — `ActivityTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "ResponsibleUserId": null,
  "PlannedTimeInHours": 0.0,
  "LeadTimeInDays": 0,
  "QueueTimeInDays": 0,
  "CostTypeId": 0,
  "IsActive": false,
  "CommentId": null,
  "Comment": null,
  "UseReminder": false,
  "ShowInProjectReport": false,
  "Code": 0,
  "Description": null,
  "IsReportedAsDirectTime": false
}
```
