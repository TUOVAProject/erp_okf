---
type: API Entity
title: PartPurchaseControlDataRows
description: Represents a purchase measuring plan for a part.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartPurchaseControlDataRow.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartPurchaseControlDataRow.html
  title: Monitor API — PartPurchaseControlDataRow
module: Inventory
api_class: PartPurchaseControlDataRow
doc_name: PartPurchaseControlDataRows
endpoint: GET /api/v1/Inventory/PartPurchaseControlDataRows
guid: 94DEB3C6-197F-4848-88FA-E1B0A5EA1DC1
permission: Show part
introduced_in: '26.6'
property_count: 8
references_out:
- /entities/Common/FormTemplate.md
- /entities/Common/MeasuringTemplate.md
- /entities/Inventory/Part.md
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Inventory/Part.md
---

# PartPurchaseControlDataRows

Represents a purchase measuring plan for a part.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PartPurchaseControlDataRow`
- **Endpoint:** `GET /api/v1/Inventory/PartPurchaseControlDataRows`
- **Required permission:** Show part
- **GUID:** `94DEB3C6-197F-4848-88FA-E1B0A5EA1DC1`
- **Introduced in:** 26.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `PartId` | `Int64` | no | [Parts](Part.md) |  | The business key identifier of the part that the row relates to. |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](../Common/MeasuringTemplate.md) |  | The business key identifier of the measuring template that the row relates to. |
| `OverriddenFormTemplateId` | `Int64?` | yes | [FormTemplates](../Common/FormTemplate.md) |  | The business key identifier of the form template specified for this row. |
| `OverriddenFrequencyText` | `String` | no |  | max length 80 | The frequency text specified for this row. |
| `OverriddenIntervalAmount` | `Int32?` | yes |  |  | The quantity value specified for this row. |
| `OverriddenInterval` | `Int32?` | yes |  |  | The interval value specified for this row. |
| `SupplierId` | `Int64?` | yes | [Suppliers](../Purchase/Supplier.md) |  | The business key identifier of the supplier that the row relates to. |

## Referenced by

**Inventory**

- [Parts](Part.md) — `ControlDataRows` (expand)


## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "MeasuringTemplateId": 0,
  "OverriddenFormTemplateId": null,
  "OverriddenFrequencyText": null,
  "OverriddenIntervalAmount": null,
  "OverriddenInterval": null,
  "SupplierId": null
}
```
