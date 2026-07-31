---
type: API Entity
title: SalesAgreements
description: Represents an agreement.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreement.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreement.html
  title: Monitor API — SalesAgreement
module: Sales
api_class: SalesAgreement
doc_name: SalesAgreements
endpoint: GET /api/v1/Sales/SalesAgreements
guid: 77CAE1A2-BBC1-405D-9C38-9F8F90950BB8
permission: Show agreement
introduced_in: '22.7'
property_count: 64
references_out:
- /entities/Accounting/Account.md
- /entities/Common/Address.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/DeliveryMethod.md
- /entities/Common/DeliveryTerm.md
- /entities/Common/PaymentTerm.md
- /entities/Common/Person.md
- /entities/Common/Project.md
- /entities/Common/VatGroup.md
- /entities/Inventory/ProductRecord.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerAccountGroup.md
- /entities/Sales/SalesAgreementBasis.md
- /entities/Sales/SalesAgreementRow.md
- /entities/Sales/SalesAgreementType.md
referenced_by:
- /entities/Sales/SalesAgreementBasis.md
- /entities/Sales/SalesAgreementRow.md
- /entities/Sales/SalesAgreementRowInflow.md
---

# SalesAgreements

Represents an agreement.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `SalesAgreement`
- **Endpoint:** `GET /api/v1/Sales/SalesAgreements`
- **Required permission:** Show agreement
- **GUID:** `77CAE1A2-BBC1-405D-9C38-9F8F90950BB8`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the agreement. |
| `OrderNumber` | `String` | no |  | unique, max length 15 | The human readable identifier of the agreement. |
| `OrderTypeId` | `Int64` | no | [SalesAgreementTypes](/entities/Sales/SalesAgreementType.md) |  | The business key identifier of the agreements type. |
| `PeriodStart` | `DateTimeOffset` | no |  |  | The start period of the agreement. |
| `PeriodEnd` | `DateTimeOffset?` | yes |  |  | The end period of the agreement. |
| `AgreementDate` | `DateTimeOffset?` | yes |  |  | The date of the agreement. |
| `LastNoticeDate` | `DateTimeOffset?` | yes |  |  | The last notice date of the agreement. |
| `TerminationDate` | `DateTimeOffset?` | yes |  |  | The termination date of the agreement. |
| `ExtensionPeriod` | `Int32?` | yes |  |  | The extension period in months of the agreement. |
| `CustomerAgreementNumber` | `String` | no |  | max length 30 | The customers number of the agreement. |
| `Status` | `Int32` | no |  | enum | The status of the agreement. |
| `ResponsibleId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the person responsible of the agreement. |
| `BusinessContactId` | `Int64` | no | [Customers](/entities/Sales/Customer.md) |  | The business key identifier of the agreements customer. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) |  | The business key identifier of the agreements customer reference. |
| `BusinessContactReferenceName` | `String` | no |  | max length 80 | The customers reference name of the agreement. |
| `OurReferenceId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of our reference on the agreement. |
| `OurReferenceName` | `String` | no |  | max length 80 | Our reference name of the agreement. |
| `Description` | `String` | no |  |  | The translated description of the agreement. |
| `UseForwardRate` | `Boolean` | no |  |  | Indicates if the agreement use forward rate. |
| `ExchangeRate` | `Decimal` | no |  |  | The exchange rate of the agreement. |
| `InternalCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the agreements internal comment. |
| `InternalComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The internal comment of the agreement. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the agreements external comment. |
| `ExternalComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The external comment of the agreement. |
| `CurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the agreements currency. |
| `TermLocation` | `String` | no |  | max length 80 | The term location of the agreement. |
| `InvoicingMethod` | `Int32` | no |  | enum | The invoicing method of the agreement. |
| `VatGroupId` | `Int64` | no | [VatGroups](/entities/Common/VatGroup.md) |  | The business key identifier of the agreements VAT group. |
| `IsAccrual` | `Boolean` | no |  |  | Indicates if the agreement is accrual. |
| `DefaultOrderPrintoutVia` | `Int32` | no |  | enum | The default printout method of the agreement. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](/entities/Common/Address.md) |  | The business key identifier of the agreements mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](/entities/Common/Address.md) | expandable | The mailing address of the agreement. |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](/entities/Common/Address.md) |  | The business key identifier of the agreements delivery address. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](/entities/Common/Address.md) | expandable | The delivery address of the agreement. |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](/entities/Sales/CustomerAccountGroup.md) |  | The business key identifier of the agreements customers account group. |
| `InvoiceBusinessContactId` | `Int64` | no | [Customers](/entities/Sales/Customer.md) |  | The business key identifier of the agreements invoice customer. |
| `ProjectId` | `Int64?` | yes | [Projects](/entities/Common/Project.md) |  | The business key identifier of the agreements project. |
| `AftermarketProductRecordId` | `Int64?` | yes | [ProductRecords](/entities/Inventory/ProductRecord.md) |  | The business key identifier of the agreements aftermarket product record. |
| `SellerId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the agreements seller. |
| `Priority` | `Int32` | no |  |  | The priority of the agreement. |
| `AccrualAccountId` | `Int64?` | yes | [Accounts](/entities/Accounting/Account.md) |  | The business key identifier of the agreements accrual account. |
| `InvoiceCurrentMonth` | `Boolean` | no |  |  | Indicates if the agreement should be invoiced the current month. |
| `InvoicingInterval` | `Int32` | no |  | enum | The invoicing interval of the agreement. |
| `ComprehensiveInvoiceChoice` | `Int32` | no |  | enum | The comprehensive invoice choice of the agreement. |
| `ReleaseAgreementBasisAutomatically` | `Boolean` | no |  |  | Indicates if agreement basis should be released automatically. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](/entities/Common/PaymentTerm.md) |  | The business key identifier of the agreements payment term. |
| `PaymentTermDescription` | `String` | no |  | max length 35 | The payment term description of the agreement. |
| `DestinationForDeliveryTerm` | `String` | no |  | max length 80 | The destination for delivery term of the agreement. |
| `GracePeriodInDays` | `Int32?` | yes |  |  | The grace period in days of the agreement. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](/entities/Common/DeliveryMethod.md) |  | The business key identifier of the agreements delivery method. |
| `DeliveryMethodDescription` | `String` | no |  | max length 35 | The delivery method description of the agreement. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](/entities/Common/DeliveryTerm.md) |  | The business key identifier of the delivery term of the agreement. |
| `DeliveryTermDescription` | `String` | no |  | max length 35 | The delivery term description of the agreement. |
| `PriceDefinition` | `Int32` | no |  | enum | The price definition of the agreement. |
| `UpdateStatusAutomatically` | `Boolean` | no |  |  | Indicates if agreement status should be updated automatically. |
| `Version` | `Int32` | no |  |  | The version of the agreement. |
| `NoticePeriod` | `Int32` | no |  |  | The notice period of the agreement. |
| `PlannedInvoiceDateOffset` | `Int32` | no |  |  | The planned invoice date offset in days of the agreement. |
| `NumberOfYearsToCreateBasisFor` | `Int32` | no |  |  | The number of years to create agreement basis for in advance. |
| `CreateAgreementBasis` | `Boolean` | no |  |  | Indicates if agreement basis should be created. |
| `Rows` | `SalesAgreementRows[]` | no | [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) | expandable, collection | The rows of the agreement. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the agreement. |
| `Factoring` | `Boolean` | no |  | since 25.7 | Specifies if factoring is activated for the agreement. |
| `Bases` | `SalesAgreementBases[]` | no | [SalesAgreementBases](/entities/Sales/SalesAgreementBasis.md) | expandable, collection, since 26.4 | The agreement bases of the agreement. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Negotiation` | 1 |
| `SignedValid` | 2 |
| `Active` | 3 |
| `Terminated` | 4 |
| `Closed` | 6 |
| `Historic` | 9 |

