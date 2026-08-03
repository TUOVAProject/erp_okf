---
type: API Entity
title: BlobData
description: A container for blob data.
resource: https://api.monitor.se/api/Monitor.API.Common.BlobData.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.BlobData.html
  title: Monitor API — BlobData
module: Common
api_class: BlobData
doc_name: BlobData
endpoint: GET /api/v1/Common/BlobData
guid: 0A07B09A-03F9-4AC2-908A-523A4BE9C770
introduced_in: '22.5'
property_count: 4
referenced_by:
- /entities/Common/Company.md
- /entities/Common/Person.md
- /entities/Inventory/PartImage.md
- /entities/Purchase/EimDocument.md
---

# BlobData

A container for blob data.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `BlobData`
- **Endpoint:** `GET /api/v1/Common/BlobData`
- **GUID:** `0A07B09A-03F9-4AC2-908A-523A4BE9C770`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the blob data. |
| `MediaType` | `Int32` | no |  | enum | The media type of the blob data. |
| `MediaSubType` | `String` | no |  | max length 32 | The media subtype of the blob data. |
| `Value` | `String` | no |  |  | The value of the blob data, represented as a Base64 string. |

## Enumerations

### MediaType

| Name | Value |
| --- | ---: |
| `Text` | 0 |
| `Image` | 1 |
| `Audio` | 2 |
| `Video` | 3 |
| `Application` | 4 |
| `Multipart` | 5 |
| `Message` | 6 |


## Referenced by

**Common**

- [Companies](Company.md) — `Image` (expand)
- [Persons](Person.md) — `Signature` (expand)

**Inventory**

- [PartImages](../Inventory/PartImage.md) — `PhotoThumbnail` (expand)
- [PartImages](../Inventory/PartImage.md) — `PhotoThumbnailId` (FK)

**Purchase**

- [EimDocuments](../Purchase/EimDocument.md) — `BlobDataId` (FK)


## Example

```json
{
  "Id": 0,
  "MediaType": 0,
  "MediaSubType": null,
  "Value": null
}
```
