---
type: API Entity
title: WorkIntervals
description: Represents a work interval.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.WorkInterval.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.WorkInterval.html
  title: Monitor API — WorkInterval
module: TimeRecording
api_class: WorkInterval
doc_name: WorkIntervals
endpoint: GET /api/v1/TimeRecording/WorkIntervals
guid: 1063170E-A961-4F6C-A3D9-DE062CC98371
permission: Show recording items
introduced_in: '2.25'
property_count: 18
references_out:
- /entities/Common/Comment.md
- /entities/Common/Person.md
- /entities/Common/ProjectActivity.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Manufacturing/WorkCenter.md
- /entities/TimeRecording/IndirectWorkCode.md
referenced_by:
- /entities/TimeRecording/RecordingDay.md
---

# WorkIntervals

Represents a work interval.

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `WorkInterval`
- **Endpoint:** `GET /api/v1/TimeRecording/WorkIntervals`
- **Required permission:** Show recording items
- **GUID:** `1063170E-A961-4F6C-A3D9-DE062CC98371`
- **Introduced in:** 2.25

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of a work interval. |
| `IntervalStart` | `DateTimeOffset` | no |  |  | The start of the interval. |
| `IntervalEnd` | `DateTimeOffset` | no |  |  | The end of the interval. |
| `IsClosedInterval` | `Boolean` | no |  |  | Indicatates if the interval was ended. If false the interval is considered an active interval on the day which a future work recording is supposed to end. |
| `BundleId` | `Guid` | no |  |  | Identifier to detect what work was recorded in the same bundle. |
| `WorkRecordingType` | `Int32` | no |  | enum | What type of work this recording represents. Indicates which id is relevant on the interval. |
| `IndirectWorkCodeId` | `Int64?` | yes | [IndirectWorkCodes](IndirectWorkCode.md) |  | The business key identifier to an indirect work code. Defined if is indirect work. |
| `OperationId` | `Int64?` | yes | [ManufacturingOrderOperations](../Manufacturing/ManufacturingOrderOperation.md) |  | The business key identifier to a manufacturing order operation. Defined if it is an operation unit or a setup recording. |
| `TimeCalculationType` | `Int32` | no |  | enum | The time calculation type for this interval. |
| `ReportingEmployeeId` | `Int64` | no | [Persons](../Common/Person.md) |  | The business key identifier to the employee making the recording. When machine recording this key will represent the operator if defined. Otherwise this will be the same as the person owning the recording day. |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](../Manufacturing/WorkCenter.md) |  | The business key identifier to the workcenter associated with the recording. |
| `WorkedTime` | `TimeSpan` | no |  |  | The calculated work time for this interval. |
| `OfWichOvertime` | `TimeSpan` | no |  |  | How much of the worked time that was considered overtime. |
| `ReportedQuantity` | `Decimal` | no |  |  | The reported quantity for this recording. |
| `RejectedQuantity` | `Decimal` | no |  |  | The rejected quantity for this recording. |
| `ActivityId` | `Int64?` | yes | [ProjectActivities](../Common/ProjectActivity.md) | since 22.6 | The business key identifier to a project activity. Defined if it is a project activity. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) | since 23.8 | The business key identifier of the work interval comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable, since 23.8 | The comment of the work interval. |

## Enumerations

### WorkRecordingType

| Name | Value |
| --- | ---: |
| `Indirect` | 0 |
| `OperationSetup` | 1 |
| `OperationUnit` | 2 |
| `ProjectActivity` | 3 |

### TimeCalculationType

| Name | Value |
| --- | ---: |
| `RecordedTime` | 0 |
| `PreCalculatedTime` | 1 |
| `BundleDistributedRecordedTime` | 2 |


## Referenced by

**TimeRecording**

- [RecordingDays](RecordingDay.md) — `WorkIntervals` (expand)


## Example

```json
{
  "Id": 0,
  "IntervalStart": "0001-01-01T00:00:00+00:00",
  "IntervalEnd": "0001-01-01T00:00:00+00:00",
  "IsClosedInterval": false,
  "BundleId": "00000000-0000-0000-0000-000000000000",
  "WorkRecordingType": 0,
  "IndirectWorkCodeId": null,
  "OperationId": null,
  "TimeCalculationType": 0,
  "ReportingEmployeeId": 0,
  "WorkCenterId": null,
  "WorkedTime": "00:00:00",
  "OfWichOvertime": "00:00:00",
  "ReportedQuantity": 0.0,
  "RejectedQuantity": 0.0,
  "ActivityId": null,
  "CommentId": null,
  "Comment": null
}
```
