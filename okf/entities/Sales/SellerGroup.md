---
type: API Entity
title: SellerGroups
description: Represents a seller group.
resource: https://api.monitor.se/api/Monitor.API.Sales.SellerGroup.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SellerGroup.html
  title: Monitor API — SellerGroup
module: Sales
api_class: SellerGroup
doc_name: SellerGroups
endpoint: GET /api/v1/Sales/SellerGroups
guid: 8a391eb8-ef86-4124-9059-f52a994b9660
permission: Show business opportunity
introduced_in: '25.9'
property_count: 4
referenced_by:
- /entities/Sales/BusinessOpportunitySalesProcessStep.md
- /entities/Sales/SalesProcessTemplateRow.md
---

# SellerGroups

Represents a seller group.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `SellerGroup`
- **Endpoint:** `GET /api/v1/Sales/SellerGroups`
- **Required permission:** Show business opportunity
- **GUID:** `8a391eb8-ef86-4124-9059-f52a994b9660`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the seller group. |
| `Code` | `Int64` | no |  | unique | The human readable identifier of the seller group. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the seller group is active. |
| `Description` | `String` | no |  | max length 400 | The translated description of the seller group. |

## Referenced by

**Sales**

- [BusinessOpportunitySalesProcessSteps](/entities/Sales/BusinessOpportunitySalesProcessStep.md) — `ResponsibleSellerGroupId` (FK)
- [SalesProcessTemplateRows](/entities/Sales/SalesProcessTemplateRow.md) — `ResponsibleSellerGroup` (expand)
- [SalesProcessTemplateRows](/entities/Sales/SalesProcessTemplateRow.md) — `ResponsibleSellerGroupId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "IsActive": false,
  "Description": null
}
```
