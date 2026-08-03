---
type: API Entity
title: BlanketOrderSalesTypes
description: Represents a blanket order type for sales.
resource: https://api.monitor.se/api/Monitor.API.Sales.BlanketOrderSalesType.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BlanketOrderSalesType.html
  title: Monitor API — BlanketOrderSalesType
module: Sales
api_class: BlanketOrderSalesType
doc_name: BlanketOrderSalesTypes
endpoint: GET /api/v1/Sales/BlanketOrderSalesTypes
guid: B54F6031-3B9B-46A4-970A-9522F4EC6537
permission: Show blanket order
introduced_in: '23.4'
property_count: 15
references_out:
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/PriceList.md
- /entities/Common/Warehouse.md
referenced_by:
- /entities/Sales/BlanketOrderSales.md
---

# BlanketOrderSalesTypes

Represents a blanket order type for sales.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `BlanketOrderSalesType`
- **Endpoint:** `GET /api/v1/Sales/BlanketOrderSalesTypes`
- **Required permission:** Show blanket order
- **GUID:** `B54F6031-3B9B-46A4-970A-9522F4EC6537`
- **Introduced in:** 23.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the blanket order type. |
| `Number` | `Int64` | no |  | unique | The number of the blanket order type. |
| `Prefix` | `String` | no |  | max length 3 | The prefix of the blanket order type. |
| `Description` | `String` | no |  | max length 400 | The translated description of the blanket order type. |
| `Priority` | `Int32` | no |  |  | The priority of the blanket order type. |
| `Visible` | `Boolean` | no |  |  | Specifies if the blanket order type is visible. |
| `IsPreset` | `Boolean` | no |  |  | Specifies if the blanket order type is preset. |
| `BaseType` | `Int32` | no |  | enum | The base type of the blanket order type. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the blanket order type's warehouse. |
| `PriceSetting` | `Int32` | no |  | enum | The price setting of the blanket order type. |
| `PriceListId` | `Int64?` | yes | [PriceLists](../Common/PriceList.md) |  | The business key identifier of the blanket order type's price list. |
| `RateTypeSetting` | `Int32` | no |  | enum | The rate typ setting of the blanket order type. |
| `BlanketOrderSalesActivityTemplateId` | `Int64?` | yes |  |  | The business key identifier of the blanket order types activity template. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](../Common/CurrencyExchangeType.md) |  | The business key identifier of the blanket order type's currency exchange type. |
| `DefaultValidDays` | `Int32` | no |  |  | The default valid days of the blanket order type. |

## Enumerations

### BaseType

| Name | Value |
| --- | ---: |
| `BlanketOrder` | 0 |

### PriceSetting

| Name | Value |
| --- | ---: |
| `Customer` | 1 |
| `PriceList` | 2 |
| `StandardPrice` | 3 |

### RateTypeSetting

| Name | Value |
| --- | ---: |
| `Customer` | 1 |
| `OrderType` | 2 |


## Referenced by

**Sales**

- [BlanketOrderSales](BlanketOrderSales.md) — `OrderType` (expand)
- [BlanketOrderSales](BlanketOrderSales.md) — `OrderTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Prefix": null,
  "Description": null,
  "Priority": 0,
  "Visible": false,
  "IsPreset": false,
  "BaseType": 0,
  "WarehouseId": 0,
  "PriceSetting": 0,
  "PriceListId": null,
  "RateTypeSetting": 0,
  "BlanketOrderSalesActivityTemplateId": null,
  "CurrencyExchangeTypeId": null,
  "DefaultValidDays": 0
}
```
