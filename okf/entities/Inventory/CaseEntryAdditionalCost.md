---
type: API Entity
title: CaseEntryAdditionalCost
description: Represents a case entry additional cost.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseEntryAdditionalCost.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseEntryAdditionalCost.html
  title: Monitor API — CaseEntryAdditionalCost
module: Inventory
api_class: CaseEntryAdditionalCost
doc_name: CaseEntryAdditionalCost
endpoint: GET /api/v1/Inventory/CaseEntryAdditionalCost
guid: 758AA611-F39D-4DCA-9F9A-412E97414D69
permission: Show basic data for case
introduced_in: '2.26'
property_count: 12
references_out:
- /entities/Common/Currency.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CaseManagementCost.md
- /entities/Inventory/Part.md
referenced_by:
- /entities/Inventory/CaseEntry.md
---

# CaseEntryAdditionalCost

Represents a case entry additional cost.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `CaseEntryAdditionalCost`
- **Endpoint:** `GET /api/v1/Inventory/CaseEntryAdditionalCost`
- **Required permission:** Show basic data for case
- **GUID:** `758AA611-F39D-4DCA-9F9A-412E97414D69`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case entry additional cost. |
| `CaseEntryId` | `Int64` | no | [CaseEntry](/entities/Inventory/CaseEntry.md) | since 22.8 | The business key identifier of the case entry. |
| `CaseManagementCostId` | `Int64` | no | [CaseManagementCost](/entities/Inventory/CaseManagementCost.md) |  | The business key identifier of the case management cost for the case entry additional cost. |
| `CaseManagementCost` | `CaseManagementCost` | no | [CaseManagementCost](/entities/Inventory/CaseManagementCost.md) | expandable | The case management cost of the case entry additional cost. |
| `Cost` | `Decimal` | no |  |  | The cost of the case entry additional cost. |
| `CostCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the case entry additional cost currency. |
| `CostType` | `Int32` | no |  | enum | The cost type of the case additional cost. |
| `Chargeable` | `Boolean` | no |  |  | Specifies if the case additional cost is chargeable. |
| `CostPerEach` | `Decimal?` | yes |  | since 24.7 | The cost per unit of the case entry additional. |
| `Quantity` | `Decimal?` | yes |  | since 24.7 | The quantity of the case entry additional cost. |
| `PartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) | since 25.1 | The business key identifier of the part for the case entry additional cost. |
| `Part` | `Parts` | no | [Parts](/entities/Inventory/Part.md) | expandable, since 25.1 | The part of the case entry additional cost. |

## Enumerations

### CostType

| Name | Value |
| --- | ---: |
| `Planned` | 0 |
| `Actual` | 1 |


## Referenced by

**Inventory**

- [CaseEntry](/entities/Inventory/CaseEntry.md) — `Costs` (expand)


## Example

```json
{
  "Id": 0,
  "CaseEntryId": 0,
  "CaseManagementCostId": 0,
  "CaseManagementCost": null,
  "Cost": 0.0,
  "CostCurrencyId": 0,
  "CostType": 0,
  "Chargeable": false,
  "CostPerEach": null,
  "Quantity": null,
  "PartId": null,
  "Part": null
}
```
