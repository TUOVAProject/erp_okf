---
type: API Entity
title: ProductRecords
description: Represents a product record.
resource: https://api.monitor.se/api/Monitor.API.Inventory.ProductRecord.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.ProductRecord.html
  title: Monitor API — ProductRecord
module: Inventory
api_class: ProductRecord
doc_name: ProductRecords
endpoint: GET /api/v1/Inventory/ProductRecords
guid: 3e3bfb7c-bb0c-495b-b88d-e1efa1f50368
permission: Show serial number
introduced_in: '2.18'
property_count: 62
references_out:
- /entities/Common/Address.md
- /entities/Common/ApplicationUser.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/DeliveryAddress.md
- /entities/Common/ExtraField.md
- /entities/Common/Person.md
- /entities/Common/Revision.md
- /entities/Inventory/Part.md
- /entities/Inventory/ProductRecordOperationReporting.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderDeliveryRow.md
referenced_by:
- /entities/Inventory/AdditionalIdsRecord.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CasePartLink.md
- /entities/Inventory/PartLocationProductRecord.md
- /entities/Inventory/PhysicalInventoryRow.md
- /entities/Inventory/ProductRecordOperationReporting.md
- /entities/Inventory/StockBalanceChange.md
- /entities/Inventory/StockTransaction.md
- /entities/Manufacturing/MaintenanceReporting.md
- /entities/Manufacturing/MaintenanceReportingRow.md
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/PackageRowPartLocation.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/SalesPickingListRowQuantity.md
---

# ProductRecords

