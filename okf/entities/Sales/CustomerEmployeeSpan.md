---
type: API Entity
title: CustomerEmployeeSpans
description: Represents a customer employee span.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerEmployeeSpan.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerEmployeeSpan.html
  title: Monitor API — CustomerEmployeeSpan
module: Sales
api_class: CustomerEmployeeSpan
doc_name: CustomerEmployeeSpans
endpoint: GET /api/v1/Sales/CustomerEmployeeSpans
guid: cec462ad-3efb-4099-aaf5-c6f0883dff3c
permission: Show customer
introduced_in: '24.3'
property_count: 3
referenced_by:
- /entities/Sales/Customer.md
---

# CustomerEmployeeSpans

Represents a customer employee span.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerEmployeeSpan`
- **Endpoint:** `GET /api/v1/Sales/CustomerEmployeeSpans`
- **Required permission:** Show customer
- **GUID:** `cec462ad-3efb-4099-aaf5-c6f0883dff3c`
- **Introduced in:** 24.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer employee span. |
| `Code` | `Int64` | no |  |  | The human readable key identifier of customer employee span. |
| `Description` | `String` | no |  |  | The description of customer employee span. |

## Referenced by

**Sales**

- [Customers](Customer.md) — `EmployeeSpan` (expand)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null
}
```
