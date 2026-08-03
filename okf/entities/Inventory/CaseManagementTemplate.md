---
type: API Entity
title: CaseManagementTemplates
description: Represents a case management template.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementTemplate.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementTemplate.html
  title: Monitor API — CaseManagementTemplate
module: Inventory
api_class: CaseManagementTemplate
doc_name: CaseManagementTemplates
endpoint: GET /api/v1/Inventory/CaseManagementTemplates
guid: 7d501c12-a6ec-41f5-ba4d-560b65315ba0
permission: Show basic data for case
introduced_in: '23.9'
property_count: 7
references_out:
- /entities/Inventory/CaseManagementTemplateCost.md
- /entities/Inventory/CaseManagementTemplateNode.md
- /entities/Inventory/CaseManagementType.md
referenced_by:
- /entities/Inventory/CaseManagementTemplateCost.md
- /entities/Inventory/CaseManagementTemplateNode.md
---

# CaseManagementTemplates

Represents a case management template.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `CaseManagementTemplate`
- **Endpoint:** `GET /api/v1/Inventory/CaseManagementTemplates`
- **Required permission:** Show basic data for case
- **GUID:** `7d501c12-a6ec-41f5-ba4d-560b65315ba0`
- **Introduced in:** 23.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case management template. |
| `Number` | `Int32` | no |  |  | The human readable identifier of the case management template. |
| `Description` | `String` | no |  |  | The description of the case management template. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the case management template is default. |
| `CaseManagementTypeId` | `Int64?` | yes | [CaseManagementType](CaseManagementType.md) |  | The business key identifier of the case management type. |
| `CaseManagementTemplateNode` | `CaseManagementTemplateNodes[]` | no | [CaseManagementTemplateNodes](CaseManagementTemplateNode.md) | expandable, collection | The case management template node of the case management template. |
| `CaseManagementTemplateCost` | `CaseManagementTemplateCosts[]` | no | [CaseManagementTemplateCosts](CaseManagementTemplateCost.md) | expandable, collection | The case management template cost of the case management template. |

## Referenced by

**Inventory**

- [CaseManagementTemplateCosts](CaseManagementTemplateCost.md) — `ParentId` (FK)
- [CaseManagementTemplateNodes](CaseManagementTemplateNode.md) — `ParentId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "IsDefault": false,
  "CaseManagementTypeId": null,
  "CaseManagementTemplateNode": null,
  "CaseManagementTemplateCost": null
}
```
