---
type: API Entity
title: OperationRows
description: Represents an operation row.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.OperationRow.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.OperationRow.html
  title: Monitor API — OperationRow
module: Manufacturing
api_class: OperationRow
doc_name: OperationRows
endpoint: GET /api/v1/Manufacturing/OperationRows
guid: 6BC59318-2E5D-4097-954D-678C90EACD77
permission: Show part
introduced_in: '2.18'
property_count: 38
references_out:
- /entities/Common/Comment.md
- /entities/Common/Currency.md
- /entities/Common/ExtraField.md
- /entities/Manufacturing/AlternativeOperationRow.md
- /entities/Manufacturing/OperationRowControlDataRow.md
referenced_by:
- /entities/Manufacturing/AlternativeOperationRow.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Manufacturing/OperationRowControlDataRow.md
- /entities/Manufacturing/Preparation.md
---

# OperationRows

Represents an operation row.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `OperationRow`
- **Endpoint:** `GET /api/v1/Manufacturing/OperationRows`
- **Required permission:** Show part
- **GUID:** `6BC59318-2E5D-4097-954D-678C90EACD77`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the material row. |
| `OperationNumber` | `Int32` | no |  |  | The operation number of the operation row. |
| `SubcontractPartId` | `Int64?` | yes |  |  | The business key identifier of the operation row's subcontract part. |
| `SupplierId` | `Int64?` | yes |  |  | The business key identifier of the operation row's supplier. |
| `WorkCenterId` | `Int64` | no |  |  | The business key identifier of the operation's row work center. |
| `IsSubcontractor` | `Boolean` | no |  |  | Specifies if the operation is subcontracted. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the operation row's comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The comment of the operation row. |
| `Description` | `String` | no |  |  | The translated description of the operation row. |
| `TimeCode` | `Int32` | no |  | enum | The time code specified for the operation row. |
| `TimeUnit` | `Int32` | no |  | enum | The time unit specified for the operation row. |
| `SetupTime` | `TimeSpan` | no |  |  | The setup time of the operation. |
| `UnitTime` | `TimeSpan` | no |  |  | The unit time of the operation. |
| `ExtraQuantityPercent` | `Decimal` | no |  |  | The extra quantity percentage of the operation row. |
| `NumberOfFlows` | `Decimal?` | yes |  |  | The number of flows specified for the operation row. |
| `OverlapPercent` | `Decimal` | no |  |  | The overlap percentage of the operation row. |
| `UnitStaffingFactor` | `Decimal?` | yes |  |  | The unit staffing factor of the operation row. |
| `SetupStaffingFactor` | `Decimal?` | yes |  |  | The setup staffing factor of the operation row. |
| `SetupQuantity` | `Decimal` | no |  |  | The setup quantity of the operation row. |
| `IsForCalculationOnly` | `Boolean` | no |  |  | Specifies if the operation row is to be used for calculations only. |
| `QueueTime` | `TimeSpan?` | yes |  |  | The queue time of the operation. |
| `UseQueueTimeWholeDayRoundOf` | `Boolean?` | yes |  |  | Specifies if queue time should be rounded to full day. |
| `UnitCostFactorId` | `Int64?` | yes |  |  | The business key identifier of the unit cost factor of the operation row. |
| `SetupCostFactorId` | `Int64?` | yes |  |  | The business key identifier of the setup cost factor of the operation row. |
| `FixedLeadTime` | `TimeSpan?` | yes |  |  | The fixed lead time of the operation row. |
| `SetupCost` | `Decimal?` | yes |  |  | The setup cost of the operation row. This value is only available if the operation is a subcontract. |
| `SetupCostCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the setup cost currency. |
| `UnitCost` | `Decimal?` | yes |  |  | The unit cost of the operation row. This value is only available if the operation is a subcontract. |
| `UnitCostCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the unit cost currency. |
| `TransportCost` | `Decimal?` | yes |  |  | The transport cost of the operation represented in the company currency. This value is only available if the operation is a subcontract. |
| `SupplierPartNumber` | `String` | no |  |  | The supplier part number of the operation subcontractor part. This value is only available if the operation is a subcontract. |
| `DeliverToEndCustomer` | `Boolean` | no |  |  | Whether the subcontractor will deliver straight to the end customer or not. This value is only available if the operation is a subcontract. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](../Common/ExtraField.md) | expandable, collection, since 22.5 | The extra fields of the operation row. |
| `ControlDataRows` | `OperationRowControlDataRows[]` | no | [OperationRowControlDataRows](OperationRowControlDataRow.md) | expandable, collection, since 22.5 | The control data rows. |
| `AlternativeOperationRows` | `AlternativeOperationRows[]` | no | [AlternativeOperationRows](AlternativeOperationRow.md) | expandable, collection, since 26.5 | The alternative operation rows (alternative work centers) of the operation row. |
| `PreparationTermType` | `Int32?` | yes |  | since 24.4 | PreparationTermType of the Operation Row. |
| `PreparationTermFromValue` | `String` | no |  | since 24.4 | PreparationTermFromValue of the Operation Row. |
| `PreparationTermToValue` | `String` | no |  | since 24.4 | PreparationTermToValue of the Operation Row. |

## Enumerations

### TimeCode

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `Calculated` | 1 |
| `Studied` | 2 |

### TimeUnit

| Name | Value |
| --- | ---: |
| `Hours` | 0 |
| `Minutes` | 1 |
| `Seconds` | 2 |
| `QuantityPerHour` | 3 |
| `QuantityPerMinute` | 4 |
| `QuantityPerSecond` | 5 |


## Referenced by

**Manufacturing**

- [AlternativeOperationRows](AlternativeOperationRow.md) — `OperationRowId` (FK)
- [ManufacturingOrderOperations](ManufacturingOrderOperation.md) — `OperationRow` (expand)
- [ManufacturingOrderOperations](ManufacturingOrderOperation.md) — `OperationRowId` (FK)
- [OperationRowControlDataRows](OperationRowControlDataRow.md) — `OperationRowId` (FK)
- [Preparations](Preparation.md) — `Operations` (expand)


## Example

```json
{
  "Id": 0,
  "OperationNumber": 0,
  "SubcontractPartId": null,
  "SupplierId": null,
  "WorkCenterId": 0,
  "IsSubcontractor": false,
  "CommentId": null,
  "Comment": null,
  "Description": null,
  "TimeCode": 0,
  "TimeUnit": 0,
  "SetupTime": "00:00:00",
  "UnitTime": "00:00:00",
  "ExtraQuantityPercent": 0.0,
  "NumberOfFlows": null,
  "OverlapPercent": 0.0,
  "UnitStaffingFactor": null,
  "SetupStaffingFactor": null,
  "SetupQuantity": 0.0,
  "IsForCalculationOnly": false,
  "QueueTime": null,
  "UseQueueTimeWholeDayRoundOf": null,
  "UnitCostFactorId": null,
  "SetupCostFactorId": null,
  "FixedLeadTime": null,
  "SetupCost": null,
  "SetupCostCurrencyId": null,
  "UnitCost": null,
  "UnitCostCurrencyId": null,
  "TransportCost": null,
  "SupplierPartNumber": null,
  "DeliverToEndCustomer": false,
  "ExtraFields": null,
  "ControlDataRows": null,
  "AlternativeOperationRows": null,
  "PreparationTermType": null,
  "PreparationTermFromValue": null,
  "PreparationTermToValue": null
}
```
