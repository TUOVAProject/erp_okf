---
type: API Entity
title: PhysicalInventoryRows
description: Represents a physical inventory row.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PhysicalInventoryRow.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PhysicalInventoryRow.html
  title: Monitor API — PhysicalInventoryRow
module: Inventory
api_class: PhysicalInventoryRow
doc_name: PhysicalInventoryRows
endpoint: GET /api/v1/Inventory/PhysicalInventoryRows
guid: D0E8D320-A7C2-4E27-9E26-1154F1F09261
permission: Report stock count
introduced_in: '22.8'
property_count: 9
references_out:
- /entities/Inventory/Part.md
- /entities/Inventory/PartLocation.md
- /entities/Inventory/PhysicalInventoryList.md
- /entities/Inventory/ProductRecord.md
---

# PhysicalInventoryRows

Represents a physical inventory row.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `PhysicalInventoryRow`
- **Endpoint:** `GET /api/v1/Inventory/PhysicalInventoryRows`
- **Required permission:** Report stock count
- **GUID:** `D0E8D320-A7C2-4E27-9E26-1154F1F09261`
- **Introduced in:** 22.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the physical inventory row. |
| `PhysicalInventoryListId` | `Int64` | no | [PhysicalInventoryLists](/entities/Inventory/PhysicalInventoryList.md) |  | The business key identifier of the physical inventory list that the row belongs to. |
| `PartId` | `Int64` | no | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the part of the physical inventory row. |
| `LocationId` | `Int64` | no | [PartLocations](/entities/Inventory/PartLocation.md) |  | The business key identifier of the part location of the physical inventory row. |
| `ProductRecordId` | `Int64` | no | [ProductRecords](/entities/Inventory/ProductRecord.md) |  | The business key identifier of the product record of the physical inventory row. |
| `Reported` | `Boolean` | no |  | **deprecated since 23.3** | Indicates if the physical inventory row is reported. _(Use ReportingState to get current state and see if row is reported, pending approval or rejected)_ |
| `ReportingState` | `Int32` | no |  | enum, since 23.3 | Reporting state of the physical inventory row. |
| `Version` | `Int32` | no |  |  | The version of the physical inventory row. |
| `ReportedQuantity` | `Decimal?` | yes |  |  | The reported quantity for the physical inventory row. |

## Enumerations

### ReportingState

| Name | Value |
| --- | ---: |
| `NotReported` | 0 |
| `Reported` | 1 |
| `PendingApproval` | 2 |
| `ApprovalRejected` | 3 |
| `Discarded` | 4 |


## Example

```json
{
  "Id": 0,
  "PhysicalInventoryListId": 0,
  "PartId": 0,
  "LocationId": 0,
  "ProductRecordId": 0,
  "Reported": false,
  "ReportingState": 0,
  "Version": 0,
  "ReportedQuantity": null
}
```
