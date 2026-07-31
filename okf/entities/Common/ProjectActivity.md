---
type: API Entity
title: ProjectActivities
description: Represents a project activity.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectActivity.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectActivity.html
  title: Monitor API — ProjectActivity
module: Common
api_class: ProjectActivity
doc_name: ProjectActivities
endpoint: GET /api/v1/Common/ProjectActivities
guid: C123B7F8-1455-4384-9267-17FE59F28A1A
permission: Show Activity list – Project
introduced_in: '2.36'
property_count: 23
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
- /entities/Common/ProjectActivityType.md
- /entities/Common/ProjectPhase.md
referenced_by:
- /entities/Common/DelegatedWork.md
- /entities/Common/ProjectActivityCalendarAppointment.md
- /entities/Common/ProjectActivityRelation.md
- /entities/Common/ProjectPhase.md
- /entities/TimeRecording/WorkInterval.md
---

# ProjectActivities

Represents a project activity.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ProjectActivity`
- **Endpoint:** `GET /api/v1/Common/ProjectActivities`
- **Required permission:** Show Activity list – Project
- **GUID:** `C123B7F8-1455-4384-9267-17FE59F28A1A`
- **Introduced in:** 2.36

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project activity. |
| `Number` | `Int64` | no |  |  | The number of the project activity. |
| `ReportedTimeInHours` | `Decimal` | no |  |  | The reported time in hours of the project activity. |
| `RestTimeInHours` | `Decimal` | no |  |  | The rest time in hours of the project activity. |
| `PlannedTimeInHours` | `Decimal` | no |  |  | The planned time in hours of the project activity. |
| `ShowInProjectReport` | `Boolean` | no |  |  | Specifies if the project activity should be shown in the project report. |
| `ParentId` | `Int64` | no | [ProjectPhases](/entities/Common/ProjectPhase.md) |  | The business key identifier of the activity's parent. References ProjectPhases . |
| `LockedDelegateWork` | `Boolean` | no |  |  | Specifies if the activity's delegate work is locked. |
| `ActivityTypeId` | `Int64` | no | [ProjectActivityTypes](/entities/Common/ProjectActivityType.md) |  | The business key identifier of the activity's type. References ProjectActivityTypes . |
| `ActivityType` | `ProjectActivityTypes` | no | [ProjectActivityTypes](/entities/Common/ProjectActivityType.md) | expandable | The type of the project activity. |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the application user that has completed the activity. References ApplicationUsers . |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the application user that is responsible for the activity. References ApplicationUsers . |
| `Description` | `String` | no |  |  | The description of the activity. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the activity's comment. References Comments . |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the activity. |
| `Status` | `Int32` | no |  | enum | The status of the activity. |
| `ReminderId` | `Int64?` | yes |  |  | The business key identifier of the activity's reminder. References Reminder. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |  | The planned completion date of the activity. |
| `CompletionDate` | `DateTimeOffset?` | yes |  |  | The completion date of the activity. |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  |  | The planned start date of the activity. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |  | The actual start date of the activity. |
| `Mandatory` | `Boolean` | no |  | since 2.50 | Whether or not the activity is mandatory. |
| `CalendarAppointmentId` | `String` | no |  | max length 256, since 2.50 | The unique calendar appointment identifier of the activity. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `InProgress` | 2 |
| `History` | 9 |


## Referenced by

**Common**

- [DelegatedWork](/entities/Common/DelegatedWork.md) — `ActivityId` (FK)
- [ProjectActivityCalendarAppointments](/entities/Common/ProjectActivityCalendarAppointment.md) — `ProjectActivityId` (FK)
- [ProjectActivityRelations](/entities/Common/ProjectActivityRelation.md) — `DependentOnEntityId` (FK)
- [ProjectActivityRelations](/entities/Common/ProjectActivityRelation.md) — `ParentId` (FK)
- [ProjectPhases](/entities/Common/ProjectPhase.md) — `Activities` (expand)

**TimeRecording**

- [WorkIntervals](/entities/TimeRecording/WorkInterval.md) — `ActivityId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "ReportedTimeInHours": 0.0,
  "RestTimeInHours": 0.0,
  "PlannedTimeInHours": 0.0,
  "ShowInProjectReport": false,
  "ParentId": 0,
  "LockedDelegateWork": false,
  "ActivityTypeId": 0,
  "ActivityType": null,
  "CompletedByUserId": null,
  "ResponsibleUserId": 0,
  "Description": null,
  "CommentId": null,
  "Comment": null,
  "Status": 0,
  "ReminderId": null,
  "PlannedCompletionDate": "0001-01-01T00:00:00+00:00",
  "CompletionDate": null,
  "PlannedStartDate": null,
  "ActualStartDate": null,
  "Mandatory": false,
  "CalendarAppointmentId": null
}
```
