---
type: API Entity
title: SalesProcessTemplateRows
description: Represents a sales process template row.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesProcessTemplateRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesProcessTemplateRow.html
  title: Monitor API — SalesProcessTemplateRow
module: Sales
api_class: SalesProcessTemplateRow
doc_name: SalesProcessTemplateRows
endpoint: GET /api/v1/Sales/SalesProcessTemplateRows
guid: 8ea28a1e-b83f-40c5-9e88-05a50b02985a
permission: Show business opportunity
introduced_in: '25.9'
property_count: 12
references_out:
- /entities/Common/Person.md
- /entities/Sales/SalesProcessStep.md
- /entities/Sales/SalesProcessTemplate.md
- /entities/Sales/SellerGroup.md
referenced_by:
- /entities/Sales/SalesProcessTemplate.md
---

# SalesProcessTemplateRows

Represents a sales process template row.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `SalesProcessTemplateRow`
- **Endpoint:** `GET /api/v1/Sales/SalesProcessTemplateRows`
- **Required permission:** Show business opportunity
- **GUID:** `8ea28a1e-b83f-40c5-9e88-05a50b02985a`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the sales process template row. |
| `Code` | `Int64` | no |  |  | The human readable identifier of the sales process template row. |
| `SalesProcessStepId` | `Int64` | no | [SalesProcessSteps](/entities/Sales/SalesProcessStep.md) |  | The business key identifier of the sales process template row's sales process step. |
| `SalesProcessStep` | `SalesProcessSteps` | no | [SalesProcessSteps](/entities/Sales/SalesProcessStep.md) | expandable | The sales process step of the sales process template row. |
| `Probability` | `Int32` | no |  |  | The probability of the sales process template row. |
| `LeadTime` | `Int32` | no |  |  | The lead time of the sales process template row. |
| `Responsibility` | `Int32` | no |  | enum | The responsibility of the sales process template row. |
| `ResponsibleSellerId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the sales process template row's responsible seller. |
| `ResponsibleSeller` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable | The sales process template row's responsible seller. |
| `ResponsibleSellerGroupId` | `Int64?` | yes | [SellerGroups](/entities/Sales/SellerGroup.md) |  | The business key identifier of the sales process template row's seller group. |
| `ResponsibleSellerGroup` | `SellerGroups` | no | [SellerGroups](/entities/Sales/SellerGroup.md) | expandable | The sales process template row's seller group. |
| `ParentId` | `Int64` | no | [SalesProcessTemplates](/entities/Sales/SalesProcessTemplate.md) |  | The business key identifier of the sales process template row's parent. |

## Enumerations

### Responsibility

| Name | Value |
| --- | ---: |
| `Seller` | 0 |
| `Group` | 1 |


## Referenced by

**Sales**

- [SalesProcessTemplates](/entities/Sales/SalesProcessTemplate.md) — `Rows` (expand)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "SalesProcessStepId": 0,
  "SalesProcessStep": null,
  "Probability": 0,
  "LeadTime": 0,
  "Responsibility": 0,
  "ResponsibleSellerId": null,
  "ResponsibleSeller": null,
  "ResponsibleSellerGroupId": null,
  "ResponsibleSellerGroup": null,
  "ParentId": 0
}
```
