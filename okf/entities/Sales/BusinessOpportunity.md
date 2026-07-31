---
type: API Entity
title: BusinessOpportunities
description: Represents a business opportunity.
resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunity.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunity.html
  title: Monitor API — BusinessOpportunity
module: Sales
api_class: BusinessOpportunity
doc_name: BusinessOpportunities
endpoint: GET /api/v1/Sales/BusinessOpportunities
guid: 6502c4f7-2fe6-49f1-9a75-4232ff9029eb
permission: Show business opportunity
introduced_in: '25.9'
property_count: 30
references_out:
- /entities/Common/BusinessContactNoteHistory.md
- /entities/Common/Comment.md
- /entities/Common/Person.md
- /entities/Sales/BusinessOpportunityGroup.md
- /entities/Sales/BusinessOpportunityType.md
- /entities/Sales/Customer.md
- /entities/Sales/ReasonCodeLostQuote.md
- /entities/Sales/SalesProcessTemplate.md
referenced_by:
- /entities/Sales/BusinessOpportunityActivity.md
- /entities/Sales/BusinessOpportunityReference.md
- /entities/Sales/BusinessOpportunitySalesProcessStep.md
- /entities/Sales/Quote.md
---

# BusinessOpportunities

Represents a business opportunity.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `BusinessOpportunity`
- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunities`
- **Required permission:** Show business opportunity
- **GUID:** `6502c4f7-2fe6-49f1-9a75-4232ff9029eb`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business opportunity. |
| `OpportunityNumber` | `String` | no |  | unique, max length 15 | The human readable identifier of the business opportunity. |
| `StartDate` | `DateTimeOffset` | no |  |  | The start date of the business opportunity. |
| `PlannedEndDate` | `DateTimeOffset?` | yes |  |  | The planned end date of the business opportunity. |
| `ActualEndDate` | `DateTimeOffset?` | yes |  |  | The actual end date of the business opportunity. |
| `BusinessOpportunityGroupId` | `Int64?` | yes | [BusinessOpportunityGroups](/entities/Sales/BusinessOpportunityGroup.md) |  | The business key identifier of the business opportunity's group. |
| `BusinessOpportunityGroup` | `BusinessOpportunityGroups` | no | [BusinessOpportunityGroups](/entities/Sales/BusinessOpportunityGroup.md) | expandable | The business opportunity's group. |
| `BusinessOpportunityCategory` | `String` | no |  | max length 20 | The category of the business opportunity. |
| `SalesProcessTemplateId` | `Int64?` | yes | [SalesProcessTemplates](/entities/Sales/SalesProcessTemplate.md) |  | The business key identifier of the business opportunity's sales process template. |
| `SalesProcessTemplate` | `SalesProcessTemplates` | no | [SalesProcessTemplates](/entities/Sales/SalesProcessTemplate.md) | expandable | The business opportunity's sales process template. |
| `OurReferenceId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the business opportunity's our reference. |
| `OurReference` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable | The business opportunity's our reference. |
| `Description` | `String` | no |  | max length 400 | The description of the business opportunity. |
| `Status` | `Int32` | no |  | enum | The status of the business opportunity. |
| `Priority` | `Int32` | no |  |  | The priority of the business opportunity. |
| `BusinessOpportunityTypeId` | `Int64?` | yes | [BusinessOpportunityTypes](/entities/Sales/BusinessOpportunityType.md) |  | The business key identifier of the business opportunity's type. |
| `BusinessOpportunityType` | `BusinessOpportunityTypes` | no | [BusinessOpportunityTypes](/entities/Sales/BusinessOpportunityType.md) | expandable | The business opportunity's type. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the business opportunity's comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The business opportunity's comment. |
| `ReasonLostCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the business opportunity's comment on lost opportunity. |
| `ReasonLostComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The business opportunity's comment on lost opportunity. |
| `TotalValue` | `Decimal?` | yes |  |  | The total value of the business opportunity. |
| `SellerId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the business opportunity's seller. |
| `Seller` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable | The business opportunity's seller. |
| `Name` | `String` | no |  |  | The translated name of the business opportunity. |
| `ReferenceName` | `String` | no |  | max length 80 | The reference name of the business opportunity. |
| `ReasonCodeLostQuoteId` | `Int64?` | yes | [ReasonCodeLostQuotes](/entities/Sales/ReasonCodeLostQuote.md) |  | The business key identifier of the business opportunity's reason code for lost quote. |
| `ReasonCodeLostQuote` | `ReasonCodeLostQuotes` | no | [ReasonCodeLostQuotes](/entities/Sales/ReasonCodeLostQuote.md) | expandable | The business opportunity's reason code for lost quote. |
| `BusinessContactNoteHistories` | `BusinessContactNoteHistories[]` | no | [BusinessContactNoteHistories](/entities/Common/BusinessContactNoteHistory.md) | expandable, collection | The business contact note history entries for the business opportunity. |
| `Customers` | `Customers[]` | no | [Customers](/entities/Sales/Customer.md) | expandable, collection | The customers on the business opportunity. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `InProgress` | 3 |
| `Finished` | 4 |
| `Cancelled` | 5 |
| `Pending` | 6 |
| `Historical` | 9 |


## Referenced by

**Sales**

- [BusinessOpportunityActivities](/entities/Sales/BusinessOpportunityActivity.md) — `OrderId` (FK)
- [BusinessOpportunityReferences](/entities/Sales/BusinessOpportunityReference.md) — `ParentId` (FK)
- [BusinessOpportunitySalesProcessSteps](/entities/Sales/BusinessOpportunitySalesProcessStep.md) — `ParentId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `BusinessOpportunity` (expand)
- [Quotes](/entities/Sales/Quote.md) — `BusinessOpportunityId` (FK)


## Example

```json
{
  "Id": 0,
  "OpportunityNumber": null,
  "StartDate": "0001-01-01T00:00:00+00:00",
  "PlannedEndDate": null,
  "ActualEndDate": null,
  "BusinessOpportunityGroupId": null,
  "BusinessOpportunityGroup": null,
  "BusinessOpportunityCategory": null,
  "SalesProcessTemplateId": null,
  "SalesProcessTemplate": null,
  "OurReferenceId": null,
  "OurReference": null,
  "Description": null,
  "Status": 0,
  "Priority": 0,
  "BusinessOpportunityTypeId": null,
  "BusinessOpportunityType": null,
  "CommentId": null,
  "Comment": null,
  "ReasonLostCommentId": null,
  "ReasonLostComment": null,
  "TotalValue": null,
  "SellerId": null,
  "Seller": null,
  "Name": null,
  "ReferenceName": null,
  "ReasonCodeLostQuoteId": null,
  "ReasonCodeLostQuote": null,
  "BusinessContactNoteHistories": null,
  "Customers": null
}
```
