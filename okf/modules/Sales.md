---
type: API Module
title: Sales
description: Monitor ERP API module Sales.
tags:
- Sales
- module
generated:
  by: process:monitor-okf-build
  from: 677a27684767
entity_count: 76
queryable_count: 70
---

# Sales

Monitor API module `Sales`: 70 queryable entities, 4 commands, 2 payload types.

Full listing: [Sales entities](../entities/Sales/index.md)

## Queryable entities

| Entity | Endpoint | Description |
| --- | --- | --- |
| [BlanketOrderSales](../entities/Sales/BlanketOrderSales.md) | `/api/v1/Sales/BlanketOrderSales` | Represents a blanket order for sales. |
| [BlanketOrderSalesRows](../entities/Sales/BlanketOrderSalesRow.md) | `/api/v1/Sales/BlanketOrderSalesRows` | Represents a blanket order row for sales. |
| [BlanketOrderSalesTypes](../entities/Sales/BlanketOrderSalesType.md) | `/api/v1/Sales/BlanketOrderSalesTypes` | Represents a blanket order type for sales. |
| [BusinessOpportunities](../entities/Sales/BusinessOpportunity.md) | `/api/v1/Sales/BusinessOpportunities` | Represents a business opportunity. |
| [BusinessOpportunityActivities](../entities/Sales/BusinessOpportunityActivity.md) | `/api/v1/Sales/BusinessOpportunityActivities` | Represents a business opportunity activity. |
| [BusinessOpportunityActivityTemplateRows](../entities/Sales/BusinessOpportunityActivityTemplateRow.md) | `/api/v1/Sales/BusinessOpportunityActivityTemplateRows` | Represents a business opportunity activity template row. |
| [BusinessOpportunityActivityTemplates](../entities/Sales/BusinessOpportunityActivityTemplate.md) | `/api/v1/Sales/BusinessOpportunityActivityTemplates` | Represents a business opportunity activity template. |
| [BusinessOpportunityGroups](../entities/Sales/BusinessOpportunityGroup.md) | `/api/v1/Sales/BusinessOpportunityGroups` | Represents a business opportunity group. |
| [BusinessOpportunityReferences](../entities/Sales/BusinessOpportunityReference.md) | `/api/v1/Sales/BusinessOpportunityReferences` | Represents a business opportunity reference. |
| [BusinessOpportunitySalesProcessSteps](../entities/Sales/BusinessOpportunitySalesProcessStep.md) | `/api/v1/Sales/BusinessOpportunitySalesProcessSteps` | Represents a business opportunity sales process step. |
| [BusinessOpportunityTypes](../entities/Sales/BusinessOpportunityType.md) | `/api/v1/Sales/BusinessOpportunityTypes` | Represents a business opportunity type. |
| [CountryDocumentSettings](../entities/Sales/CountryDocumentSettings.md) | `/api/v1/Sales/CountryDocumentSettings` | Represents a country document setting. |
| [CustomerAccountGroups](../entities/Sales/CustomerAccountGroup.md) | `/api/v1/Sales/CustomerAccountGroups` | Represents a customer account group. |
| [CustomerCountryDocumentSettings](../entities/Sales/CustomerCountryDocumentSettings.md) | `/api/v1/Sales/CustomerCountryDocumentSettings` | Represents a customer country document setting. |
| [CustomerDistricts](../entities/Sales/CustomerDistrict.md) | `/api/v1/Sales/CustomerDistricts` | Represents a customer district. |
| [CustomerEmployeeSpans](../entities/Sales/CustomerEmployeeSpan.md) | `/api/v1/Sales/CustomerEmployeeSpans` | Represents a customer employee span. |
| [CustomerOrderActivities](../entities/Sales/CustomerOrderActivity.md) | `/api/v1/Sales/CustomerOrderActivities` | Represents a customer order activity. |
| [CustomerOrderDeliveryRows](../entities/Sales/CustomerOrderDeliveryRow.md) | `/api/v1/Sales/CustomerOrderDeliveryRows` | Represents a customer delivery order row. |
| [CustomerOrderInvoiceOrderRowDiscounts](../entities/Sales/CustomerOrderInvoiceOrderRowDiscount.md) | `/api/v1/Sales/CustomerOrderInvoiceOrderRowDiscounts` | Represents a discount row for a customer order invoice row. |
| [CustomerOrderInvoiceRows](../entities/Sales/CustomerOrderInvoiceRow.md) | `/api/v1/Sales/CustomerOrderInvoiceRows` | Represents a customer order invoice row. |
| [CustomerOrderInvoices](../entities/Sales/CustomerOrderInvoice.md) | `/api/v1/Sales/CustomerOrderInvoices` | Represents a customer order invoice. |
| [CustomerOrderOrderRowDiscounts](../entities/Sales/CustomerOrderOrderRowDiscount.md) | `/api/v1/Sales/CustomerOrderOrderRowDiscounts` | Represents a discount row for a customer order row. |
| [CustomerOrderPaymentPlanRows](../entities/Sales/CustomerOrderPaymentPlanRow.md) | `/api/v1/Sales/CustomerOrderPaymentPlanRows` | Represents a customer order payment plan row. |
| [CustomerOrderRowInflows](../entities/Sales/CustomerOrderRowInflow.md) | `/api/v1/Sales/CustomerOrderRowInflows` | Represents a customer order inflow row. |
| [CustomerOrderRows](../entities/Sales/CustomerOrderRow.md) | `/api/v1/Sales/CustomerOrderRows` | Represents a customer order row. |
| [CustomerOrders](../entities/Sales/CustomerOrder.md) | `/api/v1/Sales/CustomerOrders` | Represents a customer order. |
| [CustomerOrderShippingInformationRows](../entities/Sales/CustomerOrderShippingInformationRow.md) | `/api/v1/Sales/CustomerOrderShippingInformationRows` | Represents a customer order shipping information row. |
| [CustomerOrderTypes](../entities/Sales/CustomerOrderType.md) | `/api/v1/Sales/CustomerOrderTypes` | Represents a customer order type. |
| [CustomerPartLinks](../entities/Sales/CustomerPartLink.md) | `/api/v1/Sales/CustomerPartLinks` | Represents a customer part link. |
| [CustomerRelationshipActivityTypes](../entities/Sales/CustomerRelationshipActivityType.md) | `/api/v1/Sales/CustomerRelationshipActivityTypes` | Represents a customer relationship activity type. |
| [CustomerRelationshipManagementActivities](../entities/Sales/CustomerRelationshipManagementActivity.md) | `/api/v1/Sales/CustomerRelationshipManagementActivities` | Represents a customer relationship management activity. |
| [Customers](../entities/Sales/Customer.md) | `/api/v1/Sales/Customers` | Represents a customer. |
| [CustomerStatuses](../entities/Sales/CustomerStatus.md) | `/api/v1/Sales/CustomerStatuses` | Represents a customer status. |
| [CustomerTypes](../entities/Sales/CustomerType.md) | `/api/v1/Sales/CustomerTypes` | Represents a customer type. |
| [InvoiceLogs](../entities/Sales/InvoiceLog.md) | `/api/v1/Sales/InvoiceLogs` | Represents an invoice log entry. |
| [OrderQuantityCustomerOrders](../entities/Sales/OrderQuantityCustomerOrder.md) | `/api/v1/Sales/OrderQuantityCustomerOrders` | Represents a order quantity template on part that holds many partial quantities. |
| [OtherCustomerNumbers](../entities/Sales/OtherCustomerNumber.md) | `/api/v1/Sales/OtherCustomerNumbers` | Represents an alternative customer code mainly used for EDI. |
| [PackageRowPartLocations](../entities/Sales/PackageRowPartLocation.md) | `/api/v1/Sales/PackageRowPartLocations` | Represents a package row's location. |
| [PackageRows](../entities/Sales/PackageRow.md) | `/api/v1/Sales/PackageRows` | Represents a package row. |
| [QuoteActivities](../entities/Sales/QuoteActivity.md) | `/api/v1/Sales/QuoteActivities` | Represents a quote activity. |
| [QuoteOrderRowDiscounts](../entities/Sales/QuoteOrderRowDiscount.md) | `/api/v1/Sales/QuoteOrderRowDiscounts` | Represents a discount row for a quote row. |
| [QuoteRows](../entities/Sales/QuoteRow.md) | `/api/v1/Sales/QuoteRows` | Represents a quote row. |
| [Quotes](../entities/Sales/Quote.md) | `/api/v1/Sales/Quotes` | Represents a quote. |
| [QuoteTypes](../entities/Sales/QuoteType.md) | `/api/v1/Sales/QuoteTypes` | Represents a quote type. |
| [ReasonCodeLostQuotes](../entities/Sales/ReasonCodeLostQuote.md) | `/api/v1/Sales/ReasonCodeLostQuotes` | Represents a reason code for a lost quote. |
| [RelatedQuoteEntries](../entities/Sales/RelatedQuoteEntry.md) | `/api/v1/Sales/RelatedQuoteEntries` | Represents a related quote entry. |
| [RelatedQuotes](../entities/Sales/RelatedQuote.md) | `/api/v1/Sales/RelatedQuotes` | Represents a placeholder for related quotes. |
| [SalesAgreementBases](../entities/Sales/SalesAgreementBasis.md) | `/api/v1/Sales/SalesAgreementBases` | Represents a sales agreement basis. |
| [SalesAgreementBasisRows](../entities/Sales/SalesAgreementBasisRow.md) | `/api/v1/Sales/SalesAgreementBasisRows` | Represents a sales agreement basis row. |
| [SalesAgreementRowInflows](../entities/Sales/SalesAgreementRowInflow.md) | `/api/v1/Sales/SalesAgreementRowInflows` | Represents a sales agreement inflow row. |
| [SalesAgreementRows](../entities/Sales/SalesAgreementRow.md) | `/api/v1/Sales/SalesAgreementRows` | Represents an agreement row. |
| [SalesAgreements](../entities/Sales/SalesAgreement.md) | `/api/v1/Sales/SalesAgreements` | Represents an agreement. |
| [SalesAgreementTypes](../entities/Sales/SalesAgreementType.md) | `/api/v1/Sales/SalesAgreementTypes` | Represents an agreement type. |
| [SalesPickingListRowQuantities](../entities/Sales/SalesPickingListRowQuantity.md) | `/api/v1/Sales/SalesPickingListRowQuantities` | Represents sales picking list row quantity information used by the web-client procedure. |
| [SalesPickingLists](../entities/Sales/SalesPickingList.md) | `/api/v1/Sales/SalesPickingLists` | Represents a sales picking list. |
| [SalesPrices](../entities/Sales/SalesPrice.md) | `/api/v1/Sales/SalesPrices` | Represents a sales price. |
| [SalesProcessSteps](../entities/Sales/SalesProcessStep.md) | `/api/v1/Sales/SalesProcessSteps` | Represents a sales process step. |
| [SalesProcessTemplateRows](../entities/Sales/SalesProcessTemplateRow.md) | `/api/v1/Sales/SalesProcessTemplateRows` | Represents a sales process template row. |
| [SalesProcessTemplates](../entities/Sales/SalesProcessTemplate.md) | `/api/v1/Sales/SalesProcessTemplates` | Represents a sales process template. |
| [SellerGroups](../entities/Sales/SellerGroup.md) | `/api/v1/Sales/SellerGroups` | Represents a seller group. |
| [ShipmentCustoms](../entities/Sales/ShipmentCustoms.md) | `/api/v1/Sales/ShipmentCustoms` | Represents a shipments customs information. |
| [ShipmentCustomsDocuments](../entities/Sales/ShipmentCustomsDocument.md) | `/api/v1/Sales/ShipmentCustomsDocuments` | Represents a shipments customs information document. |
| [ShipmentCustomsRows](../entities/Sales/ShipmentCustomsRow.md) | `/api/v1/Sales/ShipmentCustomsRows` | Represents a shipments customs information row. |
| [ShipmentInformationSources](../entities/Sales/ShipmentInformationSource.md) | `/api/v1/Sales/ShipmentInformationSources` | Represents a shipment information source. |
| [ShipmentPackageInformationPackageNumbers](../entities/Sales/ShipmentPackageInformationPackageNumber.md) | `/api/v1/Sales/ShipmentPackageInformationPackageNumbers` | Represents a shipping agents real package number for a shipment package information. |
| [ShipmentPackageInformations](../entities/Sales/ShipmentPackageInformation.md) | `/api/v1/Sales/ShipmentPackageInformations` | Represents a shipment package information. |
| [Shipments](../entities/Sales/Shipment.md) | `/api/v1/Sales/Shipments` | Represents a shipment. |
| [ShippingServices](../entities/Sales/ShippingService.md) | `/api/v1/Sales/ShippingServices` | Represents a shipping service. |
| [ShippingTemplates](../entities/Sales/ShippingTemplate.md) | `/api/v1/Sales/ShippingTemplates` | Represents a shipping service. |
| [ValidityTimes](../entities/Sales/ValidityTime.md) | `/api/v1/Sales/ValidityTimes` | Represents a validity time. |

