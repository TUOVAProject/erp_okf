---
type: API Entity
title: PriceChangeLogs
description: Represents a price change log entity.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PriceChangeLog.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PriceChangeLog.html
  title: Monitor API — PriceChangeLog
module: Inventory
api_class: PriceChangeLog
doc_name: PriceChangeLogs
endpoint: GET /api/v1/Inventory/PriceChangeLogs
guid: 37985af3-e55c-476e-ac05-882f1b9f8f7f
permission: Show part
introduced_in: '2.51'
property_count: 19
references_out:
- /entities/Common/Currency.md
- /entities/Common/PriceList.md
- /entities/Inventory/Part.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
---

# PriceChangeLogs

Represents a price change log entity.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `PriceChangeLog`
- **Endpoint:** `GET /api/v1/Inventory/PriceChangeLogs`
- **Required permission:** Show part
- **GUID:** `37985af3-e55c-476e-ac05-882f1b9f8f7f`
- **Introduced in:** 2.51

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the price change log. |
| `Context` | `Int32` | no |  | enum | The context of the price change in the price change log. |
| `PriceType` | `Int32` | no |  | enum | The type of the price in the price change log. |
| `PriceListId` | `Int64?` | yes | [PriceLists](/entities/Common/PriceList.md) |  | The business key identifier of the price changes log's price list. |
| `Timestamp` | `DateTimeOffset` | no |  |  | The timestamp of the price change log. |
| `UserCode` | `String` | no |  |  | The user code of the price change log. |
| `NewPriceAmount` | `Decimal?` | yes |  |  | The new price amount of the price change log. |
| `NewPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier for the new price currency of the price change log. |
| `OldPriceAmount` | `Decimal?` | yes |  |  | The old price amount of the price change log. |
| `OldPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier for the old price currency of the price change log. |
| `Balance` | `Decimal?` | yes |  |  | The balance of the price change log. |
| `PartId` | `Int64` | no | [Parts](/entities/Inventory/Part.md) |  | The part id of the price change log. |
| `CalculationId` | `Int64?` | yes |  |  | The calculation id of the price change log. |
| `SupplierId` | `Int64?` | yes | [Suppliers](/entities/Purchase/Supplier.md) |  | The supplier id of the price change log. |
| `CustomerId` | `Int64?` | yes | [Customers](/entities/Sales/Customer.md) |  | The customer id of the price change log. |
| `StaggeredQuantity` | `Decimal?` | yes |  |  | The staggered quantity of the price change log. |
| `IsSetupPrice` | `Boolean` | no |  |  | Is the price in the price change log a setup price. |
| `Discount` | `Decimal?` | yes |  |  | The discount of the price change log. |
| `IsExportedToManagementAccounting` | `Boolean` | no |  |  | Is exported to management accounting. |

## Enumerations

### Context

| Name | Value |
| --- | ---: |
| `Manual` | 0 |
| `PreCalculation` | 1 |
| `PostCalculation` | 2 |
| `ManualFromList` | 3 |
| `PriceImport` | 4 |
| `PurchaseCalculation` | 5 |
| `PartSynchronization` | 6 |
| `CancelInvoice` | 7 |
| `CreditInvoice` | 8 |
| `Invoice` | 9 |
| `ExpenseInvoice` | 10 |
| `UndoExpenseInvoice` | 11 |
| `SubcontractingCostReport` | 12 |
| `AutoUpdateFromFuturePrice` | 13 |
| `PriceCorrectionInvoice` | 14 |
| `ReportingOfReturnOrder` | 15 |
| `FinalRecordingOfCorrectionInvoice` | 16 |
| `FullReturnToSupplier` | 17 |
| `AutomaticMovingAveragePriceCalculation` | 18 |

### PriceType

| Name | Value |
| --- | ---: |
| `Standard` | 0 |
| `PriceList` | 3 |
| `FuturePriceList` | 4 |
| `PriceFromInvoiceOrCustomerOrderRow` | 5 |
| `Invoice` | 6 |
| `PriceListStaggered` | 7 |
| `FuturePriceListStaggered` | 8 |
| `CustomerStaggered` | 9 |
| `FutureCustomerStaggered` | 10 |
| `SupplierStaggered` | 11 |
| `FutureSupplierStaggered` | 12 |
| `StandardPriceFromCustomerOrderRowWithFallbackToPartStandardPrice` | 13 |
| `CustomerWithFallbackPriceListOnCustomer` | 14 |
| `FutureSetupPrice` | 15 |
| `StandardPriceOnDelivery` | 16 |
| `StandardPriceOnInvoicing` | 17 |
| `StandardPriceOnFinalBookingAccountsPayable` | 18 |
| `PurchaseOrder` | 19 |
| `FifoAtInvoicing` | 20 |
| `LinkedConfiguredCustomOrderRow` | 21 |
| `HistoricalFifoPrice` | 22 |
| `ComparativePrice` | 23 |
| `ProductRecordStandardPrice` | 24 |
| `MovingAveragePrice` | 25 |
| `MovingAveragePriceAtInvoicing` | 26 |
| `FutureSupplier` | -9998 |
| `FutureCustomer` | -9997 |
| `None` | -99 |
| `ReportedStandard` | -20 |
| `MaterialCost` | -19 |
| `HistoricalStandard` | -18 |
| `DiscountedCustomer` | -17 |
| `DiscountedSupplier` | -16 |
| `PostCalculatedAverage` | -15 |
| `SavedAverage` | -14 |
| `Lowest` | -9 |
| `FIFO` | -8 |
| `AvarageSales` | -7 |
| `LatestSales` | -6 |
| `AveragePurchase` | -5 |
| `LatestPurchase` | -4 |
| `Customer` | -3 |
| `Supplier` | -2 |
| `FutureStandard` | -1 |


## Example

```json
{
  "Id": 0,
  "Context": 0,
  "PriceType": 0,
  "PriceListId": null,
  "Timestamp": "0001-01-01T00:00:00+00:00",
  "UserCode": null,
  "NewPriceAmount": null,
  "NewPriceCurrencyId": null,
  "OldPriceAmount": null,
  "OldPriceCurrencyId": null,
  "Balance": null,
  "PartId": 0,
  "CalculationId": null,
  "SupplierId": null,
  "CustomerId": null,
  "StaggeredQuantity": null,
  "IsSetupPrice": false,
  "Discount": null,
  "IsExportedToManagementAccounting": false
}
```
