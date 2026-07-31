---
type: API Entity
title: CaseEntryActivities
description: Represents a case entry activity.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseEntryActivity.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseEntryActivity.html
  title: Monitor API — CaseEntryActivity
module: Inventory
api_class: CaseEntryActivity
doc_name: CaseEntryActivities
endpoint: GET /api/v1/Inventory/CaseEntryActivities
guid: EED439CC-248F-4370-B235-F9C585730CE8
permission: Show case
introduced_in: '2.45'
property_count: 23
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CaseManagementActivity.md
referenced_by:
- /entities/Inventory/CaseEntryPhase.md
---

# CaseEntryActivities

Represents a case entry activity.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `CaseEntryActivity`
- **Endpoint:** `GET /api/v1/Inventory/CaseEntryActivities`
- **Required permission:** Show case
- **GUID:** `EED439CC-248F-4370-B235-F9C585730CE8`
- **Introduced in:** 2.45

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the activity. |
| `CaseEntryId` | `Int64` | no | [CaseEntry](/entities/Inventory/CaseEntry.md) |  | The business key identifier of the case entry that the activity belongs to. |
| `PlannedTime` | `TimeSpan` | no |  |  | The planned time of the activity. |
| `ReportedTime` | `TimeSpan?` | yes |  |  | The reported time of the activity. |
| `ShowOnDocuments` | `Boolean` | no |  |  | Specifies if the activity should be shown on documents or not. |
| `ReportingType` | `Int32` | no |  | enum | The reporting type specified for the activity. |
| `Mandatory` | `Boolean` | no |  |  | Specifies whether or not the activity is mandatory. |
| `CostPerHour` | `Decimal?` | yes |  |  | The cost per hour of the activity. |
| `CostPerHourCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency that the cost per hour is specified in. |
| `Chargeable` | `Boolean` | no |  |  | Specifies whether or not the activity is chargeable. |
| `ActivityTypeId` | `Int64` | no | [CaseManagementActivities](/entities/Inventory/CaseManagementActivity.md) |  | The business key identifier of the case management activity that the activity is based on. |
| `CalendarAppointmentId` | `String` | no |  |  | The calendar appointment id of the activity. |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the user that completed the activity. |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the user that is responsible for the activity. |
| `Description` | `String` | no |  |  | The description of the activity. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the activity's comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The activity's comment. |
| `Status` | `Int32` | no |  | enum | The status of the activity. |
| `ReminderId` | `Int64?` | yes |  |  | The business key identifier of the reminder that is linked with the activity. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |  | The planned completion date of the activity. |
| `CompletionDate` | `DateTimeOffset?` | yes |  |  | The completion date of the activity. |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  |  | The planned start date of the activity. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |  | The actual start date of the activity. |

## Enumerations

### ReportingType

| Name | Value |
| --- | ---: |
| `Manual` | 0 |
| `Automatic` | 1 |

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `InProgress` | 2 |
| `History` | 9 |


## Referenced by

**Inventory**

- [CaseEntryPhases](/entities/Inventory/CaseEntryPhase.md) — `Activities` (expand)


## Example

```json
{
  "Id": 0,
  "CaseEntryId": 0,
  "PlannedTime": "00:00:00",
  "ReportedTime": null,
  "ShowOnDocuments": false,
  "ReportingType": 0,
  "Mandatory": false,
  "CostPerHour": null,
  "CostPerHourCurrencyId": null,
  "Chargeable": false,
  "ActivityTypeId": 0,
  "CalendarAppointmentId": null,
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
  "ActualStartDate": null
}
```
