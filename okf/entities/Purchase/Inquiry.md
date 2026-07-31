---
type: API Entity
title: Inquiries
description: Represents an inquiry.
resource: https://api.monitor.se/api/Monitor.API.Purchase.Inquiry.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.Inquiry.html
  title: Monitor API — Inquiry
module: Purchase
api_class: Inquiry
doc_name: Inquiries
endpoint: GET /api/v1/Purchase/Inquiries
guid: 83CDAF78-6D8B-4397-BBC0-D42061CA901D
permission: Show inquiry
introduced_in: '2.30'
property_count: 49
references_out:
- /entities/Common/Address.md
- /entities/Common/Comment.md
- /entities/Common/CommunicationAddress.md
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/DeliveryMethod.md
- /entities/Common/DeliveryTerm.md
- /entities/Common/PaymentTerm.md
- /entities/Common/Person.md
- /entities/Common/Project.md
- /entities/Common/VatGroup.md
- /entities/Common/Warehouse.md
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/InquiryType.md
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Purchase/InquiryRow.md
---

# Inquiries

Represents an inquiry.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `Inquiry`
- **Endpoint:** `GET /api/v1/Purchase/Inquiries`
- **Required permission:** Show inquiry
- **GUID:** `83CDAF78-6D8B-4397-BBC0-D42061CA901D`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the inquiry. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](/entities/Common/PaymentTerm.md) |  | The business key identifier of the inquiry's payment term. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](/entities/Common/PaymentTerm.md) | expandable | The payment term of the inquiry. |
| `PaymentTermDescription` | `String` | no |  | max length 35 | The payment term description of the inquiry. |
| `GracePeriodInDays` | `Int32?` | yes |  |  | The inquiry's grace period in days. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](/entities/Common/DeliveryMethod.md) |  | The business key identifier of the inquiry's delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](/entities/Common/DeliveryTerm.md) |  | The business key identifier of the inquiry's delivery term. |
| `DeliveryTermDescription` | `String` | no |  | max length 35 | The delivery term description of the inquiry. |
| `DeliveryMethodDescription` | `String` | no |  | max length 35 | The delivery method description of the inquiry. |
| `BusinessContactOrderNumber` | `String` | no |  | max length 30 | The supplier's inquiry number. |
| `OurReferenceId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of our reference on the inquiry. Reference Persons |
| `OurReferenceName` | `String` | no |  | max length 80 | The name of our reference on the inquiry. |
| `BusinessContactReferenceId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the supplier's reference on the inquiry. Reference Persons |
| `BusinessContactReferenceName` | `String` | no |  | max length 80 | The name of the supplier's reference on the inquiry. |
| `GoodsLabel` | `String` | no |  | max length 80 | The goods label of the inquiry. |
| `CurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the inquiry's currency. |
| `VatGroupId` | `Int64` | no | [VatGroups](/entities/Common/VatGroup.md) |  | The business key identifier of the inquiry's VAT group. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the inquiry's warehouse. |
| `Priority` | `Int32` | no |  |  | The priority of the inquiry. |
| `ProjectId` | `Int64?` | yes | [Projects](/entities/Common/Project.md) |  | The business key identifier of the inquiry's project. |
| `SendMethod` | `Int32` | no |  | enum | Specifies the method of the inquiry printout. |
| `InternalCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the inquiry's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The internal comment of the inquiry. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the inquiry's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The external comment of the inquiry. |
| `TransportTime` | `Int32?` | yes |  |  | The transport time of the inquiry. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the inquiry. |
| `Version` | `Int32` | no |  |  | The version of the inquiry. |
| `UseForwardRate` | `Boolean` | no |  |  | Specifies if forward rate should be used. |
| `ExchangeRate` | `Decimal` | no |  |  | The exchange rate to use for the inquiry. |
| `SupplierId` | `Int64` | no | [Suppliers](/entities/Purchase/Supplier.md) | mandatory | The business key identifier of the supplier that the inquiry belongs to. |
| `OrderNumber` | `String` | no |  | max length 15 | The order number of the purchase order created as a result of the inquiry. |
| `OrderDate` | `DateTimeOffset?` | yes |  |  | The date/time when the inquiry was made. |
| `Rows` | `InquiryRows[]` | no | [InquiryRows](/entities/Purchase/InquiryRow.md) | expandable, collection | The rows of the inquiry. |
| `CreatedById` | `Int64?` | yes | [Persons](/entities/Common/Person.md) | **deprecated since 24.3** | The business key identifier of the inquiry's creator. _(Unavailable)_ |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](/entities/Common/Address.md) |  | The business key identifier of the inquiry's delivery address. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](/entities/Common/Address.md) | expandable | The delivery address of the inquiry. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](/entities/Common/Address.md) |  | The business key identifier of the inquiry's mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](/entities/Common/Address.md) | expandable | The mailing address of the inquiry. |
| `VatNumber` | `String` | no |  | max length 80, **deprecated since 24.3** | The VAT number on the inquiry. _(Unavailable)_ |
| `Status` | `Int32` | no |  | enum | The status of the inquiry. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](/entities/Common/CommunicationAddress.md) | expandable, collection | The communication addresses registered on the inquiry. |
| `InquiryDate` | `DateTimeOffset` | no |  |  | The date when the inquiry was made to the supplier. |
| `InquiryDescription` | `String` | no |  | max length 200 | The description of the inquiry. |
| `LatestContactDate` | `DateTimeOffset?` | yes |  |  | The last contact date on the inquiry. |
| `ValidThroughDate` | `DateTimeOffset?` | yes |  |  | The valid through date of the inquiry. |
| `OrderTypeId` | `Int64?` | yes | [InquiryTypes](/entities/Purchase/InquiryType.md) | since 2.30 | The business key identifier of the inquiry's inquiry type. |
| `OrderType` | `InquiryTypes` | no | [InquiryTypes](/entities/Purchase/InquiryType.md) | expandable, since 2.30 | The inquiry type used on the inquiry. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the inquiry's currency exchange type. |

