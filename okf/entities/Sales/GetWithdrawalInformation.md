---
type: API Command
title: GetWithdrawalInformation
description: Calculates and returns the suggested withdrawal information for a picking
  list.
resource: https://api.monitor.se/api/Monitor.API.Sales.GetWithdrawalInformation.html
tags:
- Sales
- command
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.GetWithdrawalInformation.html
  title: Monitor API — GetWithdrawalInformation
module: Sales
api_class: GetWithdrawalInformation
doc_name: GetWithdrawalInformation
endpoint: POST /api/v1/Sales/SalesPickingLists/GetWithdrawalInformation
permission: Show customer orders
introduced_in: '2.53'
property_count: 1
references_out:
- /entities/Sales/SalesPickingList.md
---

# GetWithdrawalInformation

Calculates and returns the suggested withdrawal information for a picking list.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `GetWithdrawalInformation`
- **Endpoint:** `POST /api/v1/Sales/SalesPickingLists/GetWithdrawalInformation`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

## Notes

- Returns an array of WithdrawalInformationRow

## Request body

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `PickingListId` | `Int64` | no | [SalesPickingLists](/entities/Sales/SalesPickingList.md) | mandatory | The business key identifier of the picking list. |

## Example

```json
{
  "PickingListId": 0
}
```
