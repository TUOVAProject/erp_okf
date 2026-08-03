---
type: API Entity
title: Customers
description: Represents a customer.
resource: https://api.monitor.se/api/Monitor.API.Sales.Customer.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.Customer.html
  title: Monitor API — Customer
module: Sales
api_class: Customer
doc_name: Customers
endpoint: GET /api/v1/Sales/Customers
guid: 9A9B110E-D5B5-410D-AFEE-C397747EBA77
permission: Show customer
introduced_in: '2.18'
property_count: 147
references_out:
- /entities/Common/Address.md
- /entities/Common/ApplicationUser.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/CommunicationAddress.md
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/DeliveryAddress.md
- /entities/Common/DiscountCategory.md
- /entities/Common/ExtraField.md
- /entities/Common/LanguageCode.md
- /entities/Common/PaymentPlanTemplate.md
- /entities/Common/PaymentTerm.md
- /entities/Common/Person.md
- /entities/Common/PriceList.md
- /entities/Common/Probability.md
- /entities/Common/Reseller.md
- /entities/Common/VatRate.md
- /entities/Inventory/CaseEntry.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerAccountGroup.md
- /entities/Sales/CustomerDistrict.md
- /entities/Sales/CustomerEmployeeSpan.md
- /entities/Sales/CustomerPartLink.md
- /entities/Sales/CustomerStatus.md
- /entities/Sales/CustomerType.md
- /entities/Sales/OtherCustomerNumber.md
- /entities/Sales/ValidityTime.md
referenced_by:
- /entities/Accounting/AccountsReceivable.md
- /entities/Accounting/FixedAssetSale.md
- /entities/Common/EdiBehavior.md
- /entities/Common/Project.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/PriceChangeLog.md
- /entities/Inventory/ProductRecord.md
- /entities/Inventory/SalesForecast.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Sales/BlanketOrderSales.md
- /entities/Sales/BusinessOpportunity.md
- /entities/Sales/BusinessOpportunityActivity.md
- /entities/Sales/BusinessOpportunityReference.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerCountryDocumentSettings.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/CustomerPartLink.md
- /entities/Sales/CustomerRelationshipManagementActivity.md
- /entities/Sales/InvoiceLog.md
- /entities/Sales/OtherCustomerNumber.md
- /entities/Sales/Quote.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/Shipment.md
- /entities/Sales/ShipmentInformationSource.md
---

# Customers

