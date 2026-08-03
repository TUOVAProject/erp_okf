---
type: API Entity
title: ExtraFieldOptionTemplates
description: Represents an extra field option template.
resource: https://api.monitor.se/api/Monitor.API.Common.ExtraFieldOptionTemplate.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ExtraFieldOptionTemplate.html
  title: Monitor API — ExtraFieldOptionTemplate
module: Common
api_class: ExtraFieldOptionTemplate
doc_name: ExtraFieldOptionTemplates
endpoint: GET /api/v1/Common/ExtraFieldOptionTemplates
guid: 08DC4F64-ABEE-40BE-97BA-A39552C2DCCC
permission: Show extra fields
introduced_in: '2.18'
property_count: 5
references_out:
- /entities/Common/ExtraFieldTemplate.md
referenced_by:
- /entities/Common/ExtraField.md
- /entities/Common/ExtraFieldTemplate.md
---

# ExtraFieldOptionTemplates

Represents an extra field option template.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ExtraFieldOptionTemplate`
- **Endpoint:** `GET /api/v1/Common/ExtraFieldOptionTemplates`
- **Required permission:** Show extra fields
- **GUID:** `08DC4F64-ABEE-40BE-97BA-A39552C2DCCC`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the extra field option template. |
| `Code` | `String` | no |  | max length 12 | The human readable code of the extra field option template. |
| `IsActive` | `Boolean` | no |  |  | Specifies whether or not the extra field option template is active in the system. |
| `Description` | `String` | no |  |  | The translated description of the extra field option template. |
| `ExtraFieldTemplateId` | `Int64` | no | [ExtraFieldTemplates](ExtraFieldTemplate.md) |  | The business key identifier of the extra field template that the extra field option template belongs to. |

## Referenced by

**Common**

- [ExtraFieldTemplates](ExtraFieldTemplate.md) — `OptionTemplates` (expand)
- [ExtraFields](ExtraField.md) — `SelectedOption` (expand)
- [ExtraFields](ExtraField.md) — `SelectedOptionId` (FK)
- [ExtraFields](ExtraField.md) — `SelectedOptionIds` (FK)
- [ExtraFields](ExtraField.md) — `SelectedOptions` (expand)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "IsActive": false,
  "Description": null,
  "ExtraFieldTemplateId": 0
}
```
