---
type: API Entity
title: PartConfigurations
description: Represents a part configuration.
resource: https://api.monitor.se/api/Monitor.API.Common.PartConfiguration.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PartConfiguration.html
  title: Monitor API — PartConfiguration
module: Common
api_class: PartConfiguration
doc_name: PartConfigurations
endpoint: GET /api/v1/Common/PartConfigurations
guid: E73969AC-6664-4679-83E3-23BDC14BD32C
permission: Show part
introduced_in: '2.55'
property_count: 4
references_out:
- /entities/Common/Comment.md
- /entities/Common/PartConfigurationResult.md
referenced_by:
- /entities/Common/PartConfigurationPreset.md
- /entities/Common/PartConfigurationResult.md
- /entities/Common/RemotePartConfiguration.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/QuoteRow.md
---

# PartConfigurations

Represents a part configuration.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `PartConfiguration`
- **Endpoint:** `GET /api/v1/Common/PartConfigurations`
- **Required permission:** Show part
- **GUID:** `E73969AC-6664-4679-83E3-23BDC14BD32C`
- **Introduced in:** 2.55

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part configuration. |
| `ResultId` | `Int64?` | yes | [PartConfigurationResults](PartConfigurationResult.md) |  | The business key identifier of the configuration's result. |
| `CommentId` | `Int64?` | yes | [Comments](Comment.md) |  | The business key identifier of the comment that belongs to the configuration. |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The comment that belongs to the configuration. |

## Referenced by

**Common**

- [PartConfigurationPresets](PartConfigurationPreset.md) — `PartConfigurationId` (FK)
- [PartConfigurationResults](PartConfigurationResult.md) — `PartConfigurationId` (FK)
- [RemotePartConfigurations](RemotePartConfiguration.md) — `PartConfigurationIdInRemoteCompany` (FK)

**Manufacturing**

- [ManufacturingOrders](../Manufacturing/ManufacturingOrder.md) — `PartConfigurationId` (FK)

**Sales**

- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `PartConfigurationIdInRemoteCompany` (FK)
- [QuoteRows](../Sales/QuoteRow.md) — `PartConfigurationIdInRemoteCompany` (FK)


## Example

```json
{
  "Id": 0,
  "ResultId": null,
  "CommentId": null,
  "Comment": null
}
```
