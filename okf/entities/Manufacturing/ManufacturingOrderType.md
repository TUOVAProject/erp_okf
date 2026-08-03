---
type: API Entity
title: ManufacturingOrderTypes
description: Represents a manufacturing order type.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderType.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderType.html
  title: Monitor API — ManufacturingOrderType
module: Manufacturing
api_class: ManufacturingOrderType
doc_name: ManufacturingOrderTypes
endpoint: GET /api/v1/Manufacturing/ManufacturingOrderTypes
guid: E7F8D04A-2CDB-47D9-8742-A49BCB6FF225
permission: Show order types
introduced_in: '2.35'
property_count: 5
referenced_by:
- /entities/Manufacturing/ManufacturingOrder.md
---

# ManufacturingOrderTypes

Represents a manufacturing order type.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `ManufacturingOrderType`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderTypes`
- **Required permission:** Show order types
- **GUID:** `E7F8D04A-2CDB-47D9-8742-A49BCB6FF225`
- **Introduced in:** 2.35

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the type. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the type. |
| `Prefix` | `String` | no |  | max length 3 | The prefix applied to manufacturing order numbers for this type. |
| `Description` | `String` | no |  | max length 400 | The translated description of the type. |
| `BaseType` | `Int32` | no |  | enum | The base type of manufacturing orders created using this type. |

## Enumerations

### BaseType

| Name | Value |
| --- | ---: |
| `InventoryControlled` | 0 |
| `CustomerOrderControlled` | 1 |
| `MaintenanceControlled` | 2 |


## Referenced by

**Manufacturing**

- [ManufacturingOrders](ManufacturingOrder.md) — `OrderType` (expand)
- [ManufacturingOrders](ManufacturingOrder.md) — `OrderTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Prefix": null,
  "Description": null,
  "BaseType": 0
}
```
