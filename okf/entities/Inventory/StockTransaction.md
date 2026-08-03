---
type: API Entity
title: StockTransactions
description: Represents a stock transaction.
resource: https://api.monitor.se/api/Monitor.API.Inventory.StockTransaction.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.StockTransaction.html
  title: Monitor API — StockTransaction
module: Inventory
api_class: StockTransaction
doc_name: StockTransactions
endpoint: GET /api/v1/Inventory/StockTransactions
guid: F4B5074F-7694-45F4-91CE-67602641773C
permission: Show basic data for part
introduced_in: '22.4'
property_count: 21
references_out:
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartLocation.md
- /entities/Inventory/ProductRecord.md
---

# StockTransactions

Represents a stock transaction.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `StockTransaction`
- **Endpoint:** `GET /api/v1/Inventory/StockTransactions`
- **Required permission:** Show basic data for part
- **GUID:** `F4B5074F-7694-45F4-91CE-67602641773C`
- **Introduced in:** 22.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the stock transaction. |
| `PartNumber` | `String` | no |  | max length 20 | The part number of the stock transaction. |
| `PartId` | `Int64?` | yes | [Parts](Part.md) |  | The business key identifier of the part that was involved in the stock transaction. This value might not be set even though a part always is involved in a stock transaction, read part number to identify involved part in that case. |
| `BalanceChange` | `Decimal` | no |  |  | The balance change of the stock transaction. |
| `BalanceOnPartAfterChange` | `Decimal` | no |  |  | The balance on the part after the stock transaction. |
| `BalanceOnLocationAfterChange` | `Decimal` | no |  |  | The balance on the location after the stock transaction. |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  |  | The logging timestamp of the stock transaction. |
| `DeliveryDate` | `DateTimeOffset` | no |  |  | The delivery date of the stock transaction. |
| `LocationName` | `String` | no |  | max length 35 | The location name of the stock transaction. |
| `BusinessTransactionId` | `Int64` | no |  |  | The business transaction identity of the stock transaction. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse where the stock transaction occured. |
| `PhysicalInventoryListNumber` | `Int64?` | yes |  |  | The physical inventory list number of the stock transaction. |
| `PartLocationId` | `Int64?` | yes | [PartLocations](PartLocation.md) |  | The business key identifier of the part location where the stock transaction occured. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](ProductRecord.md) |  | The business key identifier of the product record used in the stock transaction. |
| `BatchNumber` | `String` | no |  | since 23.4 | The batch number of the product record in this stock transaction. |
| `OrderNumber` | `String` | no |  | since 23.4 | The order number associated to this stock transaction. |
| `BusinessTransactionContextType` | `Int32` | no |  | enum, since 23.4 | The type of the business transaction context of this stock transaction. |
| `StandardPrice` | `Decimal` | no |  | since 25.9 | The standard price of the stock transaction. |
| `Price` | `Decimal?` | yes |  | since 25.9 | The price of the stock transaction. |
| `ReportedPrice` | `Decimal` | no |  | since 25.9 | The reported price of the stock transaction. |
| `Amount` | `Decimal` | no |  | since 25.9 | The calculated amount based on Price multiplied by BalanceChange of the stock transaction. |

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


## Example

```json
{
  "Id": 0,
  "PartNumber": null,
  "PartId": null,
  "BalanceChange": 0.0,
  "BalanceOnPartAfterChange": 0.0,
  "BalanceOnLocationAfterChange": 0.0,
  "LoggingTimeStamp": "0001-01-01T00:00:00+00:00",
  "DeliveryDate": "0001-01-01T00:00:00+00:00",
  "LocationName": null,
  "BusinessTransactionId": 0,
  "WarehouseId": 0,
  "PhysicalInventoryListNumber": null,
  "PartLocationId": null,
  "ProductRecordId": null,
  "BatchNumber": null,
  "OrderNumber": null,
  "BusinessTransactionContextType": 0,
  "StandardPrice": 0.0,
  "Price": null,
  "ReportedPrice": 0.0,
  "Amount": 0.0
}
```
