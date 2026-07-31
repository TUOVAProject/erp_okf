---
type: API Entity
title: PartConfigurationPresets
description: Represents a part configuration preset.
resource: https://api.monitor.se/api/Monitor.API.Common.PartConfigurationPreset.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PartConfigurationPreset.html
  title: Monitor API — PartConfigurationPreset
module: Common
api_class: PartConfigurationPreset
doc_name: PartConfigurationPresets
endpoint: GET /api/v1/Common/PartConfigurationPresets
guid: 983A2EF1-C515-44CE-AF50-14758F86E602
permission: Show part
introduced_in: '2.55'
property_count: 8
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/PartConfiguration.md
---

# PartConfigurationPresets

Represents a part configuration preset.

- **Module:** [Common](/modules/Common.md)
- **API class:** `PartConfigurationPreset`
- **Endpoint:** `GET /api/v1/Common/PartConfigurationPresets`
- **Required permission:** Show part
- **GUID:** `983A2EF1-C515-44CE-AF50-14758F86E602`
- **Introduced in:** 2.55

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part configuration preset. |
| `Name` | `String` | no |  | max length 50 | The name of the preset. |
| `ChangedDate` | `DateTimeOffset?` | yes |  |  | The date and time the preset was last changed. |
| `ChangedBy` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the application user who last changed the preset. |
| `CreatedDate` | `DateTimeOffset` | no |  |  | The date and time the preset was created. |
| `CreatedBy` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the application user who created the preset. |
| `PartConfigurationId` | `Int64?` | yes | [PartConfigurations](/entities/Common/PartConfiguration.md) |  | The business key identifier of the preset's configuration. |
| `Type` | `Int32` | no |  | enum, since 23.7 | The type of part configuration preset. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Normal` | 0 |
| `Temporary` | 1 |


## Example

```json
{
  "Id": 0,
  "Name": null,
  "ChangedDate": null,
  "ChangedBy": null,
  "CreatedDate": "0001-01-01T00:00:00+00:00",
  "CreatedBy": null,
  "PartConfigurationId": null,
  "Type": 0
}
```
