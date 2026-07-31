---
type: API Entity
title: QuoteTypes
description: Represents a quote type.
resource: https://api.monitor.se/api/Monitor.API.Sales.QuoteType.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.QuoteType.html
  title: Monitor API — QuoteType
module: Sales
api_class: QuoteType
doc_name: QuoteTypes
endpoint: GET /api/v1/Sales/QuoteTypes
guid: 2789A0CD-4228-4273-987D-429E139DA704
permission: Show order types
introduced_in: '2.18'
property_count: 16
references_out:
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/FormReportConfiguration.md
- /entities/Common/PriceList.md
- /entities/Sales/CustomerOrderType.md
referenced_by:
- /entities/Sales/Quote.md
---

# QuoteTypes

Represents a quote type.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `QuoteType`
- **Endpoint:** `GET /api/v1/Sales/QuoteTypes`
- **Required permission:** Show order types
- **GUID:** `2789A0CD-4228-4273-987D-429E139DA704`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the type. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the type. |
| `Prefix` | `String` | no |  | max length 80 | The prefix to apply on quote numbers spawned from this type. |
| `Description` | `String` | no |  | max length 400 | The translated description of the type. |
| `Priority` | `Int32` | no |  |  | The priority of the type. |
| `Visible` | `Boolean` | no |  |  | Specifies if the type is visible. |
| `IsPreset` | `Boolean` | no |  |  | Specifies if the type is a preset type. |
| `PriceSetting` | `Int32` | no |  | enum | The price setting to apply for quotes of this type. |
| `PriceListId` | `Int64?` | yes | [PriceLists](/entities/Common/PriceList.md) |  | The business key identifier of the type's price list. |
| `BaseType` | `Int32` | no |  | enum | The base type of quotes created from this type. |
| `CodingGroupId` | `Int64` | no |  |  | The business key identifier of the type's coding group. |
| `FormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](/entities/Common/FormReportConfiguration.md) |  | The business key identifier of the type's form report configuration. |
| `RateTypeSetting` | `Int32` | no |  | enum, since 22.9 | The rate type setting of the quote type. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the quote type's currency exchange type. |
| `CustomerOrderTypeId` | `Int64?` | yes | [CustomerOrderTypes](/entities/Sales/CustomerOrderType.md) | since 23.2 | The business key identifier of the quote type's cutomer order type. |
| `CustomerOrderType` | `CustomerOrderTypes` | no | [CustomerOrderTypes](/entities/Sales/CustomerOrderType.md) | expandable, since 23.2 | The quote type's cutomer order type. |

## Enumerations

### PriceSetting

| Name | Value |
| --- | ---: |
| `Customer` | 1 |
| `PriceList` | 2 |
| `StandardPrice` | 3 |

### BaseType

| Name | Value |
| --- | ---: |
| `Quote` | 0 |

### RateTypeSetting

| Name | Value |
| --- | ---: |
| `Customer` | 1 |
| `OrderType` | 2 |


## Referenced by

**Sales**

- [Quotes](/entities/Sales/Quote.md) — `OrderType` (expand)
- [Quotes](/entities/Sales/Quote.md) — `OrderTypeId` (FK)


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
  "PriceSetting": 0,
  "PriceListId": null,
  "BaseType": 0,
  "CodingGroupId": 0,
  "FormReportConfigurationId": null,
  "RateTypeSetting": 0,
  "CurrencyExchangeTypeId": null,
  "CustomerOrderTypeId": null,
  "CustomerOrderType": null
}
```
