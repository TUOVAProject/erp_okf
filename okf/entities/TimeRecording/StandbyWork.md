---
type: API Entity
title: StandbyWorks
description: Represents a work put on standby.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.StandbyWork.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.StandbyWork.html
  title: Monitor API — StandbyWork
module: TimeRecording
api_class: StandbyWork
doc_name: StandbyWorks
endpoint: GET /api/v1/TimeRecording/StandbyWorks
guid: 2D0EFE39-5F0A-4FD5-86C4-2E497793ED96
permission: Show recording items
introduced_in: '2.26'
property_count: 9
references_out:
- /entities/Common/Person.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/TimeRecording/IndirectWorkCode.md
---

# StandbyWorks

Represents a work put on standby.

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `StandbyWork`
- **Endpoint:** `GET /api/v1/TimeRecording/StandbyWorks`
- **Required permission:** Show recording items
- **GUID:** `2D0EFE39-5F0A-4FD5-86C4-2E497793ED96`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the standby work. |
| `EmployeeId` | `Int64` | no | [Persons](../Common/Person.md) |  | The business key identifier of the employee who has this work on standby. |
| `BundleId` | `Guid` | no |  |  | The bundle id of the work. Used to identify if work should be started as a bundle when restarting. |
| `WorkRecordingType` | `Int32` | no |  | enum | What type of work this represents. |
| `IndirectWorkCodeId` | `Int64?` | yes | [IndirectWorkCodes](IndirectWorkCode.md) |  | The business key identifier of the indirect work code, defined when WorkRecordingType is Indirect. |
| `IndirectWorkCode` | `IndirectWorkCodes` | no | [IndirectWorkCodes](IndirectWorkCode.md) | expandable | The indirect work code, available when WorkRecordingType is Indirect. |
| `OperationId` | `Int64?` | yes | [ManufacturingOrderOperations](../Manufacturing/ManufacturingOrderOperation.md) |  | The business key identifier of the operation, defined when WorkRecordingType is OperationSetup or OperationUnit. |
| `Operation` | `ManufacturingOrderOperations` | no | [ManufacturingOrderOperations](../Manufacturing/ManufacturingOrderOperation.md) | expandable | The operation for this work, available when WorkRecordingType is OperationSetup or OperationUnit. |
| `ActivityId` | `Int64?` | yes |  |  | The business key identifier of the activity, defined when WorkRecordingType is Activity. References a project activity. |

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
  "EmployeeId": 0,
  "BundleId": "00000000-0000-0000-0000-000000000000",
  "WorkRecordingType": 0,
  "IndirectWorkCodeId": null,
  "IndirectWorkCode": null,
  "OperationId": null,
  "Operation": null,
  "ActivityId": null
}
```
