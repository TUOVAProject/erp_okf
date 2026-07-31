---
type: API Entity
title: MaterialRows
description: Represents a material row.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.MaterialRow.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.MaterialRow.html
  title: Monitor API — MaterialRow
module: Manufacturing
api_class: MaterialRow
doc_name: MaterialRows
endpoint: GET /api/v1/Manufacturing/MaterialRows
guid: CC45DF31-2B90-4498-9171-0975416947D3
permission: Show part
introduced_in: '2.18'
property_count: 16
references_out:
- /entities/Common/Comment.md
- /entities/Manufacturing/ReferenceNumber.md
referenced_by:
- /entities/Manufacturing/Preparation.md
- /entities/Manufacturing/ReferenceNumber.md
---

# MaterialRows

Represents a material row.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `MaterialRow`
- **Endpoint:** `GET /api/v1/Manufacturing/MaterialRows`
- **Required permission:** Show part
- **GUID:** `CC45DF31-2B90-4498-9171-0975416947D3`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the material row. |
| `PartId` | `Int64` | no |  |  | The business key identifier of material row part. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the material row's comment. References Comments /// |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the material row. |
| `Position` | `String` | no |  | max length 10 | The position of the material row. |
| `ToOperation` | `Int32` | no |  |  | The number of the operation row that the material row belongs to. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the material row. |
| `SetupQuantity` | `Decimal` | no |  |  | The setup quantity of the material row. |
| `ExtraPercent` | `Decimal` | no |  |  | The extra percent of the material row. |
| `IsForCalculationOnly` | `Boolean` | no |  |  | Specifies if the material row is only used for calculation. |
| `MainPartId` | `Int64` | no |  |  | The business key identifier of the part that the material row belongs to. |
| `RowIndex` | `Int32` | no |  |  | The row index of the material row. |
| `PreparationTermType` | `Int32?` | yes |  | since 24.4 | PreparationTermType of the Material Row. |
| `PreparationTermFromValue` | `String` | no |  | since 24.4 | PreparationTermFromValue of the Material Row. |
| `PreparationTermToValue` | `String` | no |  | since 24.4 | PreparationTermToValue of the Material Row. |
| `ReferenceNumbers` | `MaterialRowReferenceNumbers[]` | no | [MaterialRowReferenceNumbers](/entities/Manufacturing/ReferenceNumber.md) | expandable, collection, since 26.6 | The reference numbers configured for this material row. |

## Referenced by

**Manufacturing**

- [MaterialRowReferenceNumbers](/entities/Manufacturing/ReferenceNumber.md) — `MaterialRowId` (FK)
- [Preparations](/entities/Manufacturing/Preparation.md) — `Materials` (expand)


## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "CommentId": null,
  "Comment": null,
  "Position": null,
  "ToOperation": 0,
  "Quantity": 0.0,
  "SetupQuantity": 0.0,
  "ExtraPercent": 0.0,
  "IsForCalculationOnly": false,
  "MainPartId": 0,
  "RowIndex": 0,
  "PreparationTermType": null,
  "PreparationTermFromValue": null,
  "PreparationTermToValue": null,
  "ReferenceNumbers": null
}
```
