---
type: API Entity
title: DelegatedWork
description: Represents a delegated work.
resource: https://api.monitor.se/api/Monitor.API.Common.DelegatedWork.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.DelegatedWork.html
  title: Monitor API — DelegatedWork
module: Common
api_class: DelegatedWork
doc_name: DelegatedWork
endpoint: GET /api/v1/Common/DelegatedWork
guid: 513d6e5f-1b35-4530-9034-e153b4c33185
permission: Show Activity list – Project
introduced_in: '2.50'
property_count: 6
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Person.md
- /entities/Common/ProjectActivity.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
---

# DelegatedWork

Represents a delegated work.

- **Module:** [Common](/modules/Common.md)
- **API class:** `DelegatedWork`
- **Endpoint:** `GET /api/v1/Common/DelegatedWork`
- **Required permission:** Show Activity list – Project
- **GUID:** `513d6e5f-1b35-4530-9034-e153b4c33185`
- **Introduced in:** 2.50

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the delegated work. |
| `WorkRecordingType` | `Int32` | no |  | enum | The work recording type of the delegated work. |
| `DelegatedBy` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the user who delegated the work. |
| `EmployeeId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the employee the work is delegated to. |
| `ActivityId` | `Int64?` | yes | [ProjectActivities](/entities/Common/ProjectActivity.md) |  | The business key identifier of the delegated work's activity. |
| `OperationId` | `Int64?` | yes | [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) |  | The business key identifier of the delegated work's operation. |

## Enumerations

### WorkRecordingType

| Name | Value |
| --- | ---: |
| `Indirect` | 0 |
| `OperationSetup` | 1 |
| `OperationUnit` | 2 |
| `ProjectActivity` | 3 |


## Example

```json
{
  "Id": 0,
  "WorkRecordingType": 0,
  "DelegatedBy": null,
  "EmployeeId": null,
  "ActivityId": null,
  "OperationId": null
}
```
