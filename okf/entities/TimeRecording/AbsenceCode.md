---
type: API Entity
title: AbsenceCodes
description: Represents an absence code. Used in time recording to represent a period
  of absence.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AbsenceCode.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AbsenceCode.html
  title: Monitor API — AbsenceCode
module: TimeRecording
api_class: AbsenceCode
doc_name: AbsenceCodes
endpoint: GET /api/v1/TimeRecording/AbsenceCodes
guid: DB81909B-E7DC-4D55-A061-A0BB67C6606A
permission: Show basic data for attendance
introduced_in: '2.26'
property_count: 3
referenced_by:
- /entities/TimeRecording/AttendanceGroupSettings.md
- /entities/TimeRecording/AttendanceInterval.md
---

# AbsenceCodes

Represents an absence code. Used in time recording to represent a period of absence.

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `AbsenceCode`
- **Endpoint:** `GET /api/v1/TimeRecording/AbsenceCodes`
- **Required permission:** Show basic data for attendance
- **GUID:** `DB81909B-E7DC-4D55-A061-A0BB67C6606A`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the absence code. |
| `Code` | `String` | no |  |  | The human readable identifier of the absence code. |
| `Description` | `String` | no |  |  | The translated description of the absence code. |

## Referenced by

**TimeRecording**

- [AttendanceGroupSettings](AttendanceGroupSettings.md) — `UnavailableAbsenceCodes` (expand)
- [AttendanceIntervals](AttendanceInterval.md) — `AbsenceCodeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null
}
```
