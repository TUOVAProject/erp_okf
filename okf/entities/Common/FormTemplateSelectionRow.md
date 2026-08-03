---
type: API Entity
title: FormTemplateSelectionRows
description: Represents a form template selection row.
resource: https://api.monitor.se/api/Monitor.API.Common.FormTemplateSelectionRow.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.FormTemplateSelectionRow.html
  title: Monitor API — FormTemplateSelectionRow
module: Common
api_class: FormTemplateSelectionRow
doc_name: FormTemplateSelectionRows
endpoint: GET /api/v1/Common/FormTemplateSelectionRows
guid: 3D2F2645-DDD2-4947-B5BE-741B951011BA
introduced_in: '22.5'
property_count: 7
references_out:
- /entities/Common/Comment.md
- /entities/Common/FormTemplate.md
referenced_by:
- /entities/Common/FormTemplateRow.md
---

# FormTemplateSelectionRows

Represents a form template selection row.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `FormTemplateSelectionRow`
- **Endpoint:** `GET /api/v1/Common/FormTemplateSelectionRows`
- **GUID:** `3D2F2645-DDD2-4947-B5BE-741B951011BA`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `Code` | `String` | no |  | unique, max length 12 | The human readable identifier of the form template selection row. |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The comment of the form template selection row. |
| `CommentId` | `Int64?` | yes | [Comments](Comment.md) |  | The business key identifier of the form template selection row's comment. |
| `Description` | `String` | no |  |  | The translated description of the form template selection row. |
| `FormTemplateId` | `Int64` | no | [FormTemplates](FormTemplate.md) |  | The business key identifier of the form template that the form template selection row relates to. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the form template selection row. |

## Referenced by

**Common**

- [FormTemplateRows](FormTemplateRow.md) — `FormTemplateSelectionRowId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Comment": null,
  "CommentId": null,
  "Description": null,
  "FormTemplateId": 0,
  "RowIndex": null
}
```