Represents a product record.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `ProductRecord`
- **Endpoint:** `GET /api/v1/Inventory/ProductRecords`
- **Required permission:** Show serial number
- **GUID:** `3e3bfb7c-bb0c-495b-b88d-e1efa1f50368`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the product record. |
| `ProductRecordType` | `Int32` | no |  | enum | The type of the product record. |
| `SerialNumberWithPartNumber` | `String` | no |  |  | The batch or serial number along with the part number of the product record. |
| `CommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the product record's comment. |
| `Comment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The product record comment. |
| `CertificateId` | `Int64?` | yes | [Comments](../Common/Comment.md) | since 2.24 | The business key identifier of the product record's certificate. |
| `Certificate` | `Comments` | no | [Comments](../Common/Comment.md) | expandable, since 2.24 | The certificate of the product record. |
| `WarrantyCommitmentId` | `Int64?` | yes | [Comments](../Common/Comment.md) | since 2.24 | The business key identifier of the product record's warranty commitment. |
| `WarrantyCommitment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable, since 2.24 | The warranty commitment of the product record. |
| `InstallationCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) | since 2.24 | The business key identifier of the product record's installation comment. |
| `InstallationComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable, since 2.24 | The installation comment of the product record. |
| `SerialNumber` | `String` | no |  |  | The batch or serial number of the product record. |
| `ChargeNumber` | `String` | no |  |  | The charge number of the product record. |
| `PartId` | `Int64` | no | [Parts](Part.md) |  | The business key identifier of the part that the product record belongs to. |
| `Part` | `Parts` | no | [Parts](Part.md) | expandable | The part that the product record belongs to. |
| `ManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](../Manufacturing/ManufacturingOrder.md) |  | The business key identifier of the manufacturing order that the product record is linked to. |
| `ManufacturingOrder` | `ManufacturingOrders` | no | [ManufacturingOrders](../Manufacturing/ManufacturingOrder.md) | expandable | The manufacturing order that the product record is linked to. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](../Common/ExtraField.md) | expandable, collection | A collection of extra field values for the product record. |
| `HasWarranty` | `Boolean` | no |  | since 2.36 | Specifies if the product is covered by warranty. |
| `WarrantyStartDate` | `DateTimeOffset?` | yes |  | since 2.36 | The date when the warranty started. |
| `WarrantyEndDate` | `DateTimeOffset?` | yes |  | since 2.36 | The date when the warranty expires. |
| `WarrantyMonths` | `Int32` | no |  | since 2.36 | The length of the warranty period in months. |
| `OwnerId` | `Int64?` | yes | [Customers](../Sales/Customer.md) | since 2.40 | The business key identifier of the product record owner. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](../Sales/CustomerOrder.md) | since 2.40 | The business key identifier of the customer order of the product record. |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](../Sales/CustomerOrder.md) | expandable, since 2.40 | The customer order of the product record. |
| `CustomerOrderDeliveryRowId` | `Int64?` | yes | [CustomerOrderDeliveryRows](../Sales/CustomerOrderDeliveryRow.md) | since 2.40 | The business key identifier of the customer order delivery row of the product record. |
| `CustomerOrderDeliveryRow` | `CustomerOrderDeliveryRows` | no | [CustomerOrderDeliveryRows](../Sales/CustomerOrderDeliveryRow.md) | expandable, since 2.40 | The customer order of the product record. |
| `DeliveryAddressId` | `Int64?` | yes | [DeliveryAddresses](../Common/DeliveryAddress.md) | since 2.40 | The business key identifier of the delivery address of the product record. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable, since 2.40 | The delivery address of the product record. |
| `BlockMessageId` | `Int64?` | yes | [Comments](../Common/Comment.md) | since 2.45 | The business key identifier of the message for the life cycle state of the product record. |
| `BlockMessage` | `Comments` | no | [Comments](../Common/Comment.md) | expandable, since 2.45 | The message for the life cycle state of the product record. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](../Common/ApplicationUser.md) | since 2.45 | The identifier of the application user that has set the product record to blocked or message. |
| `LifeCycleState` | `Int32` | no |  | enum, since 2.45 | The life cycle state of the product record. |
| `BlockContext` | `Int32` | no |  | bitmask, enum, since 2.45 | The block context which the product records life cycle state is used for. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  | since 2.45 | The date from which the product record has been blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  | since 2.45 | The date from which the product record has been unblocked. |
| `MeasurementSetting` | `Decimal?` | yes |  | since 2.49 | The measurement setting for a product record. |
| `OperationTime` | `TimeSpan?` | yes |  | since 2.49 | The operation time for a product record. |
| `NumberOfCycles` | `Decimal?` | yes |  | since 2.49 | The number of cycles for a product record. |
| `OperationReportings` | `ProductRecordOperationReportings[]` | no | [ProductRecordOperationReportings](ProductRecordOperationReporting.md) | expandable, collection, since 2.49 | The list of product record operation reporting logs. |
| `CustomerOrderOurReferenceId` | `Int64?` | yes | [Persons](../Common/Person.md) | since 2.51 | The business key identifier of the customer order our reference person of the product record. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](../Common/BusinessContactReference.md) | since 2.51 | The business key identifier of the customer's reference of the product record. |
| `CustomerOrderPartRevisionId` | `Int64?` | yes | [Revisions](../Common/Revision.md) | **deprecated since 24.1**, since 2.51 | The business key identifier of the revision for the part of the product record. Has been replaced by the more general PartRevisionId _(Replaced by PartRevisionId)_ |
| `PartRevisionId` | `Int64?` | yes | [Revisions](../Common/Revision.md) | since 24.1 | The business key identifier of the revision for the part of the product record. |
| `PlannedDeliveryDate` | `DateTimeOffset?` | yes |  | since 2.51 | The planned delivery date for the customer order of the product record. |
| `ActualDeliveryDate` | `DateTimeOffset?` | yes |  | since 2.51 | The actual delivery date for the customer order of the product record. |
| `MeasurementSettingWarranty` | `Decimal?` | yes |  | since 2.51 | The meter reading for warranty of the product record. |
| `OperationTimeWarranty` | `TimeSpan?` | yes |  | since 2.51 | The operation time for warranty of the product record. |
| `NumberOfCyclesWarranty` | `Decimal?` | yes |  | since 2.51 | The number of cycles for warranty of the product record. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](../Purchase/PurchaseOrder.md) | since 2.51 | The business key identifier of the purchase order of the product record. |
| `ActualArrivalDate` | `DateTimeOffset?` | yes |  | since 2.51 | The actual delivery date for the purchase order of the product record. |
| `ManufactureDate` | `DateTimeOffset?` | yes |  | since 2.51 | The finish date for the manufacturing order of the product record. |
| `InstallationOrderId` | `Int64?` | yes | [CustomerOrders](../Sales/CustomerOrder.md) | since 2.51 | The business key identifier of the customer order which the installation is linked to. |
| `InstalledBy` | `Int64?` | yes | [Persons](../Common/Person.md) | since 2.51 | The business key identifier of the person that is linked to the installation of the product record. |
| `InstallationDate` | `DateTimeOffset?` | yes |  | since 2.51 | The date when the installation of the product record will take place. |
| `InstallationCode` | `String` | no |  | since 2.51 | The code that is applying to the installation of the product record. |
| `WarrantyCode` | `String` | no |  | since 2.51 | The code that is applying to the installation of the product record. |
| `RegistrationNo` | `String` | no |  | since 2.51 | The registration number for the manufacturing order of the product record. |
| `TypeDescription` | `String` | no |  | since 2.51 | The type description for the customer order of the product record. |
| `Status` | `Int32` | no |  | enum, since 22.6 | The status of the product record. |
| `BestBeforeDate` | `DateTimeOffset?` | yes |  | since 22.7 | The best before date of the product record. |
| `ProductRecordBatchId` | `Int64?` | yes |  | since 23.3 | The business key identifier of the batch number. |

## Enumerations

### ProductRecordType

| Name | Value |
| --- | ---: |
| `ProductRecord` | 0 |
| `Batch` | 1 |

### LifeCycleState

