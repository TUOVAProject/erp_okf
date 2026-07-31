---
type: API Entity
title: ValidityTimes
description: Represents a validity time.
resource: https://api.monitor.se/api/Monitor.API.Sales.ValidityTime.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.ValidityTime.html
  title: Monitor API — ValidityTime
module: Sales
api_class: ValidityTime
doc_name: ValidityTimes
endpoint: GET /api/v1/Sales/ValidityTimes
guid: 21001bbf-9c0a-4453-bf9d-fb9313a9bf8f
permission: Show terms
introduced_in: '2.18'
property_count: 6
referenced_by:
- /entities/Sales/Customer.md
- /entities/Sales/Quote.md
---

# ValidityTimes

Represents a validity time.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `ValidityTime`
- **Endpoint:** `GET /api/v1/Sales/ValidityTimes`
- **Required permission:** Show terms
- **GUID:** `21001bbf-9c0a-4453-bf9d-fb9313a9bf8f`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the validity time. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the validity time. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the validity time is default. |
| `Days` | `Int32` | no |  |  | Specifies the validity time in days. |
| `Description` | `String` | no |  | max length 35 | The translated description of the validity time. |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |

## Referenced by

**Sales**

- [Customers](/entities/Sales/Customer.md) — `ValidityTime` (expand)
- [Customers](/entities/Sales/Customer.md) — `ValidityTimeId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `ValidityTime` (expand)
- [Quotes](/entities/Sales/Quote.md) — `ValidityTimeId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "IsDefault": false,
  "Days": 0,
  "Description": null,
  "CompanyIds": null
}
```
