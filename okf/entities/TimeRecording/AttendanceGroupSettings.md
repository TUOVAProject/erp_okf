---
type: API Entity
title: AttendanceGroupSettings
description: Represents an attendance group setting.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AttendanceGroupSettings.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AttendanceGroupSettings.html
  title: Monitor API — AttendanceGroupSettings
module: TimeRecording
api_class: AttendanceGroupSettings
doc_name: AttendanceGroupSettings
endpoint: GET /api/v1/TimeRecording/AttendanceGroupSettings
guid: 22F83797-8309-4B93-B483-B0B63FF38D9F
permission: Show basic data for attendance
introduced_in: '22.1'
property_count: 39
references_out:
- /entities/TimeRecording/AbsenceCode.md
- /entities/TimeRecording/IndirectWorkCode.md
- /entities/TimeRecording/OvertimeType.md
- /entities/TimeRecording/SalaryType.md
- /entities/TimeRecording/TimeBank.md
---

# AttendanceGroupSettings

Represents an attendance group setting.

- **Module:** [TimeRecording](/modules/TimeRecording.md)
- **API class:** `AttendanceGroupSettings`
- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceGroupSettings`
- **Required permission:** Show basic data for attendance
- **GUID:** `22F83797-8309-4B93-B483-B0B63FF38D9F`
- **Introduced in:** 22.1

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the attendance group setting. |
| `AllowAttendanceRecordingAdditionsInRecordingTerminal` | `Boolean` | no |  |  | Indicates if attendance recording additions is allowed in the recording terminal. |
| `AllowAttendanceRecordingAdjustmentsInRecordingTerminal` | `Boolean` | no |  |  | Indicates if attendance recording adjustments are allowed in the recording terminal. |
| `AllowShorterWorkingHours` | `Boolean` | no |  |  | Indicates if shorter working hours are allowed. |
| `GenerateShorterWorkingHoursForHoliday` | `Boolean` | no |  |  | Indicates if shorter working hours for holidays should be generated. |
| `Description` | `String` | no |  |  | The translated description of the attendance group setting. |
| `AbsenceCheck` | `Boolean` | no |  |  | Indicates if absences should be checked. |
| `NonRegulatedWorkinghours` | `Boolean` | no |  |  | Indicates if non regulated working hours are allowed. |
| `AddRoundOffOvertimeToTimeBank` | `Int32` | no |  | enum | The round off for overtime to the time bank. |
| `Name` | `String` | no |  | unique, max length 8 | The name of the attendance group setting. |
| `AllowOvertime` | `Boolean` | no |  |  | Indicates if overtime is allowed. |
| `AllowAbsenceRecordingInNegativeFlexZones` | `Boolean` | no |  |  | Indicates if absence recording is allowed within negative flex zones. |
| `AutomaticOvertimeQuestionOutsideSchedule` | `Boolean` | no |  |  | Indicates if there should be a dialog for overtime outside of the schedule. |
| `CalculationBase` | `Int32` | no |  | enum | The calculation base type for shorter working hours. |
| `CalculationFactor` | `TimeSpan` | no |  |  | The calculation factor. |
| `CalculateOvertime` | `Int32` | no |  | enum | Indicates how overtime is calculated. |
| `FlexTime` | `Boolean` | no |  |  | Indicates if flex time is allowed. |
| `SalaryTypeForPositiveFlex` | `Int64?` | yes | [SalaryTypes](/entities/TimeRecording/SalaryType.md) |  | The salary type for positive flex. |
| `SalaryTypeForNegativeFlex` | `Int64?` | yes | [SalaryTypes](/entities/TimeRecording/SalaryType.md) |  | The salary type for negative flex. |
| `CalculateFlextime` | `Int32` | no |  | enum, since 24.8 | Indicates how flex is calculated. |
| `SalaryTypeForScheduleLessRecording` | `Int64?` | yes | [SalaryTypes](/entities/TimeRecording/SalaryType.md) |  | The salary type for schedule less recordings. |
| `MinTimePerDay` | `TimeSpan` | no |  |  | The minimum time the employee has to work for shorter working hours to apply when using per day calculation. |
| `NegativeFlexIncludedInDailyHours` | `Boolean` | no |  |  | Indicates if negative flex should be included in daily hours. |
| `NumberOfDaysBackInTimeThatCanBeAdjusted` | `Int32` | no |  |  | Determains how many days are adjustable back in time. |
| `NumberOfDaysBackInTimeThatCanBeEdited` | `Int32` | no |  |  | Determains how many days are editable back in time. |
| `OvertimeInFlexZone` | `Boolean` | no |  |  | Indicates if overtime is allowed within flex zone. |
| `OvertimeLimitAfter` | `TimeSpan` | no |  |  | The overtime limit after the end of the schedule. |
| `OvertimeLimitBefore` | `TimeSpan` | no |  |  | The overtime limit before the start of the schedule. |
| `PlanAbsenceViaRecordingTerminal` | `Boolean` | no |  |  | Indicates if planned absence is allowed from the recording terminal. |
| `RoundOffOvertime` | `Boolean` | no |  |  | Indicates if round off overtime should be used. |
| `RoundOffOvertimeTimebankId` | `Int64?` | yes | [TimeBanks](/entities/TimeRecording/TimeBank.md) |  | The timebank to use for round off overtime. |
| `RoundOffTo` | `TimeSpan` | no |  |  | The time to round off overtime to. |
| `SalaryTypeAccordingToOvertime` | `Boolean` | no |  |  | Indicates if salary type should be calculated from the start of the overtime schedule, not from where it was recorded. |
| `ShorterWorkingHoursTimeBankId` | `Int64?` | yes | [TimeBanks](/entities/TimeRecording/TimeBank.md) |  | The time bank to use for shorter working hours. |
| `TimeAfterScheduleEnd` | `TimeSpan` | no |  |  | Threshold for automatic overtime question after schedule end in recording terminal. |
| `TimeBeforeScheduleStart` | `TimeSpan` | no |  |  | Threshold for automatic overtime question before schedule start in recording terminal. |
| `UnavailableAbsenceCodes` | `AbsenceCodes[]` | no | [AbsenceCodes](/entities/TimeRecording/AbsenceCode.md) | expandable, collection, since 22.3 | Unavailable absence codes for the attendance group setting. |
| `OvertimeTypes` | `OvertimeTypes[]` | no | [OvertimeTypes](/entities/TimeRecording/OvertimeType.md) | expandable, collection, since 23.4 | The overtime types for the attendance group setting. |
| `IndirectWorkCodeId` | `Int64?` | yes | [IndirectWorkCodes](/entities/TimeRecording/IndirectWorkCode.md) | since 23.4 | The business key identifier of the indirect work. |

## Enumerations

### AddRoundOffOvertimeToTimeBank

| Name | Value |
| --- | ---: |
| `No` | 1 |
| `AllTime` | 2 |
| `TimeWithinFlexZone` | 3 |

### CalculationBase

| Name | Value |
| --- | ---: |
| `Day` | 1 |
| `Hour` | 2 |
| `AccordingToSchedule` | 3 |

### CalculateOvertime

| Name | Value |
| --- | ---: |
| `AllRecordedOvertime` | 0 |
| `AfterFulfilledDailyHours` | 1 |

### CalculateFlextime

| Name | Value |
| --- | ---: |
| `AllRecordedFlex` | 0 |
| `AfterFulfilledDailyHours` | 1 |


## Example

```json
{
  "Id": 0,
  "AllowAttendanceRecordingAdditionsInRecordingTerminal": false,
  "AllowAttendanceRecordingAdjustmentsInRecordingTerminal": false,
  "AllowShorterWorkingHours": false,
  "GenerateShorterWorkingHoursForHoliday": false,
  "Description": null,
  "AbsenceCheck": false,
  "NonRegulatedWorkinghours": false,
  "AddRoundOffOvertimeToTimeBank": 0,
  "Name": null,
  "AllowOvertime": false,
  "AllowAbsenceRecordingInNegativeFlexZones": false,
  "AutomaticOvertimeQuestionOutsideSchedule": false,
  "CalculationBase": 0,
  "CalculationFactor": "00:00:00",
  "CalculateOvertime": 0,
  "FlexTime": false,
  "SalaryTypeForPositiveFlex": null,
  "SalaryTypeForNegativeFlex": null,
  "CalculateFlextime": 0,
  "SalaryTypeForScheduleLessRecording": null,
  "MinTimePerDay": "00:00:00",
  "NegativeFlexIncludedInDailyHours": false,
  "NumberOfDaysBackInTimeThatCanBeAdjusted": 0,
  "NumberOfDaysBackInTimeThatCanBeEdited": 0,
  "OvertimeInFlexZone": false,
  "OvertimeLimitAfter": "00:00:00",
  "OvertimeLimitBefore": "00:00:00",
  "PlanAbsenceViaRecordingTerminal": false,
  "RoundOffOvertime": false,
  "RoundOffOvertimeTimebankId": null,
  "RoundOffTo": "00:00:00",
  "SalaryTypeAccordingToOvertime": false,
  "ShorterWorkingHoursTimeBankId": null,
  "TimeAfterScheduleEnd": "00:00:00",
  "TimeBeforeScheduleStart": "00:00:00",
  "UnavailableAbsenceCodes": null,
  "OvertimeTypes": null,
  "IndirectWorkCodeId": null
}
```
