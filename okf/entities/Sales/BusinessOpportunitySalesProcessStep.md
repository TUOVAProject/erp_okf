---
type: API Entity
title: BusinessOpportunitySalesProcessSteps
description: Represents a business opportunity sales process step.
resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunitySalesProcessStep.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunitySalesProcessStep.html
  title: Monitor API — BusinessOpportunitySalesProcessStep
module: Sales
api_class: BusinessOpportunitySalesProcessStep
doc_name: BusinessOpportunitySalesProcessSteps
endpoint: GET /api/v1/Sales/BusinessOpportunitySalesProcessSteps
guid: f1b30770-5735-4607-a3d8-8a341ca15e4c
permission: Show business opportunity
introduced_in: '25.9'
property_count: 13
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Person.md
- /entities/Sales/BusinessOpportunity.md
- /entities/Sales/SellerGroup.md
---

# BusinessOpportunitySalesProcessSteps

Represents a business opportunity sales process step.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `BusinessOpportunitySalesProcessStep`
- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunitySalesProcessSteps`
- **Required permission:** Show business opportunity
- **GUID:** `f1b30770-5735-4607-a3d8-8a341ca15e4c`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business opportunity sales process step. |
| `Code` | `Int64` | no |  |  | The code of the sales process step. |
| `Description` | `String` | no |  | max length 400 | The translated description of the sales process step. |
| `Probability` | `Int32` | no |  |  | The probability of the sales process step. |
| `LeadTime` | `Int32` | no |  |  | The lead time of the sales process step. |
| `Responsibility` | `Int32` | no |  | enum | Specifies what is responsibel for the sales process step. |
| `ResponsibleSellerId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The responsible seller of the sales process step. |
| `ResponsibleSellerGroupId` | `Int64?` | yes | [SellerGroups](SellerGroup.md) |  | The responsible seller group of the sales process step. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The responsible application user of the sales process step. |
| `ParentId` | `Int64?` | yes | [BusinessOpportunities](BusinessOpportunity.md) |  | The business opportunity the sales process step belongs to. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the sales process step. |
| `Status` | `Int32` | no |  | enum | The status of the sales process step. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the sales process step is active. |

## Enumerations

### Responsibility

| Name | Value |
| --- | ---: |
| `Seller` | 0 |
| `Group` | 1 |

### Status

| Name | Value |
| --- | ---: |
| `NotStarted` | 0 |
| `Started` | 1 |
| `Finished` | 2 |


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null,
  "Probability": 0,
  "LeadTime": 0,
  "Responsibility": 0,
  "ResponsibleSellerId": null,
  "ResponsibleSellerGroupId": null,
  "ResponsibleUserId": null,
  "ParentId": null,
  "RowIndex": null,
  "Status": 0,
  "IsActive": false
}
```
