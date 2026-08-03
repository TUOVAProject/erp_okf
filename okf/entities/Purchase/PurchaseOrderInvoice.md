---
type: API Entity
title: PurchaseOrderInvoices
description: Represents a purchase order invoice entry
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderInvoice.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderInvoice.html
  title: Monitor API — PurchaseOrderInvoice
module: Purchase
api_class: PurchaseOrderInvoice
doc_name: PurchaseOrderInvoices
endpoint: GET /api/v1/Purchase/PurchaseOrderInvoices
guid: 48914C07-4632-4904-8DAC-27BFA1E3FABC
permission: Show purchase orders
introduced_in: '2.27'
property_count: 15
references_out:
- /entities/Common/DeliveryMethod.md
- /entities/Common/DeliveryTerm.md
- /entities/Common/PaymentTerm.md
- /entities/Common/VatGroup.md
- /entities/Common/Warehouse.md
- /entities/Purchase/PurchaseOrderDelivery.md
- /entities/Purchase/PurchaseOrderInvoiceRow.md
- /entities/Purchase/SupplierAccountGroup.md
---

# PurchaseOrderInvoices

Represents a purchase order invoice entry

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `PurchaseOrderInvoice`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderInvoices`
- **Required permission:** Show purchase orders
- **GUID:** `48914C07-4632-4904-8DAC-27BFA1E3FABC`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the purchase order invoice. |
| `PurchaseOrderDeliveryId` | `Int64?` | yes | [PurchaseOrderDeliveries](PurchaseOrderDelivery.md) |  | The business key identifier of the purchase order delivery. |
| `AccountGroupId` | `Int64?` | yes | [SupplierAccountGroups](SupplierAccountGroup.md) |  | The business key identifier of the supplier account group. References SupplierAccountGroups . |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse that the purchase order invoice belongs to. |
| `VatGroupId` | `Int64` | no | [VatGroups](../Common/VatGroup.md) |  | The business key identifier of the VAT group that applies for the purchase order invoice. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](../Common/PaymentTerm.md) |  | The business key identifier of the payment term of the purchase order invoice. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](../Common/PaymentTerm.md) | expandable | The payment term of the purchase order invoice. |
| `PaymentTermDescription` | `String` | no |  | max length 35 | The payment term description of the purchase order invoice. |
| `GracePeriodInDays` | `Int32?` | yes |  |  | The purchase order invoice grace period in days. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](../Common/DeliveryMethod.md) |  | The business key identifier of the purchase order invoice delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](../Common/DeliveryTerm.md) |  | The business key identifier of the purchase order invoice delivery term. |
| `DeliveryTermDescription` | `String` | no |  | max length 35 | The delivery term description of the purchase order invoice. |
| `DeliveryMethodDescription` | `String` | no |  | max length 35 | The delivery method description of the purchase order invoice. |
| `ShipmentPayer` | `Int32` | no |  | enum | Specifies who is responsible for the shipment payment for the purchase order invoice. |
| `Rows` | `PurchaseOrderInvoiceRows[]` | no | [PurchaseOrderInvoiceRows](PurchaseOrderInvoiceRow.md) | expandable, collection | The rows of the purchase order invoice. |

## Enumerations

### ShipmentPayer

| Name | Value |
| --- | ---: |
| `BuyerPays` | 1 |
| `SellerPays` | 2 |
| `OtherPayer` | 3 |
| `Incoterms` | 4 |


## Example

```json
{
  "Id": 0,
  "PurchaseOrderDeliveryId": null,
  "AccountGroupId": null,
  "WarehouseId": 0,
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
  "Rows": null
}
```
