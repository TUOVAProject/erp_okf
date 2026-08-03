---
type: API Entity
title: PurchaseOrderDeliveries
description: Represents a purchase order delivery entry
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderDelivery.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderDelivery.html
  title: Monitor API — PurchaseOrderDelivery
module: Purchase
api_class: PurchaseOrderDelivery
doc_name: PurchaseOrderDeliveries
endpoint: GET /api/v1/Purchase/PurchaseOrderDeliveries
guid: 5CC82877-BA9A-4BE9-9ACF-E9825F9B40C1
permission: Show purchase orders
introduced_in: '2.26'
property_count: 8
references_out:
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderDeliveryRow.md
referenced_by:
- /entities/Purchase/PurchaseOrderInvoice.md
---

# PurchaseOrderDeliveries

Represents a purchase order delivery entry

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `PurchaseOrderDelivery`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderDeliveries`
- **Required permission:** Show purchase orders
- **GUID:** `5CC82877-BA9A-4BE9-9ACF-E9825F9B40C1`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the purchase order delivery. |
| `PurchaseOrderId` | `Int64` | no | [PurchaseOrders](PurchaseOrder.md) |  | The business key identifier of the purchase order. |
| `ConfirmationDate` | `DateTimeOffset?` | yes |  | **deprecated since 25.5** | The confirmation date of the of purchase order delivery. _(This field has been removed as it was never used.)_ |
| `AdviceDate` | `DateTimeOffset?` | yes |  | **deprecated since 25.5** | The advice date of the of purchase order delivery. _(This field has been removed as it was never used.)_ |
| `DeliveryNoteNumber` | `String` | no |  | max length 35 | The human readable delivery note number of the purchase order delivery. |
| `WayBillNumber` | `String` | no |  | max length 35 | The human readable way bill number of the purchase order delivery. |
| `Rows` | `PurchaseOrderDeliveryRows[]` | no | [PurchaseOrderDeliveryRows](PurchaseOrderDeliveryRow.md) | expandable, collection | The rows of the purchase order delivery. |
| `ArrivalNoteNumber` | `Int64` | no |  | since 25.6 | The arrival note number of the purchase order delivery. |

## Referenced by

**Purchase**

- [PurchaseOrderInvoices](PurchaseOrderInvoice.md) — `PurchaseOrderDeliveryId` (FK)


## Example

```json
{
  "Id": 0,
  "PurchaseOrderId": 0,
  "ConfirmationDate": null,
  "AdviceDate": null,
  "DeliveryNoteNumber": null,
  "WayBillNumber": null,
  "Rows": null,
  "ArrivalNoteNumber": 0
}
```
