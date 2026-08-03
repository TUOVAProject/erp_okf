---
type: API Entity
title: AdditionRecordings
description: Represents an additional recording
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AdditionRecording.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AdditionRecording.html
  title: Monitor API — AdditionRecording
module: TimeRecording
api_class: AdditionRecording
doc_name: AdditionRecordings
endpoint: GET /api/v1/TimeRecording/AdditionRecordings
guid: 4175D402-D271-4DA7-8682-08248D31F5B3
permission: Show basic data for attendance
introduced_in: '22.7'
property_count: 16
references_out:
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/Project.md
- /entities/TimeRecording/AttendanceAddition.md
- /entities/TimeRecording/TimeBank.md
referenced_by:
- /entities/TimeRecording/RecordingDay.md
---

# AdditionRecordings

Represents an additional recording

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `AdditionRecording`
- **Endpoint:** `GET /api/v1/TimeRecording/AdditionRecordings`
- **Required permission:** Show basic data for attendance
- **GUID:** `4175D402-D271-4DA7-8682-08248D31F5B3`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the additional recording. |
| `AdditionType` | `Int32` | no |  | enum | Type of attendance addition |
| `AttendanceAdditionId` | `Int64` | no | [AttendanceAdditions](AttendanceAddition.md) |  | The business key identifier of attendance addition id. |
| `AttendanceAddition` | `AttendanceAdditions` | no | [AttendanceAdditions](AttendanceAddition.md) | expandable | Attendance addition. |
| `TimeBankId` | `Int64?` | yes | [TimeBanks](TimeBank.md) |  | The business key identifier of time bank. |
| `TimeBank` | `TimeBanks` | no | [TimeBanks](TimeBank.md) | expandable | Time bank |
| `TimeBankTransaction` | `Int32` | no |  | enum | Type of time bank transaction |
| `MandatoryComment` | `Boolean` | no |  |  | Specifies whether comment is mandatory or not. |
| `CommentId` | `Int64?` | yes |  |  | The comment id on the additional recording. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The comment on the additional recording. |
| `Amount` | `Decimal` | no |  |  | The amount of the additional recording. |
| `Cost` | `Decimal?` | yes |  |  | The cost of the additional recording. |
| `CostCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the additional recording cost currency. |
| `ProjectId` | `Int64?` | yes | [Projects](../Common/Project.md) |  | The business key identifier of the project this additional recording belongs to. |
| `IntervalStart` | `DateTimeOffset?` | yes |  |  | The start of the interval. |
| `IntervalEnd` | `DateTimeOffset?` | yes |  |  | The end of the interval. |

## Enumerations

### AdditionType

| Name | Value |
| --- | ---: |
| `Standard` | 0 |
| `SystemTimebankAdjustment` | 1 |

### TimeBankTransaction

| Name | Value |
| --- | ---: |
| `Increase` | 0 |
| `Decrease` | 1 |


## Referenced by

**TimeRecording**

- [RecordingDays](RecordingDay.md) — `Additions` (expand)


## Example

```json
{
  "Id": 0,
  "AdditionType": 0,
  "AttendanceAdditionId": 0,
  "AttendanceAddition": null,
  "TimeBankId": null,
  "TimeBank": null,
  "TimeBankTransaction": 0,
  "MandatoryComment": false,
  "CommentId": null,
  "Comment": null,
  "Amount": 0.0,
  "Cost": null,
  "CostCurrencyId": null,
  "ProjectId": null,
  "IntervalStart": null,
  "IntervalEnd": null
}
```
