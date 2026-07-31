---
type: API Entity
title: BlanketOrderPurchases
description: Represents a blanket order for purchase.
resource: https://api.monitor.se/api/Monitor.API.Purchase.BlanketOrderPurchase.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.BlanketOrderPurchase.html
  title: Monitor API — BlanketOrderPurchase
module: Purchase
api_class: BlanketOrderPurchase
doc_name: BlanketOrderPurchases
endpoint: GET /api/v1/Purchase/BlanketOrderPurchases
guid: A1F017C3-02E1-4E05-A36E-514BDA5D1BF5
permission: Show blanket order
introduced_in: '23.8'
property_count: 33
references_out:
- /entities/Common/Address.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/Person.md
- /entities/Purchase/BlanketOrderPurchaseRow.md
- /entities/Purchase/BlanketOrderPurchaseType.md
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Purchase/BlanketOrderPurchaseRow.md
---

# BlanketOrderPurchases

Represents a blanket order for purchase.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `BlanketOrderPurchase`
- **Endpoint:** `GET /api/v1/Purchase/BlanketOrderPurchases`
- **Required permission:** Show blanket order
- **GUID:** `A1F017C3-02E1-4E05-A36E-514BDA5D1BF5`
- **Introduced in:** 23.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the blanket order. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the blanket order. |
| `OrderNumber` | `String` | no |  | unique, max length 15 | The human readable identifier of the blanket order. |
| `OrderTypeId` | `Int64?` | yes | [BlanketOrderPurchaseTypes](/entities/Purchase/BlanketOrderPurchaseType.md) |  | The business key identifier of the blanket order's type. |
| `BusinessContactId` | `Int64?` | yes | [Suppliers](/entities/Purchase/Supplier.md) |  | The business key identifier of the blanket order's supplier. |
| `SuppliersOrderNumber` | `String` | no |  | max length 30 | The supplier's order number of the blanket order. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) |  | The business key identifier of the blanket order's business contact reference. |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) | expandable | The business contact reference of the blanket order. |
| `BusinessContactReferenceName` | `String` | no |  | max length 80 | The business contact reference name of the blanket order. |
| `OurReferenceId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the blanket order's our reference. |
| `OurReference` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable | Our reference of the blanket order. |
| `OurReferenceName` | `String` | no |  | max length 80 | Our reference name of the blanket order. |
| `ValidationPeriod` | `Int32` | no |  | enum | Specifies the validation period of the blanket order. |
| `ValidFrom` | `DateTimeOffset` | no |  |  | The valid from date of the blanket order. |
| `ValidThrough` | `DateTimeOffset` | no |  |  | The valid through date of the blanket order. |
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
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) |  | The business key identifier of the blanket order's currency exchange type. |
| `CurrencyExchangeType` | `CurrencyExchangeTypes` | no | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) | expandable | The currency exchange type of the blanket order. |
| `Rows` | `BlanketOrderPurchaseRows[]` | no | [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) | expandable, collection | The rows of the blanket order. |

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

**Purchase**

- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `ParentOrderId` (FK)


## Example

```json
{
  "Id": 0,
  "LifeCycleState": 0,
  "OrderNumber": null,
  "OrderTypeId": null,
  "BusinessContactId": null,
  "SuppliersOrderNumber": null,
  "BusinessContactReferenceId": null,
  "BusinessContactReference": null,
  "BusinessContactReferenceName": null,
  "OurReferenceId": null,
  "OurReference": null,
  "OurReferenceName": null,
  "ValidationPeriod": 0,
  "ValidFrom": "0001-01-01T00:00:00+00:00",
  "ValidThrough": "0001-01-01T00:00:00+00:00",
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
  "CurrencyExchangeTypeId": null,
  "CurrencyExchangeType": null,
  "Rows": null
}
```
