---
type: API Entity
title: CustomerAccountGroups
description: Represents a customer account group.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerAccountGroup.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerAccountGroup.html
  title: Monitor API — CustomerAccountGroup
module: Sales
api_class: CustomerAccountGroup
doc_name: CustomerAccountGroups
endpoint: GET /api/v1/Sales/CustomerAccountGroups
guid: 10A23BD7-BF5A-4291-AA8E-F623F4A05533
permission: Show chart of accounts
introduced_in: '2.18'
property_count: 5
referenced_by:
- /entities/Accounting/AccountsReceivable.md
- /entities/Common/Country.md
- /entities/Common/DeliveryAddress.md
- /entities/Inventory/SalesForecast.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/Quote.md
- /entities/Sales/SalesAgreement.md
---

# CustomerAccountGroups

Represents a customer account group.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerAccountGroup`
- **Endpoint:** `GET /api/v1/Sales/CustomerAccountGroups`
- **Required permission:** Show chart of accounts
- **GUID:** `10A23BD7-BF5A-4291-AA8E-F623F4A05533`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the group. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the group is the default group. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the group. |
| `Description` | `String` | no |  |  | The translated description of the group. |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |

## Referenced by

**Accounting**

- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `CustomerAccountGroup` (expand)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `CustomerAccountGroupId` (FK)

**Common**

- [Countries](../Common/Country.md) — `CustomerAccountGroupId` (FK)
- [DeliveryAddresses](../Common/DeliveryAddress.md) — `CustomerAccountGroupId` (FK)

**Inventory**

- [SalesForecasts](../Inventory/SalesForecast.md) — `CustomerAccountGroupId` (FK)

**Sales**

- [CustomerOrderInvoices](CustomerOrderInvoice.md) — `AccountGroup` (expand)
- [CustomerOrderInvoices](CustomerOrderInvoice.md) — `AccountGroupId` (FK)
- [CustomerOrders](CustomerOrder.md) — `AccountGroup` (expand)
- [CustomerOrders](CustomerOrder.md) — `AccountGroupId` (FK)
- [CustomerOrders](CustomerOrder.md) — `CustomerAccountGroupId` (FK)
- [Customers](Customer.md) — `ActiveDeliveryAddressAccountGroup` (expand)
- [Customers](Customer.md) — `ActiveDeliveryAddressAccountGroupId` (FK)
- [Quotes](Quote.md) — `AccountGroup` (expand)
- [Quotes](Quote.md) — `AccountGroupId` (FK)
- [SalesAgreements](SalesAgreement.md) — `CustomerAccountGroupId` (FK)


## Example

```json
{
  "Id": 0,
  "IsDefault": false,
  "Number": 0,
  "Description": null,
  "CompanyIds": null
}
```
