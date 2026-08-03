---
type: API Entity
title: ManufacturingOrderOperations
description: Represents a manufacturing order operation.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderOperation.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderOperation.html
  title: Monitor API — ManufacturingOrderOperation
module: Manufacturing
api_class: ManufacturingOrderOperation
doc_name: ManufacturingOrderOperations
endpoint: GET /api/v1/Manufacturing/ManufacturingOrderOperations
guid: C1A9916E-607F-4720-9941-EEC496C92E2D
permission: Show manufacturing orders
introduced_in: '2.18'
property_count: 42
references_out:
- /entities/Common/Comment.md
- /entities/Inventory/Part.md
- /entities/Manufacturing/ManualOperationStatus.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Manufacturing/ManufacturingOrderMaterial.md
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Manufacturing/ManufacturingOrderOperationControlDataRow.md
- /entities/Manufacturing/OperationRow.md
- /entities/Manufacturing/OrderQuantityManufacturingOrderOperation.md
- /entities/Manufacturing/WorkCenter.md
referenced_by:
- /entities/Common/DelegatedWork.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Manufacturing/ManufacturingOrderOperationControlDataRow.md
- /entities/Manufacturing/ManufacturingOrderOperationReporting.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/TimeRecording/IndirectWorkCode.md
- /entities/TimeRecording/StandbyWork.md
- /entities/TimeRecording/WorkInterval.md
---

# ManufacturingOrderOperations

Represents a manufacturing order operation.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `ManufacturingOrderOperation`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderOperations`
- **Required permission:** Show manufacturing orders
- **GUID:** `C1A9916E-607F-4720-9941-EEC496C92E2D`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the manufacturing order operation. |
| `Priority` | `Int32?` | yes |  |  | The priority of the manufacturing order operation. Can be null. |
| `WorkCenterId` | `Int64` | no | [WorkCenters](WorkCenter.md) |  | The business key identifier of the manufacturing order operation's work center. |
| `PartId` | `Int64` | no | [Part](../Inventory/Part.md) |  | The business key identifier of the manufacturing order operation's part. |
| `Part` | `Parts` | no | [Parts](../Inventory/Part.md) | expandable | The manufacturing order operation's part. |
| `PlannedQuantity` | `Decimal` | no |  |  | The planned quantity of the manufacturing order operation. |
| `ReportedQuantity` | `Decimal` | no |  |  | The reported quantity of the manufacturing order operation. |
| `RestQuantity` | `Decimal` | no |  |  | The remaining quantity of the manufacturing order operation. |
| `ReportedSetupTime` | `TimeSpan` | no |  |  | The reported setup time of the manufacturing order operation. |
| `ReportedUnitTime` | `TimeSpan` | no |  |  | The reported unit time of the manufacturing order operation. |
| `RejectedQuantity` | `Decimal` | no |  |  | The rejected quantity of the manufacturing order operation. |
| `WipLocation` | `String` | no |  |  | The work-in-progress location of the manufacturing order operation. |
| `ReportNumber` | `Int64` | no |  |  | The report number of the manufacturing order operation. |
| `InstructionCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the manufacturing order operation's instruction comment. |
| `InstructionComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The manufacturing order operation's instruction comment. |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](ManufacturingOrder.md) |  | The business key identifier of the manufacturing order that the manufacturing order operation belongs to. |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](ManufacturingOrderNode.md) | since 2.30 | The business key identifier of the manufacturing order node that the manufacturing order operation belongs to. |
| `OperationNumber` | `Int32` | no |  |  | The operation number of the manufacturing order operation. |
| `PlannedSetupTime` | `TimeSpan` | no |  |  | The planned setup time of the manufacturing order operation. |
| `PlannedUnitTime` | `TimeSpan` | no |  |  | The planned unit time of the manufacturing order operation. |
| `PlannedStartDate` | `DateTimeOffset` | no |  | since 2.27 | The planned start date of the manufacturing order operation. |
| `PlannedFinishDate` | `DateTimeOffset` | no |  | since 2.27 | The planned finish date of the manufacturing order operation. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  | since 2.27 | The actual (reported) start date of the manufacturing order operation. |
| `ActualFinishDate` | `DateTimeOffset?` | yes |  | since 2.27 | The actual (reported) finish date of the manufacturing order operation. |
| `OperationRowId` | `Int64?` | yes | [OperationRows](OperationRow.md) | since 2.41 | The business key identifier of the operation row that the manufacturing order operation is based on. Can be null if the manufacturing order operation is added manually. |
| `OperationRow` | `OperationRows` | no | [OperationRows](OperationRow.md) | expandable, since 2.41 | The operation row that the manufacturing order operation is based on. |
| `Status` | `Int32` | no |  | enum, since 2.50 | The status of the manufacturing order operation's status. |
| `WorkshopOperationStatus` | `Int32` | no |  | enum, since 2.50 | The workshop status of the manufacturing order operation's status. |
| `BundleId` | `Int64?` | yes |  | since 2.52 | An generated id that is common for a collection of operations. |
| `Description` | `String` | no |  | since 2.54 | The translated description of the manufacturing order operation. |
| `ControlDataRows` | `ManufacturingOrderOperationControlDataRows[]` | no | [ManufacturingOrderOperationControlDataRows](ManufacturingOrderOperationControlDataRow.md) | expandable, collection, since 22.5 | The control data rows. |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityManufacturingOrderOperations](OrderQuantityManufacturingOrderOperation.md) | since 22.6 | The business key identifier of order quantity. |
| `OrderQuantity` | `OrderQuantityManufacturingOrderOperations` | no | [OrderQuantityManufacturingOrderOperations](OrderQuantityManufacturingOrderOperation.md) | expandable, since 22.6 | Order quantity that holds the partial quantities. |
| `ClearedStatus` | `Boolean` | no |  | since 23.3 | Specifies if the status is cleared. |
| `OnPriorityPlan` | `Boolean` | no |  | since 25.2 | Indicates if the operation is shown in priority plan. |
| `ManualOperationStatusId` | `Int64?` | yes | [ManualOperationStatuses](ManualOperationStatus.md) | since 25.2 | The business key identifier of manual operation status. |
| `ManualOperationStatus` | `ManualOperationStatuses` | no | [ManualOperationStatuses](ManualOperationStatus.md) | expandable, since 25.2 | The manual operation status. |
| `Materials` | `ManufacturingOrderMaterials[]` | no | [ManufacturingOrderMaterials](ManufacturingOrderMaterial.md) | expandable, collection, since 24.4 | The manufacturing order materials of the operation. |
| `FixedLeadTime` | `TimeSpan?` | yes |  | since 24.6 | The fixed lead time of the manufacturing order operation. |
| `UnitStaffingFactor` | `Decimal?` | yes |  | since 25.8 | The unit staffing factor of the manufacturing order operation. |
| `SetupStaffingFactor` | `Decimal?` | yes |  | since 25.8 | The setup staffing factor of the manufacturing order operation. |
| `IsPlannedTimeCalculated` | `Boolean` | no |  | since 26.5 | Indicates that the planned time of the operation was calculated at order creation (from a part-configurator formula or aggregated from fictitious sub-parts) and must not be overwritten when the work center is changed. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Started` | 1 |
| `PartiallyShipped` | 2 |
| `FullyShipped` | 3 |
| `PartiallyReported` | 4 |
| `Finished` | 5 |

