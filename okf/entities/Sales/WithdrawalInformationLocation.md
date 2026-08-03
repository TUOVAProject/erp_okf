---
type: API Type
title: WithdrawalInformationLocation
description: Used to provide the suggested withdrawal information of a location.
resource: https://api.monitor.se/api/Monitor.API.Sales.WithdrawalInformationLocation.html
tags:
- Sales
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.WithdrawalInformationLocation.html
  title: Monitor API — WithdrawalInformationLocation
module: Sales
api_class: WithdrawalInformationLocation
doc_name: WithdrawalInformationLocation
introduced_in: '2.53'
property_count: 5
references_out:
- /entities/Inventory/PartLocation.md
referenced_by:
- /entities/Sales/WithdrawalInformationRow.md
---

# WithdrawalInformationLocation

Used to provide the suggested withdrawal information of a location.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `WithdrawalInformationLocation`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.53

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `PartLocationId` | `Int64` | no | [PartLocations](../Inventory/PartLocation.md) |  | The business key identifier of the part location. |
| `ProductRecordId` | `Int64?` | yes | [PartLocations](../Inventory/PartLocation.md) |  | The business key identifier of the product record. |
| `ReservedQuantity` | `Decimal` | no |  |  | The reserved quantity for the location. |
| `AvailableQuantity` | `Decimal` | no |  |  | The available quantity for the location. |
| `SuggestedQuantity` | `Decimal` | no |  |  | The suggested quantity to withdraw from the location. |

## Referenced by

**Sales**

- [WithdrawalInformationRow](WithdrawalInformationRow.md) — `Locations` (expand)


## Example

```json
{
  "PartLocationId": 0,
  "ProductRecordId": null,
  "ReservedQuantity": 0.0,
  "AvailableQuantity": 0.0,
  "SuggestedQuantity": 0.0
}
```
