---
type: API Entity
title: FormReportTranslationGroups
description: Represents a form report translation group.
resource: https://api.monitor.se/api/Monitor.API.Common.FormReportTranslationGroup.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.FormReportTranslationGroup.html
  title: Monitor API — FormReportTranslationGroup
module: Common
api_class: FormReportTranslationGroup
doc_name: FormReportTranslationGroups
endpoint: GET /api/v1/Common/FormReportTranslationGroups
guid: EF268C33-EED6-4E25-81AB-9B615FEDC2D9
introduced_in: '2.48'
property_count: 6
references_out:
- /entities/Common/FormReportTranslation.md
referenced_by:
- /entities/Common/FormReportTranslation.md
---

# FormReportTranslationGroups

Represents a form report translation group.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `FormReportTranslationGroup`
- **Endpoint:** `GET /api/v1/Common/FormReportTranslationGroups`
- **GUID:** `EF268C33-EED6-4E25-81AB-9B615FEDC2D9`
- **Introduced in:** 2.48

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the translation group. |
| `DocumentFont` | `Int32` | no |  | enum | The type of document font that is applied for the translation group. |
| `IsPreset` | `Boolean` | no |  |  | Whether or not the translation group is a preset delivered with MONITOR or not. |
| `Description` | `String` | no |  |  | The translated description of the translation group. |
| `Code` | `String` | no |  | unique, max length 20 | The human readable identifier of the translation group. |
| `Translations` | `FormReportTranslations[]` | no | [FormReportTranslations](FormReportTranslation.md) | collection | The translations that belong to the translation group. |

## Enumerations

### DocumentFont

| Name | Value |
| --- | ---: |
| `Default` | 0 |
| `SimplifiedChinese` | 1 |
| `Thai` | 2 |


## Referenced by

**Common**

- [FormReportTranslations](FormReportTranslation.md) — `FormReportTranslationGroupId` (FK)


## Example

```json
{
  "Id": 0,
  "DocumentFont": 0,
  "IsPreset": false,
  "Description": null,
  "Code": null,
  "Translations": null
}
```
