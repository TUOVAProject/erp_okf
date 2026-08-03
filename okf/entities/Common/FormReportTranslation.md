---
type: API Entity
title: FormReportTranslations
description: Represents a form report translation.
resource: https://api.monitor.se/api/Monitor.API.Common.FormReportTranslation.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.FormReportTranslation.html
  title: Monitor API — FormReportTranslation
module: Common
api_class: FormReportTranslation
doc_name: FormReportTranslations
endpoint: GET /api/v1/Common/FormReportTranslations
guid: 3A02B90D-B1E2-4E64-BC3F-E31AC1B41E9C
introduced_in: '2.48'
property_count: 4
references_out:
- /entities/Common/FormReportTranslationGroup.md
referenced_by:
- /entities/Common/FormReportTranslationGroup.md
---

# FormReportTranslations

Represents a form report translation.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `FormReportTranslation`
- **Endpoint:** `GET /api/v1/Common/FormReportTranslations`
- **GUID:** `3A02B90D-B1E2-4E64-BC3F-E31AC1B41E9C`
- **Introduced in:** 2.48

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the translation. |
| `Phrase` | `String` | no |  | max length 800 | The overriding phrase text for the translation. |
| `PhraseId` | `Int64` | no |  |  | The identifier of the phrase that the translation overrides. |
| `FormReportTranslationGroupId` | `Int64` | no | [FormReportTranslationGroups](FormReportTranslationGroup.md) |  | The business key identifier of the translation group that the translation belongs to. |

## Referenced by

**Common**

- [FormReportTranslationGroups](FormReportTranslationGroup.md) — `Translations` (expand)


## Example

```json
{
  "Id": 0,
  "Phrase": null,
  "PhraseId": 0,
  "FormReportTranslationGroupId": 0
}
```
