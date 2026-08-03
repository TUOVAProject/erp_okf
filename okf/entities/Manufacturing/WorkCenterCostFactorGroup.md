---
type: API Entity
title: WorkCenterCostFactorGroups
description: Represents a cost factor group belonging to a work center. Note that
  all cost factors are represented in company currency per hour.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.WorkCenterCostFactorGroup.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.WorkCenterCostFactorGroup.html
  title: Monitor API — WorkCenterCostFactorGroup
module: Manufacturing
api_class: WorkCenterCostFactorGroup
doc_name: WorkCenterCostFactorGroups
endpoint: GET /api/v1/Manufacturing/WorkCenterCostFactorGroups
guid: 67938EE9-FED8-4983-A348-9129CC80AA1A
permission: Show work center
introduced_in: '2.46'
property_count: 13
references_out:
- /entities/Manufacturing/WorkCenter.md
referenced_by:
- /entities/Manufacturing/WorkCenter.md
---

# WorkCenterCostFactorGroups

Represents a cost factor group belonging to a work center. Note that all cost factors are represented in company currency per hour.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `WorkCenterCostFactorGroup`
- **Endpoint:** `GET /api/v1/Manufacturing/WorkCenterCostFactorGroups`
- **Required permission:** Show work center
- **GUID:** `67938EE9-FED8-4983-A348-9129CC80AA1A`
- **Introduced in:** 2.46

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the work center cost factor group. |
| `Description` | `String` | no |  |  | The translated description of the work center cost factor group. |
| `Type` | `Int32` | no |  | bitmask, enum | The types that apply to the work center cost factor group. |
| `CostFactor1` | `Decimal?` | yes |  |  | The first cost factor of the group. |
| `CostFactor2` | `Decimal?` | yes |  |  | The second cost factor of the group. |
| `CostFactor3` | `Decimal?` | yes |  |  | The third cost factor of the group. |
| `FutureCostFactor1` | `Decimal?` | yes |  |  | The future first cost factor of the group. |
| `FutureCostFactor2` | `Decimal?` | yes |  |  | The future second cost factor of the group. |
| `FutureCostFactor3` | `Decimal?` | yes |  |  | The future third cost factor of the group. |
| `IsDefaultSetupCost` | `Boolean` | no |  |  | Specifies if the cost factor group is used as the default group for setup costs for its parent work center. |
| `IsDefaultUnitCost` | `Boolean` | no |  |  | Specifies if the cost factor group is used as the default group for unit costs for its parent work center. |
| `ParentId` | `Int64` | no | [WorkCenters](WorkCenter.md) |  | The business key identifier of the work center that the cost factor group belongs to. |
| `RowIndex` | `Int32` | no |  |  | The row index of the work center cost factor group in relation to the other groups that belong to the parent work center. |

## Enumerations

### Type (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `SetupCost` | 1 |
| `UnitCost` | 2 |


## Referenced by

**Manufacturing**

- [WorkCenters](WorkCenter.md) — `CostFactorGroups` (expand)


## Example

```json
{
  "Id": 0,
  "Description": null,
  "Type": 0,
  "CostFactor1": null,
  "CostFactor2": null,
  "CostFactor3": null,
  "FutureCostFactor1": null,
  "FutureCostFactor2": null,
  "FutureCostFactor3": null,
  "IsDefaultSetupCost": false,
  "IsDefaultUnitCost": false,
  "ParentId": 0,
  "RowIndex": 0
}
```
