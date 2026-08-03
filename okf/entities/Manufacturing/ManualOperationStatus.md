---
type: API Entity
title: ManualOperationStatuses
description: Represents a manual operation status.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManualOperationStatus.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManualOperationStatus.html
  title: Monitor API — ManualOperationStatus
module: Manufacturing
api_class: ManualOperationStatus
doc_name: ManualOperationStatuses
endpoint: GET /api/v1/Manufacturing/ManualOperationStatuses
guid: CF8F5259-5466-4B82-9E1F-99851441468C
permission: Show manufacturing orders
introduced_in: '25.2'
property_count: 3
referenced_by:
- /entities/Manufacturing/ManufacturingOrderOperation.md
---

# ManualOperationStatuses

Represents a manual operation status.

- **Module:** [Manufacturing](../../modules/Manufacturing.md)
- **API class:** `ManualOperationStatus`
- **Endpoint:** `GET /api/v1/Manufacturing/ManualOperationStatuses`
- **Required permission:** Show manufacturing orders
- **GUID:** `CF8F5259-5466-4B82-9E1F-99851441468C`
- **Introduced in:** 25.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the manual operation status. |
| `Code` | `String` | no |  | unique, max length 10 | The human readable identifier of the manual operation status. |
| `Description` | `String` | no |  |  | The translated description of the manual operation status. |

## Referenced by

**Manufacturing**

- [ManufacturingOrderOperations](ManufacturingOrderOperation.md) — `ManualOperationStatus` (expand)
- [ManufacturingOrderOperations](ManufacturingOrderOperation.md) — `ManualOperationStatusId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null
}
```
