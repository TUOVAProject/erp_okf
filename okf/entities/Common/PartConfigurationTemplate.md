---
type: API Entity
title: PartConfigurationTemplates
description: Represents a part configuration template.
resource: https://api.monitor.se/api/Monitor.API.Common.PartConfigurationTemplate.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PartConfigurationTemplate.html
  title: Monitor API — PartConfigurationTemplate
module: Common
api_class: PartConfigurationTemplate
doc_name: PartConfigurationTemplates
endpoint: GET /api/v1/Common/PartConfigurationTemplates
guid: 8A3093D6-5E77-41FA-85EC-02E766FF7792
permission: Show part
introduced_in: '2.55'
property_count: 6
references_out:
- /entities/Common/Comment.md
referenced_by:
- /entities/Common/PartConfigurationResult.md
- /entities/Inventory/Part.md
---

# PartConfigurationTemplates

Represents a part configuration template.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `PartConfigurationTemplate`
- **Endpoint:** `GET /api/v1/Common/PartConfigurationTemplates`
- **Required permission:** Show part
- **GUID:** `8A3093D6-5E77-41FA-85EC-02E766FF7792`
- **Introduced in:** 2.55

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part configuration template. |
| `Version` | `Int32` | no |  |  | The version of the template. |
| `Code` | `String` | no |  | max length 20 | The human readable identifier of the template. |
| `Description` | `String` | no |  |  | The decription of the template. |
| `CommentId` | `Int64?` | yes | [Comments](Comment.md) |  | The business key identifier of the comment that belongs to the template. |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The comment that belongs to the template. |

## Referenced by

**Common**

- [PartConfigurationResults](PartConfigurationResult.md) — `TemplateId` (FK)

**Inventory**

- [Parts](../Inventory/Part.md) — `ConfigurationTemplate` (expand)


## Example

```json
{
  "Id": 0,
  "Version": 0,
  "Code": null,
  "Description": null,
  "CommentId": null,
  "Comment": null
}
```
