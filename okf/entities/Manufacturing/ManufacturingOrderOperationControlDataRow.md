---
type: API Entity
title: ManufacturingOrderOperationControlDataRows
description: Represents a measuring plan for a manufacturing order operation.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderOperationControlDataRow.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingOrderOperationControlDataRow.html
  title: Monitor API — ManufacturingOrderOperationControlDataRow
module: Manufacturing
api_class: ManufacturingOrderOperationControlDataRow
doc_name: ManufacturingOrderOperationControlDataRows
endpoint: GET /api/v1/Manufacturing/ManufacturingOrderOperationControlDataRows
guid: DEFEEB6C-69C9-40E9-9D05-C817707F855C
permission: Show manufacturing orders
introduced_in: '22.5'
property_count: 8
references_out:
- /entities/Common/FormTemplate.md
- /entities/Common/MeasuringTemplate.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Manufacturing/WorkCenter.md
referenced_by:
- /entities/Manufacturing/ManufacturingOrderOperation.md
---

# ManufacturingOrderOperationControlDataRows

Represents a measuring plan for a manufacturing order operation.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `ManufacturingOrderOperationControlDataRow`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderOperationControlDataRows`
- **Required permission:** Show manufacturing orders
- **GUID:** `DEFEEB6C-69C9-40E9-9D05-C817707F855C`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `ManufacturingOrderOperationId` | `Int64` | no | [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) |  | The business key identifier of the manufacturing order operation that the row relates to. |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](/entities/Common/MeasuringTemplate.md) |  | The business key identifier of the measuring template that the row relates to. |
| `OverridenFormTemplateId` | `Int64` | no | [FormTemplates](/entities/Common/FormTemplate.md) |  | The business key identifier of the form template specified for this row. |
| `OverridenFrequencyText` | `String` | no |  | max length 80 | The frequency text specified for this row. |
| `OverridenIntervalAmount` | `Int32?` | yes |  |  | The quantity value specified for this row. |
| `OverridenInterval` | `Int32?` | yes |  |  | The interval value specified for this row. |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](/entities/Manufacturing/WorkCenter.md) |  | The business key identifier of the work center that the row relates to. |

## Referenced by

**Manufacturing**

- [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) — `ControlDataRows` (expand)


## Example

```json
{
  "Id": 0,
  "ManufacturingOrderOperationId": 0,
  "MeasuringTemplateId": 0,
  "OverridenFormTemplateId": 0,
  "OverridenFrequencyText": null,
  "OverridenIntervalAmount": null,
  "OverridenInterval": null,
  "WorkCenterId": null
}
```
