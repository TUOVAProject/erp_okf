---
type: API Entity
title: TimeBanks
description: Represents a time bank.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.TimeBank.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.TimeBank.html
  title: Monitor API — TimeBank
module: TimeRecording
api_class: TimeBank
doc_name: TimeBanks
endpoint: GET /api/v1/TimeRecording/TimeBanks
guid: 64733207-5A23-454C-8657-B2FF9DCFC991
permission: Show recording items
introduced_in: '2.26'
property_count: 3
referenced_by:
- /entities/TimeRecording/AdditionRecording.md
- /entities/TimeRecording/AttendanceAddition.md
- /entities/TimeRecording/AttendanceGroupSettings.md
- /entities/TimeRecording/PersonTimeBank.md
---

# TimeBanks

Represents a time bank.

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `TimeBank`
- **Endpoint:** `GET /api/v1/TimeRecording/TimeBanks`
- **Required permission:** Show recording items
- **GUID:** `64733207-5A23-454C-8657-B2FF9DCFC991`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the time bank. |
| `Code` | `String` | no |  |  | The human readable identifier of the time bank. |
| `Description` | `String` | no |  |  | The translated description of the time bank. |

## Referenced by

**TimeRecording**

- [AdditionRecordings](AdditionRecording.md) — `TimeBank` (expand)
- [AdditionRecordings](AdditionRecording.md) — `TimeBankId` (FK)
- [AttendanceAdditions](AttendanceAddition.md) — `TimeBank` (expand)
- [AttendanceAdditions](AttendanceAddition.md) — `TimeBankId` (FK)
- [AttendanceGroupSettings](AttendanceGroupSettings.md) — `RoundOffOvertimeTimebankId` (FK)
- [AttendanceGroupSettings](AttendanceGroupSettings.md) — `ShorterWorkingHoursTimeBankId` (FK)
- [PersonTimeBanks](PersonTimeBank.md) — `TimeBankId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null
}
```
