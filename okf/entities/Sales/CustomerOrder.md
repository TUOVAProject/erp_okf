---
type: API Entity
title: CustomerOrders
description: Represents a customer order.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrder.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrder.html
  title: Monitor API — CustomerOrder
module: Sales
api_class: CustomerOrder
doc_name: CustomerOrders
endpoint: GET /api/v1/Sales/CustomerOrders
guid: 9A008BAB-1814-43EC-AFA5-4E42A5C3B36C
permission: Show customer orders
introduced_in: '2.18'
property_count: 115
references_out:
- /entities/Common/Address.md
- /entities/Common/ApplicationUser.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/CommunicationAddress.md
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/DeliveryMethod.md
- /entities/Common/DeliveryTerm.md
- /entities/Common/PaymentMethod.md
- /entities/Common/PaymentPlanTemplate.md
- /entities/Common/PaymentTerm.md
- /entities/Common/Person.md
- /entities/Common/ReasonCodeDebitNote.md
- /entities/Common/VatGroup.md
- /entities/Common/Warehouse.md
- /entities/Inventory/ProductRecord.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerAccountGroup.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/CustomerOrderShippingInformationRow.md
- /entities/Sales/CustomerOrderType.md
referenced_by:
- /entities/Common/Project.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CasePartLink.md
- /entities/Inventory/Location.md
- /entities/Inventory/ProductRecord.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Sales/CustomerOrderActivity.md
- /entities/Sales/CustomerOrderDeliveryRow.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/CustomerOrderPaymentPlanRow.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/CustomerRelationshipManagementActivity.md
- /entities/Sales/InvoiceLog.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/SalesAgreementBasis.md
- /entities/Sales/ShipmentInformationSource.md
---

# CustomerOrders

