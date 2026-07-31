---
type: API Entity
title: MaintenanceReportings
description: Represents a maintenance reporting.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.MaintenanceReporting.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.MaintenanceReporting.html
  title: Monitor API — MaintenanceReporting
module: Manufacturing
api_class: MaintenanceReporting
doc_name: MaintenanceReportings
endpoint: GET /api/v1/Manufacturing/MaintenanceReportings
guid: E557EAFE-1137-42B7-A3A4-A610D9066703
permission: Show maintenance plan
introduced_in: '24.6'
property_count: 21
references_out:
- /entities/Common/Comment.md
- /entities/Common/Person.md
- /entities/Inventory/ProductRecord.md
- /entities/Manufacturing/MaintenanceReportingSelectionRow.md
- /entities/Manufacturing/ManufacturingOrder.md
referenced_by:
- /entities/Manufacturing/MaintenanceReportingSelectionRow.md
---

# MaintenanceReportings

Represents a maintenance reporting.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `MaintenanceReporting`
- **Endpoint:** `GET /api/v1/Manufacturing/MaintenanceReportings`
- **Required permission:** Show maintenance plan
- **GUID:** `E557EAFE-1137-42B7-A3A4-A610D9066703`
- **Introduced in:** 24.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the maintenance reporting. |
| `SerialNumber` | `String` | no |  | unique | The serial number of the maintenance reporting. |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) |  | The business key identifier of the manufacturing order. |
| `ManufacturingOrder` | `ManufacturingOrders` | no | [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) | expandable | The maintenance reporting manufacturing order. |
| `ProductRecordId` | `Int64` | no |  |  | The business key identifier of product record. |
| `ProductRecord` | `ProductRecords` | no | [ProductRecords](/entities/Inventory/ProductRecord.md) | expandable | The product record of the maintenance reporting. |
| `MaintenanceRowId` | `Int64` | no |  |  | The business key identifier of the maintenance row. |
| `ShortComment` | `String` | no |  |  | The short comment of the maintenance reporting. |
| `CommentId` | `Int64` | no | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment of the maintenance reporting. |
| `MaintenanceStatus` | `Int32?` | yes |  | enum | The maintenance status of the maintenance reporting. |
| `ReportedById` | `Int64` | no | [Persons](/entities/Common/Person.md) |  | The business key identifier of person that reported on the maintenance reporting. |
| `ReportedBy` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable | The person that reported in the maintenance reporting. |
| `ReportingStatus` | `Int32` | no |  | enum | The reporting status of the maintenance reporting. |
| `ActualDate` | `DateTimeOffset?` | yes |  |  | The actual date of the maintenance reporting. |
| `Status` | `Int32` | no |  | enum | The serial number status of the maintenance reporting. |
| `NextOccurrence` | `DateTimeOffset?` | yes |  |  | The next occurrence of the maintenance reporting. |
| `ColorCode` | `Int32?` | yes |  |  | The color code of the maintenance reporting. |
| `InstructionId` | `Int64` | no |  |  | The business key identifier of the instruction. |
| `Instruction` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The instruction of the maintenance reporting. |
| `MaintenanceReportingSelectionRows` | `MaintenanceReportingSelectionRows[]` | no | [MaintenanceReportingSelectionRows](/entities/Manufacturing/MaintenanceReportingSelectionRow.md) | expandable, collection, since 25.7 | The maintenance reporting selection rows. |

## Enumerations

### MaintenanceStatus

| Name | Value |
| --- | ---: |
| `Ok` | 0 |
| `NotOk` | 1 |
| `OkWithAction` | 2 |

### ReportingStatus

| Name | Value |
| --- | ---: |
| `New` | 0 |
| `InProgress` | 1 |
| `Finished` | 2 |

### Status

| Name | Value |
| --- | ---: |
| `ApprovalForUse` | 0 |
| `NonApproval` | 1 |
| `ServicePastDue` | 2 |
| `UnderServiceOrCalibration` | 3 |
| `Rejected` | 4 |
| `ServiceOrCalibrationBeforeUse` | 5 |
| `Missing` | 6 |
| `Scrapped` | 7 |


## Referenced by

**Manufacturing**

- [MaintenanceReportingSelectionRows](/entities/Manufacturing/MaintenanceReportingSelectionRow.md) — `MaintenanceReportingId` (FK)


## Example

```json
{
  "Id": 0,
  "SerialNumber": null,
  "ManufacturingOrderId": 0,
  "ManufacturingOrder": null,
  "ProductRecordId": 0,
  "ProductRecord": null,
  "MaintenanceRowId": 0,
  "ShortComment": null,
  "CommentId": 0,
  "Comment": null,
  "MaintenanceStatus": null,
  "ReportedById": 0,
  "ReportedBy": null,
  "ReportingStatus": 0,
  "ActualDate": null,
  "Status": 0,
  "NextOccurrence": null,
  "ColorCode": null,
  "InstructionId": 0,
  "Instruction": null,
  "MaintenanceReportingSelectionRows": null
}
```
