---
type: API Entity
title: ProjectCostReportingEntries
description: Represents a project cost reporting entry.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectCostReportingEntry.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectCostReportingEntry.html
  title: Monitor API — ProjectCostReportingEntry
module: Common
api_class: ProjectCostReportingEntry
doc_name: ProjectCostReportingEntries
endpoint: GET /api/v1/Common/ProjectCostReportingEntries
guid: d7e1f4c3-f042-479b-b9f5-b091619eae87
permission: Report activity for any user
introduced_in: '2.50'
property_count: 22
references_out:
- /entities/Common/Comment.md
---

# ProjectCostReportingEntries

Represents a project cost reporting entry.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ProjectCostReportingEntry`
- **Endpoint:** `GET /api/v1/Common/ProjectCostReportingEntries`
- **Required permission:** Report activity for any user
- **GUID:** `d7e1f4c3-f042-479b-b9f5-b091619eae87`
- **Introduced in:** 2.50

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project cost reporting entry. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the project cost reporting entry. |
| `ProjectId` | `Int64?` | yes |  |  | The business key identifier of the project linked to the project cost reporting entry. |
| `IsIncome` | `Boolean` | no |  |  | Specifies if the project cost reporting entry concerns income. |
| `ActivityId` | `Int64?` | yes |  |  | The business key identifier of the project activity linked to the project cost reporting entry. |
| `ReportedTimeInHours` | `Decimal` | no |  |  | The time in hours reported by the project cost reporting entry. |
| `CostTypeId` | `Int64?` | yes |  |  | The business key identifier of the cost type linked to the project cost reporting entry. |
| `Amount` | `Decimal` | no |  |  | The amount reported by the project cost reporting entry. |
| `ReportingDate` | `DateTimeOffset` | no |  |  | The date of the project cost reporting entry. |
| `OurReferenceId` | `Int64?` | yes |  |  | The business key identifier of the reference for the project cost reporting entry. |
| `OurReferenceName` | `String` | no |  |  | The name of our reference for the project cost reporting entry. |
| `EmployeeId` | `Int64?` | yes |  |  | The business key identifier of the employee that performed the reporting. |
| `WorkCenterId` | `Int64?` | yes |  |  | The business key identifier of the work center the reporting concerns. |
| `DepartmentId` | `Int64?` | yes |  |  | The business key identifier of the department the reporting concerns. |
| `IsCancelled` | `Boolean` | no |  |  | Specifies if the project cost reporting entry is cancelled. |
| `CommentId` | `Int64?` | yes |  |  | The business key identifier of the comment for the project cost reporting entry. |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The comment of the project cost reporting entry. |
| `CustomerReference` | `String` | no |  | max length 80, since 26.6 | Customer reference for the project cost reporting entry. Entered per log in Authorize/adjust and copied from the work recording. |
| `CustomerOrderNumber` | `String` | no |  | max length 15, since 26.6 | Customer order number for the project cost reporting entry. Entered per log in Authorize/adjust and copied from the work recording. |
| `GoodsMark` | `String` | no |  | max length 80, since 26.6 | Goods mark for the project cost reporting entry. Entered per log in Authorize/adjust and copied from the work recording. |
| `InternalCommentId` | `Int64?` | yes |  | since 26.6 | The business key identifier of the internal comment for the project cost reporting entry. |
| `InternalComment` | `Comments` | no | [Comments](Comment.md) | expandable, since 26.6 | The internal comment of the project cost reporting entry. |

## Example

```json
{
  "Id": 0,
  "Number": 0,
  "ProjectId": null,
  "IsIncome": false,
  "ActivityId": null,
  "ReportedTimeInHours": 0.0,
  "CostTypeId": null,
  "Amount": 0.0,
  "ReportingDate": "0001-01-01T00:00:00+00:00",
  "OurReferenceId": null,
  "OurReferenceName": null,
  "EmployeeId": null,
  "WorkCenterId": null,
  "DepartmentId": null,
  "IsCancelled": false,
  "CommentId": null,
  "Comment": null,
  "CustomerReference": null,
  "CustomerOrderNumber": null,
  "GoodsMark": null,
  "InternalCommentId": null,
  "InternalComment": null
}
```
