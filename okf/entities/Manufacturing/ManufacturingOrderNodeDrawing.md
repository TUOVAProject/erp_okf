---
type: API Entity
title: ManufacturingOrderNodeDrawings
description: Represents a drawing for manufacturing order node.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderNodeDrawing.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderNodeDrawing.html
  title: Monitor API — ManufacturingOrderNodeDrawing
module: Manufacturing
api_class: ManufacturingOrderNodeDrawing
doc_name: ManufacturingOrderNodeDrawings
endpoint: GET /api/v1/Manufacturing/ManufacturingOrderNodeDrawings
guid: 96073CDC-9160-4379-A30E-E3FBBE29A152
permission: Show manufacturing orders
introduced_in: '24.2'
property_count: 5
references_out:
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Manufacturing/ManufacturingOrderNodeDrawingRevision.md
referenced_by:
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Manufacturing/ManufacturingOrderNodeDrawingRevision.md
---

# ManufacturingOrderNodeDrawings

Represents a drawing for manufacturing order node.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `ManufacturingOrderNodeDrawing`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderNodeDrawings`
- **Required permission:** Show manufacturing orders
- **GUID:** `96073CDC-9160-4379-A30E-E3FBBE29A152`
- **Introduced in:** 24.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the drawing. |
| `DrawingNumber` | `String` | no |  |  | The human readable number of the drawing. |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](ManufacturingOrderNode.md) |  | The business key identifier of the manufacturing order node that the drawing belongs to. |
| `Revisions` | `ManufacturingOrderNodeDrawingRevisions[]` | no | [ManufacturingOrderNodeDrawingRevisions](ManufacturingOrderNodeDrawingRevision.md) | expandable, collection | A collection of revisions that belong the the drawing. |
| `ActiveDrawingRevisionId` | `Int64?` | yes | [ManufacturingOrderNodeDrawingRevisions](ManufacturingOrderNodeDrawingRevision.md) |  | The business key identifier of the active drawing revision. |

## Referenced by

**Manufacturing**

- [ManufacturingOrderNodeDrawingRevisions](ManufacturingOrderNodeDrawingRevision.md) — `ParentId` (FK)
- [ManufacturingOrderNodes](ManufacturingOrderNode.md) — `Drawings` (expand)


## Example

```json
{
  "Id": 0,
  "DrawingNumber": null,
  "ManufacturingOrderNodeId": 0,
  "Revisions": null,
  "ActiveDrawingRevisionId": null
}
```
