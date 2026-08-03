---
type: API Entity
title: WorkshopScheduleSalaryTypes
description: Represent a workshop schedule salary type
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.WorkshopScheduleSalaryType.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.WorkshopScheduleSalaryType.html
  title: Monitor API — WorkshopScheduleSalaryType
module: TimeRecording
api_class: WorkshopScheduleSalaryType
doc_name: WorkshopScheduleSalaryTypes
endpoint: GET /api/v1/TimeRecording/WorkshopScheduleSalaryTypes
guid: 830EA6C4-4310-44AB-9B47-565BE491ED8F
permission: Show basic data for attendance
introduced_in: '24.4'
property_count: 6
references_out:
- /entities/TimeRecording/OvertimeType.md
- /entities/TimeRecording/SalaryType.md
- /entities/TimeRecording/WorkshopScheduleSalaryTypeRow.md
---

# WorkshopScheduleSalaryTypes

Represent a workshop schedule salary type

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `WorkshopScheduleSalaryType`
- **Endpoint:** `GET /api/v1/TimeRecording/WorkshopScheduleSalaryTypes`
- **Required permission:** Show basic data for attendance
- **GUID:** `830EA6C4-4310-44AB-9B47-565BE491ED8F`
- **Introduced in:** 24.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of workshop schedule salary type |
| `WorkshopScheduleSalaryTypeRowId` | `Int64` | no | [WorkshopScheduleSalaryTypeRows](WorkshopScheduleSalaryTypeRow.md) |  | The business key identifier of workshop schedule salary type row |
| `OvertimeTypeId` | `Int64?` | yes | [OvertimeTypes](OvertimeType.md) |  | The business key identifier of overtime type |
| `Factor` | `Decimal?` | yes |  |  | The factor of workshop schedule salary type |
| `RowIndex` | `Int32?` | yes |  |  | The row index of workshop schedule salary type |
| `SalaryTypes` | `SalaryTypes[]` | no | [SalaryTypes](SalaryType.md) | expandable, collection | List of salary type |

## Example

```json
{
  "Id": 0,
  "WorkshopScheduleSalaryTypeRowId": 0,
  "OvertimeTypeId": null,
  "Factor": null,
  "RowIndex": null,
  "SalaryTypes": null
}
```
