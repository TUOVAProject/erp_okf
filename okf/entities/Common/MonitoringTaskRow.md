---
type: API Entity
title: MonitoringTaskRows
description: Represents a monitoring task row.
resource: https://api.monitor.se/api/Monitor.API.Common.MonitoringTaskRow.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.MonitoringTaskRow.html
  title: Monitor API — MonitoringTaskRow
module: Common
api_class: MonitoringTaskRow
doc_name: MonitoringTaskRows
endpoint: GET /api/v1/Common/MonitoringTaskRows
guid: f829ad58-6069-4811-8938-cf767f743317
permission: Create and handle all monitoring tasks
introduced_in: '24.7'
property_count: 8
references_out:
- /entities/Common/MonitoringTask.md
- /entities/Common/Warehouse.md
---

# MonitoringTaskRows

Represents a monitoring task row.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `MonitoringTaskRow`
- **Endpoint:** `GET /api/v1/Common/MonitoringTaskRows`
- **Required permission:** Create and handle all monitoring tasks
- **GUID:** `f829ad58-6069-4811-8938-cf767f743317`
- **Introduced in:** 24.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the monitoring task row. |
| `TaskId` | `Int64` | no | [MonitoringTasks](MonitoringTask.md) |  | The business key identifier of the monitoring task that the row belongs to. |
| `EntityId` | `Int64` | no |  |  | The business key identifier of the entity type that the row belongs to. |
| `EntityType` | `Guid` | no |  |  | The type of entity that the row belongs to. |
| `ConditionType` | `Int32` | no |  |  | The condition type of the monitoring task row. |
| `Value` | `String` | no |  | max length 2500 | The threshold balance of stock. Applicable to monitoring task type of StockBalance |
| `Message` | `String` | no |  |  | The message of row to be sent to recipient. |
| `Warehouses` | `Warehouses[]` | no | [Warehouses](Warehouse.md) | expandable, collection | Specifies the warehouse of the monitoring task row. |

## Example

```json
{
  "Id": 0,
  "TaskId": 0,
  "EntityId": 0,
  "EntityType": "00000000-0000-0000-0000-000000000000",
  "ConditionType": 0,
  "Value": null,
  "Message": null,
  "Warehouses": null
}
```
