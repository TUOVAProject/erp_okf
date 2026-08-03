---
type: API Entity
title: CurrencyExchangeRateChangeLogs
description: Represents a currency exchange rate entry.
resource: https://api.monitor.se/api/Monitor.API.Common.CurrencyExchangeRateChangeLog.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.CurrencyExchangeRateChangeLog.html
  title: Monitor API — CurrencyExchangeRateChangeLog
module: Common
api_class: CurrencyExchangeRateChangeLog
doc_name: CurrencyExchangeRateChangeLogs
endpoint: GET /api/v1/Common/CurrencyExchangeRateChangeLogs
permission: Show currencies
introduced_in: '2.26'
property_count: 5
references_out:
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
referenced_by:
- /entities/Common/Currency.md
---

# CurrencyExchangeRateChangeLogs

Represents a currency exchange rate entry.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `CurrencyExchangeRateChangeLog`
- **Endpoint:** `GET /api/v1/Common/CurrencyExchangeRateChangeLogs`
- **Required permission:** Show currencies
- **Introduced in:** 2.26

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the currency exchange rate change log entry. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](CurrencyExchangeType.md) |  | The currency exchange type of the entry. |
| `Rate` | `Decimal` | no |  |  | The exchange rate of the entry. |
| `ValidUntilDate` | `DateTimeOffset` | no |  |  | The date when entry was changed. |
| `CurrencyId` | `Int64` | no | [Currencies](Currency.md) | since 24.6 | The business key identifier of the currency the exchange rate log entry belongs to. |

## Referenced by

**Common**

- [Currencies](Currency.md) — `ExchangeRatesChangeLog` (expand)


## Example

```json
{
  "Id": 0,
  "CurrencyExchangeTypeId": 0,
  "Rate": 0.0,
  "ValidUntilDate": "0001-01-01T00:00:00+00:00",
  "CurrencyId": 0
}
```
