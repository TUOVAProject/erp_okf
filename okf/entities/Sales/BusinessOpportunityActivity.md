---
type: API Entity
title: BusinessOpportunityActivities
description: Represents a business opportunity activity.
resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityActivity.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityActivity.html
  title: Monitor API — BusinessOpportunityActivity
module: Sales
api_class: BusinessOpportunityActivity
doc_name: BusinessOpportunityActivities
endpoint: GET /api/v1/Sales/BusinessOpportunityActivities
guid: 6525fbab-7229-4c61-a9ad-8d916f44b9e0
permission: Show business opportunity
introduced_in: '25.9'
property_count: 23
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
- /entities/Common/Person.md
- /entities/Sales/BusinessOpportunity.md
- /entities/Sales/Customer.md
---

# BusinessOpportunityActivities

Represents a business opportunity activity.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `BusinessOpportunityActivity`
- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityActivities`
- **Required permission:** Show business opportunity
- **GUID:** `6525fbab-7229-4c61-a9ad-8d916f44b9e0`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business opportunity activity. |
| `OrderId` | `Int64?` | yes | [BusinessOpportunities](BusinessOpportunity.md) |  | The business key identifier of the activity's business opportunity. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the actifity. |
| `ActivityTypeId` | `Int64?` | yes |  |  | The business key identifier of the activity's type. |
| `IsMandatory` | `Boolean` | no |  |  | Specifies if the activity is mandatory. |
| `IsDueDatePlannedCompletionDate` | `Boolean` | no |  |  | Specifies if due date id planned completion date on the activity. |
| `IsAdministratorResponsibleUser` | `Boolean` | no |  |  | Specifies if the administrator is the responsible user of the activity. |
| `Description` | `String` | no |  | max length 400 | The translated description of the activity. |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  |  | The planned start date of the activity. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the user who is responsible for this activity. |
| `CustomerId` | `Int64?` | yes | [Customers](Customer.md) |  | The business key identifier of the customer on this activity. |
| `ReferenceId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the reference on this activity. |
| `DueDateType` | `Int32` | no |  | enum | The due date type of the activity. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the activity's comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The comment of the activity. |
| `Status` | `Int32` | no |  | enum | The status of the activity. |
| `NumberDaysFromDueDate` | `Int32?` | yes |  |  | Specifies number of days from due date on this activity. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |  | The planned completion date of the activity. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |  | The actual start date of the activity. |
| `CompletionDate` | `DateTimeOffset?` | yes |  |  | The completion date of the activity. |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the user who completed this activity. |
| `ReminderId` | `Int64?` | yes |  |  | The business key identifier of the activity's reminder. |
| `CalendarAppointmentId` | `String` | no |  | max length 256 | The calendar appointment id of the activity. |

## Enumerations

### DueDateType

| Name | Value |
| --- | ---: |
| `RegistrationDate` | 0 |
| `ValidThrough` | 1 |

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `InProgress` | 2 |
| `History` | 9 |


## Example

```json
{
  "Id": 0,
  "OrderId": null,
  "RowIndex": null,
  "ActivityTypeId": null,
  "IsMandatory": false,
  "IsDueDatePlannedCompletionDate": false,
  "IsAdministratorResponsibleUser": false,
  "Description": null,
  "PlannedStartDate": null,
  "ResponsibleUserId": null,
  "CustomerId": null,
  "ReferenceId": null,
  "DueDateType": 0,
  "CommentId": null,
  "Comment": null,
  "Status": 0,
  "NumberDaysFromDueDate": null,
  "PlannedCompletionDate": "0001-01-01T00:00:00+00:00",
  "ActualStartDate": null,
  "CompletionDate": null,
  "CompletedByUserId": null,
  "ReminderId": null,
  "CalendarAppointmentId": null
}
```
