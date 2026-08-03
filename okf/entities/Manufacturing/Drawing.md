---
type: API Entity
title: Drawings
description: Represents a drawing.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.Drawing.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.Drawing.html
  title: Monitor API — Drawing
module: Manufacturing
api_class: Drawing
doc_name: Drawings
endpoint: GET /api/v1/Manufacturing/Drawings
guid: F3EFB1BB-3877-4E34-8148-424F23779AAE
permission: Show part
introduced_in: '2.18'
property_count: 5
references_out:
- /entities/Inventory/Part.md
- /entities/Manufacturing/DrawingRevision.md
referenced_by:
- /entities/Inventory/Part.md
- /entities/Manufacturing/DrawingRevision.md
---

# Drawings

Represents a drawing.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `Drawing`
- **Endpoint:** `GET /api/v1/Manufacturing/Drawings`
- **Required permission:** Show part
- **GUID:** `F3EFB1BB-3877-4E34-8148-424F23779AAE`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the drawing. |
| `DrawingNumber` | `String` | no |  | unique (per per Part), max length 80 | The human readable number of the drawing. |
| `PartId` | `Int64` | no | [Parts](../Inventory/Part.md) |  | The business key identifier of the part that the drawing belongs to. |
| `Revisions` | `DrawingRevisions[]` | no | [DrawingRevisions](DrawingRevision.md) | expandable, collection | A collection of revisions that belong the the drawing. |
| `ActiveDrawingRevisionId` | `Int64?` | yes | [DrawingRevisions](DrawingRevision.md) | since 23.2 | The business key identifier of the active drawing revision. |

## Referenced by

**Inventory**

- [Parts](../Inventory/Part.md) — `Drawings` (expand)

**Manufacturing**

- [DrawingRevisions](DrawingRevision.md) — `ParentId` (FK)


## Example

```json
{
  "Id": 0,
  "DrawingNumber": null,
  "PartId": 0,
  "Revisions": null,
  "ActiveDrawingRevisionId": null
}
```
