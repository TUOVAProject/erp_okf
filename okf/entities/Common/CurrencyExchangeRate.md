---
type: API Entity
title: CurrencyExchangeRates
description: Represents a currency exchange rate entry.
resource: https://api.monitor.se/api/Monitor.API.Common.CurrencyExchangeRate.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.CurrencyExchangeRate.html
  title: Monitor API — CurrencyExchangeRate
module: Common
api_class: CurrencyExchangeRate
doc_name: CurrencyExchangeRates
endpoint: GET /api/v1/Common/CurrencyExchangeRates
guid: B411E551-3556-447A-B1E6-B887C876F345
permission: Show currencies
introduced_in: '2.18'
property_count: 3
references_out:
- /entities/Common/CurrencyExchangeType.md
referenced_by:
- /entities/Common/Currency.md
---

# CurrencyExchangeRates

Represents a currency exchange rate entry.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `CurrencyExchangeRate`
- **Endpoint:** `GET /api/v1/Common/CurrencyExchangeRates`
- **Required permission:** Show currencies
- **GUID:** `B411E551-3556-447A-B1E6-B887C876F345`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the currency exchange rate entry. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](CurrencyExchangeType.md) |  | The currency exchange type of the entry. |
| `Rate` | `Decimal` | no |  |  | The exchange rate of the entry. |

## Referenced by

**Common**

- [Currencies](Currency.md) — `ExchangeRates` (expand)


## Example

```json
{
  "Id": 0,
  "CurrencyExchangeTypeId": 0,
  "Rate": 0.0
}
```
