---
type: API Entity
title: PurchaseOrders
description: Represents a purchase order.
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrder.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrder.html
  title: Monitor API — PurchaseOrder
module: Purchase
api_class: PurchaseOrder
doc_name: PurchaseOrders
endpoint: GET /api/v1/Purchase/PurchaseOrders
guid: 3A8DD78D-902D-4E50-8DE6-C0AEE4CE582E
permission: Show purchase orders
introduced_in: '2.26'
property_count: 79
references_out:
- /entities/Common/Address.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/CommunicationAddress.md
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/DeliveryMethod.md
- /entities/Common/DeliveryTerm.md
- /entities/Common/PaymentTerm.md
- /entities/Common/Person.md
- /entities/Common/VatGroup.md
- /entities/Common/Warehouse.md
- /entities/Purchase/PackingTerm.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Purchase/PurchaseOrderType.md
- /entities/Purchase/Supplier.md
- /entities/Purchase/SupplierAccountGroup.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CasePartLink.md
- /entities/Inventory/Location.md
- /entities/Inventory/ProductRecord.md
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderDelivery.md
- /entities/Purchase/PurchaseOrderDeliveryRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/CustomerOrder.md
---

# PurchaseOrders

Represents a purchase order.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `PurchaseOrder`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrders`
- **Required permission:** Show purchase orders
- **GUID:** `3A8DD78D-902D-4E50-8DE6-C0AEE4CE582E`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the purchase order. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](../Common/PaymentTerm.md) |  | The business key identifier of the payment term of the purchase order. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](../Common/PaymentTerm.md) | expandable | The payment term of the purchase order. |
| `PaymentTermDescription` | `String` | no |  | max length 35 | The payment term description of the purchase order. |
| `GracePeriodInDays` | `Int32?` | yes |  |  | The purchase order's grace period in days. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](../Common/DeliveryMethod.md) |  | The business key identifier of the purchase order's delivery method. |
| `DeliveryMethod` | `DeliveryMethods` | no | [DeliveryMethods](../Common/DeliveryMethod.md) | expandable, since 2.30 | The purchase order's delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](../Common/DeliveryTerm.md) |  | The business key identifier of the purchase order's delivery term. |
| `DeliveryTerm` | `DeliveryTerms` | no | [DeliveryTerms](../Common/DeliveryTerm.md) | expandable, since 2.30 | The purchase order's delivery term. |
| `DeliveryTermDescription` | `String` | no |  | max length 35 | The delivery term description of the purchase order. |
| `DeliveryMethodDescription` | `String` | no |  | max length 35 | The delivery method description of the purchase order. |
| `ShipmentPayer` | `Int32` | no |  | enum | Specifies who is responsible for the shipment payment for the purchase order. |
| `BusinessContactOrderNumber` | `String` | no |  | max length 30 | The supplier's order number for the purchase order. |
| `OurReferenceId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of our reference for the purchase order. Reference Persons |
| `OurReference` | `Persons` | no | [Persons](../Common/Person.md) | expandable, since 2.30 | Our reference for the purchase order. |
| `OurReferenceName` | `String` | no |  | max length 80 | The name of our reference for the purchase order. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](../Common/BusinessContactReference.md) |  | The business key identifier of the supplier's reference for the purchase order. |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](../Common/BusinessContactReference.md) | expandable, since 2.30 | The supplier's reference for the purchase order. |
| `BusinessContactReferenceName` | `String` | no |  | max length 80 | The name of the supplier's reference for the purchase order. |
| `GoodsLabel` | `String` | no |  | max length 80 | The goods label of the purchase order. |
| `CurrencyId` | `Int64` | no | [Currencies](../Common/Currency.md) |  | The business key identifier of the currency of the purchase order. |
| `Currency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable, since 2.30 | The currency for the purchase order. |
| `VatGroupId` | `Int64` | no | [VatGroups](../Common/VatGroup.md) |  | The business key identifier of the VAT group that applies for the purchase order. |
| `VatGroup` | `VatGroups` | no | [VatGroups](../Common/VatGroup.md) | expandable, since 2.30 | The VAT group that applies for the purchase order. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse that the purchase order belongs to. |
| `Warehouse` | `Warehouses` | no | [Warehouses](../Common/Warehouse.md) | expandable, since 2.30 | The warehouse that the purchase order belongs to. |
| `Priority` | `Int32` | no |  |  | The priority of the purchase order. |
| `ProjectId` | `Int64?` | yes |  |  | The business key identifier of the purchase order's project. |
| `SendMethod` | `Int32` | no |  | enum | Specifies the printout method for the purchase order. |
| `InvoicePrintoutMethod` | `Int32` | no |  | enum | Specifies the printout method that should be used for invoices. |
| `InternalCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the purchase order's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The internal comment of the purchase order. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the purchase order's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The external comment of the purchase order. |
| `TransportTime` | `Int32?` | yes |  |  | The transport time of the purchase order in workdays. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the purchase order. |
| `Version` | `Int32` | no |  |  | The version of the purchase order. |
| `UseForwardRate` | `Boolean` | no |  |  | Specifies if forward rate should apply for the purchase order. |
| `ExchangeRate` | `Decimal` | no |  |  | Specifies the exchange rate to use for the purchase order. |
| `OrderAmount` | `Decimal` | no |  | **deprecated since 2.36** | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `OrderAmountInCompanyCurrency` | `Decimal` | no |  | **deprecated since 2.36** | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `AgentSupplierId` | `Int64?` | yes | [Suppliers](Supplier.md) |  | The business key identifier of the agent that the purchase order belongs to. |
| `SuppliersQuoteNumber` | `String` | no |  | max length 30 | The readable supplier's quote number. |
| `IsStockOrder` | `Boolean` | no |  |  | Specifies if the purchase order is a Stock order. |
| `IsConfirmed` | `Boolean` | no |  |  | Specifies if the order is Confirmed. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](../Sales/CustomerOrder.md) |  | The business key identifier of the customer order. |
| `OrderNumber` | `String` | no |  | unique, max length 15 | The human readable identifier of the purchase order. |
| `OrderDate` | `DateTimeOffset` | no |  |  | The order date of the purchase order. |
| `Rows` | `PurchaseOrderRows[]` | no | [PurchaseOrderRows](PurchaseOrderRow.md) | expandable, collection | The rows of the purchase order. |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](../Sales/Customer.md) |  | The business key identifier of the customer source of the active delivery address. |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](Supplier.md) |  | The business key identifier of the supplier source of the active delivery address. |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  |  | The business key identifier of the company source of the active delivery address. |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  | enum | Specifies the source of the purchase order delivery address. |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the purchase order's delivery address. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The delivery address of the purchase order. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the purchase order's mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The mailing address of the purchase order. |
| `GoodsAddressNumber` | `String` | no |  | max length 80 | The goods address number of the purchase order. |
| `FromInquiryNumber` | `String` | no |  | max length 15 | The human readable identifier of the inquiry that resulted in the purchase order. |
| `Status` | `Int32` | no |  | enum | The status of the purchase order. |
| `InquiryId` | `Int64?` | yes |  | since 2.30 | The business key identifier of the purchase order's inquiry. |
| `PackingTermId` | `Int64?` | yes | [PackingTerms](PackingTerm.md) | since 2.30 | The business key identifier of the purchase order's packing term. |
| `PackingTerm` | `PackingTerms` | no | [PackingTerms](PackingTerm.md) | expandable, since 2.30 | The packing term of the purchase order. |
| `PackingTermDescription` | `String` | no |  | max length 35, since 2.30 | The packing term description of the purchase order. |
| `ShowPriceInFormReport` | `Boolean` | no |  | since 2.30 | Specifies if the purchase order shows price in form report. |
| `ShowTotalInFormReport` | `Boolean` | no |  | since 2.30 | Specifies if the purchase order shows total in form report. |
| `IsCredit` | `Boolean` | no |  | since 2.30 | Specifies if the purchase order is a credit order. |
| `CausingCreditPurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](PurchaseOrder.md) | since 2.30 | The business key identifier of the purchase order which caused this credit purchase order to be created. |
| `BusinessContactId` | `Int64` | no | [Suppliers](Supplier.md) | since 2.30 | The business key identifier of the purchase order's supplier. |
| `InvoiceBusinessContactId` | `Int64` | no | [Suppliers](Supplier.md) | since 2.30 | The business key identifier of the purchase order's supplier sending the invoice. |
| `OrderTypeId` | `Int64` | no | [PurchaseOrderTypes](PurchaseOrderType.md) | since 2.30 | The business key identifier of the purchase order's type. |
| `OrderType` | `PurchaseOrderTypes` | no | [PurchaseOrderTypes](PurchaseOrderType.md) | expandable, since 2.30 | The order type of the purchase order. |
| `AccountGroupId` | `Int64` | no | [SupplierAccountGroups](SupplierAccountGroup.md) | since 2.30 | The business key identifier of the purchase order's account group. |
| `AccountGroup` | `SupplierAccountGroups` | no | [SupplierAccountGroups](SupplierAccountGroup.md) | expandable, since 2.30 | The account group of the purchase order. |
| `CategoryString` | `String` | no |  | max length 15, since 2.30 | The category string of the purchase order. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](../Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the purchase order's currency exchange type. |
| `DestinationForDeliveryTerm` | `String` | no |  | max length 35, since 23.9 | The destination for the delivery term. |
| `TransportDistance` | `Int32?` | yes |  | since 26.6 | The transport distance of the purchase order in kilometres. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](../Common/CommunicationAddress.md) | expandable, collection, since 24.3 | The communication addresses of the purchase order. |

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

### Status

| Name | Value |
| --- | ---: |
| `PendingAuthorization` | 0 |
| `Registered` | 1 |
| `PurchaseOrderPrinted` | 2 |
| `PartiallyDelivered` | 5 |
| `Declined` | 8 |
| `History` | 9 |


## Referenced by

**Accounting**

- [AccountsPayables](../Accounting/AccountsPayable.md) — `PurchaseOrderId` (FK)

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `PurchaseOrder` (expand)
- [CaseEntry](../Inventory/CaseEntry.md) — `PurchaseOrderId` (FK)
- [CaseEntryPartLinks](../Inventory/CasePartLink.md) — `CompensationPurchaseOrderId` (FK)
- [Locations](../Inventory/Location.md) — `PurchaseOrderId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `PurchaseOrderId` (FK)

