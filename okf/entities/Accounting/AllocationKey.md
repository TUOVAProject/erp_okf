---
type: API Entity
title: AllocationKeys
description: Represent an allocation key.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AllocationKey.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AllocationKey.html
  title: Monitor API — AllocationKey
module: Accounting
api_class: AllocationKey
doc_name: AllocationKeys
endpoint: GET /api/v1/Accounting/AllocationKeys
guid: a576c8b3-cdc5-404a-b14f-3fd68b85ba9d
permission: Show allocation keys
introduced_in: '24.8'
property_count: 4
references_out:
- /entities/Accounting/AllocationKeyResultRow.md
referenced_by:
- /entities/Accounting/AllocationKeyResultRow.md
- /entities/Accounting/AutoAllocation.md
---

# AllocationKeys

Represent an allocation key.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `AllocationKey`
- **Endpoint:** `GET /api/v1/Accounting/AllocationKeys`
- **Required permission:** Show allocation keys
- **GUID:** `a576c8b3-cdc5-404a-b14f-3fd68b85ba9d`
- **Introduced in:** 24.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the allocation key. |
| `Number` | `Int64` | no |  | unique | The human readable identifier of the allocation key. |
| `Name` | `String` | no |  | max length 64 | The name of the allocation key. |
| `AllocationKeyResultRow` | `AllocationKeyResultRows[]` | no | [AllocationKeyResultRows](/entities/Accounting/AllocationKeyResultRow.md) | expandable, collection | The result rows of the allocation key. |

## Referenced by

**Accounting**

- [AllocationKeyResultRows](/entities/Accounting/AllocationKeyResultRow.md) — `AllocationKeyId` (FK)
- [AutoAllocations](/entities/Accounting/AutoAllocation.md) — `AllocationKey` (expand)
- [AutoAllocations](/entities/Accounting/AutoAllocation.md) — `AllocationKeyId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Name": null,
  "AllocationKeyResultRow": null
}
```
