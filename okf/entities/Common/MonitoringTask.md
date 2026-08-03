---
type: API Entity
title: MonitoringTasks
description: Represents a monitoring task.
resource: https://api.monitor.se/api/Monitor.API.Common.MonitoringTask.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.MonitoringTask.html
  title: Monitor API — MonitoringTask
module: Common
api_class: MonitoringTask
doc_name: MonitoringTasks
endpoint: GET /api/v1/Common/MonitoringTasks
guid: 12a7006c-bc65-4e18-9029-4fe3d9854be0
permission: Create and handle all monitoring tasks
introduced_in: '24.7'
property_count: 13
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
referenced_by:
- /entities/Common/MonitoringTaskRecipient.md
- /entities/Common/MonitoringTaskRow.md
---

# MonitoringTasks

Represents a monitoring task.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `MonitoringTask`
- **Endpoint:** `GET /api/v1/Common/MonitoringTasks`
- **Required permission:** Create and handle all monitoring tasks
- **GUID:** `12a7006c-bc65-4e18-9029-4fe3d9854be0`
- **Introduced in:** 24.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the monitoring task. |
| `Number` | `String` | no |  | unique, max length 20 | The monitoring task number. |
| `Name` | `String` | no |  |  | The name of monitoring task. |
| `TaskType` | `Int32` | no |  | enum | The type of monitoring task. |
| `Status` | `Int32` | no |  | enum | The status of monitoring task. |
| `UseSchedule` | `Boolean` | no |  |  | Specifies if the monitoring task should be used in schedule. |
| `RunOnce` | `Boolean` | no |  |  | Specifies if the monitoring task should be deactivated when any of the terms are fulfilled. |
| `StartTime` | `DateTimeOffset?` | yes |  |  | The start time of the monitoring task. |
| `StopTime` | `DateTimeOffset?` | yes |  |  | The end time of the monitoring task. |
| `ApplicationUserId` | `Int64` | no | [ApplicationUsers](ApplicationUser.md) |  | The business key identifier of the application user that create the monitoring task. |
| `ApplicationUser` | `ApplicationUsers` | no | [ApplicationUsers](ApplicationUser.md) | expandable | The application user that create the monitoring task. |
| `CommentId` | `Int64` | no | [Comments](Comment.md) |  | The business key identifier of the monitoring task's comment. |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The monitoring task's comment. |

## Enumerations

### TaskType

| Name | Value |
| --- | ---: |
| `StockBalance` | 0 |
| `PersonActivity` | 1 |
| `CustomerActivity` | 2 |
| `QuoteActivity` | 3 |
| `CustomerOrderActivity` | 4 |
| `SupplierActivity` | 5 |
| `PartActivity` | 6 |
| `PurchaseOrderActivity` | 7 |
| `InquiryActivity` | 8 |
| `ManufacturingOrderOperation` | 9 |
| `ArrivalReporting` | 10 |
| `OrderRowArrivalReporting` | 11 |
| `BlanketOrderPurchaseActivity` | 12 |
| `BlanketOrderSalesActivity` | 13 |
| `SalesAgreementActivity` | 14 |
| `CaseEntryActivity` | 15 |
| `ExposureTime` | 16 |
| `BusinessOpportunityActivity` | 17 |
| `ProductRecordActivity` | 18 |
| `SupplierAgreementActivity` | 19 |

### Status

| Name | Value |
| --- | ---: |
| `Active` | 0 |
| `Disabled` | 1 |


## Referenced by

**Common**

- [MonitoringTaskRecipients](MonitoringTaskRecipient.md) — `TaskId` (FK)
- [MonitoringTaskRows](MonitoringTaskRow.md) — `TaskId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": null,
  "Name": null,
  "TaskType": 0,
  "Status": 0,
  "UseSchedule": false,
  "RunOnce": false,
  "StartTime": null,
  "StopTime": null,
  "ApplicationUserId": 0,
  "ApplicationUser": null,
  "CommentId": 0,
  "Comment": null
}
```
