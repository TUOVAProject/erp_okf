---
type: API Entity
title: VatGroups
description: Represents a VAT group.
resource: https://api.monitor.se/api/Monitor.API.Common.VatGroup.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.VatGroup.html
  title: Monitor API — VatGroup
module: Common
api_class: VatGroup
doc_name: VatGroups
endpoint: GET /api/v1/Common/VatGroups
guid: A4C42058-E000-4102-AADB-53773B571235
permission: Show VAT settings
introduced_in: '2.18'
property_count: 6
references_out:
- /entities/Common/VatRate.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/AccountsReceivable.md
- /entities/Common/Country.md
- /entities/Common/DeliveryAddress.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderInvoice.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/Quote.md
- /entities/Sales/SalesAgreement.md
---

# VatGroups

Represents a VAT group.

- **Module:** [Common](/modules/Common.md)
- **API class:** `VatGroup`
- **Endpoint:** `GET /api/v1/Common/VatGroups`
- **Required permission:** Show VAT settings
- **GUID:** `A4C42058-E000-4102-AADB-53773B571235`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the VAT group. |
| `Number` | `Int64` | no |  | unique | The VAT group number. |
| `Description` | `String` | no |  |  | The translated description of the VAT group. |
| `DefaultVatRateForPurchaseId` | `Int64` | no | [VatRates](/entities/Common/VatRate.md) | since 2.42 | The business key identifier of the VAT group's default VAT rate for Purchase. References VatRates . |
| `DefaultVatRateForSalesId` | `Int64` | no | [VatRates](/entities/Common/VatRate.md) | since 2.42 | The business key identifier of the VAT group's default VAT rate for Sales. References VatRates . |
| `DefaultVatRateId` | `Int64` | no | [VatRates](/entities/Common/VatRate.md) |  | This property is obsolete and split into DefaultVatRateForPurchaseId and DefaultVatRateForSalesId The business key identifier of the VAT group's default VAT rate. References VatRates . |

## Referenced by

**Accounting**

- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `VatGroupId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `VatGroupId` (FK)

**Common**

- [Countries](/entities/Common/Country.md) — `CustomerVatGroupId` (FK)
- [Countries](/entities/Common/Country.md) — `SupplierVatGroupId` (FK)
- [Countries](/entities/Common/Country.md) — `VatGroupId` (FK)
- [DeliveryAddresses](/entities/Common/DeliveryAddress.md) — `VatGroupId` (FK)

**Purchase**

- [Inquiries](/entities/Purchase/Inquiry.md) — `VatGroupId` (FK)
- [PurchaseOrderInvoices](/entities/Purchase/PurchaseOrderInvoice.md) — `VatGroupId` (FK)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `VatGroup` (expand)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `VatGroupId` (FK)

**Sales**

- [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) — `VatGroupId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `VatGroupId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `VatGroupId` (FK)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `VatGroupId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "DefaultVatRateForPurchaseId": 0,
  "DefaultVatRateForSalesId": 0,
  "DefaultVatRateId": 0
}
```
