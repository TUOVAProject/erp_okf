---
type: API Entity
title: Probabilities
description: Represents a probability.
resource: https://api.monitor.se/api/Monitor.API.Common.Probability.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Probability.html
  title: Monitor API — Probability
module: Common
api_class: Probability
doc_name: Probabilities
endpoint: GET /api/v1/Common/Probabilities
guid: 8eb552b1-9064-4067-9caf-4ff8779f9452
permission: Show probability codes
introduced_in: '2.18'
property_count: 5
referenced_by:
- /entities/Sales/Customer.md
- /entities/Sales/Quote.md
---

# Probabilities

Represents a probability.

- **Module:** [Common](/modules/Common.md)
- **API class:** `Probability`
- **Endpoint:** `GET /api/v1/Common/Probabilities`
- **Required permission:** Show probability codes
- **GUID:** `8eb552b1-9064-4067-9caf-4ff8779f9452`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the probability. |
| `Number` | `Int64` | no |  |  | The probability number. |
| `Description` | `String` | no |  |  | The translated description of the probability. |
| `Percentage` | `Decimal?` | yes |  |  | The probability percentage. |
| `IsPreset` | `Boolean` | no |  |  | Specifies if the probability is the default. |

## Referenced by

**Sales**

- [Customers](/entities/Sales/Customer.md) — `ActualCustomerProbability` (expand)
- [Customers](/entities/Sales/Customer.md) — `ActualCustomerProbabilityId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `Probability` (expand)
- [Quotes](/entities/Sales/Quote.md) — `ProbabilityId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "Percentage": null,
  "IsPreset": false
}
```
