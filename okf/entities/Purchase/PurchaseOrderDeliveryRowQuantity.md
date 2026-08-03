---
type: API Entity
title: PurchaseOrderDeliveryRowQuantities
description: Represents a purchase order delivery row quantity entry
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderDeliveryRowQuantity.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderDeliveryRowQuantity.html
  title: Monitor API — PurchaseOrderDeliveryRowQuantity
module: Purchase
api_class: PurchaseOrderDeliveryRowQuantity
doc_name: PurchaseOrderDeliveryRowQuantities
endpoint: GET /api/v1/Purchase/PurchaseOrderDeliveryRowQuantities
guid: 8B7409DA-392A-4335-AB12-52575FC571C0
permission: Show purchase orders
introduced_in: '26.4'
property_count: 5
references_out:
- /entities/Inventory/QuantityChange.md
- /entities/Purchase/PurchaseOrderDeliveryRow.md
referenced_by:
- /entities/Purchase/PurchaseOrderDeliveryRow.md
---

# PurchaseOrderDeliveryRowQuantities

Represents a purchase order delivery row quantity entry

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `PurchaseOrderDeliveryRowQuantity`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderDeliveryRowQuantities`
- **Required permission:** Show purchase orders
- **GUID:** `8B7409DA-392A-4335-AB12-52575FC571C0`
- **Introduced in:** 26.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the purchase order delivery row quantity. |
| `QuantityChangeId` | `Int64` | no | [QuantityChanges](../Inventory/QuantityChange.md) |  | The business key identifier of the quantity change. |
| `QuantityChange` | `QuantityChanges` | no | [QuantityChanges](../Inventory/QuantityChange.md) | expandable | The quantity change. |
| `BusinessTransactionContextType` | `Int32` | no |  | enum | The type of business transaction context. |
| `ParentId` | `Int64` | no | [PurchaseOrderDeliveryRows](PurchaseOrderDeliveryRow.md) |  | The business key identifier of the purchase order delivery row. |

## Enumerations

### BusinessTransactionContextType

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `ArrivalReporting` | 1 |
| `ManufacturingOrderReporting` | 2 |
| `DeliveryReporting` | 3 |
| `PhysicalInventory` | 4 |
| `UnplannedStockWithdrawal` | 5 |
| `MoveBetweenWarehouse` | 6 |
| `MoveStockBalance` | 7 |
| `NonconformityPosteriorRejection` | 8 |
| `DirectlyRegisteredInvoice` | 9 |
| `RemovalOfPartLocation` | 10 |
| `ManufacturingOrderMaterialReporting` | 11 |
| `UnplannedStockArrivalReporting` | 12 |
| `StockImport` | 13 |
| `DeliveryReportingStockOrder` | 14 |
| `ArrivalReportingStockOrder` | 15 |
| `UndoManufacturingOrderMaterialReporting` | 16 |
| `UndoManufacturingOrderReporting` | 17 |
| `UndoArrivalReporting` | 18 |
| `UndoDeliveryReporting` | 19 |
| `UndoArrivalReportingStockOrder` | 20 |
| `UndoDeliveryReportingStockOrder` | 21 |
| `OutgoingReusable` | 22 |
| `ArrivalReusable` | 23 |
| `UndoOutgoingReusable` | 24 |
| `UndoArrivalReusable` | 25 |
| `ToolWithdrawal` | 26 |
| `ToolReturn` | 27 |
| `CreditSupplierInvoice` | 28 |
| `CreditCustomerInvoice` | 29 |
| `ReturnPurchaseOrder` | 30 |
| `SplitInvoiceBasis` | 31 |
| `CreationOfPartLocation` | 32 |
| `ArrivalsCorrection` | 33 |
| `ArrivalRejection` | 34 |
| `UndoReturnPurchaseOrder` | 35 |


## Referenced by

**Purchase**

- [PurchaseOrderDeliveryRows](PurchaseOrderDeliveryRow.md) — `PurchaseOrderDeliveryRowQuantities` (expand)


## Example

```json
{
  "Id": 0,
  "QuantityChangeId": 0,
  "QuantityChange": null,
  "BusinessTransactionContextType": 0,
  "ParentId": 0
}
```
