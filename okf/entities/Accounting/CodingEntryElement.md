---
type: API Entity
title: CodingEntryElements
description: Represents a coding entry element.
resource: https://api.monitor.se/api/Monitor.API.Accounting.CodingEntryElement.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.CodingEntryElement.html
  title: Monitor API — CodingEntryElement
module: Accounting
api_class: CodingEntryElement
doc_name: CodingEntryElements
endpoint: GET /api/v1/Accounting/CodingEntryElements
guid: 98B48443-2BCD-41A7-A3F0-522F7CF830FB
permission: Show dimensions/dimension codes
introduced_in: '2.30'
property_count: 5
references_out:
- /entities/Accounting/CodingDimension.md
- /entities/Accounting/CodingElement.md
- /entities/Accounting/CodingEntry.md
referenced_by:
- /entities/Accounting/CodingEntry.md
---

# CodingEntryElements

Represents a coding entry element.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `CodingEntryElement`
- **Endpoint:** `GET /api/v1/Accounting/CodingEntryElements`
- **Required permission:** Show dimensions/dimension codes
- **GUID:** `98B48443-2BCD-41A7-A3F0-522F7CF830FB`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the coding entry element. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](CodingEntry.md) |  | The business key identifier of the coding entry that the element belongs to. |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](CodingDimension.md) |  | The business key identifier of the element's coding dimension. |
| `CodingDimension` | `CodingDimensions` | no | [CodingDimensions](CodingDimension.md) | expandable | The coding dimension of the coding entry element. |
| `ReferencingEntityId` | `Int64?` | yes | [CodingElements](CodingElement.md) |  | The business key identifier of the referencing entity. References an entity of type according to the coding dimension's ReferenceEntityType, or CodingElements if None. |

## Referenced by

**Accounting**

- [CodingEntries](CodingEntry.md) — `CodingEntryElements` (expand)


## Example

```json
{
  "Id": 0,
  "CodingEntryId": 0,
  "CodingDimensionId": 0,
  "CodingDimension": null,
  "ReferencingEntityId": null
}
```
