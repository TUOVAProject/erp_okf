---
type: API Entity
title: EdiChannelConfigurations
description: Represents an Edi Channel Configuration.
resource: https://api.monitor.se/api/Monitor.API.Common.EdiChannelConfiguration.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.EdiChannelConfiguration.html
  title: Monitor API — EdiChannelConfiguration
module: Common
api_class: EdiChannelConfiguration
doc_name: EdiChannelConfigurations
endpoint: GET /api/v1/Common/EdiChannelConfigurations
guid: 4c3dc5d5-fad2-4d63-a3cf-61565b1e8196
introduced_in: '25.4'
property_count: 5
referenced_by:
- /entities/Common/EdiBehavior.md
---

# EdiChannelConfigurations

Represents an Edi Channel Configuration.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `EdiChannelConfiguration`
- **Endpoint:** `GET /api/v1/Common/EdiChannelConfigurations`
- **GUID:** `4c3dc5d5-fad2-4d63-a3cf-61565b1e8196`
- **Introduced in:** 25.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the edi channel configuration. |
| `ParentId` | `Int64` | no |  |  | The parent id of the edi channel configuration. |
| `ChannelId` | `Int64` | no |  |  | The channel id of the edi channel configuration. |
| `NotificationsActive` | `Boolean` | no |  |  | The notification active identifier of the edi channel configuration. |
| `Active` | `Boolean` | no |  |  | The active of the edi channel configuration. |

## Referenced by

**Common**

- [EdiBehaviors](EdiBehavior.md) — `EdiChannelConfigurations` (expand)


## Example

```json
{
  "Id": 0,
  "ParentId": 0,
  "ChannelId": 0,
  "NotificationsActive": false,
  "Active": false
}
```
