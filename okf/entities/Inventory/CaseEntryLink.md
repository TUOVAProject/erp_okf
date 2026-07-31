---
type: API Entity
title: CaseEntryLinks
description: Represents a case link.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseEntryLink.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseEntryLink.html
  title: Monitor API — CaseEntryLink
module: Inventory
api_class: CaseEntryLink
doc_name: CaseEntryLinks
endpoint: GET /api/v1/Inventory/CaseEntryLinks
guid: 9203faf3-6e53-476f-91ff-1414b13201ca
permission: Show case
introduced_in: '25.1'
property_count: 3
references_out:
- /entities/Inventory/CaseEntry.md
---

# CaseEntryLinks

Represents a case link.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `CaseEntryLink`
- **Endpoint:** `GET /api/v1/Inventory/CaseEntryLinks`
- **Required permission:** Show case
- **GUID:** `9203faf3-6e53-476f-91ff-1414b13201ca`
- **Introduced in:** 25.1

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case link. |
| `ParentId` | `Int64` | no | [CaseEntry](/entities/Inventory/CaseEntry.md) |  | The business key identifier of the parent case entry of this case link. |
| `ChildId` | `Int64` | no | [CaseEntry](/entities/Inventory/CaseEntry.md) |  | The business key identifier of the child case entry of this case link. |

## Example

```json
{
  "Id": 0,
  "ParentId": 0,
  "ChildId": 0
}
```
