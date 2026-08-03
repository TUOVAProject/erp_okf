---
type: API Entity
title: PersonWorkCenters
description: Represents a table that determines which work centers (and thereby which
  report numbers) the person should be allowed to select among in the priority plan
  and when starting work via report numbers.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.PersonWorkCenter.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.PersonWorkCenter.html
  title: Monitor API — PersonWorkCenter
module: TimeRecording
api_class: PersonWorkCenter
doc_name: PersonWorkCenters
endpoint: GET /api/v1/TimeRecording/PersonWorkCenters
guid: 5B48A4ED-603E-453E-AA54-74E9E590A245
permission: Show person
introduced_in: '24.3'
property_count: 7
references_out:
- /entities/Common/Person.md
- /entities/Manufacturing/WorkCenter.md
referenced_by:
- /entities/Common/Person.md
- /entities/Manufacturing/WorkCenter.md
---

# PersonWorkCenters

Represents a table that determines which work centers (and thereby which report numbers) the person should be allowed to select among in the priority plan and when starting work via report numbers.

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `PersonWorkCenter`
- **Endpoint:** `GET /api/v1/TimeRecording/PersonWorkCenters`
- **Required permission:** Show person
- **GUID:** `5B48A4ED-603E-453E-AA54-74E9E590A245`
- **Introduced in:** 24.3

## Notes

- Used in WorkCenters and Persons

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the person work center. |
| `WorkCenterId` | `Int64` | no | [WorkCenters](../Manufacturing/WorkCenter.md) |  | The business key identifier of the work center that is linked to the person. |
| `PersonId` | `Int64` | no | [Persons](../Common/Person.md) |  | The business key identifier of the employee that is linked to the work center. |
| `Availability` | `Decimal?` | yes |  |  | Availability in percent |
| `IsCapacityWorkCenter` | `Boolean` | no |  |  | Determines if the Work Center has the employee linked as capacity. |
| `IsDefault` | `Boolean` | no |  |  | Determines if the work center should be selected by default when starting direct work. |
| `ShowOnPriorityPlan` | `Boolean` | no |  |  | Determine if the work center should be available to select in the work center field in order for priority plan to be shown in the recording terminal during start of direct work. |

## Referenced by

**Common**

- [Persons](../Common/Person.md) — `AvailableWorkCenters` (expand)

**Manufacturing**

- [WorkCenters](../Manufacturing/WorkCenter.md) — `Employees` (expand)


## Example

```json
{
  "Id": 0,
  "WorkCenterId": 0,
  "PersonId": 0,
  "Availability": null,
  "IsCapacityWorkCenter": false,
  "IsDefault": false,
  "ShowOnPriorityPlan": false
}
```
