---
type: API Entity
title: CustomerOrderRowInflows
description: Represents a customer order inflow row.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderRowInflow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderRowInflow.html
  title: Monitor API — CustomerOrderRowInflow
module: Sales
api_class: CustomerOrderRowInflow
doc_name: CustomerOrderRowInflows
endpoint: GET /api/v1/Sales/CustomerOrderRowInflows
guid: 446FED74-283D-4566-AC69-BF3F207946AA
permission: Show customer orders
introduced_in: '23.3'
property_count: 24
references_out:
- /entities/Common/Currency.md
- /entities/Common/Unit.md
- /entities/Inventory/Part.md
- /entities/Sales/CustomerOrderRow.md
---

# CustomerOrderRowInflows

Represents a customer order inflow row.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `CustomerOrderRowInflow`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderRowInflows`
- **Required permission:** Show customer orders
- **GUID:** `446FED74-283D-4566-AC69-BF3F207946AA`
- **Introduced in:** 23.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the inflow row. |
| `OrderRowId` | `Int64?` | yes | [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) |  | The business key identifier of the inflow rows customer order row. |
| `OrderRow` | `CustomerOrderRows` | no | [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) | expandable | The inflow rows customer order row. |
| `BlanketOrderSalesRowId` | `Int64?` | yes |  |  | The business key identifier of the inflow rows blanket order sales row. |
| `PartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the inflow rows part. |
| `Part` | `Parts` | no | [Parts](/entities/Inventory/Part.md) | expandable | The inflow rows part. |
| `EntityIdentityString` | `String` | no |  | max length 20 | The human readable identifier of the entity subject of the inflow row. |
| `AdditionalRowDescription` | `String` | no |  | max length 80 | The additional row description of the inflow row. |
| `Status` | `Int32` | no |  | enum | The status of the inflow row. |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  |  | The logging timestamp of the inflow row. |
| `OrderedQuantityChange` | `Decimal?` | yes |  |  | The ordered quantity change of the inflow row. |
| `UnitId` | `Int64?` | yes |  |  | The business key identifier of the inflow rows unit. |
| `Unit` | `Units` | no | [Units](/entities/Common/Unit.md) | expandable | The inflow rows unit. |
| `PriceChange` | `Decimal?` | yes |  |  | The price change of the inflow row. |
| `PriceChangeCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the inflow rows price changes currency. |
| `PriceChangeCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The inflow rows price changes currency. |
| `SetupPriceChange` | `Decimal?` | yes |  |  | The setup price change of the inflow row. |
| `SetupPriceChangeCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the inflow rows setup price changes currency. |
| `SetupPriceChangeCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The inflow rows setup price changes currency. |
| `DiscountChange` | `Decimal?` | yes |  |  | The discount change of the inflow row. |
| `TotalValueChange` | `Decimal` | no |  |  | The total value change of the inflow row. |
| `TotalValueChangeCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the inflow rows total value changes currency. |
| `TotalValueChangeCurrency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The inflow rows total value changes currency. |
| `OrderRowType` | `Int32` | no |  | enum | The order row type of the inflow row. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `New` | 0 |
| `Changed` | 1 |
| `Removed` | 2 |

### OrderRowType

| Name | Value |
| --- | ---: |
| `Part` | 1 |
| `Additional` | 2 |
| `Sum` | 3 |
| `FreeText` | 4 |


## Example

```json
{
  "Id": 0,
  "OrderRowId": null,
  "OrderRow": null,
  "BlanketOrderSalesRowId": null,
  "PartId": null,
  "Part": null,
  "EntityIdentityString": null,
  "AdditionalRowDescription": null,
  "Status": 0,
  "LoggingTimeStamp": "0001-01-01T00:00:00+00:00",
  "OrderedQuantityChange": null,
  "UnitId": null,
  "Unit": null,
  "PriceChange": null,
  "PriceChangeCurrencyId": null,
  "PriceChangeCurrency": null,
  "SetupPriceChange": null,
  "SetupPriceChangeCurrencyId": null,
  "SetupPriceChangeCurrency": null,
  "DiscountChange": null,
  "TotalValueChange": 0.0,
  "TotalValueChangeCurrencyId": null,
  "TotalValueChangeCurrency": null,
  "OrderRowType": 0
}
```
