---
type: API Entity
title: BusinessOpportunityTypes
description: Represents a business opportunity type.
resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityType.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityType.html
  title: Monitor API — BusinessOpportunityType
module: Sales
api_class: BusinessOpportunityType
doc_name: BusinessOpportunityTypes
endpoint: GET /api/v1/Sales/BusinessOpportunityTypes
guid: b7640a9a-eae7-444d-bcff-e05e63360be7
permission: Show business opportunity
introduced_in: '25.9'
property_count: 17
references_out:
- /entities/Common/Comment.md
- /entities/Common/Person.md
- /entities/Sales/BusinessOpportunityActivityTemplate.md
- /entities/Sales/BusinessOpportunityGroup.md
- /entities/Sales/SalesProcessTemplate.md
referenced_by:
- /entities/Sales/BusinessOpportunity.md
---

# BusinessOpportunityTypes

Represents a business opportunity type.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `BusinessOpportunityType`
- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityTypes`
- **Required permission:** Show business opportunity
- **GUID:** `b7640a9a-eae7-444d-bcff-e05e63360be7`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business opportunity type. |
| `Code` | `Int64` | no |  | unique | The human readable identifier of the business opportunity type. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the business opportunity type is active. |
| `Description` | `String` | no |  | max length 400 | The translated description of the business opportunity type. |
| `Prefix` | `String` | no |  | max length 3 | The prefix of the opportunity number created by the business opportunity type. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the business opportunity type is the default type. |
| `Priority` | `Int32` | no |  |  | The priority of the business opportunity type. |
| `BusinessOpportunityGroupId` | `Int64?` | yes | [BusinessOpportunityGroups](BusinessOpportunityGroup.md) |  | The business key identifier of the business opportunity type's business opportunity group. |
| `BusinessOpportunityGroup` | `BusinessOpportunityGroups` | no | [BusinessOpportunityGroups](BusinessOpportunityGroup.md) | expandable | The business opportunity type's business opportunity group. |
| `ResponsibleSellerId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the business opportunity type's .responsible seller. |
| `ResponsibleSeller` | `Persons` | no | [Persons](../Common/Person.md) | expandable | The business opportunity type's .responsible seller. |
| `SalesProcessTemplateId` | `Int64?` | yes | [SalesProcessTemplates](SalesProcessTemplate.md) |  | The business key identifier of the business opportunity type's .sales process template. |
| `SalesProcessTemplate` | `SalesProcessTemplates` | no | [SalesProcessTemplates](SalesProcessTemplate.md) | expandable | The business opportunity type's .sales process template. |
| `BusinessOpportunityActivityTemplateId` | `Int64?` | yes | [BusinessOpportunityActivityTemplates](BusinessOpportunityActivityTemplate.md) |  | The business key identifier of the business opportunity type's .activity template. |
| `BusinessOpportunityActivityTemplate` | `BusinessOpportunityActivityTemplates` | no | [BusinessOpportunityActivityTemplates](BusinessOpportunityActivityTemplate.md) |  | The business opportunity type's .activity template. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the business opportunity type's .comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The business opportunity type's .comment. |

## Referenced by

**Sales**

- [BusinessOpportunities](BusinessOpportunity.md) — `BusinessOpportunityType` (expand)
- [BusinessOpportunities](BusinessOpportunity.md) — `BusinessOpportunityTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "IsActive": false,
  "Description": null,
  "Prefix": null,
  "IsDefault": false,
  "Priority": 0,
  "BusinessOpportunityGroupId": null,
  "BusinessOpportunityGroup": null,
  "ResponsibleSellerId": null,
  "ResponsibleSeller": null,
  "SalesProcessTemplateId": null,
  "SalesProcessTemplate": null,
  "BusinessOpportunityActivityTemplateId": null,
  "BusinessOpportunityActivityTemplate": null,
  "CommentId": null,
  "Comment": null
}
```
