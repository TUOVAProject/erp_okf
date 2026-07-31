---
type: API Entity
title: CaseManagementTemplateCosts
description: Represents a case management template cost.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementTemplateCost.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementTemplateCost.html
  title: Monitor API — CaseManagementTemplateCost
module: Inventory
api_class: CaseManagementTemplateCost
doc_name: CaseManagementTemplateCosts
endpoint: GET /api/v1/Inventory/CaseManagementTemplateCosts
guid: ce2f5ffc-9d17-4c67-8cff-a256100dd6ec
permission: Show basic data for case
introduced_in: '23.9'
property_count: 8
references_out:
- /entities/Common/Currency.md
- /entities/Inventory/CaseManagementCost.md
- /entities/Inventory/CaseManagementTemplate.md
referenced_by:
- /entities/Inventory/CaseManagementTemplate.md
---

# CaseManagementTemplateCosts

Represents a case management template cost.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `CaseManagementTemplateCost`
- **Endpoint:** `GET /api/v1/Inventory/CaseManagementTemplateCosts`
- **Required permission:** Show basic data for case
- **GUID:** `ce2f5ffc-9d17-4c67-8cff-a256100dd6ec`
- **Introduced in:** 23.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case management template cost. |
| `Description` | `String` | no |  |  | The description of the case management template cost. |
| `Cost` | `Decimal` | no |  |  | The cost of the case management template cost. |
| `CostCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the case management template cost currency. |
| `CostId` | `Int64?` | yes | [CaseManagementCost](/entities/Inventory/CaseManagementCost.md) |  | The business key identifier of the case management cost. |
| `ParentId` | `Int64?` | yes | [CaseManagementTemplates](/entities/Inventory/CaseManagementTemplate.md) |  | The business key identifier of the case management template. |
| `IsChargeable` | `Boolean` | no |  |  | Specifies if the case management template cost is chargeable. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the case management template cost. |

## Referenced by

**Inventory**

- [CaseManagementTemplates](/entities/Inventory/CaseManagementTemplate.md) — `CaseManagementTemplateCost` (expand)


## Example

```json
{
  "Id": 0,
  "Description": null,
  "Cost": 0.0,
  "CostCurrencyId": null,
  "CostId": null,
  "ParentId": null,
  "IsChargeable": false,
  "RowIndex": null
}
```
