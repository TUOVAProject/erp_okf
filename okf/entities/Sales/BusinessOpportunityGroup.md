---
type: API Entity
title: BusinessOpportunityGroups
description: Represents a business opportunity group.
resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityGroup.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityGroup.html
  title: Monitor API — BusinessOpportunityGroup
module: Sales
api_class: BusinessOpportunityGroup
doc_name: BusinessOpportunityGroups
endpoint: GET /api/v1/Sales/BusinessOpportunityGroups
guid: a0e1099d-5eb4-4321-9b47-e13f7e55ac35
permission: Show business opportunity
introduced_in: '25.9'
property_count: 4
referenced_by:
- /entities/Sales/BusinessOpportunity.md
- /entities/Sales/BusinessOpportunityType.md
---

# BusinessOpportunityGroups

Represents a business opportunity group.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `BusinessOpportunityGroup`
- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityGroups`
- **Required permission:** Show business opportunity
- **GUID:** `a0e1099d-5eb4-4321-9b47-e13f7e55ac35`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business opportunity group. |
| `Code` | `Int64` | no |  | unique | The human readable identifier of the business opportunity group. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the business opportunity group is active. |
| `Description` | `String` | no |  | max length 400 | The translated description of the business opportunity group. |

## Referenced by

**Sales**

- [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) — `BusinessOpportunityGroup` (expand)
- [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) — `BusinessOpportunityGroupId` (FK)
- [BusinessOpportunityTypes](/entities/Sales/BusinessOpportunityType.md) — `BusinessOpportunityGroup` (expand)
- [BusinessOpportunityTypes](/entities/Sales/BusinessOpportunityType.md) — `BusinessOpportunityGroupId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "IsActive": false,
  "Description": null
}
```
