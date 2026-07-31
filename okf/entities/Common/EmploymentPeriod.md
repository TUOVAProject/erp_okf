---
type: API Entity
title: EmploymentPeriods
description: Represents the employment period of a personnel record.
resource: https://api.monitor.se/api/Monitor.API.Common.EmploymentPeriod.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.EmploymentPeriod.html
  title: Monitor API — EmploymentPeriod
module: Common
api_class: EmploymentPeriod
doc_name: EmploymentPeriods
endpoint: GET /api/v1/Common/EmploymentPeriods
guid: 1AB99122-6197-420D-9AFE-A9FA17FC3935
permission: Show person
introduced_in: '22.3'
property_count: 7
references_out:
- /entities/Common/Comment.md
- /entities/Common/Person.md
referenced_by:
- /entities/Common/Person.md
---

# EmploymentPeriods

Represents the employment period of a personnel record.

- **Module:** [Common](/modules/Common.md)
- **API class:** `EmploymentPeriod`
- **Endpoint:** `GET /api/v1/Common/EmploymentPeriods`
- **Required permission:** Show person
- **GUID:** `1AB99122-6197-420D-9AFE-A9FA17FC3935`
- **Introduced in:** 22.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the employment period. |
| `StartDate` | `DateTimeOffset` | no |  |  | The start date of the employment period. |
| `FinishDate` | `DateTimeOffset?` | yes |  |  | The finish date of the employment period. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the comment that belongs to the employment period. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment that belongs to the employment period. |
| `PersonId` | `Int64` | no | [Persons](/entities/Common/Person.md) |  | The business key identifier of the personnel record that the employment period belongs to. |
| `RowIndex` | `Int32` | no |  |  | The ordered row index of the employment period. |

## Referenced by

**Common**

- [Persons](/entities/Common/Person.md) — `EmploymentPeriods` (expand)


## Example

```json
{
  "Id": 0,
  "StartDate": "0001-01-01T00:00:00+00:00",
  "FinishDate": null,
  "CommentId": null,
  "Comment": null,
  "PersonId": 0,
  "RowIndex": 0
}
```
