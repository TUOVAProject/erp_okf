---
type: API Entity
title: CustomerOrderInvoices
description: Represents a customer order invoice.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderInvoice.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderInvoice.html
  title: Monitor API — CustomerOrderInvoice
module: Sales
api_class: CustomerOrderInvoice
doc_name: CustomerOrderInvoices
endpoint: GET /api/v1/Sales/CustomerOrderInvoices
guid: 61435D1A-FCFC-4DA4-B199-03BDA9E30A9B
permission: Show customer orders
introduced_in: '2.33'
property_count: 72
references_out:
- /entities/Common/Address.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Currency.md
- /entities/Common/DeliveryMethod.md
- /entities/Common/DeliveryTerm.md
- /entities/Common/FormReportConfiguration.md
- /entities/Common/PaymentTerm.md
- /entities/Common/Person.md
- /entities/Common/Project.md
- /entities/Common/VatGroup.md
- /entities/Common/Warehouse.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerAccountGroup.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderDeliveryRow.md
referenced_by:
- /entities/Sales/CustomerOrderDeliveryRow.md
- /entities/Sales/SalesAgreementBasis.md
- /entities/Sales/SalesPickingList.md
- /entities/Sales/ShipmentInformationSource.md
---

# CustomerOrderInvoices

Represents a customer order invoice.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `CustomerOrderInvoice`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderInvoices`
- **Required permission:** Show customer orders
- **GUID:** `61435D1A-FCFC-4DA4-B199-03BDA9E30A9B`
- **Introduced in:** 2.33

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer order invoice. |
| `Status` | `Int32` | no |  | enum | The status of the customer order invoice. |
| `DeliveryNoteNumber` | `Int64` | no |  |  | The delivery note number of the customer order invoice. |
| `DeliveryIndex` | `Int32` | no |  |  | The delivery index of the customer order invoice. |
| `OrderDeliveryNumber` | `String` | no |  | max length 18 | The order delivery number of the customer order invoice. |
| `PickingListId` | `Int64?` | yes |  |  | The business key identifier of the picking list of the customer order invoice. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse that the customer order invoice belongs to. |
| `Version` | `Int32` | no |  | since 2.34 | The version of the customer order invoice. |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](/entities/Sales/Customer.md) | since 2.34 | The business key identifier of the customer source of the active delivery address. |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](/entities/Purchase/Supplier.md) | since 2.34 | The business key identifier of the supplier source of the active delivery address. |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  | since 2.34 | The business key identifier of the company source of the active delivery address. |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  | enum, since 2.34 | Specifies the source of the customer order invoice delivery address. |
| `ConsigneeReferenceId` | `Int64?` | yes | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) | since 2.34 | The business key identifier of the consignee reference of the customer order invoice. |
| `ConsigneeReference` | `BusinessContactReferences` | no | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) | expandable, since 2.34 | The consignee reference on the customer order invoice. |
| `ProformaStatus` | `Int32` | no |  | enum, since 2.34 | The proforma status of the customer order invoice. |
| `ProjectId` | `Int64?` | yes | [Projects](/entities/Common/Project.md) | since 2.34 | The business key identifier of project of the customer order invoice. |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](/entities/Common/Address.md) | since 2.34 | The business key identifier of the delivery address of the customer order invoice. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](/entities/Common/Address.md) | expandable, since 2.34 | The delivery address of the customer order invoice. |
| `InvoiceAddressId` | `Int64?` | yes | [Addresses](/entities/Common/Address.md) | since 2.34 | The business key identifier of the invoice address of the customer order invoice. |
| `InvoiceAddress` | `Addresses` | no | [Addresses](/entities/Common/Address.md) | expandable, since 2.34 | The invoice address of the customer order invoice. |
| `OurReferenceId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) | since 2.34 | The business key identifier of our reference for the customer order invoice. Reference Persons |
| `OurReferenceName` | `String` | no |  | max length 80, since 2.34 | The name of our reference for the customer order invoice. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) | since 2.34 | The business key identifier of the customer's reference for the customer order invoice. |
| `BusinessContactReferenceName` | `String` | no |  | max length 80, since 2.34 | The name of the customer's reference for the customer order invoice. |
| `GoodsLabel` | `String` | no |  | max length 80, since 2.34 | The goods label of the customer order invoice. |
| `InvoiceStatusPending` | `Boolean` | no |  | since 2.34 | Specifies if the invoice status is pending on the customer order invoice. |
| `IsPartOfComprehensiveInvoice` | `Boolean` | no |  | **deprecated since 2.41**, since 2.34 | Specifies if the customer order invoice is part of a comprehensive invoice. _(Replaced by ComprehensiveInvoiceGroupingMode)_ |
| `ComprehensiveInvoiceGroupingMode` | `Int32` | no |  | enum, since 2.41 | Specifies if the customer order invoice is part of a comprehensive invoice, and how they are grouped. |
| `HasInvoicingCharge` | `Boolean` | no |  | since 2.34 | Specifies if the customer order invoice involves an invoicing charge. |
| `IsFreeDeliveryMonth` | `Boolean` | no |  | since 2.34 | Specifies if the customer order invoice have a free delivery month. |
| `GoodsAddressNumber` | `String` | no |  | max length 80, since 2.34 | The goods address number of the customer order invoice. |
| `VatNumber` | `String` | no |  | max length 80, since 2.34 | The VAT number of the customer order invoice. |
| `Dock` | `String` | no |  | max length 35, since 2.34 | The dock of the customer order invoice. |
| `DeliveryInstruction` | `String` | no |  | max length 80, since 2.34 | The delivery instruction of the customer order invoice. |
| `InvoicePrintoutMethod` | `Int32?` | yes |  | enum, since 2.34 | Specifies the printout method for the customer order invoice. |
| `PrintProformaInvoiceVia` | `Int32?` | yes |  | enum, since 2.34 | The preferred Proforma printout method of the customer order invoice. |
| `EInvoiceExportMode` | `Int32?` | yes |  | enum, since 2.34 | The preffered electronic invoice export mode to use on this customer order invoice. |
| `Priority` | `Int32` | no |  | since 2.34 | The priority of the customer order invoice. |
| `DirectlyRegistered` | `Boolean` | no |  | since 2.34 | Specifies if the customer order invoice is directly registered. |
| `PartialInvoiceType` | `Int32?` | yes |  | enum, since 2.34 | The partial invoice type of the customer order invoice. |
| `FormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](/entities/Common/FormReportConfiguration.md) | since 2.34 | The business key identifier of the customer order invoice's form report configuration. |
| `DeliveryNoteCreationDate` | `DateTimeOffset?` | yes |  | since 2.34 | The delivery note creation date on the customer order invoice. |
| `ExcludeFromEdi` | `Boolean` | no |  | since 2.34 | Specifies if the customer order invoice will be excluded from EDI. |
| `SellerId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) | since 2.34 | The business key identifier of the seller on the customer order invoice. |
| `ShippingInformationId` | `Int64?` | yes |  | since 2.34 | The business key identifier of the shipping information on the customer order invoice. |
| `ProformaNumber` | `Int64?` | yes |  | since 2.34 | The proforma number of the customer order invoice. |
| `ProformaDate` | `DateTimeOffset?` | yes |  | since 2.34 | The proforma date of the customer order invoice. |
| `DestinationForDeliveryTerm` | `String` | no |  | max length 35, since 2.34 | The destination for delivery term for the customer order invoice. |
| `CandidateDebitInvoiceId` | `Int64?` | yes |  | since 2.34 | The business key identifier to the accounts receivable linked to the debit invoice candidate for this customer order invoice. References AccountsReceivable. |
| `ConsigneeReferenceName` | `String` | no |  | max length 80, since 2.34 | The consignee reference name of the customer order invoice. |
| `LedgerId` | `Int64?` | yes |  | since 2.34 | The business key identifier to the ledger's accounts receivable of the customer order invoice. References AccountsReceivable. |
| `BusinessContactOrderId` | `Int64` | no | [CustomerOrders](/entities/Sales/CustomerOrder.md) | since 2.34 | The business key identifier to the customre order of the customer order invoice. References CustomerOrders . |
| `InvoiceBusinessContactId` | `Int64` | no | [Customers](/entities/Sales/Customer.md) | since 2.34 | The business key identifier to the customer on the customer order invoice. References Customers . |
| `AccountGroupId` | `Int64` | no | [CustomerAccountGroups](/entities/Sales/CustomerAccountGroup.md) | since 2.34 | The business key identifier of the account group of the customer order invoice. |
| `AccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](/entities/Sales/CustomerAccountGroup.md) | expandable, since 2.34 | The account group on the customer order invoice. |
| `VatGroupId` | `Int64` | no | [VatGroups](/entities/Common/VatGroup.md) | since 2.34 | The business key identifier of the VAT group that applies for the customer order invoice. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](/entities/Common/PaymentTerm.md) | since 2.34 | The business key identifier of the payment term of the customer order invoice. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](/entities/Common/PaymentTerm.md) | expandable, since 2.34 | The payment term of the customer order invoice. |
| `PaymentTermDescription` | `String` | no |  | max length 35, since 2.34 | The payment term description of the customer order invoice. |
| `GracePeriodInDays` | `Int32?` | yes |  | since 2.34 | The grace period in days of the customer order invoice. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](/entities/Common/DeliveryMethod.md) | since 2.34 | The business key identifier of the delivery method of the customer order invoice. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](/entities/Common/DeliveryTerm.md) | since 2.34 | The business key identifier of the delivery term of the customer order invoices. |
| `DeliveryTermDescription` | `String` | no |  | max length 35, since 2.34 | The delivery term description of the customer order invoice. |
| `DeliveryMethodDescription` | `String` | no |  | max length 35, since 2.34 | The delivery method description of the customer order invoice. |
| `ShipmentPayer` | `Int32` | no |  | enum, since 2.34 | Specifies who is responsible for the shipment payment for the customer order invoce. |
| `DeliveryRows` | `CustomerOrderDeliveryRows[]` | no | [CustomerOrderDeliveryRows](/entities/Sales/CustomerOrderDeliveryRow.md) | expandable, collection, since 2.36 | The customer order delivery rows. CustomerOrderDeliveryRows |
| `InvoiceType` | `Int32` | no |  | enum, since 2.53 | Invoice type of customer order invoice |
| `EditedOrderAmountExcludingVat` | `Decimal?` | yes |  | since 24.8 | The edited order amount excluding VAT for the customer order invoice. |
| `EditedOrderAmountExcludingVatCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) | since 24.8 | The currency of the edited order amount excluding VAT for the customer order invoice. |
| `EditedOrderAmountDiscount` | `Decimal?` | yes |  | since 24.8 | The edited order amount discount in percent for the customer order invoice. |
| `TypeOfOrderAmountEntered` | `Int32?` | yes |  | enum, since 24.8 | The type of edited order value entered on the customer order invoice. |
| `Factoring` | `Boolean` | no |  | since 25.7 | Specifies if factoring is activated for the customer order invoice. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Canceled` | 0 |
| `Registered` | 1 |
| `Preliminary` | 2 |
| `Waiting` | 3 |
| `InvoiceApproved` | 8 |
| `InvoicePrinted` | 9 |

### SourceOfAlternativeDeliveryAddresses

| Name | Value |
| --- | ---: |
| `CurrentCustomer` | 0 |
| `Customer` | 1 |
| `Supplier` | 2 |
| `Company` | 3 |
| `CurrentSupplier` | 4 |

### ProformaStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `ApprovedForPrint` | 1 |
| `Printed` | 2 |

### ComprehensiveInvoiceGroupingMode

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Customer` | 1 |
| `Order` | 2 |
| `DeliveryNote` | 3 |

