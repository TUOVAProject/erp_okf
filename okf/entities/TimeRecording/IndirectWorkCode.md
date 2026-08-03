---
type: API Entity
title: IndirectWorkCodes
description: Represents indirect work used for work recording.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.IndirectWorkCode.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.IndirectWorkCode.html
  title: Monitor API — IndirectWorkCode
module: TimeRecording
api_class: IndirectWorkCode
doc_name: IndirectWorkCodes
endpoint: GET /api/v1/TimeRecording/IndirectWorkCodes
guid: F8F01355-B2DB-44DC-9610-1B5578EF4263
permission: Show basic data for attendance
introduced_in: '2.26'
property_count: 7
references_out:
- /entities/Manufacturing/ManufacturingOrderOperation.md
referenced_by:
- /entities/TimeRecording/AttendanceGroupSettings.md
- /entities/TimeRecording/StandbyWork.md
- /entities/TimeRecording/WorkInterval.md
---

# IndirectWorkCodes

Represents indirect work used for work recording.

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `IndirectWorkCode`
- **Endpoint:** `GET /api/v1/TimeRecording/IndirectWorkCodes`
- **Required permission:** Show basic data for attendance
- **GUID:** `F8F01355-B2DB-44DC-9610-1B5578EF4263`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the indirect work. |
| `Code` | `String` | no |  |  | The human readable identifier of the indirect work. |
| `Description` | `String` | no |  |  | The translated description of the indirect work. |
| `CommentInputType` | `Int32` | no |  | enum | Describes if a comment may or must be supplied when recording. |
| `AffectsOrder` | `Int32` | no | [ManufacturingOrderOperations](../Manufacturing/ManufacturingOrderOperation.md) | enum | Describes how this indirect work is reported when linked to a ManufacturingOrderOperations in recording. |
| `ColorCode` | `Int32?` | yes |  |  | Color code encoded as an ARGB. |
| `Active` | `Boolean` | no |  | since 26.6 | Indicates whether the indirect work code is active and may be used to start new indirect work. |

## Enumerations

### CommentInputType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Optional` | 1 |
| `Mandatory` | 2 |

### AffectsOrder

| Name | Value |
| --- | ---: |
| `No` | 0 |
| `UnitTime` | 1 |
| `SetupTime` | 2 |


## Referenced by

**TimeRecording**

- [AttendanceGroupSettings](AttendanceGroupSettings.md) — `IndirectWorkCodeId` (FK)
- [StandbyWorks](StandbyWork.md) — `IndirectWorkCode` (expand)
- [StandbyWorks](StandbyWork.md) — `IndirectWorkCodeId` (FK)
- [WorkIntervals](WorkInterval.md) — `IndirectWorkCodeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "CommentInputType": 0,
  "AffectsOrder": 0,
  "ColorCode": null,
  "Active": false
}
```
