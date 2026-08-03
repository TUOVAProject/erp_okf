---
type: API Entity
title: Persons
description: Represents a person.
resource: https://api.monitor.se/api/Monitor.API.Common.Person.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Person.html
  title: Monitor API — Person
module: Common
api_class: Person
doc_name: Persons
endpoint: GET /api/v1/Common/Persons
guid: 50651357-4726-4877-A944-87820BED57BA
permission: Show person
introduced_in: '2.18'
property_count: 60
references_out:
- /entities/Common/Address.md
- /entities/Common/ApplicationUser.md
- /entities/Common/BlobData.md
- /entities/Common/Comment.md
- /entities/Common/Department.md
- /entities/Common/EmploymentPeriod.md
- /entities/Common/ExtraField.md
- /entities/Common/LanguageCode.md
- /entities/Common/PersonManufacturingPrintSettings.md
- /entities/Common/PersonRelative.md
- /entities/Common/Warehouse.md
- /entities/Sales/CustomerDistrict.md
- /entities/TimeRecording/PersonTimeBank.md
- /entities/TimeRecording/PersonWorkCenter.md
- /entities/TimeRecording/PlannedAbsence.md
- /entities/TimeRecording/Schedule.md
referenced_by:
- /entities/Common/DelegatedWork.md
- /entities/Common/EmploymentPeriod.md
- /entities/Common/Project.md
- /entities/Common/ProjectActivityCalendarAppointment.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartPlanningInformation.md
- /entities/Inventory/PartTemplate.md
- /entities/Inventory/ProductRecord.md
- /entities/Inventory/QuantityChange.md
- /entities/Manufacturing/MaintenanceReporting.md
- /entities/Manufacturing/ManufacturingOrderOperationReporting.md
- /entities/Manufacturing/ManufacturingPickingList.md
- /entities/Purchase/BlanketOrderPurchase.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/Supplier.md
- /entities/Sales/BlanketOrderSales.md
- /entities/Sales/BusinessOpportunity.md
- /entities/Sales/BusinessOpportunityActivity.md
- /entities/Sales/BusinessOpportunitySalesProcessStep.md
- /entities/Sales/BusinessOpportunityType.md
- /entities/Sales/CreateSalesPickingList.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/Quote.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/SalesPickingList.md
- /entities/Sales/SalesProcessTemplateRow.md
- /entities/Sales/ShipmentCustoms.md
- /entities/TimeRecording/AttendanceChart.md
- /entities/TimeRecording/PersonTimeBank.md
- /entities/TimeRecording/PersonWorkCenter.md
- /entities/TimeRecording/RecordingDay.md
- /entities/TimeRecording/StandbyWork.md
- /entities/TimeRecording/WorkInterval.md
---

# Persons

