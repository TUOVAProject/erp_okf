---
type: API Entity
title: PartPlanningInformation
description: Represents part planning information for a warehouse.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartPlanningInformation.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartPlanningInformation.html
  title: Monitor API — PartPlanningInformation
module: Inventory
api_class: PartPlanningInformation
doc_name: PartPlanningInformation
endpoint: GET /api/v1/Inventory/PartPlanningInformation
guid: 9215F190-5E07-46AD-9A9F-A46BE27A7007
permission: Show part
introduced_in: '2.18'
property_count: 26
references_out:
- /entities/Common/Person.md
- /entities/Common/TransferProfile.md
- /entities/Common/Warehouse.md
- /entities/Inventory/AbcCode.md
- /entities/Purchase/SupplierPartLink.md
referenced_by:
- /entities/Inventory/Part.md
---

# PartPlanningInformation

Represents part planning information for a warehouse.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `PartPlanningInformation`
- **Endpoint:** `GET /api/v1/Inventory/PartPlanningInformation`
- **Required permission:** Show part
- **GUID:** `9215F190-5E07-46AD-9A9F-A46BE27A7007`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part planning information. |
| `ContactId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the contact person of the part planning information. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse that the part planning information is defined for. |
| `AbcCodeId` | `Int64?` | yes | [AbcCodes](/entities/Inventory/AbcCode.md) | since 2.31 | The business key identifier of the AbcCode used. |
| `AcquisitionWarehouseId` | `Int64?` | yes | [Warehouses](/entities/Common/Warehouse.md) | since 2.31 | The business key identifier of the warehouse to refill from. |
| `Eoq` | `Decimal` | no |  | since 2.31 | The economic order quantity. |
| `RoundingBase` | `Decimal` | no |  | since 2.31 | The rounding quantity for orders. |
| `SafetyStock` | `Decimal` | no |  | since 2.31 | The safety stock for the part . |
| `AnnualVolume` | `Decimal` | no |  | since 2.31 | The annual volume for the part. |
| `LeadTime` | `TimeSpan?` | yes |  | since 2.31 | The lead time for the part. |
| `MinQuantity` | `Decimal` | no |  | since 2.31 | The minimum order quantity (both purchase and manufacturing). |
| `MaxQuantity` | `Decimal` | no |  | since 2.31 | The maximum quantity per order when manufacturing. |
| `ReorderPoint` | `Decimal` | no |  | since 2.31 | The reorder quantity for the part. |
| `PalletQuantity` | `Decimal` | no |  | since 2.31 | The quantity per packet when manufacturing. |
| `AnnualVolumePace` | `Decimal` | no |  | since 2.31 | The annual volume, current pace. |
| `EoqPace` | `Decimal` | no |  | since 2.31 | Order quantity current pace. |
| `LotSizingRule` | `Int32` | no |  | enum, since 2.31 | The lot sizing rule for the part. |
| `LotSizingPeriod` | `TimeSpan` | no |  | since 2.31 | The length of the period when using period requirement as lot sizing rule. |
| `AllowOrderCreationFromCustomerOrder` | `Boolean` | no |  | since 2.31 | Allow to create orders from customer order (manufacturing order for manufactured parts and purchase orders for purchased parts). |
| `SafetyTime` | `TimeSpan` | no |  | since 2.31 | Safety time. |
| `DeductSalesForecast` | `Int32` | no |  | enum, since 2.31 | The type of forecast deduction used. |
| `DeductionMethod` | `Int32` | no |  | enum, since 2.31 | The method of forecast deduction used. |
| `ActiveSupplierPartLinkId` | `Int64?` | yes | [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) | since 2.55 | The business key identifier of the active supplier part link of the part planning information. |
| `ActiveSupplierPartLink` | `SupplierPartLinks` | no | [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) | expandable | The active supplier part link of the part planning information. |
| `DefaultTransferProfileId` | `Int64?` | yes | [TransferProfiles](/entities/Common/TransferProfile.md) | since 22.1 | The business key identifier of the default transfer profile. |
| `PlanningMethod` | `Int32` | no |  | enum, since 22.1 | The planning method of the part planning information. |

## Enumerations

### LotSizingRule

| Name | Value |
| --- | ---: |
| `LotForLot` | 1 |
| `FixedQuantity` | 2 |
| `PeriodRequirement` | 3 |
| `Bucketpart` | 4 |
| `Linked` | 5 |

### DeductSalesForecast

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `LeadTime` | 1 |
| `Now` | 2 |

### DeductionMethod

| Name | Value |
| --- | ---: |
| `Percent` | 0 |
| `TimeOrder` | 1 |
| `Closest` | 2 |
| `ClosestBefore` | 3 |
| `PeriodicIntervals` | 4 |

### PlanningMethod

| Name | Value |
| --- | ---: |
| `Netting` | 0 |
| `StockRefill` | 1 |
| `Physical` | 2 |


## Referenced by

**Inventory**

- [Parts](/entities/Inventory/Part.md) — `PartPlanningInformations` (expand)


## Example

```json
{
  "Id": 0,
  "ContactId": null,
  "WarehouseId": 0,
  "AbcCodeId": null,
  "AcquisitionWarehouseId": null,
  "Eoq": 0.0,
  "RoundingBase": 0.0,
  "SafetyStock": 0.0,
  "AnnualVolume": 0.0,
  "LeadTime": null,
  "MinQuantity": 0.0,
  "MaxQuantity": 0.0,
  "ReorderPoint": 0.0,
  "PalletQuantity": 0.0,
  "AnnualVolumePace": 0.0,
  "EoqPace": 0.0,
  "LotSizingRule": 0,
  "LotSizingPeriod": "00:00:00",
  "AllowOrderCreationFromCustomerOrder": false,
  "SafetyTime": "00:00:00",
  "DeductSalesForecast": 0,
  "DeductionMethod": 0,
  "ActiveSupplierPartLinkId": null,
  "ActiveSupplierPartLink": null,
  "DefaultTransferProfileId": null,
  "PlanningMethod": 0
}
```
