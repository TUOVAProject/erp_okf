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

- **Module:** [Common](../../modules/Common.md)
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
| `WarehouseId` | `Int64` | no | [Warehouses](Warehouse.md) | since 2.52 | The business key identifier of the application user's default warehouse. References Warehouses . |
| `LanguageId` | `Int64` | no | [LanguageCodes](LanguageCode.md) | since 2.52 | The business key identifier of the application user's default language code. References LanguageCodes . |
| `MailAddress` | `String` | no |  | max length 80, since 2.52 | The email address of the user. |
| `MailMethod` | `Int32?` | yes |  | enum, since 2.52 | The email method of the user. |
| `Printers` | `ApplicationUserPrinters[]` | no | [ApplicationUserPrinters](ApplicationUserPrinter.md) | expandable, collection, since 2.52 | The printers that have been assigned to the user. |
| `DefaultPrinter` | `String` | no |  | since 2.52 | The name of the default printer that have been assigned to the user. |
| `External1Printer` | `String` | no |  | max length 300, **deprecated since 26.3**, since 2.52 | The name of the external 1 printer that has been assigned to the user. _(Use the Printers collection with FormReportType = FilesExternal1 instead)_ |
| `External2Printer` | `String` | no |  | max length 300, **deprecated since 26.3**, since 2.52 | The name of the external 2 printer that has been assigned to the user. _(Use the Printers collection with FormReportType = FilesExternal2 instead)_ |
| `External3Printer` | `String` | no |  | max length 300, **deprecated since 26.3**, since 2.52 | The name of the external 3 printer that has been assigned to the user. _(Use the Printers collection with FormReportType = FilesExternal3 instead)_ |
| `PrintoutFormatForParcel` | `Int32` | no |  | enum, since 2.52 | The printout document format type that have been assigned to the user. |
| `WarehousePermissions` | `WarehousePermissions[]` | no | [WarehousePermissions](WarehousePermission.md) | expandable, collection, since 22.3 | The warehouse permissions that apply to the application user. |
| `DefaultVoucherSeriesId` | `Int64?` | yes | [VoucherSeries](../Accounting/VoucherSeries.md) | since 22.3 | The business key identifier of the application user's default voucher series. |
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

- [AccountsPayables](../Accounting/AccountsPayable.md) — `BlockedBy` (expand)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `BlockedById` (FK)
- [IncomingPayments](../Accounting/IncomingPayment.md) — `CancelledByUserId` (FK)
- [OutgoingPayments](../Accounting/OutgoingPayment.md) — `CancelledByUserId` (FK)

**Common**

- [ApplicationUserPrinters](ApplicationUserPrinter.md) — `ApplicationUserId` (FK)
- [BusinessContactNoteHistories](BusinessContactNoteHistory.md) — `CreatedByUserId` (FK)
- [DelegatedWork](DelegatedWork.md) — `DelegatedBy` (FK)
- [MonitoringTaskRecipients](MonitoringTaskRecipient.md) — `ApplicationUserId` (FK)
- [MonitoringTasks](MonitoringTask.md) — `ApplicationUser` (expand)
- [MonitoringTasks](MonitoringTask.md) — `ApplicationUserId` (FK)
- [PartConfigurationPresets](PartConfigurationPreset.md) — `ChangedBy` (FK)
- [PartConfigurationPresets](PartConfigurationPreset.md) — `CreatedBy` (FK)
- [Persons](Person.md) — `ApplicationUserId` (FK)
- [ProjectActivities](ProjectActivity.md) — `CompletedByUserId` (FK)
- [ProjectActivities](ProjectActivity.md) — `ResponsibleUserId` (FK)
- [ProjectActivityTypes](ProjectActivityType.md) — `ResponsibleUserId` (FK)
- [ProjectPhaseTypes](ProjectPhaseType.md) — `ManagerId` (FK)
- [ProjectPhases](ProjectPhase.md) — `ResponsibleUserId` (FK)

**Inventory**

- [CaseEntryActivities](../Inventory/CaseEntryActivity.md) — `CompletedByUserId` (FK)
- [CaseEntryActivities](../Inventory/CaseEntryActivity.md) — `ResponsibleUserId` (FK)
- [CaseEntryPhases](../Inventory/CaseEntryPhase.md) — `ResponsibleUserId` (FK)
- [CaseManagementTemplateNodes](../Inventory/CaseManagementTemplateNode.md) — `UserId` (FK)
- [Locations](../Inventory/Location.md) — `BlockedBy` (expand)
- [Locations](../Inventory/Location.md) — `BlockedById` (FK)
- [PartActivities](../Inventory/PartActivity.md) — `ResponsibleUserId` (FK)
- [Parts](../Inventory/Part.md) — `BlockedBy` (expand)
- [Parts](../Inventory/Part.md) — `BlockedById` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `BlockedById` (FK)
- [QuantityChanges](../Inventory/QuantityChange.md) — `DeliveredByUserId` (FK)
- [QuantityChanges](../Inventory/QuantityChange.md) — `PickingByUserId` (FK)

**Manufacturing**

- [ManufacturingPickingLists](../Manufacturing/ManufacturingPickingList.md) — `CreatedByApplicationUserId` (FK)
- [ManufacturingPickingLists](../Manufacturing/ManufacturingPickingList.md) — `PrintedByApplicationUserId` (FK)

**Purchase**

- [Suppliers](../Purchase/Supplier.md) — `BlockedBy` (expand)
- [Suppliers](../Purchase/Supplier.md) — `BlockedById` (FK)

**Sales**

- [BusinessOpportunityActivities](../Sales/BusinessOpportunityActivity.md) — `CompletedByUserId` (FK)
- [BusinessOpportunityActivities](../Sales/BusinessOpportunityActivity.md) — `ResponsibleUserId` (FK)
- [BusinessOpportunityActivityTemplateRows](../Sales/BusinessOpportunityActivityTemplateRow.md) — `ResponsibleUserId` (FK)
- [BusinessOpportunitySalesProcessSteps](../Sales/BusinessOpportunitySalesProcessStep.md) — `ResponsibleUserId` (FK)
- [CustomerOrderActivities](../Sales/CustomerOrderActivity.md) — `ResponsibleUserId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `PrintoutBy` (FK)
- [CustomerRelationshipManagementActivities](../Sales/CustomerRelationshipManagementActivity.md) — `CompletedByUserId` (FK)
- [CustomerRelationshipManagementActivities](../Sales/CustomerRelationshipManagementActivity.md) — `ResponsibleUserId` (FK)
- [Customers](../Sales/Customer.md) — `BlockedBy` (expand)
- [Customers](../Sales/Customer.md) — `BlockedById` (FK)
- [InvoiceLogs](../Sales/InvoiceLog.md) — `UserId` (FK)
- [QuoteActivities](../Sales/QuoteActivity.md) — `CompletedByUserId` (FK)
- [QuoteActivities](../Sales/QuoteActivity.md) — `ResponsibleUserId` (FK)
- [SalesPickingLists](../Sales/SalesPickingList.md) — `PrintedByApplicationUserId` (FK)


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
