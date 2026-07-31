---
type: API Entity
title: ApplicationUsers
description: Represents a queryable MONITOR application user.
resource: https://api.monitor.se/api/Monitor.API.Common.ApplicationUser.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ApplicationUser.html
  title: Monitor API — ApplicationUser
module: Common
api_class: ApplicationUser
doc_name: ApplicationUsers
endpoint: GET /api/v1/Common/ApplicationUsers
guid: 1B543334-333B-4D74-8680-C8A2395C8D9F
permission: Show user
introduced_in: '2.18'
property_count: 21
references_out:
- /entities/Accounting/VoucherSeries.md
- /entities/Common/ApplicationUserPrinter.md
- /entities/Common/LanguageCode.md
- /entities/Common/Warehouse.md
- /entities/Common/WarehousePermission.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/IncomingPayment.md
- /entities/Accounting/OutgoingPayment.md
- /entities/Common/ApplicationUserPrinter.md
- /entities/Common/BusinessContactNoteHistory.md
- /entities/Common/DelegatedWork.md
- /entities/Common/MonitoringTask.md
- /entities/Common/MonitoringTaskRecipient.md
- /entities/Common/PartConfigurationPreset.md
- /entities/Common/Person.md
- /entities/Common/ProjectActivity.md
- /entities/Common/ProjectActivityType.md
- /entities/Common/ProjectPhase.md
- /entities/Common/ProjectPhaseType.md
- /entities/Inventory/CaseEntryActivity.md
- /entities/Inventory/CaseEntryPhase.md
- /entities/Inventory/CaseManagementTemplateNode.md
- /entities/Inventory/Location.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartActivity.md
- /entities/Inventory/ProductRecord.md
- /entities/Inventory/QuantityChange.md
- /entities/Manufacturing/ManufacturingPickingList.md
- /entities/Purchase/Supplier.md
- /entities/Sales/BusinessOpportunityActivity.md
- /entities/Sales/BusinessOpportunityActivityTemplateRow.md
- /entities/Sales/BusinessOpportunitySalesProcessStep.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderActivity.md
- /entities/Sales/CustomerRelationshipManagementActivity.md
- /entities/Sales/InvoiceLog.md
- /entities/Sales/QuoteActivity.md
- /entities/Sales/SalesPickingList.md
---

# ApplicationUsers

