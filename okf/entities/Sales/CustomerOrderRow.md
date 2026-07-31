---
type: API Entity
title: CustomerOrderRows
description: Represents a customer order row.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderRow.html
  title: Monitor API — CustomerOrderRow
module: Sales
api_class: CustomerOrderRow
doc_name: CustomerOrderRows
endpoint: GET /api/v1/Sales/CustomerOrderRows
guid: 65969D1D-6139-4C75-8EA2-1A271448674A
permission: Show customer orders
introduced_in: '2.18'
property_count: 107
references_out:
- /entities/Accounting/Coding.md
- /entities/Accounting/FixedAsset.md
- /entities/Common/Currency.md
- /entities/Common/PartConfiguration.md
- /entities/Common/Revision.md
- /entities/Common/StatisticalGoodsCode.md
- /entities/Common/TariffAndServiceCode.md
- /entities/Common/TransactionTypeIntrastat.md
- /entities/Common/TransferProfile.md
- /entities/Common/Unit.md
- /entities/Common/VatRate.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/BlanketOrderSalesRow.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderOrderRowDiscount.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/OrderQuantityCustomerOrder.md
referenced_by:
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderDeliveryRow.md
- /entities/Sales/CustomerOrderOrderRowDiscount.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/CustomerOrderRowInflow.md
- /entities/Sales/SalesAgreementBasisRow.md
- /entities/Sales/WithdrawalInformationRow.md
---

# CustomerOrderRows

