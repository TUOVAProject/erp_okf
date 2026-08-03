---
type: API Entity
title: Suppliers
description: Represents a supplier.
resource: https://api.monitor.se/api/Monitor.API.Purchase.Supplier.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.Supplier.html
  title: Monitor API — Supplier
module: Purchase
api_class: Supplier
doc_name: Suppliers
endpoint: GET /api/v1/Purchase/Suppliers
guid: 42A7D204-268F-4AC0-9912-8341107A9A2D
permission: Show supplier
introduced_in: '2.18'
property_count: 116
references_out:
- /entities/Accounting/CodingEntry.md
- /entities/Common/Address.md
- /entities/Common/ApplicationUser.md
- /entities/Common/BusinessContactBankAccount.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/CommunicationAddress.md
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/DeliveryAddress.md
- /entities/Common/DiscountCategory.md
- /entities/Common/ExtraField.md
- /entities/Common/LanguageCode.md
- /entities/Common/PaymentMethod.md
- /entities/Common/PaymentTerm.md
- /entities/Common/Person.md
- /entities/Inventory/CaseEntry.md
- /entities/Purchase/OtherSupplierNumber.md
- /entities/Purchase/PackingTerm.md
- /entities/Purchase/ResponseTime.md
- /entities/Purchase/Supplier.md
- /entities/Purchase/SupplierAccount.md
- /entities/Purchase/SupplierAccountGroup.md
- /entities/Purchase/SupplierDistrict.md
- /entities/Purchase/SupplierPartLink.md
- /entities/Purchase/SupplierStatus.md
- /entities/Purchase/SupplierType.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/FixedAsset.md
- /entities/Accounting/OutgoingPayment.md
- /entities/Common/DeliveryMethod.md
- /entities/Common/TransferProfile.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/PartPurchaseControlDataRow.md
- /entities/Inventory/PriceChangeLog.md
- /entities/Purchase/BlanketOrderPurchase.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/OtherSupplierNumber.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderAdvice.md
- /entities/Purchase/Supplier.md
- /entities/Purchase/SupplierAccount.md
- /entities/Purchase/SupplierPartLink.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/Shipment.md
- /entities/Sales/ShipmentInformationSource.md
- /entities/Sales/ShippingService.md
- /entities/Sales/ShippingTemplate.md
---

# Suppliers

