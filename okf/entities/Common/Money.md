---
type: API Type
title: Money
description: An object composite representing a money value.
resource: https://api.monitor.se/api/Monitor.API.Common.Money.html
tags:
- Common
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Money.html
  title: Monitor API — Money
module: Common
api_class: Money
doc_name: Money
introduced_in: '2.33'
property_count: 2
references_out:
- /entities/Common/Currency.md
---

# Money

An object composite representing a money value.

- **Module:** [Common](/modules/Common.md)
- **API class:** `Money`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 2.33

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Amount` | `Decimal` | no |  |  | The money amount. |
| `CurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency that the amount is specified in. |

## Example

```json
{
  "Amount": 0.0,
  "CurrencyId": null
}
```
