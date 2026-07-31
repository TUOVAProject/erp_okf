---
type: API Entity
title: BlanketOrderPurchaseTypes
description: Represents a blanket order type for purchase.
resource: https://api.monitor.se/api/Monitor.API.Purchase.BlanketOrderPurchaseType.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.BlanketOrderPurchaseType.html
  title: Monitor API — BlanketOrderPurchaseType
module: Purchase
api_class: BlanketOrderPurchaseType
doc_name: BlanketOrderPurchaseTypes
endpoint: GET /api/v1/Purchase/BlanketOrderPurchaseTypes
guid: 9DBE25A4-F742-4A8C-8045-D54E0EE1833A
permission: Show blanket order
introduced_in: '26.3'
property_count: 12
references_out:
- /entities/Common/CurrencyExchangeType.md
referenced_by:
- /entities/Purchase/BlanketOrderPurchase.md
---

# BlanketOrderPurchaseTypes

Represents a blanket order type for purchase.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `BlanketOrderPurchaseType`
- **Endpoint:** `GET /api/v1/Purchase/BlanketOrderPurchaseTypes`
- **Required permission:** Show blanket order
- **GUID:** `9DBE25A4-F742-4A8C-8045-D54E0EE1833A`
- **Introduced in:** 26.3

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
| `BlanketOrderPurchaseActivityTemplateId` | `Int64?` | yes |  |  | The business key identifier of the blanket order types activity template. |
| `RateTypeSetting` | `Int32` | no |  | enum | The rate typ setting of the blanket order type. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) |  | The business key identifier of the blanket order type's currency exchange type. |
| `DefaultValidDays` | `Int32` | no |  |  | The default valid days of the blanket order type. |

## Enumerations

### BaseType

| Name | Value |
| --- | ---: |
| `BlanketOrder` | 0 |

### RateTypeSetting

| Name | Value |
| --- | ---: |
| `Supplier` | 1 |
| `OrderType` | 2 |


## Referenced by

**Purchase**

- [BlanketOrderPurchases](/entities/Purchase/BlanketOrderPurchase.md) — `OrderTypeId` (FK)


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
  "BlanketOrderPurchaseActivityTemplateId": null,
  "RateTypeSetting": 0,
  "CurrencyExchangeTypeId": null,
  "DefaultValidDays": 0
}
```
