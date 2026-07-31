---
type: API Type
title: FormReportData
description: Represents form report data from MONITOR.
resource: https://api.monitor.se/api/Monitor.API.Common.FormReportData.html
tags:
- Common
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.FormReportData.html
  title: Monitor API — FormReportData
module: Common
api_class: FormReportData
doc_name: FormReportData
property_count: 3
references_out:
- /entities/Common/FileLink.md
---

# FormReportData

Represents form report data from MONITOR.

- **Module:** [Common](/modules/Common.md)
- **API class:** `FormReportData`
- **Endpoint:** none — this is a payload type, not a queryable resource.

## Notes

- Used by the following types:

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Name` | `String` | no |  |  | The name of the form report. |
| `Data` | `String` | no |  |  | The form report PDF data represented as a Base64 string. |
| `FileLinkIds` | `Int64[]` | no | [FileLink](/entities/Common/FileLink.md) | collection, since 2.41 | The business key identifiers of the file links associated with this report. References FileLink . |

## Example

```json
{
  "Name": null,
  "Data": null,
  "FileLinkIds": null
}
```
