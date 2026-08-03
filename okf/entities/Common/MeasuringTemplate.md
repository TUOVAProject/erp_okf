---
type: API Entity
title: MeasuringTemplates
description: Represents a measuring template.
resource: https://api.monitor.se/api/Monitor.API.Common.MeasuringTemplate.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.MeasuringTemplate.html
  title: Monitor API — MeasuringTemplate
module: Common
api_class: MeasuringTemplate
doc_name: MeasuringTemplates
endpoint: GET /api/v1/Common/MeasuringTemplates
guid: EFE8C4CC-35D2-4D05-B257-52FCEEF604A1
permission: Show measuring templates
introduced_in: '22.5'
property_count: 9
references_out:
- /entities/Common/FormTemplate.md
referenced_by:
- /entities/Inventory/PartPurchaseControlDataRow.md
- /entities/Manufacturing/ManufacturingOrderOperationControlDataRow.md
- /entities/Manufacturing/OperationRowControlDataRow.md
---

# MeasuringTemplates

Represents a measuring template.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `MeasuringTemplate`
- **Endpoint:** `GET /api/v1/Common/MeasuringTemplates`
- **Required permission:** Show measuring templates
- **GUID:** `EFE8C4CC-35D2-4D05-B257-52FCEEF604A1`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `FormTemplateId` | `Int64` | no | [FormTemplates](FormTemplate.md) |  | The business key identifier of the form template that the measuring template relates to. |
| `Code` | `String` | no |  | unique, max length 40 | The human readable identifier of the measuring template. |
| `Description` | `String` | no |  |  | The translated description of the measuring template. |
| `FrequencyText` | `String` | no |  | max length 80 | The frequency text defined for the measuring template. |
| `IntervalAmount` | `Int32?` | yes |  |  | The quantity value defined for the measuring template. |
| `Interval` | `Int32?` | yes |  |  | The interval value defined for the measuring template. |
| `MeasuringFrequency` | `Int32` | no |  | enum | The frequency value defined for the measuring template. |
| `Type` | `Int32` | no |  | bitmask, enum | Type of the measuring template which restricts in which module the measuring template can be used. |

## Enumerations

### MeasuringFrequency

| Name | Value |
| --- | ---: |
| `First` | 0 |
| `Last` | 1 |
| `All` | 2 |
| `Sample` | 3 |
| `Other` | 4 |
| `PerOrder` | 5 |

### Type (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Manufacturing` | 1 |
| `Purchase` | 2 |


## Referenced by

**Inventory**

- [PartPurchaseControlDataRows](../Inventory/PartPurchaseControlDataRow.md) — `MeasuringTemplateId` (FK)

**Manufacturing**

- [ManufacturingOrderOperationControlDataRows](../Manufacturing/ManufacturingOrderOperationControlDataRow.md) — `MeasuringTemplateId` (FK)
- [OperationRowControlDataRows](../Manufacturing/OperationRowControlDataRow.md) — `MeasuringTemplateId` (FK)


## Example

```json
{
  "Id": 0,
  "FormTemplateId": 0,
  "Code": null,
  "Description": null,
  "FrequencyText": null,
  "IntervalAmount": null,
  "Interval": null,
  "MeasuringFrequency": 0,
  "Type": 0
}
```