Represents a customer order row.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `CustomerOrderRow`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderRows`
- **Required permission:** Show customer orders
- **GUID:** `65969D1D-6139-4C75-8EA2-1A271448674A`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the row. |
| `Position` | `Int64?` | yes |  |  | The relative numeric position of the row. |
| `OrderRowType` | `Int32` | no |  | enum | The type of the row. |
| `PartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the part set for the row. |
| `Part` | `Parts` | no | [Parts](/entities/Inventory/Part.md) | expandable | The part of the row. |
| `EntityIdentityString` | `String` | no |  | max length 20 | The human readable identifier of the entity subject of the row. |
| `AdditionalRowDescription` | `String` | no |  | max length 80 | The additional row description of the row. |
| `FreeTextHtml` | `String` | no |  | max length 0 | The free text row's rich text HTML row data. |
| `FreeText` | `String` | no |  | max length 0 | The free text row's raw text. |
| `ParentRowId` | `Int64?` | yes | [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) |  | The business key identifier of the current row's parent. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |  | The delivery date set for the row. |
| `RevisionId` | `Int64?` | yes | [Revisions](/entities/Common/Revision.md) |  | The business key identifier of the row's revision. |
| `Revision` | `Revisions` | no | [Revisions](/entities/Common/Revision.md) |  | The revision of the row. |
| `OrderedQuantity` | `Decimal` | no |  |  | The ordered quantity of the row. |
| `Price` | `Decimal?` | yes |  |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the row price currency. |
| `Discount` | `Decimal` | no |  |  | The discount in percent set for the row. |
| `ToolId` | `Int64?` | yes |  | **deprecated since 2.48** | The business key identifier of the tool of the row. _(Replaced by Part)_ |
| `UnitId` | `Int64?` | yes | [Units](/entities/Common/Unit.md) |  | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](/entities/Common/Unit.md) | expandable | The unit of the row. |
| `VatRateId` | `Int64` | no | [VatRates](/entities/Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse that the row belongs to. |
| `WeightPerUnit` | `Decimal?` | yes |  |  | The weight per unit of the row. |
| `OrderDate` | `DateTimeOffset` | no |  |  | The order date of the row. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor of the row. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The row price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the company currency. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |  | The setup price of the row in the company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes |  |  | The business key identifier of the company currency. |
| `StandardPrice` | `Decimal?` | yes |  |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the row's standard price currency. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the row's setup price currency. |
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
| `CustomerCommitmentLevel` | `Int32` | no |  | enum | The customer commitment level of the row. |
| `PickingQuantity` | `Decimal?` | yes |  |  | The picking quantity of the row. |
| `AlternatePreparationCode` | `String` | no |  | max length 200 | The alternate preparation code of the row. |
| `Storage` | `String` | no |  | max length 35 | The storage specified by the row. |
| `ShowFreeTextIn` | `Int32` | no |  | bitmask, enum | Specifies which documents the free text row data will appear on. |
| `CreateManufacturingOrder` | `Boolean` | no |  |  | Specifies if a manufacturing order should be created for the row. |
| `CreatePurchaseOrder` | `Boolean` | no |  |  | Specifies if a purchase order should be created for the row. |
| `LinkedPurchaseOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) |  | The business key identifier of the row's linked purchase order row. |
| `LinkedManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) |  | The business key identifier of the row's linked manufacturing order. |
| `LinkedWithdrawalReservationId` | `Int64?` | yes |  |  | The business key identifier of the row's linked withdrawal reservation. References PartWithdrawalReservation. |
| `PlannedDateOfArrival` | `DateTimeOffset?` | yes |  | **deprecated since 24.3** | The planned date of arrival specified by the row. _(Unavailable)_ |
| `BacklogAmount` | `Decimal` | no |  |  | The backlog amount on the row. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](/entities/Common/StatisticalGoodsCode.md) |  | The business key identifier of the row's statistical goods code. |
| `RowStatus` | `Int32` | no |  | bitmask, enum | The status of the customer order row. |
| `ParentOrderId` | `Int64` | no | [CustomerOrders](/entities/Sales/CustomerOrder.md) | since 2.27 | The business key identifier of the rows parent order. |
| `Dock` | `String` | no |  | max length 35, since 2.28 | The dock for the row (EDI). |
| `DockName` | `String` | no |  | max length 80, since 2.28 | The dock description for the row (EDI). |
| `KanbanNumber` | `String` | no |  | max length 80, since 2.28 | The kanban number for the row (EDI). |
| `CustomerOrderRowPosition` | `String` | no |  | max length 15, since 2.30 | The customer's order row position for the row. |
| `ReferenceNumberManufacturing` | `String` | no |  | max length 80, since 2.30 | The reference number for manufacturing for the row. |
| `ReferenceNumberDelivery` | `String` | no |  | max length 80, since 2.30 | The reference number for delivery for the row. |
| `ShowDeliveryDate` | `Boolean` | no |  | since 2.30 | Specifies if the delivery date is shown on the row |
| `CreatedFrom` | `Int32` | no |  | enum, since 2.30 | Specifies what the row was created from. |
| `FixedAssetId` | `Int64?` | yes | [FixedAssets](/entities/Accounting/FixedAsset.md) | since 2.30 | The business key identifier of the rows fixed asset. |
| `LinkedStockOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) | since 2.30 | The business key identifier of the rows linked stock order row. |
| `LinkedStockOrderRow` | `PurchaseOrderRows` | no | [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) | expandable, since 2.30 | The linked stock order row for the row. |
| `NewFinishDate` | `DateTimeOffset?` | yes |  | since 2.30 | The new finish date for the row. |
| `TransferStatus` | `Int32` | no |  | enum, since 2.30 | The transfer status for the row. |
| `TransferProfileId` | `Int64?` | yes | [TransferProfiles](/entities/Common/TransferProfile.md) | since 2.30 | The business key identifier of the rows transfer profile. |
| `OrderNumberInRemoteCompany` | `String` | no |  | max length 15, since 2.30 | The order number in remote company for the row. |
| `PositionInRemoteCompany` | `Int64?` | yes |  | since 2.30 | The position in remote company for the row. |
| `CodingId` | `Int64?` | yes |  | since 2.30 | The business key identifier of the rows coding. |
| `Coding` | `Codings` | no | [Codings](/entities/Accounting/Coding.md) | expandable, since 2.33 | The coding of the row. |
| `PaymentPlanRowId` | `Int64?` | yes |  | since 2.30 | The business key identifier of the rows customer order payment plan row. |
| `IsCreditedPaymentPlanRow` | `Boolean` | no |  | since 2.30 | Specifies if the row is a credited payment plan row. |
| `IsIncludedInPaymentPlan` | `Boolean` | no |  | since 2.30 | Specifies if the row is included in payment plan. |
| `Status` | `Int32` | no |  | enum, since 2.30 | The status of the customer order. |
| `ProformaStatus` | `Int32` | no |  | enum, since 2.30 | The status of the row's proforma invoice. |
| `ProformaNumber` | `Int64?` | yes |  | since 2.30 | The proforma number of the row. |
| `SubPartParentRowId` | `Int64?` | yes | [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) | since 2.30 | The business key identifier of the sub part row's parent row. |
| `QuantityRatio` | `Decimal?` | yes |  | since 2.30 | The quantity ratio of the row. |
| `RowIndex` | `Int32?` | yes |  | since 2.30 | The index of the row. |
| `SumRowId` | `Int64?` | yes | [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) | since 2.30 | The business key identifier of the row's sum row. |
| `PriceOrigin` | `Int32?` | yes |  | enum, since 2.30 | The price origin of the row. |
| `PriceOriginPriceListId` | `Int64?` | yes |  | since 2.30 | The business key identifier of the row's original pricelist. |
| `DiscountIsLockedFromAutomaticChanges` | `Boolean` | no |  | since 2.30 | Specifies if the row's discount is locked from automatic changes. |
| `IntrastatTransactionTypeId` | `Int64?` | yes | [TransactionTypeIntrastats](/entities/Common/TransactionTypeIntrastat.md) | since 2.30 | The business key identifier of the row's intrastat transaction type. |
| `IntrastatTransactionType` | `TransactionTypeIntrastats` | no | [TransactionTypeIntrastats](/entities/Common/TransactionTypeIntrastat.md) | expandable, since 2.30 | The intrastat transaction type of the row. |
| `TariffAndServiceCodeId` | `Int64?` | yes | [TariffAndServiceCodes](/entities/Common/TariffAndServiceCode.md) | since 2.30 | The business key identifier of the row's tariff and service code. |
| `TariffAndServiceCode` | `TariffAndServiceCodes` | no | [TariffAndServiceCodes](/entities/Common/TariffAndServiceCode.md) | expandable, since 2.30 | The tariff and service code of the row. |
| `PartConfigurationId` | `Int64?` | yes |  | since 2.30 | The business key identifier of the row's part configuration. |
| `RowsGoodsLabel` | `String` | no |  | max length 80, since 2.45 | The rows goods label specified by the row. |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityCustomerOrders](/entities/Sales/OrderQuantityCustomerOrder.md) | since 22.6 | The business key identifier of order quantity. |
| `OrderQuantity` | `OrderQuantityCustomerOrders` | no | [OrderQuantityCustomerOrders](/entities/Sales/OrderQuantityCustomerOrder.md) | expandable, since 22.6 | Order quantity that holds the partial quantities. |
| `CustomerOrderTransferRowIdentifier` | `Guid?` | yes |  | since 23.2 | The customer order transfer row identifier. |
| `PartConfigurationIdInRemoteCompany` | `Int64?` | yes | [PartConfigurations](/entities/Common/PartConfiguration.md) | since 23.2 | The business key identifier of the row's part configuration in the remote company. |
| `PriceLockedFromAutomaticChanges` | `Boolean?` | yes |  | since 24.2 | Specifies if the rows price is locked from automatic changes. |
| `SerialNumberInformation` | `SerialNumberOrderRowInformation[]` | no |  | expandable, collection, since 24.4 | The serial number information of customer order row |
| `DiscountRows` | `CustomerOrderOrderRowDiscounts[]` | no | [CustomerOrderOrderRowDiscounts](/entities/Sales/CustomerOrderOrderRowDiscount.md) | expandable, collection, since 24.8 | The discount rows for the row. |
| `ComparativePrice` | `Decimal?` | yes |  | since 25.2 | The manually edited comparative price for the row. Note if this price is automatically calculated it is not stored here. |
| `ComparativePriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) | since 25.2 | The business key identifier of the row's manually edited comparative price currency. |
| `BlanketOrderSalesRowId` | `Int64?` | yes | [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) | since 26.1 | The business key identifier of the row's blanket order sales row. |

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

