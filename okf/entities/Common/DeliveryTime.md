---
type: API Entity
title: DeliveryTimes
description: Represents a queryable delivery time.
resource: https://api.monitor.se/api/Monitor.API.Common.DeliveryTime.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.DeliveryTime.html
  title: Monitor API — DeliveryTime
module: Common
api_class: DeliveryTime
doc_name: DeliveryTimes
endpoint: GET /api/v1/Common/DeliveryTimes
guid: 9AEA81AE-DAF0-4692-AF28-6938D68D73D0
permission: Show terms
introduced_in: '23.6'
property_count: 5
referenced_by:
- /entities/Sales/Quote.md
---

# DeliveryTimes

Represents a queryable delivery time.

- **Module:** [Common](/modules/Common.md)
- **API class:** `DeliveryTime`
- **Endpoint:** `GET /api/v1/Common/DeliveryTimes`
- **Required permission:** Show terms
- **GUID:** `9AEA81AE-DAF0-4692-AF28-6938D68D73D0`
- **Introduced in:** 23.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the delivery time. |
| `Days` | `Int32` | no |  |  | The number of days until delivery of the delivery time. |
| `Description` | `String` | no |  |  | The translated description of the delivery time. |
| `Number` | `Int64` | no |  |  | The delivery time number. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the delivery time is the default time. |

## Referenced by

**Sales**

- [Quotes](/entities/Sales/Quote.md) — `DeliveryTime` (expand)
- [Quotes](/entities/Sales/Quote.md) — `DeliveryTimeId` (FK)


## Example

```json
{
  "Id": 0,
  "Days": 0,
  "Description": null,
  "Number": 0,
  "IsDefault": false
}
```
