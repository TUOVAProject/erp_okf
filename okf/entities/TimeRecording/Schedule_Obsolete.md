---
type: API Entity
title: Shedules
description: Represents a schedule used for time recording.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.Schedule_Obsolete.html
tags:
- TimeRecording
- queryable
status: deprecated
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.Schedule_Obsolete.html
  title: Monitor API — Schedule_Obsolete
module: TimeRecording
api_class: Schedule_Obsolete
doc_name: Shedules
endpoint: GET /api/v1/TimeRecording/Shedules
guid: 7A50172F-FE1F-40F7-9BDA-6C8566C34991
permission: Show basic data for attendance
introduced_in: '2.26'
property_count: 3
---

# Shedules

Represents a schedule used for time recording.

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `Schedule_Obsolete`
- **Endpoint:** `GET /api/v1/TimeRecording/Shedules`
- **Required permission:** Show basic data for attendance
- **GUID:** `7A50172F-FE1F-40F7-9BDA-6C8566C34991`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the shedule. |
| `Code` | `String` | no |  |  | The human readable identifier of the shedule. |
| `Description` | `String` | no |  |  | The translated description of the shedule. |

## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null
}
```