Represents a customer.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `Customer`
- **Endpoint:** `GET /api/v1/Sales/Customers`
- **Required permission:** Show customer
- **GUID:** `9A9B110E-D5B5-410D-AFEE-C397747EBA77`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer. |
| `Name` | `String` | no |  | max length 100 | The name of the customer. |
| `Code` | `String` | no |  | unique, max length 10 | The human readable identifier of the customer. |
| `AlternativeName` | `String` | no |  | max length 100 | The alternative name of the customer. |
| `CorporationIdentificationNumber` | `String` | no |  | max length 30 | The corporation identification number of the customer. |
| `PersonalNumber` | `String` | no |  | max length 13 | The personal number of the customer. |
| `IsPrivateCustomer` | `Boolean` | no |  |  | Specifies if the customer is a private person. |
| `VatNumber` | `String` | no |  | max length 30 | The VAT number of the customer. |
| `DeliveryAddresses` | `DeliveryAddresses[]` | no | [DeliveryAddresses](../Common/DeliveryAddress.md) | expandable, collection | The delivery addresses of the customer. |
| `ActiveDeliveryAddressId` | `Int64` | no | [DeliveryAddresses](../Common/DeliveryAddress.md) |  | The business key identifier of the customer's active delivery address. |
| `ActiveDeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](../Common/DeliveryAddress.md) | expandable | The active delivery address of the customer. |
| `References` | `BusinessContactReferences[]` | no | [BusinessContactReferences](../Common/BusinessContactReference.md) | expandable, collection | The business contact references belonging to the customer. |
| `DefaultReferenceId` | `Int64?` | yes | [BusinessContactReferences](../Common/BusinessContactReference.md) |  | The business key identifier of the customer's default business contact reference. |
| `DefaultReference` | `BusinessContactReferences` | no | [BusinessContactReferences](../Common/BusinessContactReference.md) | expandable | The default reference of the customer. |
| `Alias` | `String` | no |  | max length 10 | The alias code of the customer. |
| `AlloyCost` | `Int32` | no |  |  | The alloy cost associated with the customer. |
| `ApplyBankCharge` | `Boolean` | no |  |  | Specifies if bank charge should be applied for the customer. |
| `ApplyInvoicingCharge` | `Boolean` | no |  |  | Specifies if invoicing charge should be applied for the customer. |
| `ApplyReminderCharge` | `Boolean` | no |  |  | Specifies if reminder charge should be applied for the customer. |
| `AccountManagerId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the customer's account manager. |
| `AccountManager` | `Persons` | no | [Persons](../Common/Person.md) | expandable | The account manager of the customer. |
| `ActiveDeliveryAddressAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](CustomerAccountGroup.md) | since 2.28 | The business key identifier of the customer's active delivery address account group. |
| `ActiveDeliveryAddressAccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](CustomerAccountGroup.md) | expandable, since 2.28 | The active delivery address account group of the customer. |
| `ActualCustomerProbabilityId` | `Int64?` | yes | [Probabilities](../Common/Probability.md) |  | The business key identifier of the customer's actualization probability. |
| `ActualCustomerProbability` | `Probabilities` | no | [Probabilities](../Common/Probability.md) | expandable | The actualization probability of the customer. |
| `AttachDatafileWithOrder` | `Boolean` | no |  |  | Specifies if data file should be attached with orders for the customer. |
| `AttachDatafileWithInvoice` | `Boolean` | no |  |  | Specifies if data file should be attached with invoices for the customer. |
| `AttachDatafileWithCase` | `Boolean` | no |  | since 22.2 | Specifies if data file should be attached with cases for the customer. |
| `AttachDatafileWithPart` | `Boolean` | no |  |  | Specifies if data file should be attached with parts for the customer. |
| `AttachDatafileWithDispatchAdvice` | `Boolean` | no |  |  | Specifies if data file should be attached with dispatch advice for the customer. |
| `BankChargeAmount` | `Decimal` | no |  |  | The bank charge amount of the customer. |
| `BankGiroNo` | `String` | no |  | max length 15 | The bank giro number of the customer. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the application user that blocked the entity. |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](../Common/ApplicationUser.md) | expandable | The application user that blocked the customer. |
| `BlockedStatus` | `Int32` | no |  | enum | The block status of the entity. |
| `BlockedContextType` | `Int32` | no |  | bitmask, enum | Specifies in which contexts that the customer is blocked. |
| `BlockMessageId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The block message that applies for the customer. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |  | The date when the entity stops being blocked. |
| `CategoryString` | `String` | no |  | max length 15 | The category string of the customer. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the customer's comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The comment of the customer. |
| `CompanyId` | `Int64` | no |  |  | The business key identifier of the company that the customer belongs to. |
| `ConfigurationPriceListId` | `Int64?` | yes | [PriceLists](../Common/PriceList.md) |  | The business key identifier of the configuration price list that the customer belongs to. |
| `CreditLimit` | `Decimal` | no |  |  | The credit limit of the customer. |
| `CurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the customer's currency. |
| `Currency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable, since 2.28 | The currency of the customer. |
| `DateDisplayFormat` | `Int32` | no |  | enum, since 2.28 | The date display format of the customer. |
| `DecimalSymbol` | `String` | no |  | max length 1, since 2.28 | The decimal symbol of the customer. |
| `DeliveryHorizon` | `Int64?` | yes |  | since 2.28 | The delivery horizon of the customer. |
| `DeliveryNoteNumberWhenDeliveryPlanning` | `Boolean` | no |  | since 2.28 | The delivery note number when delivery planning of the customer. |
| `DistrictId` | `Int64?` | yes | [CustomerDistricts](CustomerDistrict.md) |  | The business key identifier of the district that the customer belongs to. |
| `District` | `CustomerDistricts` | no | [CustomerDistricts](CustomerDistrict.md) | expandable | The district that the customer belongs to. |
| `DateForTransitionToActualContact` | `DateTimeOffset?` | yes |  |  | The date/time when transition to actual contact was made for the customer. Changed from DateTimeOffset to DateTimeOffset? in 26.3 |
| `Discount` | `Decimal?` | yes |  |  | The general discount of the customer. |
| `DiscountCategoryId` | `Int64?` | yes | [DiscountCategories](../Common/DiscountCategory.md) |  | The business key identifier of the discount category that applies for the customer. |
| `DiscountCategory` | `DiscountCategories` | no | [DiscountCategories](../Common/DiscountCategory.md) | expandable | The discount category that applies for the customer. |
| `DefaultOrderPrintoutVia` | `Int32` | no |  | enum | The preferred order printout method of the customer. |
| `PrintProformaInvoiceVia` | `Int32` | no |  | enum | The preferred Proforma printout method of the customer. |
| `PrintPaymentReminderVia` | `Int32` | no |  | enum | The preferred payment reminder printout method of the customer. |
| `DeliveryInstruction` | `String` | no |  | max length 80 | The delivery instruction of the customer. |
| `DefaultInvoiceStatusPending` | `Boolean` | no |  |  | Specifies if invoices should be pending by default for the customer. |
| `EdiCode` | `String` | no |  | max length 80, **deprecated since 2.32** | The EDI code of the customer. _(Replaced by OtherCustomerNumbers)_ |
| `EInvoiceElectronicAddressIdentifier` | `String` | no |  | max length 6, since 2.28 | The e-invoice electronic address identifier of the customer. |
| `EInvoiceId` | `String` | no |  | max length 30, since 2.28 | The e-invoice id of the customer. |
| `EInvoiceOperatorCode` | `String` | no |  | max length 30, since 2.28 | The e-invoice operator code of the customer. |
| `Factoring` | `Boolean` | no |  |  | Specifies if factoring applies for the customer. |
| `GracePeriod` | `TimeSpan?` | yes |  |  | The grace period of the customer. |
| `HideDiscountOnProformaInvoice` | `Boolean` | no |  | **deprecated since 26.3**, since 2.28 | Specifies if the customer hides discount on proforma invoices. _(Replaced by CustomerCountryDocumentSettings)_ |
| `IncludeInDeliveryAnalysis` | `Boolean?` | yes |  | since 2.28 | Specifies if the customer is included in delivery analysis. |
| `InvoiceAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the customer's invoice address. If there is no value here use MailingAddressId. |
| `InvoiceAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The invoice address of the customer. If there is no value here use MailingAddress. |
| `InterestType` | `Int32` | no |  | enum | Specifies the interest type of the customer. |
| `IsCasualCustomer` | `Boolean` | no |  |  | Specifies if the customer is a stray customer. |
| `InterestInvoiceDays` | `Int32?` | yes |  |  | Specifies the interest invoice days for the customer. |
| `InsuranceCost` | `Decimal` | no |  |  | The insurance cost specified for the customer. |
| `InvoiceCustomerId` | `Int64?` | yes | [Customers](Customer.md) |  | The business key identifier of the invoice customer of the customer. |
| `InvoicePrintoutMethod` | `Int32` | no |  | enum | The customer's preferred printout method for invoices. |
| `InvoicePrintoutOccasion` | `Int32` | no |  | enum | Specifies when invoices should be printed for the customer. |
| `IsInternal` | `Boolean` | no |  | since 2.28 | Specifies if the customer is internal. |
| `LanguageId` | `Int64` | no | [LanguageCodes](../Common/LanguageCode.md) |  | The business key identifier of the customer's preferred language. |
| `Language` | `LanguageCodes` | no | [LanguageCodes](../Common/LanguageCode.md) | since 2.28 | The language of the customer. |
| `LatePaymentFee` | `Decimal?` | yes |  |  | The late payment fee of the customer. |
| `MailingAddressId` | `Int64` | no | [Addresses](../Common/Address.md) |  | The business key identifier of the customer's mailing address. If InvoiceAddressId does not have a value this is also used as invoice adress. |
| `MailingAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The mailing address of the customer. If InvoiceAddressId does not have a value this is also used as invoice adress. |
| `NumberOfInvoiceCopies` | `Int32?` | yes |  |  | The number of invoice copies that should be produced for the customer. |
| `OurCodeByYou` | `String` | no |  | max length 50 | The supplier code assigned to us by the customer. |
| `PalletRegistrationNo` | `String` | no |  | max length 35 | The customer's pallet registration number. |
| `PartialDeliveryType` | `Int32` | no |  | enum, since 2.28 | The partial delivery type of the customer. |
| `PaymentPlanTemplateId` | `Int64?` | yes | [PaymentPlanTemplates](../Common/PaymentPlanTemplate.md) | since 2.28 | The business key identifier of the customer's payment plan template. |
| `PaymentPlanTemplate` | `PaymentPlanTemplates` | no | [PaymentPlanTemplates](../Common/PaymentPlanTemplate.md) | expandable, since 2.28 | The payment plan template of the customer. |
| `PaymentTermId` | `Int64` | no | [PaymentTerms](../Common/PaymentTerm.md) |  | The business key identifier of the customer's payment term. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](../Common/PaymentTerm.md) | expandable | The payment term of the customer. |
| `PlusGiroNo` | `String` | no |  | max length 15 | The PlusGiro number of the customer. |
| `PriceListId` | `Int64` | no | [PriceLists](../Common/PriceList.md) |  | The business key identifier of the customer's price list. |
| `Priority` | `Int32` | no |  |  | The priority of the customer. |
| `PickingListCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the customer's picking list comment. |
| `PickingListComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The picking list comment of the customer. |
| `ProformaInvoicePrintoutOccasion` | `Int32` | no |  | enum | Specifies when proforma invoices should be printed for the customer. |
| `ResellerId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the customer's reseller. |
| `Reseller` | `Resellers` | no | [Resellers](../Common/Reseller.md) | expandable | The reseller of the customer. |
| `RoundOff` | `Boolean` | no |  |  | Specifies if round off applies for the customer. |
| `SellerId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the customer's seller. |
| `Seller` | `Persons` | no | [Persons](../Common/Person.md) | expandable | The seller of the customer. |
| `ServiceAgreementId` | `Int64?` | yes |  |  | The business key identifier of the customer's service agreement. |
| `ServiceTaxNumber` | `String` | no |  | max length 30, since 2.28 | The service tax number of the customer. |
| `ShowPartStatisticalGoodsCodeAndCountryOfOriginInForms` | `Int32` | no |  | bitmask, enum, **deprecated since 24.3** | New properties available: ShowPartStatisticalGoodsCodeInForms and ShowCountryOfOriginInForms. Try to use new properties instead. _(Replaced by ShowPartStatisticalGoodsCodeInForms and ShowCountryOfOriginInForms)_ |
| `ShowPartStatisticalGoodsCodeInForms` | `Int32` | no |  | bitmask, enum, **deprecated since 26.3**, since 24.3 | Specifies which documents should display statistical goods codes for the customer. _(Replaced by CustomerCountryDocumentSettings)_ |
| `ShowCountryOfOriginInForms` | `Int32` | no |  | bitmask, enum, **deprecated since 26.3**, since 24.3 | Specifies which documents should show country of origin for the customer. _(Replaced by CustomerCountryDocumentSettings)_ |
| `ShowPartWeightInForms` | `Int32` | no |  | bitmask, enum, **deprecated since 26.3** | Specifies which documents should show part weight for the customer. _(Replaced by CustomerCountryDocumentSettings)_ |
| `StatusId` | `Int64` | no | [CustomerStatuses](CustomerStatus.md) |  | The business key identifier of the customer's status. |
| `Status` | `CustomerStatuses` | no | [CustomerStatuses](CustomerStatus.md) | expandable | The status of the customer. |
| `TimeZone` | `String` | no |  | since 2.29 | The time zone of the customer. Specified as a time zone identifier (e.g. "W. Europe Standard Time"). |
| `TimeZoneOffset` | `Decimal` | no |  | **deprecated since 2.29**, since 2.28 | The time zone offset of the customer. _(Replaced by TimeZone)_ |
| `ToleranceForLateDelivery` | `TimeSpan?` | yes |  |  | The customer's tolerance for late delivery. |
| `ToleranceForEarlyDelivery` | `TimeSpan?` | yes |  |  | The customer's tolerance for early delivery. |
| `TypeId` | `Int64?` | yes | [CustomerTypes](CustomerType.md) |  | The business key identifier of the customer's type. |
| `Type` | `CustomerTypes` | no | [CustomerTypes](CustomerType.md) | expandable | The type of the customer. |
| `Url` | `String` | no |  | max length 255 | The URL of the customer. |
| `UseBundling` | `Boolean?` | yes |  | since 2.28 | Specifies if the customer uses bundling. |
| `UseComprehensiveInvoices` | `Boolean` | no |  | **deprecated since 2.41** | Specifies if comprehensive invoices should be used for the customer. _(Replaced by ComprehensiveInvoiceGroupingMode)_ |
| `ComprehensiveInvoiceGroupingMode` | `Int32` | no |  | enum, since 2.41 | Specifies if comprehensive invoices should be used for the customer and if so, what they should be grouped on. |
| `UseDeliveryNoteCollectionFormReport` | `Boolean` | no |  |  | Specifies if comprehensive delivery notes should be used for the customer. |
| `UseEInvoicing` | `Boolean` | no |  | since 2.28 | Specifies if the customer uses e-invoicing. |
| `UseForwardRate` | `Boolean` | no |  |  | Specifies if forward rate should be used for the customer. |
| `UseInvoiceCustomersVatNumber` | `Boolean` | no |  |  | Specifies if VAT number should be taken via the invoice customer. |
| `UsePackageSpecification` | `Boolean?` | yes |  | since 2.28 | Specifies if the customer uses package specification. |
| `UseReminder` | `Boolean` | no |  |  | Specifies if reminders should be enabled for the customer. |
| `VatRateId` | `Int64?` | yes | [VatRates](../Common/VatRate.md) | **deprecated since 23.6** | The business key identifier of the customer's VAT rate. _(Replaced by VatGroupId on DeliveryAddress)_ |
| `VatRate` | `VatRates` | no | [VatRates](../Common/VatRate.md) | expandable, **deprecated since 23.6** | The VAT rate of the customer. _(Replaced by VatGroup from DeliveryAddress)_ |
| `ValidityTimeId` | `Int64` | no | [ValidityTimes](ValidityTime.md) |  | The business key identifier of the customer's validity time. |
| `ValidityTime` | `ValidityTimes` | no | [ValidityTimes](ValidityTime.md) |  | The validity time of the customer. |
| `Version` | `Int32` | no |  |  | The version of the customer. |
| `VisitingAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the customer's visiting address. |
| `VisitingAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The visiting address of the customer. |
| `CustomerPartLinks` | `CustomerPartLinks[]` | no | [CustomerPartLinks](CustomerPartLink.md) | expandable, collection | The part links defined for the customer. |
| `CaseEntries` | `CaseEntry[]` | no | [CaseEntry](../Inventory/CaseEntry.md) | expandable, collection | A collection of case entries that belong to the customer. |
| `OtherCustomerNumbers` | `OtherCustomerNumbers[]` | no | [OtherCustomerNumbers](OtherCustomerNumber.md) | expandable, collection, since 2.32 | Available other customer numbers. Mainly used as EDI identifiers. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](../Common/CommunicationAddress.md) | expandable, collection, since 2.50 | The communication addresses for the customer. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](../Common/ExtraField.md) | expandable, collection, since 2.54 | A collection of extra field values for the customer. |
| `PreliminaryPickingList` | `Boolean` | no |  | since 22.6 | Specifies if the customer should apply preliminary picking list. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](../Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the customer's currency exchange type. |
| `RootId` | `Int64` | no |  | since 24.3 | The business key identifier of the customer's root entity. |
| `EmployeeSpanId` | `Int64?` | yes |  | since 24.3 | The business key identifier of employee span of customer |
| `EmployeeSpan` | `CustomerEmployeeSpans` | no | [CustomerEmployeeSpans](CustomerEmployeeSpan.md) | expandable, since 24.3 | The employee span of customer |
| `TinNumber` | `String` | no |  | max length 13, since 25.9 | The customer's income tax reference number |

## Enumerations

### BlockedStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Message` | 1 |
| `Blocked` | 2 |

### BlockedContextType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Register` | 1 |
| `Report` | 2 |
| `RegisterSupplierInvoice` | 4 |
| `Payments` | 8 |

### DateDisplayFormat

| Name | Value |
| --- | ---: |
| `YYYYMMDD_Dash` | 1 |
| `YYMMDD_Dash` | 2 |
| `DDMMYYYY_Dash` | 3 |
| `DDMMYY_Dash` | 4 |
| `YYYYMMDD_Slash` | 5 |
| `YYMMDD_Slash` | 6 |
| `MMDDYYYY_Slash` | 7 |
| `MMDDYY_Slash` | 8 |
| `MDYY_Slash` | 9 |
| `DDMMYYYY_Slash` | 10 |
| `DDMMYY_Slash` | 11 |
| `DMMYY_Slash` | 12 |
| `YYYYMMDD_Dot` | 13 |
| `DDMMYYYY_Dot` | 14 |
| `DDMMYY_Dot` | 15 |
| `DDMYY_Dot` | 16 |
| `DMMYYYY_Dot` | 17 |
| `DMMYY_Dot` | 18 |
| `DMYYYY_Dot` | 19 |
| `DMYY_Dot` | 20 |
| `YYWWD` | 21 |

### DefaultOrderPrintoutVia

| Name | Value |
| --- | ---: |
| `Printer` | 0 |
| `Email` | 1 |
| `Edi` | 2 |
| `None` | 9 |

### PrintProformaInvoiceVia

| Name | Value |
| --- | ---: |
| `Printer` | 0 |
| `Email` | 1 |
| `Edi` | 2 |
| `None` | 9 |

### PrintPaymentReminderVia

| Name | Value |
| --- | ---: |
| `Printer` | 0 |
| `Email` | 1 |
| `Edi` | 2 |
| `None` | 9 |

### InterestType

| Name | Value |
| --- | ---: |
| `InterestInvoice` | 0 |
| `NextRegularInvoice` | 1 |
| `None` | 2 |

### InvoicePrintoutMethod

| Name | Value |
| --- | ---: |
| `Printer` | 0 |
| `Email` | 1 |
| `Edi` | 2 |
| `None` | 9 |

### InvoicePrintoutOccasion

| Name | Value |
| --- | ---: |
| `AfterDeliveryReport` | 0 |
| `OnDeliveryReportPreliminary` | 1 |
| `OnDeliveryReportDefinite` | 2 |

### PartialDeliveryType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `PerOrder` | 1 |
| `PerRow` | 2 |
| `NoneDelete` | 3 |
| `PerDeliveryDate` | 4 |

### ProformaInvoicePrintoutOccasion

| Name | Value |
| --- | ---: |
| `AfterDeliveryReport` | 0 |
| `OnDeliveryReport` | 1 |

### ShowPartStatisticalGoodsCodeAndCountryOfOriginInForms (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Quote` | 1 |
| `Acknowledgement` | 2 |
| `DeliveryNote` | 4 |
| `Invoice` | 8 |
| `ProFormaInvoice` | 16 |

### ShowPartStatisticalGoodsCodeInForms (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Quote` | 1 |
| `Acknowledgement` | 2 |
| `DeliveryNote` | 4 |
| `Invoice` | 8 |
| `ProFormaInvoice` | 16 |

### ShowCountryOfOriginInForms (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Quote` | 1 |
| `Acknowledgement` | 2 |
| `DeliveryNote` | 4 |
| `Invoice` | 8 |
| `ProFormaInvoice` | 16 |

### ShowPartWeightInForms (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Quote` | 1 |
| `Acknowledgement` | 2 |
| `DeliveryNote` | 4 |
| `Invoice` | 8 |
| `ProFormaInvoice` | 16 |

### ComprehensiveInvoiceGroupingMode

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Customer` | 1 |
| `Order` | 2 |
| `DeliveryNote` | 3 |


## Referenced by

**Accounting**

- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `BusinessContactId` (FK)
- [FixedAssetSales](../Accounting/FixedAssetSale.md) — `CustomerId` (FK)

**Common**

- [EdiBehaviors](../Common/EdiBehavior.md) — `Customers` (expand)
- [EdiBehaviors](../Common/EdiBehavior.md) — `InvoiceCustomers` (expand)
- [Projects](../Common/Project.md) — `CustomerId` (FK)

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `CustomerId` (FK)
- [PriceChangeLogs](../Inventory/PriceChangeLog.md) — `CustomerId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `OwnerId` (FK)
- [SalesForecasts](../Inventory/SalesForecast.md) — `CustomerId` (FK)

**Manufacturing**

- [ManufacturingOrders](../Manufacturing/ManufacturingOrder.md) — `CustomerId` (FK)

**Purchase**

- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `ActiveDeliveryAddressCustomerId` (FK)

**Sales**

- [BlanketOrderSales](BlanketOrderSales.md) — `BusinessContact` (expand)
- [BlanketOrderSales](BlanketOrderSales.md) — `BusinessContactId` (FK)
- [BusinessOpportunities](BusinessOpportunity.md) — `Customers` (expand)
- [BusinessOpportunityActivities](BusinessOpportunityActivity.md) — `CustomerId` (FK)
- [BusinessOpportunityReferences](BusinessOpportunityReference.md) — `CustomerId` (FK)
- [CustomerCountryDocumentSettings](CustomerCountryDocumentSettings.md) — `CustomerId` (FK)
- [CustomerOrderInvoices](CustomerOrderInvoice.md) — `ActiveDeliveryAddressCustomerId` (FK)
- [CustomerOrderInvoices](CustomerOrderInvoice.md) — `InvoiceBusinessContactId` (FK)
- [CustomerOrders](CustomerOrder.md) — `ActiveDeliveryAddressCustomerId` (FK)
- [CustomerOrders](CustomerOrder.md) — `CustomerId` (FK)
- [CustomerOrders](CustomerOrder.md) — `InvoiceCustomerId` (FK)
- [CustomerPartLinks](CustomerPartLink.md) — `CustomerId` (FK)
- [CustomerRelationshipManagementActivities](CustomerRelationshipManagementActivity.md) — `CustomerId` (FK)
- [Customers](Customer.md) — `InvoiceCustomerId` (FK)
- [InvoiceLogs](InvoiceLog.md) — `CustomerId` (FK)
- [OtherCustomerNumbers](OtherCustomerNumber.md) — `CustomerId` (FK)
- [Quotes](Quote.md) — `CustomerId` (FK)
- [SalesAgreements](SalesAgreement.md) — `BusinessContactId` (FK)
- [SalesAgreements](SalesAgreement.md) — `InvoiceBusinessContactId` (FK)
- [ShipmentInformationSources](ShipmentInformationSource.md) — `CustomerId` (FK)
- [Shipments](Shipment.md) — `ActiveDeliveryAddressCustomerId` (FK)


## Example

```json
{
  "Id": 0,
  "Name": null,
  "Code": null,
  "AlternativeName": null,
  "CorporationIdentificationNumber": null,
  "PersonalNumber": null,
  "IsPrivateCustomer": false,
  "VatNumber": null,
  "DeliveryAddresses": null,
  "ActiveDeliveryAddressId": 0,
  "ActiveDeliveryAddress": null,
  "References": null,
  "DefaultReferenceId": null,
  "DefaultReference": null,
  "Alias": null,
  "AlloyCost": 0,
  "ApplyBankCharge": false,
  "ApplyInvoicingCharge": false,
  "ApplyReminderCharge": false,
  "AccountManagerId": null,
  "AccountManager": null,
  "ActiveDeliveryAddressAccountGroupId": null,
  "ActiveDeliveryAddressAccountGroup": null,
  "ActualCustomerProbabilityId": null,
  "ActualCustomerProbability": null,
  "AttachDatafileWithOrder": false,
  "AttachDatafileWithInvoice": false,
  "AttachDatafileWithCase": false,
  "AttachDatafileWithPart": false,
  "AttachDatafileWithDispatchAdvice": false,
  "BankChargeAmount": 0.0,
  "BankGiroNo": null,
  "BlockedById": null,
  "BlockedBy": null,
  "BlockedStatus": 0,
  "BlockedContextType": 0,
  "BlockMessageId": null,
  "BlockMessage": null,
  "BlockedFromDate": null,
  "BlockedToDate": null,
  "CategoryString": null,
  "CommentId": null,
  "Comment": null,
  "CompanyId": 0,
  "ConfigurationPriceListId": null,
  "CreditLimit": 0.0,
  "CurrencyId": 0,
  "Currency": null,
  "DateDisplayFormat": 0,
  "DecimalSymbol": null,
  "DeliveryHorizon": null,
  "DeliveryNoteNumberWhenDeliveryPlanning": false,
  "DistrictId": null,
  "District": null,
  "DateForTransitionToActualContact": null,
  "Discount": null,
  "DiscountCategoryId": null,
  "DiscountCategory": null,
  "DefaultOrderPrintoutVia": 0,
  "PrintProformaInvoiceVia": 0,
  "PrintPaymentReminderVia": 0,
  "DeliveryInstruction": null,
  "DefaultInvoiceStatusPending": false,
  "EdiCode": null,
  "EInvoiceElectronicAddressIdentifier": null,
  "EInvoiceId": null,
  "EInvoiceOperatorCode": null,
  "Factoring": false,
  "GracePeriod": null,
  "HideDiscountOnProformaInvoice": false,
  "IncludeInDeliveryAnalysis": null,
  "InvoiceAddressId": null,
  "InvoiceAddress": null,
  "InterestType": 0,
  "IsCasualCustomer": false,
  "InterestInvoiceDays": null,
  "InsuranceCost": 0.0,
  "InvoiceCustomerId": null,
  "InvoicePrintoutMethod": 0,
  "InvoicePrintoutOccasion": 0,
  "IsInternal": false,
  "LanguageId": 0,
  "Language": null,
  "LatePaymentFee": null,
  "MailingAddressId": 0,
  "MailingAddress": null,
  "NumberOfInvoiceCopies": null,
  "OurCodeByYou": null,
  "PalletRegistrationNo": null,
  "PartialDeliveryType": 0,
  "PaymentPlanTemplateId": null,
  "PaymentPlanTemplate": null,
  "PaymentTermId": 0,
  "PaymentTerm": null,
  "PlusGiroNo": null,
  "PriceListId": 0,
  "Priority": 0,
  "PickingListCommentId": null,
  "PickingListComment": null,
  "ProformaInvoicePrintoutOccasion": 0,
  "ResellerId": null,
  "Reseller": null,
  "RoundOff": false,
  "SellerId": null,
  "Seller": null,
  "ServiceAgreementId": null,
  "ServiceTaxNumber": null,
  "ShowPartStatisticalGoodsCodeAndCountryOfOriginInForms": 0,
  "ShowPartStatisticalGoodsCodeInForms": 0,
  "ShowCountryOfOriginInForms": 0,
  "ShowPartWeightInForms": 0,
  "StatusId": 0,
  "Status": null,
  "TimeZone": null,
  "TimeZoneOffset": 0.0,
  "ToleranceForLateDelivery": null,
  "ToleranceForEarlyDelivery": null,
  "TypeId": null,
  "Type": null,
  "Url": null,
  "UseBundling": null,
  "UseComprehensiveInvoices": false,
  "ComprehensiveInvoiceGroupingMode": 0,
  "UseDeliveryNoteCollectionFormReport": false,
  "UseEInvoicing": false,
  "UseForwardRate": false,
  "UseInvoiceCustomersVatNumber": false,
  "UsePackageSpecification": null,
  "UseReminder": false,
  "VatRateId": null,
  "VatRate": null,
  "ValidityTimeId": 0,
  "ValidityTime": null,
  "Version": 0,
  "VisitingAddressId": null,
  "VisitingAddress": null,
  "CustomerPartLinks": null,
  "CaseEntries": null,
  "OtherCustomerNumbers": null,
  "CommunicationAddresses": null,
  "ExtraFields": null,
  "PreliminaryPickingList": false,
  "CurrencyExchangeTypeId": 0,
  "RootId": 0,
  "EmployeeSpanId": null,
  "EmployeeSpan": null,
  "TinNumber": null
}
```