### InvoicePrintoutMethod

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

### EInvoiceExportMode

| Name | Value |
| --- | ---: |
| `No` | 0 |
| `Yes` | 1 |
| `YesIncludingPrintoutOrEmail` | 2 |
| `SaveToFile` | 3 |

### PartialInvoiceType

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `InAdvance` | 1 |
| `Delivery` | 2 |
| `InArrears` | 3 |
| `Text` | 4 |

### ShipmentPayer

| Name | Value |
| --- | ---: |
| `BuyerPays` | 1 |
| `SellerPays` | 2 |
| `OtherPayer` | 3 |
| `Incoterms` | 4 |

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

### TypeOfOrderAmountEntered

| Name | Value |
| --- | ---: |
| `Percent` | 1 |
| `Amount` | 2 |


## Referenced by

**Sales**

- [CustomerOrderDeliveryRows](/entities/Sales/CustomerOrderDeliveryRow.md) — `InvoiceId` (FK)
- [SalesAgreementBases](/entities/Sales/SalesAgreementBasis.md) — `InvoiceId` (FK)
- [SalesPickingLists](/entities/Sales/SalesPickingList.md) — `CustomerOrderInvoices` (expand)
- [ShipmentInformationSources](/entities/Sales/ShipmentInformationSource.md) — `CustomerOrderInvoiceId` (FK)


