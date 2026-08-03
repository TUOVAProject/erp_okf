---
type: API Entity
title: PurchaseOrderRows
description: Represents a purchase order row.
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderRow.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderRow.html
  title: Monitor API — PurchaseOrderRow
module: Purchase
api_class: PurchaseOrderRow
doc_name: PurchaseOrderRows
endpoint: GET /api/v1/Purchase/PurchaseOrderRows
guid: E2C7B35D-48E3-45E6-AEEC-A297943E583F
permission: Show purchase orders
introduced_in: '2.26'
property_count: 101
references_out:
- /entities/Accounting/Coding.md
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/ReasonCode.md
- /entities/Common/Revision.md
- /entities/Common/StatisticalGoodsCode.md
- /entities/Common/TariffAndServiceCode.md
- /entities/Common/TransactionTypeIntrastat.md
- /entities/Common/Unit.md
- /entities/Common/VatRate.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Purchase/BlanketOrderPurchaseRow.md
- /entities/Purchase/OrderQuantityPurchaseOrder.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderDeliveryRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/CustomerOrderRow.md
referenced_by:
- /entities/Manufacturing/ManufacturingOrderMaterial.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderAdviceRow.md
- /entities/Purchase/PurchaseOrderDeliveryRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/CustomerOrderRow.md
---

# PurchaseOrderRows

