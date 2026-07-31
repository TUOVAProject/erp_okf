---
type: API Entity
title: PlannedAbsences
description: Represents a planned absence.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.PlannedAbsence.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.PlannedAbsence.html
  title: Monitor API — PlannedAbsence
module: TimeRecording
api_class: PlannedAbsence
doc_name: PlannedAbsences
endpoint: GET /api/v1/TimeRecording/PlannedAbsences
guid: C065ACFA-57F8-4397-BFBB-F33E56B24750
permission: Show person
introduced_in: '2.47'
property_count: 10
referenced_by:
- /entities/Common/Person.md
---

# PlannedAbsences

Represents a planned absence.

- **Module:** [TimeRecording](/modules/TimeRecording.md)
- **API class:** `PlannedAbsence`
- **Endpoint:** `GET /api/v1/TimeRecording/PlannedAbsences`
- **Required permission:** Show person
- **GUID:** `C065ACFA-57F8-4397-BFBB-F33E56B24750`
- **Introduced in:** 2.47

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the planned absence. |
| `PersonId` | `Int64` | no |  |  | The business key identifier of the person. References(Person) |
| `AbsenceFrom` | `DateTimeOffset` | no |  |  | The start of the absence period. |
| `AbsenceTo` | `DateTimeOffset` | no |  |  | The end of the absence period. |
| `AbsenceCodeId` | `Int64` | no |  |  | The business key identifier of the absence code. References(AbsenceCode) |
| `PartOfDay` | `Boolean` | no |  |  | Specifies if the absence is part of a day. |
| `Approved` | `Boolean` | no |  | **deprecated since 24.7** | Specifies if the absence is approved. _(Use status instead. (Returns true if status is approved else returns false))_ |
| `Status` | `Int32` | no |  | enum, since 24.7 | Specifies the absence status. |
| `AbsenceDuration` | `TimeSpan` | no |  |  | The absence duration of the planned absence. |
| `AttendanceDuration` | `TimeSpan` | no |  |  | The attendance duration of the planned absence. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `AppliedFor` | 0 |
| `Approved` | 1 |
| `Denied` | 2 |


## Referenced by

**Common**

- [Persons](/entities/Common/Person.md) — `PlannedAbsences` (expand)


## Example

```json
{
  "Id": 0,
  "PersonId": 0,
  "AbsenceFrom": "0001-01-01T00:00:00+00:00",
  "AbsenceTo": "0001-01-01T00:00:00+00:00",
  "AbsenceCodeId": 0,
  "PartOfDay": false,
  "Approved": false,
  "Status": 0,
  "AbsenceDuration": "00:00:00",
  "AttendanceDuration": "00:00:00"
}
```
