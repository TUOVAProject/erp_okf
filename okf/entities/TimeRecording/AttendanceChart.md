---
type: API Entity
title: AttendanceChart
description: Represents an attendance chart.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AttendanceChart.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AttendanceChart.html
  title: Monitor API — AttendanceChart
module: TimeRecording
api_class: AttendanceChart
doc_name: AttendanceChart
endpoint: GET /api/v1/TimeRecording/AttendanceChart
permission: Show recording items
introduced_in: '2.18'
property_count: 21
references_out:
- /entities/Common/Person.md
- /entities/TimeRecording/RecordingDay.md
---

# AttendanceChart

Represents an attendance chart.

- **Module:** [TimeRecording](/modules/TimeRecording.md)
- **API class:** `AttendanceChart`
- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceChart`
- **Required permission:** Show recording items
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no | [RecordingDays](/entities/TimeRecording/RecordingDay.md) |  | The business key identifier of the latest recording day. |
| `RecordingDate` | `DateTime` | no |  |  | The date of the last recording. |
| `EmployeeId` | `Int64` | no | [Persons](/entities/Common/Person.md) |  | The business key identifier of the employee that the recording belongs to. |
| `EmployeeNumber` | `String` | no |  | max length 10 | The employee number of the recording employee. |
| `FirstName` | `String` | no |  | max length 35 | The first name of the recording employee. |
| `LastName` | `String` | no |  | max length 35 | The last name of the recording employee. |
| `InternalPhoneNumber` | `String` | no |  | max length 80 | The internal phone number of the recording employee. |
| `IsClosedInterval` | `Boolean` | no |  |  | Specifies if the interval of the attendance period has been closed. |
| `IntervalStart` | `DateTimeOffset` | no |  |  | When the interval started. |
| `IntervalEnd` | `DateTimeOffset` | no |  |  | When the interval ended. |
| `AbsenceCodeId` | `Int64?` | yes |  |  | The business key identifier of the recording's absence code. |
| `AbsenceCode` | `String` | no |  | max length 4 | The human readable identifier of the recording's absence code. |
| `AbsenceDescription` | `String` | no |  | max length 35 | The absence code description. |
| `IsBreak` | `Boolean` | no |  |  | Specifies if the interval is considered break time. |
| `ScheduleId` | `Int64?` | yes |  |  | The business key identifier of the schedule that the recording is based upon. |
| `AbsenceKind` | `Int32` | no |  |  | The absence kind of the recording. |
| `ScheduleType` | `Int32?` | yes |  |  | The schedule type of the recording. Represents Monitor.StrawberryFields.Shared.Workshop.WorkshopScheduleType 1 - Ordinary 2 - Overtime |
| `IsNightSchedule` | `Boolean?` | yes |  |  | Specifies if the recording falls under night schedule. |
| `ScheduleNumber` | `String` | no |  | max length 10 | The schedule number of the recording. |
| `DepartmentId` | `Int64` | no |  |  | The business key identifier of the department linked to the recording. |
| `DepartmentCode` | `String` | no |  | max length 6 | The department code of the recording. |

## Example

```json
{
  "Id": 0,
  "RecordingDate": "0001-01-01T00:00:00",
  "EmployeeId": 0,
  "EmployeeNumber": null,
  "FirstName": null,
  "LastName": null,
  "InternalPhoneNumber": null,
  "IsClosedInterval": false,
  "IntervalStart": "0001-01-01T00:00:00+00:00",
  "IntervalEnd": "0001-01-01T00:00:00+00:00",
  "AbsenceCodeId": null,
  "AbsenceCode": null,
  "AbsenceDescription": null,
  "IsBreak": false,
  "ScheduleId": null,
  "AbsenceKind": 0,
  "ScheduleType": null,
  "IsNightSchedule": null,
  "ScheduleNumber": null,
  "DepartmentId": 0,
  "DepartmentCode": null
}
```
