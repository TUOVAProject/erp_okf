---
type: API Module
title: TimeRecording
description: Monitor ERP API module TimeRecording.
tags:
- TimeRecording
- module
generated:
  by: process:monitor-okf-build
  from: 677a27684767
entity_count: 20
queryable_count: 20
---

# TimeRecording

Monitor API module `TimeRecording`: 20 queryable entities, 0 commands, 0 payload types.

Full listing: [TimeRecording entities](/entities/TimeRecording/index.md)

## Queryable entities

| Entity | Endpoint | Description |
| --- | --- | --- |
| [AbsenceCodes](/entities/TimeRecording/AbsenceCode.md) | `/api/v1/TimeRecording/AbsenceCodes` | Represents an absence code. Used in time recording to represent a period of absence. |
| [AdditionRecordings](/entities/TimeRecording/AdditionRecording.md) | `/api/v1/TimeRecording/AdditionRecordings` | Represents an additional recording |
| [AttendanceAdditions](/entities/TimeRecording/AttendanceAddition.md) | `/api/v1/TimeRecording/AttendanceAdditions` | Represents an attendance addition |
| [AttendanceChart](/entities/TimeRecording/AttendanceChart.md) | `/api/v1/TimeRecording/AttendanceChart` | Represents an attendance chart. |
| [AttendanceGroupSettings](/entities/TimeRecording/AttendanceGroupSettings.md) | `/api/v1/TimeRecording/AttendanceGroupSettings` | Represents an attendance group setting. |
| [AttendanceIntervals](/entities/TimeRecording/AttendanceInterval.md) | `/api/v1/TimeRecording/AttendanceIntervals` | Represents an attendance recording interval on a recording day. |
| [IndirectWorkCodes](/entities/TimeRecording/IndirectWorkCode.md) | `/api/v1/TimeRecording/IndirectWorkCodes` | Represents indirect work used for work recording. |
| [OvertimeTypes](/entities/TimeRecording/OvertimeType.md) | `/api/v1/TimeRecording/OvertimeTypes` | Represents a overtime type. |
| [PersonTimeBanks](/entities/TimeRecording/PersonTimeBank.md) | `/api/v1/TimeRecording/PersonTimeBanks` | Represents a persons time bank. |
| [PersonWorkCenters](/entities/TimeRecording/PersonWorkCenter.md) | `/api/v1/TimeRecording/PersonWorkCenters` | Represents a table that determines which work centers (and thereby which report numbers) the person should be allowed to select among in the priority plan and when starting work via report numbers. |
| [PlannedAbsences](/entities/TimeRecording/PlannedAbsence.md) | `/api/v1/TimeRecording/PlannedAbsences` | Represents a planned absence. |
| [RecordingDays](/entities/TimeRecording/RecordingDay.md) | `/api/v1/TimeRecording/RecordingDays` | Represents a Recording Day, which holds the attendance and work recordings which belongs to an employee for a specific date. |
| [SalaryTypes](/entities/TimeRecording/SalaryType.md) | `/api/v1/TimeRecording/SalaryTypes` | Represents a salary type. |
| [Schedules](/entities/TimeRecording/Schedule.md) | `/api/v1/TimeRecording/Schedules` | Represents a schedule used for time recording. |
| [Shedules](/entities/TimeRecording/Schedule_Obsolete.md) | `/api/v1/TimeRecording/Shedules` | Represents a schedule used for time recording. |
| [StandbyWorks](/entities/TimeRecording/StandbyWork.md) | `/api/v1/TimeRecording/StandbyWorks` | Represents a work put on standby. |
| [TimeBanks](/entities/TimeRecording/TimeBank.md) | `/api/v1/TimeRecording/TimeBanks` | Represents a time bank. |
| [WorkIntervals](/entities/TimeRecording/WorkInterval.md) | `/api/v1/TimeRecording/WorkIntervals` | Represents a work interval. |
| [WorkshopScheduleSalaryTypeRows](/entities/TimeRecording/WorkshopScheduleSalaryTypeRow.md) | `/api/v1/TimeRecording/WorkshopScheduleSalaryTypeRows` | Represent a workshop schedule salary type row. |
| [WorkshopScheduleSalaryTypes](/entities/TimeRecording/WorkshopScheduleSalaryType.md) | `/api/v1/TimeRecording/WorkshopScheduleSalaryTypes` | Represent a workshop schedule salary type |

## Depends on other modules

- [Common](/modules/Common.md): [Comments](/entities/Common/Comment.md), [Currencies](/entities/Common/Currency.md), [Persons](/entities/Common/Person.md), [ProjectActivities](/entities/Common/ProjectActivity.md), [ProjectCostTypes](/entities/Common/ProjectCostType.md), [Projects](/entities/Common/Project.md)
- [Manufacturing](/modules/Manufacturing.md): [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md), [WorkCenters](/entities/Manufacturing/WorkCenter.md)