### WorkshopOperationStatus

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `InProgress` | 1 |
| `ClockedOut` | 2 |
| `Interrupted` | 3 |
| `PartiallyReported` | 4 |
| `SetupTime` | 5 |
| `IsStandingBy` | 6 |
| `Finished` | 9 |


## Referenced by

**Common**

- [DelegatedWork](../Common/DelegatedWork.md) — `OperationId` (FK)

**Manufacturing**

- [ManufacturingOrderOperationControlDataRows](ManufacturingOrderOperationControlDataRow.md) — `ManufacturingOrderOperationId` (FK)
- [ManufacturingOrderOperationReportings](ManufacturingOrderOperationReporting.md) — `OperationId` (FK)
- [ManufacturingOrders](ManufacturingOrder.md) — `Operations` (expand)

**Purchase**

- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `LinkedSubcontractingManufacturingOrderOperation` (FK)

**TimeRecording**

- [IndirectWorkCodes](../TimeRecording/IndirectWorkCode.md) — `AffectsOrder` (FK)
- [StandbyWorks](../TimeRecording/StandbyWork.md) — `Operation` (expand)
- [StandbyWorks](../TimeRecording/StandbyWork.md) — `OperationId` (FK)
- [WorkIntervals](../TimeRecording/WorkInterval.md) — `OperationId` (FK)


## Example

```json
{
  "Id": 0,
  "Priority": null,
  "WorkCenterId": 0,
  "PartId": 0,
  "Part": null,
  "PlannedQuantity": 0.0,
  "ReportedQuantity": 0.0,
  "RestQuantity": 0.0,
  "ReportedSetupTime": "00:00:00",
  "ReportedUnitTime": "00:00:00",
  "RejectedQuantity": 0.0,
  "WipLocation": null,
  "ReportNumber": 0,
  "InstructionCommentId": null,
  "InstructionComment": null,
  "ManufacturingOrderId": 0,
  "ManufacturingOrderNodeId": 0,
  "OperationNumber": 0,
  "PlannedSetupTime": "00:00:00",
  "PlannedUnitTime": "00:00:00",
  "PlannedStartDate": "0001-01-01T00:00:00+00:00",
  "PlannedFinishDate": "0001-01-01T00:00:00+00:00",
  "ActualStartDate": null,
  "ActualFinishDate": null,
  "OperationRowId": null,
  "OperationRow": null,
  "Status": 0,
  "WorkshopOperationStatus": 0,
  "BundleId": null,
  "Description": null,
  "ControlDataRows": null,
  "OrderQuantityId": null,
  "OrderQuantity": null,
  "ClearedStatus": false,
  "OnPriorityPlan": false,
  "ManualOperationStatusId": null,
  "ManualOperationStatus": null,
  "Materials": null,
  "FixedLeadTime": null,
  "UnitStaffingFactor": null,
  "SetupStaffingFactor": null,
  "IsPlannedTimeCalculated": false
}
```
