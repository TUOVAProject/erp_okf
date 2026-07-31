---
type: API Entity
title: OperationRowControlDataRows
description: Represents a measuring plan for an operation row.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.OperationRowControlDataRow.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.OperationRowControlDataRow.html
  title: Monitor API — OperationRowControlDataRow
module: Manufacturing
api_class: OperationRowControlDataRow
doc_name: OperationRowControlDataRows
endpoint: GET /api/v1/Manufacturing/OperationRowControlDataRows
guid: C92286E5-7C4A-4669-B5DF-2226D6E6EECB
permission: Show manufacturing orders
introduced_in: '22.5'
property_count: 8
references_out:
- /entities/Common/FormTemplate.md
- /entities/Common/MeasuringTemplate.md
- /entities/Manufacturing/OperationRow.md
- /entities/Manufacturing/WorkCenter.md
referenced_by:
- /entities/Manufacturing/OperationRow.md
---

# OperationRowControlDataRows

Represents a measuring plan for an operation row.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `OperationRowControlDataRow`
- **Endpoint:** `GET /api/v1/Manufacturing/OperationRowControlDataRows`
- **Required permission:** Show manufacturing orders
- **GUID:** `C92286E5-7C4A-4669-B5DF-2226D6E6EECB`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `OperationRowId` | `Int64` | no | [OperationRows](/entities/Manufacturing/OperationRow.md) |  | The business key identifier of the operation row that the row relates to. |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](/entities/Common/MeasuringTemplate.md) |  | The business key identifier of the measuring template that the row relates to. |
| `OverriddenFormTemplateId` | `Int64?` | yes | [FormTemplates](/entities/Common/FormTemplate.md) |  | The business key identifier of the form template specified for this row. |
| `OverriddenFrequencyText` | `String` | no |  | max length 80 | The frequency text specified for this row. |
| `OverriddenIntervalAmount` | `Int32?` | yes |  |  | The quantity value specified for this row. |
| `OverriddenInterval` | `Int32?` | yes |  |  | The interval value specified for this row. |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](/entities/Manufacturing/WorkCenter.md) |  | The business key identifier of the work center that the row relates to. |

## Referenced by

**Manufacturing**

- [OperationRows](/entities/Manufacturing/OperationRow.md) — `ControlDataRows` (expand)


## Example

```json
{
  "Id": 0,
  "OperationRowId": 0,
  "MeasuringTemplateId": 0,
  "OverriddenFormTemplateId": null,
  "OverriddenFrequencyText": null,
  "OverriddenIntervalAmount": null,
  "OverriddenInterval": null,
  "WorkCenterId": null
}
```
