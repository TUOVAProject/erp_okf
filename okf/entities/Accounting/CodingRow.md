---
type: API Entity
title: CodingRows
description: Represents a coding row.
resource: https://api.monitor.se/api/Monitor.API.Accounting.CodingRow.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.CodingRow.html
  title: Monitor API — CodingRow
module: Accounting
api_class: CodingRow
doc_name: CodingRows
endpoint: GET /api/v1/Accounting/CodingRows
guid: 31C893BD-61C5-42E4-AD40-9D9FF51362CE
introduced_in: '2.30'
property_count: 4
references_out:
- /entities/Accounting/CodingEntry.md
referenced_by:
- /entities/Accounting/Coding.md
---

# CodingRows

Represents a coding row.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `CodingRow`
- **Endpoint:** `GET /api/v1/Accounting/CodingRows`
- **GUID:** `31C893BD-61C5-42E4-AD40-9D9FF51362CE`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the coding row. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) |  | The business key identifier of the coding row's coding entry. |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) |  | The coding entry of the coding row. |
| `Type` | `Int32` | no |  | enum | The type of the coding row. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Standard` | 1 |
| `Setup` | 2 |
| `Material` | 3 |
| `Inventory` | 4 |
| `PriceDifference` | 5 |
| `Cost` | 6 |


## Referenced by

**Accounting**

- [Codings](/entities/Accounting/Coding.md) — `CodingRows` (expand)


## Example

```json
{
  "Id": 0,
  "CodingEntryId": 0,
  "CodingEntry": null,
  "Type": 0
}
```
