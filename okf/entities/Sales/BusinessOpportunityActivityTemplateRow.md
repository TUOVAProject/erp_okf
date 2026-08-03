---
type: API Entity
title: BusinessOpportunityActivityTemplateRows
description: Represents a business opportunity activity template row.
resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityActivityTemplateRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityActivityTemplateRow.html
  title: Monitor API — BusinessOpportunityActivityTemplateRow
module: Sales
api_class: BusinessOpportunityActivityTemplateRow
doc_name: BusinessOpportunityActivityTemplateRows
endpoint: GET /api/v1/Sales/BusinessOpportunityActivityTemplateRows
guid: ede2c6f3-b875-4926-bd64-01fed5cd4909
permission: Show business opportunity
introduced_in: '25.9'
property_count: 14
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
- /entities/Sales/BusinessOpportunityActivityTemplate.md
- /entities/Sales/CustomerRelationshipActivityType.md
referenced_by:
- /entities/Sales/BusinessOpportunityActivityTemplate.md
---

# BusinessOpportunityActivityTemplateRows

Represents a business opportunity activity template row.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `BusinessOpportunityActivityTemplateRow`
- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityActivityTemplateRows`
- **Required permission:** Show business opportunity
- **GUID:** `ede2c6f3-b875-4926-bd64-01fed5cd4909`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business opportunity activity template row. |
| `ActivityTemplateId` | `Int64?` | yes | [BusinessOpportunityActivityTemplates](BusinessOpportunityActivityTemplate.md) |  | The business key identifier of the row's business opportunity activity template. |
| `ActivityTypeId` | `Int64?` | yes | [CustomerRelationshipActivityTypes](CustomerRelationshipActivityType.md) |  | The business key identifier of the template row's activity type. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the template row's responsible application user. |
| `Code` | `Int64` | no |  |  | The code of the template row. |
| `IsAdministratorResponsible` | `Boolean` | no |  |  | Specifies if administrator is responsible for the template row. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the template row's comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The template row's comment. |
| `DueDateType` | `Int32` | no |  | enum | The due date type of the template row. |
| `NumberDaysFromDueDate` | `Int32` | no |  |  | The number of work days from due date of the template row. |
| `Status` | `Int32` | no |  | enum | The status of the template row. |
| `IsMandatory` | `Boolean` | no |  |  | Specifies if the template row is mandatory. |
| `IsReminder` | `Boolean` | no |  |  | Specifies if the template row is a reminder. |
| `IsLoggedUserResponsible` | `Boolean` | no |  |  | Specifies if the logged user is responsible for the remplate row. |

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


## Referenced by

**Sales**

- [BusinessOpportunityActivityTemplates](BusinessOpportunityActivityTemplate.md) — `Rows` (expand)


## Example

```json
{
  "Id": 0,
  "ActivityTemplateId": null,
  "ActivityTypeId": null,
  "ResponsibleUserId": null,
  "Code": 0,
  "IsAdministratorResponsible": false,
  "CommentId": null,
  "Comment": null,
  "DueDateType": 0,
  "NumberDaysFromDueDate": 0,
  "Status": 0,
  "IsMandatory": false,
  "IsReminder": false,
  "IsLoggedUserResponsible": false
}
```