**Purchase**

- [InquiryRows](InquiryRow.md) — `PurchaseOrderId` (FK)
- [PurchaseOrderDeliveries](PurchaseOrderDelivery.md) — `PurchaseOrderId` (FK)
- [PurchaseOrderDeliveryRows](PurchaseOrderDeliveryRow.md) — `PurchaseOrderId` (FK)
- [PurchaseOrderRows](PurchaseOrderRow.md) — `ParentOrderId` (FK)
- [PurchaseOrders](PurchaseOrder.md) — `CausingCreditPurchaseOrderId` (FK)

**Sales**

- [CustomerOrders](../Sales/CustomerOrder.md) — `PurchaseOrder` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `PurchaseOrderId` (FK)


## Example

```json
{
  "Id": 0,
  "PaymentTermId": null,
  "PaymentTerm": null,
  "PaymentTermDescription": null,
  "GracePeriodInDays": null,
  "DeliveryMethodId": null,
  "DeliveryMethod": null,
  "DeliveryTermId": null,
  "DeliveryTerm": null,
  "DeliveryTermDescription": null,
  "DeliveryMethodDescription": null,
  "ShipmentPayer": 0,
  "BusinessContactOrderNumber": null,
  "OurReferenceId": null,
  "OurReference": null,
  "OurReferenceName": null,
  "BusinessContactReferenceId": null,
  "BusinessContactReference": null,
  "BusinessContactReferenceName": null,
  "GoodsLabel": null,
  "CurrencyId": 0,
  "Currency": null,
  "VatGroupId": 0,
  "VatGroup": null,
  "WarehouseId": 0,
  "Warehouse": null,
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
  "AgentSupplierId": null,
  "SuppliersQuoteNumber": null,
  "IsStockOrder": false,
  "IsConfirmed": false,
  "CustomerOrderId": null,
  "OrderNumber": null,
  "OrderDate": "0001-01-01T00:00:00+00:00",
  "Rows": null,
  "ActiveDeliveryAddressCustomerId": null,
  "ActiveDeliveryAddressSupplierId": null,
  "ActiveDeliveryAddressCompanyId": null,
  "SourceOfAlternativeDeliveryAddresses": 0,
  "DeliveryAddressId": null,
  "DeliveryAddress": null,
  "MailingAddressId": null,
  "MailingAddress": null,
  "GoodsAddressNumber": null,
  "FromInquiryNumber": null,
  "Status": 0,
  "InquiryId": null,
  "PackingTermId": null,
  "PackingTerm": null,
  "PackingTermDescription": null,
  "ShowPriceInFormReport": false,
  "ShowTotalInFormReport": false,
  "IsCredit": false,
  "CausingCreditPurchaseOrderId": null,
  "BusinessContactId": 0,
  "InvoiceBusinessContactId": 0,
  "OrderTypeId": 0,
  "OrderType": null,
  "AccountGroupId": 0,
  "AccountGroup": null,
  "CategoryString": null,
  "CurrencyExchangeTypeId": 0,
  "DestinationForDeliveryTerm": null,
  "TransportDistance": null,
  "CommunicationAddresses": null
}
```
