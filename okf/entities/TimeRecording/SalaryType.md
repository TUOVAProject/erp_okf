---
type: API Entity
title: SalaryTypes
description: Represents a salary type.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.SalaryType.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.SalaryType.html
  title: Monitor API — SalaryType
module: TimeRecording
api_class: SalaryType
doc_name: SalaryTypes
endpoint: GET /api/v1/TimeRecording/SalaryTypes
guid: 072C3C10-AC56-4CDC-9FB3-247F6D0F2D19
permission: Show basic data for attendance
introduced_in: '2.26'
property_count: 3
referenced_by:
- /entities/TimeRecording/AttendanceAddition.md
- /entities/TimeRecording/AttendanceGroupSettings.md
- /entities/TimeRecording/WorkshopScheduleSalaryType.md
---

# SalaryTypes

Represents a salary type.

- **Module:** [TimeRecording](/modules/TimeRecording.md)
- **API class:** `SalaryType`
- **Endpoint:** `GET /api/v1/TimeRecording/SalaryTypes`
- **Required permission:** Show basic data for attendance
- **GUID:** `072C3C10-AC56-4CDC-9FB3-247F6D0F2D19`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the salary type. |
| `Code` | `String` | no |  |  | The human readable identifier of the salary type. |
| `Description` | `String` | no |  |  | The translated description of the salary type. |

## Referenced by

**TimeRecording**

- [AttendanceAdditions](/entities/TimeRecording/AttendanceAddition.md) — `SalaryTypes` (expand)
- [AttendanceGroupSettings](/entities/TimeRecording/AttendanceGroupSettings.md) — `SalaryTypeForNegativeFlex` (FK)
- [AttendanceGroupSettings](/entities/TimeRecording/AttendanceGroupSettings.md) — `SalaryTypeForPositiveFlex` (FK)
- [AttendanceGroupSettings](/entities/TimeRecording/AttendanceGroupSettings.md) — `SalaryTypeForScheduleLessRecording` (FK)
- [WorkshopScheduleSalaryTypes](/entities/TimeRecording/WorkshopScheduleSalaryType.md) — `SalaryTypes` (expand)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null
}
```
