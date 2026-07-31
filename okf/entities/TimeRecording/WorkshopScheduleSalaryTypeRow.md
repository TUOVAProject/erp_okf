---
type: API Entity
title: WorkshopScheduleSalaryTypeRows
description: Represent a workshop schedule salary type row.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.WorkshopScheduleSalaryTypeRow.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.WorkshopScheduleSalaryTypeRow.html
  title: Monitor API — WorkshopScheduleSalaryTypeRow
module: TimeRecording
api_class: WorkshopScheduleSalaryTypeRow
doc_name: WorkshopScheduleSalaryTypeRows
endpoint: GET /api/v1/TimeRecording/WorkshopScheduleSalaryTypeRows
guid: 5C3DA91E-9C7D-4590-852E-4D0FEB1CAA9D
permission: Show basic data for attendance
introduced_in: '24.4'
property_count: 5
references_out:
- /entities/TimeRecording/Schedule.md
referenced_by:
- /entities/TimeRecording/WorkshopScheduleSalaryType.md
---

# WorkshopScheduleSalaryTypeRows

Represent a workshop schedule salary type row.

- **Module:** [TimeRecording](/modules/TimeRecording.md)
- **API class:** `WorkshopScheduleSalaryTypeRow`
- **Endpoint:** `GET /api/v1/TimeRecording/WorkshopScheduleSalaryTypeRows`
- **Required permission:** Show basic data for attendance
- **GUID:** `5C3DA91E-9C7D-4590-852E-4D0FEB1CAA9D`
- **Introduced in:** 24.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the row |
| `ScheduleId` | `Int64` | no | [Schedules](/entities/TimeRecording/Schedule.md) |  | The business key identifier of schedule |
| `Start` | `Int64?` | yes |  |  | Information about the start of the salary type row |
| `End` | `Int64?` | yes |  |  | Information about the end of the salary type row |
| `RowNumber` | `Int32?` | yes |  |  | The row number of the workshop salary type row. |

## Referenced by

**TimeRecording**

- [WorkshopScheduleSalaryTypes](/entities/TimeRecording/WorkshopScheduleSalaryType.md) — `WorkshopScheduleSalaryTypeRowId` (FK)


## Example

```json
{
  "Id": 0,
  "ScheduleId": 0,
  "Start": null,
  "End": null,
  "RowNumber": null
}
```
