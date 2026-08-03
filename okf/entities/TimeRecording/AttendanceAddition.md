---
type: API Entity
title: AttendanceAdditions
description: Represents an attendance addition
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AttendanceAddition.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.AttendanceAddition.html
  title: Monitor API — AttendanceAddition
module: TimeRecording
api_class: AttendanceAddition
doc_name: AttendanceAdditions
endpoint: GET /api/v1/TimeRecording/AttendanceAdditions
guid: 4A4998B4-667D-429E-89EF-DA6C07FE77EE
permission: Show basic data for attendance
introduced_in: '22.7'
property_count: 17
references_out:
- /entities/Common/Currency.md
- /entities/Common/ProjectCostType.md
- /entities/TimeRecording/SalaryType.md
- /entities/TimeRecording/TimeBank.md
referenced_by:
- /entities/TimeRecording/AdditionRecording.md
---

# AttendanceAdditions

Represents an attendance addition

- **Module:** [TimeRecording](../../modules/TimeRecording.md)
- **API class:** `AttendanceAddition`
- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceAdditions`
- **Required permission:** Show basic data for attendance
- **GUID:** `4A4998B4-667D-429E-89EF-DA6C07FE77EE`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the attendance addition. |
| `RowNumber` | `Int32` | no |  |  | Row number of the attendance addition. |
| `Description` | `String` | no |  |  | The translated description of the attendance addition. |
| `AdditionType` | `Int32` | no |  | enum | Type of attendance addition. |
| `IsActive` | `Boolean` | no |  |  | Specifies if attendance addition is active. |
| `EnterFromTo` | `Boolean` | no |  |  | Specifies whether Enter from/to is enabled. |
| `MandatoryComment` | `Boolean` | no |  |  | Specifies whether comment is mandatory or not. |
| `LinkToProjectType` | `Int32` | no |  | enum | Type of link to project. |
| `TimeBankId` | `Int64?` | yes | [TimeBanks](TimeBank.md) |  | The business key identifier of time bank. |
| `TimeBank` | `TimeBanks` | no | [TimeBanks](TimeBank.md) | expandable | Time bank. |
| `TimeBankTransaction` | `Int32` | no |  | enum | Type of time bank transaction. |
| `Cost` | `Decimal` | no |  |  | The cost of the attendance addition. |
| `CostCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the attendance addition cost currency. |
| `SalaryTypes` | `SalaryTypes[]` | no | [SalaryTypes](SalaryType.md) | expandable, collection, since 24.9 | The salary types of the attendance addition cost. |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](../Common/ProjectCostType.md) | since 24.9 | The business key identifier of the project cost type of the attendance addition. |
| `CostType` | `ProjectCostTypes` | no | [ProjectCostTypes](../Common/ProjectCostType.md) | expandable, since 24.9 | The project cost type of the attendance addition. |
| `CostVisibility` | `Int32` | no |  | enum, since 24.9 | The visibility or editability of the cost of the attendance addition. |

## Enumerations

### AdditionType

| Name | Value |
| --- | ---: |
| `Standard` | 0 |
| `SystemTimebankAdjustment` | 1 |

### LinkToProjectType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Optional` | 1 |
| `Mandatory` | 2 |

### TimeBankTransaction

| Name | Value |
| --- | ---: |
| `Increase` | 0 |
| `Decrease` | 1 |

### CostVisibility

| Name | Value |
| --- | ---: |
| `No` | 0 |
| `Yes` | 1 |
| `Editable` | 2 |


## Referenced by

**TimeRecording**

- [AdditionRecordings](AdditionRecording.md) — `AttendanceAddition` (expand)
- [AdditionRecordings](AdditionRecording.md) — `AttendanceAdditionId` (FK)


## Example

```json
{
  "Id": 0,
  "RowNumber": 0,
  "Description": null,
  "AdditionType": 0,
  "IsActive": false,
  "EnterFromTo": false,
  "MandatoryComment": false,
  "LinkToProjectType": 0,
  "TimeBankId": null,
  "TimeBank": null,
  "TimeBankTransaction": 0,
  "Cost": 0.0,
  "CostCurrencyId": null,
  "SalaryTypes": null,
  "CostTypeId": null,
  "CostType": null,
  "CostVisibility": 0
}
```