Represents a person.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `Person`
- **Endpoint:** `GET /api/v1/Common/Persons`
- **Required permission:** Show person
- **GUID:** `50651357-4726-4877-A944-87820BED57BA`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the person. |
| `BlockedContextType` | `Int32` | no |  | bitmask, enum | Specifies where the person block applies. |
| `IsRecordingEmployee` | `Boolean` | no |  |  | Specifies if the person has any type of employee recording enabled. |
| `EmployeeNumber` | `String` | no |  | unique, max length 10 | The human readable employee number of the person. |
| `FirstName` | `String` | no |  | max length 35 | The first name of the person. |
| `LastName` | `String` | no |  | max length 35 | The last name of the person. |
| `PhoneNumber` | `String` | no |  | max length 80 | The phone number of the person. |
| `PrivatePhoneNumber` | `String` | no |  | max length 80, since 23.7 | The private phone number of the person. |
| `CellPhoneNumber` | `String` | no |  | max length 80 | The cell phone number of the person. |
| `PrivateCellPhoneNumber` | `String` | no |  | max length 80, since 23.7 | The private cell phone number of the person. |
| `InternalPhoneNumber` | `String` | no |  | max length 80, since 2.43 | The internal phone number of the person. |
| `EmailAddress` | `String` | no |  | max length 80 | The email address of the person. |
| `PrivateEmailAddress` | `String` | no |  | max length 80, since 23.7 | The private email address of the person. |
| `SkypeId` | `String` | no |  | max length 35 | The Skype identifier of the person. |
| `FaxNumber` | `String` | no |  |  | The fax number of the person. |
| `Position` | `String` | no |  | max length 80 | The position of the person. |
| `IsReference` | `Boolean` | no |  |  | Specifies if the person is a reference. |
| `IsPurchaseManager` | `Boolean` | no |  |  | Specifies if the person is a purchase manager. |
| `IsPlanner` | `Boolean` | no |  |  | Specififes if the person is a planner. |
| `IsAccountManager` | `Boolean` | no |  |  | Specifies if the person is an account manager. |
| `Contact` | `String` | no |  | max length 80 | The name of the person's contact. |
| `ContactPhoneNumber` | `String` | no |  | max length 80 | The phone number of the person's contact. |
| `ContactCellPhoneNumber` | `String` | no |  | max length 80 | The cell phone number of the person's contact. |
| `ContactEmailAddress` | `String` | no |  | max length 80 | The email address of the person's contact. |
| `AddressId` | `Int64?` | yes | [Addresses](Address.md) |  | The business key identifier of the person's address. References Addresses . |
| `Address` | `Addresses` | no | [Addresses](Address.md) | expandable | The address of the person. |
| `CommentId` | `Int64?` | yes | [Comments](Comment.md) |  | The business key identifier of the person's comment. Reference Comments . |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The comment of the person. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |  | The date that the person starts being blocked from. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |  | The date that the person stops being blocked. |
| `IsPersonBlocked` | `Boolean` | no |  |  | Specifies if the person is blocked. |
| `PersonBlockedById` | `Int64?` | yes |  |  | Specifies the application user that blocked the person. |
| `PersonBlockedDate` | `DateTimeOffset?` | yes |  |  | The date when the person was blocked. |
| `CanAuthorize` | `Boolean` | no |  |  | Specifies if the person can authorize invoices provided that EIM is not enabled for this MONITOR system. |
| `ApplicationUserId` | `Int64?` | yes | [ApplicationUsers](ApplicationUser.md) |  | The business key identifier of the application user that is coupled to the person. References ApplicationUsers . |
| `IsSeller` | `Boolean` | no |  |  | Specifies if the person is a seller. |
| `Initials` | `String` | no |  | max length 5, since 2.43 | Max length 5 |
| `DepartmentId` | `Int64` | no | [Departments](Department.md) | since 2.43 | The business key identifier of the department that the person belongs to. References Departments . |
| `DistrictId` | `Int64?` | yes | [CustomerDistricts](../Sales/CustomerDistrict.md) | since 2.43 | The business key identifier of the district that the person belongs to. References CustomerDistricts . |
| `LanguageId` | `Int64` | no | [LanguageCodes](LanguageCode.md) |  | The business key identifier of the person's preferred language. References LanguageCodes . |
| `WarehouseId` | `Int64` | no | [Warehouses](Warehouse.md) |  | The business key identifier of the person's default warehouse. References Warehouses . |
| `Category` | `String` | no |  | max length 15 | The category of the person. |
| `IdentityNumber` | `String` | no |  | max length 16, since 2.43 | The identity number of the person. |
| `GroupSettingsId` | `Int64?` | yes |  |  | The business key identifier of the person's attendance group settings. References AttendanceGroupSettings. |
| `UseWorkCenterManufacturingPrintSettings` | `Boolean` | no |  | since 2.28 | Specifies if manufacturing order document settings should come from the work center's settings or the person's settings. |
| `ManufacturingPrintSettings` | `PersonManufacturingPrintSettings[]` | no | [PersonManufacturingPrintSettings](PersonManufacturingPrintSettings.md) | expandable, collection, since 2.28 | The person's print settings for manufacturing order documents. |
| `PlannedAbsences` | `PlannedAbsences[]` | no | [PlannedAbsences](../TimeRecording/PlannedAbsence.md) | expandable, collection, since 2.47 | The planned absences for the person. |
| `TimeBanks` | `PersonTimeBanks[]` | no | [PersonTimeBanks](../TimeRecording/PersonTimeBank.md) | expandable, collection, since 22.3 | The time banks for the person. |
| `Relatives` | `PersonRelatives[]` | no | [PersonRelatives](PersonRelative.md) | expandable, collection, since 22.3 | The relatives of the person. |
| `EmploymentPeriods` | `EmploymentPeriods[]` | no | [EmploymentPeriods](EmploymentPeriod.md) | expandable, collection, since 22.3 | The employment periods that belong to the personnel record. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](ExtraField.md) | expandable, collection, since 22.3 | The extra fields of the personnel record. |
| `IsProjectManager` | `Boolean` | no |  | since 23.3 | Specifies if the person is a project manager. |
| `AvailableWorkshopSchedules` | `Schedules[]` | no | [Schedules](../TimeRecording/Schedule.md) | expandable, collection, since 24.3 | The workshop schedules of the personnel record. |
| `AvailableWorkCenters` | `PersonWorkCenters[]` | no | [PersonWorkCenters](../TimeRecording/PersonWorkCenter.md) | expandable, collection, since 24.3 | Specifies which work centers (and thereby which report numbers) the person should be allowed to select among in the priority plan and when starting work via report numbers. |
| `Signature` | `BlobData` | no | [BlobData](BlobData.md) | expandable, since 24.5 | The entity signature blob data |
| `EmployeeRecordingType` | `Int32` | no |  | bitmask, enum, since 24.5 | The employee recording type of the person. |
| `ScheduleManagementType` | `Int32` | no |  | bitmask, enum, since 24.5 | The schedule management type of the person. |
| `PersonScheduleCycles` | `PersonScheduleCycles[]` | no |  | expandable, collection, since 24.5 | The schedule cycles of the personnel record. |
| `AttendanceRecordingAuthorizers` | `AttendanceRecordingAuthorizers[]` | no |  | expandable, collection, since 24.5 | The attendance recording authorizers of the personnel record. |
| `WorkMethod` | `Int32` | no |  | enum, since 24.9 | The work method of the person. |