### CustomerCommitmentLevel

| Name | Value |
| --- | ---: |
| `FixedOrder` | 1 |
| `Manufacture` | 2 |
| `BuyMaterial` | 3 |
| `Forecast` | 4 |

### ShowFreeTextIn (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Quote` | 1 |
| `Acknowledgement` | 2 |
| `DeliveryNote` | 4 |
| `Invoice` | 8 |
| `ProFormaInvoice` | 16 |

### RowStatus (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `OrderConfirmationPrinted` | 1 |
| `DeliveryNotePrinted` | 2 |

### CreatedFrom

| Name | Value |
| --- | ---: |
| `Client` | 0 |
| `M2M` | 1 |
| `EDI` | 2 |
| `DeliverySchedule` | 3 |
| `DeliveryScheduleCallOff` | 4 |

### TransferStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Partial` | 1 |
| `Fully` | 2 |

### Status

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `Registered` | 1 |
| `OrderConfirmationPrinted` | 2 |
| `CanNotConfirmDeliveryTime` | 3 |
| `DeliveryNotePrinted` | 4 |
| `PartiallyDelivered` | 5 |
| `History` | 9 |

### ProformaStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `ApprovedForPrint` | 1 |
| `Printed` | 2 |

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

**Purchase**

- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `LinkedStockOrderRowId` (FK)

