---
type: API Entity
title: SalesForecastRows
description: Represents a sales forecast row.
resource: https://api.monitor.se/api/Monitor.API.Inventory.SalesForecastRow.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.SalesForecastRow.html
  title: Monitor API — SalesForecastRow
module: Inventory
api_class: SalesForecastRow
doc_name: SalesForecastRows
endpoint: GET /api/v1/Inventory/SalesForecastRows
guid: 170040fd-bfb9-4f48-bea7-40376eb3e7bd
permission: Show basic data for part
introduced_in: '22.3'
property_count: 6
references_out:
- /entities/Common/Unit.md
- /entities/Inventory/Part.md
- /entities/Inventory/SalesForecast.md
referenced_by:
- /entities/Inventory/SalesForecast.md
---

# SalesForecastRows

Represents a sales forecast row.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `SalesForecastRow`
- **Endpoint:** `GET /api/v1/Inventory/SalesForecastRows`
- **Required permission:** Show basic data for part
- **GUID:** `170040fd-bfb9-4f48-bea7-40376eb3e7bd`
- **Introduced in:** 22.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the sales forecast row. |
| `PartId` | `Int64` | no | [Parts](Part.md) |  | The business key identifier for the part of the sales forecast row. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the sales forecast row. |
| `UnitId` | `Int64` | no | [Units](../Common/Unit.md) |  | The business key identifier for the unit of the sales forecast row. |
| `DeliveryDate` | `DateTimeOffset` | no |  |  | The delivery date of the sales forecast row. |
| `SalesForecastId` | `Int64` | no | [SalesForecasts](SalesForecast.md) | since 23.2 | The business key identifier of the sales forecast that the row belongs to. |

## Referenced by

**Inventory**

- [SalesForecasts](SalesForecast.md) — `SalesForecastRows` (expand)


## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "Quantity": 0.0,
  "UnitId": 0,
  "DeliveryDate": "0001-01-01T00:00:00+00:00",
  "SalesForecastId": 0
}
```
