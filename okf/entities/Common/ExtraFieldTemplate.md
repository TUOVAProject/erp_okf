---
type: API Entity
title: ExtraFieldTemplates
description: Represents an extra field template.
resource: https://api.monitor.se/api/Monitor.API.Common.ExtraFieldTemplate.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ExtraFieldTemplate.html
  title: Monitor API — ExtraFieldTemplate
module: Common
api_class: ExtraFieldTemplate
doc_name: ExtraFieldTemplates
endpoint: GET /api/v1/Common/ExtraFieldTemplates
guid: E74EFF2A-DDB8-4457-A4A4-4EC46EB5CEB5
permission: Show extra fields
introduced_in: '2.18'
property_count: 8
references_out:
- /entities/Common/ExtraFieldGroup.md
- /entities/Common/ExtraFieldOptionTemplate.md
referenced_by:
- /entities/Common/ExtraFieldGroup.md
- /entities/Common/ExtraFieldOptionTemplate.md
- /entities/Manufacturing/Preparation.md
---

# ExtraFieldTemplates

Represents an extra field template.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ExtraFieldTemplate`
- **Endpoint:** `GET /api/v1/Common/ExtraFieldTemplates`
- **Required permission:** Show extra fields
- **GUID:** `E74EFF2A-DDB8-4457-A4A4-4EC46EB5CEB5`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the extra field template. |
| `Name` | `String` | no |  |  | The translated name of the extra field template. |
| `Description` | `String` | no |  |  | The translated description of the extra field template. |
| `Type` | `Int32` | no |  | enum | The extra field template type. |
| `ParentId` | `Int64` | no | [ExtraFieldGroups](/entities/Common/ExtraFieldGroup.md) |  | The business key identifier of the extra field group that the template belongs to. |
| `RowNumber` | `Int32` | no |  |  | The row number of the extra field template. |
| `Identifier` | `String` | no |  | max length 12 | The alphanumeric identifier of the extra field template. |
| `OptionTemplates` | `ExtraFieldOptionTemplates[]` | no | [ExtraFieldOptionTemplates](/entities/Common/ExtraFieldOptionTemplate.md) | expandable, collection | The extra field option templates that belong to the extra field template. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `String` | 0 |
| `Integer` | 1 |
| `Decimal` | 2 |
| `Date` | 3 |
| `DateTime` | 4 |
| `Comment` | 5 |
| `Options` | 6 |
| `MultiOptions` | 7 |


## Referenced by

**Common**

- [ExtraFieldGroups](/entities/Common/ExtraFieldGroup.md) — `Templates` (expand)
- [ExtraFieldOptionTemplates](/entities/Common/ExtraFieldOptionTemplate.md) — `ExtraFieldTemplateId` (FK)

**Manufacturing**

- [Preparations](/entities/Manufacturing/Preparation.md) — `VariantXAxis` (expand)
- [Preparations](/entities/Manufacturing/Preparation.md) — `VariantXAxisId` (FK)
- [Preparations](/entities/Manufacturing/Preparation.md) — `VariantYAxis` (expand)
- [Preparations](/entities/Manufacturing/Preparation.md) — `VariantYAxisId` (FK)


## Example

```json
{
  "Id": 0,
  "Name": null,
  "Description": null,
  "Type": 0,
  "ParentId": 0,
  "RowNumber": 0,
  "Identifier": null,
  "OptionTemplates": null
}
```
