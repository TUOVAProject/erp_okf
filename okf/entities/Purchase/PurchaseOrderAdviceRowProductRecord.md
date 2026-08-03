---
type: API Entity
title: PurchaseOrderAdviceRowProductRecords
description: Represents a purchase order advice row product record.
resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderAdviceRowProductRecord.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.PurchaseOrderAdviceRowProductRecord.html
  title: Monitor API — PurchaseOrderAdviceRowProductRecord
module: Purchase
api_class: PurchaseOrderAdviceRowProductRecord
doc_name: PurchaseOrderAdviceRowProductRecords
endpoint: GET /api/v1/Purchase/PurchaseOrderAdviceRowProductRecords
guid: 6CBD9EF6-2FD4-44D4-B1D2-8568A451CFC8
permission: Show arrival
introduced_in: '22.2'
property_count: 10
references_out:
- /entities/Purchase/PurchaseOrderAdviceRow.md
---

# PurchaseOrderAdviceRowProductRecords

Represents a purchase order advice row product record.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `PurchaseOrderAdviceRowProductRecord`
- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderAdviceRowProductRecords`
- **Required permission:** Show arrival
- **GUID:** `6CBD9EF6-2FD4-44D4-B1D2-8568A451CFC8`
- **Introduced in:** 22.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the purchase order advice row product record. |
| `ParentId` | `Int64?` | yes | [PurchaseOrderAdviceRows](PurchaseOrderAdviceRow.md) |  | The business key identifier of the purchase order advice row that this product record belongs to. |
| `TraceabilityMode` | `Int32` | no |  | enum | The traceability mode for the product record. |
| `BatchNumber` | `String` | no |  | max length 60 | The batch number for the product record. |
| `BatchQuantity` | `Decimal` | no |  |  | The batch quantity for the product record. |
| `BatchBestBeforeDate` | `DateTimeOffset?` | yes |  |  | The batch best before date for the product record. |
| `SerialNumberPrefix` | `String` | no |  | max length 5 | The serial number prefix for the product records. |
| `SerialNumberStart` | `String` | no |  | max length 60 | The serial number start for the product records. |
| `SerialNumberCount` | `Int32` | no |  |  | Number of product records with serial number to create. |
| `ChargeNumber` | `String` | no |  | max length 30 | The charge number of the product record(s). |

## Enumerations

### TraceabilityMode

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Batch` | 1 |
| `Individual` | 2 |
| `IndividualOnlyWithdrawal` | 4 |


## Example

```json
{
  "Id": 0,
  "ParentId": null,
  "TraceabilityMode": 0,
  "BatchNumber": null,
  "BatchQuantity": 0.0,
  "BatchBestBeforeDate": null,
  "SerialNumberPrefix": null,
  "SerialNumberStart": null,
  "SerialNumberCount": 0,
  "ChargeNumber": null
}
```
