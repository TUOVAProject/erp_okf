---
type: API Entity
title: ManufacturingPickingLists
description: Represents a manufacturing picking list.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingPickingList.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingPickingList.html
  title: Monitor API — ManufacturingPickingList
module: Manufacturing
api_class: ManufacturingPickingList
doc_name: ManufacturingPickingLists
endpoint: GET /api/v1/Manufacturing/ManufacturingPickingLists
guid: D122535F-F5F6-486F-8EED-B43426AD17C4
permission: Show manufacturing orders
introduced_in: '2.48'
property_count: 14
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Person.md
- /entities/Common/Warehouse.md
- /entities/Manufacturing/ManufacturingPickingListMaterial.md
---

# ManufacturingPickingLists

Represents a manufacturing picking list.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `ManufacturingPickingList`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingPickingLists`
- **Required permission:** Show manufacturing orders
- **GUID:** `D122535F-F5F6-486F-8EED-B43426AD17C4`
- **Introduced in:** 2.48

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the picking list. |
| `Number` | `String` | no |  |  | The human readable identifier of the picking list. |
| `CreatedByApplicationUserId` | `Int64` | no | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the application user that created the picking list. |
| `CreatedByPersonId` | `Int64` | no | [Persons](../Common/Person.md) |  | The business key identifier of the person that created the picking list. |
| `CreatedTimestamp` | `DateTimeOffset` | no |  |  | The date the picking list was created. |
| `PrintedByApplicationUserId` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the application user that printed the picking list. |
| `PrintedByPersonId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the person that printed the picking list. |
| `PrintedTimestamp` | `DateTimeOffset?` | yes |  |  | The date the picking list was printed. |
| `Status` | `Int32` | no |  | enum | The status of the picking list. |
| `Grouping` | `Int32` | no |  | enum | The grouping for the picking list. |
| `Sorting` | `Int32` | no |  | enum | The sorting for the picking list. |
| `WarehouseId` | `Int64?` | yes | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse for the picking list. |
| `Type` | `Int32` | no |  | enum | The type of picking list. |
| `Materials` | `ManufacturingPickingListMaterials[]` | no | [ManufacturingPickingListMaterials](ManufacturingPickingListMaterial.md) | collection | The picking lists materials |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `Printed` | 2 |
| `Reported` | 5 |
| `History` | 9 |

### Grouping

| Name | Value |
| --- | ---: |
| `Order` | 0 |
| `Material` | 1 |
| `NoGrouping` | 2 |

### Sorting

| Name | Value |
| --- | ---: |
| `Location` | 0 |
| `MainLocation` | 1 |
| `MaterialPartNumber` | 2 |
| `LocationSortingOrder` | 3 |
| `MainLocationSortingOrder` | 4 |

### Type

| Name | Value |
| --- | ---: |
| `Regular` | 0 |
| `Equipment` | 1 |


## Example

```json
{
  "Id": 0,
  "Number": null,
  "CreatedByApplicationUserId": 0,
  "CreatedByPersonId": 0,
  "CreatedTimestamp": "0001-01-01T00:00:00+00:00",
  "PrintedByApplicationUserId": null,
  "PrintedByPersonId": null,
  "PrintedTimestamp": null,
  "Status": 0,
  "Grouping": 0,
  "Sorting": 0,
  "WarehouseId": null,
  "Type": 0,
  "Materials": null
}
```
