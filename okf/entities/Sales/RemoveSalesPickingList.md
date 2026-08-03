---
type: API Command
title: RemoveSalesPickingList
description: Deletes a picking list.
resource: https://api.monitor.se/api/Monitor.API.Sales.RemoveSalesPickingList.html
tags:
- Sales
- command
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.RemoveSalesPickingList.html
  title: Monitor API — RemoveSalesPickingList
module: Sales
api_class: RemoveSalesPickingList
doc_name: Remove
endpoint: POST /api/v1/Sales/SalesPickingLists/Remove
permission: Show customer orders
introduced_in: '2.53'
property_count: 1
references_out:
- /entities/Sales/SalesPickingList.md
---

# RemoveSalesPickingList

Operation `Remove` on the Monitor API.

Deletes a picking list.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `RemoveSalesPickingList`
- **Endpoint:** `POST /api/v1/Sales/SalesPickingLists/Remove`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

## Notes

- Returns EntityCommandResponse
- The root entity id and the entity id of the response is zero.

## Request body

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `PickingListId` | `Int64` | no | [SalesPickingLists](SalesPickingList.md) | mandatory | The business key identifier of the picking list that will get removed. |

## Example

```json
{
  "PickingListId": 0
}
```
