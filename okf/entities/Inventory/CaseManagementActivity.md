---
type: API Entity
title: CaseManagementActivities
description: Represents a case management activity.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementActivity.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementActivity.html
  title: Monitor API — CaseManagementActivity
module: Inventory
api_class: CaseManagementActivity
doc_name: CaseManagementActivities
endpoint: GET /api/v1/Inventory/CaseManagementActivities
guid: AE8AEF0A-A3BB-40D7-BC67-9DCE39F11A7B
permission: Show case
introduced_in: '2.45'
property_count: 7
references_out:
- /entities/Common/Currency.md
referenced_by:
- /entities/Inventory/CaseEntryActivity.md
- /entities/Inventory/CaseManagementTemplateNode.md
---

# CaseManagementActivities

Represents a case management activity.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `CaseManagementActivity`
- **Endpoint:** `GET /api/v1/Inventory/CaseManagementActivities`
- **Required permission:** Show case
- **GUID:** `AE8AEF0A-A3BB-40D7-BC67-9DCE39F11A7B`
- **Introduced in:** 2.45

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case management activity. |
| `PlannedTime` | `TimeSpan` | no |  |  | The planned time of the case management activity. |
| `CostPerHour` | `Decimal` | no |  |  | The cost per hour of the case management activity. |
| `CostPerHourCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency that applies to the cost per hour of the case management activity. |
| `Chargeable` | `Boolean` | no |  |  | Specifies if the case management activity is chargeable or not. |
| `Code` | `Int64` | no |  |  | The human readable identifier of the case management activity. |
| `Description` | `String` | no |  |  | The description of the case management activity. |

## Referenced by

**Inventory**

- [CaseEntryActivities](/entities/Inventory/CaseEntryActivity.md) — `ActivityTypeId` (FK)
- [CaseManagementTemplateNodes](/entities/Inventory/CaseManagementTemplateNode.md) — `ActivityId` (FK)


## Example

```json
{
  "Id": 0,
  "PlannedTime": "00:00:00",
  "CostPerHour": 0.0,
  "CostPerHourCurrencyId": null,
  "Chargeable": false,
  "Code": 0,
  "Description": null
}
```
