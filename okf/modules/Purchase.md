---
type: API Module
title: Purchase
description: Monitor ERP API module Purchase.
tags:
- Purchase
- module
generated:
  by: process:monitor-okf-build
  from: 677a27684767
entity_count: 30
queryable_count: 30
---

# Purchase

Monitor API module `Purchase`: 30 queryable entities, 0 commands, 0 payload types.

Full listing: [Purchase entities](../entities/Purchase/index.md)

## Queryable entities

| Entity | Endpoint | Description |
| --- | --- | --- |
| [BlanketOrderPurchaseRows](../entities/Purchase/BlanketOrderPurchaseRow.md) | `/api/v1/Purchase/BlanketOrderPurchaseRows` | Represents a blanket order row for purchase. |
| [BlanketOrderPurchases](../entities/Purchase/BlanketOrderPurchase.md) | `/api/v1/Purchase/BlanketOrderPurchases` | Represents a blanket order for purchase. |
| [BlanketOrderPurchaseTypes](../entities/Purchase/BlanketOrderPurchaseType.md) | `/api/v1/Purchase/BlanketOrderPurchaseTypes` | Represents a blanket order type for purchase. |
| [EimDocuments](../entities/Purchase/EimDocument.md) | `/api/v1/Purchase/EimDocuments` | Represents an EimDocument. |
| [EimDocumentTypes](../entities/Purchase/EimDocumentType.md) | `/api/v1/Purchase/EimDocumentTypes` | Represents an EIM document type. |
| [Inquiries](../entities/Purchase/Inquiry.md) | `/api/v1/Purchase/Inquiries` | Represents an inquiry. |
| [InquiryRows](../entities/Purchase/InquiryRow.md) | `/api/v1/Purchase/InquiryRows` | Represents an inquiry row. |
| [InquiryTypes](../entities/Purchase/InquiryType.md) | `/api/v1/Purchase/InquiryTypes` | Represents an inquiry type. |
| [OrderQuantityPurchaseOrders](../entities/Purchase/OrderQuantityPurchaseOrder.md) | `/api/v1/Purchase/OrderQuantityPurchaseOrders` | Represents a order quantity template on part that holds many partial quantities. |
| [OtherSupplierNumbers](../entities/Purchase/OtherSupplierNumber.md) | `/api/v1/Purchase/OtherSupplierNumbers` | Represents an alternative supplier code mainly used for EDI. |
| [PackingTerms](../entities/Purchase/PackingTerm.md) | `/api/v1/Purchase/PackingTerms` | Represents a packing term. |
| [PurchaseOrderAdviceRowProductRecords](../entities/Purchase/PurchaseOrderAdviceRowProductRecord.md) | `/api/v1/Purchase/PurchaseOrderAdviceRowProductRecords` | Represents a purchase order advice row product record. |
| [PurchaseOrderAdviceRows](../entities/Purchase/PurchaseOrderAdviceRow.md) | `/api/v1/Purchase/PurchaseOrderAdviceRows` | Represents a purchase order advice row. |
| [PurchaseOrderAdvices](../entities/Purchase/PurchaseOrderAdvice.md) | `/api/v1/Purchase/PurchaseOrderAdvices` | Represents a purchase order advice. |
| [PurchaseOrderDeliveries](../entities/Purchase/PurchaseOrderDelivery.md) | `/api/v1/Purchase/PurchaseOrderDeliveries` | Represents a purchase order delivery entry |
| [PurchaseOrderDeliveryRowQuantities](../entities/Purchase/PurchaseOrderDeliveryRowQuantity.md) | `/api/v1/Purchase/PurchaseOrderDeliveryRowQuantities` | Represents a purchase order delivery row quantity entry |
| [PurchaseOrderDeliveryRows](../entities/Purchase/PurchaseOrderDeliveryRow.md) | `/api/v1/Purchase/PurchaseOrderDeliveryRows` | Represents a purchase order delivery row entry |
| [PurchaseOrderInvoiceRows](../entities/Purchase/PurchaseOrderInvoiceRow.md) | `/api/v1/Purchase/PurchaseOrderInvoiceRows` | Represents a purchase order invoice row entry |
| [PurchaseOrderInvoices](../entities/Purchase/PurchaseOrderInvoice.md) | `/api/v1/Purchase/PurchaseOrderInvoices` | Represents a purchase order invoice entry |
| [PurchaseOrderRows](../entities/Purchase/PurchaseOrderRow.md) | `/api/v1/Purchase/PurchaseOrderRows` | Represents a purchase order row. |
| [PurchaseOrders](../entities/Purchase/PurchaseOrder.md) | `/api/v1/Purchase/PurchaseOrders` | Represents a purchase order. |
| [PurchaseOrderTypes](../entities/Purchase/PurchaseOrderType.md) | `/api/v1/Purchase/PurchaseOrderTypes` | Represents a purchase order type. |
| [ResponseTimes](../entities/Purchase/ResponseTime.md) | `/api/v1/Purchase/ResponseTimes` | Represents a response time. |
| [SupplierAccountGroups](../entities/Purchase/SupplierAccountGroup.md) | `/api/v1/Purchase/SupplierAccountGroups` | Represents a supplier account group. |
| [SupplierAccounts](../entities/Purchase/SupplierAccount.md) | `/api/v1/Purchase/SupplierAccounts` | Represents a supplier account. |
| [SupplierDistricts](../entities/Purchase/SupplierDistrict.md) | `/api/v1/Purchase/SupplierDistricts` | Represents a supplier district. |
| [SupplierPartLinks](../entities/Purchase/SupplierPartLink.md) | `/api/v1/Purchase/SupplierPartLinks` | Represents a supplier part link. |
| [Suppliers](../entities/Purchase/Supplier.md) | `/api/v1/Purchase/Suppliers` | Represents a supplier. |
| [SupplierStatuses](../entities/Purchase/SupplierStatus.md) | `/api/v1/Purchase/SupplierStatuses` | Represents a supplier status. |
| [SupplierTypes](../entities/Purchase/SupplierType.md) | `/api/v1/Purchase/SupplierTypes` | Represents a supplier type. |

