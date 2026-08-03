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

- **Module:** [Common](../../modules/Common.md)
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
| `DefaultVatRateForPurchaseId` | `Int64` | no | [VatRates](VatRate.md) | since 2.42 | The business key identifier of the VAT group's default VAT rate for Purchase. References VatRates . |
| `DefaultVatRateForSalesId` | `Int64` | no | [VatRates](VatRate.md) | since 2.42 | The business key identifier of the VAT group's default VAT rate for Sales. References VatRates . |
| `DefaultVatRateId` | `Int64` | no | [VatRates](VatRate.md) |  | This property is obsolete and split into DefaultVatRateForPurchaseId and DefaultVatRateForSalesId The business key identifier of the VAT group's default VAT rate. References VatRates . |

## Referenced by

**Accounting**

- [AccountsPayables](../Accounting/AccountsPayable.md) — `VatGroupId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `VatGroupId` (FK)

**Common**

- [Countries](Country.md) — `CustomerVatGroupId` (FK)
- [Countries](Country.md) — `SupplierVatGroupId` (FK)
- [Countries](Country.md) — `VatGroupId` (FK)
- [DeliveryAddresses](DeliveryAddress.md) — `VatGroupId` (FK)

**Purchase**

- [Inquiries](../Purchase/Inquiry.md) — `VatGroupId` (FK)
- [PurchaseOrderInvoices](../Purchase/PurchaseOrderInvoice.md) — `VatGroupId` (FK)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `VatGroup` (expand)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `VatGroupId` (FK)

**Sales**

- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `VatGroupId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `VatGroupId` (FK)
- [Quotes](../Sales/Quote.md) — `VatGroupId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `VatGroupId` (FK)


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
