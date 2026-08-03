---
type: API Entity
title: RecordingDays
description: Represents a Recording Day, which holds the attendance and work recordings
  which belongs to an employee for a specific date.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.RecordingDay.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.RecordingDay.html
  title: Monitor API — RecordingDay
module: TimeRecording
api_class: RecordingDay
doc_name: RecordingDays
endpoint: GET /api/v1/TimeRecording/RecordingDays
guid: 0E8C9FCB-5AA5-4075-8FD0-2CF9305FCE4F
permission: Show recording items
introduced_in: '2.25'
property_count: 17
references_out:
- /entities/Common/Person.md
- /entities/TimeRecording/AdditionRecording.md
- /entities/TimeRecording/AttendanceInterval.md
- /entities/TimeRecording/WorkInterval.md
referenced_by:
- /entities/TimeRecording/AttendanceChart.md
---

# RecordingDays

Represents a Recording Day, which holds the attendance and work recordings which belongs to an employee for a specific date.

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `RecordingDay`
- **Endpoint:** `GET /api/v1/TimeRecording/RecordingDays`
- **Required permission:** Show recording items
- **GUID:** `0E8C9FCB-5AA5-4075-8FD0-2CF9305FCE4F`
- **Introduced in:** 2.25

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the recording day. |
| `RecordingDate` | `DateTime` | no |  |  | The date this recording day belongs to. |
| `PersonId` | `Int64` | no | [Persons](../Common/Person.md) |  | The business key identifier of the Employee that this recording day belongs to. |
| `ScheduleId` | `Int64?` | yes |  |  | The business key identifier of the workshop schedule assigned to this day. Null if recording without schedule. |
| `OvertimeScheduleId` | `Int64?` | yes |  |  | The business key identifier of the workshop overtime schedule assigned to this day. Null if recording without overtime schedule. |
| `CalculatedScheduleDiff` | `TimeSpan` | no |  |  | The calculated difference between the schedule length and the sum of recorded attendance and absence on the day. |
| `CalculatedFlex` | `TimeSpan` | no |  |  | The days calculated total flex-time. |
| `CalculatedOvertime` | `TimeSpan` | no |  |  | The days calculated total overtime. |
| `CalculatedAbsence` | `TimeSpan` | no |  |  | The days calculated total absence. |
| `CalculatedAttendance` | `TimeSpan` | no |  |  | The days calculated total attendance. |
| `Exported` | `Boolean` | no |  |  | Indicatates if the day has been exported by the salary export system. When true the creation of new or modification of existing attendance recordings is not allowed. |
| `Authorized` | `Boolean` | no |  |  | Indicatates if the day has been authorized. |
| `AttendanceIntervals` | `AttendanceIntervals[]` | no | [AttendanceIntervals](AttendanceInterval.md) | expandable, collection | The recorded attendance intervals belonging to this day. |
| `WorkIntervals` | `WorkIntervals[]` | no | [WorkIntervals](WorkInterval.md) | expandable, collection | The recorded work intervals belonging to this day. |
| `Additions` | `AdditionRecordings[]` | no | [AdditionRecordings](AdditionRecording.md) | expandable, collection | Additional recordings belonging to this day. |
| `Approved` | `Boolean` | no |  | since 22.1 | Indicates that the employee is finished with the adding or adjustments. |
| `CommentText` | `String` | no |  | since 22.7 | Recording comment |

## Referenced by

**TimeRecording**

- [AttendanceChart](AttendanceChart.md) — `Id` (FK)


## Example

```json
{
  "Id": 0,
  "RecordingDate": "0001-01-01T00:00:00",
  "PersonId": 0,
  "ScheduleId": null,
  "OvertimeScheduleId": null,
  "CalculatedScheduleDiff": "00:00:00",
  "CalculatedFlex": "00:00:00",
  "CalculatedOvertime": "00:00:00",
  "CalculatedAbsence": "00:00:00",
  "CalculatedAttendance": "00:00:00",
  "Exported": false,
  "Authorized": false,
  "AttendanceIntervals": null,
  "WorkIntervals": null,
  "Additions": null,
  "Approved": false,
  "CommentText": null
}
```
