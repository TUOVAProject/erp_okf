---
type: API Entity
title: SalesForecasts
description: Represents a sales forecast.
resource: https://api.monitor.se/api/Monitor.API.Inventory.SalesForecast.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.SalesForecast.html
  title: Monitor API — SalesForecast
module: Inventory
api_class: SalesForecast
doc_name: SalesForecasts
endpoint: GET /api/v1/Inventory/SalesForecasts
guid: eb703584-f436-4762-819c-2b1d65ee61f7
permission: Show basic data for part
introduced_in: '22.3'
property_count: 10
references_out:
- /entities/Common/Warehouse.md
- /entities/Inventory/SalesForecastRow.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerAccountGroup.md
- /entities/Sales/CustomerDistrict.md
referenced_by:
- /entities/Inventory/SalesForecastRow.md
---

# SalesForecasts

Represents a sales forecast.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `SalesForecast`
- **Endpoint:** `GET /api/v1/Inventory/SalesForecasts`
- **Required permission:** Show basic data for part
- **GUID:** `eb703584-f436-4762-819c-2b1d65ee61f7`
- **Introduced in:** 22.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the sales forecast. |
| `ForecastCode` | `String` | no |  | unique, max length 8, min length 1 | The human readbale identifier of the sales forecast. |
| `Description` | `String` | no |  |  | The translated description of the sales forecast. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse that the sales forecast belongs to. |
| `TimeSpan` | `TimeSpan` | no |  |  | The interval time span of the sales forecast. |
| `IsActive` | `Boolean` | no |  |  | The flag that indicates if the sales forecast is active. |
| `CustomerId` | `Int64?` | yes | [Customers](../Sales/Customer.md) |  | The business key identifier for the customer of the sales forecast. |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](../Sales/CustomerAccountGroup.md) |  | The business key identifier for the customer account group of the sales forecast. |
| `CustomerDistrictId` | `Int64?` | yes | [CustomerDistricts](../Sales/CustomerDistrict.md) |  | The business key identifier for the customer district of the sales forecast. |
| `SalesForecastRows` | `SalesForecastRows[]` | no | [SalesForecastRows](SalesForecastRow.md) | expandable, collection, since 23.2 | The rows of the sales forecast. |

## Referenced by

**Inventory**

- [SalesForecastRows](SalesForecastRow.md) — `SalesForecastId` (FK)


## Example

```json
{
  "Id": 0,
  "ForecastCode": null,
  "Description": null,
  "WarehouseId": 0,
  "TimeSpan": "00:00:00",
  "IsActive": false,
  "CustomerId": null,
  "CustomerAccountGroupId": null,
  "CustomerDistrictId": null,
  "SalesForecastRows": null
}
```
