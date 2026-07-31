---
type: API Entity
title: RelatedQuotes
description: Represents a placeholder for related quotes.
resource: https://api.monitor.se/api/Monitor.API.Sales.RelatedQuote.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.RelatedQuote.html
  title: Monitor API — RelatedQuote
module: Sales
api_class: RelatedQuote
doc_name: RelatedQuotes
endpoint: GET /api/v1/Sales/RelatedQuotes
guid: B95A7A13-BF1D-44C1-861D-7B6AD42A719E
permission: Show quote
introduced_in: '26.2'
property_count: 1
referenced_by:
- /entities/Sales/Quote.md
- /entities/Sales/RelatedQuoteEntry.md
---

# RelatedQuotes

Represents a placeholder for related quotes.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `RelatedQuote`
- **Endpoint:** `GET /api/v1/Sales/RelatedQuotes`
- **Required permission:** Show quote
- **GUID:** `B95A7A13-BF1D-44C1-861D-7B6AD42A719E`
- **Introduced in:** 26.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the related quote placeholder. |

## Referenced by

**Sales**

- [Quotes](/entities/Sales/Quote.md) — `RelatedQuotesId` (FK)
- [RelatedQuoteEntries](/entities/Sales/RelatedQuoteEntry.md) — `RelatedQuotesId` (FK)


## Example

```json
{
  "Id": 0
}
```
