---
type: API Command
title: CreateSalesPickingList
description: Creates picking lists.
resource: https://api.monitor.se/api/Monitor.API.Sales.CreateSalesPickingList.html
tags:
- Sales
- command
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CreateSalesPickingList.html
  title: Monitor API — CreateSalesPickingList
module: Sales
api_class: CreateSalesPickingList
doc_name: Create
endpoint: POST /api/v1/Sales/SalesPickingLists/Create
permission: Show customer orders
introduced_in: '2.53'
property_count: 3
references_out:
- /entities/Common/Person.md
---

# CreateSalesPickingList

Operation `Create` on the Monitor API.

Creates picking lists.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `CreateSalesPickingList`
- **Endpoint:** `POST /api/v1/Sales/SalesPickingLists/Create`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

## Notes

- Returns Int64 [] (the collection of picking list ids created).

## Request body

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `DeliveryRows` | `DeliveryRow[]` | no |  | collection | Collection of the customer order rows that should be added to the picking list. |
| `CreatedByPersonId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the person that created the picking list. |
| `OutgoingDeliveryLocationName` | `String` | no |  | max length 35 | The name of the outgoing delivery location for the picking list. |

## Example

```json
{
  "DeliveryRows": null,
  "CreatedByPersonId": null,
  "OutgoingDeliveryLocationName": null
}
```
