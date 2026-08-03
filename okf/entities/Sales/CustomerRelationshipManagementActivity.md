---
type: API Entity
title: CustomerRelationshipManagementActivities
description: Represents a customer relationship management activity.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerRelationshipManagementActivity.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerRelationshipManagementActivity.html
  title: Monitor API — CustomerRelationshipManagementActivity
module: Sales
api_class: CustomerRelationshipManagementActivity
doc_name: CustomerRelationshipManagementActivities
endpoint: GET /api/v1/Sales/CustomerRelationshipManagementActivities
guid: 8C3D18C5-572C-4EAF-8E9D-3721BA5D0981
permission: Show customer
introduced_in: '2.55'
property_count: 24
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerRelationshipActivityType.md
---

# CustomerRelationshipManagementActivities

Represents a customer relationship management activity.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerRelationshipManagementActivity`
- **Endpoint:** `GET /api/v1/Sales/CustomerRelationshipManagementActivities`
- **Required permission:** Show customer
- **GUID:** `8C3D18C5-572C-4EAF-8E9D-3721BA5D0981`
- **Introduced in:** 2.55

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer relationship management activity. |
| `CustomerId` | `Int64` | no | [Customers](Customer.md) |  | The business key identifier of the activity's customer. |
| `IsMandatory` | `Boolean` | no |  |  | Specify if the activity is mandatory. |
| `AdministratorType` | `Int32?` | yes |  | enum | The administrator type of the activity. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](../Common/BusinessContactReference.md) |  | The business key identifier of the activity's business contact reference. |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](../Common/BusinessContactReference.md) | expandable | The activity's business contact reference. |
| `OrderId` | `Int64?` | yes | [CustomerOrders](CustomerOrder.md) |  | The business key identifier of the activity's customer order. |
| `ActivityTypeId` | `Int64?` | yes | [CustomerRelationshipActivityTypes](CustomerRelationshipActivityType.md) |  | The business key identifier of the activity's customer relationship activity type. |
| `ActivityType` | `CustomerRelationshipActivityTypes` | no | [CustomerRelationshipActivityTypes](CustomerRelationshipActivityType.md) | expandable | The type of the activity. |
| `CalendarAppointmentId` | `String` | no |  | max length 256 | The unique identifier of the appointment created in the user's calendar program for the activity. |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the application user that has completed the activity. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the application user that is responsible for the activity. |
| `Description` | `String` | no |  |  | The description of the activity. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the activity's comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The comment of the activity. |
| `Status` | `Int32` | no |  | enum | The status of the activity. |
| `ReminderId` | `Int64?` | yes |  |  | The business key identifier of the activity's reminder. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |  | The planned completion date of the activity. |
| `CompletionDate` | `DateTimeOffset?` | yes |  |  | The completion date of the activity. |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  |  | The planned start date of the activity. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |  | The actual start date of the activity. |
| `IsAdministratorResponsibleUser` | `Boolean` | no |  |  | Specify if the activity's responsible user is synced with the customer's account manager. |
| `IsAdministratorResponsibleUserRestorable` | `Boolean` | no |  |  | Specify if the activity's responsible user should be changed when changing customer's account manager. |
| `IsDueDatePlannedCompletionDateRestorable` | `Boolean` | no |  |  | Specify if the activity's planned completion date can be changed from the customer orders delivery date. |

## Enumerations

### AdministratorType

| Name | Value |
| --- | ---: |
| `CustomerResponsible` | 0 |
| `Seller` | 1 |

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
  "CustomerId": 0,
  "IsMandatory": false,
  "AdministratorType": null,
  "BusinessContactReferenceId": null,
  "BusinessContactReference": null,
  "OrderId": null,
  "ActivityTypeId": null,
  "ActivityType": null,
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
  "IsAdministratorResponsibleUserRestorable": false,
  "IsDueDatePlannedCompletionDateRestorable": false
}
```
