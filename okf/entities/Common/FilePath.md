---
type: API Entity
title: FilePaths
description: Represents a queryable file path.
resource: https://api.monitor.se/api/Monitor.API.Common.FilePath.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.FilePath.html
  title: Monitor API — FilePath
module: Common
api_class: FilePath
doc_name: FilePaths
endpoint: GET /api/v1/Common/FilePaths
guid: D4041A7A-385E-46FB-81A7-75F1BE942EF6
permission: Show paths
introduced_in: '2.18'
property_count: 7
referenced_by:
- /entities/Common/ServerPrinter.md
---

# FilePaths

Represents a queryable file path.

- **Module:** [Common](/modules/Common.md)
- **API class:** `FilePath`
- **Endpoint:** `GET /api/v1/Common/FilePaths`
- **Required permission:** Show paths
- **GUID:** `D4041A7A-385E-46FB-81A7-75F1BE942EF6`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the file path. |
| `Path` | `String` | no |  | unique, max length 255 | The server-local path of the file path. |
| `Description` | `String` | no |  | max length 200 | The description of the file path. |
| `Active` | `Boolean` | no |  | since 2.45 | Specifies whether the file path is active or not. |
| `Category` | `Int32` | no |  | enum, since 26.3 | The category of the file path. |
| `FileType` | `Int32` | no |  | enum, since 26.3 | The file type of the file path. |
| `PathType` | `Int32` | no |  | bitmask, enum, since 26.3 | The path type of the file path. |

## Enumerations

### Category

| Name | Value |
| --- | ---: |
| `FileViewer` | 1 |
| `ExportAccounting` | 2 |
| `ExportAgent` | 3 |
| `ExportFactoring` | 4 |
| `ExportServerPrinter` | 5 |
| `ImportAccounting` | 6 |
| `ImportSerialNumbers` | 7 |
| `ImportAdditionalIds` | 8 |

### FileType

| Name | Value |
| --- | ---: |
| `FileSystem` | 0 |
| `SharePoint` | 1 |

### PathType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `LocalServerDrives` | 1 |
| `UncServerShare` | 2 |
| `SharePoint` | 4 |
| `AvailablePaths` | 8 |
| `RegisteredPaths` | 16 |
| `LocalClient` | 32 |


## Referenced by

**Common**

- [ServerPrinters](/entities/Common/ServerPrinter.md) — `FilePath` (expand)
- [ServerPrinters](/entities/Common/ServerPrinter.md) — `FilePathId` (FK)
- [ServerPrinters](/entities/Common/ServerPrinter.md) — `SubPath` (FK)


## Example

```json
{
  "Id": 0,
  "Path": null,
  "Description": null,
  "Active": false,
  "Category": 0,
  "FileType": 0,
  "PathType": 0
}
```
