---
type: API Entity
title: CaseManagementType
description: Represents a case management type.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementType.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementType.html
  title: Monitor API — CaseManagementType
module: Inventory
api_class: CaseManagementType
doc_name: CaseManagementType
endpoint: GET /api/v1/Inventory/CaseManagementType
guid: 26DBCE14-6D7D-40CF-8A1B-C6C907678BCB
permission: Show basic data for case
introduced_in: '2.22'
property_count: 8
referenced_by:
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CaseManagementTemplate.md
---

# CaseManagementType

Represents a case management type.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `CaseManagementType`
- **Endpoint:** `GET /api/v1/Inventory/CaseManagementType`
- **Required permission:** Show basic data for case
- **GUID:** `26DBCE14-6D7D-40CF-8A1B-C6C907678BCB`
- **Introduced in:** 2.22

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case management type. |
| `Description` | `String` | no |  |  | The description of the case management type. |
| `IsPreset` | `Boolean` | no |  |  | Specifies if the case management type is preset. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the case management type. |
| `Prefix` | `String` | no |  | max length 3 | The prefix of the case management type. |
| `Priority` | `Int32` | no |  |  | The priority of the case management type. |
| `Visible` | `Boolean` | no |  |  | Specifies if the case management type is visible. |
| `Type` | `Int32` | no |  | enum | The base type of the case management type. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `CustomerNonconformity` | 1 |
| `SupplierNonconformity` | 2 |
| `InternalNonconformity` | 3 |
| `Standard8D` | 4 |


## Referenced by

**Inventory**

- [CaseEntry](/entities/Inventory/CaseEntry.md) — `CaseType` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `CaseTypeId` (FK)
- [CaseManagementTemplates](/entities/Inventory/CaseManagementTemplate.md) — `CaseManagementTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Description": null,
  "IsPreset": false,
  "Number": 0,
  "Prefix": null,
  "Priority": 0,
  "Visible": false,
  "Type": 0
}
```
