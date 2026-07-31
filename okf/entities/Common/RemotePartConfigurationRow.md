---
type: API Entity
title: RemotePartConfigurationRows
description: Represents a remote part configuration row.
resource: https://api.monitor.se/api/Monitor.API.Common.RemotePartConfigurationRow.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.RemotePartConfigurationRow.html
  title: Monitor API — RemotePartConfigurationRow
module: Common
api_class: RemotePartConfigurationRow
doc_name: RemotePartConfigurationRows
endpoint: GET /api/v1/Common/RemotePartConfigurationRows
guid: 2B61E815-C3E1-4D5F-AF69-60FB97EEE3EB
permission: Show part
introduced_in: '24.8'
property_count: 6
referenced_by:
- /entities/Common/RemotePartConfiguration.md
---

# RemotePartConfigurationRows

Represents a remote part configuration row.

- **Module:** [Common](/modules/Common.md)
- **API class:** `RemotePartConfigurationRow`
- **Endpoint:** `GET /api/v1/Common/RemotePartConfigurationRows`
- **Required permission:** Show part
- **GUID:** `2B61E815-C3E1-4D5F-AF69-60FB97EEE3EB`
- **Introduced in:** 24.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the remote part configuration row. |
| `ParentId` | `Int64` | no |  |  | The business key identifier of the remote part configuration. |
| `ManualPriceOrDiscount` | `Boolean` | no |  |  | Indicates manual change of price or discount. |
| `PriceEach` | `Decimal` | no |  |  | The price set. |
| `Discount` | `Decimal` | no |  |  | The discount set. |
| `CurrencyCode` | `String` | no |  | since 26.2 | The currency set. |

## Referenced by

**Common**

- [RemotePartConfigurations](/entities/Common/RemotePartConfiguration.md) — `Rows` (expand)


## Example

```json
{
  "Id": 0,
  "ParentId": 0,
  "ManualPriceOrDiscount": false,
  "PriceEach": 0.0,
  "Discount": 0.0,
  "CurrencyCode": null
}
```
