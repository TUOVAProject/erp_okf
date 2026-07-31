---
type: API Entity
title: PurchaseOrderAdvices
description: Represents a purchase order advice.
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderAdvice.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderAdvice.html
  title: Monitor API — PurchaseOrderAdvice
module: Purchase
api_class: PurchaseOrderAdvice
doc_name: PurchaseOrderAdvices
endpoint: GET /api/v1/Purchase/PurchaseOrderAdvices
guid: 3020A4C1-7B63-497D-BB9D-A9E265EDD125
permission: Show arrival
introduced_in: '22.2'
property_count: 7
references_out:
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Purchase/PurchaseOrderAdviceRow.md
---

# PurchaseOrderAdvices

Represents a purchase order advice.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `PurchaseOrderAdvice`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderAdvices`
- **Required permission:** Show arrival
- **GUID:** `3020A4C1-7B63-497D-BB9D-A9E265EDD125`
- **Introduced in:** 22.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the purchase order advice. |
| `SupplierId` | `Int64` | no | [Suppliers](/entities/Purchase/Supplier.md) |  | The business key identifier of the supplier for the advice. |
| `Status` | `Int32` | no |  | enum | The status of the advice. |
| `DispatchDate` | `DateTimeOffset` | no |  |  | The dispatch date of the advice. |
| `DeliveryNoteNumber` | `String` | no |  | max length 35 | The delivery note number of the advice. |
| `ShipmentNumber` | `String` | no |  | max length 35 | The shipment number of the advice. |
| `GoodsTrackingUrl` | `String` | no |  | max length 255 | The gods tracking url of the advice. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `PartiallyDelivered` | 5 |
| `History` | 9 |


## Referenced by

**Purchase**

- [PurchaseOrderAdviceRows](/entities/Purchase/PurchaseOrderAdviceRow.md) — `ParentId` (FK)


## Example

```json
{
  "Id": 0,
  "SupplierId": 0,
  "Status": 0,
  "DispatchDate": "0001-01-01T00:00:00+00:00",
  "DeliveryNoteNumber": null,
  "ShipmentNumber": null,
  "GoodsTrackingUrl": null
}
```