Represents a queryable MONITOR application user.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ApplicationUser`
- **Endpoint:** `GET /api/v1/Common/ApplicationUsers`
- **Required permission:** Show user
- **GUID:** `1B543334-333B-4D74-8680-C8A2395C8D9F`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the application user. |
| `Username` | `String` | no |  | unique, max length 20 | The username of the application user. |
| `Description` | `String` | no |  | max length 35, since 2.52 | The description of the application user. |
| `WindowsUserAccountName` | `String` | no |  | max length 80 | The windows account username of the application user. |
| `IsInvisible` | `Boolean` | no |  | since 2.52 | Specifies if the application user is hidden from general use in the MONITOR system. |
| `DefaultRole` | `Int64` | no |  | since 2.52 | The default role of the application user. |
| `DefaultGroup` | `Int64?` | yes |  | since 2.52 | The business key identifier of the application user's default permission group. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) | since 2.52 | The business key identifier of the application user's default warehouse. References Warehouses . |
| `LanguageId` | `Int64` | no | [LanguageCodes](/entities/Common/LanguageCode.md) | since 2.52 | The business key identifier of the application user's default language code. References LanguageCodes . |
| `MailAddress` | `String` | no |  | max length 80, since 2.52 | The email address of the user. |
| `MailMethod` | `Int32?` | yes |  | enum, since 2.52 | The email method of the user. |
| `Printers` | `ApplicationUserPrinters[]` | no | [ApplicationUserPrinters](/entities/Common/ApplicationUserPrinter.md) | expandable, collection, since 2.52 | The printers that have been assigned to the user. |
| `DefaultPrinter` | `String` | no |  | since 2.52 | The name of the default printer that have been assigned to the user. |
| `External1Printer` | `String` | no |  | max length 300, **deprecated since 26.3**, since 2.52 | The name of the external 1 printer that has been assigned to the user. _(Use the Printers collection with FormReportType = FilesExternal1 instead)_ |
| `External2Printer` | `String` | no |  | max length 300, **deprecated since 26.3**, since 2.52 | The name of the external 2 printer that has been assigned to the user. _(Use the Printers collection with FormReportType = FilesExternal2 instead)_ |
| `External3Printer` | `String` | no |  | max length 300, **deprecated since 26.3**, since 2.52 | The name of the external 3 printer that has been assigned to the user. _(Use the Printers collection with FormReportType = FilesExternal3 instead)_ |
| `PrintoutFormatForParcel` | `Int32` | no |  | enum, since 2.52 | The printout document format type that have been assigned to the user. |
| `WarehousePermissions` | `WarehousePermissions[]` | no | [WarehousePermissions](/entities/Common/WarehousePermission.md) | expandable, collection, since 22.3 | The warehouse permissions that apply to the application user. |
| `DefaultVoucherSeriesId` | `Int64?` | yes | [VoucherSeries](/entities/Accounting/VoucherSeries.md) | since 22.3 | The business key identifier of the application user's default voucher series. |
| `UserAuthenticationMethod` | `Int32` | no |  | enum, since 25.3 | The selected authentication method of the application user. |
| `Culture` | `String` | no |  | since 25.7 | The culture setting of the user in .NET format. |

## Enumerations

### MailMethod

| Name | Value |
| --- | ---: |
| `ClientBasedOutlook` | 0 |
| `ServerBasedExchange` | 2 |
| `ServerBasedSmtp` | 3 |
| `ServerBasedExchangeOnline` | 4 |

### PrintoutFormatForParcel

| Name | Value |
| --- | ---: |
| `PDF` | 0 |
| `ZPL` | 1 |
| `LaserSte` | 2 |
| `ThermoSe` | 3 |
| `LaserA5` | 4 |
| `Laser2A5` | 5 |
| `Thermo190` | 6 |
| `ThermoBrev3` | 7 |
| `Thermo165` | 8 |

### UserAuthenticationMethod

| Name | Value |
| --- | ---: |
| `Password` | 0 |
| `WindowsIntegrated` | 1 |
| `Oidc` | 4 |


## Referenced by

**Accounting**

- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `BlockedBy` (expand)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `BlockedById` (FK)
- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `CancelledByUserId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `CancelledByUserId` (FK)

**Common**

- [ApplicationUserPrinters](/entities/Common/ApplicationUserPrinter.md) — `ApplicationUserId` (FK)
- [BusinessContactNoteHistories](/entities/Common/BusinessContactNoteHistory.md) — `CreatedByUserId` (FK)
- [DelegatedWork](/entities/Common/DelegatedWork.md) — `DelegatedBy` (FK)
- [MonitoringTaskRecipients](/entities/Common/MonitoringTaskRecipient.md) — `ApplicationUserId` (FK)
- [MonitoringTasks](/entities/Common/MonitoringTask.md) — `ApplicationUser` (expand)
- [MonitoringTasks](/entities/Common/MonitoringTask.md) — `ApplicationUserId` (FK)
- [PartConfigurationPresets](/entities/Common/PartConfigurationPreset.md) — `ChangedBy` (FK)
- [PartConfigurationPresets](/entities/Common/PartConfigurationPreset.md) — `CreatedBy` (FK)
- [Persons](/entities/Common/Person.md) — `ApplicationUserId` (FK)
- [ProjectActivities](/entities/Common/ProjectActivity.md) — `CompletedByUserId` (FK)
- [ProjectActivities](/entities/Common/ProjectActivity.md) — `ResponsibleUserId` (FK)
- [ProjectActivityTypes](/entities/Common/ProjectActivityType.md) — `ResponsibleUserId` (FK)
- [ProjectPhaseTypes](/entities/Common/ProjectPhaseType.md) — `ManagerId` (FK)
- [ProjectPhases](/entities/Common/ProjectPhase.md) — `ResponsibleUserId` (FK)

