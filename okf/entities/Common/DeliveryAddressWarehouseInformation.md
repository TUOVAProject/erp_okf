---
type: API Entity
title: DeliveryAddressWarehouseInformations
description: Represents a queryable delivery address warehouse information entry.
resource: https://api.monitor.se/api/Monitor.API.Common.DeliveryAddressWarehouseInformation.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.DeliveryAddressWarehouseInformation.html
  title: Monitor API — DeliveryAddressWarehouseInformation
module: Common
api_class: DeliveryAddressWarehouseInformation
doc_name: DeliveryAddressWarehouseInformations
endpoint: GET /api/v1/Common/DeliveryAddressWarehouseInformations
guid: F8FF21F1-DDFF-4363-BD87-D12425990A7E
introduced_in: '2.43'
property_count: 8
references_out:
- /entities/Common/DeliveryAddress.md
- /entities/Common/DeliveryMethod.md
- /entities/Common/DeliveryTerm.md
- /entities/Common/Warehouse.md
referenced_by:
- /entities/Common/DeliveryAddress.md
---

# DeliveryAddressWarehouseInformations

Represents a queryable delivery address warehouse information entry.

- **Module:** [Common](/modules/Common.md)
- **API class:** `DeliveryAddressWarehouseInformation`
- **Endpoint:** `GET /api/v1/Common/DeliveryAddressWarehouseInformations`
- **GUID:** `F8FF21F1-DDFF-4363-BD87-D12425990A7E`
- **Introduced in:** 2.43

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the warehouse information entry. |
| `WarehouseId` | `Int64?` | yes | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse that the information pertains to. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](/entities/Common/DeliveryMethod.md) |  | The business key identifier of the delivery method that applies to the warehouse and delivery address. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](/entities/Common/DeliveryTerm.md) |  | The business key identifier of the delivery term that applies to the warehouse and delivery address. |
| `TransportTime` | `TimeSpan?` | yes |  |  | The transport time that applies to the warehouse and delivery address. |
| `DeliveryWeekdays` | `Int32` | no |  | bitmask, enum | Specifies what days delivery can be made for the warehouse and delivery address. |
| `DestinationForDeliveryTerm` | `String` | no |  | max length 80 | Specifies the destination for the delivery term. |
| `ParentId` | `Int64` | no | [DeliveryAddresses](/entities/Common/DeliveryAddress.md) |  | The business key identifier of the delivery address that the warehouse information pertains to. |

## Enumerations

### DeliveryWeekdays (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Monday` | 1 |
| `Tuesday` | 2 |
| `Wednesday` | 4 |
| `Thursday` | 8 |
| `Friday` | 16 |
| `Saturday` | 32 |
| `Sunday` | 64 |


## Referenced by

**Common**

- [DeliveryAddresses](/entities/Common/DeliveryAddress.md) — `Warehouses` (expand)


## Example

```json
{
  "Id": 0,
  "WarehouseId": null,
  "DeliveryMethodId": null,
  "DeliveryTermId": null,
  "TransportTime": null,
  "DeliveryWeekdays": 0,
  "DestinationForDeliveryTerm": null,
  "ParentId": 0
}
```
