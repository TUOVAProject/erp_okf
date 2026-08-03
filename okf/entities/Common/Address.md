---
type: API Entity
title: Addresses
description: Represents a queryable address.
resource: https://api.monitor.se/api/Monitor.API.Common.Address.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Address.html
  title: Monitor API — Address
module: Common
api_class: Address
doc_name: Addresses
endpoint: GET /api/v1/Common/Addresses
guid: ED951587-26A0-4BC8-9315-8FA5B9809546
introduced_in: '2.18'
property_count: 15
references_out:
- /entities/Common/Country.md
- /entities/Common/LanguageCode.md
referenced_by:
- /entities/Accounting/BankAccount.md
- /entities/Common/BusinessContactBankAccount.md
- /entities/Common/DeliveryAddress.md
- /entities/Common/Person.md
- /entities/Inventory/ProductRecord.md
- /entities/Purchase/BlanketOrderPurchase.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/Supplier.md
- /entities/Sales/BlanketOrderSales.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/Quote.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/Shipment.md
---

# Addresses

Represents a queryable address.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `Address`
- **Endpoint:** `GET /api/v1/Common/Addresses`
- **GUID:** `ED951587-26A0-4BC8-9315-8FA5B9809546`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the address. |
| `Addressee` | `String` | no |  | max length 100 | The addressee of the address. |
| `Field1` | `String` | no |  | max length 50 | The first field of the address. |
| `Field2` | `String` | no |  | max length 50 | The second field of the address. |
| `Field3` | `String` | no |  | max length 50 | The third field of the address. |
| `Field4` | `String` | no |  | max length 50 | The fourth field of the address. |
| `Field5` | `String` | no |  | max length 50 | The fifth field of the address. |
| `Locality` | `String` | no |  | max length 50 | The locality of the address. |
| `Region` | `String` | no |  | max length 50 | The region of the address. |
| `PostalCode` | `String` | no |  | max length 10 | The postal code of the address. |
| `AddressFormatType` | `Int32` | no |  | enum | The format type of the address. |
| `CountryId` | `Int64` | no | [Countries](Country.md) |  | References Countries . |
| `LanguageId` | `Int64` | no | [LanguageCodes](LanguageCode.md) |  | The business key identifier of the language code. References LanguageCodes . |
| `FormReportTranslationGroupId` | `Int64` | no |  |  | The business key identifier of the form report translation group. References FormReportTranslationGroup. |
| `PostalCodeId` | `Int64?` | yes |  | **deprecated since 2.44** | The business key identifier of the postal code. References PostalCode. _(Unavailable)_ |

## Enumerations

### AddressFormatType

| Name | Value |
| --- | ---: |
| `Generic` | 0 |
| `PostalCodeCity` | 1 |
| `CityStatePostalCode` | 2 |
| `CityPostalCodeTwoRows` | 3 |
| `CityProvinsPostalCode` | 4 |


## Referenced by

**Accounting**

- [BankAccounts](../Accounting/BankAccount.md) — `BankAddressId` (FK)

**Common**

- [BusinessContactBankAccounts](BusinessContactBankAccount.md) — `BankAddress` (expand)
- [BusinessContactBankAccounts](BusinessContactBankAccount.md) — `BankAddressId` (FK)
- [DeliveryAddresses](DeliveryAddress.md) — `AddressId` (FK)
- [Persons](Person.md) — `Address` (expand)
- [Persons](Person.md) — `AddressId` (FK)

**Inventory**

- [ProductRecords](../Inventory/ProductRecord.md) — `DeliveryAddress` (expand)

**Purchase**

- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `MailingAddress` (expand)
- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `MailingAddressId` (FK)
- [Inquiries](../Purchase/Inquiry.md) — `DeliveryAddress` (expand)
- [Inquiries](../Purchase/Inquiry.md) — `DeliveryAddressId` (FK)
- [Inquiries](../Purchase/Inquiry.md) — `MailingAddress` (expand)
- [Inquiries](../Purchase/Inquiry.md) — `MailingAddressId` (FK)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `DeliveryAddress` (expand)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `DeliveryAddressId` (FK)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `MailingAddress` (expand)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `MailingAddressId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `MailingAddress` (expand)
- [Suppliers](../Purchase/Supplier.md) — `MailingAddressId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `VisitingAddress` (expand)
- [Suppliers](../Purchase/Supplier.md) — `VisitingAddressId` (FK)

**Sales**

- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `MailingAddress` (expand)
- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `MailingAddressId` (FK)
- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `DeliveryAddress` (expand)
- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `DeliveryAddressId` (FK)
- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `InvoiceAddress` (expand)
- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `InvoiceAddressId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `DeliveryAddress` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `DeliveryAddressId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `InvoiceAddress` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `InvoiceAddressId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `MailingAddress` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `MailingAddressId` (FK)
- [Customers](../Sales/Customer.md) — `InvoiceAddress` (expand)
- [Customers](../Sales/Customer.md) — `InvoiceAddressId` (FK)
- [Customers](../Sales/Customer.md) — `MailingAddress` (expand)
- [Customers](../Sales/Customer.md) — `MailingAddressId` (FK)
- [Customers](../Sales/Customer.md) — `VisitingAddress` (expand)
- [Customers](../Sales/Customer.md) — `VisitingAddressId` (FK)
- [Quotes](../Sales/Quote.md) — `DeliveryAddress` (expand)
- [Quotes](../Sales/Quote.md) — `DeliveryAddressId` (FK)
- [Quotes](../Sales/Quote.md) — `MailingAddress` (expand)
- [Quotes](../Sales/Quote.md) — `MailingAddressId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `DeliveryAddress` (expand)
- [SalesAgreements](../Sales/SalesAgreement.md) — `DeliveryAddressId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `MailingAddress` (expand)
- [SalesAgreements](../Sales/SalesAgreement.md) — `MailingAddressId` (FK)
- [Shipments](../Sales/Shipment.md) — `FreightPayerAddress` (expand)
- [Shipments](../Sales/Shipment.md) — `FreightPayerAddressId` (FK)
- [Shipments](../Sales/Shipment.md) — `OurInvoiceAddress` (expand)
- [Shipments](../Sales/Shipment.md) — `OurInvoiceAdressId` (FK)
- [Shipments](../Sales/Shipment.md) — `OurPickUpAddress` (expand)
- [Shipments](../Sales/Shipment.md) — `OurPickUpAddressId` (FK)
- [Shipments](../Sales/Shipment.md) — `RecipientAdress` (expand)
- [Shipments](../Sales/Shipment.md) — `RecipientAdressId` (FK)
- [Shipments](../Sales/Shipment.md) — `RecipientInvoiceAddress` (expand)
- [Shipments](../Sales/Shipment.md) — `RecipientInvoiceAddressId` (FK)


## Example

```json
{
  "Id": 0,
  "Addressee": null,
  "Field1": null,
  "Field2": null,
  "Field3": null,
  "Field4": null,
  "Field5": null,
  "Locality": null,
  "Region": null,
  "PostalCode": null,
  "AddressFormatType": 0,
  "CountryId": 0,
  "LanguageId": 0,
  "FormReportTranslationGroupId": 0,
  "PostalCodeId": null
}
```
