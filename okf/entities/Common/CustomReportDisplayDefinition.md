---
type: API Entity
title: CustomReportDisplayDefinitions
description: Represents a queryable custom report display definition.
resource: https://api.monitor.se/api/Monitor.API.Common.CustomReportDisplayDefinition.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.CustomReportDisplayDefinition.html
  title: Monitor API — CustomReportDisplayDefinition
module: Common
api_class: CustomReportDisplayDefinition
doc_name: CustomReportDisplayDefinitions
endpoint: GET /api/v1/Common/CustomReportDisplayDefinitions
guid: 74DDBC7F-7649-416D-BA9A-4FA8AF1BC7DA
introduced_in: '2.18'
property_count: 6
references_out:
- /entities/Common/CustomReportDefinition.md
referenced_by:
- /entities/Common/CustomReportDefinition.md
---

# CustomReportDisplayDefinitions

Represents a queryable custom report display definition.

- **Module:** [Common](/modules/Common.md)
- **API class:** `CustomReportDisplayDefinition`
- **Endpoint:** `GET /api/v1/Common/CustomReportDisplayDefinitions`
- **GUID:** `74DDBC7F-7649-416D-BA9A-4FA8AF1BC7DA`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the custom report display definition. |
| `DisplayId` | `Guid` | no |  | since 2.40 | The identifier of the custom report display definition. |
| `Description` | `String` | no |  |  | The translated description of the custom report display definition. |
| `ReportType` | `Int32` | no |  | enum | The report type of the custom report display definition. |
| `Sql` | `String` | no |  |  | The SQL query of the custom report display definition. |
| `ParentId` | `Int64` | no | [CustomReportDefinitions](/entities/Common/CustomReportDefinition.md) |  | The business key identifier of the parent custom report definition. References CustomReportDefinitions . |

## Enumerations

### ReportType

| Name | Value |
| --- | ---: |
| `Grid` | 0 |
| `Report` | 1 |
| `SubReport` | 2 |


## Referenced by

**Common**

- [CustomReportDefinitions](/entities/Common/CustomReportDefinition.md) — `DisplayDefinitions` (expand)


## Example

```json
{
  "Id": 0,
  "DisplayId": "00000000-0000-0000-0000-000000000000",
  "Description": null,
  "ReportType": 0,
  "Sql": null,
  "ParentId": 0
}
```
