---
type: API Type
title: WithdrawalInformationRow
description: Used to provide the suggested withdrawal information of a customer order
  row.
resource: https://api.monitor.se/api/Monitor.API.Sales.WithdrawalInformationRow.html
tags:
- Sales
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.WithdrawalInformationRow.html
  title: Monitor API — WithdrawalInformationRow
module: Sales
api_class: WithdrawalInformationRow
doc_name: WithdrawalInformationRow
introduced_in: '2.53'
property_count: 5
references_out:
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/SalesPickingList.md
- /entities/Sales/WithdrawalInformationLocation.md
---

# WithdrawalInformationRow

Used to provide the suggested withdrawal information of a customer order row.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `WithdrawalInformationRow`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.53

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `CustomerOrderRowId` | `Int64` | no | [CustomerOrderRows](CustomerOrderRow.md) |  | The business key identifier of the customer order row that the withdrawal information is for. |
| `PickingListId` | `Int64` | no | [SalesPickingLists](SalesPickingList.md) |  | The business key identifier of the picking list that the withdrawal information is for. |
| `Locations` | `WithdrawalInformationLocation[]` | no | [WithdrawalInformationLocation](WithdrawalInformationLocation.md) | collection | The location withdrawal information. |
| `SuggestedQuantity` | `Decimal` | no |  | since 22.2 | The suggested quantity to withdraw. |
| `ParentCustomerOrderRowId` | `Int64?` | yes | [CustomerOrderRows](CustomerOrderRow.md) | since 22.2 | The business key identifier of the customer order row's parent row that the withdrawal information is for. |

## Example

```json
{
  "CustomerOrderRowId": 0,
  "PickingListId": 0,
  "Locations": null,
  "SuggestedQuantity": 0.0,
  "ParentCustomerOrderRowId": null
}
```
