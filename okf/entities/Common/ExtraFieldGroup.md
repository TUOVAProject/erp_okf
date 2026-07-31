---
type: API Entity
title: ExtraFieldGroups
description: Represents an extra field group.
resource: https://api.monitor.se/api/Monitor.API.Common.ExtraFieldGroup.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ExtraFieldGroup.html
  title: Monitor API — ExtraFieldGroup
module: Common
api_class: ExtraFieldGroup
doc_name: ExtraFieldGroups
endpoint: GET /api/v1/Common/ExtraFieldGroups
guid: 41FA38FD-D9CD-4AC8-A677-F365F52043BD
permission: Show extra fields
introduced_in: '2.18'
property_count: 5
references_out:
- /entities/Common/ExtraFieldTemplate.md
referenced_by:
- /entities/Common/ExtraFieldTemplate.md
---

# ExtraFieldGroups

Represents an extra field group.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ExtraFieldGroup`
- **Endpoint:** `GET /api/v1/Common/ExtraFieldGroups`
- **Required permission:** Show extra fields
- **GUID:** `41FA38FD-D9CD-4AC8-A677-F365F52043BD`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the extra field group. |
| `Name` | `String` | no |  |  | The translated name of the extra field group. |
| `EntityId` | `Guid` | no |  |  | The business-domain identifier of the entity that the extra field group is defined for. |
| `RowNumber` | `Int32` | no |  |  | The row number of the extra field group. |
| `Templates` | `ExtraFieldTemplates[]` | no | [ExtraFieldTemplates](/entities/Common/ExtraFieldTemplate.md) | expandable, collection | A collection of extra field templates that belong to the extra field group. |

## Referenced by

**Common**

- [ExtraFieldTemplates](/entities/Common/ExtraFieldTemplate.md) — `ParentId` (FK)


## Example

```json
{
  "Id": 0,
  "Name": null,
  "EntityId": "00000000-0000-0000-0000-000000000000",
  "RowNumber": 0,
  "Templates": null
}
```
