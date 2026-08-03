---
type: API Entity
title: BusinessContactReferences
description: Represents a queryable business contact reference.
resource: https://api.monitor.se/api/Monitor.API.Common.BusinessContactReference.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.BusinessContactReference.html
  title: Monitor API — BusinessContactReference
module: Common
api_class: BusinessContactReference
doc_name: BusinessContactReferences
endpoint: GET /api/v1/Common/BusinessContactReferences
guid: 6D7D358E-84D3-41DE-87D9-0A505EE16983
introduced_in: '2.18'
property_count: 14
references_out:
- /entities/Common/Comment.md
referenced_by:
- /entities/Common/DeliveryAddress.md
- /entities/Common/Project.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/ProductRecord.md
- /entities/Purchase/BlanketOrderPurchase.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/Supplier.md
- /entities/Sales/BlanketOrderSales.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/CustomerRelationshipManagementActivity.md
- /entities/Sales/Quote.md
- /entities/Sales/SalesAgreement.md
---

# BusinessContactReferences

Represents a queryable business contact reference.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `BusinessContactReference`
- **Endpoint:** `GET /api/v1/Common/BusinessContactReferences`
- **GUID:** `6D7D358E-84D3-41DE-87D9-0A505EE16983`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business contact reference. |
| `Name` | `String` | no |  | max length 40 | The name of the business contact reference. |
| `ExtraInformation1` | `String` | no |  | max length 80 | The first extra information field of the business contact reference. |
| `ExtraInformation2` | `String` | no |  | max length 80 | The second extra information field of the business contact reference. |
| `ExtraInformation3` | `String` | no |  | max length 80 | The third extra information field of the business contact reference. |
| `Category` | `String` | no |  | max length 20 | The category of the business contact reference. |
| `Note` | `String` | no |  | max length 80 | Any extra notes regarding the business contact reference. |
| `CommentId` | `Int64?` | yes | [Comments](Comment.md) |  | The business key identifier of the comment that is linked to the business contact reference. References Comments . |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The comment that is linked to the the business contact reference. |
| `CellPhoneNumber` | `String` | no |  |  | The value of the communication address. |
| `PhoneNumber` | `String` | no |  |  | The value of the communication address. |
| `EmailAddress` | `String` | no |  |  | The value of the communication address. |
| `FaxNumber` | `String` | no |  |  | The value of the communication address. |
| `Code` | `String` | no |  | max length 40, since 26.6 | The code / number of the business contact reference. |

## Referenced by

**Common**

- [DeliveryAddresses](DeliveryAddress.md) — `ConsigneeReferenceId` (FK)
- [Projects](Project.md) — `CustomerReference` (expand)
- [Projects](Project.md) — `CustomerReferenceId` (FK)

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `ContactReferenceId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `BusinessContactReferenceId` (FK)

**Purchase**

- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `BusinessContactReference` (expand)
- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `BusinessContactReferenceId` (FK)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `BusinessContactReference` (expand)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `BusinessContactReferenceId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `DefaultReference` (expand)
- [Suppliers](../Purchase/Supplier.md) — `DefaultReferenceId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `References` (expand)

**Sales**

- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `BusinessContactReference` (expand)
- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `BusinessContactReferenceId` (FK)
- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `BusinessContactReferenceId` (FK)
- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `ConsigneeReference` (expand)
- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `ConsigneeReferenceId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `BusinessContactReferenceId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `ConsigneeReference` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `ConsigneeReferenceId` (FK)
- [CustomerRelationshipManagementActivities](../Sales/CustomerRelationshipManagementActivity.md) — `BusinessContactReference` (expand)
- [CustomerRelationshipManagementActivities](../Sales/CustomerRelationshipManagementActivity.md) — `BusinessContactReferenceId` (FK)
- [Customers](../Sales/Customer.md) — `DefaultReference` (expand)
- [Customers](../Sales/Customer.md) — `DefaultReferenceId` (FK)
- [Customers](../Sales/Customer.md) — `References` (expand)
- [Quotes](../Sales/Quote.md) — `BusinessContactReferenceId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `BusinessContactReferenceId` (FK)


## Example

```json
{
  "Id": 0,
  "Name": null,
  "ExtraInformation1": null,
  "ExtraInformation2": null,
  "ExtraInformation3": null,
  "Category": null,
  "Note": null,
  "CommentId": null,
  "Comment": null,
  "CellPhoneNumber": null,
  "PhoneNumber": null,
  "EmailAddress": null,
  "FaxNumber": null,
  "Code": null
}
```
