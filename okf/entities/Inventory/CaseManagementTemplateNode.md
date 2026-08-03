---
type: API Entity
title: CaseManagementTemplateNodes
description: Represents a case management template node.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementTemplateNode.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseManagementTemplateNode.html
  title: Monitor API — CaseManagementTemplateNode
module: Inventory
api_class: CaseManagementTemplateNode
doc_name: CaseManagementTemplateNodes
endpoint: GET /api/v1/Inventory/CaseManagementTemplateNodes
guid: 8f557596-d54f-45e5-abcb-a7782e7a5f52
permission: Show basic data for case
introduced_in: '23.9'
property_count: 16
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Comment.md
- /entities/Inventory/CaseManagementActivity.md
- /entities/Inventory/CaseManagementPhase.md
- /entities/Inventory/CaseManagementTemplate.md
referenced_by:
- /entities/Inventory/CaseManagementTemplate.md
---

# CaseManagementTemplateNodes

Represents a case management template node.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `CaseManagementTemplateNode`
- **Endpoint:** `GET /api/v1/Inventory/CaseManagementTemplateNodes`
- **Required permission:** Show basic data for case
- **GUID:** `8f557596-d54f-45e5-abcb-a7782e7a5f52`
- **Introduced in:** 23.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case management template node. |
| `ActivityId` | `Int64?` | yes | [CaseManagementActivities](CaseManagementActivity.md) |  | The business key identifier of the case management activity. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the case management template node comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The comment of the case management template node. |
| `PlannedTime` | `TimeSpan?` | yes |  |  | The planned time of the case management template node. |
| `LeadTime` | `Int32?` | yes |  |  | The lead time of the case management template node in work days. |
| `Status` | `Int32` | no |  | enum | The status for the case management template node. |
| `IsReminder` | `Boolean` | no |  |  | Whether or not to create a reminder for the case management template node. |
| `IsMandatory` | `Boolean` | no |  |  | Specifies if the case management template node is mandatory. |
| `IsIncludeActivityOnDocument` | `Boolean` | no |  |  | Whether or not to include activity on document for the case management template node. |
| `IsChargeable` | `Boolean` | no |  |  | Specifies if the case management template node is chargeable. |
| `UserId` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier for the application user of the case management template node. |
| `PhaseId` | `Int64?` | yes | [CaseManagementPhases](CaseManagementPhase.md) |  | The business key identifier for the case management phase of the case management template node. |
| `ParentId` | `Int64?` | yes | [CaseManagementTemplates](CaseManagementTemplate.md) |  | The business key identifier of the case management template. |
| `ParentNodeId` | `Int64?` | yes |  |  | The business key identifier of the case management template node's parent that the case management template node belongs to. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the case management template node. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `NotStarted` | 0 |
| `Started` | 1 |


## Referenced by

**Inventory**

- [CaseManagementTemplates](CaseManagementTemplate.md) — `CaseManagementTemplateNode` (expand)


## Example

```json
{
  "Id": 0,
  "ActivityId": null,
  "CommentId": null,
  "Comment": null,
  "PlannedTime": null,
  "LeadTime": null,
  "Status": 0,
  "IsReminder": false,
  "IsMandatory": false,
  "IsIncludeActivityOnDocument": false,
  "IsChargeable": false,
  "UserId": null,
  "PhaseId": null,
  "ParentId": null,
  "ParentNodeId": null,
  "RowIndex": null
}
```
