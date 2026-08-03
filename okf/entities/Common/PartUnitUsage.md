---
type: API Entity
title: PartUnitUsages
description: Represents a part unit usage.
resource: https://api.monitor.se/api/Monitor.API.Common.PartUnitUsage.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PartUnitUsage.html
  title: Monitor API — PartUnitUsage
module: Common
api_class: PartUnitUsage
doc_name: PartUnitUsages
endpoint: GET /api/v1/Common/PartUnitUsages
guid: AECC59A8-B997-42A5-8777-A20858A1D36D
permission: Show part
introduced_in: '2.18'
property_count: 6
references_out:
- /entities/Common/Unit.md
- /entities/Inventory/Part.md
referenced_by:
- /entities/Inventory/Part.md
---

# PartUnitUsages

Represents a part unit usage.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `PartUnitUsage`
- **Endpoint:** `GET /api/v1/Common/PartUnitUsages`
- **Required permission:** Show part
- **GUID:** `AECC59A8-B997-42A5-8777-A20858A1D36D`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part unit usage. |
| `UnitId` | `Int64` | no | [Units](Unit.md) |  | The unit of the part unit usage. References Units . |
| `IsRemoved` | `Boolean` | no |  |  | Specifies if the part unit usage has been removed. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor between the default part unit usage and this part unit usage. |
| `UsageType` | `Int32` | no |  | bitmask, enum | The usage type of the part unit usage. |
| `PartId` | `Int64` | no | [Part](../Inventory/Part.md) |  | The business key identifier of the part that the part unit usage belongs to. References . |

## Enumerations

### UsageType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `ManufacturingMaterialWithdrawal` | 1 |
| `PurchaseOrder` | 2 |
| `ArrivalReporting` | 4 |
| `CustomerOrder` | 8 |
| `DeliveryReporting` | 16 |
| `PhysicalInventoryAndStockReporting` | 32 |
| `StatisticalUnit` | 64 |
| `PackForDelivery` | 128 |


## Referenced by

**Inventory**

- [Parts](../Inventory/Part.md) — `PartUnitUsages` (expand)
- [Parts](../Inventory/Part.md) — `StandardPartUnitUsage` (expand)
- [Parts](../Inventory/Part.md) — `StandardPartUnitUsageId` (FK)


## Example

```json
{
  "Id": 0,
  "UnitId": 0,
  "IsRemoved": false,
  "ConversionFactor": 0.0,
  "UsageType": 0,
  "PartId": 0
}
```
