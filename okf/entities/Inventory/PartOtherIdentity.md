---
type: API Entity
title: PartOtherIdentities
description: Represents an alternate identity for a part.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartOtherIdentity.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartOtherIdentity.html
  title: Monitor API — PartOtherIdentity
module: Inventory
api_class: PartOtherIdentity
doc_name: PartOtherIdentities
endpoint: GET /api/v1/Inventory/PartOtherIdentities
guid: 1445e739-4b85-42d9-86f7-4ffab92422d3
permission: Show part
introduced_in: '2.47'
property_count: 5
references_out:
- /entities/Inventory/Part.md
- /entities/Inventory/PartIdentityType.md
referenced_by:
- /entities/Inventory/Part.md
---

# PartOtherIdentities

Represents an alternate identity for a part.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `PartOtherIdentity`
- **Endpoint:** `GET /api/v1/Inventory/PartOtherIdentities`
- **Required permission:** Show part
- **GUID:** `1445e739-4b85-42d9-86f7-4ffab92422d3`
- **Introduced in:** 2.47

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the alternate identity. |
| `TypeId` | `Int64` | no | [PartIdentityTypes](/entities/Inventory/PartIdentityType.md) |  | The business key identifier of the identity type of the alternate identity. |
| `Value` | `String` | no |  |  | The value of the alternate identity. |
| `IsActive` | `Boolean` | no |  |  | Whether or not the alternate identity is active. |
| `PartId` | `Int64` | no | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the part that the alternate identity belongs to. |

## Referenced by

**Inventory**

- [Parts](/entities/Inventory/Part.md) — `OtherIdentities` (expand)


## Example

```json
{
  "Id": 0,
  "TypeId": 0,
  "Value": null,
  "IsActive": false,
  "PartId": 0
}
```
