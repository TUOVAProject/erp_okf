---
type: API Entity
title: BusinessOpportunityActivityTemplates
description: Represents a business opportunity activity template.
resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityActivityTemplate.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityActivityTemplate.html
  title: Monitor API — BusinessOpportunityActivityTemplate
module: Sales
api_class: BusinessOpportunityActivityTemplate
doc_name: BusinessOpportunityActivityTemplates
endpoint: GET /api/v1/Sales/BusinessOpportunityActivityTemplates
guid: 3e50ac40-635e-4d2a-a648-b2442276a2bd
permission: Show business opportunity
introduced_in: '25.9'
property_count: 4
references_out:
- /entities/Sales/BusinessOpportunityActivityTemplateRow.md
referenced_by:
- /entities/Sales/BusinessOpportunityActivityTemplateRow.md
- /entities/Sales/BusinessOpportunityType.md
---

# BusinessOpportunityActivityTemplates

Represents a business opportunity activity template.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `BusinessOpportunityActivityTemplate`
- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityActivityTemplates`
- **Required permission:** Show business opportunity
- **GUID:** `3e50ac40-635e-4d2a-a648-b2442276a2bd`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business opportunity activity template. |
| `Code` | `Int64` | no |  |  | The human readable identifier of the business opportunity activity template. |
| `Description` | `String` | no |  | max length 400 | The translated description of the business opportunity activity template. |
| `Rows` | `BusinessOpportunityActivityTemplateRows[]` | no | [BusinessOpportunityActivityTemplateRows](BusinessOpportunityActivityTemplateRow.md) | expandable, collection | The rows of the business opportunity activity template. |

## Referenced by

**Sales**

- [BusinessOpportunityActivityTemplateRows](BusinessOpportunityActivityTemplateRow.md) — `ActivityTemplateId` (FK)
- [BusinessOpportunityTypes](BusinessOpportunityType.md) — `BusinessOpportunityActivityTemplate` (expand)
- [BusinessOpportunityTypes](BusinessOpportunityType.md) — `BusinessOpportunityActivityTemplateId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null,
  "Rows": null
}
```
