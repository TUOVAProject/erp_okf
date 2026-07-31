---
type: API Type
title: AccountingExportResponse
description: The response object used by accounting exports.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingExportResponse.html
tags:
- Accounting
- type
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingExportResponse.html
  title: Monitor API — AccountingExportResponse
module: Accounting
api_class: AccountingExportResponse
doc_name: AccountingExportResponse
introduced_in: '23.9'
property_count: 3
---

# AccountingExportResponse

The response object used by accounting exports.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `AccountingExportResponse`
- **Endpoint:** none — this is a payload type, not a queryable resource.
- **Introduced in:** 23.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `CommandName` | `String` | no |  |  | The name of the command that was invoked. |
| `Name` | `String` | no |  |  | The name of the accounting exporter. |
| `Data` | `String` | no |  |  | The accounting export data represented as a Base64 string. |

## Example

```json
{
  "CommandName": null,
  "Name": null,
  "Data": null
}
```
