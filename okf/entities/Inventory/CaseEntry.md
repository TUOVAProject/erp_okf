---
type: API Entity
title: CaseEntry
description: Represents a case entry.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseEntry.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CaseEntry.html
  title: Monitor API — CaseEntry
module: Inventory
api_class: CaseEntry
doc_name: CaseEntry
endpoint: GET /api/v1/Inventory/CaseEntry
guid: B1A83C64-4AC0-41B3-89B2-6FDB7DD0E3BE
permission: Show case
introduced_in: '2.22'
property_count: 60
references_out:
- /entities/Accounting/AccountsReceivable.md
- /entities/Common/BusinessContactNoteHistory.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/Department.md
- /entities/Common/ExtraField.md
- /entities/Common/Person.md
- /entities/Common/Project.md
- /entities/Common/RejectionCodeItem.md
- /entities/Common/Revision.md
- /entities/Common/Warehouse.md
- /entities/Inventory/CaseEntryAdditionalCost.md
- /entities/Inventory/CaseEntryPhase.md
- /entities/Inventory/CaseManagementType.md
- /entities/Inventory/CasePartLink.md
- /entities/Inventory/Part.md
- /entities/Inventory/ProductRecord.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Manufacturing/WorkCenter.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
referenced_by:
- /entities/Inventory/CaseEntryActivity.md
- /entities/Inventory/CaseEntryAdditionalCost.md
- /entities/Inventory/CaseEntryLink.md
- /entities/Inventory/CaseEntryPhase.md
- /entities/Inventory/CasePartLink.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
---

# CaseEntry

