---
type: API Entity
title: VoucherSeries
description: Represents a voucher series.
resource: https://api.monitor.se/api/Monitor.API.Accounting.VoucherSeries.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.VoucherSeries.html
  title: Monitor API — VoucherSeries
module: Accounting
api_class: VoucherSeries
doc_name: VoucherSeries
endpoint: GET /api/v1/Accounting/VoucherSeries
guid: CE1349A1-F0AB-4267-AE39-C6CD5CF61FA6
permission: Show voucher
introduced_in: '2.30'
property_count: 3
referenced_by:
- /entities/Accounting/Voucher.md
- /entities/Common/ApplicationUser.md
---

# VoucherSeries

Represents a voucher series.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `VoucherSeries`
- **Endpoint:** `GET /api/v1/Accounting/VoucherSeries`
- **Required permission:** Show voucher
- **GUID:** `CE1349A1-F0AB-4267-AE39-C6CD5CF61FA6`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the voucher series. |
| `Series` | `String` | no |  | max length 2 | The identifying code of the voucher series. |
| `IsActive` | `Boolean` | no |  |  | Defines if the voucher series is active. |

## Referenced by

**Accounting**

- [Vouchers](Voucher.md) — `SeriesId` (FK)

**Common**

- [ApplicationUsers](../Common/ApplicationUser.md) — `DefaultVoucherSeriesId` (FK)


## Example

```json
{
  "Id": 0,
  "Series": null,
  "IsActive": false
}
```
