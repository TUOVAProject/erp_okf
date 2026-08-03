---
type: API Entity
title: AllocationKeyResultRows
description: Represent an allocation key result row.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AllocationKeyResultRow.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AllocationKeyResultRow.html
  title: Monitor API — AllocationKeyResultRow
module: Accounting
api_class: AllocationKeyResultRow
doc_name: AllocationKeyResultRows
endpoint: GET /api/v1/Accounting/AllocationKeyResultRows
guid: 9d67c2ac-88ab-4032-824f-139326fffb52
permission: Show allocation keys
introduced_in: '24.8'
property_count: 6
references_out:
- /entities/Accounting/AllocationKey.md
- /entities/Accounting/CodingEntry.md
referenced_by:
- /entities/Accounting/AllocationKey.md
---

# AllocationKeyResultRows

Represent an allocation key result row.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `AllocationKeyResultRow`
- **Endpoint:** `GET /api/v1/Accounting/AllocationKeyResultRows`
- **Required permission:** Show allocation keys
- **GUID:** `9d67c2ac-88ab-4032-824f-139326fffb52`
- **Introduced in:** 24.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the allocation key result row. |
| `AllocationKeyId` | `Int64` | no | [AllocationKeys](AllocationKey.md) |  | The business key identifier of the allocation key the result row belongs to. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](CodingEntry.md) | expandable | The business key identifier of the coding entry of the allocation key result row. |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](CodingEntry.md) |  | The coding entry of the allocation key result row. |
| `Percentage` | `Decimal` | no |  |  | The percentage value of the allocation key result row. |
| `RowIndex` | `Int32` | no |  |  | The row index of the allocation key result row. |

## Referenced by

**Accounting**

- [AllocationKeys](AllocationKey.md) — `AllocationKeyResultRow` (expand)


## Example

```json
{
  "Id": 0,
  "AllocationKeyId": 0,
  "CodingEntryId": 0,
  "CodingEntry": null,
  "Percentage": 0.0,
  "RowIndex": 0
}
```