Represents a customer order.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerOrder`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrders`
- **Required permission:** Show customer orders
- **GUID:** `9A008BAB-1814-43EC-AFA5-4E42A5C3B36C`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer order. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](../Common/PaymentTerm.md) |  | The business key identifier of the payment term of the customer order. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](../Common/PaymentTerm.md) | expandable | The payment term of the customer order. |
| `PaymentTermDescription` | `String` | no |  | max length 35 | The payment term description of the customer order. |
| `GracePeriodInDays` | `Int32?` | yes |  |  | The customer order's grace period in days. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](../Common/DeliveryMethod.md) |  | The business key identifier of the customer order's delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](../Common/DeliveryTerm.md) |  | The business key identifier of the customer order's delivery term. |
| `DeliveryTermDescription` | `String` | no |  | max length 35 | The delivery term description of the customer order. |
| `DeliveryMethodDescription` | `String` | no |  | max length 35 | The delivery method description of the customer order. |
| `ShipmentPayer` | `Int32` | no |  | enum | Specifies who is responsible for the shipment payment for the customer order. |
| `BusinessContactOrderNumber` | `String` | no |  | max length 30 | The end-customer's order number for the customer order. |
| `OurReferenceId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of our reference for the customer order. Reference Persons |
| `OurReferenceName` | `String` | no |  | max length 80 | The name of our reference for the customer order. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](../Common/BusinessContactReference.md) |  | The business key identifier of the customer's reference for the customer order. |
| `BusinessContactReferenceName` | `String` | no |  | max length 80 | The name of the customer's reference for the customer order. |
| `GoodsLabel` | `String` | no |  | max length 80 | The goods label of the customer order. |
| `CurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the currency of the customer order. |
| `VatGroupId` | `Int64` | no | [VatGroups](../Common/VatGroup.md) |  | The business key identifier of the VAT group that applies for the customer order. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse that the customer order belongs to. |
| `Priority` | `Int32` | no |  |  | The priority of the customer order. |
| `ProjectId` | `Int64?` | yes |  |  | The business key identifier of the customer order's project. |
| `SendMethod` | `Int32` | no |  | enum | Specifies the printout method for the customer order. |
| `InvoicePrintoutMethod` | `Int32` | no |  | enum | Specifies the printout method that should be used for invoices. |
| `InternalCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the customer order's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The internal comment of the customer order. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the customer order's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The external comment of the customer order. |
| `TransportTime` | `Int32?` | yes |  |  | The transport time of the customer order in workdays. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the customer order. |
| `Version` | `Int32` | no |  |  | The version of the customer order. |
| `UseForwardRate` | `Boolean` | no |  |  | Specifies if forward rate should apply for the customer order. |
| `ExchangeRate` | `Decimal` | no |  |  | Specifies the exchange rate to use for the customer order. |
| `OrderAmount` | `Decimal` | no |  | **deprecated since 2.36** | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `OrderAmountInCompanyCurrency` | `Decimal` | no |  | **deprecated since 2.36** | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `CustomerId` | `Int64` | no | [Customers](Customer.md) |  | The business key identifier of the customer that the customer order belongs to. |
| `InvoiceCustomerId` | `Int64` | no | [Customers](Customer.md) |  | The business key identifier of the invoice customer that the customer order belongs to. |
| `OrderNumber` | `String` | no |  | unique, max length 15 | The human readable identifier of the customer order. |
| `OrderDate` | `DateTimeOffset` | no |  |  | The order date of the customer order. |
| `Rows` | `CustomerOrderRows[]` | no | [CustomerOrderRows](CustomerOrderRow.md) | expandable, collection | The rows of the customer order. |
| `SellerId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the customer order's seller. |
| `ShowPriceInAcknowledgement` | `Boolean` | no |  |  | Specifies if price should be shown in the acknowledgement of the customer order. |
| `ShowTotalInAcknowledgement` | `Boolean` | no |  |  | Specifies if the price total should be shown in the acknowledgement of the customer order. |
| `ThirdPartyTrading` | `Boolean` | no |  |  | Specifies if the customer order falls under third party trading. |
| `DeliveryInstruction` | `String` | no |  | max length 80 | The delivery instruction of the customer order. |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](Customer.md) |  | The business key identifier of the customer source of the active delivery address. |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](../Purchase/Supplier.md) |  | The business key identifier of the supplier source of the active delivery address. |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  |  | The business key identifier of the company source of the active delivery address. |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  | enum | Specifies the source of the customer order delivery address. |
| `IsCredit` | `Boolean` | no |  |  | Specifies if the customer order is on credit or not. |
| `InvoiceType` | `Int32` | no |  | enum | The invoice type of the customer order. |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](../Common/PaymentMethod.md) |  | The business key identifier of the customer order's payment method. |
| `PaymentMethod` | `PaymentMethods` | no | [PaymentMethods](../Common/PaymentMethod.md) | expandable, since 2.30 | The payment method on the customer order. |
| `PrintoutTimeStamp` | `DateTimeOffset` | no |  | **deprecated since 2.35** | The date/time when the printout of the customer order was made. _(Printout date is not stored on the order)_ |
| `ConsigneeReferenceId` | `Int64?` | yes | [BusinessContactReferences](../Common/BusinessContactReference.md) |  | The business key identifier of the customer order's consignee reference. |
| `ConsigneeReference` | `BusinessContactReferences` | no | [BusinessContactReferences](../Common/BusinessContactReference.md) | expandable, since 2.30 | The consignee reference on the customer order. |
| `PrintoutBy` | `String` | no | [ApplicationUsers](../Common/ApplicationUser.md) | max length 20, **deprecated since 2.35** | The user name of the ApplicationUsers that printed the customer order. _(Printout user is not stored on the order)_ |
| `Preliminary` | `Boolean` | no |  |  | Specifies if the customer order is to be considered preliminary. |
| `ConsigneeReferenceName` | `String` | no |  | max length 80 | The consignee reference name of the customer order. |
| `DestinationForDeliveryTerm` | `String` | no |  | max length 80 | The destination for the delivery term. |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](CustomerAccountGroup.md) | **deprecated since 2.30** | The business key identifier of the customer account group of the customer order. _(Replaced by AccountGroupId)_ |
| `SupplierAccountGroupId` | `Int64?` | yes |  | **deprecated since 24.3** | The business key identifier of the supplier account group of the customer order. References a SupplierAccountGroup _(Refer to DeliveryAddress)_ |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the customer order's delivery address. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The delivery address of the customer order. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the customer order's mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The mailing address of the customer order. |
| `InvoiceAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the customer order's invoice address. |
| `InvoiceAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The invoice address of the customer order. |
| `InvoiceStatusPending` | `Boolean` | no |  |  | Specifies if the invoice created for the customer order should start out as pending. |
| `IsPartOfComprehensiveInvoice` | `Boolean` | no |  | **deprecated since 2.41** | Specifies if the customer order is part of a comprehensive invoice. _(Replaced by ComprehensiveInvoiceGroupingMode)_ |
| `ComprehensiveInvoiceGroupingMode` | `Int32` | no |  | enum, since 2.41 | Specifies if the customer order is part of a comprehensive invoice, and how they are grouped. |
| `HasInvoicingCharge` | `Boolean` | no |  |  | Specifies if the customer order involves an invoicing charge. |
| `GoodsAddressNumber` | `String` | no |  | max length 80 | The goods address number of the customer order. |
| `VatNumber` | `String` | no |  | max length 80 | The VAT number of the customer order. |
| `Dock` | `String` | no |  | max length 35 | The dock of the customer order. |
| `FromQuoteNumber` | `String` | no |  | max length 15 | The human readable identifier of the quote that resulted in the customer order. |
| `Status` | `Int32` | no |  | enum | The status of the customer order. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](../Common/CommunicationAddress.md) | collection | The communication addresses registered on the customer order. |
| `PrintProformaInvoiceVia` | `Int32?` | yes |  | enum | The preferred Proforma printout method of the customer. |
| `OrderTypeId` | `Int64?` | yes | [CustomerOrderTypes](CustomerOrderType.md) | since 2.27 | The business key identifier of the customer order's order type. |
| `OrderType` | `CustomerOrderTypes` | no | [CustomerOrderTypes](CustomerOrderType.md) | expandable, since 2.27 | The order type used on the customer order. |
| `IsStockOrder` | `Boolean` | no |  | since 2.30 | Specifies if the customer order is stock order. |
| `ExcludeFromEdi` | `Boolean` | no |  | since 2.30 | Specifies if the customer order will be excluded from EDI. |
| `IncludeInDeliveryAnalysis` | `Boolean?` | yes |  | since 2.30 | Specifies if the customer order will be included in delivery analysis. |
| `PartialDeliveryType` | `Int32` | no |  | enum, since 2.30 | The partial delivery type on the customer order. |
| `DeliveryHorizon` | `TimeSpan?` | yes |  | since 2.30 | The delivery horizon on the customer order. |
| `DeliveryNoteNumberWhenDeliveryPlanning` | `Boolean` | no |  | since 2.30 | Specifies if using delivery note number when delivery planning on the customer order. |
| `AftermarketProductRecordId` | `Int64?` | yes | [ProductRecords](../Inventory/ProductRecord.md) | since 2.30 | The business key identifier of the customer order's aftermarket product record. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](../Purchase/PurchaseOrder.md) | since 2.30 | The business key identifier of the customer order's purchase order. |
| `PurchaseOrder` | `PurchaseOrders` | no | [PurchaseOrders](../Purchase/PurchaseOrder.md) | expandable, since 2.30 | The purchase order on the customer order. |
| `PaymentPlanTemplateId` | `Int64?` | yes | [PaymentPlanTemplates](../Common/PaymentPlanTemplate.md) | since 2.30 | The business key identifier of the customer order's payment plan template. |
| `PaymentPlanTemplate` | `PaymentPlanTemplates` | no | [PaymentPlanTemplates](../Common/PaymentPlanTemplate.md) | expandable, since 2.30 | The payment plan template on the customer order. |
| `UnpaidAdvanceWarningType` | `Int32` | no |  | enum, since 2.30 | The unpaid advance warning type on the customer order. |
| `CreatedFrom` | `Int32` | no |  | enum, since 2.30 | Specifies what the customer order was created from. |
| `ShippingInformationId` | `Int64?` | yes |  | since 2.30 | The business key identifier of the customer order's shipping information. |
| `ShippingInformationRows` | `CustomerOrderShippingInformationRows[]` | no | [CustomerOrderShippingInformationRows](CustomerOrderShippingInformationRow.md) | expandable, collection, since 2.30 | The shipping information rows on the customer order. |
| `ExcludeFromPaymentPlanReconciliation` | `Boolean` | no |  | since 2.30 | Specifies if the customer order is excluded from payment plan reconciliation. |
| `ResetPaymentPlanDifferenceAmount` | `Decimal?` | yes |  | since 2.30 | The reset payment plan difference amount on the customer order. |
| `ResetPaymentPlanDifferenceAmountCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) | since 2.30 | The business key identifier of the customer order's reset payment plan difference amount currency. |
| `ResetPaymentPlanDifferenceAmountCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable, since 2.30 | The reset payment plan difference amount currency on the customer order. |
| `TransferStatus` | `Int32` | no |  | enum, since 2.30 | The transfer status of the customer order. |
| `CreatedInCompanyWithRole` | `Int32?` | yes |  | enum, since 2.30 | The role of the company who created the customer order. |
| `AccountGroupId` | `Int64` | no | [CustomerAccountGroups](CustomerAccountGroup.md) | since 2.30 | The business key identifier of the account group of the customer order. |
| `AccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](CustomerAccountGroup.md) | expandable, since 2.30 | The account group on the customer order. |
| `CategoryString` | `String` | no |  | max length 20, since 2.30 | The category string on the customer order. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](../Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the customer order's currency exchange type. |
| `EditedOrderAmountExcludingVat` | `Decimal?` | yes |  | since 24.8 | The edited order amount excluding VAT for the customer order. |
| `EditedOrderAmountExcludingVatCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) | since 24.8 | The currency of the edited order amount excluding VAT for the customer order. |
| `EditedOrderAmountDiscount` | `Decimal?` | yes |  | since 24.8 | The edited order amount discount in percent for the customer order. |
| `TypeOfOrderAmountEntered` | `Int32?` | yes |  | enum, since 24.8 | The type of edited order value entered on the customer order. |
| `ReasonCodeDebitNoteId` | `Int64?` | yes | [ReasonCodeDebitNotes](../Common/ReasonCodeDebitNote.md) | since 25.6 | The business key identifier of the customer order's reason code debit note. |
| `ReasonCodeDebitNote` | `ReasonCodeDebitNotes` | no | [ReasonCodeDebitNotes](../Common/ReasonCodeDebitNote.md) | expandable, since 25.6 | The reason code debit note on the customer order. |
| `Factoring` | `Boolean` | no |  | since 25.7 | Specifies if factoring is activated for the customer order. |
| `ReferenceCode` | `String` | no |  | max length 100, since 26.5 | The customer's reference code on the customer order. |
| `PickInstructionId` | `Int64?` | yes | [Comments](../Common/Comment.md) | since 26.5 | The business key identifier of the customer order's pick instruction. |
| `PickInstruction` | `Comments` | no | [Comments](../Common/Comment.md) | expandable, since 26.5 | The pick instruction of the customer order. |

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

