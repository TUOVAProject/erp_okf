---
type: API Entity
title: MonitoringTaskRecipients
description: Represents a recipient for monitoring task.
resource: https://api.monitor.se/api/Monitor.API.Common.MonitoringTaskRecipient.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.MonitoringTaskRecipient.html
  title: Monitor API — MonitoringTaskRecipient
module: Common
api_class: MonitoringTaskRecipient
doc_name: MonitoringTaskRecipients
endpoint: GET /api/v1/Common/MonitoringTaskRecipients
guid: 03362f10-226d-4ddc-ba14-9892a9abef89
permission: Create and handle all monitoring tasks
introduced_in: '24.7'
property_count: 6
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/LanguageCode.md
- /entities/Common/MonitoringTask.md
---

# MonitoringTaskRecipients

Represents a recipient for monitoring task.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `MonitoringTaskRecipient`
- **Endpoint:** `GET /api/v1/Common/MonitoringTaskRecipients`
- **Required permission:** Create and handle all monitoring tasks
- **GUID:** `03362f10-226d-4ddc-ba14-9892a9abef89`
- **Introduced in:** 24.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier key of the monitoring task recipient. |
| `TaskId` | `Int64` | no | [MonitoringTasks](MonitoringTask.md) |  | The business key identifier of the monitoring task that the recipient belongs to. |
| `LanguageCodeId` | `Int64` | no | [LanguageCodes](LanguageCode.md) |  | The business key identifier of the language code used in the recipient. |
| `RecipientType` | `Int32` | no |  | enum | Specifies the type of the monitoring task's recipient. |
| `Email` | `String` | no |  | max length 2500 | Specifies the mail of recipient if recipient type is email. |
| `ApplicationUserId` | `Int64` | no | [ApplicationUsers](ApplicationUser.md) |  | The business key identifier of the application user of the monitoring task's recipient. |

## Enumerations

### RecipientType

| Name | Value |
| --- | ---: |
| `EmailRecipient` | 0 |
| `NotificationRecipient` | 1 |
| `UserEmailRecipient` | 2 |


## Example

```json
{
  "Id": 0,
  "TaskId": 0,
  "LanguageCodeId": 0,
  "RecipientType": 0,
  "Email": null,
  "ApplicationUserId": 0
}
```
