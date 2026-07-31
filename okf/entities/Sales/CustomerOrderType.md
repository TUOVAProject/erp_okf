---
type: API Entity
title: CustomerOrderTypes
description: Represents a customer order type.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderType.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderType.html
  title: Monitor API — CustomerOrderType
module: Sales
api_class: CustomerOrderType
doc_name: CustomerOrderTypes
endpoint: GET /api/v1/Sales/CustomerOrderTypes
guid: e0620e45-0f23-4148-a4eb-79ec9d6375a0
permission: Show order types
introduced_in: '2.18'
property_count: 19
references_out:
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/PaymentTerm.md
- /entities/Common/PriceList.md
- /entities/Common/TransferProfile.md
referenced_by:
- /entities/Sales/CustomerOrder.md
- /entities/Sales/QuoteType.md
---

# CustomerOrderTypes

Represents a customer order type.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `CustomerOrderType`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderTypes`
- **Required permission:** Show order types
- **GUID:** `e0620e45-0f23-4148-a4eb-79ec9d6375a0`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the type. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the type. |
| `Prefix` | `String` | no |  | max length 80 | The prefix applied to customer order numbers for this type. |
| `Description` | `String` | no |  | max length 400 | The translated description of the type. |
| `Priority` | `Int32` | no |  |  | The priority of the type. |
| `Visible` | `Boolean` | no |  |  | Specifies if the type is visible. |
| `IsPreset` | `Boolean` | no |  |  | Specifies if the type is a preset type. |
| `PriceSetting` | `Int32` | no |  | enum | The price settings of the type. |
| `PriceListId` | `Int64?` | yes | [PriceLists](/entities/Common/PriceList.md) |  | The business key identifier of the type's price list. |
| `IncludeInDeliveryAnalysis` | `Boolean` | no |  |  | Specifies if customer orders of this type should be included in delivery analysis. |
| `IncludeInStatistics` | `Boolean` | no |  |  | Specifies if customer orders of this type should be included in statistics. |
| `InvoiceType` | `Int32?` | yes |  | enum | The default invoice type of customer orders created with this type. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](/entities/Common/PaymentTerm.md) |  | The business key identifier of the type's default payment term. References a PaymentTerms |
| `PurchaseOrderAddressStrategy` | `Int32` | no |  | enum | The purchase order from customer order address strategy to use for customer orders of this type. |
| `BaseType` | `Int32` | no |  | enum | The base type of customer orders created using this type. |
| `CodingGroupId` | `Int64` | no |  |  | The business key identifier of the type's coding group. |
| `RateTypeSetting` | `Int32` | no |  | enum, since 22.9 | The rate type setting of the customer order type. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the customer order type's currency exchange type. |
| `DefaultTransferProfileId` | `Int64?` | yes | [TransferProfiles](/entities/Common/TransferProfile.md) | since 23.2 | The business key identifier of the customer order's default transfer profile. |

## Enumerations

### PriceSetting

| Name | Value |
| --- | ---: |
| `Customer` | 1 |
| `PriceList` | 2 |
| `StandardPrice` | 3 |

### InvoiceType

| Name | Value |
| --- | ---: |
| `Standard` | 1 |
| `Internal` | 2 |
| `CashReceipt` | 3 |
| `Interest` | 4 |
| `OnAccount` | 5 |
| `DebitNote` | 6 |
| `ServiceTax` | 7 |
| `CorrectionInvoice` | 8 |
| `CollectiveCorrectionInvoice` | 9 |

### PurchaseOrderAddressStrategy

| Name | Value |
| --- | ---: |
| `CustomerOrder` | 0 |
| `Company` | 1 |

### BaseType

| Name | Value |
| --- | ---: |
| `NewSales` | 0 |
| `StockOrder` | 1 |
| `Agreement` | 2 |

### RateTypeSetting

| Name | Value |
| --- | ---: |
| `Customer` | 1 |
| `OrderType` | 2 |


## Referenced by

**Sales**

- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `OrderType` (expand)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `OrderTypeId` (FK)
- [QuoteTypes](/entities/Sales/QuoteType.md) — `CustomerOrderType` (expand)
- [QuoteTypes](/entities/Sales/QuoteType.md) — `CustomerOrderTypeId` (FK)


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
  "IncludeInDeliveryAnalysis": false,
  "IncludeInStatistics": false,
  "InvoiceType": null,
  "PaymentTermId": null,
  "PurchaseOrderAddressStrategy": 0,
  "BaseType": 0,
  "CodingGroupId": 0,
  "RateTypeSetting": 0,
  "CurrencyExchangeTypeId": null,
  "DefaultTransferProfileId": null
}
```
