---
type: API Entity
title: ReasonCodeDebitNotes
description: Represents a reason code for debit note.
resource: https://api.monitor.se/api/Monitor.API.Common.ReasonCodeDebitNote.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ReasonCodeDebitNote.html
  title: Monitor API — ReasonCodeDebitNote
module: Common
api_class: ReasonCodeDebitNote
doc_name: ReasonCodeDebitNotes
endpoint: GET /api/v1/Common/ReasonCodeDebitNotes
guid: 21d6aac7-e23a-4b78-9dc2-aacf8dd0c41c
permission: Show cause codes
introduced_in: '25.6'
property_count: 4
referenced_by:
- /entities/Sales/CustomerOrder.md
---

# ReasonCodeDebitNotes

Represents a reason code for debit note.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ReasonCodeDebitNote`
- **Endpoint:** `GET /api/v1/Common/ReasonCodeDebitNotes`
- **Required permission:** Show cause codes
- **GUID:** `21d6aac7-e23a-4b78-9dc2-aacf8dd0c41c`
- **Introduced in:** 25.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the reason code debit note. |
| `Code` | `String` | no |  | unique, max length 6 | The human readable identifier of the reason code debit note. |
| `Description` | `String` | no |  | max length 35 | The translated description of the reason code debit note. |
| `Active` | `Boolean` | no |  |  | Specifies if the reason code debit note is active. |

## Referenced by

**Sales**

- [CustomerOrders](../Sales/CustomerOrder.md) — `ReasonCodeDebitNote` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `ReasonCodeDebitNoteId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "Active": false
}
```
