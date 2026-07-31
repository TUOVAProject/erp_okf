---
type: API Entity
title: ManufacturingOrderOperationReportings
description: Represents a manufacturing order operation reporting.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderOperationReporting.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderOperationReporting.html
  title: Monitor API — ManufacturingOrderOperationReporting
module: Manufacturing
api_class: ManufacturingOrderOperationReporting
doc_name: ManufacturingOrderOperationReportings
endpoint: GET /api/v1/Manufacturing/ManufacturingOrderOperationReportings
guid: F134C530-0C75-432C-8B76-8065A897202D
permission: Show manufacturing orders
introduced_in: '24.9'
property_count: 47
references_out:
- /entities/Common/Comment.md
- /entities/Common/Person.md
- /entities/Common/Warehouse.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Manufacturing/ReasonCodeTimeConsumption.md
- /entities/Manufacturing/WorkCenter.md
- /entities/Purchase/PurchaseOrderDeliveryRow.md
referenced_by:
- /entities/Inventory/Location.md
---

# ManufacturingOrderOperationReportings

Represents a manufacturing order operation reporting.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `ManufacturingOrderOperationReporting`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderOperationReportings`
- **Required permission:** Show manufacturing orders
- **GUID:** `F134C530-0C75-432C-8B76-8065A897202D`
- **Introduced in:** 24.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the manufacturing order operation reporting. |
| `OperationId` | `Int64` | no | [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) |  | The business key identifier of the operation that the manufacturing order operation reporting applies. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the manufacturing order operation reporting. |
| `SetupTime` | `TimeSpan?` | yes |  |  | The setup time of the manufacturing order operation reporting. |
| `UnitTime` | `TimeSpan?` | yes |  |  | The unit time of the manufacturing order operation reporting. |
| `WorkCenterId` | `Int64` | no | [WorkCenters](/entities/Manufacturing/WorkCenter.md) |  | The business key identifier of the work center that the manufacturing order operation reporting applies. |
| `EmployeeId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the employee that make the manufacturing order operation reporting. |
| `ReportingEmployeeId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the employee to report as. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse the manufacturing order operation reporting applies to. |
| `ActualReportedDate` | `DateTimeOffset` | no |  |  | The actual reported date of the manufacturing order operation reporting. |
| `PreviousRestQuantity` | `Decimal` | no |  |  | The previous rest quantity of the manufacturing order operation reporting. |
| `RestQuantity` | `Decimal` | no |  |  | The rest quantity of the manufacturing order operation reporting. |
| `OverReceiveQuantity` | `Decimal` | no |  |  | The over receive quantity of the manufacturing order operation reporting. |
| `SetupCost` | `Decimal?` | yes |  |  | The setup cost of the manufacturing order operation reporting. |
| `SetupCostCurrencyId` | `Int64?` | yes |  |  | The business key identifier of the currency that the setup cost of the manufacturing order operation reporting applies to. |
| `SetupCostFactor1` | `Decimal` | no |  |  | The setup cost factor 1 of the manufacturing order operation reporting. |
| `SetupCostFactor2` | `Decimal` | no |  |  | The setup cost factor 2 of the manufacturing order operation reporting. |
| `SetupCostFactor3` | `Decimal` | no |  |  | The setup cost factor 3 of the manufacturing order operation reporting. |
| `SetupCostInForeignCurrency` | `Decimal?` | yes |  |  | The setup cost in foreign currency of the manufacturing order operation reporting. |
| `SetupCostInForeignCurrencyCurrencyId` | `Int64?` | yes |  |  | The business key identifier of the foreign currency that the setup cost of the manufacturing order operation reporting applies to. |
| `UnitCost` | `Decimal?` | yes |  |  | The unit cost of the manufacturing order operation reporting. |
| `UnitCostCurrencyId` | `Int64?` | yes |  |  | The business key identifier of the currency that the unit cost of the manufacturing order operation reporting applies to. |
| `UnitCostFactor1` | `Decimal` | no |  |  | The unit cost factor 1 of the manufacturing order operation reporting. |
| `UnitCostFactor2` | `Decimal` | no |  |  | The unit cost factor 2 of the manufacturing order operation reporting. |
| `UnitCostFactor3` | `Decimal` | no |  |  | The unit cost factor 3 of the manufacturing order operation reporting. |
| `UnitCostInForeignCurrency` | `Decimal?` | yes |  |  | The unit cost in foreign currency of the manufacturing order operation reporting. |
| `UnitCostInForeignCurrencyCurrencyId` | `Int64?` | yes |  |  | The business key identifier of the foreign currency that the unit cost of the manufacturing order operation reporting applies to. |
| `IsSubcontractor` | `Boolean` | no |  |  | Specifies if the operation is subcontracted. |
| `Type` | `Int32` | no |  | enum | The type that the manufacturing order operation reporting is. |
| `SubcontractorRequestedDeliveryDate` | `DateTimeOffset?` | yes |  |  | The date requested by the subcontractor for delivering the manufacturing order operation reporting. |
| `SubcontractorActualDeliveryDate` | `DateTimeOffset?` | yes |  |  | The actual delivery date provided by the subcontractor for the manufacturing order operation reporting. |
| `ReportRestQuantitiesOnSubsequentOperations` | `Boolean` | no |  |  | Indicates whether to report remaining quantities on subsequent operations for the manufacturing order operation reporting. |
| `IsExportedToManagementAccounting` | `Boolean` | no |  |  | Indicates whether the data has been exported to management accounting for the manufacturing order operation reporting. |
| `WipLocation` | `String` | no |  |  | The work in progress location for the manufacturing order operation reporting. |
| `PreviousWipLocation` | `String` | no |  |  | The previous work in progress location for the manufacturing order operation reporting. |
| `OfWichTime` | `TimeSpan?` | yes |  |  | Represents the duration related to a specific event or process. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the manufacturing order operation reporting comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | Additional comments or remarks related to the manufacturing order operation reporting. |
| `ReasonCodeTimeConsumptionId` | `Int64?` | yes | [ReasonCodeTimeConsumptions](/entities/Manufacturing/ReasonCodeTimeConsumption.md) |  | The business key identifier of the reason code associated with time consumption for the manufacturing order operation reporting applies to. |
| `ReasonCodeTimeConsumption` | `ReasonCodeTimeConsumptions` | no | [ReasonCodeTimeConsumptions](/entities/Manufacturing/ReasonCodeTimeConsumption.md) | expandable | The reason code associated with time consumption for the manufacturing order operation reporting applies to. |
| `AutomaticMaterialReporting` | `Boolean` | no |  |  | Indicates whether material reporting is performed automatically for the manufacturing order operation reporting. |
| `PurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](/entities/Purchase/PurchaseOrderDeliveryRow.md) |  | The business key identifier of the delivery row associated with a purchase order for the manufacturing order operation reporting applies to. |
| `PreviousNodeStatus` | `Int32` | no |  | enum | The previous status of the manufacturing order node for the manufacturing order operation reporting applies to. |
| `OriginalApprovedQuantityFromDeliveryRow` | `Decimal?` | yes |  |  | The originally approved quantity from the delivery row for the manufacturing order operation reporting applies to. |
| `ReportingId` | `Int64?` | yes |  |  | The business key identifier of the manufacturing order operation that the reporting applies to. |
| `ReportingTimestamp` | `DateTimeOffset` | no |  |  | The timestamp where the manufacturing order operation reporting occurred. |
| `RowNumber` | `Int32` | no |  |  | The row number of the manufacturing order operation reporting. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Regular` | 0 |
| `SendToSubcontractor` | 1 |
| `ReceiveFromSubcontractor` | 2 |
| `CancelRest` | 3 |
| `MaterialOnly` | 4 |
| `SubcontractorInvoicePrice` | 5 |
| `RecordingTerminal` | 6 |
| `AdjustRecording` | 7 |
| `UndoRegular` | 8 |
| `UndoRecordingTerminal` | 9 |
| `UndoAdjustRecording` | 10 |
| `SubcontractorPosteriorReport` | 11 |
| `SubcontractorCostsManualReport` | 12 |
| `PickWorkCenter` | 13 |

### PreviousNodeStatus

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `Registrered` | 1 |
| `Printed` | 2 |
| `Started` | 3 |
| `Finished` | 4 |
| `PostCalculated` | 5 |
| `Delivered` | 6 |
| `Historical` | 9 |


## Referenced by

**Inventory**

- [Locations](/entities/Inventory/Location.md) — `ManufacturingOrderMaterialId` (FK)


## Example

```json
{
  "Id": 0,
  "OperationId": 0,
  "Quantity": 0.0,
  "SetupTime": null,
  "UnitTime": null,
  "WorkCenterId": 0,
  "EmployeeId": null,
  "ReportingEmployeeId": null,
  "WarehouseId": 0,
  "ActualReportedDate": "0001-01-01T00:00:00+00:00",
  "PreviousRestQuantity": 0.0,
  "RestQuantity": 0.0,
  "OverReceiveQuantity": 0.0,
  "SetupCost": null,
  "SetupCostCurrencyId": null,
  "SetupCostFactor1": 0.0,
  "SetupCostFactor2": 0.0,
  "SetupCostFactor3": 0.0,
  "SetupCostInForeignCurrency": null,
  "SetupCostInForeignCurrencyCurrencyId": null,
  "UnitCost": null,
  "UnitCostCurrencyId": null,
  "UnitCostFactor1": 0.0,
  "UnitCostFactor2": 0.0,
  "UnitCostFactor3": 0.0,
  "UnitCostInForeignCurrency": null,
  "UnitCostInForeignCurrencyCurrencyId": null,
  "IsSubcontractor": false,
  "Type": 0,
  "SubcontractorRequestedDeliveryDate": null,
  "SubcontractorActualDeliveryDate": null,
  "ReportRestQuantitiesOnSubsequentOperations": false,
  "IsExportedToManagementAccounting": false,
  "WipLocation": null,
  "PreviousWipLocation": null,
  "OfWichTime": null,
  "CommentId": null,
  "Comment": null,
  "ReasonCodeTimeConsumptionId": null,
  "ReasonCodeTimeConsumption": null,
  "AutomaticMaterialReporting": false,
  "PurchaseOrderDeliveryRowId": null,
  "PreviousNodeStatus": 0,
  "OriginalApprovedQuantityFromDeliveryRow": null,
  "ReportingId": null,
  "ReportingTimestamp": "0001-01-01T00:00:00+00:00",
  "RowNumber": 0
}
```