## Depends on other modules

- [Accounting](Accounting.md): [AccountsPayables](../entities/Accounting/AccountsPayable.md), [CodingEntries](../entities/Accounting/CodingEntry.md), [Codings](../entities/Accounting/Coding.md), [StandardAccounts](../entities/Accounting/StandardAccount.md)
- [Common](Common.md): [Addresses](../entities/Common/Address.md), [ApplicationUsers](../entities/Common/ApplicationUser.md), [BlobData](../entities/Common/BlobData.md), [BusinessContactBankAccounts](../entities/Common/BusinessContactBankAccount.md), [BusinessContactReferences](../entities/Common/BusinessContactReference.md), [Comments](../entities/Common/Comment.md), [CommunicationAddresses](../entities/Common/CommunicationAddress.md), [Currencies](../entities/Common/Currency.md), [CurrencyExchangeTypes](../entities/Common/CurrencyExchangeType.md), [DeliveryAddresses](../entities/Common/DeliveryAddress.md), [DeliveryMethods](../entities/Common/DeliveryMethod.md), [DeliveryTerms](../entities/Common/DeliveryTerm.md), [DiscountCategories](../entities/Common/DiscountCategory.md), [ExtraFields](../entities/Common/ExtraField.md), [LanguageCodes](../entities/Common/LanguageCode.md), [PartialQuantities](../entities/Common/PartialQuantity.md), [PaymentMethods](../entities/Common/PaymentMethod.md), [PaymentTerms](../entities/Common/PaymentTerm.md), [Persons](../entities/Common/Person.md), [PriceLists](../entities/Common/PriceList.md), [Projects](../entities/Common/Project.md), [ReasonCodes](../entities/Common/ReasonCode.md), [Revisions](../entities/Common/Revision.md), [StatisticalGoodsCodes](../entities/Common/StatisticalGoodsCode.md), [TariffAndServiceCodes](../entities/Common/TariffAndServiceCode.md), [TransactionTypeIntrastats](../entities/Common/TransactionTypeIntrastat.md), [Units](../entities/Common/Unit.md), [VatGroups](../entities/Common/VatGroup.md), [VatRates](../entities/Common/VatRate.md), [Warehouses](../entities/Common/Warehouse.md)
- [Inventory](Inventory.md): [CaseEntry](../entities/Inventory/CaseEntry.md), [PartPurchaseExpenseValues](../entities/Inventory/PartPurchaseExpenseValues.md), [Parts](../entities/Inventory/Part.md), [QuantityChanges](../entities/Inventory/QuantityChange.md)
- [Manufacturing](Manufacturing.md): [ManufacturingOrderOperations](../entities/Manufacturing/ManufacturingOrderOperation.md)
- [Sales](Sales.md): [CustomerOrderRows](../entities/Sales/CustomerOrderRow.md), [CustomerOrders](../entities/Sales/CustomerOrder.md), [Customers](../entities/Sales/Customer.md)
