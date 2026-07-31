---
type: API Entity
title: PurchaseOrderTypes
description: Represents a purchase order type.
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderType.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderType.html
  title: Monitor API — PurchaseOrderType
module: Purchase
api_class: PurchaseOrderType
doc_name: PurchaseOrderTypes
endpoint: GET /api/v1/Purchase/PurchaseOrderTypes
guid: D727E289-88F2-495E-8869-F122B0E8453D
permission: Show order types
introduced_in: '2.26'
property_count: 12
references_out:
- /entities/Common/CurrencyExchangeType.md
referenced_by:
- /entities/Purchase/PurchaseOrder.md
---

# PurchaseOrderTypes

Represents a purchase order type.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `PurchaseOrderType`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderTypes`
- **Required permission:** Show order types
- **GUID:** `D727E289-88F2-495E-8869-F122B0E8453D`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the type. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the type. |
| `Prefix` | `String` | no |  | max length 80 | The prefix applied to purchase order numbers for this type. |
| `Description` | `String` | no |  | max length 400 | The translated description of the type. |
| `Priority` | `Int32` | no |  |  | The priority of the type. |
| `Visible` | `Boolean` | no |  |  | Specifies if the type is visible. |
| `IsPreset` | `Boolean` | no |  |  | Specifies if the type is a preset type. |
| `IncludeInPurchaseStatistics` | `Boolean` | no |  |  | Specifies if purchase orders of this type should be included in statistics. |
| `BaseType` | `Int32` | no |  | enum | The base type of purchase orders created using this type. |
| `CodingGroupId` | `Int64` | no |  |  | The business key identifier of the type's coding group. |
| `RateTypeSetting` | `Int32` | no |  | enum, since 22.9 | The rate type setting of the purchase order type. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the purchase order type's currency exchange type. |

## Enumerations

### BaseType

| Name | Value |
| --- | ---: |
| `Acquisition` | 0 |
| `Subcontract` | 1 |
| `StockOrder` | 2 |
| `ReturnOrder` | 3 |
| `Agreement` | 4 |

### RateTypeSetting

| Name | Value |
| --- | ---: |
| `Supplier` | 1 |
| `OrderType` | 2 |


## Referenced by

**Purchase**

- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `OrderType` (expand)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `OrderTypeId` (FK)


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
  "IncludeInPurchaseStatistics": false,
  "BaseType": 0,
  "CodingGroupId": 0,
  "RateTypeSetting": 0,
  "CurrencyExchangeTypeId": null
}
```
