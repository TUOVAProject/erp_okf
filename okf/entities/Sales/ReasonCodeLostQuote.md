---
type: API Entity
title: ReasonCodeLostQuotes
description: Represents a reason code for a lost quote.
resource: https://api.monitor.se/api/Monitor.API.Sales.ReasonCodeLostQuote.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.ReasonCodeLostQuote.html
  title: Monitor API — ReasonCodeLostQuote
module: Sales
api_class: ReasonCodeLostQuote
doc_name: ReasonCodeLostQuotes
endpoint: GET /api/v1/Sales/ReasonCodeLostQuotes
guid: 7C5B1AE1-61DC-4D45-9345-E4E82833C325
permission: Show cause codes
introduced_in: '2.18'
property_count: 5
referenced_by:
- /entities/Sales/BusinessOpportunity.md
- /entities/Sales/Quote.md
---

# ReasonCodeLostQuotes

Represents a reason code for a lost quote.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `ReasonCodeLostQuote`
- **Endpoint:** `GET /api/v1/Sales/ReasonCodeLostQuotes`
- **Required permission:** Show cause codes
- **GUID:** `7C5B1AE1-61DC-4D45-9345-E4E82833C325`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the reason code. |
| `Code` | `String` | no |  | unique, max length 6 | The human readable identifier of the reason code. |
| `Description` | `String` | no |  | max length 35 | The translated description of the reason code. |
| `CommentMandatory` | `Boolean` | no |  |  | Specifies if a comment is mandatory for this reason code. |
| `Active` | `Boolean` | no |  |  | Specifies if the reason code is active. |

## Referenced by

**Sales**

- [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) — `ReasonCodeLostQuote` (expand)
- [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) — `ReasonCodeLostQuoteId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `ReasonCodeLostQuote` (expand)
- [Quotes](/entities/Sales/Quote.md) — `ReasonCodeLostQuoteId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "CommentMandatory": false,
  "Active": false
}
```
