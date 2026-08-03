---
type: API Entity
title: HyperLinks
description: Represents a part hyperlink.
resource: https://api.monitor.se/api/Monitor.API.Inventory.HyperLink.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.HyperLink.html
  title: Monitor API — HyperLink
module: Inventory
api_class: HyperLink
doc_name: HyperLinks
endpoint: GET /api/v1/Inventory/HyperLinks
guid: A5CE7740-7BFC-4E08-8351-B994B6927D5D
permission: Show part
introduced_in: '2.55'
property_count: 4
references_out:
- /entities/Inventory/Part.md
referenced_by:
- /entities/Inventory/Part.md
---

# HyperLinks

Represents a part hyperlink.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `HyperLink`
- **Endpoint:** `GET /api/v1/Inventory/HyperLinks`
- **Required permission:** Show part
- **GUID:** `A5CE7740-7BFC-4E08-8351-B994B6927D5D`
- **Introduced in:** 2.55

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the hyperlink. |
| `PartId` | `Int64` | no | [Parts](Part.md) |  | The business key identifier of the part that the hyperlink belongs to. |
| `Link` | `String` | no |  |  | The link (url) of the hyperlink. |
| `Description` | `String` | no |  |  | The description of the hyperlink. |

## Referenced by

**Inventory**

- [Parts](Part.md) — `HyperLinks` (expand)


## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "Link": null,
  "Description": null
}
```
