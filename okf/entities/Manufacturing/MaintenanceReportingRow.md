---
type: API Entity
title: MaintenanceReportingRows
description: Represents a maintenance reporting row.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.MaintenanceReportingRow.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.MaintenanceReportingRow.html
  title: Monitor API — MaintenanceReportingRow
module: Manufacturing
api_class: MaintenanceReportingRow
doc_name: MaintenanceReportingRows
endpoint: GET /api/v1/Manufacturing/MaintenanceReportingRows
guid: 12415FBC-16A6-411C-B1BF-C11F152A8271
permission: Show maintenance plan
introduced_in: '25.7'
property_count: 21
references_out:
- /entities/Common/Comment.md
- /entities/Common/Unit.md
- /entities/Inventory/Part.md
- /entities/Inventory/ProductRecord.md
- /entities/Manufacturing/MaintenanceReportingSelectionRow.md
referenced_by:
- /entities/Manufacturing/MaintenanceReportingSelectionRow.md
---

# MaintenanceReportingRows

Represents a maintenance reporting row.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `MaintenanceReportingRow`
- **Endpoint:** `GET /api/v1/Manufacturing/MaintenanceReportingRows`
- **Required permission:** Show maintenance plan
- **GUID:** `12415FBC-16A6-411C-B1BF-C11F152A8271`
- **Introduced in:** 25.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `Code` | `String` | no |  | max length 12 | The human readable identifier of the maintenance reporting row. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the maintenance reporting row. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the maintenance reporting row's comment. |
| `Instruction` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The instruction of the maintenance reporting row. |
| `InstructionId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the maintenance reporting row's instruction. |
| `Description` | `String` | no |  |  | The translated description of the maintenance reporting row. |
| `MaintenanceReportingSelectionRowId` | `Int64` | no | [MaintenanceReportingSelectionRows](/entities/Manufacturing/MaintenanceReportingSelectionRow.md) |  | The business key identifier of the maintenance reporting selection row that the maintenance reporting row relates to. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the maintenance reporting row. |
| `Checkbox` | `Boolean` | no |  |  | The boolean value of the maintenance reporting row. |
| `DateTimeValue` | `DateTimeOffset?` | yes |  |  | The timestamp of the maintenance reporting row. |
| `Number` | `Decimal?` | yes |  |  | The numeric value of the maintenance reporting row. |
| `TextValue` | `String` | no |  | max length 80 | The text value of the maintenance reporting row. |
| `Type` | `Int32` | no |  | enum | The type of the value stored in the maintenance reporting row. |
| `ReportingStatus` | `Int32?` | yes |  | enum | The status of the value stored in the maintenance reporting row. |
| `MinValue` | `Decimal?` | yes |  |  | The minimum tolerance value of the maintenance reporting row. |
| `MaxValue` | `Decimal?` | yes |  |  | The maximum tolerance value of the maintenance reporting row. |
| `Value` | `Decimal?` | yes |  |  | The setpoint value of the maintenance reporting row. |
| `MasterToolId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the tool that the maintenance reporting row relates to. |
| `MasterToolProductRecordId` | `Int64?` | yes | [ProductRecords](/entities/Inventory/ProductRecord.md) |  | The business key identifier of the tool's product record that the maintenance reporting row relates to. |
| `UnitId` | `Int64?` | yes | [Units](/entities/Common/Unit.md) |  | The business key identifier of the unit of the maintenance reporting row's value. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Decimal` | 0 |
| `Text` | 1 |
| `CheckBox` | 2 |
| `Date` | 3 |

### ReportingStatus

| Name | Value |
| --- | ---: |
| `Ok` | 0 |
| `NotOk` | 1 |
| `OkWithAction` | 2 |


## Referenced by

**Manufacturing**

- [MaintenanceReportingSelectionRows](/entities/Manufacturing/MaintenanceReportingSelectionRow.md) — `MaintenanceReportingRows` (expand)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Comment": null,
  "CommentId": null,
  "Instruction": null,
  "InstructionId": null,
  "Description": null,
  "MaintenanceReportingSelectionRowId": 0,
  "RowIndex": null,
  "Checkbox": false,
  "DateTimeValue": null,
  "Number": null,
  "TextValue": null,
  "Type": 0,
  "ReportingStatus": null,
  "MinValue": null,
  "MaxValue": null,
  "Value": null,
  "MasterToolId": null,
  "MasterToolProductRecordId": null,
  "UnitId": null
}
```
