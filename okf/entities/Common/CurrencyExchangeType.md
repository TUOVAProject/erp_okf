---
type: API Entity
title: CurrencyExchangeTypes
description: Represents a currency exchange type.
resource: https://api.monitor.se/api/Monitor.API.Common.CurrencyExchangeType.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.CurrencyExchangeType.html
  title: Monitor API — CurrencyExchangeType
module: Common
api_class: CurrencyExchangeType
doc_name: CurrencyExchangeTypes
endpoint: GET /api/v1/Common/CurrencyExchangeTypes
guid: 9d516f58-da27-405d-9df3-f5071859276d
permission: Show currencies
introduced_in: '22.9'
property_count: 3
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/AccountsReceivable.md
- /entities/Common/CurrencyExchangeRate.md
- /entities/Common/CurrencyExchangeRateChangeLog.md
- /entities/Purchase/BlanketOrderPurchase.md
- /entities/Purchase/BlanketOrderPurchaseType.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/InquiryType.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderType.md
- /entities/Purchase/Supplier.md
- /entities/Sales/BlanketOrderSales.md
- /entities/Sales/BlanketOrderSalesType.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderType.md
- /entities/Sales/Quote.md
- /entities/Sales/QuoteType.md
- /entities/Sales/ShipmentCustoms.md
---

# CurrencyExchangeTypes

Represents a currency exchange type.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `CurrencyExchangeType`
- **Endpoint:** `GET /api/v1/Common/CurrencyExchangeTypes`
- **Required permission:** Show currencies
- **GUID:** `9d516f58-da27-405d-9df3-f5071859276d`
- **Introduced in:** 22.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the currency exchange type. |
| `Description` | `String` | no |  |  | The translated description of the currency exchange type. |
| `IsDefaultAFSRate` | `Boolean` | no |  |  | Specifies if default AFS rate. |

## Referenced by

**Accounting**

- [AccountsPayables](../Accounting/AccountsPayable.md) — `CurrencyExchangeTypeId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `CurrencyExchangeTypeId` (FK)

**Common**

- [CurrencyExchangeRateChangeLogs](CurrencyExchangeRateChangeLog.md) — `CurrencyExchangeTypeId` (FK)
- [CurrencyExchangeRates](CurrencyExchangeRate.md) — `CurrencyExchangeTypeId` (FK)

**Purchase**

- [BlanketOrderPurchaseTypes](../Purchase/BlanketOrderPurchaseType.md) — `CurrencyExchangeTypeId` (FK)
- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `CurrencyExchangeType` (expand)
- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `CurrencyExchangeTypeId` (FK)
- [Inquiries](../Purchase/Inquiry.md) — `CurrencyExchangeTypeId` (FK)
- [InquiryTypes](../Purchase/InquiryType.md) — `CurrencyExchangeTypeId` (FK)
- [PurchaseOrderTypes](../Purchase/PurchaseOrderType.md) — `CurrencyExchangeTypeId` (FK)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `CurrencyExchangeTypeId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `CurrencyExchangeTypeId` (FK)

**Sales**

- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `CurrencyExchangeType` (expand)
- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `CurrencyExchangeTypeId` (FK)
- [BlanketOrderSalesTypes](../Sales/BlanketOrderSalesType.md) — `CurrencyExchangeTypeId` (FK)
- [CustomerOrderTypes](../Sales/CustomerOrderType.md) — `CurrencyExchangeTypeId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `CurrencyExchangeTypeId` (FK)
- [Customers](../Sales/Customer.md) — `CurrencyExchangeTypeId` (FK)
- [QuoteTypes](../Sales/QuoteType.md) — `CurrencyExchangeTypeId` (FK)
- [Quotes](../Sales/Quote.md) — `CurrencyExchangeTypeId` (FK)
- [ShipmentCustoms](../Sales/ShipmentCustoms.md) — `CurrencyExchangeType` (expand)
- [ShipmentCustoms](../Sales/ShipmentCustoms.md) — `CurrencyExchangeTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Description": null,
  "IsDefaultAFSRate": false
}
```