## Commands

| Command | Endpoint | Description |
| --- | --- | --- |
| [CreateCustomerEmployeeSpan](../entities/Sales/CreateCustomerEmployeeSpan.md) | `POST /api/v1/Sales/CustomerEmployeeSpans/Create` | Creates a new customer employee span object. |
| [CreateSalesPickingList](../entities/Sales/CreateSalesPickingList.md) | `POST /api/v1/Sales/SalesPickingLists/Create` | Creates picking lists. |
| [GetWithdrawalInformation](../entities/Sales/GetWithdrawalInformation.md) | `POST /api/v1/Sales/SalesPickingLists/GetWithdrawalInformation` | Calculates and returns the suggested withdrawal information for a picking list. |
| [RemoveSalesPickingList](../entities/Sales/RemoveSalesPickingList.md) | `POST /api/v1/Sales/SalesPickingLists/Remove` | Deletes a picking list. |

## Payload types

| Type | Description |
| --- | --- |
| [WithdrawalInformationLocation](../entities/Sales/WithdrawalInformationLocation.md) | Used to provide the suggested withdrawal information of a location. |
| [WithdrawalInformationRow](../entities/Sales/WithdrawalInformationRow.md) | Used to provide the suggested withdrawal information of a customer order row. |

## Depends on other modules

