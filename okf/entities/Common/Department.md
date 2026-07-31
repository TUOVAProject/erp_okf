---
type: API Entity
title: Departments
description: Represents a queryable department.
resource: https://api.monitor.se/api/Monitor.API.Common.Department.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Department.html
  title: Monitor API — Department
module: Common
api_class: Department
doc_name: Departments
endpoint: GET /api/v1/Common/Departments
guid: b70b9b65-d77e-4e00-99ad-ddefce8ab14e
permission: Show departments
introduced_in: '2.18'
property_count: 3
referenced_by:
- /entities/Accounting/FixedAsset.md
- /entities/Common/Person.md
- /entities/Inventory/CaseEntry.md
---

# Departments

Represents a queryable department.

- **Module:** [Common](/modules/Common.md)
- **API class:** `Department`
- **Endpoint:** `GET /api/v1/Common/Departments`
- **Required permission:** Show departments
- **GUID:** `b70b9b65-d77e-4e00-99ad-ddefce8ab14e`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the department. |
| `Code` | `String` | no |  | unique, max length 6 | The human readable code of the department. |
| `Description` | `String` | no |  |  | The translated description of the department. |

## Referenced by

**Accounting**

- [FixedAssets](/entities/Accounting/FixedAsset.md) — `DepartmentId` (FK)

**Common**

- [Persons](/entities/Common/Person.md) — `DepartmentId` (FK)

**Inventory**

- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ReasonDepartmentId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null
}
```
