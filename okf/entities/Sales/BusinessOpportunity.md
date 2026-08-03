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

- **Module:** [Sales](../../modules/Sales.md)
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
| `BusinessOpportunityGroupId` | `Int64?` | yes | [BusinessOpportunityGroups](BusinessOpportunityGroup.md) |  | The business key identifier of the business opportunity's group. |
| `BusinessOpportunityGroup` | `BusinessOpportunityGroups` | no | [BusinessOpportunityGroups](BusinessOpportunityGroup.md) | expandable | The business opportunity's group. |
| `BusinessOpportunityCategory` | `String` | no |  | max length 20 | The category of the business opportunity. |
| `SalesProcessTemplateId` | `Int64?` | yes | [SalesProcessTemplates](SalesProcessTemplate.md) |  | The business key identifier of the business opportunity's sales process template. |
| `SalesProcessTemplate` | `SalesProcessTemplates` | no | [SalesProcessTemplates](SalesProcessTemplate.md) | expandable | The business opportunity's sales process template. |
| `OurReferenceId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the business opportunity's our reference. |
| `OurReference` | `Persons` | no | [Persons](../Common/Person.md) | expandable | The business opportunity's our reference. |
| `Description` | `String` | no |  | max length 400 | The description of the business opportunity. |
| `Status` | `Int32` | no |  | enum | The status of the business opportunity. |
| `Priority` | `Int32` | no |  |  | The priority of the business opportunity. |
| `BusinessOpportunityTypeId` | `Int64?` | yes | [BusinessOpportunityTypes](BusinessOpportunityType.md) |  | The business key identifier of the business opportunity's type. |
| `BusinessOpportunityType` | `BusinessOpportunityTypes` | no | [BusinessOpportunityTypes](BusinessOpportunityType.md) | expandable | The business opportunity's type. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the business opportunity's comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The business opportunity's comment. |
| `ReasonLostCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the business opportunity's comment on lost opportunity. |
| `ReasonLostComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The business opportunity's comment on lost opportunity. |
| `TotalValue` | `Decimal?` | yes |  |  | The total value of the business opportunity. |
| `SellerId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the business opportunity's seller. |
| `Seller` | `Persons` | no | [Persons](../Common/Person.md) | expandable | The business opportunity's seller. |
| `Name` | `String` | no |  |  | The translated name of the business opportunity. |
| `ReferenceName` | `String` | no |  | max length 80 | The reference name of the business opportunity. |
| `ReasonCodeLostQuoteId` | `Int64?` | yes | [ReasonCodeLostQuotes](ReasonCodeLostQuote.md) |  | The business key identifier of the business opportunity's reason code for lost quote. |
| `ReasonCodeLostQuote` | `ReasonCodeLostQuotes` | no | [ReasonCodeLostQuotes](ReasonCodeLostQuote.md) | expandable | The business opportunity's reason code for lost quote. |
| `BusinessContactNoteHistories` | `BusinessContactNoteHistories[]` | no | [BusinessContactNoteHistories](../Common/BusinessContactNoteHistory.md) | expandable, collection | The business contact note history entries for the business opportunity. |
| `Customers` | `Customers[]` | no | [Customers](Customer.md) | expandable, collection | The customers on the business opportunity. |

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

- [BusinessOpportunityActivities](BusinessOpportunityActivity.md) — `OrderId` (FK)
- [BusinessOpportunityReferences](BusinessOpportunityReference.md) — `ParentId` (FK)
- [BusinessOpportunitySalesProcessSteps](BusinessOpportunitySalesProcessStep.md) — `ParentId` (FK)
- [Quotes](Quote.md) — `BusinessOpportunity` (expand)
- [Quotes](Quote.md) — `BusinessOpportunityId` (FK)


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
