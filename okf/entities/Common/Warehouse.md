---
type: API Entity
title: Warehouses
description: Represents a warehouse.
resource: https://api.monitor.se/api/Monitor.API.Common.Warehouse.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Warehouse.html
  title: Monitor API — Warehouse
module: Common
api_class: Warehouse
doc_name: Warehouses
endpoint: GET /api/v1/Common/Warehouses
guid: DA31FCD6-18FE-4607-91F9-44CAE738840A
permission: Show company information
introduced_in: '2.18'
property_count: 14
references_out:
- /entities/Common/Calendar.md
- /entities/Common/Company.md
- /entities/Common/Country.md
- /entities/Common/DeliveryAddress.md
- /entities/Common/LanguageCode.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Common/ApplicationUser.md
- /entities/Common/Company.md
- /entities/Common/DeliveryAddressWarehouseInformation.md
- /entities/Common/EdiBehavior.md
- /entities/Common/MonitoringTaskRow.md
- /entities/Common/Person.md
- /entities/Common/TransferProfile.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/Location.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartLocation.md
- /entities/Inventory/PartPlanningInformation.md
- /entities/Inventory/PhysicalInventoryList.md
- /entities/Inventory/QuantityChange.md
- /entities/Inventory/SalesForecast.md
- /entities/Inventory/StockTransaction.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Manufacturing/ManufacturingOrderOperationReporting.md
- /entities/Manufacturing/ManufacturingPickingList.md
- /entities/Manufacturing/WorkCenter.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderInvoice.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/BlanketOrderSalesType.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/InvoiceLog.md
- /entities/Sales/Quote.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/SalesPickingList.md
- /entities/Sales/Shipment.md
---

# Warehouses

Represents a warehouse.

- **Module:** [Common](/modules/Common.md)
- **API class:** `Warehouse`
- **Endpoint:** `GET /api/v1/Common/Warehouses`
- **Required permission:** Show company information
- **GUID:** `DA31FCD6-18FE-4607-91F9-44CAE738840A`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the warehouse. |
| `Name` | `String` | no |  | max length 35 | The warehouse name. |
| `Code` | `String` | no |  | unique, max length 10 | The warehouse code. |
| `LanguageId` | `Int64` | no | [LanguageCodes](/entities/Common/LanguageCode.md) |  | The business key identifier of the warehouse language code. References LanguageCodes . |
| `CountryId` | `Int64` | no | [Countries](/entities/Common/Country.md) |  | The business key identifier of the warehouse country. References Countries . |
| `PlaceOfDispatch` | `String` | no |  | max length 40 | The place of dispatch for the warehouse. |
| `PalletRegistrationNumber` | `String` | no |  | max length 40, **deprecated since 2.54** | The pallet registration number of the warehouse. _(Never used in G5.)_ |
| `Url` | `String` | no |  | max length 255 | The website URL of the warehouse. |
| `TimeZoneId` | `String` | no | [Companies](/entities/Common/Company.md) | **deprecated since 25.2**, since 2.29 | The time zone of the warehouse. Specified as a time zone identifier (e.g. "W. Europe Standard Time"). From 25.2 moved to Companies . _(Time zone is now on company level. All warhouses will return the same value as the company time zone.)_ |
| `TimeZone` | `Decimal?` | yes |  | **deprecated since 2.29** | The timezone offset of the warehouse. _(Replaced by TimeZoneId)_ |
| `CalendarId` | `Int64` | no | [Calendars](/entities/Common/Calendar.md) |  | The business key identifier of the warehouse calendar. References Calendars . |
| `Calendar` | `Calendars` | no | [Calendars](/entities/Common/Calendar.md) | expandable | The warehouse calendar. |
| `VatNumber` | `String` | no |  | max length 25 | The VAT number of the warehouse. |
| `DeliveryAddresses` | `DeliveryAddresses[]` | no | [DeliveryAddresses](/entities/Common/DeliveryAddress.md) | expandable, collection, since 25.4 | All available delivery addresses of the warehouse. |

## Referenced by

**Accounting**

- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `WarehouseId` (FK)

**Common**

