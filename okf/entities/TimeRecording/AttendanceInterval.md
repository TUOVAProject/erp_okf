---
type: API Entity
title: AttendanceIntervals
description: Represents an attendance recording interval on a recording day.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AttendanceInterval.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AttendanceInterval.html
  title: Monitor API — AttendanceInterval
module: TimeRecording
api_class: AttendanceInterval
doc_name: AttendanceIntervals
endpoint: GET /api/v1/TimeRecording/AttendanceIntervals
guid: AF05FFA8-2F8E-43CA-9F65-790C8182B170
permission: Show recording items
introduced_in: '2.25'
property_count: 14
references_out:
- /entities/TimeRecording/AbsenceCode.md
- /entities/TimeRecording/OvertimeType.md
referenced_by:
- /entities/TimeRecording/RecordingDay.md
---

# AttendanceIntervals

Represents an attendance recording interval on a recording day.

- **Module:** [TimeRecording](/modules/TimeRecording.md)
- **API class:** `AttendanceInterval`
- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceIntervals`
- **Required permission:** Show recording items
- **GUID:** `AF05FFA8-2F8E-43CA-9F65-790C8182B170`
- **Introduced in:** 2.25

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of an attendance interval. |
| `IntervalStart` | `DateTimeOffset` | no |  |  | The start of the interval. |
| `IntervalEnd` | `DateTimeOffset` | no |  |  | The end of the interval. |
| `IsClosedInterval` | `Boolean` | no |  |  | Indicatates if the interval was ended. If false the interval is considered the active interval on the day which the next attendance recording is supposed to end. |
| `AbsenceCodeId` | `Int64?` | yes | [AbsenceCodes](/entities/TimeRecording/AbsenceCode.md) |  | The business key identifier of an absence code. If defined this interval is an absence recording. References a AbsenceCodes |
| `DeductedIfDailyHoursNotFulfilledOverride` | `Boolean?` | yes |  |  | Used to per recording be able to override the setting from an absence code if it should affect deduction of overtime. |
| `OvertimeTypeBeforeId` | `Int64?` | yes | [OvertimeTypes](/entities/TimeRecording/OvertimeType.md) |  | The business key identifier of an overtime type selected at the start of the interval. References a OvertimeTypes |
| `OvertimeTypeAfterId` | `Int64?` | yes | [OvertimeTypes](/entities/TimeRecording/OvertimeType.md) |  | The business key identifier of an overtime type selected at the end of the interval. References a OvertimeTypes |
| `IsBreak` | `Boolean` | no |  |  | Indicates if this is a break recording. |
| `IsAutomaticOut` | `Boolean` | no |  |  | Indicates if this was an automatic clock-out recording due to forgotten clock-out the previous day. |
| `AbsenceKind` | `Int32` | no |  | enum | Specifies the absence kind recorded for this interval. |
| `CalculatedTime` | `TimeSpan` | no |  |  | The recorded time for this interval after schedule and settings has been taken into account. |
| `CalculatedOvertimeBefore` | `TimeSpan` | no |  |  | The amount of overtime before schedule start. |
| `CalculatedOvertimeAfter` | `TimeSpan` | no |  |  | The amount of overtime after schedule end. |

## Enumerations

### AbsenceKind

| Name | Value |
| --- | ---: |
| `Default` | 0 |
| `Planned` | 1 |
| `Approved` | 2 |
| `TimeCard` | 3 |
| `NotContinue` | 4 |


## Referenced by

**TimeRecording**

- [RecordingDays](/entities/TimeRecording/RecordingDay.md) — `AttendanceIntervals` (expand)


## Example

```json
{
  "Id": 0,
  "IntervalStart": "0001-01-01T00:00:00+00:00",
  "IntervalEnd": "0001-01-01T00:00:00+00:00",
  "IsClosedInterval": false,
  "AbsenceCodeId": null,
  "DeductedIfDailyHoursNotFulfilledOverride": null,
  "OvertimeTypeBeforeId": null,
  "OvertimeTypeAfterId": null,
  "IsBreak": false,
  "IsAutomaticOut": false,
  "AbsenceKind": 0,
  "CalculatedTime": "00:00:00",
  "CalculatedOvertimeBefore": "00:00:00",
  "CalculatedOvertimeAfter": "00:00:00"
}
```
