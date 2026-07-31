---
type: API Entity
title: SalesProcessTemplates
description: Represents a sales process template.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesProcessTemplate.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesProcessTemplate.html
  title: Monitor API — SalesProcessTemplate
module: Sales
api_class: SalesProcessTemplate
doc_name: SalesProcessTemplates
endpoint: GET /api/v1/Sales/SalesProcessTemplates
guid: 3666bb12-374e-438a-8f76-2cdaf549959a
permission: Show business opportunity
introduced_in: '25.9'
property_count: 5
references_out:
- /entities/Sales/SalesProcessTemplateRow.md
referenced_by:
- /entities/Sales/BusinessOpportunity.md
- /entities/Sales/BusinessOpportunityType.md
- /entities/Sales/SalesProcessTemplateRow.md
---

# SalesProcessTemplates

Represents a sales process template.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `SalesProcessTemplate`
- **Endpoint:** `GET /api/v1/Sales/SalesProcessTemplates`
- **Required permission:** Show business opportunity
- **GUID:** `3666bb12-374e-438a-8f76-2cdaf549959a`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the sales process template. |
| `Code` | `String` | no |  | unique, max length 5 | The human readable identifier of the sales process template. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the sales process template is active. |
| `Description` | `String` | no |  | max length 400 | The translated description of the sales process template. |
| `Rows` | `SalesProcessTemplateRows[]` | no | [SalesProcessTemplateRows](/entities/Sales/SalesProcessTemplateRow.md) | expandable, collection | The rows of the sales process template. |

## Referenced by

**Sales**

- [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) — `SalesProcessTemplate` (expand)
- [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) — `SalesProcessTemplateId` (FK)
- [BusinessOpportunityTypes](/entities/Sales/BusinessOpportunityType.md) — `SalesProcessTemplate` (expand)
- [BusinessOpportunityTypes](/entities/Sales/BusinessOpportunityType.md) — `SalesProcessTemplateId` (FK)
- [SalesProcessTemplateRows](/entities/Sales/SalesProcessTemplateRow.md) — `ParentId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "IsActive": false,
  "Description": null,
  "Rows": null
}
```
