---
type: API Entity
title: PackageTypes
description: Represents a package type.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PackageType.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PackageType.html
  title: Monitor API — PackageType
module: Inventory
api_class: PackageType
doc_name: PackageTypes
endpoint: GET /api/v1/Inventory/PackageTypes
guid: FBE23B85-1E78-4644-868F-A922DD54199F
permission: Show basic data for part
introduced_in: '2.18'
property_count: 5
referenced_by:
- /entities/Inventory/Part.md
- /entities/Sales/CustomerOrderShippingInformationRow.md
- /entities/Sales/ShipmentPackageInformation.md
---

# PackageTypes

Represents a package type.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PackageType`
- **Endpoint:** `GET /api/v1/Inventory/PackageTypes`
- **Required permission:** Show basic data for part
- **GUID:** `FBE23B85-1E78-4644-868F-A922DD54199F`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the package type. |
| `Number` | `Int64` | no |  | unique | The human readable identifier of the package type. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the package type is active in the system. |
| `Description` | `String` | no |  | max length 35 | The translated description of the package type. |
| `DefaultCode` | `String` | no |  | max length 5 | The default code of the package type. |

## Referenced by

**Inventory**

- [Parts](Part.md) — `PackageType` (expand)
- [Parts](Part.md) — `PackageTypeId` (FK)

**Sales**

- [CustomerOrderShippingInformationRows](../Sales/CustomerOrderShippingInformationRow.md) — `PackageType` (expand)
- [CustomerOrderShippingInformationRows](../Sales/CustomerOrderShippingInformationRow.md) — `PackageTypeId` (FK)
- [ShipmentPackageInformations](../Sales/ShipmentPackageInformation.md) — `PackageType` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "IsActive": false,
  "Description": null,
  "DefaultCode": null
}
```