Represents a case entry.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `CaseEntry`
- **Endpoint:** `GET /api/v1/Inventory/CaseEntry`
- **Required permission:** Show case
- **GUID:** `B1A83C64-4AC0-41B3-89B2-6FDB7DD0E3BE`
- **Introduced in:** 2.22

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case entry. |
| `Number` | `String` | no |  | unique, max length 20, since 2.36 | The human readable identifier of the case entry. |
| `ProjectId` | `Int64?` | yes | [Projects](/entities/Common/Project.md) | since 2.36 | The business key identifier of the project that belongs to the case entry. |
| `Project` | `Projects` | no | [Projects](/entities/Common/Project.md) | expandable, since 2.36 | The project that belongs to the case entry |
| `ContactCaseNumber` | `String` | no |  | unique, max length 40, since 2.36 | The customer's or the supplier's case number (depending on case type) |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](/entities/Sales/CustomerOrder.md) | since 2.36 | The business key identifier of the customer order that is linked to the case entry. |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](/entities/Sales/CustomerOrder.md) | expandable, since 2.36 | The customer order that is linked to the case entry. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) | since 2.36 | The business key identifier of the purchase order that is linked to the case entry. |
| `PurchaseOrder` | `PurchaseOrders` | no | [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) | expandable, since 2.36 | The purchase order that is linked to the case entry. |
| `ArrivalDate` | `DateTimeOffset?` | yes |  | since 2.36 | Date when delivery arrived. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  | since 2.36 | Date when delivery was made. |
| `DeliveredQuantity` | `Decimal?` | yes |  | since 2.36 | The quantity the delivery consisted of. |
| `ArrivedQuantity` | `Decimal?` | yes |  | since 2.36 | The quantity the arrival consisted of. |
| `ReasonSupplierId` | `Int64?` | yes | [Suppliers](/entities/Purchase/Supplier.md) | since 2.36 | The business key identifier of the supplier that caused the nonconformity. References Suppliers . |
| `ReasonWorkCenterId` | `Int64?` | yes | [WorkCenters](/entities/Manufacturing/WorkCenter.md) | since 2.36 | The business key identifier of the work center that caused the nonconformity. References WorkCenters . |
| `ReasonDepartmentId` | `Int64?` | yes | [Departments](/entities/Common/Department.md) | since 2.36 | The business key identifier of the department that caused the nonconformity. References Departments . |
| `ReasonRejectionCodeId` | `Int64?` | yes | [RejectionCodeItems](/entities/Common/RejectionCodeItem.md) | since 2.36 | The business key identifier of the rejection that caused the nonconformity. |
| `ReasonPartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) | since 2.36 | The business key identifier of the part that caused the nonconformity. |
| `InternalCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the case internal comment. |
| `InternalComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The internal comment of the case. |
| `ReasonCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) | since 2.36 | The business key identifier of the reason comment. |
| `ReasonComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable, since 2.36 | The reason comment of the case. |
| `ActualRejectionCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) | since 2.36 | The business key identifier of the actual rejections description. |
| `ActualRejectionComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable, since 2.36 | The actual rejections description. |
| `Status` | `Int32` | no |  | enum | The status of the case. |
| `CaseTypeId` | `Int64` | no | [CaseManagementType](/entities/Inventory/CaseManagementType.md) |  | The business key identifier of the case management type. |
| `CaseType` | `CaseManagementType` | no | [CaseManagementType](/entities/Inventory/CaseManagementType.md) | expandable | The case management type of the case. |
| `CaseDate` | `DateTimeOffset` | no |  |  | The case date of the case. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse where the case is registered. |
| `Warehouse` | `Warehouses` | no | [Warehouses](/entities/Common/Warehouse.md) | expandable | The warehouse of the case. |
| `CustomerId` | `Int64?` | yes | [Customers](/entities/Sales/Customer.md) |  | The business key identifier of the customer. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](/entities/Inventory/ProductRecord.md) |  | The business key identifier of the used product record for the case. |
| `ProductRecord` | `ProductRecords` | no | [ProductRecords](/entities/Inventory/ProductRecord.md) | expandable | The product record of the case. |
| `PartRevisionId` | `Int64?` | yes | [Revisions](/entities/Common/Revision.md) | since 24.5 | The business key identifier of the part revision used for the case. |
| `PartRevision` | `Revisions` | no | [Revisions](/entities/Common/Revision.md) | expandable, since 24.5 | The part revision of the case. |
| `PartId` | `Int64` | no | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the used part for the case. |
| `Part` | `Parts` | no | [Parts](/entities/Inventory/Part.md) | expandable | The part of the case. |
| `ManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) |  | The business key identifier of the manufacturing order. |
| `ManufacturingOrder` | `ManufacturingOrders` | no | [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) | expandable | The manufacturing order of the case. |
| `SupplierId` | `Int64` | no | [Suppliers](/entities/Purchase/Supplier.md) |  | The business key identifier of the supplier. |
| `ActualRejectionCodeId` | `Int64?` | yes | [RejectionCodeItems](/entities/Common/RejectionCodeItem.md) |  | The business key identifier of the actual rejection code for the case. |
| `ActualRejectionCode` | `RejectionCodeItems` | no | [RejectionCodeItems](/entities/Common/RejectionCodeItem.md) | expandable | The actual rejection code for the case. |
| `RejectionCodeItemId` | `Int64` | no | [RejectionCodeItems](/entities/Common/RejectionCodeItem.md) |  | The business key identifier of the planned rejection code item for the case. |
| `RejectionCodeItem` | `RejectionCodeItems` | no | [RejectionCodeItems](/entities/Common/RejectionCodeItem.md) | expandable | The rejection code item of the case. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](/entities/Common/ExtraField.md) | expandable, collection | A collection of extra field values for the case. |
| `Costs` | `CaseEntryAdditionalCost[]` | no | [CaseEntryAdditionalCost](/entities/Inventory/CaseEntryAdditionalCost.md) | expandable, collection, since 2.26 | A collection of case entry additional cost values for the case. |
| `OurReferenceId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) | since 2.36 | The business key identifier of our reference for the case entry. Reference Persons |
| `OurReferenceName` | `String` | no |  | max length 80, since 2.36 | The name of our reference for the case entry. |
| `Phases` | `CaseEntryPhases[]` | no | [CaseEntryPhases](/entities/Inventory/CaseEntryPhase.md) | expandable, collection, since 2.45 | The phases that belong to the case entry |
| `RejectionDescription` | `String` | no |  | max length 400, since 2.45 | The rejection description of the case entry. |
| `Notes` | `BusinessContactNoteHistories[]` | no | [BusinessContactNoteHistories](/entities/Common/BusinessContactNoteHistory.md) | expandable, collection, since 2.55 | Rows of business contact notes. |
| `ContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) | since 2.54 | The business key identifier of business contact reference. |
| `ContactName` | `String` | no |  | max length 80, since 2.54 | The customer's or supplier's reference name. Only set when ContactReferenceId is not set. |
| `AccountReciveableId` | `Int64?` | yes | [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) | since 2.54 | The business key identifier of the accounts receiveable. |
| `AccountsReceivable` | `AccountsReceivables` | no | [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) | expandable, since 2.54 | The accounts receiveable that is linked on the case entry |
| `CategoryString` | `String` | no |  | max length 20, since 2.54 | Category string. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) | since 23.2 | The business key identifier of the case entry external comment. |
| `ExternalComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable, since 23.2 | The case entry external comment. |
| `RejectedQuantity` | `Decimal` | no |  | since 24.3 | The case entry rejected quantity. |
| `CasePartLinks` | `CaseEntryPartLinks[]` | no | [CaseEntryPartLinks](/entities/Inventory/CasePartLink.md) | expandable, collection, since 24.5 | Case part links that reference the parts included in this case. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `Printed` | 2 |
| `Started` | 3 |
| `Finished` | 4 |
| `History` | 9 |
| `Rejected` | 99 |


## Referenced by

**Inventory**

- [CaseEntryActivities](/entities/Inventory/CaseEntryActivity.md) — `CaseEntryId` (FK)
- [CaseEntryAdditionalCost](/entities/Inventory/CaseEntryAdditionalCost.md) — `CaseEntryId` (FK)
- [CaseEntryLinks](/entities/Inventory/CaseEntryLink.md) — `ChildId` (FK)
- [CaseEntryLinks](/entities/Inventory/CaseEntryLink.md) — `ParentId` (FK)
- [CaseEntryPartLinks](/entities/Inventory/CasePartLink.md) — `CaseId` (FK)
- [CaseEntryPhases](/entities/Inventory/CaseEntryPhase.md) — `ParentId` (FK)

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `CaseEntries` (expand)

**Sales**

- [Customers](/entities/Sales/Customer.md) — `CaseEntries` (expand)


## Example

```json
{
  "Id": 0,
  "Number": null,
  "ProjectId": null,
  "Project": null,
  "ContactCaseNumber": null,
  "CustomerOrderId": null,
  "CustomerOrder": null,
  "PurchaseOrderId": null,
  "PurchaseOrder": null,
  "ArrivalDate": null,
  "DeliveryDate": null,
  "DeliveredQuantity": null,
  "ArrivedQuantity": null,
  "ReasonSupplierId": null,
  "ReasonWorkCenterId": null,
  "ReasonDepartmentId": null,
  "ReasonRejectionCodeId": null,
  "ReasonPartId": null,
  "InternalCommentId": null,
  "InternalComment": null,
  "ReasonCommentId": null,
  "ReasonComment": null,
  "ActualRejectionCommentId": null,
  "ActualRejectionComment": null,
  "Status": 0,
  "CaseTypeId": 0,
  "CaseType": null,
  "CaseDate": "0001-01-01T00:00:00+00:00",
  "WarehouseId": 0,
  "Warehouse": null,
  "CustomerId": null,
  "ProductRecordId": null,
  "ProductRecord": null,
  "PartRevisionId": null,
  "PartRevision": null,
  "PartId": 0,
  "Part": null,
  "ManufacturingOrderId": null,
  "ManufacturingOrder": null,
  "SupplierId": 0,
  "ActualRejectionCodeId": null,
  "ActualRejectionCode": null,
  "RejectionCodeItemId": 0,
  "RejectionCodeItem": null,
  "ExtraFields": null,
  "Costs": null,
  "OurReferenceId": null,
  "OurReferenceName": null,
  "Phases": null,
  "RejectionDescription": null,
  "Notes": null,
  "ContactReferenceId": null,
  "ContactName": null,
  "AccountReciveableId": null,
  "AccountsReceivable": null,
  "CategoryString": null,
  "ExternalCommentId": null,
  "ExternalComment": null,
  "RejectedQuantity": 0.0,
  "CasePartLinks": null
}
```