Represents a supplier.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `Supplier`
- **Endpoint:** `GET /api/v1/Purchase/Suppliers`
- **Required permission:** Show supplier
- **GUID:** `42A7D204-268F-4AC0-9912-8341107A9A2D`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the supplier. |
| `SupplierCode` | `String` | no |  |  | The human readable code of the supplier. |
| `Name` | `String` | no |  |  | The name of the supplier. |
| `AlternativeName` | `String` | no |  | max length 100, since 2.28 | The alternative name of the supplier. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) | since 2.28 | The business key identifier of the supplier mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable, since 2.28 | The mailing address of then supplier. |
| `CorporationIdentificationNumber` | `String` | no |  |  | The corporation identification number of the supplier. |
| `VatNumber` | `String` | no |  |  | The VAT number of the supplier. |
| `ServiceTaxNumber` | `String` | no |  | max length 30, since 2.28 | The service tax number of the supplier. |
| `PersonalNumber` | `String` | no |  | since 23.9 | The name of private person if is private supplier enabled. |
| `PackingTermId` | `Int64?` | yes | [PackingTerms](PackingTerm.md) |  | The business key identifier of the supplier packing term. |
| `PackingTerm` | `PackingTerms` | no | [PackingTerms](PackingTerm.md) | expandable, since 2.28 | The packing term of the supplier. |
| `GracePeriodOrderConfirmation` | `Int32?` | yes |  | since 2.28 | The grace period order confirmation of the supplier. |
| `GracePeriodDelivery` | `Int32?` | yes |  | since 2.28 | The grace period delivery of the supplier. |
| `InvoiceSupplierId` | `Int64` | no | [Suppliers](Supplier.md) |  | The business key identifier of the supplier invoice supplier. |
| `AuthorizedSignerPersonId` | `Int64?` | yes | [Persons](../Common/Person.md) | since 2.28 | The business key identifier of the supplier authorized signer person. |
| `AuthorizedSignerPerson` | `Persons` | no | [Persons](../Common/Person.md) | expandable, since 2.28 | The authorized signer person of the supplier. |
| `BankIdNumber` | `String` | no |  |  | The bank id number of the supplier. |
| `CentralBankCode` | `String` | no |  | max length 3, since 2.28 | The central bank code of the supplier. |
| `ResponseTimeId` | `Int64?` | yes | [ResponseTimes](ResponseTime.md) | since 2.28 | The business key identifier of the supplier response time. |
| `ResponseTime` | `ResponseTimes` | no | [ResponseTimes](ResponseTime.md) | expandable, since 2.28 | The response time of the supplier. |
| `InvoiceBasisException` | `Boolean` | no |  | since 2.28 | The invoice basis exception of the supplier. |
| `Role` | `Int32` | no |  | bitmask, enum, since 2.28 | The role of the supplier. |
| `AttachDatafileWithOrder` | `Boolean` | no |  | since 2.28 | Specifies if the supplier have attached datafile with order. |
| `AttachDatafileWithDeliverySchedule` | `Boolean` | no |  | since 22.2 | Specifies if the supplier have attached datafile with delivery schedule. |
| `AttachDatafileWithCase` | `Boolean` | no |  | since 22.2 | Specifies if the supplier have attached datafile with case. |
| `ReceivingInspectionType` | `Int32` | no |  | enum, since 2.28 | The receiving inspection type of the supplier. |
| `ArrivalReportingInstructionId` | `Int64?` | yes | [Comments](../Common/Comment.md) | since 2.28 | The business key identifier of the supplier arrival reporting instruction. |
| `ArrivalReportingInstruction` | `Comments` | no | [Comments](../Common/Comment.md) | expandable, since 2.28 | The arrival reporting instruction of the supplier. |
| `UseOCRNumber` | `Boolean` | no |  | since 2.28 | Specifies if the supplier use OCR number. |
| `UseReferenceNumber` | `Boolean` | no |  | since 2.28 | Specifies if the supplier use reference number. |
| `FixedReferenceNumber` | `String` | no |  | max length 20, since 2.28 | The fixed reference number of the supplier. |
| `EInvoiceId` | `String` | no |  | max length 30, since 2.28 | The e-invoice id of the supplier. |
| `PurchaseManagerId` | `Int64?` | yes | [Persons](../Common/Person.md) | since 2.28 | The business key identifier of the supplier purchase manager. |
| `PurchaseManager` | `Persons` | no | [Persons](../Common/Person.md) | expandable, since 2.28 | The purchase manager of the supplier. |
| `ShippingAgentCode` | `String` | no |  | max length 15, since 2.28 | The shipping agent code of the supplier. |
| `DefaultBusinessContactBankAccountId` | `Int64?` | yes | [BusinessContactBankAccounts](../Common/BusinessContactBankAccount.md) | since 2.28 | The business key identifier of the supplier default business contact bank account. |
| `DefaultBusinessContactBankAccount` | `BusinessContactBankAccounts` | no | [BusinessContactBankAccounts](../Common/BusinessContactBankAccount.md) | expandable, since 2.28 | The default business contact bank account of the supplier. |
| `IsCasualSupplier` | `Boolean` | no |  | since 2.28 | Specifies if the supplier is a casual supplier. |
| `ShippingAgentType` | `Int32?` | yes |  | enum, since 2.28 | The shipping agent type of the supplier. |
| `BookTransport` | `Boolean` | no |  | since 2.28 | The book transport of the supplier. |
| `ReturnLabel` | `Boolean` | no |  | since 2.28 | The return label of the supplier. |
| `ShipmentPrintSetting` | `Int32` | no |  | enum, since 2.28 | The shipment print setting of the supplier. |
| `Url` | `String` | no |  |  | The URL of the supplier. |
| `Discount` | `Decimal?` | yes |  |  | The discount of the supplier. |
| `StatusId` | `Int64` | no | [SupplierStatuses](SupplierStatus.md) |  | The business key identifier of the supplier status. |
| `Status` | `SupplierStatuses` | no | [SupplierStatuses](SupplierStatus.md) | expandable, since 2.28 | The status of the supplier. |
| `TypeId` | `Int64?` | yes | [SupplierTypes](SupplierType.md) |  | The business key identifier of the supplier type. |
| `Type` | `SupplierTypes` | no | [SupplierTypes](SupplierType.md) | expandable, since 2.28 | The type of the supplier. |
| `DistrictId` | `Int64?` | yes | [SupplierDistricts](SupplierDistrict.md) |  | The business key identifier of the supplier district. |
| `District` | `SupplierDistricts` | no | [SupplierDistricts](SupplierDistrict.md) | expandable, since 2.28 | The district of the supplier. |
| `PayViaId` | `Int64?` | yes | [Suppliers](Supplier.md) |  | The business key identifier of the supplier that the current supplier payments should go through. |
| `DateForTransitionToActualContact` | `DateTimeOffset?` | yes |  | since 2.28 | The date for transition to actual contact of the supplier. Changed from DateTimeOffset to DateTimeOffset? in 26.3 |
| `PaymentTermId` | `Int64` | no | [PaymentTerms](../Common/PaymentTerm.md) | since 2.28 | The business key identifier of the supplier payment term |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](../Common/PaymentTerm.md) | since 2.28 | The payment term of the supplier. |
| `BankGiroNo` | `String` | no |  | max length 15, since 2.28 | The bank giro no of the supplier. |
| `EdiCode` | `String` | no |  | max length 20, **deprecated since 2.32**, since 2.28 | The EDI code of the supplier. _(Replaced by OtherSupplierNumbers)_ |
| `DefaultOrderPrintoutVia` | `Int32` | no |  | enum, since 2.28 | The default order printout via of the supplier. |
| `PlusGiroNo` | `String` | no |  | max length 15, since 2.28 | The plus giro number of the supplier. |
| `OurCodeByYou` | `String` | no |  | max length 50, since 2.28 | The human readable identifier that the the supplier uses to identify the current company. |
| `DiscountCategoryId` | `Int64?` | yes | [DiscountCategories](../Common/DiscountCategory.md) | since 2.28 | The business key identifier of the supplier discount category. |
| `DiscountCategory` | `DiscountCategories` | no | [DiscountCategories](../Common/DiscountCategory.md) | expandable, since 2.28 | The discount category of the supplier. |
| `ToleranceForEarlyDelivery` | `Int64?` | yes |  |  | The tolerance value for early delivery by the supplier. |
| `ToleranceForLateDelivery` | `Int64?` | yes |  |  | The tolerance value for late delivery by the supplier. |
| `Alias` | `String` | no |  | max length 10, since 2.28 | The alias of the supplier. |
| `BlockedContextType` | `Int32` | no |  | bitmask, enum, since 2.28 | The blocked context type of the supplier. |
| `IsInternal` | `Boolean` | no |  | since 2.28 | Specifies if the supplier is internal. |
| `CompanyId` | `Int64` | no |  |  | The business key identifier of the company that the supplier data is active for. |
| `BlockedStatus` | `Int32` | no |  | enum | The block status of the entity. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |  | The date when the entity stops being blocked. |
| `Priority` | `Int32` | no |  |  | The priority of the supplier. |
| `CategoryString` | `String` | no |  |  | The category string of the supplier. |
| `DeliveryInstruction` | `String` | no |  |  | The delivery instruction of the supplier. |
| `PaymentMethodId` | `Int64` | no | [PaymentMethods](../Common/PaymentMethod.md) |  | The business key identifier of the supplier payment method. |
| `LastChange` | `DateTimeOffset?` | yes |  | since 2.26 | Last change on Supplier från EntityChangeLog |
| `PaymentMethod` | `PaymentMethods` | no | [PaymentMethods](../Common/PaymentMethod.md) | expandable | The payment method of the supplier. |
| `LanguageId` | `Int64` | no | [LanguageCodes](../Common/LanguageCode.md) |  | The business key identifier of the supplier language. |
| `Language` | `LanguageCodes` | no | [LanguageCodes](../Common/LanguageCode.md) | expandable | The language of the supplier. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the supplier comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The supplier comment. |
| `CurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the supplier currency. References Currencies . |
| `Currency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The currency of the supplier. |
| `VisitingAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the supplier visiting address. |
| `VisitingAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The visiting address of the supplier. |
| `BlockMessageId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The block message of the supplier. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the application user that blocked the entity. |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](../Common/ApplicationUser.md) | expandable | The application user that blocked the supplier. |
| `DefaultReferenceId` | `Int64?` | yes | [BusinessContactReferences](../Common/BusinessContactReference.md) |  | The business key identifier of the default reference of the supplier. |
| `DefaultReference` | `BusinessContactReferences` | no | [BusinessContactReferences](../Common/BusinessContactReference.md) | expandable | The default reference of the supplier. |
| `DeliveryAddressId` | `Int64` | no | [DeliveryAddresses](../Common/DeliveryAddress.md) | since 2.28 | The business key identifier of the supplier delivery address. |
| `DeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](../Common/DeliveryAddress.md) | expandable | The delivery address of the supplier. |
| `SupplierPartLinks` | `SupplierPartLinks[]` | no | [SupplierPartLinks](SupplierPartLink.md) | expandable, collection | A collection of supplier part links that belong to the supplier. |
| `CaseEntries` | `CaseEntry[]` | no | [CaseEntry](../Inventory/CaseEntry.md) | expandable, collection | A collection of case entries that belong to the supplier. |
| `OtherSupplierNumbers` | `OtherSupplierNumbers[]` | no | [OtherSupplierNumbers](OtherSupplierNumber.md) | expandable, collection, since 2.32 | Available other supplier numbers. Mainly used as EDI identifiers. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](../Common/CommunicationAddress.md) | expandable, collection, since 2.52 | The communication addresses for the supplier. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](../Common/ExtraField.md) | expandable, collection, since 2.54 | A collection of extra field values for the supplier. |
| `PurchaseAccountId` | `Int64?` | yes | [CodingEntries](../Accounting/CodingEntry.md) | since 22.7 | The business key identifier of the coding entry with supplier purchase account. |
| `PurchaseAccount` | `CodingEntries` | no | [CodingEntries](../Accounting/CodingEntry.md) | expandable, since 22.7 | The coding entry with supplier purchase account. |
| `AccrualAccountingReverseAccountId` | `Int64?` | yes | [CodingEntries](../Accounting/CodingEntry.md) | since 22.7 | The business key identifier of the coding entry with supplier offset account for accruals. |
| `AccrualAccountingReverseAccount` | `CodingEntries` | no | [CodingEntries](../Accounting/CodingEntry.md) | expandable, since 22.7 | The coding entry with supplier offset account for accruals. |
| `OutgoingPaymentsAccountId` | `Int64?` | yes | [CodingEntries](../Accounting/CodingEntry.md) | since 22.7 | The business key identifier of the coding entry with supplier account for outgoing payments. |
| `OutgoingPaymentsAccount` | `CodingEntries` | no | [CodingEntries](../Accounting/CodingEntry.md) | expandable, since 22.7 | The coding entry with supplier account for outgoing payments. |
| `SupplierAccounts` | `SupplierAccounts[]` | no | [SupplierAccounts](SupplierAccount.md) | expandable, collection, since 22.7 | The supplier account exceptions. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](../Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the supplier's currency exchange type. |
| `RootId` | `Int64` | no |  | since 23.9 | The business key identifier of the supplier root id. |
| `References` | `BusinessContactReferences[]` | no | [BusinessContactReferences](../Common/BusinessContactReference.md) | expandable, collection, since 23.9 | The business contact references belonging to the supplier. |
| `ReceivingInspecionFromDate` | `DateTimeOffset?` | yes |  | since 23.9 | The receiving inspection from date for supplier. |
| `ReceivingInspecionEndDate` | `DateTimeOffset?` | yes |  | since 23.9 | The receiving inspection end date for supplier. |
| `SupplierAccountGroupId` | `Int64` | no | [SupplierAccountGroups](SupplierAccountGroup.md) | **deprecated since 24.3**, since 23.9 | The business key identifier of the supplier account group for supplier. _(Refer to DeliveryAddress)_ |
| `IsPrivateSupplier` | `Boolean` | no |  | since 23.9 | The private person setting of supplier. |
| `EORINumber` | `String` | no |  | since 23.9 | The eori of supplier. mainly used for validation to retrieve business address. |
| `DeliveryAddresses` | `DeliveryAddresses[]` | no | [DeliveryAddresses](../Common/DeliveryAddress.md) | expandable, collection, since 24.4 | All available delivery addresses of the supplier. |
| `AllBusinessContactBankAccountOfSupplier` | `BusinessContactBankAccounts[]` | no | [BusinessContactBankAccounts](../Common/BusinessContactBankAccount.md) | expandable, collection, since 25.3 | All available supplier's business contact bank accounts. |
| `TinNumber` | `String` | no |  | max length 13, since 25.9 | The supplier’s income tax reference number |

## Enumerations

### Role (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `MaterialSupplier` | 1 |
| `SubContractor` | 2 |
| `ShippingAgent` | 4 |
| `Miscelaneous` | 8 |
| `CustomsSupplier` | 16 |

### ReceivingInspectionType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Always` | 1 |
| `VariableInspection` | 2 |

### ShippingAgentType

| Name | Value |
| --- | ---: |
| `Other` | 0 |
| `DHL` | 1 |
| `Schenker` | 2 |
| `PostNord` | 3 |
| `DSV` | 4 |

### ShipmentPrintSetting

| Name | Value |
| --- | ---: |
| `WaybillAndParcel` | 0 |
| `Waybill` | 1 |
| `Parcel` | 2 |

### DefaultOrderPrintoutVia

| Name | Value |
| --- | ---: |
| `Printer` | 0 |
| `Email` | 1 |
| `Edi` | 2 |
| `None` | 9 |

### BlockedContextType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Register` | 1 |
| `Report` | 2 |
| `RegisterSupplierInvoice` | 4 |
| `Payments` | 8 |

### BlockedStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Message` | 1 |
| `Blocked` | 2 |


## Referenced by

**Accounting**

- [AccountsPayables](../Accounting/AccountsPayable.md) — `BusinessContactId` (FK)
- [FixedAssets](../Accounting/FixedAsset.md) — `SupplierId` (FK)
- [OutgoingPayments](../Accounting/OutgoingPayment.md) — `SupplierId` (FK)

**Common**

- [DeliveryMethods](../Common/DeliveryMethod.md) — `SupplierId` (FK)
- [TransferProfiles](../Common/TransferProfile.md) — `SupplierId` (FK)

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `ReasonSupplierId` (FK)
- [CaseEntry](../Inventory/CaseEntry.md) — `SupplierId` (FK)
- [PartPurchaseControlDataRows](../Inventory/PartPurchaseControlDataRow.md) — `SupplierId` (FK)
- [PriceChangeLogs](../Inventory/PriceChangeLog.md) — `SupplierId` (FK)

**Purchase**

- [BlanketOrderPurchases](BlanketOrderPurchase.md) — `BusinessContactId` (FK)
- [Inquiries](Inquiry.md) — `SupplierId` (FK)
- [OtherSupplierNumbers](OtherSupplierNumber.md) — `SupplierId` (FK)
- [PurchaseOrderAdvices](PurchaseOrderAdvice.md) — `SupplierId` (FK)
- [PurchaseOrders](PurchaseOrder.md) — `ActiveDeliveryAddressSupplierId` (FK)
- [PurchaseOrders](PurchaseOrder.md) — `AgentSupplierId` (FK)
- [PurchaseOrders](PurchaseOrder.md) — `BusinessContactId` (FK)
- [PurchaseOrders](PurchaseOrder.md) — `InvoiceBusinessContactId` (FK)
- [SupplierAccounts](SupplierAccount.md) — `SupplierId` (FK)
- [SupplierPartLinks](SupplierPartLink.md) — `SupplierId` (FK)
- [Suppliers](Supplier.md) — `InvoiceSupplierId` (FK)
- [Suppliers](Supplier.md) — `PayViaId` (FK)

**Sales**

- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `ActiveDeliveryAddressSupplierId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `ActiveDeliveryAddressSupplierId` (FK)
- [ShipmentInformationSources](../Sales/ShipmentInformationSource.md) — `SupplierId` (FK)
- [Shipments](../Sales/Shipment.md) — `ActiveDeliveryAddressSupplierId` (FK)
- [Shipments](../Sales/Shipment.md) — `ShippingAgentId` (FK)
- [ShippingServices](../Sales/ShippingService.md) — `SupplierId` (FK)
- [ShippingTemplates](../Sales/ShippingTemplate.md) — `SupplierId` (FK)


## Example

```json
{
  "Id": 0,
  "SupplierCode": null,
  "Name": null,
  "AlternativeName": null,
  "MailingAddressId": null,
  "MailingAddress": null,
  "CorporationIdentificationNumber": null,
  "VatNumber": null,
  "ServiceTaxNumber": null,
  "PersonalNumber": null,
  "PackingTermId": null,
  "PackingTerm": null,
  "GracePeriodOrderConfirmation": null,
  "GracePeriodDelivery": null,
  "InvoiceSupplierId": 0,
  "AuthorizedSignerPersonId": null,
  "AuthorizedSignerPerson": null,
  "BankIdNumber": null,
  "CentralBankCode": null,
  "ResponseTimeId": null,
  "ResponseTime": null,
  "InvoiceBasisException": false,
  "Role": 0,
  "AttachDatafileWithOrder": false,
  "AttachDatafileWithDeliverySchedule": false,
  "AttachDatafileWithCase": false,
  "ReceivingInspectionType": 0,
  "ArrivalReportingInstructionId": null,
  "ArrivalReportingInstruction": null,
  "UseOCRNumber": false,
  "UseReferenceNumber": false,
  "FixedReferenceNumber": null,
  "EInvoiceId": null,
  "PurchaseManagerId": null,
  "PurchaseManager": null,
  "ShippingAgentCode": null,
  "DefaultBusinessContactBankAccountId": null,
  "DefaultBusinessContactBankAccount": null,
  "IsCasualSupplier": false,
  "ShippingAgentType": null,
  "BookTransport": false,
  "ReturnLabel": false,
  "ShipmentPrintSetting": 0,
  "Url": null,
  "Discount": null,
  "StatusId": 0,
  "Status": null,
  "TypeId": null,
  "Type": null,
  "DistrictId": null,
  "District": null,
  "PayViaId": null,
  "DateForTransitionToActualContact": null,
  "PaymentTermId": 0,
  "PaymentTerm": null,
  "BankGiroNo": null,
  "EdiCode": null,
  "DefaultOrderPrintoutVia": 0,
  "PlusGiroNo": null,
  "OurCodeByYou": null,
  "DiscountCategoryId": null,
  "DiscountCategory": null,
  "ToleranceForEarlyDelivery": null,
  "ToleranceForLateDelivery": null,
  "Alias": null,
  "BlockedContextType": 0,
  "IsInternal": false,
  "CompanyId": 0,
  "BlockedStatus": 0,
  "BlockedFromDate": null,
  "BlockedToDate": null,
  "Priority": 0,
  "CategoryString": null,
  "DeliveryInstruction": null,
  "PaymentMethodId": 0,
  "LastChange": null,
  "PaymentMethod": null,
  "LanguageId": 0,
  "Language": null,
  "CommentId": null,
  "Comment": null,
  "CurrencyId": 0,
  "Currency": null,
  "VisitingAddressId": null,
  "VisitingAddress": null,
  "BlockMessageId": null,
  "BlockMessage": null,
  "BlockedById": null,
  "BlockedBy": null,
  "DefaultReferenceId": null,
  "DefaultReference": null,
  "DeliveryAddressId": 0,
  "DeliveryAddress": null,
  "SupplierPartLinks": null,
  "CaseEntries": null,
  "OtherSupplierNumbers": null,
  "CommunicationAddresses": null,
  "ExtraFields": null,
  "PurchaseAccountId": null,
  "PurchaseAccount": null,
  "AccrualAccountingReverseAccountId": null,
  "AccrualAccountingReverseAccount": null,
  "OutgoingPaymentsAccountId": null,
  "OutgoingPaymentsAccount": null,
  "SupplierAccounts": null,
  "CurrencyExchangeTypeId": 0,
  "RootId": 0,
  "References": null,
  "ReceivingInspecionFromDate": null,
  "ReceivingInspecionEndDate": null,
  "SupplierAccountGroupId": 0,
  "IsPrivateSupplier": false,
  "EORINumber": null,
  "DeliveryAddresses": null,
  "AllBusinessContactBankAccountOfSupplier": null,
  "TinNumber": null
}
```
