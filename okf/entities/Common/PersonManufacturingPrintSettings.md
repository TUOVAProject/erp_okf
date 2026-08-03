---
type: API Entity
title: PersonManufacturingPrintSettings
description: Represents manufacturing print settings for a person.
resource: https://api.monitor.se/api/Monitor.API.Common.PersonManufacturingPrintSettings.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PersonManufacturingPrintSettings.html
  title: Monitor API — PersonManufacturingPrintSettings
module: Common
api_class: PersonManufacturingPrintSettings
doc_name: PersonManufacturingPrintSettings
endpoint: GET /api/v1/Common/PersonManufacturingPrintSettings
guid: 0013D9FD-51F4-406A-9624-A14DBE304634
permission: Show person
introduced_in: '2.28'
property_count: 4
referenced_by:
- /entities/Common/Person.md
---

# PersonManufacturingPrintSettings

Represents manufacturing print settings for a person.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `PersonManufacturingPrintSettings`
- **Endpoint:** `GET /api/v1/Common/PersonManufacturingPrintSettings`
- **Required permission:** Show person
- **GUID:** `0013D9FD-51F4-406A-9624-A14DBE304634`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the person manufacturing print settings. |
| `Copies` | `Int32` | no |  |  | Number of copies of the document. |
| `PrintExternalDocuments` | `Boolean` | no |  |  | Specifies if external documents should be included in the printout. |
| `FormReportId` | `Int64` | no |  |  | The business key identifier of the form report the settings applies to. |

## Referenced by

**Common**

- [Persons](Person.md) — `ManufacturingPrintSettings` (expand)


## Example

```json
{
  "Id": 0,
  "Copies": 0,
  "PrintExternalDocuments": false,
  "FormReportId": 0
}
```
