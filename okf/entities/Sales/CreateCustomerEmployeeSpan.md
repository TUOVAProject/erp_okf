---
type: API Command
title: CreateCustomerEmployeeSpan
description: Creates a new customer employee span object.
resource: https://api.monitor.se/api/Monitor.API.Sales.CreateCustomerEmployeeSpan.html
tags:
- Sales
- command
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CreateCustomerEmployeeSpan.html
  title: Monitor API — CreateCustomerEmployeeSpan
module: Sales
api_class: CreateCustomerEmployeeSpan
doc_name: Create
endpoint: POST /api/v1/Sales/CustomerEmployeeSpans/Create
permission: Create new customer
introduced_in: '24.3'
property_count: 2
---

# CreateCustomerEmployeeSpan

Operation `Create` on the Monitor API.

Creates a new customer employee span object.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CreateCustomerEmployeeSpan`
- **Endpoint:** `POST /api/v1/Sales/CustomerEmployeeSpans/Create`
- **Required permission:** Create new customer
- **Introduced in:** 24.3

## Notes

- Returns EntityCommandResponse
- The root entity id of the response is the business key identifier of the created customer employee span object. References CustomerEmployeeSpans
- The entity id of the response is the same as the root entity id.

## Request body

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Code` | `Int64` | no |  | unique | The human readable identifier of the customer employee span object. |
| `Description` | `String` | no |  | mandatory, max length 400 | The translated description of the customer employee span object. |

## Example

```json
{
  "Code": 0,
  "Description": null
}
```
