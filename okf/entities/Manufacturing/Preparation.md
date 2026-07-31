---
type: API Entity
title: Preparations
description: Represents a part preparation
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.Preparation.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.Preparation.html
  title: Monitor API — Preparation
module: Manufacturing
api_class: Preparation
doc_name: Preparations
endpoint: GET /api/v1/Manufacturing/Preparations
guid: 7800F6AB-A703-470E-8EFE-41052D1D4108
permission: Show part
introduced_in: '2.18'
property_count: 10
references_out:
- /entities/Common/ExtraFieldTemplate.md
- /entities/Manufacturing/MaterialRow.md
- /entities/Manufacturing/OperationRow.md
referenced_by:
- /entities/Inventory/Part.md
---

# Preparations

Represents a part preparation

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `Preparation`
- **Endpoint:** `GET /api/v1/Manufacturing/Preparations`
- **Required permission:** Show part
- **GUID:** `7800F6AB-A703-470E-8EFE-41052D1D4108`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part preparation. |
| `PartNumber` | `String` | no |  | unique, max length 20 | The part number of the part that the part preparation represents. |
| `Description` | `String` | no |  |  | The translated description of the part preparation. |
| `UseVariantManagement` | `Boolean` | no |  |  | Specifies if variant management is applied for the preparation. |
| `VariantXAxisId` | `Int64?` | yes | [ExtraFieldTemplates](/entities/Common/ExtraFieldTemplate.md) |  | The business key identifier of the extra field template used for the X axis of the variant management system. |
| `VariantXAxis` | `ExtraFieldTemplates` | no | [ExtraFieldTemplates](/entities/Common/ExtraFieldTemplate.md) | expandable | The extra field template that is applied for the X axis of the variant management system. |
| `VariantYAxisId` | `Int64?` | yes | [ExtraFieldTemplates](/entities/Common/ExtraFieldTemplate.md) |  | The business key identifier of the extra field template used for the Y axis of the variant management system. References ExtraFieldTemplates . |
| `VariantYAxis` | `ExtraFieldTemplates` | no | [ExtraFieldTemplates](/entities/Common/ExtraFieldTemplate.md) | expandable | The extra field template that is applied for the Y axis of the variant management system. |
| `Materials` | `MaterialRows[]` | no | [MaterialRows](/entities/Manufacturing/MaterialRow.md) | expandable, collection | The material rows of the preparation. |
| `Operations` | `OperationRows[]` | no | [OperationRows](/entities/Manufacturing/OperationRow.md) | expandable, collection | The operation rows of the preparation. |

## Referenced by

**Inventory**

- [Parts](/entities/Inventory/Part.md) — `PreparationId` (FK)


## Example

```json
{
  "Id": 0,
  "PartNumber": null,
  "Description": null,
  "UseVariantManagement": false,
  "VariantXAxisId": null,
  "VariantXAxis": null,
  "VariantYAxisId": null,
  "VariantYAxis": null,
  "Materials": null,
  "Operations": null
}
```
