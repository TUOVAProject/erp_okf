---
type: API Entity
title: StockBalanceChanges
description: Represents a stock balance change.
resource: https://api.monitor.se/api/Monitor.API.Inventory.StockBalanceChange.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.StockBalanceChange.html
  title: Monitor API — StockBalanceChange
module: Inventory
api_class: StockBalanceChange
doc_name: StockBalanceChanges
endpoint: GET /api/v1/Inventory/StockBalanceChanges
guid: 32319F75-BB6D-43E4-AD08-C7601B24A29A
permission: Show part
introduced_in: '2.48'
property_count: 6
references_out:
- /entities/Inventory/PartLocation.md
- /entities/Inventory/ProductRecord.md
- /entities/Inventory/QuantityChange.md
referenced_by:
- /entities/Inventory/QuantityChange.md
---

# StockBalanceChanges

Represents a stock balance change.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `StockBalanceChange`
- **Endpoint:** `GET /api/v1/Inventory/StockBalanceChanges`
- **Required permission:** Show part
- **GUID:** `32319F75-BB6D-43E4-AD08-C7601B24A29A`
- **Introduced in:** 2.48

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the stock balance change. |
| `PartLocationId` | `Int64?` | yes | [PartLocations](PartLocation.md) |  | The part location that the balance change effects. |
| `BalanceChange` | `Decimal` | no |  |  | The balance change for this part location. |
| `AvailableBalance` | `Decimal` | no |  |  | The available balance for the part location before the balance change was performed. NOTE: This only produces a value for arrival reporting and manufacturing reportings. This property is not suitable for looking at the historical balance of a part location. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](ProductRecord.md) |  | The product record that is used for this balance change. |
| `QuantityChangeId` | `Int64` | no | [QuantityChanges](QuantityChange.md) |  | The parent quantity change of the stock balance change. |

## Referenced by

**Inventory**

- [QuantityChanges](QuantityChange.md) — `StockBalanceChanges` (expand)


## Example

```json
{
  "Id": 0,
  "PartLocationId": null,
  "BalanceChange": 0.0,
  "AvailableBalance": 0.0,
  "ProductRecordId": null,
  "QuantityChangeId": 0
}
```
