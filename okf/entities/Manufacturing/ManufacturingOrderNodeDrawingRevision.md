---
type: API Entity
title: ManufacturingOrderNodeDrawingRevisions
description: Represents a drawing revision for manufacturing order node.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderNodeDrawingRevision.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderNodeDrawingRevision.html
  title: Monitor API — ManufacturingOrderNodeDrawingRevision
module: Manufacturing
api_class: ManufacturingOrderNodeDrawingRevision
doc_name: ManufacturingOrderNodeDrawingRevisions
endpoint: GET /api/v1/Manufacturing/ManufacturingOrderNodeDrawingRevisions
guid: 50A5261B-B35A-4647-AA74-1DCFEC1A642E
permission: Show manufacturing orders
introduced_in: '24.2'
property_count: 5
references_out:
- /entities/Common/Comment.md
- /entities/Manufacturing/ManufacturingOrderNodeDrawing.md
referenced_by:
- /entities/Manufacturing/ManufacturingOrderNodeDrawing.md
---

# ManufacturingOrderNodeDrawingRevisions

Represents a drawing revision for manufacturing order node.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `ManufacturingOrderNodeDrawingRevision`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderNodeDrawingRevisions`
- **Required permission:** Show manufacturing orders
- **GUID:** `50A5261B-B35A-4647-AA74-1DCFEC1A642E`
- **Introduced in:** 24.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the revision. |
| `Number` | `String` | no |  | unique (per per Drawing), max length 25 | The human readable number of the revision. |
| `ParentId` | `Int64?` | yes | [ManufacturingOrderNodeDrawings](ManufacturingOrderNodeDrawing.md) |  | The business key identifier of the drawing that the revision belongs to. |
| `RevisionCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the revision comment. |
| `RevisionComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The revision comment. |

## Referenced by

**Manufacturing**

- [ManufacturingOrderNodeDrawings](ManufacturingOrderNodeDrawing.md) — `ActiveDrawingRevisionId` (FK)
- [ManufacturingOrderNodeDrawings](ManufacturingOrderNodeDrawing.md) — `Revisions` (expand)


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
