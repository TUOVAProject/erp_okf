---
type: API Entity
title: Resellers
description: Represents a reseller.
resource: https://api.monitor.se/api/Monitor.API.Common.Reseller.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Reseller.html
  title: Monitor API — Reseller
module: Common
api_class: Reseller
doc_name: Resellers
endpoint: GET /api/v1/Common/Resellers
guid: 7018AEC2-A878-4285-92AC-8F1BDED87DE3
permission: Show customer
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Sales/Customer.md
---

# Resellers

Represents a reseller.

- **Module:** [Common](/modules/Common.md)
- **API class:** `Reseller`
- **Endpoint:** `GET /api/v1/Common/Resellers`
- **Required permission:** Show customer
- **GUID:** `7018AEC2-A878-4285-92AC-8F1BDED87DE3`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the reseller. |
| `Code` | `Int64` | no |  | unique | The reseller code. |
| `Name` | `String` | no |  | max length 80 | The name of the reseller. |
| `Provision` | `Decimal` | no |  |  | The reseller provision in percent. |

## Referenced by

**Sales**

- [Customers](/entities/Sales/Customer.md) — `Reseller` (expand)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Name": null,
  "Provision": 0.0
}
```
