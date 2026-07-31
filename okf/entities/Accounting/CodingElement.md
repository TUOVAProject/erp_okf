---
type: API Entity
title: CodingElements
description: Represents a Coding element.
resource: https://api.monitor.se/api/Monitor.API.Accounting.CodingElement.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.CodingElement.html
  title: Monitor API — CodingElement
module: Accounting
api_class: CodingElement
doc_name: CodingElements
endpoint: GET /api/v1/Accounting/CodingElements
guid: E39E8DCA-FEF4-433F-9F8F-B5B9D21AA883
permission: Show dimensions/dimension codes
introduced_in: '2.27'
property_count: 5
references_out:
- /entities/Accounting/CodingDimension.md
referenced_by:
- /entities/Accounting/CodingDimension.md
- /entities/Accounting/CodingEntryElement.md
---

# CodingElements

Represents a Coding element.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `CodingElement`
- **Endpoint:** `GET /api/v1/Accounting/CodingElements`
- **Required permission:** Show dimensions/dimension codes
- **GUID:** `E39E8DCA-FEF4-433F-9F8F-B5B9D21AA883`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the coding element. |
| `Code` | `String` | no |  | max length 12 | The human readable coding element code. |
| `Description` | `String` | no |  |  | The description of the coding element. |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](/entities/Accounting/CodingDimension.md) |  | The business key identifier of the coding element. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the coding element is active. |

## Referenced by

**Accounting**

- [CodingDimensions](/entities/Accounting/CodingDimension.md) — `CodingElements` (expand)
- [CodingEntryElements](/entities/Accounting/CodingEntryElement.md) — `ReferencingEntityId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "CodingDimensionId": 0,
  "IsActive": false
}
```
