---
type: API Entity
title: RemotePartConfigurations
description: Represents a remote part configuration.
resource: https://api.monitor.se/api/Monitor.API.Common.RemotePartConfiguration.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.RemotePartConfiguration.html
  title: Monitor API — RemotePartConfiguration
module: Common
api_class: RemotePartConfiguration
doc_name: RemotePartConfigurations
endpoint: GET /api/v1/Common/RemotePartConfigurations
guid: EACC3250-0C15-4BD4-A733-798BA5582BA2
permission: Show part
introduced_in: '24.8'
property_count: 3
references_out:
- /entities/Common/PartConfiguration.md
- /entities/Common/RemotePartConfigurationRow.md
---

# RemotePartConfigurations

Represents a remote part configuration.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `RemotePartConfiguration`
- **Endpoint:** `GET /api/v1/Common/RemotePartConfigurations`
- **Required permission:** Show part
- **GUID:** `EACC3250-0C15-4BD4-A733-798BA5582BA2`
- **Introduced in:** 24.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | /// The business key identifier of the remote part configuration. |
| `PartConfigurationIdInRemoteCompany` | `Int64` | no | [PartConfigurations](PartConfiguration.md) |  | The business key identifier of the row's part configuration in the remote company. |
| `Rows` | `RemotePartConfigurationRows[]` | no | [RemotePartConfigurationRows](RemotePartConfigurationRow.md) | expandable, collection | A collection of remote comfiguration rows that belong to the remote configuration. |

## Example

```json
{
  "Id": 0,
  "PartConfigurationIdInRemoteCompany": 0,
  "Rows": null
}
```
