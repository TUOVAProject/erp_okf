---
type: API Entity
title: CaseManagementCost
description: Represents a case management cost.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementCost.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementCost.html
  title: Monitor API — CaseManagementCost
module: Inventory
api_class: CaseManagementCost
doc_name: CaseManagementCost
endpoint: GET /api/v1/Inventory/CaseManagementCost
guid: C96229D4-1CC9-49A7-86E8-CA489AFB3D11
permission: Show basic data for case
introduced_in: '2.26'
property_count: 6
references_out:
- /entities/Common/Currency.md
referenced_by:
- /entities/Inventory/CaseEntryAdditionalCost.md
- /entities/Inventory/CaseManagementTemplateCost.md
---

# CaseManagementCost

Represents a case management cost.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `CaseManagementCost`
- **Endpoint:** `GET /api/v1/Inventory/CaseManagementCost`
- **Required permission:** Show basic data for case
- **GUID:** `C96229D4-1CC9-49A7-86E8-CA489AFB3D11`
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case management cost. |
| `Number` | `Int32` | no |  |  | The human readable identifier of the case management cost. |
| `Description` | `String` | no |  |  | The translated description of the case management cost. |
| `Cost` | `Decimal` | no |  |  | The cost of the case management. |
| `CostCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the case management cost currency. |
| `Chargeable` | `Boolean` | no |  |  | Specifies if the case management cost is chargeable. |

## Referenced by

**Inventory**

- [CaseEntryAdditionalCost](/entities/Inventory/CaseEntryAdditionalCost.md) — `CaseManagementCost` (expand)
- [CaseEntryAdditionalCost](/entities/Inventory/CaseEntryAdditionalCost.md) — `CaseManagementCostId` (FK)
- [CaseManagementTemplateCosts](/entities/Inventory/CaseManagementTemplateCost.md) — `CostId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "Cost": 0.0,
  "CostCurrencyId": 0,
  "Chargeable": false
}
```
