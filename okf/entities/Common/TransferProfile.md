---
type: API Entity
title: TransferProfiles
description: Represents a transfer profile.
resource: https://api.monitor.se/api/Monitor.API.Common.TransferProfile.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.TransferProfile.html
  title: Monitor API — TransferProfile
module: Common
api_class: TransferProfile
doc_name: TransferProfiles
endpoint: GET /api/v1/Common/TransferProfiles
guid: 8034FC32-051D-4CC8-990E-B3DF876E7561
permission: Show transfer profile
introduced_in: '22.1'
property_count: 12
references_out:
- /entities/Common/ConnectionProfile.md
- /entities/Common/OrderTransferSetting.md
- /entities/Common/Warehouse.md
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Inventory/PartPlanningInformation.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/CustomerOrderType.md
- /entities/Sales/QuoteRow.md
---

# TransferProfiles

Represents a transfer profile.

- **Module:** [Common](/modules/Common.md)
- **API class:** `TransferProfile`
- **Endpoint:** `GET /api/v1/Common/TransferProfiles`
- **Required permission:** Show transfer profile
- **GUID:** `8034FC32-051D-4CC8-990E-B3DF876E7561`
- **Introduced in:** 22.1

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the transfer profile. |
| `Number` | `Int64` | no |  | unique | The number of the transfer profile. |
| `Description` | `String` | no |  |  | The description of the transfer profile. |
| `Usages` | `Int32` | no |  | bitmask, enum | The usages type of the transfer profile. |
| `TargetRole` | `Int32` | no |  | enum, since 23.2 | The role of the transfer profile. |
| `IsVerified` | `Boolean` | no |  | since 23.2 | Specifies if this transfer profile is verified. |
| `IsActive` | `Boolean` | no |  | since 23.2 | Specifies if this transfer profile is active. |
| `ConnectionProfileId` | `Int64` | no | [ConnectionProfiles](/entities/Common/ConnectionProfile.md) | since 23.2 | The business key identifier of the transfer profile's connection profile. |
| `RemoteWarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) | since 23.2 | The business key identifier of the transfer profile's remote warehouse. |
| `OrderTransferSettingsId` | `Int64` | no | [OrderTransferSettings](/entities/Common/OrderTransferSetting.md) | since 23.2 | The business key identifier of the transfer profile's order transfer setting. |
| `SupplierId` | `Int64?` | yes | [Suppliers](/entities/Purchase/Supplier.md) | since 23.2 | The business key identifier of the transfer profile's supplier. |
| `CustomerCode` | `String` | no |  | max length 10, since 23.2 | The customer code of the transfer profile. |

## Enumerations

### Usages (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `CustomerOrderTransfer` | 1 |
| `PartSynchronization` | 2 |
| `PartInformation` | 4 |

### TargetRole

| Name | Value |
| --- | ---: |
| `ManufacturingCompany` | 0 |
| `SalesCompany` | 1 |


## Referenced by

**Inventory**

- [PartPlanningInformation](/entities/Inventory/PartPlanningInformation.md) — `DefaultTransferProfileId` (FK)

**Sales**

- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `TransferProfileId` (FK)
- [CustomerOrderTypes](/entities/Sales/CustomerOrderType.md) — `DefaultTransferProfileId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `TransferProfileId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "Usages": 0,
  "TargetRole": 0,
  "IsVerified": false,
  "IsActive": false,
  "ConnectionProfileId": 0,
  "RemoteWarehouseId": 0,
  "OrderTransferSettingsId": 0,
  "SupplierId": null,
  "CustomerCode": null
}
```