| Name | Value |
| --- | ---: |
| `ApprovalForUse` | 0 |
| `NonApproval` | 1 |
| `ServicePastDue` | 2 |
| `UnderServiceOrCalibration` | 3 |
| `Rejected` | 4 |
| `ServiceOrCalibrationBeforeUse` | 5 |
| `Missing` | 6 |
| `Scrapped` | 7 |

### BlockContext (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `ManufacturingOrderWithdrawal` | 1 |
| `ManufacturingOrderClearance` | 2 |
| `CustomerOrderDelivery` | 4 |
| `CustomerOrderClearance` | 8 |
| `RequirementCalculation` | 16 |

### Status

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `Registrered` | 1 |
| `Manufacturing` | 2 |
| `ManufacturingPending` | 3 |
| `Inventory` | 4 |
| `Blocked` | 5 |
| `Packed` | 6 |
| `PackedAndMarked` | 7 |
| `Historical` | 9 |


## Referenced by

**Inventory**

- [AdditionalIDsRecords](AdditionalIdsRecord.md) — `ProductRecordId` (FK)
- [CaseEntry](CaseEntry.md) — `ProductRecord` (expand)
- [CaseEntry](CaseEntry.md) — `ProductRecordId` (FK)
- [CaseEntryPartLinks](CasePartLink.md) — `ProductRecordBatchId` (FK)
- [CaseEntryPartLinks](CasePartLink.md) — `ProductRecordId` (FK)
- [PartLocationProductRecords](PartLocationProductRecord.md) — `ProductRecordId` (FK)
- [PhysicalInventoryRows](PhysicalInventoryRow.md) — `ProductRecordId` (FK)
- [ProductRecordOperationReportings](ProductRecordOperationReporting.md) — `ProductRecordId` (FK)
- [StockBalanceChanges](StockBalanceChange.md) — `ProductRecordId` (FK)
- [StockTransactions](StockTransaction.md) — `ProductRecordId` (FK)

**Manufacturing**

- [MaintenanceReportingRows](../Manufacturing/MaintenanceReportingRow.md) — `MasterToolProductRecordId` (FK)
- [MaintenanceReportings](../Manufacturing/MaintenanceReporting.md) — `ProductRecord` (expand)
- [ManufacturingOrderNodes](../Manufacturing/ManufacturingOrderNode.md) — `SerialNumberProductRecords` (expand)

**Sales**

- [CustomerOrders](../Sales/CustomerOrder.md) — `AftermarketProductRecordId` (FK)
- [PackageRowPartLocations](../Sales/PackageRowPartLocation.md) — `ProductRecordId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `AftermarketProductRecordId` (FK)
- [SalesPickingListRowQuantities](../Sales/SalesPickingListRowQuantity.md) — `ProductRecordId` (FK)


## Example

```json
{
  "Id": 0,
  "ProductRecordType": 0,
  "SerialNumberWithPartNumber": null,
  "CommentId": null,
  "Comment": null,
  "CertificateId": null,
  "Certificate": null,
  "WarrantyCommitmentId": null,
  "WarrantyCommitment": null,
  "InstallationCommentId": null,
  "InstallationComment": null,
  "SerialNumber": null,
  "ChargeNumber": null,
  "PartId": 0,
  "Part": null,
  "ManufacturingOrderId": null,
  "ManufacturingOrder": null,
  "ExtraFields": null,
  "HasWarranty": false,
  "WarrantyStartDate": null,
  "WarrantyEndDate": null,
  "WarrantyMonths": 0,
  "OwnerId": null,
  "CustomerOrderId": null,
  "CustomerOrder": null,
  "CustomerOrderDeliveryRowId": null,
  "CustomerOrderDeliveryRow": null,
  "DeliveryAddressId": null,
  "DeliveryAddress": null,
  "BlockMessageId": null,
  "BlockMessage": null,
  "BlockedById": null,
  "LifeCycleState": 0,
  "BlockContext": 0,
  "BlockedFromDate": null,
  "BlockedToDate": null,
  "MeasurementSetting": null,
  "OperationTime": null,
  "NumberOfCycles": null,
  "OperationReportings": null,
  "CustomerOrderOurReferenceId": null,
  "BusinessContactReferenceId": null,
  "CustomerOrderPartRevisionId": null,
  "PartRevisionId": null,
  "PlannedDeliveryDate": null,
  "ActualDeliveryDate": null,
  "MeasurementSettingWarranty": null,
  "OperationTimeWarranty": null,
  "NumberOfCyclesWarranty": null,
  "PurchaseOrderId": null,
  "ActualArrivalDate": null,
  "ManufactureDate": null,
  "InstallationOrderId": null,
  "InstalledBy": null,
  "InstallationDate": null,
  "InstallationCode": null,
  "WarrantyCode": null,
  "RegistrationNo": null,
  "TypeDescription": null,
  "Status": 0,
  "BestBeforeDate": null,
  "ProductRecordBatchId": null
}
```
