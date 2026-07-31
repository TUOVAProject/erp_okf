---
type: API Entity
title: FixedAssetDepreciations
description: Represents a depreciation for a fixed assets object.
resource: https://api.monitor.se/api/Monitor.API.Accounting.FixedAssetDepreciation.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.FixedAssetDepreciation.html
  title: Monitor API — FixedAssetDepreciation
module: Accounting
api_class: FixedAssetDepreciation
doc_name: FixedAssetDepreciations
endpoint: GET /api/v1/Accounting/FixedAssetDepreciations
guid: 0e97d1b6-421e-47ba-937a-f33db0f55dfb
permission: Show depreciation
introduced_in: '23.5'
property_count: 6
references_out:
- /entities/Accounting/FixedAsset.md
---

# FixedAssetDepreciations

Represents a depreciation for a fixed assets object.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `FixedAssetDepreciation`
- **Endpoint:** `GET /api/v1/Accounting/FixedAssetDepreciations`
- **Required permission:** Show depreciation
- **GUID:** `0e97d1b6-421e-47ba-937a-f33db0f55dfb`
- **Introduced in:** 23.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the depreciation. |
| `Amount` | `Decimal` | no |  |  | The amount of the depreciation. |
| `DepreciationDate` | `DateTimeOffset` | no |  |  | The depreciation date of the depreciation. |
| `VoucherDate` | `DateTimeOffset` | no |  |  | The voucher date of the depreciation. |
| `VoucherText` | `String` | no |  | max length 100 | The voucher date of the depreciation. |
| `ParentId` | `Int64` | no | [FixedAssets](/entities/Accounting/FixedAsset.md) |  | The fixed assets object to which the depreciation belongs. |

## Example

```json
{
  "Id": 0,
  "Amount": 0.0,
  "DepreciationDate": "0001-01-01T00:00:00+00:00",
  "VoucherDate": "0001-01-01T00:00:00+00:00",
  "VoucherText": null,
  "ParentId": 0
}
```
