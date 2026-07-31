---
type: API Entity
title: QuoteActivities
description: Represents a quote activity.
resource: https://api.monitor.se/api/Monitor.API.Sales.QuoteActivity.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.QuoteActivity.html
  title: Monitor API — QuoteActivity
module: Sales
api_class: QuoteActivity
doc_name: QuoteActivities
endpoint: GET /api/v1/Sales/QuoteActivities
guid: 95D6B3A6-2EC0-4C17-B998-B32A14DB52E8
permission: Show quote
introduced_in: '24.2'
property_count: 20
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
- /entities/Sales/CustomerRelationshipActivityType.md
- /entities/Sales/Quote.md
---

# QuoteActivities

Represents a quote activity.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `QuoteActivity`
- **Endpoint:** `GET /api/v1/Sales/QuoteActivities`
- **Required permission:** Show quote
- **GUID:** `95D6B3A6-2EC0-4C17-B998-B32A14DB52E8`
- **Introduced in:** 24.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the quote activity. |
| `QuoteId` | `Int64` | no | [Quotes](/entities/Sales/Quote.md) |  | The business key identifier of the quote this activity belongs to. |
| `IsMandatory` | `Boolean` | no |  |  | Specifies if this activity is mandatory. |
| `ActivityTypeId` | `Int64` | no | [CustomerRelationshipActivityTypes](/entities/Sales/CustomerRelationshipActivityType.md) |  | The business key identifier of the activity's type. |
| `CalendarAppointmentId` | `String` | no |  | max length 256 | The calendar appointment id of the activity. |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the user who completed this activity. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the user who is responsible for this activity. |
| `Description` | `String` | no |  | max length 400 | The translated description of the activity. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the activity's comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the activity. |
| `Status` | `Int32` | no |  | enum | The status of the activity. |
| `ReminderId` | `Int64?` | yes |  |  | The business key identifier of the activity's reminder. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |  | The planned completion date of the activity. |
| `CompletionDate` | `DateTimeOffset?` | yes |  |  | The completion date of the activity. |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  |  | The planned start date of the activity. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |  | The actual start date of the activity. |
| `IsAdministratorResponsibleUser` | `Boolean` | no |  |  | Specifies if the administrator is the responsible user of the activity. |
| `NumberDaysFromDueDate` | `Int32?` | yes |  |  | Specifies number of days from due date on this activity. |
| `IsDueDatePlannedCompletionDate` | `Boolean` | no |  |  | Specifies if due date id planned completion date on the activity. |
| `DueDateType` | `Int32` | no |  | enum | The due date type of the activity. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `InProgress` | 2 |
| `History` | 9 |

### DueDateType

| Name | Value |
| --- | ---: |
| `RegistrationDate` | 0 |
| `ValidThrough` | 1 |


## Example

```json
{
  "Id": 0,
  "QuoteId": 0,
  "IsMandatory": false,
  "ActivityTypeId": 0,
  "CalendarAppointmentId": null,
  "CompletedByUserId": null,
  "ResponsibleUserId": null,
  "Description": null,
  "CommentId": null,
  "Comment": null,
  "Status": 0,
  "ReminderId": null,
  "PlannedCompletionDate": "0001-01-01T00:00:00+00:00",
  "CompletionDate": null,
  "PlannedStartDate": null,
  "ActualStartDate": null,
  "IsAdministratorResponsibleUser": false,
  "NumberDaysFromDueDate": null,
  "IsDueDatePlannedCompletionDate": false,
  "DueDateType": 0
}
```
