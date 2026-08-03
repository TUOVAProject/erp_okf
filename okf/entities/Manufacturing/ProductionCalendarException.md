---
type: API Entity
title: ProductionCalendarExceptions
description: Represents a table that contains exceptions from the production calendar.
  Only used when using daily planning.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ProductionCalendarException.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ProductionCalendarException.html
  title: Monitor API — ProductionCalendarException
module: Manufacturing
api_class: ProductionCalendarException
doc_name: ProductionCalendarExceptions
endpoint: GET /api/v1/Manufacturing/ProductionCalendarExceptions
guid: 32843774-0FF8-4A8C-9E06-62FE088E4593
permission: Show work center
introduced_in: '24.3'
property_count: 6
references_out:
- /entities/Manufacturing/WorkCenter.md
- /entities/TimeRecording/Schedule.md
referenced_by:
- /entities/Manufacturing/WorkCenter.md
---

# ProductionCalendarExceptions

Represents a table that contains exceptions from the production calendar. Only used when using daily planning.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `ProductionCalendarException`
- **Endpoint:** `GET /api/v1/Manufacturing/ProductionCalendarExceptions`
- **Required permission:** Show work center
- **GUID:** `32843774-0FF8-4A8C-9E06-62FE088E4593`
- **Introduced in:** 24.3

## Notes

- Used in WorkCenters />

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the production calendar exception. |
| `WorkCenterId` | `Int64` | no | [WorkCenters](WorkCenter.md) |  | The business key identifier of the work center that is linked to the production calendar exception. |
| `NumberOfPlanningUnits` | `Decimal?` | yes |  |  | Number of persons or number of machines depending on the work center type. |
| `ExceptionDate` | `DateTime` | no |  |  | Day of the production calendar exception. |
| `BasicTime` | `TimeSpan?` | yes |  |  | Basic time used on this production calendar exception date. |
| `ScheduleId` | `Int64?` | yes | [Schedules](../TimeRecording/Schedule.md) |  | The business key identifier of the schedule used on this production calendar exception date. |

## Referenced by

**Manufacturing**

- [WorkCenters](WorkCenter.md) — `ProductionCalendarExceptions` (expand)


## Example

```json
{
  "Id": 0,
  "WorkCenterId": 0,
  "NumberOfPlanningUnits": null,
  "ExceptionDate": "0001-01-01T00:00:00",
  "BasicTime": null,
  "ScheduleId": null
}
```