Represents a purchase order row.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `PurchaseOrderRow`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderRows`
- **Required permission:** Show purchase orders
- **GUID:** `E2C7B35D-48E3-45E6-AEEC-A297943E583F`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the row. |
| `Position` | `Int64?` | yes |  |  | The relative numeric position of the row. |
| `OrderRowType` | `Int32` | no |  | enum | The type of the row. |
| `PartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the part set for the row. |
| `Part` | `Parts` | no | [Parts](../Inventory/Part.md) | expandable | The part of the row. |
| `EntityIdentityString` | `String` | no |  | max length 20 | The human readable identifier of the entity subject of the row. |
| `AdditionalRowDescription` | `String` | no |  | max length 80 | The additional row description of the row. |
| `FreeTextHtml` | `String` | no |  | max length 0 | The free text row's rich text HTML row data. |
| `FreeText` | `String` | no |  | max length 0 | The free text row's raw text. |
| `ParentRowId` | `Int64?` | yes | [PurchaseOrderRows](PurchaseOrderRow.md) |  | The business key identifier of the current row's parent. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |  | The delivery date set for the row. |
| `RevisionId` | `Int64?` | yes | [Revisions](../Common/Revision.md) |  | The business key identifier of the row's revision. |
| `Revision` | `Revisions` | no | [Revisions](../Common/Revision.md) | expandable | The revision of the row. |
| `OrderedQuantity` | `Decimal` | no |  |  | The ordered quantity of the row. |
| `Price` | `Decimal?` | yes |  |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row price currency. |
| `PriceCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable, since 2.30 | The price currency for the row. |
| `Discount` | `Decimal` | no |  |  | The discount in percent set for the row. |
| `ToolId` | `Int64?` | yes |  | **deprecated since 2.48** | The business key identifier of the tool of the row. _(Replaced by Part)_ |
| `UnitId` | `Int64?` | yes | [Units](../Common/Unit.md) |  | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](../Common/Unit.md) | expandable | The unit of the row. |
| `VatRateId` | `Int64` | no | [VatRates](../Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `VatRate` | `VatRates` | no | [VatRates](../Common/VatRate.md) | expandable, since 2.30 | The VAT rate of the row. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse that the row belongs to. |
| `Warehouse` | `Warehouses` | no | [Warehouses](../Common/Warehouse.md) | expandable, since 2.30 | The warehouse that the row belongs to. |
| `WeightPerUnit` | `Decimal?` | yes |  |  | The weight per unit of the row. |
| `OrderDate` | `DateTimeOffset` | no |  |  | The order date of the row. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor of the row. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The row price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the company currency. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |  | The setup price of the row in the company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes |  |  | The business key identifier of the company currency. |
| `StandardPrice` | `Decimal?` | yes |  |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's standard price currency. |
| `StandardPriceCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable, since 2.30 | The standard price currency of the row. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's setup price currency. |
| `SetupPriceCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable, since 2.30 | The setup price currency of the row. |
| `ShowPrice` | `Boolean` | no |  |  | Specifies if price should be shown for the row. |
| `PartRowType` | `Int32` | no |  | enum | The part row type of the row. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the row. |
| `PartStatus` | `Int32?` | yes |  | enum | The part status of the part at the time of row creation. |
| `OrderedQuantityInOrderUnit` | `Decimal` | no |  |  | The ordered quantity in the order unit. |
| `RestQuantity` | `Decimal` | no |  |  | The rest quantity of the row. |
| `DeliveredQuantity` | `Decimal` | no |  |  | The delivered quantity of the row. |
| `InitialDeliveryDate` | `DateTimeOffset?` | yes |  |  | The initial delivery date of the row. |
| `DesiredDeliveryDate` | `DateTimeOffset?` | yes |  |  | The desired delivery date of the row. |
| `RestQuantityInOrderUnit` | `Decimal` | no |  |  | The rest quantity in the order unit. |
| `DeliveredQuantityInOrderUnit` | `Decimal` | no |  |  | The delivered quantity in the order unit. |
| `CreationContext` | `Int32` | no |  | enum | The creation context of the row. |
| `ShowFreeTextIn` | `Int32` | no |  | bitmask, enum | Specifies which documents the free text row data will appear on. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](../Common/StatisticalGoodsCode.md) |  | The business key identifier of the row's statistical goods code. |
| `StatisticalGoodsCode` | `StatisticalGoodsCodes` | no | [StatisticalGoodsCodes](../Common/StatisticalGoodsCode.md) | expandable, since 2.30 | The statistical goods code of the row. |
| `RowStatus` | `Int32` | no |  | enum | The status of the purchase order row. |
| `Version` | `Int32` | no |  | since 2.30 | The version of the row. |
| `ArrivalReporting` | `Boolean` | no |  | since 2.30 | Specifies if the row uses arrival reporting. |
| `ConfirmedDelayed` | `Boolean` | no |  | since 2.30 | Specifies if the row is confirmed delayed. |
| `DelayCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) | since 2.30 | The business key identifier of the row's delay comment. |
| `DelayComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable, since 2.30 | The delay comment of the row. |
| `DelayReasonId` | `Int64?` | yes | [ReasonCodes](../Common/ReasonCode.md) | since 2.30 | The business key identifier of the row's delay reason. |
| `DelayReason` | `ReasonCodes` | no | [ReasonCodes](../Common/ReasonCode.md) | expandable, since 2.30 | The delay reason of the row. |
| `CodingId` | `Int64?` | yes |  | since 2.30 | The business key identifier of the row's coding. |
| `Coding` | `Codings` | no | [Codings](../Accounting/Coding.md) | expandable, since 2.30 | The coding of the row. |
| `IsConfirmed` | `Boolean` | no |  | since 2.30 | Specifies if the row is confirmed. |
| `ReceivingInspectionInstructionId` | `Int64?` | yes | [Comments](../Common/Comment.md) | since 2.30 | The business key identifier of the row's receiving inspection instruction. |
| `ReceivingInspectionInstruction` | `Comments` | no | [Comments](../Common/Comment.md) | expandable, since 2.30 | The receiving inspection instruction of the row. |
| `ReceivingInspectionType` | `Int32` | no |  | enum, since 2.30 | The receiving inspection type of the row. |
| `ReceivingMessageId` | `Int64?` | yes | [Comments](../Common/Comment.md) | since 2.30 | The business key identifier of the row's receiving message. |
| `ReceivingMessage` | `Comments` | no | [Comments](../Common/Comment.md) | expandable, since 2.30 | The receiving message of the row. |
| `RequiredForManufacturingOrderNode` | `Int64?` | yes |  | since 2.30 | The business key identifier of the manufacturing order node that requires this row. |
| `Weight` | `Decimal` | no |  | since 2.30 | The weight of the row. |
| `LinkedStockOrderRowId` | `Int64?` | yes | [CustomerOrderRows](../Sales/CustomerOrderRow.md) | since 2.30 | The business key identifier of the row's linked stock order row. |
| `LinkedSubcontractingManufacturingOrderOperation` | `Int64?` | yes | [ManufacturingOrderOperations](../Manufacturing/ManufacturingOrderOperation.md) | since 2.30 | The business key identifier of the row's linked subcontracting manufacturing order operation. |
| `OriginatingPurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](PurchaseOrderDeliveryRow.md) | since 2.30 | The business key identifier of the row's originating purchase order delivery row. |
| `CausingTransType` | `Int32` | no |  | enum, since 2.30 | The causing transaction type of the row. |
| `CausingOrderRowId` | `Int64?` | yes |  | since 2.30 | The business key identifier of the order row that was the cause of this row. References depends on CausingTransType |
| `RequirementDate` | `DateTimeOffset?` | yes |  | since 2.30 | The requirement date of the row. |
| `PreviousOrderedQuantity` | `Decimal?` | yes |  | since 2.30 | The previous ordered quantity of the row. |
| `PreviousDeliveryDate` | `DateTimeOffset?` | yes |  | since 2.30 | The previous delivery date of the row. |
| `SubPartParentRowId` | `Int64?` | yes | [PurchaseOrderRows](PurchaseOrderRow.md) | since 2.30 | The business key identifier of the row's sub part parent row. |
| `QuantityRatio` | `Decimal?` | yes |  | since 2.30 | The quantity ratio of the row. |
| `ParentOrderId` | `Int64` | no | [PurchaseOrders](PurchaseOrder.md) | since 2.30 | The business key identifier of the row's purchase order. |
| `RowIndex` | `Int32` | no |  | since 2.30 | The row index of the row. |
| `SumRowId` | `Int64?` | yes | [PurchaseOrderRows](PurchaseOrderRow.md) | since 2.30 | The business key identifier of the row's sum row. |
| `PriceOrigin` | `Int32` | no |  | enum, since 2.30 | The row index of the row. |
| `DiscountIsLockedFromAutomaticChanges` | `Boolean` | no |  | since 2.30 | Specifies if the row's discount is locked from automatic changes. |
| `IntrastatTransactionTypeId` | `Int64?` | yes | [TransactionTypeIntrastats](../Common/TransactionTypeIntrastat.md) | since 2.30 | The business key identifier of the row's intrastat transaction type. |
| `IntrastatTransactionType` | `TransactionTypeIntrastats` | no | [TransactionTypeIntrastats](../Common/TransactionTypeIntrastat.md) | expandable, since 2.30 | The intrastat transaction type of the row. |
| `TariffAndServiceCodeId` | `Int64?` | yes | [TariffAndServiceCodes](../Common/TariffAndServiceCode.md) | since 2.30 | The business key identifier of the row's tariff and service code. |
| `TariffAndServiceCode` | `TariffAndServiceCodes` | no | [TariffAndServiceCodes](../Common/TariffAndServiceCode.md) | expandable, since 2.30 | The tariff and service code of the row. |
| `PartConfigurationId` | `Int64?` | yes |  | since 2.30 | The business key identifier of the row's part configuration. |
| `RowsGoodsLabel` | `String` | no |  | max length 80, since 2.46 | The goods label of the purchase order row. |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityPurchaseOrders](OrderQuantityPurchaseOrder.md) | since 22.6 | The business key identifier of order quantity. |
| `OrderQuantity` | `OrderQuantityPurchaseOrders` | no | [OrderQuantityPurchaseOrders](OrderQuantityPurchaseOrder.md) | expandable, since 22.6 | Order quantity that holds the partial quantities. |
| `SupplierDrawingNumber` | `String` | no |  | since 24.6 | The supplier drawing number of the purchase order row. |
| `SupplierRevisionNumber` | `String` | no |  | since 24.6 | The supplier revision number of the purchase order row. |
| `RowNotes` | `String` | no |  | max length 100, since 24.9 | The note of the purchase order row. |
| `BlanketOrderPurchaseRowId` | `Int64?` | yes | [BlanketOrderPurchaseRows](BlanketOrderPurchaseRow.md) | since 26.2 | The business key identifier of the row's blanket order purchase row. |
| `SupplierOrderNumber` | `String` | no |  | since 26.2 | The supplier order number of the purchase order row. |
| `SupplierOrderRowPosition` | `String` | no |  | since 26.2 | The supplier order row position of the purchase order row. |
| `SupplierPartNumber` | `String` | no |  | max length 50, since 26.4 | The supplier's part number of the purchase order row. |

