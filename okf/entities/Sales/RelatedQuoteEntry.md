---
type: API Entity
title: RelatedQuoteEntries
description: Represents a related quote entry.
resource: https://api.monitor.se/api/Monitor.API.Sales.RelatedQuoteEntry.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.RelatedQuoteEntry.html
  title: Monitor API — RelatedQuoteEntry
module: Sales
api_class: RelatedQuoteEntry
doc_name: RelatedQuoteEntries
endpoint: GET /api/v1/Sales/RelatedQuoteEntries
guid: 83B03101-C04D-4ECD-A94D-44CFF7022268
permission: Show quote
introduced_in: '26.2'
property_count: 4
references_out:
- /entities/Sales/Quote.md
- /entities/Sales/RelatedQuote.md
---

# RelatedQuoteEntries

Represents a related quote entry.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `RelatedQuoteEntry`
- **Endpoint:** `GET /api/v1/Sales/RelatedQuoteEntries`
- **Required permission:** Show quote
- **GUID:** `83B03101-C04D-4ECD-A94D-44CFF7022268`
- **Introduced in:** 26.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the related quote entry. |
| `QuoteId` | `Int64?` | yes | [Quotes](/entities/Sales/Quote.md) |  | The business key identifier of the entry's related quote. |
| `IsPrimary` | `Boolean` | no |  |  | Specifies if this is the primary related quote. |
| `RelatedQuotesId` | `Int64?` | yes | [RelatedQuotes](/entities/Sales/RelatedQuote.md) |  | The business key identifier of the entry's related quotes placeholder. |

## Example

```json
{
  "Id": 0,
  "QuoteId": null,
  "IsPrimary": false,
  "RelatedQuotesId": null
}
```
