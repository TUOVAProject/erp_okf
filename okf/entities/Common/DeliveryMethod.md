---
type: API Entity
title: DeliveryMethods
description: Represents a queryable delivery method.
resource: https://api.monitor.se/api/Monitor.API.Common.DeliveryMethod.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.DeliveryMethod.html
  title: Monitor API — DeliveryMethod
module: Common
api_class: DeliveryMethod
doc_name: DeliveryMethods
endpoint: GET /api/v1/Common/DeliveryMethods
guid: 5B0E2E18-673B-44DE-9321-281F6A5BF1A7
permission: Show terms
introduced_in: '2.18'
property_count: 9
references_out:
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Common/DeliveryAddressWarehouseInformation.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderInvoice.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/Quote.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/Shipment.md
- /entities/Sales/ShipmentCustoms.md
---

# DeliveryMethods

Represents a queryable delivery method.

- **Module:** [Common](/modules/Common.md)
- **API class:** `DeliveryMethod`
- **Endpoint:** `GET /api/v1/Common/DeliveryMethods`
- **Required permission:** Show terms
- **GUID:** `5B0E2E18-673B-44DE-9321-281F6A5BF1A7`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the delivery method. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the delivery method is the default method. |
| `Number` | `Int64` | no |  |  | The delivery method number. |
| `Description` | `String` | no |  |  | The translated description of the delivery method. |
| `SupplierId` | `Int64?` | yes | [Suppliers](/entities/Purchase/Supplier.md) |  | The business key identifier of the delivery method supplier. References Suppliers . |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |
| `ShippingServiceId` | `Int64?` | yes |  |  | The business key identifier of the delivery method shipping service. References ShippingService. |
| `ShippingTemplateId` | `Int64?` | yes |  |  | The business key identifier of the delivery method shipping template. References ShippingTemplate. |
| `Code` | `String` | no |  | max length 15, since 24.8 | The code of the delivery method. |

## Referenced by

**Common**

- [DeliveryAddressWarehouseInformations](/entities/Common/DeliveryAddressWarehouseInformation.md) — `DeliveryMethodId` (FK)

**Purchase**

- [Inquiries](/entities/Purchase/Inquiry.md) — `DeliveryMethodId` (FK)
- [PurchaseOrderInvoices](/entities/Purchase/PurchaseOrderInvoice.md) — `DeliveryMethodId` (FK)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `DeliveryMethod` (expand)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `DeliveryMethodId` (FK)

**Sales**

- [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) — `DeliveryMethodId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `DeliveryMethodId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `DeliveryMethodId` (FK)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `DeliveryMethodId` (FK)
- [ShipmentCustoms](/entities/Sales/ShipmentCustoms.md) — `DeliveryMethod` (expand)
- [ShipmentCustoms](/entities/Sales/ShipmentCustoms.md) — `DeliveryMethodId` (FK)
- [ShipmentCustoms](/entities/Sales/ShipmentCustoms.md) — `ForeignDeliveryMethod` (expand)
- [ShipmentCustoms](/entities/Sales/ShipmentCustoms.md) — `ForeignDeliveryMethodId` (FK)
- [Shipments](/entities/Sales/Shipment.md) — `DeliveryMethodId` (FK)


## Example

```json
{
  "Id": 0,
  "IsDefault": false,
  "Number": 0,
  "Description": null,
  "SupplierId": null,
  "CompanyIds": null,
  "ShippingServiceId": null,
  "ShippingTemplateId": null,
  "Code": null
}
```
