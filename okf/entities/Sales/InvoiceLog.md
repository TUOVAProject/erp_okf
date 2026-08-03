---
type: API Entity
title: InvoiceLogs
description: Represents an invoice log entry.
resource: https://api.monitor.se/api/Monitor.API.Sales.InvoiceLog.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.InvoiceLog.html
  title: Monitor API — InvoiceLog
module: Sales
api_class: InvoiceLog
doc_name: InvoiceLogs
endpoint: GET /api/v1/Sales/InvoiceLogs
guid: bd995956-dc78-4373-ba58-c79b638861c8
permission: Show customer orders
introduced_in: '2.55'
property_count: 45
references_out:
- /entities/Accounting/AccountsReceivable.md
- /entities/Common/ApplicationUser.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderDeliveryRow.md
---

# InvoiceLogs

Represents an invoice log entry.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `InvoiceLog`
- **Endpoint:** `GET /api/v1/Sales/InvoiceLogs`
- **Required permission:** Show customer orders
- **GUID:** `bd995956-dc78-4373-ba58-c79b638861c8`
- **Introduced in:** 2.55

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the invoice log entry. |
| `InvoiceId` | `Int64?` | yes | [AccountsReceivables](../Accounting/AccountsReceivable.md) |  | The business key identifier of accounts receivable of the log entry. |
| `LoggingTimestamp` | `DateTimeOffset` | no |  |  | The date when the log entry was created. |
| `InvoiceDate` | `DateTimeOffset` | no |  |  | The invoice date of the log entry. |
| `InvoiceNumber` | `Int64` | no |  |  | The invoice number of the log entry. |
| `DeliveryRowId` | `Int64?` | yes | [CustomerOrderDeliveryRows](CustomerOrderDeliveryRow.md) |  | The business key identifier for the customer order delivery row of the log entry. |
| `PartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier for the part of the log entry. |
| `PartNumber` | `String` | no |  | max length 20 | The part number of the log entry. |
| `PartCategory` | `String` | no |  | max length 20 | The part category of the log entry. |
| `PartCode` | `String` | no |  | max length 20 | The part code of the log entry. |
| `CustomerId` | `Int64?` | yes | [Customers](Customer.md) |  | The business key identifier for the customer of the log entry. |
| `CustomerCode` | `String` | no |  | max length 10 | The customer code of the log entry. |
| `CustomerGroup` | `Int64?` | yes |  |  | The customer account group number of the log entry. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](CustomerOrder.md) |  | The business key identifier for the customer order of the log entry. |
| `CustomerOrderNumber` | `String` | no |  | max length 15 | The customer order number of the log entry. |
| `WarehouseId` | `Int64?` | yes | [Warehouses](../Common/Warehouse.md) |  | The business key identifier for the warehouse of the log entry. |
| `UserId` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) |  | The business key identifier for the application user of the log entry. |
| `UserName` | `String` | no |  | max length 20 | The user name of the log entry. |
| `Seller` | `String` | no |  | max length 35 | The seller of the log entry. |
| `OrderedQuantity` | `Decimal` | no |  |  | The ordered quantity of the log entry. |
| `InvoicedQuantity` | `Decimal` | no |  |  | The invoiced quantity of the log entry. |
| `UnitCode` | `String` | no |  | max length 10 | The unit code of the log entry. |
| `Discount` | `Decimal` | no |  |  | The discount of the log entry. |
| `Price` | `Decimal?` | yes |  |  | The price of the log entry. |
| `SetupPrice` | `Decimal?` | yes |  |  | The setup price of the log entry. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The price in company currency of the log entry. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |  | The setup price in company currency of the log entry. |
| `StandardPrice` | `Decimal?` | yes |  |  | The standard price of the log entry. |
| `WeightPerUnit` | `Decimal?` | yes |  |  | The weight per unit of the log entry. |
| `ProductGroupNumber` | `String` | no |  | max length 10 | The product group number of the log entry. |
| `StatisticalGoodsCode` | `String` | no |  | max length 14 | The statistical goods code of the log entry. |
| `IntrastatTransactionType` | `Int64?` | yes |  |  | The intrastat transaction type number of the log entry. |
| `TariffAndServiceCode` | `String` | no |  | max length 20 | The tariff and service code of the log entry. |
| `CurrencyCode` | `String` | no |  | max length 6 | The currency code of the log entry. |
| `ExchangeRate` | `Decimal` | no |  |  | The exchange rate of the log entry. |
| `CustomerOrderCategory` | `String` | no |  | max length 20 | The customer order category of the log entry. |
| `BusinessContactOrderNumber` | `String` | no |  | max length 30 | The business contact order number of the log entry. |
| `OrderRowType` | `Int32` | no |  | enum | The order row type of the log entry. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor of the log entry. |
| `DeliveryIndex` | `Int32` | no |  |  | The delivery index of the log entry. |
| `FifoPrice` | `Decimal?` | yes |  |  | The FIFO price of the log entry. |
| `ServiceType` | `Int32?` | yes |  |  | The service type of the log entry. |
| `AccountNumber` | `String` | no |  | max length 10 | The account number of the log entry. |
| `DeliveryAddressAddressee` | `String` | no |  | max length 50 | The delivery address addressee of the log entry. |
| `IsExportedToManagementAccounting` | `Boolean` | no |  |  | If the log entry is exported to management accounting. |

## Enumerations

### OrderRowType

| Name | Value |
| --- | ---: |
| `Part` | 1 |
| `Additional` | 2 |
| `Sum` | 3 |
| `FreeText` | 4 |


## Example

```json
{
  "Id": 0,
  "InvoiceId": null,
  "LoggingTimestamp": "0001-01-01T00:00:00+00:00",
  "InvoiceDate": "0001-01-01T00:00:00+00:00",
  "InvoiceNumber": 0,
  "DeliveryRowId": null,
  "PartId": null,
  "PartNumber": null,
  "PartCategory": null,
  "PartCode": null,
  "CustomerId": null,
  "CustomerCode": null,
  "CustomerGroup": null,
  "CustomerOrderId": null,
  "CustomerOrderNumber": null,
  "WarehouseId": null,
  "UserId": null,
  "UserName": null,
  "Seller": null,
  "OrderedQuantity": 0.0,
  "InvoicedQuantity": 0.0,
  "UnitCode": null,
  "Discount": 0.0,
  "Price": null,
  "SetupPrice": null,
  "PriceInCompanyCurrency": null,
  "SetupPriceInCompanyCurrency": null,
  "StandardPrice": null,
  "WeightPerUnit": null,
  "ProductGroupNumber": null,
  "StatisticalGoodsCode": null,
  "IntrastatTransactionType": null,
  "TariffAndServiceCode": null,
  "CurrencyCode": null,
  "ExchangeRate": 0.0,
  "CustomerOrderCategory": null,
  "BusinessContactOrderNumber": null,
  "OrderRowType": 0,
  "ConversionFactor": 0.0,
  "DeliveryIndex": 0,
  "FifoPrice": null,
  "ServiceType": null,
  "AccountNumber": null,
  "DeliveryAddressAddressee": null,
  "IsExportedToManagementAccounting": false
}
```