## Enumerations

### SendMethod

| Name | Value |
| --- | ---: |
| `Printer` | 0 |
| `Email` | 1 |
| `Edi` | 2 |
| `None` | 9 |

### LifeCycleState

| Name | Value |
| --- | ---: |
| `Transient` | 1 |
| `Persistent` | 10 |
| `History` | 20 |
| `RemovableCandidate` | 99 |

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `Printed` | 2 |
| `Responded` | 3 |
| `Closed` | 6 |
| `PartialOrder` | 7 |
| `OrderViaRelatedInquiry` | 8 |
| `Order` | 9 |


## Referenced by

**Purchase**

- [InquiryRows](/entities/Purchase/InquiryRow.md) — `ParentOrderId` (FK)


## Example

```json
{
  "Id": 0,
  "PaymentTermId": null,
  "PaymentTerm": null,
  "PaymentTermDescription": null,
  "GracePeriodInDays": null,
  "DeliveryMethodId": null,
  "DeliveryTermId": null,
  "DeliveryTermDescription": null,
  "DeliveryMethodDescription": null,
  "BusinessContactOrderNumber": null,
  "OurReferenceId": null,
  "OurReferenceName": null,
  "BusinessContactReferenceId": null,
  "BusinessContactReferenceName": null,
  "GoodsLabel": null,
  "CurrencyId": 0,
  "VatGroupId": 0,
  "WarehouseId": 0,
  "Priority": 0,
  "ProjectId": null,
  "SendMethod": 0,
  "InternalCommentId": null,
  "InternalComment": null,
  "ExternalCommentId": null,
  "ExternalComment": null,
  "TransportTime": null,
  "LifeCycleState": 0,
  "Version": 0,
  "UseForwardRate": false,
  "ExchangeRate": 0.0,
  "SupplierId": 0,
  "OrderNumber": null,
  "OrderDate": null,
  "Rows": null,
  "CreatedById": null,
  "DeliveryAddressId": null,
  "DeliveryAddress": null,
  "MailingAddressId": null,
  "MailingAddress": null,
  "VatNumber": null,
  "Status": 0,
  "CommunicationAddresses": null,
  "InquiryDate": "0001-01-01T00:00:00+00:00",
  "InquiryDescription": null,
  "LatestContactDate": null,
  "ValidThroughDate": null,
  "OrderTypeId": null,
  "OrderType": null,
  "CurrencyExchangeTypeId": 0
}
```