## Enumerations

### OrderRowType

| Name | Value |
| --- | ---: |
| `Part` | 1 |
| `Additional` | 2 |
| `Sum` | 3 |
| `FreeText` | 4 |

### PartRowType

| Name | Value |
| --- | ---: |
| `NotPartRow` | 0 |
| `RegularRow` | 1 |
| `SubPartRow` | 2 |
| `SetupPriceRow` | 3 |
| `AlloyCostRow` | 4 |
| `PaymentPlanRow` | 5 |
| `PackagingRow` | 6 |

### LifeCycleState

| Name | Value |
| --- | ---: |
| `Transient` | 1 |
| `Persistent` | 10 |
| `History` | 20 |
| `RemovableCandidate` | 99 |

### PartStatus

| Name | Value |
| --- | ---: |
| `Quote` | 1 |
| `Prototype` | 2 |
| `New` | 3 |
| `Normal` | 4 |
| `NewRevision` | 5 |
| `PhasingOut` | 6 |
| `Expired` | 9 |
| `Inactive` | 99 |

### CreationContext

| Name | Value |
| --- | ---: |
| `OrderRegistration` | 0 |
| `DeliveryReporting` | 1 |
| `Invoicing` | 2 |
| `PartialInvoicing` | 3 |

### ShowFreeTextIn (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `Internal` | 0 |
| `Inquiry` | 1 |
| `Order` | 2 |
| `DeliverySchedule` | 4 |

