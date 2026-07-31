---
type: API Entity
title: ResponseTimes
description: Represents a response time.
resource: https://api.monitor.se/api/Monitor.API.Purchase.ResponseTime.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.ResponseTime.html
  title: Monitor API — ResponseTime
module: Purchase
api_class: ResponseTime
doc_name: ResponseTimes
endpoint: GET /api/v1/Purchase/ResponseTimes
guid: 98c86b1e-1c6c-44d4-a137-4329af2226e7
permission: Show terms
introduced_in: '2.28'
property_count: 5
referenced_by:
- /entities/Purchase/Supplier.md
---

# ResponseTimes

Represents a response time.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `ResponseTime`
- **Endpoint:** `GET /api/v1/Purchase/ResponseTimes`
- **Required permission:** Show terms
- **GUID:** `98c86b1e-1c6c-44d4-a137-4329af2226e7`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the response time. |
| `Days` | `Int32?` | yes |  |  | The days of the response time. |
| `Description` | `String` | no |  |  | The description of the response time. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the response time. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the response time is default. |

## Referenced by

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `ResponseTime` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `ResponseTimeId` (FK)


## Example

```json
{
  "Id": 0,
  "Days": null,
  "Description": null,
  "Number": 0,
  "IsDefault": false
}
```
