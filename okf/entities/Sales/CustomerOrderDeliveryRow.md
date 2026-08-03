---
type: API Entity
title: CustomerOrderDeliveryRows
description: Represents a customer delivery order row.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderDeliveryRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderDeliveryRow.html
  title: Monitor API — CustomerOrderDeliveryRow
module: Sales
api_class: CustomerOrderDeliveryRow
doc_name: CustomerOrderDeliveryRows
endpoint: GET /api/v1/Sales/CustomerOrderDeliveryRows
guid: 5FE65C60-1B7B-4993-AF57-CE8CEA055706
permission: Show customer orders
introduced_in: '2.36'
property_count: 15
references_out:
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/CustomerOrderInvoiceRow.md
- /entities/Sales/CustomerOrderRow.md
referenced_by:
- /entities/Inventory/ProductRecord.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/InvoiceLog.md
- /entities/Sales/PackageRow.md
- /entities/Sales/SalesPickingListRowQuantity.md
---

# CustomerOrderDeliveryRows

Represents a customer delivery order row.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerOrderDeliveryRow`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderDeliveryRows`
- **Required permission:** Show customer orders
- **GUID:** `5FE65C60-1B7B-4993-AF57-CE8CEA055706`
- **Introduced in:** 2.36

## Notes

- CustomerOrderDeliveryRows

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the row. |
| `AffectStockBalance` | `Boolean` | no |  |  | Specifies if row affect the stock balance. |
| `BusinessTransactionContextType` | `Int32` | no |  | enum | The type of the business transaction context. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](CustomerOrder.md) |  | The business key identifier of the customer order. |
| `CustomerOrderRowId` | `Int64?` | yes | [CustomerOrderRows](CustomerOrderRow.md) |  | The business key identifier of the customer order row. |
| `DeliveryDate` | `DateTimeOffset` | no |  |  | The delivery date of the row. |
| `FreeTextHtml` | `String` | no |  | max length 0 | The free text row's rich text HTML row data. |
| `FreeText` | `String` | no |  | max length 0 | The free text row's raw text. |
| `InvoiceId` | `Int64?` | yes | [CustomerOrderInvoices](CustomerOrderInvoice.md) |  | The business key identifier of the customer order invoice. CustomerOrderInvoices |
| `ParentId` | `Int64?` | yes |  |  | The business key identifier of the parent. |
| `ParentInvoiceId` | `Int64?` | yes |  |  | The business key identifier of the parent invoice. |
| `PickListDeliveryDate` | `DateTimeOffset?` | yes |  |  | The delivery date of the pick list. |
| `QuantityChangeId` | `Int64?` | yes |  |  | The business key identifier of the quantity change. |
| `InvoiceRowId` | `Int64?` | yes | [CustomerOrderInvoiceRows](CustomerOrderInvoiceRow.md) |  | The business key identifier of the customer order invoice row. CustomerOrderInvoiceRows |
| `InvoiceRow` | `CustomerOrderInvoiceRows` | no | [CustomerOrderInvoiceRows](CustomerOrderInvoiceRow.md) |  | The invoice row of the customer order delivery row. CustomerOrderInvoiceRows |

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

**Inventory**

- [ProductRecords](../Inventory/ProductRecord.md) — `CustomerOrderDeliveryRow` (expand)
- [ProductRecords](../Inventory/ProductRecord.md) — `CustomerOrderDeliveryRowId` (FK)

**Sales**

- [CustomerOrderInvoices](CustomerOrderInvoice.md) — `DeliveryRows` (expand)
- [InvoiceLogs](InvoiceLog.md) — `DeliveryRowId` (FK)
- [PackageRows](PackageRow.md) — `CustomerOrderDeliveryRowId` (FK)
- [SalesPickingListRowQuantities](SalesPickingListRowQuantity.md) — `CustomerOrderDeliveryRowId` (FK)


## Example

```json
{
  "Id": 0,
  "AffectStockBalance": false,
  "BusinessTransactionContextType": 0,
  "CustomerOrderId": null,
  "CustomerOrderRowId": null,
  "DeliveryDate": "0001-01-01T00:00:00+00:00",
  "FreeTextHtml": null,
  "FreeText": null,
  "InvoiceId": null,
  "ParentId": null,
  "ParentInvoiceId": null,
  "PickListDeliveryDate": null,
  "QuantityChangeId": null,
  "InvoiceRowId": null,
  "InvoiceRow": null
}
```
