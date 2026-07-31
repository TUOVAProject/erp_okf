---
type: API Entity
title: OrderTransferSettings
description: Represents an order transfer setting.
resource: https://api.monitor.se/api/Monitor.API.Common.OrderTransferSetting.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.OrderTransferSetting.html
  title: Monitor API — OrderTransferSetting
module: Common
api_class: OrderTransferSetting
doc_name: OrderTransferSettings
endpoint: GET /api/v1/Common/OrderTransferSettings
guid: 902041A1-6942-4E25-BB86-11F888B783D5
permission: Show setting
introduced_in: '23.2'
property_count: 4
referenced_by:
- /entities/Common/TransferProfile.md
---

# OrderTransferSettings

Represents an order transfer setting.

- **Module:** [Common](/modules/Common.md)
- **API class:** `OrderTransferSetting`
- **Endpoint:** `GET /api/v1/Common/OrderTransferSettings`
- **Required permission:** Show setting
- **GUID:** `902041A1-6942-4E25-BB86-11F888B783D5`
- **Introduced in:** 23.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the setting. |
| `ManufacturingCompanyPartIdentityTypeCode` | `String` | no |  | max length 10 | The manufacturing company part identity type code of the setting. |
| `ManufacturingCompanyUsePartOtherIdentities` | `Boolean` | no |  |  | Specifies if the manufacturing company use part other identities. |
| `ManufacturingCompanyOrderOrderTypeCode` | `String` | no |  | max length 15 | The manufacturing company orders order type code. |

## Referenced by

**Common**

- [TransferProfiles](/entities/Common/TransferProfile.md) — `OrderTransferSettingsId` (FK)


## Example

```json
{
  "Id": 0,
  "ManufacturingCompanyPartIdentityTypeCode": null,
  "ManufacturingCompanyUsePartOtherIdentities": false,
  "ManufacturingCompanyOrderOrderTypeCode": null
}
```
