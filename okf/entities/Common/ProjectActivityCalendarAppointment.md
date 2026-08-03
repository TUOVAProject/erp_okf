---
type: API Entity
title: ProjectActivityCalendarAppointments
description: Represents a Project Activity Calendar Appointment.
resource: https://api.monitor.se/api/Monitor.API.Common.ProjectActivityCalendarAppointment.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ProjectActivityCalendarAppointment.html
  title: Monitor API — ProjectActivityCalendarAppointment
module: Common
api_class: ProjectActivityCalendarAppointment
doc_name: ProjectActivityCalendarAppointments
endpoint: GET /api/v1/Common/ProjectActivityCalendarAppointments
guid: 4f779e41-3d84-4a36-adb3-b0c86655a20d
permission: Show projects
introduced_in: '25.6'
property_count: 4
references_out:
- /entities/Common/Person.md
- /entities/Common/ProjectActivity.md
---

# ProjectActivityCalendarAppointments

Represents a Project Activity Calendar Appointment.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ProjectActivityCalendarAppointment`
- **Endpoint:** `GET /api/v1/Common/ProjectActivityCalendarAppointments`
- **Required permission:** Show projects
- **GUID:** `4f779e41-3d84-4a36-adb3-b0c86655a20d`
- **Introduced in:** 25.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project appointment. |
| `ProjectActivityId` | `Int64?` | yes | [ProjectActivities](ProjectActivity.md) |  | The business key identifier of the project activity. |
| `SenderPersonId` | `Int64?` | yes | [Persons](Person.md) |  | The business key identifier of the sender person. |
| `CalendarAppointmentId` | `String` | no |  | max length 256 | The unique identifier of the appointment created in the user's calendar program. |

## Example

```json
{
  "Id": 0,
  "ProjectActivityId": null,
  "SenderPersonId": null,
  "CalendarAppointmentId": null
}
```