**Sales**

- [CustomerOrderDeliveryRows](/entities/Sales/CustomerOrderDeliveryRow.md) — `CustomerOrderRowId` (FK)
- [CustomerOrderOrderRowDiscounts](/entities/Sales/CustomerOrderOrderRowDiscount.md) — `OrderRowId` (FK)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `OrderRow` (expand)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `OrderRowId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `ParentRowId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `SubPartParentRowId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `SumRowId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `Rows` (expand)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `CustomerOrderRowId` (FK)
- [WithdrawalInformationRow](/entities/Sales/WithdrawalInformationRow.md) — `CustomerOrderRowId` (FK)
- [WithdrawalInformationRow](/entities/Sales/WithdrawalInformationRow.md) — `ParentCustomerOrderRowId` (FK)


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
  "Discount": 0.0,
  "ToolId": null,
  "UnitId": null,
  "Unit": null,
  "VatRateId": 0,
  "WarehouseId": 0,
  "WeightPerUnit": null,
  "OrderDate": "0001-01-01T00:00:00+00:00",
  "ConversionFactor": 0.0,
  "PriceInCompanyCurrency": null,
  "PriceInCompanyCurrencyCurrencyId": null,
  "SetupPriceInCompanyCurrency": null,
  "SetupPriceInCompanyCurrencyCurrencyId": null,
  "StandardPrice": null,
  "StandardPriceCurrencyId": null,
  "SetupPrice": null,
  "SetupPriceCurrencyId": null,
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
  "CustomerCommitmentLevel": 0,
  "PickingQuantity": null,
  "AlternatePreparationCode": null,
  "Storage": null,
  "ShowFreeTextIn": 0,
  "CreateManufacturingOrder": false,
  "CreatePurchaseOrder": false,
  "LinkedPurchaseOrderRowId": null,
  "LinkedManufacturingOrderId": null,
  "LinkedWithdrawalReservationId": null,
  "PlannedDateOfArrival": null,
  "BacklogAmount": 0.0,
  "StatisticalGoodsCodeId": null,
  "RowStatus": 0,
  "ParentOrderId": 0,
  "Dock": null,
  "DockName": null,
  "KanbanNumber": null,
  "CustomerOrderRowPosition": null,
  "ReferenceNumberManufacturing": null,
  "ReferenceNumberDelivery": null,
  "ShowDeliveryDate": false,
  "CreatedFrom": 0,
  "FixedAssetId": null,
  "LinkedStockOrderRowId": null,
  "LinkedStockOrderRow": null,
  "NewFinishDate": null,
  "TransferStatus": 0,
  "TransferProfileId": null,
  "OrderNumberInRemoteCompany": null,
  "PositionInRemoteCompany": null,
  "CodingId": null,
  "Coding": null,
  "PaymentPlanRowId": null,
  "IsCreditedPaymentPlanRow": false,
  "IsIncludedInPaymentPlan": false,
  "Status": 0,
  "ProformaStatus": 0,
  "ProformaNumber": null,
  "SubPartParentRowId": null,
  "QuantityRatio": null,
  "RowIndex": null,
  "SumRowId": null,
  "PriceOrigin": null,
  "PriceOriginPriceListId": null,
  "DiscountIsLockedFromAutomaticChanges": false,
  "IntrastatTransactionTypeId": null,
  "IntrastatTransactionType": null,
  "TariffAndServiceCodeId": null,
  "TariffAndServiceCode": null,
  "PartConfigurationId": null,
  "RowsGoodsLabel": null,
  "OrderQuantityId": null,
  "OrderQuantity": null,
  "CustomerOrderTransferRowIdentifier": null,
  "PartConfigurationIdInRemoteCompany": null,
  "PriceLockedFromAutomaticChanges": null,
  "SerialNumberInformation": null,
  "DiscountRows": null,
  "ComparativePrice": null,
  "ComparativePriceCurrencyId": null,
  "BlanketOrderSalesRowId": null
}
```
