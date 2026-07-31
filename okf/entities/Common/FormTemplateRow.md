---
type: API Entity
title: FormTemplateRows
description: Represents a form template row.
resource: https://api.monitor.se/api/Monitor.API.Common.FormTemplateRow.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.FormTemplateRow.html
  title: Monitor API — FormTemplateRow
module: Common
api_class: FormTemplateRow
doc_name: FormTemplateRows
endpoint: GET /api/v1/Common/FormTemplateRows
guid: 98FDCACE-1DA2-42A0-9D9F-85733BFD0B61
introduced_in: '22.5'
property_count: 21
references_out:
- /entities/Common/Comment.md
- /entities/Common/FormTemplateSelectionRow.md
- /entities/Common/Unit.md
- /entities/Inventory/Part.md
---

# FormTemplateRows

Represents a form template row.

- **Module:** [Common](/modules/Common.md)
- **API class:** `FormTemplateRow`
- **Endpoint:** `GET /api/v1/Common/FormTemplateRows`
- **GUID:** `98FDCACE-1DA2-42A0-9D9F-85733BFD0B61`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `Code` | `String` | no |  | max length 12 | The human readable identifier of the form template row. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the form template row. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the form template row's comment. |
| `Description` | `String` | no |  |  | The translated description of the form template row. |
| `FormTemplateSelectionRowId` | `Int64` | no | [FormTemplateSelectionRows](/entities/Common/FormTemplateSelectionRow.md) |  | The business key identifier of the form template selection row that the form template row relates to. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the form template row. |
| `Checkbox` | `Boolean` | no |  |  | The boolean value of the form template row. |
| `DateTimeValue` | `DateTimeOffset?` | yes |  |  | The timestamp of the form template row. |
| `Number` | `Decimal?` | yes |  |  | The numeric value of the form template row. |
| `TextValue` | `String` | no |  | max length 80 | The text value of the form template row. |
| `Type` | `Int32` | no |  | enum | The type of the value stored in the form template row. |
| `LowerBoundary` | `Decimal?` | yes |  |  | The minimum setpoint value of the form template row. |
| `UpperBoundary` | `Decimal?` | yes |  |  | The maximum setpoint value of the form template row. |
| `MinValue` | `Decimal?` | yes |  |  | The minimum tolerance value of the form template row. |
| `MaxValue` | `Decimal?` | yes |  |  | The maximum tolerance value of the form template row. |
| `Value` | `Decimal?` | yes |  |  | The setpoint value of the form template row. |
| `Mandatory` | `Boolean` | no |  |  | Indicates if the value of the form template row needs to be reported. |
| `PrintOut` | `Boolean` | no |  |  | Indicates if the form template row's properties should be printed on the document. |
| `MasterToolId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the tool that the form template row relates to. |
| `UnitId` | `Int64?` | yes | [Units](/entities/Common/Unit.md) |  | The business key identifier of the unit of the form template row's value. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Decimal` | 0 |
| `Text` | 1 |
| `CheckBox` | 2 |
| `Date` | 3 |


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Comment": null,
  "CommentId": null,
  "Description": null,
  "FormTemplateSelectionRowId": 0,
  "RowIndex": null,
  "Checkbox": false,
  "DateTimeValue": null,
  "Number": null,
  "TextValue": null,
  "Type": 0,
  "LowerBoundary": null,
  "UpperBoundary": null,
  "MinValue": null,
  "MaxValue": null,
  "Value": null,
  "Mandatory": false,
  "PrintOut": false,
  "MasterToolId": null,
  "UnitId": null
}
```
