---
type: API Entity
title: PurchaseOrderDeliveryRows
description: Represents a purchase order delivery row entry
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderDeliveryRow.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderDeliveryRow.html
  title: Monitor API — PurchaseOrderDeliveryRow
module: Purchase
api_class: PurchaseOrderDeliveryRow
doc_name: PurchaseOrderDeliveryRows
endpoint: GET /api/v1/Purchase/PurchaseOrderDeliveryRows
guid: DDBDFA96-3D45-4A77-B5BF-A3B6A19DEFD6
permission: Show purchase orders
introduced_in: '2.26'
property_count: 12
references_out:
- /entities/Accounting/AccountsPayable.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderDeliveryRowQuantity.md
- /entities/Purchase/PurchaseOrderRow.md
referenced_by:
- /entities/Accounting/BookingRow.md
- /entities/Manufacturing/ManufacturingOrderOperationReporting.md
- /entities/Purchase/PurchaseOrderDelivery.md
- /entities/Purchase/PurchaseOrderDeliveryRowQuantity.md
- /entities/Purchase/PurchaseOrderInvoiceRow.md
- /entities/Purchase/PurchaseOrderRow.md
---

# PurchaseOrderDeliveryRows

Represents a purchase order delivery row entry

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `PurchaseOrderDeliveryRow`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderDeliveryRows`
- **Required permission:** Show purchase orders
- **GUID:** `DDBDFA96-3D45-4A77-B5BF-A3B6A19DEFD6`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the purchase order delivery row. |
| `Version` | `Int32` | no |  |  | The version of the purchase order delivery row. |
| `PurchaseOrderId` | `Int64` | no | [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) |  | The business key identifier of the purchase order. |
| `PurchaseOrderRowId` | `Int64` | no | [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) |  | The business key identifier of the purchase order row. |
| `PurchaseOrderRow` | `PurchaseOrderRows` | no | [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) | expandable | The purchase order row. |
| `DeliveryDate` | `DateTimeOffset` | no |  |  | The delivery date of the of order delivery row. |
| `GoodsLocation` | `String` | no |  | max length 40 | The human readable goods location of the order delivery row. |
| `GoodsMessage` | `String` | no |  | max length 100 | The human readable good message on the order delivery row. |
| `ArrivedQuantity` | `Decimal` | no |  |  | The arrived qty on the order delivery row. |
| `ApprovedQuantity` | `Decimal` | no |  |  | The approved qty on the order delivery row. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](/entities/Accounting/AccountsPayable.md) | since 22.5 | The business key identifier of the accounts payable the delivery row is linked to. |
| `PurchaseOrderDeliveryRowQuantities` | `PurchaseOrderDeliveryRowQuantities[]` | no | [PurchaseOrderDeliveryRowQuantities](/entities/Purchase/PurchaseOrderDeliveryRowQuantity.md) | collection, since 26.4 | The quantities of the order delivery row. |

## Referenced by

**Accounting**

- [BookingRows](/entities/Accounting/BookingRow.md) — `PurchaseOrderDeliveryRowId` (FK)

**Manufacturing**

- [ManufacturingOrderOperationReportings](/entities/Manufacturing/ManufacturingOrderOperationReporting.md) — `PurchaseOrderDeliveryRowId` (FK)

**Purchase**

- [PurchaseOrderDeliveries](/entities/Purchase/PurchaseOrderDelivery.md) — `Rows` (expand)
- [PurchaseOrderDeliveryRowQuantities](/entities/Purchase/PurchaseOrderDeliveryRowQuantity.md) — `ParentId` (FK)
- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `PurchaseOrderDeliveryRowId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `OriginatingPurchaseOrderDeliveryRowId` (FK)


## Example

```json
{
  "Id": 0,
  "Version": 0,
  "PurchaseOrderId": 0,
  "PurchaseOrderRowId": 0,
  "PurchaseOrderRow": null,
  "DeliveryDate": "0001-01-01T00:00:00+00:00",
  "GoodsLocation": null,
  "GoodsMessage": null,
  "ArrivedQuantity": 0.0,
  "ApprovedQuantity": 0.0,
  "AccountsPayableId": null,
  "PurchaseOrderDeliveryRowQuantities": null
}
```