### SourceOfAlternativeDeliveryAddresses

| Name | Value |
| --- | ---: |
| `CurrentCustomer` | 0 |
| `Customer` | 1 |
| `Supplier` | 2 |
| `Company` | 3 |
| `CurrentSupplier` | 4 |

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

### ComprehensiveInvoiceGroupingMode

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Customer` | 1 |
| `Order` | 2 |
| `DeliveryNote` | 3 |

### Status

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `Registered` | 1 |
| `OrderConfirmationPrinted` | 2 |
| `CanNotConfirmDeliveryTime` | 3 |
| `DeliveryNotePrinted` | 4 |
| `PartiallyDelivered` | 5 |
| `History` | 9 |

### PrintProformaInvoiceVia

| Name | Value |
| --- | ---: |
| `Printer` | 0 |
| `Email` | 1 |
| `Edi` | 2 |
| `None` | 9 |

### PartialDeliveryType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `PerOrder` | 1 |
| `PerRow` | 2 |
| `NoneDelete` | 3 |
| `PerDeliveryDate` | 4 |

### UnpaidAdvanceWarningType

| Name | Value |
| --- | ---: |
| `NoAlert` | 0 |
| `Warning` | 1 |
| `PreventDelivery` | 2 |

### CreatedFrom

| Name | Value |
| --- | ---: |
| `Client` | 0 |
| `M2M` | 1 |
| `EDI` | 2 |
| `DeliverySchedule` | 3 |
| `DeliveryScheduleCallOff` | 4 |

### TransferStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Partial` | 1 |
| `Fully` | 2 |

