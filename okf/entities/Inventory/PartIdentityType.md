---
type: API Entity
title: PartIdentityTypes
description: Represents a part identity type.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartIdentityType.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartIdentityType.html
  title: Monitor API — PartIdentityType
module: Inventory
api_class: PartIdentityType
doc_name: PartIdentityTypes
endpoint: GET /api/v1/Inventory/PartIdentityTypes
guid: 19a0fb4f-e580-41ab-b1a3-5b661020e5ea
permission: Show basic data for part
introduced_in: '2.47'
property_count: 5
referenced_by:
- /entities/Inventory/PartOtherIdentity.md
---

# PartIdentityTypes

Represents a part identity type.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PartIdentityType`
- **Endpoint:** `GET /api/v1/Inventory/PartIdentityTypes`
- **Required permission:** Show basic data for part
- **GUID:** `19a0fb4f-e580-41ab-b1a3-5b661020e5ea`
- **Introduced in:** 2.47

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part identity type. |
| `Code` | `String` | no |  | unique, max length 10 | The human readable identifier of the part identity type. |
| `Description` | `String` | no |  |  | The translated description of the part identity type. |
| `IsActive` | `Boolean` | no |  |  | Specifies whether or not the part identity type is active. |
| `Type` | `Int32?` | yes |  | enum | The type of code that the part identity type defines. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `GTIN8` | 1 |
| `GTIN12` | 2 |
| `GTIN13` | 3 |
| `GTIN14` | 4 |
| `SGTIN` | 5 |


## Referenced by

**Inventory**

- [PartOtherIdentities](PartOtherIdentity.md) — `TypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "IsActive": false,
  "Type": null
}
```
