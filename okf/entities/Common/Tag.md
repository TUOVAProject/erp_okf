---
type: API Entity
title: Tags
description: Represents a tag.
resource: https://api.monitor.se/api/Monitor.API.Common.Tag.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Tag.html
  title: Monitor API — Tag
module: Common
api_class: Tag
doc_name: Tags
endpoint: GET /api/v1/Common/Tags
guid: 3DC6747F-6E38-47AC-8FDD-5B0CFE753285
permission: Show part
introduced_in: '22.5'
property_count: 4
---

# Tags

Represents a tag.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `Tag`
- **Endpoint:** `GET /api/v1/Common/Tags`
- **Required permission:** Show part
- **GUID:** `3DC6747F-6E38-47AC-8FDD-5B0CFE753285`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the tag. |
| `OwnerTypeId` | `Guid` | no |  |  | The GUID identifier for the type of entity that owns the tag. |
| `OwnerId` | `Int64` | no |  |  | The business key identifier for the owner of the tag. |
| `Name` | `String` | no |  | max length 50 | The name of the tag. |

## Example

```json
{
  "Id": 0,
  "OwnerTypeId": "00000000-0000-0000-0000-000000000000",
  "OwnerId": 0,
  "Name": null
}
```