### CreatedInCompanyWithRole

| Name | Value |
| --- | ---: |
| `ManufacturingCompany` | 0 |
| `SalesCompany` | 1 |

### TypeOfOrderAmountEntered

| Name | Value |
| --- | ---: |
| `Percent` | 1 |
| `Amount` | 2 |


## Referenced by

**Common**

- [Projects](../Common/Project.md) — `CustomerOrder` (expand)
- [Projects](../Common/Project.md) — `CustomerOrderId` (FK)

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `CustomerOrder` (expand)
- [CaseEntry](../Inventory/CaseEntry.md) — `CustomerOrderId` (FK)
- [CaseEntryPartLinks](../Inventory/CasePartLink.md) — `CompensationCustomerOrderId` (FK)
- [Locations](../Inventory/Location.md) — `CustomerOrderId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `CustomerOrder` (expand)
- [ProductRecords](../Inventory/ProductRecord.md) — `CustomerOrderId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `InstallationOrderId` (FK)

**Manufacturing**

- [ManufacturingOrders](../Manufacturing/ManufacturingOrder.md) — `CustomerOrder` (expand)
- [ManufacturingOrders](../Manufacturing/ManufacturingOrder.md) — `CustomerOrderId` (FK)

**Purchase**

- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `CustomerOrderId` (FK)

