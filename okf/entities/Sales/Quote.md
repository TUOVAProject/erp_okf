---
type: API Entity
title: Quotes
description: Represents a quote.
resource: https://api.monitor.se/api/Monitor.API.Sales.Quote.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.Quote.html
  title: Monitor API — Quote
module: Sales
api_class: Quote
doc_name: Quotes
endpoint: GET /api/v1/Sales/Quotes
guid: FC8419EB-AF90-4416-A025-8C41B29AE06B
permission: Show quote
introduced_in: '2.18'
property_count: 80
references_out:
- /entities/Common/Address.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/CommunicationAddress.md
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/DeliveryMethod.md
- /entities/Common/DeliveryTerm.md
- /entities/Common/DeliveryTime.md
- /entities/Common/PaymentTerm.md
- /entities/Common/Person.md
- /entities/Common/Probability.md
- /entities/Common/VatGroup.md
- /entities/Common/Warehouse.md
- /entities/Sales/BusinessOpportunity.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerAccountGroup.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/QuoteType.md
- /entities/Sales/ReasonCodeLostQuote.md
- /entities/Sales/RelatedQuote.md
- /entities/Sales/ValidityTime.md
referenced_by:
- /entities/Sales/QuoteActivity.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/RelatedQuoteEntry.md
---

# Quotes