### InvoicingMethod

| Name | Value |
| --- | ---: |
| `InAdvance` | 1 |
| `InArrears` | 2 |

### DefaultOrderPrintoutVia

| Name | Value |
| --- | ---: |
| `Printer` | 0 |
| `Email` | 1 |
| `Edi` | 2 |
| `None` | 9 |

### InvoicingInterval

| Name | Value |
| --- | ---: |
| `Monthly` | 1 |
| `EveryOtherMonth` | 2 |
| `Quarterly` | 3 |
| `FourMonthly` | 4 |
| `SemiAnnually` | 5 |
| `Annually` | 6 |

### ComprehensiveInvoiceChoice

| Name | Value |
| --- | ---: |
| `No` | 1 |
| `PerCustomer` | 2 |

### PriceDefinition

| Name | Value |
| --- | ---: |
| `AccordingToInvoicingInterval` | 0 |
| `Day` | 1 |
| `Week` | 2 |
| `Month` | 3 |
| `TwoMonths` | 4 |
| `Quarter` | 5 |
| `FourMonths` | 6 |
| `SixMonths` | 7 |
| `Annual` | 8 |

### LifeCycleState

| Name | Value |
| --- | ---: |
| `Transient` | 1 |
| `Persistent` | 10 |
| `History` | 20 |
| `RemovableCandidate` | 99 |