- [Accounting](Accounting.md): [Accounts](../entities/Accounting/Account.md), [AccountsReceivables](../entities/Accounting/AccountsReceivable.md), [CodingEntries](../entities/Accounting/CodingEntry.md), [Codings](../entities/Accounting/Coding.md), [FixedAssets](../entities/Accounting/FixedAsset.md)
- [Common](Common.md): [Addresses](../entities/Common/Address.md), [ApplicationUsers](../entities/Common/ApplicationUser.md), [BusinessContactNoteHistories](../entities/Common/BusinessContactNoteHistory.md), [BusinessContactReferences](../entities/Common/BusinessContactReference.md), [Comments](../entities/Common/Comment.md), [CommunicationAddresses](../entities/Common/CommunicationAddress.md), [Countries](../entities/Common/Country.md), [Currencies](../entities/Common/Currency.md), [CurrencyExchangeTypes](../entities/Common/CurrencyExchangeType.md), [DeliveryAddresses](../entities/Common/DeliveryAddress.md), [DeliveryMethods](../entities/Common/DeliveryMethod.md), [DeliveryTerms](../entities/Common/DeliveryTerm.md), [DeliveryTimes](../entities/Common/DeliveryTime.md), [DiscountCategories](../entities/Common/DiscountCategory.md), [Discounts](../entities/Common/Discount.md), [ExtraFields](../entities/Common/ExtraField.md), [FormReportConfigurations](../entities/Common/FormReportConfiguration.md), [LanguageCodes](../entities/Common/LanguageCode.md), [PartConfigurations](../entities/Common/PartConfiguration.md), [PartialQuantities](../entities/Common/PartialQuantity.md), [PaymentMethods](../entities/Common/PaymentMethod.md), [PaymentPlanTemplates](../entities/Common/PaymentPlanTemplate.md), [PaymentTerms](../entities/Common/PaymentTerm.md), [Persons](../entities/Common/Person.md), [PriceLists](../entities/Common/PriceList.md), [Probabilities](../entities/Common/Probability.md), [Projects](../entities/Common/Project.md), [ReasonCodeDebitNotes](../entities/Common/ReasonCodeDebitNote.md), [Resellers](../entities/Common/Reseller.md), [Revisions](../entities/Common/Revision.md), [StaggeredPrices](../entities/Common/StaggeredPrice.md), [StatisticalGoodsCodes](../entities/Common/StatisticalGoodsCode.md), [TariffAndServiceCodes](../entities/Common/TariffAndServiceCode.md), [TransactionTypeIntrastats](../entities/Common/TransactionTypeIntrastat.md), [TransferProfiles](../entities/Common/TransferProfile.md), [Units](../entities/Common/Unit.md), [VatGroups](../entities/Common/VatGroup.md), [VatRates](../entities/Common/VatRate.md), [Warehouses](../entities/Common/Warehouse.md)
- [Inventory](Inventory.md): [CaseEntry](../entities/Inventory/CaseEntry.md), [GoodsTypes](../entities/Inventory/GoodsType.md), [PackageTypes](../entities/Inventory/PackageType.md), [PartLocations](../entities/Inventory/PartLocation.md), [Parts](../entities/Inventory/Part.md), [ProductRecords](../entities/Inventory/ProductRecord.md)
- [Manufacturing](Manufacturing.md): [ManufacturingOrders](../entities/Manufacturing/ManufacturingOrder.md)
- [Purchase](Purchase.md): [PurchaseOrderRows](../entities/Purchase/PurchaseOrderRow.md), [PurchaseOrders](../entities/Purchase/PurchaseOrder.md), [Suppliers](../entities/Purchase/Supplier.md)
