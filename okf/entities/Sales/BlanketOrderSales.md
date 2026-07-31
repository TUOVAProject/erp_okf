---
type: API Entity
title: BlanketOrderSales
description: Represents a blanket order for sales.
resource: https://api.monitor.se/api/Monitor.API.Sales.BlanketOrderSales.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BlanketOrderSales.html
  title: Monitor API — BlanketOrderSales
module: Sales
api_class: BlanketOrderSales
doc_name: BlanketOrderSales
endpoint: GET /api/v1/Sales/BlanketOrderSales
guid: ABC96016-61A4-45CC-AD2D-B0F543B4855B
permission: Show blanket order
introduced_in: '23.4'
property_count: 39
references_out:
- /entities/Common/Address.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/Person.md
- /entities/Sales/BlanketOrderSalesRow.md
- /entities/Sales/BlanketOrderSalesType.md
- /entities/Sales/Customer.md
referenced_by:
- /entities/Sales/BlanketOrderSalesRow.md
---

# BlanketOrderSales

Represents a blanket order for sales.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `BlanketOrderSales`
- **Endpoint:** `GET /api/v1/Sales/BlanketOrderSales`
- **Required permission:** Show blanket order
- **GUID:** `ABC96016-61A4-45CC-AD2D-B0F543B4855B`
- **Introduced in:** 23.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the blanket order. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the blanket order. |
| `OrderNumber` | `String` | no |  | unique, max length 15 | The human readable identifier of the blanket order. |
| `OrderTypeId` | `Int64?` | yes | [BlanketOrderSalesTypes](/entities/Sales/BlanketOrderSalesType.md) |  | The business key identifier of the blanket order's type. |
| `OrderType` | `BlanketOrderSalesTypes` | no | [BlanketOrderSalesTypes](/entities/Sales/BlanketOrderSalesType.md) | expandable | The type of the blanket order. |
| `BusinessContactId` | `Int64?` | yes | [Customers](/entities/Sales/Customer.md) |  | The business key identifier of the blanket order's customer. |
| `BusinessContact` | `Customers` | no | [Customers](/entities/Sales/Customer.md) | expandable | The customer of the blanket order. |
| `CustomersOrderNumber` | `String` | no |  | max length 30 | The customer's order number of the blanket order. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) |  | The business key identifier of the blanket order's business contact reference. |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) | expandable | The business contact reference of the blanket order. |
| `IncludeInNetRequirementCalculation` | `Boolean` | no |  |  | Specifies if the blanket order is included in net requirement calculation. |
| `BusinessContactReferenceName` | `String` | no |  | max length 80 | The business contact reference name of the blanket order. |
| `OurReferenceId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the blanket order's our reference. |
| `OurReference` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable | Our reference of the blanket order. |
| `OurReferenceName` | `String` | no |  | max length 80 | Our reference name of the blanket order. |
| `ValidationPeriod` | `Int32` | no |  | enum | Specifies the validation period of the blanket order. |
| `ValidFrom` | `DateTimeOffset` | no |  |  | The valid from date of the blanket order. |
| `ValidThrough` | `DateTimeOffset` | no |  |  | The valid through date of the blanket order. |
| `RequirementDate` | `DateTimeOffset` | no |  |  | The requirement date of the blanket order. |
| `Priority` | `Int32` | no |  |  | The priority of the blanket order. |
| `Status` | `Int32` | no |  | enum | The status of the blanket order. |
| `CategoryString` | `String` | no |  | max length 20 | The category string of the blanket order. |
| `UseForwardRate` | `Boolean` | no |  |  | Specifies if the blanket order use forward rate. |
| `ExchangeRate` | `Decimal` | no |  |  | The exchange rate of the blanket order. |
| `CurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the blanket order's currency. |
| `Currency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The currency of the blanket order. |
| `OrderDate` | `DateTimeOffset` | no |  |  | The order date of the blanket order. |
| `DefaultOrderPrintoutVia` | `Int32` | no |  | enum | The default order printout method of the blanket order. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](/entities/Common/Address.md) |  | The business key identifier of the blanket order's mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](/entities/Common/Address.md) | expandable | The mailing address of the blanket order. |
| `InternalCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the blanket order's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The internal comment of the blanket order. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the blanket order's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The external comment of the blanket order. |
| `SellerId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the blanket order's seller. |
| `Seller` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable | The seller of the blanket order. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) |  | The business key identifier of the blanket order's currency exchange type. |
| `CurrencyExchangeType` | `CurrencyExchangeTypes` | no | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) | expandable | The currency exchange type of the blanket order. |
| `Rows` | `BlanketOrderSalesRows[]` | no | [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) | expandable, collection | The rows of the blanket order. |

## Enumerations

### LifeCycleState

| Name | Value |
| --- | ---: |
| `Transient` | 1 |
| `Persistent` | 10 |
| `History` | 20 |
| `RemovableCandidate` | 99 |

### ValidationPeriod

| Name | Value |
| --- | ---: |
| `OrderDate` | 0 |
| `DeliveryDate` | 1 |

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `Printed` | 2 |
| `PartiallyCalledOf` | 7 |
| `FullyCalledOf` | 8 |
| `History` | 9 |

### DefaultOrderPrintoutVia

| Name | Value |
| --- | ---: |
| `Printer` | 0 |
| `Email` | 1 |
| `Edi` | 2 |
| `None` | 9 |


## Referenced by

**Sales**

- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `ParentOrderId` (FK)


## Example

```json
{
  "Id": 0,
  "LifeCycleState": 0,
  "OrderNumber": null,
  "OrderTypeId": null,
  "OrderType": null,
  "BusinessContactId": null,
  "BusinessContact": null,
  "CustomersOrderNumber": null,
  "BusinessContactReferenceId": null,
  "BusinessContactReference": null,
  "IncludeInNetRequirementCalculation": false,
  "BusinessContactReferenceName": null,
  "OurReferenceId": null,
  "OurReference": null,
  "OurReferenceName": null,
  "ValidationPeriod": 0,
  "ValidFrom": "0001-01-01T00:00:00+00:00",
  "ValidThrough": "0001-01-01T00:00:00+00:00",
  "RequirementDate": "0001-01-01T00:00:00+00:00",
  "Priority": 0,
  "Status": 0,
  "CategoryString": null,
  "UseForwardRate": false,
  "ExchangeRate": 0.0,
  "CurrencyId": null,
  "Currency": null,
  "OrderDate": "0001-01-01T00:00:00+00:00",
  "DefaultOrderPrintoutVia": 0,
  "MailingAddressId": null,
  "MailingAddress": null,
  "InternalCommentId": null,
  "InternalComment": null,
  "ExternalCommentId": null,
  "ExternalComment": null,
  "SellerId": null,
  "Seller": null,
  "CurrencyExchangeTypeId": null,
  "CurrencyExchangeType": null,
  "Rows": null
}
```
