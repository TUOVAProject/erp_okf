---
type: API Entity
title: PaymentPlanTemplates
description: Represents a payment plan template.
resource: https://api.monitor.se/api/Monitor.API.Common.PaymentPlanTemplate.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PaymentPlanTemplate.html
  title: Monitor API — PaymentPlanTemplate
module: Common
api_class: PaymentPlanTemplate
doc_name: PaymentPlanTemplates
endpoint: GET /api/v1/Common/PaymentPlanTemplates
guid: 789C920D-3AAC-4D67-BFF5-5FAB1E7765E0
permission: Show invoicing plan
introduced_in: '2.28'
property_count: 7
references_out:
- /entities/Common/PaymentPlanTemplateRow.md
referenced_by:
- /entities/Common/PaymentPlanTemplateRow.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
---

# PaymentPlanTemplates

Represents a payment plan template.

- **Module:** [Common](/modules/Common.md)
- **API class:** `PaymentPlanTemplate`
- **Endpoint:** `GET /api/v1/Common/PaymentPlanTemplates`
- **Required permission:** Show invoicing plan
- **GUID:** `789C920D-3AAC-4D67-BFF5-5FAB1E7765E0`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the payment plan template. |
| `PaymentPlanTemplateType` | `Int32` | no |  | enum | The type of the payment plan template. |
| `Number` | `String` | no |  | unique, max length 5 | The human readable identifier of the payment plan template. |
| `Description` | `String` | no |  |  | The description of the payment plan template. |
| `IsActive` | `Boolean` | no |  |  | The is active of the payment plan template. |
| `InvoiceTextTypes` | `Int32` | no |  | bitmask, enum | The invoice text types of the payment plan template. |
| `PaymentPlanTemplateRows` | `PaymentPlanTemplateRows[]` | no | [PaymentPlanTemplateRows](/entities/Common/PaymentPlanTemplateRow.md) | expandable, collection | A collection of payment plan template rows that belong to the payment plan template. |

## Enumerations

### PaymentPlanTemplateType

| Name | Value |
| --- | ---: |
| `ForSales` | 1 |
| `ForPurchase` | 2 |
| `ForSalesAndPurchase` | 3 |

### InvoiceTextTypes (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `OrderRowText` | 1 |
| `OrderRows` | 2 |
| `ProjectNumberAndName` | 4 |
| `GoodsLabel` | 8 |
| `OrderAdditionalText` | 16 |
| `ConfigurationInfo` | 32 |
| `OrderRowTextInPolishOrderInfo` | 64 |
| `ConfigurationInfoInPolishOrderInfo` | 128 |


## Referenced by

**Common**

- [PaymentPlanTemplateRows](/entities/Common/PaymentPlanTemplateRow.md) — `PaymentPlanTemplateId` (FK)

**Sales**

- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `PaymentPlanTemplate` (expand)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `PaymentPlanTemplateId` (FK)
- [Customers](/entities/Sales/Customer.md) — `PaymentPlanTemplate` (expand)
- [Customers](/entities/Sales/Customer.md) — `PaymentPlanTemplateId` (FK)


## Example

```json
{
  "Id": 0,
  "PaymentPlanTemplateType": 0,
  "Number": null,
  "Description": null,
  "IsActive": false,
  "InvoiceTextTypes": 0,
  "PaymentPlanTemplateRows": null
}
```