### RowStatus

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `PurchaseOrderRowPrinted` | 2 |
| `PartiallyDelivered` | 5 |
| `Declined` | 8 |
| `History` | 9 |

### ReceivingInspectionType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Always` | 1 |
| `VariableInspection` | 2 |

### CausingTransType

| Name | Value |
| --- | ---: |
| `StockBalanceRow` | 0 |
| `ReceivedPurchaseOrder` | 1 |
| `PurchaseOrder` | 2 |
| `PurchaseOrderSuggestion` | 3 |
| `ManufactureOrderNode` | 4 |
| `ManufactureOrderNodeSuggestion` | 5 |
| `ManufactureOrderNodeSimulation` | 6 |
| `CustomerOrder` | 7 |
| `SalesForecast` | 8 |
| `CustomerOrderForecast` | 9 |
| `MaterialRequirementFromManufactureOrderNode` | 10 |
| `MaterialRequirementFromManufactureOrderSuggestion` | 11 |
| `MaterialRequirementFromManufactureOrderSimulation` | 12 |
| `Quote` | 13 |
| `MaterialRequirementSuggestionFromQuoteSimulation` | 14 |
| `ArrivingStockOrder` | 15 |
| `DeliveringStockOrder` | 16 |
| `StockOrderArrivalSuggestion` | 17 |
| `StockOrderDeliverySuggestion` | 18 |
| `CustomerOrderFromDeliveryTimeControl` | 19 |
| `MaterialRequirementSuggestionFromDeliveryTimeControl` | 20 |
| `ManufactureOrderNodeFromDeliveryTimeControl` | 21 |
| `PurchaseOrderFromDeliveryTimeControl` | 22 |
| `PurchaseOrderAdvice` | 23 |
| `DeliveringStockOrderFromDeliveryTimeControl` | 24 |
| `CustomerOrderPreliminary` | 27 |
| `CustomerOrderRowMissingDeliveryDate` | 28 |
| `DeliveringStockOrderPreliminary` | 29 |
| `ServiceOrder` | 30 |
| `ReturnTool` | 33 |
| `WithdrawalTool` | 34 |
| `QuotePreliminary` | 35 |
| `QuoteMissingDeliveryDate` | 36 |
| `SalesBlanketOrder` | 40 |
| `PurchaseBlanketOrder` | 41 |
| `ReturnPurchaseOrder` | 42 |

### PriceOrigin

| Name | Value |
| --- | ---: |
| `Undefined` | 0 |
| `UserDefined` | 1 |
| `PriceList` | 2 |
| `PriceListStaggered` | 3 |
| `BusinessPartLink` | 4 |
| `BusinessPartLinkStaggered` | 5 |
| `StandardPrice` | 6 |
| `PartConfiguration` | 7 |
| `PostCalculatedAverage` | 8 |
| `BusinessPartLinkFuturePrice` | 9 |


## Referenced by

**Manufacturing**

- [ManufacturingOrderMaterials](../Manufacturing/ManufacturingOrderMaterial.md) — `LinkedPurchaseOrderRowId` (FK)

**Purchase**