**Sales**

- [CustomerOrderActivities](CustomerOrderActivity.md) — `OrderId` (FK)
- [CustomerOrderDeliveryRows](CustomerOrderDeliveryRow.md) — `CustomerOrderId` (FK)
- [CustomerOrderInvoices](CustomerOrderInvoice.md) — `BusinessContactOrderId` (FK)
- [CustomerOrderPaymentPlanRows](CustomerOrderPaymentPlanRow.md) — `CustomerOrderId` (FK)
- [CustomerOrderRows](CustomerOrderRow.md) — `ParentOrderId` (FK)
- [CustomerRelationshipManagementActivities](CustomerRelationshipManagementActivity.md) — `OrderId` (FK)
- [InvoiceLogs](InvoiceLog.md) — `CustomerOrderId` (FK)
- [QuoteRows](QuoteRow.md) — `CustomerOrderId` (FK)
- [SalesAgreementBases](SalesAgreementBasis.md) — `CustomerOrderId` (FK)
- [ShipmentInformationSources](ShipmentInformationSource.md) — `CustomerOrderId` (FK)


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
  "InvoiceCustomerId": 0,
  "OrderNumber": null,
  "OrderDate": "0001-01-01T00:00:00+00:00",
  "Rows": null,
  "SellerId": null,
  "ShowPriceInAcknowledgement": false,
  "ShowTotalInAcknowledgement": false,
  "ThirdPartyTrading": false,
  "DeliveryInstruction": null,
  "ActiveDeliveryAddressCustomerId": null,
  "ActiveDeliveryAddressSupplierId": null,
  "ActiveDeliveryAddressCompanyId": null,
  "SourceOfAlternativeDeliveryAddresses": 0,
  "IsCredit": false,
  "InvoiceType": 0,
  "PaymentMethodId": null,
  "PaymentMethod": null,
  "PrintoutTimeStamp": "0001-01-01T00:00:00+00:00",
  "ConsigneeReferenceId": null,
  "ConsigneeReference": null,
  "PrintoutBy": null,
  "Preliminary": false,
  "ConsigneeReferenceName": null,
  "DestinationForDeliveryTerm": null,
  "CustomerAccountGroupId": null,
  "SupplierAccountGroupId": null,
  "DeliveryAddressId": null,
  "DeliveryAddress": null,
  "MailingAddressId": null,
  "MailingAddress": null,
  "InvoiceAddressId": null,
  "InvoiceAddress": null,
  "InvoiceStatusPending": false,
  "IsPartOfComprehensiveInvoice": false,
  "ComprehensiveInvoiceGroupingMode": 0,
  "HasInvoicingCharge": false,
  "GoodsAddressNumber": null,
  "VatNumber": null,
  "Dock": null,
  "FromQuoteNumber": null,
  "Status": 0,
  "CommunicationAddresses": null,
  "PrintProformaInvoiceVia": null,
  "OrderTypeId": null,
  "OrderType": null,
  "IsStockOrder": false,
  "ExcludeFromEdi": false,
  "IncludeInDeliveryAnalysis": null,
  "PartialDeliveryType": 0,
  "DeliveryHorizon": null,
  "DeliveryNoteNumberWhenDeliveryPlanning": false,
  "AftermarketProductRecordId": null,
  "PurchaseOrderId": null,
  "PurchaseOrder": null,
  "PaymentPlanTemplateId": null,
  "PaymentPlanTemplate": null,
  "UnpaidAdvanceWarningType": 0,
  "CreatedFrom": 0,
  "ShippingInformationId": null,
  "ShippingInformationRows": null,
  "ExcludeFromPaymentPlanReconciliation": false,
  "ResetPaymentPlanDifferenceAmount": null,
  "ResetPaymentPlanDifferenceAmountCurrencyId": null,
  "ResetPaymentPlanDifferenceAmountCurrency": null,
  "TransferStatus": 0,
  "CreatedInCompanyWithRole": null,
  "AccountGroupId": 0,
  "AccountGroup": null,
  "CategoryString": null,
  "CurrencyExchangeTypeId": 0,
  "EditedOrderAmountExcludingVat": null,
  "EditedOrderAmountExcludingVatCurrencyId": null,
  "EditedOrderAmountDiscount": null,
  "TypeOfOrderAmountEntered": null,
  "ReasonCodeDebitNoteId": null,
  "ReasonCodeDebitNote": null,
  "Factoring": false,
  "ReferenceCode": null,
  "PickInstructionId": null,
  "PickInstruction": null
}
```
