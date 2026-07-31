---
type: API Entity
title: CustomReportDefinitions
description: Represents a queryable custom report definition.
resource: https://api.monitor.se/api/Monitor.API.Common.CustomReportDefinition.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.CustomReportDefinition.html
  title: Monitor API — CustomReportDefinition
module: Common
api_class: CustomReportDefinition
doc_name: CustomReportDefinitions
endpoint: GET /api/v1/Common/CustomReportDefinitions
guid: 888AEAB7-14E1-4A07-A3A1-CEFF67559DC1
introduced_in: '2.18'
property_count: 4
references_out:
- /entities/Common/CustomReportDisplayDefinition.md
referenced_by:
- /entities/Common/CustomReportDisplayDefinition.md
---

# CustomReportDefinitions

Represents a queryable custom report definition.

- **Module:** [Common](/modules/Common.md)
- **API class:** `CustomReportDefinition`
- **Endpoint:** `GET /api/v1/Common/CustomReportDefinitions`
- **GUID:** `888AEAB7-14E1-4A07-A3A1-CEFF67559DC1`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the custom report. |
| `ReportNumber` | `String` | no |  | unique, max length 10 | The report number of the custom report. |
| `Description` | `String` | no |  |  | The translated description of the custom report. |
| `DisplayDefinitions` | `CustomReportDisplayDefinitions[]` | no | [CustomReportDisplayDefinitions](/entities/Common/CustomReportDisplayDefinition.md) | expandable, collection | A collection of display definitions belonging to the custom report definition. |

## Referenced by

**Common**

- [CustomReportDisplayDefinitions](/entities/Common/CustomReportDisplayDefinition.md) — `ParentId` (FK)


## Example

```json
{
  "Id": 0,
  "ReportNumber": null,
  "Description": null,
  "DisplayDefinitions": null
}
```
