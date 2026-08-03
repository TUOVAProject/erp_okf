---
type: API Entity
title: OvertimeTypes
description: Represents a overtime type.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.OvertimeType.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.OvertimeType.html
  title: Monitor API — OvertimeType
module: TimeRecording
api_class: OvertimeType
doc_name: OvertimeTypes
endpoint: GET /api/v1/TimeRecording/OvertimeTypes
guid: 42CF73A0-037C-4E61-93AC-F79B0D326348
permission: Show basic data for attendance
introduced_in: '2.26'
property_count: 3
referenced_by:
- /entities/TimeRecording/AttendanceGroupSettings.md
- /entities/TimeRecording/AttendanceInterval.md
- /entities/TimeRecording/WorkshopScheduleSalaryType.md
---

# OvertimeTypes

Represents a overtime type.

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `OvertimeType`
- **Endpoint:** `GET /api/v1/TimeRecording/OvertimeTypes`
- **Required permission:** Show basic data for attendance
- **GUID:** `42CF73A0-037C-4E61-93AC-F79B0D326348`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the overtime type. |
| `Code` | `String` | no |  |  | The human readable identifier of the overtime type. |
| `Description` | `String` | no |  |  | The translated description of the overtime type. |

## Referenced by

**TimeRecording**

- [AttendanceGroupSettings](AttendanceGroupSettings.md) — `OvertimeTypes` (expand)
- [AttendanceIntervals](AttendanceInterval.md) — `OvertimeTypeAfterId` (FK)
- [AttendanceIntervals](AttendanceInterval.md) — `OvertimeTypeBeforeId` (FK)
- [WorkshopScheduleSalaryTypes](WorkshopScheduleSalaryType.md) — `OvertimeTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null
}
```
