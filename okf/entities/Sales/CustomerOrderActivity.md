---
type: API Entity
title: CustomerOrderActivities
description: Represents a customer order activity.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderActivity.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderActivity.html
  title: Monitor API — CustomerOrderActivity
module: Sales
api_class: CustomerOrderActivity
doc_name: CustomerOrderActivities
endpoint: GET /api/v1/Sales/CustomerOrderActivities
guid: CEE60004-79DD-4809-A096-CFF58DAF2119
permission: Show customer orders
introduced_in: '24.3'
property_count: 7
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerRelationshipActivityType.md
---

# CustomerOrderActivities

Represents a customer order activity.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerOrderActivity`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderActivities`
- **Required permission:** Show customer orders
- **GUID:** `CEE60004-79DD-4809-A096-CFF58DAF2119`
- **Introduced in:** 24.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer order activity. |
| `OrderId` | `Int64` | no | [CustomerOrders](CustomerOrder.md) |  | The business key identifier of the customer order to add the activity to. |
| `ActivityTypeId` | `Int64` | no | [CustomerRelationshipActivityTypes](CustomerRelationshipActivityType.md) |  | The business key identifier of the customer order activity type that the activity is based on. |
| `Description` | `String` | no |  | default: From the activity type | The description of the activity. |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier of the application user that is responsible for the activity. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |  | The planned completion date of the activity. |
| `Reminder` | `Boolean?` | yes |  |  | Sets whether or not a reminder should be created for the activity. |

## Example

```json
{
  "Id": 0,
  "OrderId": 0,
  "ActivityTypeId": 0,
  "Description": null,
  "ResponsibleUserId": 0,
  "PlannedCompletionDate": "0001-01-01T00:00:00+00:00",
  "Reminder": null
}
```