Represents a quote.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `Quote`
- **Endpoint:** `GET /api/v1/Sales/Quotes`
- **Required permission:** Show quote
- **GUID:** `FC8419EB-AF90-4416-A025-8C41B29AE06B`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the quote. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](../Common/PaymentTerm.md) |  | The business key identifier of the quote's payment term. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](../Common/PaymentTerm.md) | expandable | The payment term of the quote. |
| `PaymentTermDescription` | `String` | no |  | max length 35 | The payment term description of the quote. |
| `GracePeriodInDays` | `Int32?` | yes |  |  | The quote's grace period in days. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](../Common/DeliveryMethod.md) |  | The business key identifier of the quote's delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](../Common/DeliveryTerm.md) |  | The business key identifier of the quote's delivery term. |
| `DeliveryTermDescription` | `String` | no |  | max length 35 | The delivery term description of the quote. |
| `DeliveryMethodDescription` | `String` | no |  | max length 35 | The delivery method description of the quote. |
| `ShipmentPayer` | `Int32` | no |  | enum | Specifies the shipment payer of the quote. |
| `BusinessContactOrderNumber` | `String` | no |  | max length 30 | The customer's quote number. |
| `OurReferenceId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of our reference on the quote. Reference Persons |
| `OurReferenceName` | `String` | no |  | max length 80 | The name of our reference on the quote. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](../Common/BusinessContactReference.md) |  | The business key identifier of the customer's reference on the quote. |
| `BusinessContactReferenceName` | `String` | no |  | max length 80 | The name of the customer's reference on the quote. |
| `GoodsLabel` | `String` | no |  | max length 80 | The goods label of the quote. |
| `CurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the quote's currency. |
| `VatGroupId` | `Int64` | no | [VatGroups](../Common/VatGroup.md) |  | The business key identifier of the quote's VAT group. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the quote's warehouse. |
| `Priority` | `Int32` | no |  |  | The priority of the quote. |
| `ProjectId` | `Int64?` | yes |  |  | The business key identifier of the quote's project. |
| `SendMethod` | `Int32` | no |  | enum | Specifies the method of the quote printout. |
| `InvoicePrintoutMethod` | `Int32` | no |  | enum | Specifies the method of future invoice printouts resulted from the quote. |
| `InternalCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the quote's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The internal comment of the quote. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the quote's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The external comment of the quote. |
| `TransportTime` | `Int32?` | yes |  |  | The transport time of the quote. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the quote. |
| `Version` | `Int32` | no |  |  | The version of the quote. |
| `UseForwardRate` | `Boolean` | no |  |  | Specifies if forward rate should be used. |
| `ExchangeRate` | `Decimal` | no |  |  | The exchange rate to use for the quote. |
| `OrderAmount` | `Decimal` | no |  | **deprecated since 2.36** | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `OrderAmountInCompanyCurrency` | `Decimal` | no |  | **deprecated since 2.36** | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `CustomerId` | `Int64` | no | [Customers](Customer.md) |  | The business key identifier of the customer that the quote belongs to. |
| `OrderNumber` | `String` | no |  | max length 15 | The order number of the customer order created as a result of the quote. |
| `OrderDate` | `DateTimeOffset?` | yes |  |  | The date/time when the quote was made into an order. |
| `Rows` | `QuoteRows[]` | no | [QuoteRows](QuoteRow.md) | expandable, collection | The rows of the quote. |
| `SellerId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the quote's seller. |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the quote's delivery address. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The delivery address of the quote. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the quote's mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The mailing address of the quote. |
| `VatNumber` | `String` | no |  | max length 80 | The VAT number on the quote. |
| `Status` | `Int32` | no |  | enum | The status of the quote. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](../Common/CommunicationAddress.md) | expandable, collection | The communication addresses registered on the quote. |
| `QuoteDate` | `DateTimeOffset` | no |  |  | The date when the quote was made to the customer. |
| `QuoteDescription` | `String` | no |  | max length 200 | The description of the quote. |
| `LatestContactDate` | `DateTimeOffset?` | yes |  |  | The last contact date on the quote. |
| `RequestForQuoteDate` | `DateTimeOffset` | no |  |  | The date when the RFQ was made. |
| `ValidityTimeId` | `Int64?` | yes | [ValidityTimes](ValidityTime.md) |  | The business key identifier of the validity time of the quote. |
| `ValidityTime` | `ValidityTimes` | no | [ValidityTimes](ValidityTime.md) | expandable | The validity time of the quote. |
| `ValidityTimeDescription` | `String` | no |  | max length 30 | The validity time description of the quote. |
| `ValidityTimeInDays` | `Int32` | no |  |  | The validity time of the quote in days. |
| `ValidThroughDate` | `DateTimeOffset` | no |  |  | The valid through date of the quote. |
| `ProbabilityId` | `Int64` | no | [Probabilities](../Common/Probability.md) |  | The business key of the quote's probability. References a Probabilities |
| `Probability` | `Probabilities` | no | [Probabilities](../Common/Probability.md) |  | The probability of the quote. |
| `ReasonCodeLostQuoteId` | `Int64?` | yes | [ReasonCodeLostQuotes](ReasonCodeLostQuote.md) |  | The business key identifier of the reason why the quote was lost. |
| `ReasonCodeLostQuote` | `ReasonCodeLostQuotes` | no | [ReasonCodeLostQuotes](ReasonCodeLostQuote.md) | expandable | The reason why the quote was lost. |
| `ReasonLostCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the quote's reason of loss comment. Reference Comments |
| `ReasonLostComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The reason of loss comment for the quote. |
| `OrderTypeId` | `Int64?` | yes | [QuoteTypes](QuoteType.md) | since 2.27 | The business key identifier of the quote's quote type. |
| `OrderType` | `QuoteTypes` | no | [QuoteTypes](QuoteType.md) | expandable, since 2.27 | The quote type used on the quote. |
| `Preliminary` | `Boolean` | no |  | since 2.53 | Specifies if the quote is to be considered preliminary. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](../Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the quote's currency exchange type. |
| `DeliveryTimeId` | `Int64?` | yes | [DeliveryTimes](../Common/DeliveryTime.md) | since 23.6 | The business key identifier of the quote's delivery time. |
| `DeliveryTime` | `DeliveryTimes` | no | [DeliveryTimes](../Common/DeliveryTime.md) | expandable, since 23.6 | The delivery time of the quote. |
| `DeliveryTimeInDays` | `Int32?` | yes |  | since 23.6 | The delivery time in days of the quote. |
| `AccountGroupId` | `Int64` | no | [CustomerAccountGroups](CustomerAccountGroup.md) | since 24.2 | The business key identifier of the account group of the quote. |
| `AccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](CustomerAccountGroup.md) | expandable, since 24.2 | The account group on the quote. |
| `CategoryString` | `String` | no |  | max length 20, since 24.3 | The category string on the quote. |
| `DestinationForDeliveryTerm` | `String` | no |  | max length 80, since 24.7 | The destination for the delivery term. |
| `EditedOrderAmountExcludingVat` | `Decimal?` | yes |  | since 24.8 | The edited order amount excluding VAT for the quote. |
| `EditedOrderAmountExcludingVatCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) | since 24.8 | The currency of the edited order amount excluding VAT for the quote. |
| `EditedOrderAmountDiscount` | `Decimal?` | yes |  | since 24.8 | The edited order amount discount in percent for the quote. |
| `TypeOfOrderAmountEntered` | `Int32?` | yes |  | enum, since 24.8 | The type of edited order value entered on the quote. |
| `Factoring` | `Boolean` | no |  | since 25.7 | Specifies if factoring is activated for the quote. |
| `BusinessOpportunityId` | `Int64?` | yes | [BusinessOpportunities](BusinessOpportunity.md) | since 25.9 | The business key identifier of the business opportunity of the quote. |
| `BusinessOpportunity` | `BusinessOpportunities` | no | [BusinessOpportunities](BusinessOpportunity.md) | expandable, since 25.9 | The business opportunity of the quote. |
| `RelatedQuotesId` | `Int64?` | yes | [RelatedQuotes](RelatedQuote.md) | since 26.2 | The business key identifier of the related quotes placeholder. |

