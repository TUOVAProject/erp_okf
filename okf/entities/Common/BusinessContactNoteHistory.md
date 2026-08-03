---
type: API Entity
title: BusinessContactNoteHistories
description: Represents a business contact note history entry.
resource: https://api.monitor.se/api/Monitor.API.Common.BusinessContactNoteHistory.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.BusinessContactNoteHistory.html
  title: Monitor API — BusinessContactNoteHistory
module: Common
api_class: BusinessContactNoteHistory
doc_name: BusinessContactNoteHistories
endpoint: GET /api/v1/Common/BusinessContactNoteHistories
guid: d3610d12-29bb-44b8-9871-137873f0fb98
introduced_in: '2.55'
property_count: 8
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
referenced_by:
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/Part.md
- /entities/Sales/BusinessOpportunity.md
---

# BusinessContactNoteHistories

Represents a business contact note history entry.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `BusinessContactNoteHistory`
- **Endpoint:** `GET /api/v1/Common/BusinessContactNoteHistories`
- **GUID:** `d3610d12-29bb-44b8-9871-137873f0fb98`
- **Introduced in:** 2.55

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business contact note. |
| `Subject` | `String` | no |  | max length 64 | The subject of the business contact note. |
| `BodyId` | `Int64?` | yes |  |  | The business key identifier for the body of the business contact note. |
| `Body` | `Comments` | no | [Comments](Comment.md) | expandable | The body of the business contact note. |
| `CreatedByUserId` | `Int64` | no | [ApplicationUsers](ApplicationUser.md) |  | The business key identifier of the application user that created the business contact note. |
| `CreatedTimestamp` | `DateTimeOffset` | no |  |  | The date the business contact note was created. |
| `ParentId` | `Int64` | no |  |  | The business key identifier of the parent. |
| `ParentClass` | `Guid` | no |  |  | The GUID of the parent type. |

## Referenced by

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `Notes` (expand)
- [Parts](../Inventory/Part.md) — `Notes` (expand)

**Sales**

- [BusinessOpportunities](../Sales/BusinessOpportunity.md) — `BusinessContactNoteHistories` (expand)


## Example

```json
{
  "Id": 0,
  "Subject": null,
  "BodyId": null,
  "Body": null,
  "CreatedByUserId": 0,
  "CreatedTimestamp": "0001-01-01T00:00:00+00:00",
  "ParentId": 0,
  "ParentClass": "00000000-0000-0000-0000-000000000000"
}
```
