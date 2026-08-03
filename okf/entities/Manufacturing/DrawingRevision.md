---
type: API Entity
title: DrawingRevisions
description: Represents a drawing revision.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.DrawingRevision.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.DrawingRevision.html
  title: Monitor API — DrawingRevision
module: Manufacturing
api_class: DrawingRevision
doc_name: DrawingRevisions
endpoint: GET /api/v1/Manufacturing/DrawingRevisions
guid: 988D24AF-A5BC-4972-8015-3362A3E18355
permission: Show part
introduced_in: '2.18'
property_count: 5
references_out:
- /entities/Common/Comment.md
- /entities/Manufacturing/Drawing.md
referenced_by:
- /entities/Manufacturing/Drawing.md
---

# DrawingRevisions

Represents a drawing revision.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `DrawingRevision`
- **Endpoint:** `GET /api/v1/Manufacturing/DrawingRevisions`
- **Required permission:** Show part
- **GUID:** `988D24AF-A5BC-4972-8015-3362A3E18355`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the revision. |
| `Number` | `String` | no |  | unique (per per Drawing), max length 25 | The human readable number of the revision. |
| `ParentId` | `Int64?` | yes | [Drawings](Drawing.md) |  | The business key identifier of the drawing that the revision belongs to. |
| `RevisionCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the revision comment. |
| `RevisionComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The revision comment. |

## Referenced by

**Manufacturing**

- [Drawings](Drawing.md) — `ActiveDrawingRevisionId` (FK)
- [Drawings](Drawing.md) — `Revisions` (expand)


## Example

```json
{
  "Id": 0,
  "Number": null,
  "ParentId": null,
  "RevisionCommentId": null,
  "RevisionComment": null
}
```