## Enumerations

### ShipmentPayer

| Name | Value |
| --- | ---: |
| `BuyerPays` | 1 |
| `SellerPays` | 2 |
| `OtherPayer` | 3 |
| `Incoterms` | 4 |

### SendMethod

| Name | Value |
| --- | ---: |
| `Printer` | 0 |
| `Email` | 1 |
| `Edi` | 2 |
| `None` | 9 |

### InvoicePrintoutMethod

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
| `Closed` | 6 |
| `PartialOrder` | 7 |
| `OrderViaRelatedQuote` | 8 |
| `Order` | 9 |

### TypeOfOrderAmountEntered

| Name | Value |
| --- | ---: |
| `Percent` | 1 |
| `Amount` | 2 |


## Referenced by

**Sales**

- [QuoteActivities](QuoteActivity.md) — `QuoteId` (FK)
- [QuoteRows](QuoteRow.md) — `ParentOrderId` (FK)
- [RelatedQuoteEntries](RelatedQuoteEntry.md) — `QuoteId` (FK)


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
  "ShipmentPayer": 0,
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
  "InvoicePrintoutMethod": 0,
  "InternalCommentId": null,
  "InternalComment": null,
  "ExternalCommentId": null,
  "ExternalComment": null,
  "TransportTime": null,
  "LifeCycleState": 0,
  "Version": 0,
  "UseForwardRate": false,
  "ExchangeRate": 0.0,
  "OrderAmount": 0.0,
  "OrderAmountInCompanyCurrency": 0.0,
  "CustomerId": 0,
  "OrderNumber": null,
  "OrderDate": null,
  "Rows": null,
  "SellerId": null,
  "DeliveryAddressId": null,
  "DeliveryAddress": null,
  "MailingAddressId": null,
  "MailingAddress": null,
  "VatNumber": null,
  "Status": 0,
  "CommunicationAddresses": null,
  "QuoteDate": "0001-01-01T00:00:00+00:00",
  "QuoteDescription": null,
  "LatestContactDate": null,
  "RequestForQuoteDate": "0001-01-01T00:00:00+00:00",
  "ValidityTimeId": null,
  "ValidityTime": null,
  "ValidityTimeDescription": null,
  "ValidityTimeInDays": 0,
  "ValidThroughDate": "0001-01-01T00:00:00+00:00",
  "ProbabilityId": 0,
  "Probability": null,
  "ReasonCodeLostQuoteId": null,
  "ReasonCodeLostQuote": null,
  "ReasonLostCommentId": null,
  "ReasonLostComment": null,
  "OrderTypeId": null,
  "OrderType": null,
  "Preliminary": false,
  "CurrencyExchangeTypeId": 0,
  "DeliveryTimeId": null,
  "DeliveryTime": null,
  "DeliveryTimeInDays": null,
  "AccountGroupId": 0,
  "AccountGroup": null,
  "CategoryString": null,
  "DestinationForDeliveryTerm": null,
  "EditedOrderAmountExcludingVat": null,
  "EditedOrderAmountExcludingVatCurrencyId": null,
  "EditedOrderAmountDiscount": null,
  "TypeOfOrderAmountEntered": null,
  "Factoring": false,
  "BusinessOpportunityId": null,
  "BusinessOpportunity": null,
  "RelatedQuotesId": null
}
```
