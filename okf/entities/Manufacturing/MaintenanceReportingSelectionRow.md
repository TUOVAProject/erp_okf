---
type: API Entity
title: MaintenanceReportingSelectionRows
description: Represents a maintenance reporting selection row.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.MaintenanceReportingSelectionRow.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.MaintenanceReportingSelectionRow.html
  title: Monitor API — MaintenanceReportingSelectionRow
module: Manufacturing
api_class: MaintenanceReportingSelectionRow
doc_name: MaintenanceReportingSelectionRows
endpoint: GET /api/v1/Manufacturing/MaintenanceReportingSelectionRows
guid: 46A44B24-CB52-4C7C-9DB9-A0EAC86DEF0E
permission: Show maintenance plan
introduced_in: '25.7'
property_count: 8
references_out:
- /entities/Common/Comment.md
- /entities/Manufacturing/MaintenanceReporting.md
- /entities/Manufacturing/MaintenanceReportingRow.md
referenced_by:
- /entities/Manufacturing/MaintenanceReporting.md
- /entities/Manufacturing/MaintenanceReportingRow.md
---

# MaintenanceReportingSelectionRows

Represents a maintenance reporting selection row.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `MaintenanceReportingSelectionRow`
- **Endpoint:** `GET /api/v1/Manufacturing/MaintenanceReportingSelectionRows`
- **Required permission:** Show maintenance plan
- **GUID:** `46A44B24-CB52-4C7C-9DB9-A0EAC86DEF0E`
- **Introduced in:** 25.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `Code` | `String` | no |  | unique, max length 12 | The human readable identifier of the maintenance reporting selection row. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the maintenance reporting selection row. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the maintenance reporting selection row's comment. |
| `Description` | `String` | no |  |  | The translated description of the maintenance reporting selection row. |
| `MaintenanceReportingId` | `Int64` | no | [MaintenanceReportings](/entities/Manufacturing/MaintenanceReporting.md) |  | The business key identifier of the maintenance reporting that the maintenance reporting selection row relates to. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the maintenance reporting selection row. |
| `MaintenanceReportingRows` | `MaintenanceReportingRows[]` | no | [MaintenanceReportingRows](/entities/Manufacturing/MaintenanceReportingRow.md) | expandable, collection | The maintenance reporting rows. |

## Referenced by

**Manufacturing**

- [MaintenanceReportingRows](/entities/Manufacturing/MaintenanceReportingRow.md) — `MaintenanceReportingSelectionRowId` (FK)
- [MaintenanceReportings](/entities/Manufacturing/MaintenanceReporting.md) — `MaintenanceReportingSelectionRows` (expand)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Comment": null,
  "CommentId": null,
  "Description": null,
  "MaintenanceReportingId": 0,
  "RowIndex": null,
  "MaintenanceReportingRows": null
}
```
