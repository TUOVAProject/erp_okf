---
type: API Entity
title: FormTemplates
description: Represents a measuring or maintenance form template.
resource: https://api.monitor.se/api/Monitor.API.Common.FormTemplate.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.FormTemplate.html
  title: Monitor API — FormTemplate
module: Common
api_class: FormTemplate
doc_name: FormTemplates
endpoint: GET /api/v1/Common/FormTemplates
guid: A11F4598-EC23-4BE4-88C5-E4E9899678F7
introduced_in: '22.5'
property_count: 7
references_out:
- /entities/Common/Comment.md
referenced_by:
- /entities/Common/FormTemplateSelectionRow.md
- /entities/Common/MeasuringTemplate.md
- /entities/Inventory/PartPurchaseControlDataRow.md
- /entities/Manufacturing/ManufacturingOrderOperationControlDataRow.md
- /entities/Manufacturing/OperationRowControlDataRow.md
---

# FormTemplates

Represents a measuring or maintenance form template.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `FormTemplate`
- **Endpoint:** `GET /api/v1/Common/FormTemplates`
- **GUID:** `A11F4598-EC23-4BE4-88C5-E4E9899678F7`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the entity. |
| `Code` | `String` | no |  | unique, max length 40 | The human readable identifier of the form template. |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The comment of the form template. |
| `CommentId` | `Int64?` | yes | [Comments](Comment.md) |  | The business key identifier of the form template's comment. |
| `Description` | `String` | no |  |  | The translated description of the form template. |
| `ControlDataType` | `Int32` | no |  | enum | The type of the template form which specifices in which apps the form can be used. |
| `Type` | `Int32` | no |  | bitmask, enum | The usage type of the measuring template form that restricts in which module the measuring form template can be used. |

## Enumerations

### ControlDataType

| Name | Value |
| --- | ---: |
| `Maintenance` | 0 |
| `MeasuringData` | 1 |

### Type (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Manufacturing` | 1 |
| `Purchase` | 2 |


## Referenced by

**Common**

- [FormTemplateSelectionRows](FormTemplateSelectionRow.md) — `FormTemplateId` (FK)
- [MeasuringTemplates](MeasuringTemplate.md) — `FormTemplateId` (FK)

**Inventory**

- [PartPurchaseControlDataRows](../Inventory/PartPurchaseControlDataRow.md) — `OverriddenFormTemplateId` (FK)

**Manufacturing**

- [ManufacturingOrderOperationControlDataRows](../Manufacturing/ManufacturingOrderOperationControlDataRow.md) — `OverridenFormTemplateId` (FK)
- [OperationRowControlDataRows](../Manufacturing/OperationRowControlDataRow.md) — `OverriddenFormTemplateId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Comment": null,
  "CommentId": null,
  "Description": null,
  "ControlDataType": 0,
  "Type": 0
}
```
