---
type: API Entity
title: AutoCompleteConfigurations
description: Represents an auto-complete configuration.
resource: https://api.monitor.se/api/Monitor.API.Common.AutoCompleteConfiguration.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.AutoCompleteConfiguration.html
  title: Monitor API — AutoCompleteConfiguration
module: Common
api_class: AutoCompleteConfiguration
doc_name: AutoCompleteConfigurations
endpoint: GET /api/v1/Common/AutoCompleteConfigurations
guid: 3EDCE59F-DC9E-4963-B0D2-72BDA03C9A99
introduced_in: '2.46'
property_count: 4
---

# AutoCompleteConfigurations

Represents an auto-complete configuration.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `AutoCompleteConfiguration`
- **Endpoint:** `GET /api/v1/Common/AutoCompleteConfigurations`
- **GUID:** `3EDCE59F-DC9E-4963-B0D2-72BDA03C9A99`
- **Introduced in:** 2.46

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the auto-complete configuration. |
| `Description` | `String` | no |  |  | The description of the auto-complete configuration. |
| `IsPreset` | `Boolean` | no |  |  | Specifies whether or not the auto-complete configuration is a preset configuration. |
| `PopupTypeId` | `Guid` | no |  |  | The GUID identifier of the popup-type that the auto-complete configuration applies to. |

## Example

```json
{
  "Id": 0,
  "Description": null,
  "IsPreset": false,
  "PopupTypeId": "00000000-0000-0000-0000-000000000000"
}
```
