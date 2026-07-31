---
type: API Entity
title: CustomerRelationshipActivityTypes
description: Represents a customer relationship activity type.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerRelationshipActivityType.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerRelationshipActivityType.html
  title: Monitor API — CustomerRelationshipActivityType
module: Sales
api_class: CustomerRelationshipActivityType
doc_name: CustomerRelationshipActivityTypes
endpoint: GET /api/v1/Sales/CustomerRelationshipActivityTypes
guid: 11710A5B-5D7F-4576-A5DD-1E6DAF679404
permission: Show customer
introduced_in: '2.55'
property_count: 4
referenced_by:
- /entities/Sales/BusinessOpportunityActivityTemplateRow.md
- /entities/Sales/CustomerOrderActivity.md
- /entities/Sales/CustomerRelationshipManagementActivity.md
- /entities/Sales/QuoteActivity.md
---

# CustomerRelationshipActivityTypes

Represents a customer relationship activity type.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `CustomerRelationshipActivityType`
- **Endpoint:** `GET /api/v1/Sales/CustomerRelationshipActivityTypes`
- **Required permission:** Show customer
- **GUID:** `11710A5B-5D7F-4576-A5DD-1E6DAF679404`
- **Introduced in:** 2.55

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer relationship activity type. |
| `Code` | `Int64` | no |  | unique | The human readable identifier of the activity type. |
| `Description` | `String` | no |  |  | The description of the activity type. |
| `Sources` | `Int32` | no |  | bitmask, enum, since 24.2 | Specifies where this activity type can be used. |

## Enumerations

### Sources (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `Part` | 1 |
| `Quote` | 2 |
| `CustomerOrder` | 4 |
| `Customer` | 8 |
| `PurchaseOrder` | 16 |
| `Inquiry` | 32 |
| `BlanketOrderPurchase` | 64 |
| `Supplier` | 128 |
| `BlanketOrderSales` | 256 |
| `SalesAgreement` | 512 |
| `PurchaseAgreement` | 1024 |
| `BusinessOpportunity` | 2048 |


## Referenced by

**Sales**

- [BusinessOpportunityActivityTemplateRows](/entities/Sales/BusinessOpportunityActivityTemplateRow.md) — `ActivityTypeId` (FK)
- [CustomerOrderActivities](/entities/Sales/CustomerOrderActivity.md) — `ActivityTypeId` (FK)
- [CustomerRelationshipManagementActivities](/entities/Sales/CustomerRelationshipManagementActivity.md) — `ActivityType` (expand)
- [CustomerRelationshipManagementActivities](/entities/Sales/CustomerRelationshipManagementActivity.md) — `ActivityTypeId` (FK)
- [QuoteActivities](/entities/Sales/QuoteActivity.md) — `ActivityTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null,
  "Sources": 0
}
```
