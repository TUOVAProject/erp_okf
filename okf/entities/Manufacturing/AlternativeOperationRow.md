---
type: API Entity
title: AlternativeOperationRows
description: Represents an alternative work center on an operation row.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.AlternativeOperationRow.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.AlternativeOperationRow.html
  title: Monitor API — AlternativeOperationRow
module: Manufacturing
api_class: AlternativeOperationRow
doc_name: AlternativeOperationRows
endpoint: GET /api/v1/Manufacturing/AlternativeOperationRows
guid: E3E25806-EF54-43CA-9B22-C1417D0CED80
permission: Show part
introduced_in: '26.5'
property_count: 9
references_out:
- /entities/Manufacturing/OperationRow.md
- /entities/Manufacturing/WorkCenter.md
referenced_by:
- /entities/Manufacturing/OperationRow.md
---

# AlternativeOperationRows

Represents an alternative work center on an operation row.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `AlternativeOperationRow`
- **Endpoint:** `GET /api/v1/Manufacturing/AlternativeOperationRows`
- **Required permission:** Show part
- **GUID:** `E3E25806-EF54-43CA-9B22-C1417D0CED80`
- **Introduced in:** 26.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the alternative operation row. |
| `OperationRowId` | `Int64` | no | [OperationRows](/entities/Manufacturing/OperationRow.md) |  | The business key identifier of the operation row that owns this alternative. |
| `WorkCenterId` | `Int64` | no | [WorkCenters](/entities/Manufacturing/WorkCenter.md) |  | The business key identifier of the alternative work center. |
| `UnitStaffingFactor` | `Decimal?` | yes |  |  | The unit staffing factor of the alternative operation row. |
| `SetupStaffingFactor` | `Decimal?` | yes |  |  | The setup staffing factor of the alternative operation row. |
| `QueueTime` | `TimeSpan?` | yes |  |  | The queue time of the alternative operation row. |
| `SetupTime` | `TimeSpan?` | yes |  |  | The setup time of the alternative operation row. |
| `UnitTime` | `TimeSpan?` | yes |  |  | The unit time of the alternative operation row. |
| `CycleTime` | `TimeSpan?` | yes |  |  | The cycle time of the alternative operation row. |

## Referenced by

**Manufacturing**

- [OperationRows](/entities/Manufacturing/OperationRow.md) — `AlternativeOperationRows` (expand)


## Example

```json
{
  "Id": 0,
  "OperationRowId": 0,
  "WorkCenterId": 0,
  "UnitStaffingFactor": null,
  "SetupStaffingFactor": null,
  "QueueTime": null,
  "SetupTime": null,
  "UnitTime": null,
  "CycleTime": null
}
```