## Enumerations

### BlockedContextType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `RegisterCustomerOrder` | 1 |

### EmployeeRecordingType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `AttendanceAndWork` | 1 |
| `OnlyWork` | 2 |

### ScheduleManagementType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `ScheduleCycle` | 1 |

### WorkMethod

| Name | Value |
| --- | ---: |
| `OnlyChange` | 0 |
| `StartFinishAtWill` | 1 |


## Referenced by

**Common**

- [DelegatedWork](DelegatedWork.md) — `EmployeeId` (FK)
- [EmploymentPeriods](EmploymentPeriod.md) — `PersonId` (FK)
- [ProjectActivityCalendarAppointments](ProjectActivityCalendarAppointment.md) — `SenderPersonId` (FK)
- [Projects](Project.md) — `OurReference` (expand)
- [Projects](Project.md) — `OurReferenceId` (FK)
- [Projects](Project.md) — `ProjectManagerId` (FK)
- [Projects](Project.md) — `Seller` (expand)
- [Projects](Project.md) — `SellerId` (FK)

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `OurReferenceId` (FK)
- [PartPlanningInformation](../Inventory/PartPlanningInformation.md) — `ContactId` (FK)
- [PartTemplates](../Inventory/PartTemplate.md) — `PreparerId` (FK)
- [Parts](../Inventory/Part.md) — `Preparer` (expand)
- [Parts](../Inventory/Part.md) — `PreparerId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `CustomerOrderOurReferenceId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `InstalledBy` (FK)
- [QuantityChanges](../Inventory/QuantityChange.md) — `DeliveredByPersonId` (FK)
- [QuantityChanges](../Inventory/QuantityChange.md) — `PickingByPersonId` (FK)

**Manufacturing**

- [MaintenanceReportings](../Manufacturing/MaintenanceReporting.md) — `ReportedBy` (expand)
- [MaintenanceReportings](../Manufacturing/MaintenanceReporting.md) — `ReportedById` (FK)
- [ManufacturingOrderOperationReportings](../Manufacturing/ManufacturingOrderOperationReporting.md) — `EmployeeId` (FK)
- [ManufacturingOrderOperationReportings](../Manufacturing/ManufacturingOrderOperationReporting.md) — `ReportingEmployeeId` (FK)
- [ManufacturingPickingLists](../Manufacturing/ManufacturingPickingList.md) — `CreatedByPersonId` (FK)
- [ManufacturingPickingLists](../Manufacturing/ManufacturingPickingList.md) — `PrintedByPersonId` (FK)

**Purchase**

- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `OurReference` (expand)
- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `OurReferenceId` (FK)
- [Inquiries](../Purchase/Inquiry.md) — `BusinessContactReferenceId` (FK)
- [Inquiries](../Purchase/Inquiry.md) — `CreatedById` (FK)
- [Inquiries](../Purchase/Inquiry.md) — `OurReferenceId` (FK)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `OurReference` (expand)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `OurReferenceId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `AuthorizedSignerPerson` (expand)
- [Suppliers](../Purchase/Supplier.md) — `AuthorizedSignerPersonId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `PurchaseManager` (expand)
- [Suppliers](../Purchase/Supplier.md) — `PurchaseManagerId` (FK)

**Sales**

- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `OurReference` (expand)
- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `OurReferenceId` (FK)
- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `Seller` (expand)
- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `SellerId` (FK)
- [BusinessOpportunities](../Sales/BusinessOpportunity.md) — `OurReference` (expand)
- [BusinessOpportunities](../Sales/BusinessOpportunity.md) — `OurReferenceId` (FK)
- [BusinessOpportunities](../Sales/BusinessOpportunity.md) — `Seller` (expand)
- [BusinessOpportunities](../Sales/BusinessOpportunity.md) — `SellerId` (FK)
- [BusinessOpportunityActivities](../Sales/BusinessOpportunityActivity.md) — `ReferenceId` (FK)
- [BusinessOpportunitySalesProcessSteps](../Sales/BusinessOpportunitySalesProcessStep.md) — `ResponsibleSellerId` (FK)
- [BusinessOpportunityTypes](../Sales/BusinessOpportunityType.md) — `ResponsibleSeller` (expand)
- [BusinessOpportunityTypes](../Sales/BusinessOpportunityType.md) — `ResponsibleSellerId` (FK)
- [CreateSalesPickingList](../Sales/CreateSalesPickingList.md) — `CreatedByPersonId` (FK)
- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `OurReferenceId` (FK)
- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `SellerId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `OurReferenceId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `SellerId` (FK)
- [Customers](../Sales/Customer.md) — `AccountManager` (expand)
- [Customers](../Sales/Customer.md) — `AccountManagerId` (FK)
- [Customers](../Sales/Customer.md) — `ResellerId` (FK)
- [Customers](../Sales/Customer.md) — `Seller` (expand)
- [Customers](../Sales/Customer.md) — `SellerId` (FK)
- [Quotes](../Sales/Quote.md) — `OurReferenceId` (FK)
- [Quotes](../Sales/Quote.md) — `SellerId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `OurReferenceId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `ResponsibleId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `SellerId` (FK)
- [SalesPickingLists](../Sales/SalesPickingList.md) — `PrintedByPersonId` (FK)
- [SalesProcessTemplateRows](../Sales/SalesProcessTemplateRow.md) — `ResponsibleSeller` (expand)
- [SalesProcessTemplateRows](../Sales/SalesProcessTemplateRow.md) — `ResponsibleSellerId` (FK)
- [ShipmentCustoms](../Sales/ShipmentCustoms.md) — `Declarant` (expand)
- [ShipmentCustoms](../Sales/ShipmentCustoms.md) — `DeclarantId` (FK)

**TimeRecording**

- [AttendanceChart](../TimeRecording/AttendanceChart.md) — `EmployeeId` (FK)
- [PersonTimeBanks](../TimeRecording/PersonTimeBank.md) — `PersonId` (FK)
- [PersonWorkCenters](../TimeRecording/PersonWorkCenter.md) — `PersonId` (FK)
- [RecordingDays](../TimeRecording/RecordingDay.md) — `PersonId` (FK)
- [StandbyWorks](../TimeRecording/StandbyWork.md) — `EmployeeId` (FK)
- [WorkIntervals](../TimeRecording/WorkInterval.md) — `ReportingEmployeeId` (FK)


## Example

```json
{
  "SignatureId": null,
  "Id": 0,
  "BlockedContextType": 0,
  "IsRecordingEmployee": false,
  "EmployeeNumber": null,
  "FirstName": null,
  "LastName": null,
  "PhoneNumber": null,
  "PrivatePhoneNumber": null,
  "CellPhoneNumber": null,
  "PrivateCellPhoneNumber": null,
  "InternalPhoneNumber": null,
  "EmailAddress": null,
  "PrivateEmailAddress": null,
  "SkypeId": null,
  "FaxNumber": null,
  "Position": null,
  "IsReference": false,
  "IsPurchaseManager": false,
  "IsPlanner": false,
  "IsAccountManager": false,
  "Contact": null,
  "ContactPhoneNumber": null,
  "ContactCellPhoneNumber": null,
  "ContactEmailAddress": null,
  "AddressId": null,
  "Address": null,
  "CommentId": null,
  "Comment": null,
  "BlockedFromDate": null,
  "BlockedToDate": null,
  "IsPersonBlocked": false,
  "PersonBlockedById": null,
  "PersonBlockedDate": null,
  "CanAuthorize": false,
  "ApplicationUserId": null,
  "IsSeller": false,
  "Initials": null,
  "DepartmentId": 0,
  "DistrictId": null,
  "LanguageId": 0,
  "WarehouseId": 0,
  "Category": null,
  "IdentityNumber": null,
  "GroupSettingsId": null,
  "UseWorkCenterManufacturingPrintSettings": false,
  "ManufacturingPrintSettings": null,
  "PlannedAbsences": null,
  "TimeBanks": null,
  "Relatives": null,
  "EmploymentPeriods": null,
  "ExtraFields": null,
  "IsProjectManager": false,
  "AvailableWorkshopSchedules": null,
  "AvailableWorkCenters": null,
  "Signature": null,
  "EmployeeRecordingType": 0,
  "ScheduleManagementType": 0,
  "PersonScheduleCycles": null,
  "AttendanceRecordingAuthorizers": null,
  "WorkMethod": 0
}
```
