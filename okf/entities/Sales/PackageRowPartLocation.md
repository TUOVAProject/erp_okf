---
type: API Entity
title: PackageRowPartLocations
description: Represents a package row's location.
resource: https://api.monitor.se/api/Monitor.API.Sales.PackageRowPartLocation.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.PackageRowPartLocation.html
  title: Monitor API — PackageRowPartLocation
module: Sales
api_class: PackageRowPartLocation
doc_name: PackageRowPartLocations
endpoint: GET /api/v1/Sales/PackageRowPartLocations
guid: EC6FA6BE-EC57-4381-8890-9863F7DE423C
permission: Show customer orders
introduced_in: '25.5'
property_count: 5
references_out:
- /entities/Inventory/PartLocation.md
- /entities/Inventory/ProductRecord.md
- /entities/Sales/PackageRow.md
---

# PackageRowPartLocations

Represents a package row's location.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `PackageRowPartLocation`
- **Endpoint:** `GET /api/v1/Sales/PackageRowPartLocations`
- **Required permission:** Show customer orders
- **GUID:** `EC6FA6BE-EC57-4381-8890-9863F7DE423C`
- **Introduced in:** 25.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the package row location. |
| `ParentPackageRowId` | `Int64` | no | [PackageRows](PackageRow.md) |  | The business key identifier of the location's parent package row. |
| `PartLocationId` | `Int64` | no | [PartLocations](../Inventory/PartLocation.md) |  | The business key identifier of the package row location's part location. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](../Inventory/ProductRecord.md) |  | The business key identifier of the package row location's product record. |
| `BalanceChange` | `Decimal` | no |  |  | The balance change of the package row location. |

## Example

```json
{
  "Id": 0,
  "ParentPackageRowId": 0,
  "PartLocationId": 0,
  "ProductRecordId": null,
  "BalanceChange": 0.0
}
```
