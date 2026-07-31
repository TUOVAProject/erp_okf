---
type: API Entity
title: WorkCenterManufacturingPrintSettings
description: Represents manufacturing print settings for a work center.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.WorkCenterManufacturingPrintSettings.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.WorkCenterManufacturingPrintSettings.html
  title: Monitor API — WorkCenterManufacturingPrintSettings
module: Manufacturing
api_class: WorkCenterManufacturingPrintSettings
doc_name: WorkCenterManufacturingPrintSettings
endpoint: GET /api/v1/Common/WorkCenterManufacturingPrintSettings
guid: 919CFF4D-0BCE-4244-ADE3-0F31C94378B1
permission: Show work center
introduced_in: '2.28'
property_count: 4
referenced_by:
- /entities/Manufacturing/WorkCenter.md
---

# WorkCenterManufacturingPrintSettings

Represents manufacturing print settings for a work center.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `WorkCenterManufacturingPrintSettings`
- **Endpoint:** `GET /api/v1/Common/WorkCenterManufacturingPrintSettings`
- **Required permission:** Show work center
- **GUID:** `919CFF4D-0BCE-4244-ADE3-0F31C94378B1`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the workcenter manufacturing print settings. |
| `Copies` | `Int32` | no |  |  | Number of copies of the document. |
| `PrintExternalDocuments` | `Boolean` | no |  |  | Specifies if external documents should be included in the printout. |
| `FormReportId` | `Int64` | no |  |  | The business key identifier of the form report the settings applies to. |

## Referenced by

**Manufacturing**

- [WorkCenters](/entities/Manufacturing/WorkCenter.md) — `ManufacturingPrintSettings` (expand)


## Example

```json
{
  "Id": 0,
  "Copies": 0,
  "PrintExternalDocuments": false,
  "FormReportId": 0
}
```
