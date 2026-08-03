---
type: API Entity
title: PartImages
description: Represents a part image.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartImage.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartImage.html
  title: Monitor API — PartImage
module: Inventory
api_class: PartImage
doc_name: PartImages
endpoint: GET /api/v1/Inventory/PartImages
guid: AB504CDD-AA53-4D03-99BD-601D76D331EC
permission: Show part
introduced_in: '25.7'
property_count: 5
references_out:
- /entities/Common/BlobData.md
- /entities/Inventory/Part.md
---

# PartImages

Represents a part image.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PartImage`
- **Endpoint:** `GET /api/v1/Inventory/PartImages`
- **Required permission:** Show part
- **GUID:** `AB504CDD-AA53-4D03-99BD-601D76D331EC`
- **Introduced in:** 25.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part image. |
| `PartId` | `Int64` | no | [Parts](Part.md) |  | The business key identifier of the part that the image belongs to. |
| `PhotoThumbnailId` | `Int64` | no | [BlobData](../Common/BlobData.md) |  | The business key identifier of entity downscaled thumbnail blob data. |
| `PhotoThumbnail` | `BlobData` | no | [BlobData](../Common/BlobData.md) | expandable | The entity thumbnail blob data |
| `ExternalVisible` | `Boolean` | no |  |  | Whether the part image should be shown externally. |

## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "PhotoThumbnailId": 0,
  "PhotoThumbnail": null,
  "ExternalVisible": false
}
```
