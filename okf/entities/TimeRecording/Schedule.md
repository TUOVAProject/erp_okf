---
type: API Entity
title: Schedules
description: Represents a schedule used for time recording.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.Schedule.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.Schedule.html
  title: Monitor API — Schedule
module: TimeRecording
api_class: Schedule
doc_name: Schedules
endpoint: GET /api/v1/TimeRecording/Schedules
guid: 7A50172F-FE1F-40F7-9BDA-6C8566C34991
permission: Show basic data for attendance
introduced_in: '22.2'
property_count: 22
references_out:
- /entities/Common/Comment.md
- /entities/TimeRecording/Schedule.md
referenced_by:
- /entities/Common/Person.md
- /entities/Manufacturing/ProductionCalendarException.md
- /entities/TimeRecording/Schedule.md
- /entities/TimeRecording/WorkshopScheduleSalaryTypeRow.md
---

# Schedules

Represents a schedule used for time recording.

- **Module:** [TimeRecording](/modules/TimeRecording.md)
- **API class:** `Schedule`
- **Endpoint:** `GET /api/v1/TimeRecording/Schedules`
- **Required permission:** Show basic data for attendance
- **GUID:** `7A50172F-FE1F-40F7-9BDA-6C8566C34991`
- **Introduced in:** 22.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the schedule. |
| `Code` | `String` | no |  |  | The human readable identifier of the schedule. |
| `Description` | `String` | no |  |  | The translated description of the schedule. |
| `ScheduleLength` | `Int64` | no |  | since 23.1 | The length of the schedule. |
| `Start` | `Int64` | no |  | since 23.1 | Information about the start of the schedule. |
| `End` | `Int64` | no |  | since 23.1 | Information about the end of the schedule. |
| `OvertimeScheduleId` | `Int64?` | yes | [Schedules](/entities/TimeRecording/Schedule.md) | since 23.1 | The business key identifier of the Overtime schedule. |
| `FlexInStart` | `Int64?` | yes |  | since 23.1 | The flex in start of the schedule. |
| `FlexInEnd` | `Int64?` | yes |  | since 23.1 | The flex in end of the schedule. |
| `FlexOutStart` | `Int64?` | yes |  | since 23.1 | The flex out start of the schedule. |
| `FlexOutEnd` | `Int64?` | yes |  | since 23.1 | The flex out end of the schedule. |
| `IsNightSchedule` | `Boolean` | no |  | since 23.1 | The boolean value for the night schedule. |
| `Type` | `Int32` | no |  | bitmask, enum, since 23.1 | A type of schedule. |
| `AmountSwh` | `Decimal?` | yes |  | since 24.4 | The amount of shorter work hours (SWH) |
| `ScheduleNumberForExport` | `String` | no |  | since 24.4 | The schedule number for export |
| `BlockedContextType` | `Int32` | no |  | bitmask, enum, since 24.4 | The context type of block |
| `BlockedById` | `Int64?` | yes |  | since 24.4 | The business key identifier of the application user that blocked the entity. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  | since 24.4 | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  | since 24.4 | The date when the entity stops being blocked. |
| `BlockedStatus` | `Int32` | no |  | enum, since 24.4 | The block status of the entity. |
| `BlockMessageId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) | since 24.4 | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable, since 24.4 | The entity block message comment |

## Enumerations

### Type (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `Ordinary` | 1 |
| `Overtime` | 2 |

### BlockedContextType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `RegisterScheduleCycle` | 1 |
| `CreateRecording` | 2 |

### BlockedStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Message` | 1 |
| `Blocked` | 2 |


## Referenced by

**Common**

- [Persons](/entities/Common/Person.md) — `AvailableWorkshopSchedules` (expand)

**Manufacturing**

- [ProductionCalendarExceptions](/entities/Manufacturing/ProductionCalendarException.md) — `ScheduleId` (FK)

**TimeRecording**

- [Schedules](/entities/TimeRecording/Schedule.md) — `OvertimeScheduleId` (FK)
- [WorkshopScheduleSalaryTypeRows](/entities/TimeRecording/WorkshopScheduleSalaryTypeRow.md) — `ScheduleId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "ScheduleLength": 0,
  "Start": 0,
  "End": 0,
  "OvertimeScheduleId": null,
  "FlexInStart": null,
  "FlexInEnd": null,
  "FlexOutStart": null,
  "FlexOutEnd": null,
  "IsNightSchedule": false,
  "Type": 0,
  "AmountSwh": null,
  "ScheduleNumberForExport": null,
  "BlockedContextType": 0,
  "BlockedById": null,
  "BlockedFromDate": null,
  "BlockedToDate": null,
  "BlockedStatus": 0,
  "BlockMessageId": null,
  "BlockMessage": null
}
```
