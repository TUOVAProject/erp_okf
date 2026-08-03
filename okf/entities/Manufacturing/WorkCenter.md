---
type: API Entity
title: WorkCenters
description: Represents a manufacturing work center.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.WorkCenter.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.WorkCenter.html
  title: Monitor API — WorkCenter
module: Manufacturing
api_class: WorkCenter
doc_name: WorkCenters
endpoint: GET /api/v1/Manufacturing/WorkCenters
guid: 2A2247AB-2CB4-40BD-B5F3-2E2D3DE37170
permission: Show work center
introduced_in: '2.18'
property_count: 22
references_out:
- /entities/Common/Comment.md
- /entities/Common/Warehouse.md
- /entities/Manufacturing/ProductionCalendarException.md
- /entities/Manufacturing/WorkCenterCostFactorGroup.md
- /entities/Manufacturing/WorkCenterManufacturingPrintSettings.md
- /entities/TimeRecording/PersonWorkCenter.md
referenced_by:
- /entities/Accounting/FixedAsset.md
- /entities/Inventory/CaseEntry.md
- /entities/Manufacturing/AlternativeOperationRow.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Manufacturing/ManufacturingOrderOperationControlDataRow.md
- /entities/Manufacturing/ManufacturingOrderOperationReporting.md
- /entities/Manufacturing/OperationRowControlDataRow.md
- /entities/Manufacturing/ProductionCalendarException.md
- /entities/Manufacturing/WorkCenterCostFactorGroup.md
- /entities/TimeRecording/PersonWorkCenter.md
- /entities/TimeRecording/WorkInterval.md
---

# WorkCenters

Represents a manufacturing work center.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `WorkCenter`
- **Endpoint:** `GET /api/v1/Manufacturing/WorkCenters`
- **Required permission:** Show work center
- **GUID:** `2A2247AB-2CB4-40BD-B5F3-2E2D3DE37170`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the work center. |
| `Number` | `String` | no |  | unique, max length 8 | The human readable identifier of the work center. |
| `Description` | `String` | no |  |  | The translated description of the work center. |
| `OperationDescription` | `String` | no |  |  | The translated operation description of the work center. |
| `Type` | `Int32` | no |  | enum | The work center type. |
| `DepartmentId` | `Int64` | no |  |  | The business key identifier of the department that the work center belongs to. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the warehouse that the work center belongs to. References Warehouses . |
| `Warehouse` | `Warehouses` | no | [Warehouses](../Common/Warehouse.md) | expandable | The warehouse that the work center belongs to. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the work center comment. References Comments . |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The work center comment. |
| `ManufacturingPrintSettings` | `WorkCenterManufacturingPrintSettings[]` | no | [WorkCenterManufacturingPrintSettings](WorkCenterManufacturingPrintSettings.md) | expandable, collection, since 2.28 | The print settings for manufacturing order documents. |
| `CostFactorGroups` | `WorkCenterCostFactorGroups[]` | no | [WorkCenterCostFactorGroups](WorkCenterCostFactorGroup.md) | expandable, collection, since 2.46 | The cost factor groups that belong to the work center. |
| `TimePrecision` | `Int32` | no |  | enum, since 24.3 | Time precision for the work center |
| `BasicTime` | `TimeSpan` | no |  | since 24.3 | Basic time (capacity per day) |
| `NumberOfPlanningUnits` | `Decimal` | no |  | since 24.3 | Number of planning units, can be machines or persons depending on the work center type. |
| `NumberOfFlows` | `Decimal` | no |  | since 24.3 | Number of machines per order or number of persons per order depending on the work center type. |
| `AvailabilityFactor` | `Decimal` | no |  | since 24.3 | Availability factor in percent for the work center. |
| `SimulationFactor` | `Decimal` | no |  | since 24.3 | Simulation factor in percent for the work center. |
| `UnitStaffFactor` | `Decimal` | no |  | since 24.3 | Indicates how large (in percent) a share of the operating unit time that is staffed for the work center. |
| `SetupStaffFactor` | `Decimal` | no |  | since 24.3 | Indicates how large (in percent) a share of the operating setup time that is staffed for the work center. |
| `Employees` | `PersonWorkCenters[]` | no | [PersonWorkCenters](../TimeRecording/PersonWorkCenter.md) | expandable, collection, since 24.3 | Specifies the persons that should be allowed to select work from this work center. |
| `ProductionCalendarExceptions` | `ProductionCalendarExceptions[]` | no | [ProductionCalendarExceptions](ProductionCalendarException.md) | expandable, collection, since 24.3 | Specifies the production calendar exceptions for this work center. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Machine` | 0 |
| `ManualWork` | 1 |
| `SubContract` | 2 |
| `Pool` | 3 |
| `Pick` | 4 |
| `Staffing` | 5 |

### TimePrecision

| Name | Value |
| --- | ---: |
| `Day` | 0 |
| `Schedule` | 1 |
| `Hourly` | 2 |


## Referenced by

**Accounting**

- [FixedAssets](../Accounting/FixedAsset.md) — `WorkCenterId` (FK)

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `ReasonWorkCenterId` (FK)

**Manufacturing**

- [AlternativeOperationRows](AlternativeOperationRow.md) — `WorkCenterId` (FK)
- [ManufacturingOrderOperationControlDataRows](ManufacturingOrderOperationControlDataRow.md) — `WorkCenterId` (FK)
- [ManufacturingOrderOperationReportings](ManufacturingOrderOperationReporting.md) — `WorkCenterId` (FK)
- [ManufacturingOrderOperations](ManufacturingOrderOperation.md) — `WorkCenterId` (FK)
- [OperationRowControlDataRows](OperationRowControlDataRow.md) — `WorkCenterId` (FK)
- [ProductionCalendarExceptions](ProductionCalendarException.md) — `WorkCenterId` (FK)
- [WorkCenterCostFactorGroups](WorkCenterCostFactorGroup.md) — `ParentId` (FK)

**TimeRecording**

- [PersonWorkCenters](../TimeRecording/PersonWorkCenter.md) — `WorkCenterId` (FK)
- [WorkIntervals](../TimeRecording/WorkInterval.md) — `WorkCenterId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": null,
  "Description": null,
  "OperationDescription": null,
  "Type": 0,
  "DepartmentId": 0,
  "WarehouseId": 0,
  "Warehouse": null,
  "CommentId": null,
  "Comment": null,
  "ManufacturingPrintSettings": null,
  "CostFactorGroups": null,
  "TimePrecision": 0,
  "BasicTime": "00:00:00",
  "NumberOfPlanningUnits": 0.0,
  "NumberOfFlows": 0.0,
  "AvailabilityFactor": 0.0,
  "SimulationFactor": 0.0,
  "UnitStaffFactor": 0.0,
  "SetupStaffFactor": 0.0,
  "Employees": null,
  "ProductionCalendarExceptions": null
}
```
