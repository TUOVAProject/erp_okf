---
type: API Entity
title: ServerPrinters
description: Represents a server printer that can be used to print documents via the
  MONITOR server.
resource: https://api.monitor.se/api/Monitor.API.Common.ServerPrinter.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ServerPrinter.html
  title: Monitor API — ServerPrinter
module: Common
api_class: ServerPrinter
doc_name: ServerPrinters
endpoint: GET /api/v1/Common/ServerPrinters
guid: 33D557AF-A625-45EF-87FB-0B07DED04BFD
introduced_in: '2.52'
property_count: 13
references_out:
- /entities/Common/FilePath.md
referenced_by:
- /entities/Common/ApplicationUserPrinter.md
---

# ServerPrinters

Represents a server printer that can be used to print documents via the MONITOR server.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ServerPrinter`
- **Endpoint:** `GET /api/v1/Common/ServerPrinters`
- **GUID:** `33D557AF-A625-45EF-87FB-0B07DED04BFD`
- **Introduced in:** 2.52

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the server printer. |
| `Number` | `String` | no |  | unique, max length 20 | The human readable identifier of the server printer. |
| `Description` | `String` | no |  |  | The translated description of the server printer. |
| `Name` | `String` | no |  | max length 255 | The name of the printer that the server printer connects to. |
| `Orientation` | `Int32` | no |  | enum | The printout orientation to apply to the server printer. |
| `DuplexMode` | `Int32` | no |  | enum | The duplex mode to apply to the server printer. |
| `PaperSize` | `Int32` | no |  | enum | The paper size to apply to the server printer. |
| `Width` | `Int32` | no |  |  | The paper width in millimeters to use if the paper size is "custom". |
| `Height` | `Int32` | no |  |  | The paper height in millimeters to use if the paper size is "custom". |
| `ColorMode` | `Int32` | no |  | enum | The color mode to apply to the server printer. |
| `FilePathId` | `Int64?` | yes | [FilePaths](/entities/Common/FilePath.md) | since 26.4 | The business key identifier of the file path used as output path of a Microsoft Print To PDF Printer References FilePaths . |
| `FilePath` | `FilePaths` | no | [FilePaths](/entities/Common/FilePath.md) | expandable, since 26.4 | The file path used as output path of a Microsoft Print To PDF Printer References FilePaths . |
| `SubPath` | `String` | no | [FilePaths](/entities/Common/FilePath.md) | max length 300, since 26.4 | The sub path applied to used as output path of a Microsoft Print To PDF Printer |

## Enumerations

### Orientation

| Name | Value |
| --- | ---: |
| `Portrait` | 0 |
| `Landscape` | 1 |
| `Auto` | 2 |

### DuplexMode

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `LongEdge` | 1 |
| `ShortEdge` | 2 |

### PaperSize

| Name | Value |
| --- | ---: |
| `A4` | 0 |
| `A3` | 1 |
| `A5` | 2 |
| `Custom` | 3 |
| `PrinterDefault` | 4 |
| `Letter` | 5 |

### ColorMode

| Name | Value |
| --- | ---: |
| `BlackAndWhite` | 0 |
| `FullColor` | 1 |


## Referenced by

**Common**

- [ApplicationUserPrinters](/entities/Common/ApplicationUserPrinter.md) — `ServerPrinterId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": null,
  "Description": null,
  "Name": null,
  "Orientation": 0,
  "DuplexMode": 0,
  "PaperSize": 0,
  "Width": 0,
  "Height": 0,
  "ColorMode": 0,
  "FilePathId": null,
  "FilePath": null,
  "SubPath": null
}
```