**Inventory**

- [CaseEntryActivities](/entities/Inventory/CaseEntryActivity.md) — `CompletedByUserId` (FK)
- [CaseEntryActivities](/entities/Inventory/CaseEntryActivity.md) — `ResponsibleUserId` (FK)
- [CaseEntryPhases](/entities/Inventory/CaseEntryPhase.md) — `ResponsibleUserId` (FK)
- [CaseManagementTemplateNodes](/entities/Inventory/CaseManagementTemplateNode.md) — `UserId` (FK)
- [Locations](/entities/Inventory/Location.md) — `BlockedBy` (expand)
- [Locations](/entities/Inventory/Location.md) — `BlockedById` (FK)
- [PartActivities](/entities/Inventory/PartActivity.md) — `ResponsibleUserId` (FK)
- [Parts](/entities/Inventory/Part.md) — `BlockedBy` (expand)
- [Parts](/entities/Inventory/Part.md) — `BlockedById` (FK)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `BlockedById` (FK)
- [QuantityChanges](/entities/Inventory/QuantityChange.md) — `DeliveredByUserId` (FK)
- [QuantityChanges](/entities/Inventory/QuantityChange.md) — `PickingByUserId` (FK)

**Manufacturing**

- [ManufacturingPickingLists](/entities/Manufacturing/ManufacturingPickingList.md) — `CreatedByApplicationUserId` (FK)
- [ManufacturingPickingLists](/entities/Manufacturing/ManufacturingPickingList.md) — `PrintedByApplicationUserId` (FK)

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `BlockedBy` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `BlockedById` (FK)

**Sales**

- [BusinessOpportunityActivities](/entities/Sales/BusinessOpportunityActivity.md) — `CompletedByUserId` (FK)
- [BusinessOpportunityActivities](/entities/Sales/BusinessOpportunityActivity.md) — `ResponsibleUserId` (FK)
- [BusinessOpportunityActivityTemplateRows](/entities/Sales/BusinessOpportunityActivityTemplateRow.md) — `ResponsibleUserId` (FK)
- [BusinessOpportunitySalesProcessSteps](/entities/Sales/BusinessOpportunitySalesProcessStep.md) — `ResponsibleUserId` (FK)
- [CustomerOrderActivities](/entities/Sales/CustomerOrderActivity.md) — `ResponsibleUserId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `PrintoutBy` (FK)
- [CustomerRelationshipManagementActivities](/entities/Sales/CustomerRelationshipManagementActivity.md) — `CompletedByUserId` (FK)
- [CustomerRelationshipManagementActivities](/entities/Sales/CustomerRelationshipManagementActivity.md) — `ResponsibleUserId` (FK)
- [Customers](/entities/Sales/Customer.md) — `BlockedBy` (expand)
- [Customers](/entities/Sales/Customer.md) — `BlockedById` (FK)
- [InvoiceLogs](/entities/Sales/InvoiceLog.md) — `UserId` (FK)
- [QuoteActivities](/entities/Sales/QuoteActivity.md) — `CompletedByUserId` (FK)
- [QuoteActivities](/entities/Sales/QuoteActivity.md) — `ResponsibleUserId` (FK)
- [SalesPickingLists](/entities/Sales/SalesPickingList.md) — `PrintedByApplicationUserId` (FK)


## Example

```json
{
  "Id": 0,
  "Username": null,
  "Description": null,
  "WindowsUserAccountName": null,
  "IsInvisible": false,
  "DefaultRole": 0,
  "DefaultGroup": null,
  "WarehouseId": 0,
  "LanguageId": 0,
  "MailAddress": null,
  "MailMethod": null,
  "Printers": null,
  "DefaultPrinter": null,
  "External1Printer": null,
  "External2Printer": null,
  "External3Printer": null,
  "PrintoutFormatForParcel": 0,
  "WarehousePermissions": null,
  "DefaultVoucherSeriesId": null,
  "UserAuthenticationMethod": 0,
  "Culture": null
}
```