## Referenced by

**Sales**

- [SalesAgreementBases](/entities/Sales/SalesAgreementBasis.md) — `SalesAgreementId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `SalesAgreementId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `ParentOrderId` (FK)


## Example

```json
{
  "Id": 0,
  "OrderNumber": null,
  "OrderTypeId": 0,
  "PeriodStart": "0001-01-01T00:00:00+00:00",
  "PeriodEnd": null,
  "AgreementDate": null,
  "LastNoticeDate": null,
  "TerminationDate": null,
  "ExtensionPeriod": null,
  "CustomerAgreementNumber": null,
  "Status": 0,
  "ResponsibleId": null,
  "BusinessContactId": 0,
  "BusinessContactReferenceId": null,
  "BusinessContactReferenceName": null,
  "OurReferenceId": null,
  "OurReferenceName": null,
  "Description": null,
  "UseForwardRate": false,
  "ExchangeRate": 0.0,
  "InternalCommentId": null,
  "InternalComment": null,
  "ExternalCommentId": null,
  "ExternalComment": null,
  "CurrencyId": 0,
  "TermLocation": null,
  "InvoicingMethod": 0,
  "VatGroupId": 0,
  "IsAccrual": false,
  "DefaultOrderPrintoutVia": 0,
  "MailingAddressId": null,
  "MailingAddress": null,
  "DeliveryAddressId": null,
  "DeliveryAddress": null,
  "CustomerAccountGroupId": null,
  "InvoiceBusinessContactId": 0,
  "ProjectId": null,
  "AftermarketProductRecordId": null,
  "SellerId": null,
  "Priority": 0,
  "AccrualAccountId": null,
  "InvoiceCurrentMonth": false,
  "InvoicingInterval": 0,
  "ComprehensiveInvoiceChoice": 0,
  "ReleaseAgreementBasisAutomatically": false,
  "PaymentTermId": null,
  "PaymentTermDescription": null,
  "DestinationForDeliveryTerm": null,
  "GracePeriodInDays": null,
  "DeliveryMethodId": null,
  "DeliveryMethodDescription": null,
  "DeliveryTermId": null,
  "DeliveryTermDescription": null,
  "PriceDefinition": 0,
  "UpdateStatusAutomatically": false,
  "Version": 0,
  "NoticePeriod": 0,
  "PlannedInvoiceDateOffset": 0,
  "NumberOfYearsToCreateBasisFor": 0,
  "CreateAgreementBasis": false,
  "Rows": null,
  "LifeCycleState": 0,
  "Factoring": false,
  "Bases": null
}
```