- [ApplicationUsers](/entities/Common/ApplicationUser.md) — `WarehouseId` (FK)
- [Companies](/entities/Common/Company.md) — `Warehouses` (expand)
- [DeliveryAddressWarehouseInformations](/entities/Common/DeliveryAddressWarehouseInformation.md) — `WarehouseId` (FK)
- [EdiBehaviors](/entities/Common/EdiBehavior.md) — `Warehouse` (expand)
- [EdiBehaviors](/entities/Common/EdiBehavior.md) — `WarehouseId` (FK)
- [MonitoringTaskRows](/entities/Common/MonitoringTaskRow.md) — `Warehouses` (expand)
- [Persons](/entities/Common/Person.md) — `WarehouseId` (FK)
- [TransferProfiles](/entities/Common/TransferProfile.md) — `RemoteWarehouseId` (FK)

**Inventory**

- [CaseEntry](/entities/Inventory/CaseEntry.md) — `Warehouse` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `WarehouseId` (FK)
- [Locations](/entities/Inventory/Location.md) — `Warehouse` (expand)
- [Locations](/entities/Inventory/Location.md) — `WarehouseId` (FK)
- [PartLocations](/entities/Inventory/PartLocation.md) — `Warehouse` (expand)
- [PartLocations](/entities/Inventory/PartLocation.md) — `WarehouseId` (FK)
- [PartPlanningInformation](/entities/Inventory/PartPlanningInformation.md) — `AcquisitionWarehouseId` (FK)
- [PartPlanningInformation](/entities/Inventory/PartPlanningInformation.md) — `WarehouseId` (FK)
- [Parts](/entities/Inventory/Part.md) — `DefaultCustomerOrderWarehouseId` (FK)
- [PhysicalInventoryLists](/entities/Inventory/PhysicalInventoryList.md) — `WarehouseId` (FK)
- [QuantityChanges](/entities/Inventory/QuantityChange.md) — `WarehouseId` (FK)
- [SalesForecasts](/entities/Inventory/SalesForecast.md) — `WarehouseId` (FK)
- [StockTransactions](/entities/Inventory/StockTransaction.md) — `WarehouseId` (FK)

**Manufacturing**

- [ManufacturingOrderNodes](/entities/Manufacturing/ManufacturingOrderNode.md) — `WarehouseId` (FK)
- [ManufacturingOrderOperationReportings](/entities/Manufacturing/ManufacturingOrderOperationReporting.md) — `WarehouseId` (FK)
- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `WarehouseId` (FK)
- [ManufacturingPickingLists](/entities/Manufacturing/ManufacturingPickingList.md) — `WarehouseId` (FK)
- [WorkCenters](/entities/Manufacturing/WorkCenter.md) — `Warehouse` (expand)
- [WorkCenters](/entities/Manufacturing/WorkCenter.md) — `WarehouseId` (FK)

**Purchase**

- [Inquiries](/entities/Purchase/Inquiry.md) — `WarehouseId` (FK)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `WarehouseId` (FK)
- [PurchaseOrderInvoices](/entities/Purchase/PurchaseOrderInvoice.md) — `WarehouseId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `Warehouse` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `WarehouseId` (FK)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `Warehouse` (expand)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `WarehouseId` (FK)

**Sales**

- [BlanketOrderSalesTypes](/entities/Sales/BlanketOrderSalesType.md) — `WarehouseId` (FK)
- [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) — `WarehouseId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `WarehouseId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `WarehouseId` (FK)
- [InvoiceLogs](/entities/Sales/InvoiceLog.md) — `WarehouseId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `WarehouseId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `WarehouseId` (FK)
- [SalesPickingLists](/entities/Sales/SalesPickingList.md) — `WarehouseId` (FK)
- [Shipments](/entities/Sales/Shipment.md) — `WarehouseId` (FK)


## Example

```json
{
  "Id": 0,
  "Name": null,
  "Code": null,
  "LanguageId": 0,
  "CountryId": 0,
  "PlaceOfDispatch": null,
  "PalletRegistrationNumber": null,
  "Url": null,
  "TimeZoneId": null,
  "TimeZone": null,
  "CalendarId": 0,
  "Calendar": null,
  "VatNumber": null,
  "DeliveryAddresses": null
}
```