- [PurchaseOrderAdviceRows](PurchaseOrderAdviceRow.md) — `PurchaseOrderRowId` (FK)
- [PurchaseOrderDeliveryRows](PurchaseOrderDeliveryRow.md) — `PurchaseOrderRow` (expand)
- [PurchaseOrderDeliveryRows](PurchaseOrderDeliveryRow.md) — `PurchaseOrderRowId` (FK)
- [PurchaseOrderRows](PurchaseOrderRow.md) — `ParentRowId` (FK)
- [PurchaseOrderRows](PurchaseOrderRow.md) — `SubPartParentRowId` (FK)
- [PurchaseOrderRows](PurchaseOrderRow.md) — `SumRowId` (FK)
- [PurchaseOrders](PurchaseOrder.md) — `Rows` (expand)

**Sales**

- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `LinkedPurchaseOrderRowId` (FK)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `LinkedStockOrderRow` (expand)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `LinkedStockOrderRowId` (FK)


## Example

```json
{
  "Id": 0,
  "Position": null,
  "OrderRowType": 0,
  "PartId": null,
  "Part": null,
  "EntityIdentityString": null,
  "AdditionalRowDescription": null,
  "FreeTextHtml": null,
  "FreeText": null,
  "ParentRowId": null,
  "DeliveryDate": null,
  "RevisionId": null,
  "Revision": null,
  "OrderedQuantity": 0.0,
  "Price": null,
  "PriceCurrencyId": null,
  "PriceCurrency": null,
  "Discount": 0.0,
  "ToolId": null,
  "UnitId": null,
  "Unit": null,
  "VatRateId": 0,
  "VatRate": null,
  "WarehouseId": 0,
  "Warehouse": null,
  "WeightPerUnit": null,
  "OrderDate": "0001-01-01T00:00:00+00:00",
  "ConversionFactor": 0.0,
  "PriceInCompanyCurrency": null,
  "PriceInCompanyCurrencyCurrencyId": null,
  "SetupPriceInCompanyCurrency": null,
  "SetupPriceInCompanyCurrencyCurrencyId": null,
  "StandardPrice": null,
  "StandardPriceCurrencyId": null,
  "StandardPriceCurrency": null,
  "SetupPrice": null,
  "SetupPriceCurrencyId": null,
  "SetupPriceCurrency": null,
  "ShowPrice": false,
  "PartRowType": 0,
  "LifeCycleState": 0,
  "PartStatus": null,
  "OrderedQuantityInOrderUnit": 0.0,
  "RestQuantity": 0.0,
  "DeliveredQuantity": 0.0,
  "InitialDeliveryDate": null,
  "DesiredDeliveryDate": null,
  "RestQuantityInOrderUnit": 0.0,
  "DeliveredQuantityInOrderUnit": 0.0,
  "CreationContext": 0,
  "ShowFreeTextIn": 0,
  "StatisticalGoodsCodeId": null,
  "StatisticalGoodsCode": null,
  "RowStatus": 0,
  "Version": 0,
  "ArrivalReporting": false,
  "ConfirmedDelayed": false,
  "DelayCommentId": null,
  "DelayComment": null,
  "DelayReasonId": null,
  "DelayReason": null,
  "CodingId": null,
  "Coding": null,
  "IsConfirmed": false,
  "ReceivingInspectionInstructionId": null,
  "ReceivingInspectionInstruction": null,
  "ReceivingInspectionType": 0,
  "ReceivingMessageId": null,
  "ReceivingMessage": null,
  "RequiredForManufacturingOrderNode": null,
  "Weight": 0.0,
  "LinkedStockOrderRowId": null,
  "LinkedSubcontractingManufacturingOrderOperation": null,
  "OriginatingPurchaseOrderDeliveryRowId": null,
  "CausingTransType": 0,
  "CausingOrderRowId": null,
  "RequirementDate": null,
  "PreviousOrderedQuantity": null,
  "PreviousDeliveryDate": null,
  "SubPartParentRowId": null,
  "QuantityRatio": null,
  "ParentOrderId": 0,
  "RowIndex": 0,
  "SumRowId": null,
  "PriceOrigin": 0,
  "DiscountIsLockedFromAutomaticChanges": false,
  "IntrastatTransactionTypeId": null,
  "IntrastatTransactionType": null,
  "TariffAndServiceCodeId": null,
  "TariffAndServiceCode": null,
  "PartConfigurationId": null,
  "RowsGoodsLabel": null,
  "OrderQuantityId": null,
  "OrderQuantity": null,
  "SupplierDrawingNumber": null,
  "SupplierRevisionNumber": null,
  "RowNotes": null,
  "BlanketOrderPurchaseRowId": null,
  "SupplierOrderNumber": null,
  "SupplierOrderRowPosition": null,
  "SupplierPartNumber": null
}
```
