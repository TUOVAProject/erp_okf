---
type: API Entity
title: ProductRecordOperationReportings
description: Represents a product record operation reporting.
resource: https://api.monitor.se/api/Monitor.API.Inventory.ProductRecordOperationReporting.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.ProductRecordOperationReporting.html
  title: Monitor API — ProductRecordOperationReporting
module: Inventory
api_class: ProductRecordOperationReporting
doc_name: ProductRecordOperationReportings
endpoint: GET /api/v1/Inventory/ProductRecordOperationReportings
guid: 4f6460a6-2d27-47b4-87a7-8c424f92ba08
permission: Show serial number
introduced_in: '2.49'
property_count: 14
references_out:
- /entities/Inventory/ProductRecord.md
referenced_by:
- /entities/Inventory/ProductRecord.md
---

# ProductRecordOperationReportings

Represents a product record operation reporting.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `ProductRecordOperationReporting`
- **Endpoint:** `GET /api/v1/Inventory/ProductRecordOperationReportings`
- **Required permission:** Show serial number
- **GUID:** `4f6460a6-2d27-47b4-87a7-8c424f92ba08`
- **Introduced in:** 2.49

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the product record operation reporting. |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  |  | The time when the product record operation reporting was reported. |
| `ReportingType` | `Int32` | no |  | enum | The type that the product record operation reporting is. |
| `ProductRecordId` | `Int64` | no | [ProductRecords](/entities/Inventory/ProductRecord.md) |  | The business key identifier of the product record that the product record operation reporting applies. |
| `OperationReportingId` | `Int64?` | yes |  |  | The business key identifier of the manufacturing order operation reporting that the product record operation reporting applies. |
| `OrderNumber` | `String` | no |  |  | The product record operation reportings order number. |
| `ReportedTime` | `TimeSpan?` | yes |  |  | The product record operation reportings reported time. |
| `ReportedQuantity` | `Decimal?` | yes |  |  | The product record operation reportings reported quantity. |
| `QuantityPerCycle` | `Decimal?` | yes |  |  | The product record operation reportings quantity per cycle. |
| `CycleTime` | `TimeSpan?` | yes |  |  | The product record operation reportings cycle time. |
| `TotalTime` | `TimeSpan?` | yes |  |  | The product record operation reportings total time. |
| `TotalCycles` | `Decimal` | no |  |  | The product record operation reportings total cycle. |
| `TotalMeasurementSetting` | `Decimal` | no |  |  | The product record operation reportings total seasurement setting. |
| `ReportedMeasurementSetting` | `Decimal?` | yes |  |  | The product record operation reportings reported measurement setting. |

## Enumerations

### ReportingType

| Name | Value |
| --- | ---: |
| `OperationReporting` | 0 |
| `Inventory` | 1 |
| `Rejection` | 2 |


## Referenced by

**Inventory**

- [ProductRecords](/entities/Inventory/ProductRecord.md) — `OperationReportings` (expand)


## Example

```json
{
  "Id": 0,
  "LoggingTimeStamp": "0001-01-01T00:00:00+00:00",
  "ReportingType": 0,
  "ProductRecordId": 0,
  "OperationReportingId": null,
  "OrderNumber": null,
  "ReportedTime": null,
  "ReportedQuantity": null,
  "QuantityPerCycle": null,
  "CycleTime": null,
  "TotalTime": null,
  "TotalCycles": 0.0,
  "TotalMeasurementSetting": 0.0,
  "ReportedMeasurementSetting": null
}
```
