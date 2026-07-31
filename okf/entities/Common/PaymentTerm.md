---
type: API Entity
title: PaymentTerms
description: Represents a queryable payment term.
resource: https://api.monitor.se/api/Monitor.API.Common.PaymentTerm.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PaymentTerm.html
  title: Monitor API — PaymentTerm
module: Common
api_class: PaymentTerm
doc_name: PaymentTerms
endpoint: GET /api/v1/Common/PaymentTerms
guid: 9ebf4a69-e304-4c4a-94bc-2cd2e8bd3209
permission: Show terms
introduced_in: '2.18'
property_count: 12
references_out:
- /entities/Common/PaymentMethod.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/AccountsReceivable.md
- /entities/Common/PaymentPlanTemplateRow.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderInvoice.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/CustomerOrderPaymentPlanRow.md
- /entities/Sales/CustomerOrderType.md
- /entities/Sales/Quote.md
- /entities/Sales/SalesAgreement.md
---

# PaymentTerms

Represents a queryable payment term.

- **Module:** [Common](/modules/Common.md)
- **API class:** `PaymentTerm`
- **Endpoint:** `GET /api/v1/Common/PaymentTerms`
- **Required permission:** Show terms
- **GUID:** `9ebf4a69-e304-4c4a-94bc-2cd2e8bd3209`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the payment term. |
| `Number` | `Int64` | no |  |  | The payment term number. |
| `Description` | `String` | no |  |  | The translated description of the payment term. |
| `GracePeriodInDays` | `Int32` | no |  |  | The grace period of the payment term specified in days. |
| `IsFreeDeliveryMonth` | `Boolean` | no |  | **deprecated since 22.4** | Specifies if the payment term implies a free delivery month. _(Replaced by Method)_ |
| `Method` | `Int32` | no |  | enum, since 22.4 | The method of the payment term. |
| `AddDaysToEOM` | `Int32` | no |  | since 22.4 | The number of days to add to the due date when using the end of month method. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the payment term is the default. |
| `InvoiceType` | `Int32` | no |  | enum | The invoice type of the payment term. |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](/entities/Common/PaymentMethod.md) |  | The business key identifier of the payment method of the payment term. References PaymentMethods . |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |
| `Code` | `String` | no |  | max length 15, since 24.8 | The code of the payment term. |

## Enumerations

### Method

| Name | Value |
| --- | ---: |
| `Days` | 0 |
| `FreeDeliveryMonth` | 1 |
| `EOM` | 2 |

### InvoiceType

| Name | Value |
| --- | ---: |
| `Standard` | 1 |
| `Internal` | 2 |
| `CashReceipt` | 3 |
| `Interest` | 4 |
| `OnAccount` | 5 |
| `DebitNote` | 6 |
| `ServiceTax` | 7 |
| `CorrectionInvoice` | 8 |
| `CollectiveCorrectionInvoice` | 9 |


## Referenced by

**Accounting**

- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `PaymentTerm` (expand)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `PaymentTermId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `PaymentTermId` (FK)

**Common**

- [PaymentPlanTemplateRows](/entities/Common/PaymentPlanTemplateRow.md) — `PaymentTerm` (expand)
- [PaymentPlanTemplateRows](/entities/Common/PaymentPlanTemplateRow.md) — `PaymentTermId` (FK)

**Purchase**

- [Inquiries](/entities/Purchase/Inquiry.md) — `PaymentTerm` (expand)
- [Inquiries](/entities/Purchase/Inquiry.md) — `PaymentTermId` (FK)
- [PurchaseOrderInvoices](/entities/Purchase/PurchaseOrderInvoice.md) — `PaymentTerm` (expand)
- [PurchaseOrderInvoices](/entities/Purchase/PurchaseOrderInvoice.md) — `PaymentTermId` (FK)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `PaymentTerm` (expand)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `PaymentTermId` (FK)
- [Suppliers](/entities/Purchase/Supplier.md) — `PaymentTerm` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `PaymentTermId` (FK)

**Sales**

- [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) — `PaymentTerm` (expand)
- [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) — `PaymentTermId` (FK)
- [CustomerOrderPaymentPlanRows](/entities/Sales/CustomerOrderPaymentPlanRow.md) — `PaymentTermId` (FK)
- [CustomerOrderTypes](/entities/Sales/CustomerOrderType.md) — `PaymentTermId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `PaymentTerm` (expand)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `PaymentTermId` (FK)
- [Customers](/entities/Sales/Customer.md) — `PaymentTerm` (expand)
- [Customers](/entities/Sales/Customer.md) — `PaymentTermId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `PaymentTerm` (expand)
- [Quotes](/entities/Sales/Quote.md) — `PaymentTermId` (FK)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `PaymentTermId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "GracePeriodInDays": 0,
  "IsFreeDeliveryMonth": false,
  "Method": 0,
  "AddDaysToEOM": 0,
  "IsDefault": false,
  "InvoiceType": 0,
  "PaymentMethodId": null,
  "CompanyIds": null,
  "Code": null
}
```
