---
type: API Entity
title: PaymentPlanTemplateRows
description: Represents a payment plan template row.
resource: https://api.monitor.se/api/Monitor.API.Common.PaymentPlanTemplateRow.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PaymentPlanTemplateRow.html
  title: Monitor API — PaymentPlanTemplateRow
module: Common
api_class: PaymentPlanTemplateRow
doc_name: PaymentPlanTemplateRows
endpoint: GET /api/v1/Common/PaymentPlanTemplateRows
guid: 2217102F-3B6A-4183-BDE1-3188492C214A
permission: Show invoicing plan
introduced_in: '2.28'
property_count: 11
references_out:
- /entities/Common/PaymentPlanTemplate.md
- /entities/Common/PaymentTerm.md
- /entities/Inventory/Part.md
referenced_by:
- /entities/Common/PaymentPlanTemplate.md
---

# PaymentPlanTemplateRows

Represents a payment plan template row.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `PaymentPlanTemplateRow`
- **Endpoint:** `GET /api/v1/Common/PaymentPlanTemplateRows`
- **Required permission:** Show invoicing plan
- **GUID:** `2217102F-3B6A-4183-BDE1-3188492C214A`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the payment plan template row. |
| `UnpaidAdvanceWarningType` | `Int32?` | yes |  | enum | The unpaid advance warning type of the payment plan template row. |
| `PaymentPlanTemplateId` | `Int64` | no | [PaymentPlanTemplates](PaymentPlanTemplate.md) |  | The business key identifier of the payment plan template of the payment plan template row. |
| `PartialInvoiceType` | `Int32` | no |  | enum | The partial invoice type of the payment plan template row. |
| `PartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the part of the payment plan template row. |
| `Part` | `Parts` | no | [Parts](../Inventory/Part.md) | expandable | The part of the payment plan template row. |
| `OverrideDescription` | `String` | no |  | max length 80 | The override description of the payment plan template row. |
| `FractionOfTotal` | `Decimal` | no |  |  | The fraction of total of the payment plan template row. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](PaymentTerm.md) |  | The business key identifier of the payment term of the payment plan template row. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](PaymentTerm.md) | expandable | The payment term of the payment plan template row. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the payment plan template row. |

## Enumerations

### UnpaidAdvanceWarningType

| Name | Value |
| --- | ---: |
| `NoAlert` | 0 |
| `Warning` | 1 |
| `PreventDelivery` | 2 |

### PartialInvoiceType

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `InAdvance` | 1 |
| `Delivery` | 2 |
| `InArrears` | 3 |
| `Text` | 4 |


## Referenced by

**Common**

- [PaymentPlanTemplates](PaymentPlanTemplate.md) — `PaymentPlanTemplateRows` (expand)


## Example

```json
{
  "Id": 0,
  "UnpaidAdvanceWarningType": null,
  "PaymentPlanTemplateId": 0,
  "PartialInvoiceType": 0,
  "PartId": null,
  "Part": null,
  "OverrideDescription": null,
  "FractionOfTotal": 0.0,
  "PaymentTermId": null,
  "PaymentTerm": null,
  "RowIndex": null
}
```