## Example

```json
{
  "Id": 0,
  "Status": 0,
  "DeliveryNoteNumber": 0,
  "DeliveryIndex": 0,
  "OrderDeliveryNumber": null,
  "PickingListId": null,
  "WarehouseId": 0,
  "Version": 0,
  "ActiveDeliveryAddressCustomerId": null,
  "ActiveDeliveryAddressSupplierId": null,
  "ActiveDeliveryAddressCompanyId": null,
  "SourceOfAlternativeDeliveryAddresses": 0,
  "ConsigneeReferenceId": null,
  "ConsigneeReference": null,
  "ProformaStatus": 0,
  "ProjectId": null,
  "DeliveryAddressId": null,
  "DeliveryAddress": null,
  "InvoiceAddressId": null,
  "InvoiceAddress": null,
  "OurReferenceId": null,
  "OurReferenceName": null,
  "BusinessContactReferenceId": null,
  "BusinessContactReferenceName": null,
  "GoodsLabel": null,
  "InvoiceStatusPending": false,
  "IsPartOfComprehensiveInvoice": false,
  "ComprehensiveInvoiceGroupingMode": 0,
  "HasInvoicingCharge": false,
  "IsFreeDeliveryMonth": false,
  "GoodsAddressNumber": null,
  "VatNumber": null,
  "Dock": null,
  "DeliveryInstruction": null,
  "InvoicePrintoutMethod": null,
  "PrintProformaInvoiceVia": null,
  "EInvoiceExportMode": null,
  "Priority": 0,
  "DirectlyRegistered": false,
  "PartialInvoiceType": null,
  "FormReportConfigurationId": null,
  "DeliveryNoteCreationDate": null,
  "ExcludeFromEdi": false,
  "SellerId": null,
  "ShippingInformationId": null,
  "ProformaNumber": null,
  "ProformaDate": null,
  "DestinationForDeliveryTerm": null,
  "CandidateDebitInvoiceId": null,
  "ConsigneeReferenceName": null,
  "LedgerId": null,
  "BusinessContactOrderId": 0,
  "InvoiceBusinessContactId": 0,
  "AccountGroupId": 0,
  "AccountGroup": null,
  "VatGroupId": 0,
  "PaymentTermId": null,
  "PaymentTerm": null,
  "PaymentTermDescription": null,
  "GracePeriodInDays": null,
  "DeliveryMethodId": null,
  "DeliveryTermId": null,
  "DeliveryTermDescription": null,
  "DeliveryMethodDescription": null,
  "ShipmentPayer": 0,
  "DeliveryRows": null,
  "InvoiceType": 0,
  "EditedOrderAmountExcludingVat": null,
  "EditedOrderAmountExcludingVatCurrencyId": null,
  "EditedOrderAmountDiscount": null,
  "TypeOfOrderAmountEntered": null,
  "Factoring": false
}
```
