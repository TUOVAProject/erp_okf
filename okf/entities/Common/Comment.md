---
type: API Entity
title: Comments
description: Represents a comment, containing both raw and HTML formatted text.
resource: https://api.monitor.se/api/Monitor.API.Common.Comment.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Comment.html
  title: Monitor API — Comment
module: Common
api_class: Comment
doc_name: Comments
endpoint: GET /api/v1/Common/Comments
guid: FA8BCB02-98C2-49E5-B03C-07B6FAD90786
introduced_in: '2.18'
property_count: 5
references_out:
- /entities/Common/FileLink.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/AccountsReceivable.md
- /entities/Accounting/AccrualAccounting.md
- /entities/Accounting/FixedAssetSale.md
- /entities/Accounting/Voucher.md
- /entities/Common/BusinessContactNoteHistory.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/EmploymentPeriod.md
- /entities/Common/ExtraField.md
- /entities/Common/FormTemplate.md
- /entities/Common/FormTemplateRow.md
- /entities/Common/FormTemplateSelectionRow.md
- /entities/Common/MonitoringTask.md
- /entities/Common/PartConfiguration.md
- /entities/Common/PartConfigurationTemplate.md
- /entities/Common/Person.md
- /entities/Common/Project.md
- /entities/Common/ProjectActivity.md
- /entities/Common/ProjectActivityType.md
- /entities/Common/ProjectCostBudget.md
- /entities/Common/ProjectCostForecast.md
- /entities/Common/ProjectCostReportingEntry.md
- /entities/Common/Revision.md
- /entities/Common/VatRate.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CaseEntryActivity.md
- /entities/Inventory/CaseManagementTemplateNode.md
- /entities/Inventory/Location.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartActivity.md
- /entities/Inventory/ProductRecord.md
- /entities/Manufacturing/DrawingRevision.md
- /entities/Manufacturing/MaintenanceReporting.md
- /entities/Manufacturing/MaintenanceReportingRow.md
- /entities/Manufacturing/MaintenanceReportingSelectionRow.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Manufacturing/ManufacturingOrderMaterial.md
- /entities/Manufacturing/ManufacturingOrderNodeDrawingRevision.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Manufacturing/ManufacturingOrderOperationReporting.md
- /entities/Manufacturing/MaterialRow.md
- /entities/Manufacturing/OperationRow.md
- /entities/Manufacturing/WorkCenter.md
- /entities/Purchase/BlanketOrderPurchase.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderInvoiceRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Purchase/Supplier.md
- /entities/Purchase/SupplierPartLink.md
- /entities/Sales/BlanketOrderSales.md
- /entities/Sales/BusinessOpportunity.md
- /entities/Sales/BusinessOpportunityActivity.md
- /entities/Sales/BusinessOpportunityActivityTemplateRow.md
- /entities/Sales/BusinessOpportunityReference.md
- /entities/Sales/BusinessOpportunityType.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerPartLink.md
- /entities/Sales/CustomerRelationshipManagementActivity.md
- /entities/Sales/PackageRow.md
- /entities/Sales/Quote.md
- /entities/Sales/QuoteActivity.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/SalesPrice.md
- /entities/TimeRecording/AdditionRecording.md
- /entities/TimeRecording/Schedule.md
- /entities/TimeRecording/WorkInterval.md
---

# Comments

Represents a comment, containing both raw and HTML formatted text.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `Comment`
- **Endpoint:** `GET /api/v1/Common/Comments`
- **GUID:** `FA8BCB02-98C2-49E5-B03C-07B6FAD90786`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the comment. |
| `Text` | `String` | no |  |  | The comment text with HTML formatting. |
| `RawText` | `String` | no |  |  | The comment text without HTML formatting. In MONITOR this is used exclusively for indexing purposes and is not shown anywhere in the system. |
| `HasFileLinks` | `Boolean` | no |  |  | Specifies if the comment has files linked to it. |
| `FileLinks` | `FileLink[]` | no | [FileLink](FileLink.md) | expandable, collection | A collection of all file links that belong to the comment. |

## Referenced by

**Accounting**

- [AccountsPayables](../Accounting/AccountsPayable.md) — `BlockMessage` (expand)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `BlockMessageId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `CancelComment` (expand)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `CancelCommentId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `Comment` (expand)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `CommentId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `CancelComment` (expand)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `CancelCommentId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `Comment` (expand)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `CommentId` (FK)
- [AccrualAccountings](../Accounting/AccrualAccounting.md) — `CancelComment` (expand)
- [AccrualAccountings](../Accounting/AccrualAccounting.md) — `CancelCommentId` (FK)
- [AccrualAccountings](../Accounting/AccrualAccounting.md) — `Comment` (expand)
- [AccrualAccountings](../Accounting/AccrualAccounting.md) — `CommentId` (FK)
- [FixedAssetSales](../Accounting/FixedAssetSale.md) — `Comment` (expand)
- [FixedAssetSales](../Accounting/FixedAssetSale.md) — `CommentId` (FK)
- [Vouchers](../Accounting/Voucher.md) — `Comment` (expand)
- [Vouchers](../Accounting/Voucher.md) — `CommentId` (FK)

**Common**

- [BusinessContactNoteHistories](BusinessContactNoteHistory.md) — `Body` (expand)
- [BusinessContactReferences](BusinessContactReference.md) — `Comment` (expand)
- [BusinessContactReferences](BusinessContactReference.md) — `CommentId` (FK)
- [EmploymentPeriods](EmploymentPeriod.md) — `Comment` (expand)
- [EmploymentPeriods](EmploymentPeriod.md) — `CommentId` (FK)
- [ExtraFields](ExtraField.md) — `Comment` (expand)
- [ExtraFields](ExtraField.md) — `CommentId` (FK)
- [FormTemplateRows](FormTemplateRow.md) — `Comment` (expand)
- [FormTemplateRows](FormTemplateRow.md) — `CommentId` (FK)
- [FormTemplateSelectionRows](FormTemplateSelectionRow.md) — `Comment` (expand)
- [FormTemplateSelectionRows](FormTemplateSelectionRow.md) — `CommentId` (FK)
- [FormTemplates](FormTemplate.md) — `Comment` (expand)
- [FormTemplates](FormTemplate.md) — `CommentId` (FK)
- [MonitoringTasks](MonitoringTask.md) — `Comment` (expand)
- [MonitoringTasks](MonitoringTask.md) — `CommentId` (FK)
- [PartConfigurationTemplates](PartConfigurationTemplate.md) — `Comment` (expand)
- [PartConfigurationTemplates](PartConfigurationTemplate.md) — `CommentId` (FK)
- [PartConfigurations](PartConfiguration.md) — `Comment` (expand)
- [PartConfigurations](PartConfiguration.md) — `CommentId` (FK)
- [Persons](Person.md) — `Comment` (expand)
- [Persons](Person.md) — `CommentId` (FK)
- [ProjectActivities](ProjectActivity.md) — `Comment` (expand)
- [ProjectActivities](ProjectActivity.md) — `CommentId` (FK)
- [ProjectActivityTypes](ProjectActivityType.md) — `Comment` (expand)
- [ProjectActivityTypes](ProjectActivityType.md) — `CommentId` (FK)
- [ProjectCostBudgets](ProjectCostBudget.md) — `Comment` (expand)
- [ProjectCostBudgets](ProjectCostBudget.md) — `CommentId` (FK)
- [ProjectCostForecasts](ProjectCostForecast.md) — `Comment` (expand)
- [ProjectCostForecasts](ProjectCostForecast.md) — `CommentId` (FK)
- [ProjectCostReportingEntries](ProjectCostReportingEntry.md) — `Comment` (expand)
- [ProjectCostReportingEntries](ProjectCostReportingEntry.md) — `InternalComment` (expand)
- [Projects](Project.md) — `ExternalComment` (expand)
- [Projects](Project.md) — `ExternalCommentId` (FK)
- [Projects](Project.md) — `InternalComment` (expand)
- [Projects](Project.md) — `InternalCommentId` (FK)
- [Revisions](Revision.md) — `Comment` (expand)
- [Revisions](Revision.md) — `CommentId` (FK)
- [VatRates](VatRate.md) — `ReferenceText` (expand)
- [VatRates](VatRate.md) — `ReferenceTextId` (FK)

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `ActualRejectionComment` (expand)
- [CaseEntry](../Inventory/CaseEntry.md) — `ActualRejectionCommentId` (FK)
- [CaseEntry](../Inventory/CaseEntry.md) — `ExternalComment` (expand)
- [CaseEntry](../Inventory/CaseEntry.md) — `ExternalCommentId` (FK)
- [CaseEntry](../Inventory/CaseEntry.md) — `InternalComment` (expand)
- [CaseEntry](../Inventory/CaseEntry.md) — `InternalCommentId` (FK)
- [CaseEntry](../Inventory/CaseEntry.md) — `ReasonComment` (expand)
- [CaseEntry](../Inventory/CaseEntry.md) — `ReasonCommentId` (FK)
- [CaseEntryActivities](../Inventory/CaseEntryActivity.md) — `Comment` (expand)
- [CaseEntryActivities](../Inventory/CaseEntryActivity.md) — `CommentId` (FK)
- [CaseManagementTemplateNodes](../Inventory/CaseManagementTemplateNode.md) — `Comment` (expand)
- [CaseManagementTemplateNodes](../Inventory/CaseManagementTemplateNode.md) — `CommentId` (FK)
- [Locations](../Inventory/Location.md) — `BlockMessage` (expand)
- [Locations](../Inventory/Location.md) — `BlockMessageId` (FK)
- [Locations](../Inventory/Location.md) — `Comment` (expand)
- [Locations](../Inventory/Location.md) — `CommentId` (FK)
- [PartActivities](../Inventory/PartActivity.md) — `CommentId` (FK)
- [Parts](../Inventory/Part.md) — `BlockMessage` (expand)
- [Parts](../Inventory/Part.md) — `BlockMessageId` (FK)
- [Parts](../Inventory/Part.md) — `Comment` (expand)
- [Parts](../Inventory/Part.md) — `CommentId` (FK)
- [Parts](../Inventory/Part.md) — `ManufacturingComment` (expand)
- [Parts](../Inventory/Part.md) — `ManufacturingCommentId` (FK)
- [Parts](../Inventory/Part.md) — `PickingInstruction` (expand)
- [Parts](../Inventory/Part.md) — `PickingInstructionId` (FK)
- [Parts](../Inventory/Part.md) — `PurchaseComment` (expand)
- [Parts](../Inventory/Part.md) — `PurchaseCommentId` (FK)
- [Parts](../Inventory/Part.md) — `ReceivingInstruction` (expand)
- [Parts](../Inventory/Part.md) — `ReceivingInstructionId` (FK)
- [Parts](../Inventory/Part.md) — `SalesComment` (expand)
- [Parts](../Inventory/Part.md) — `SalesCommentId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `BlockMessage` (expand)
- [ProductRecords](../Inventory/ProductRecord.md) — `BlockMessageId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `Certificate` (expand)
- [ProductRecords](../Inventory/ProductRecord.md) — `CertificateId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `Comment` (expand)
- [ProductRecords](../Inventory/ProductRecord.md) — `CommentId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `InstallationComment` (expand)
- [ProductRecords](../Inventory/ProductRecord.md) — `InstallationCommentId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `WarrantyCommitment` (expand)
- [ProductRecords](../Inventory/ProductRecord.md) — `WarrantyCommitmentId` (FK)

**Manufacturing**

- [DrawingRevisions](../Manufacturing/DrawingRevision.md) — `RevisionComment` (expand)
- [DrawingRevisions](../Manufacturing/DrawingRevision.md) — `RevisionCommentId` (FK)
- [MaintenanceReportingRows](../Manufacturing/MaintenanceReportingRow.md) — `Comment` (expand)
- [MaintenanceReportingRows](../Manufacturing/MaintenanceReportingRow.md) — `CommentId` (FK)
- [MaintenanceReportingRows](../Manufacturing/MaintenanceReportingRow.md) — `Instruction` (expand)
- [MaintenanceReportingRows](../Manufacturing/MaintenanceReportingRow.md) — `InstructionId` (FK)
- [MaintenanceReportingSelectionRows](../Manufacturing/MaintenanceReportingSelectionRow.md) — `Comment` (expand)
- [MaintenanceReportingSelectionRows](../Manufacturing/MaintenanceReportingSelectionRow.md) — `CommentId` (FK)
- [MaintenanceReportings](../Manufacturing/MaintenanceReporting.md) — `Comment` (expand)
- [MaintenanceReportings](../Manufacturing/MaintenanceReporting.md) — `CommentId` (FK)
- [MaintenanceReportings](../Manufacturing/MaintenanceReporting.md) — `Instruction` (expand)
- [ManufacturingOrderMaterials](../Manufacturing/ManufacturingOrderMaterial.md) — `InstructionComment` (expand)
- [ManufacturingOrderMaterials](../Manufacturing/ManufacturingOrderMaterial.md) — `InstructionCommentId` (FK)
- [ManufacturingOrderNodeDrawingRevisions](../Manufacturing/ManufacturingOrderNodeDrawingRevision.md) — `RevisionComment` (expand)
- [ManufacturingOrderNodeDrawingRevisions](../Manufacturing/ManufacturingOrderNodeDrawingRevision.md) — `RevisionCommentId` (FK)
- [ManufacturingOrderOperationReportings](../Manufacturing/ManufacturingOrderOperationReporting.md) — `Comment` (expand)
- [ManufacturingOrderOperationReportings](../Manufacturing/ManufacturingOrderOperationReporting.md) — `CommentId` (FK)
- [ManufacturingOrderOperations](../Manufacturing/ManufacturingOrderOperation.md) — `InstructionComment` (expand)
- [ManufacturingOrderOperations](../Manufacturing/ManufacturingOrderOperation.md) — `InstructionCommentId` (FK)
- [ManufacturingOrders](../Manufacturing/ManufacturingOrder.md) — `Comment` (expand)
- [ManufacturingOrders](../Manufacturing/ManufacturingOrder.md) — `CommentId` (FK)
- [MaterialRows](../Manufacturing/MaterialRow.md) — `Comment` (expand)
- [MaterialRows](../Manufacturing/MaterialRow.md) — `CommentId` (FK)
- [OperationRows](../Manufacturing/OperationRow.md) — `Comment` (expand)
- [OperationRows](../Manufacturing/OperationRow.md) — `CommentId` (FK)
- [WorkCenters](../Manufacturing/WorkCenter.md) — `Comment` (expand)
- [WorkCenters](../Manufacturing/WorkCenter.md) — `CommentId` (FK)

**Purchase**

- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `ExternalComment` (expand)
- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `ExternalCommentId` (FK)
- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `InternalComment` (expand)
- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `InternalCommentId` (FK)
- [Inquiries](../Purchase/Inquiry.md) — `ExternalComment` (expand)
- [Inquiries](../Purchase/Inquiry.md) — `ExternalCommentId` (FK)
- [Inquiries](../Purchase/Inquiry.md) — `InternalComment` (expand)
- [Inquiries](../Purchase/Inquiry.md) — `InternalCommentId` (FK)
- [PurchaseOrderInvoiceRows](../Purchase/PurchaseOrderInvoiceRow.md) — `Comment` (expand)
- [PurchaseOrderInvoiceRows](../Purchase/PurchaseOrderInvoiceRow.md) — `CommentId` (FK)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `DelayComment` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `DelayCommentId` (FK)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `ReceivingInspectionInstruction` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `ReceivingInspectionInstructionId` (FK)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `ReceivingMessage` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `ReceivingMessageId` (FK)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `ExternalComment` (expand)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `ExternalCommentId` (FK)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `InternalComment` (expand)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `InternalCommentId` (FK)
- [SupplierPartLinks](../Purchase/SupplierPartLink.md) — `OverridePurchaseComment` (expand)
- [SupplierPartLinks](../Purchase/SupplierPartLink.md) — `OverridePurchaseCommentId` (FK)
- [SupplierPartLinks](../Purchase/SupplierPartLink.md) — `PriceComment` (expand)
- [SupplierPartLinks](../Purchase/SupplierPartLink.md) — `PriceCommentId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `ArrivalReportingInstruction` (expand)
- [Suppliers](../Purchase/Supplier.md) — `ArrivalReportingInstructionId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `BlockMessage` (expand)
- [Suppliers](../Purchase/Supplier.md) — `BlockMessageId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `Comment` (expand)
- [Suppliers](../Purchase/Supplier.md) — `CommentId` (FK)

**Sales**

- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `ExternalComment` (expand)
- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `ExternalCommentId` (FK)
- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `InternalComment` (expand)
- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `InternalCommentId` (FK)
- [BusinessOpportunities](../Sales/BusinessOpportunity.md) — `Comment` (expand)
- [BusinessOpportunities](../Sales/BusinessOpportunity.md) — `CommentId` (FK)
- [BusinessOpportunities](../Sales/BusinessOpportunity.md) — `ReasonLostComment` (expand)
- [BusinessOpportunities](../Sales/BusinessOpportunity.md) — `ReasonLostCommentId` (FK)
- [BusinessOpportunityActivities](../Sales/BusinessOpportunityActivity.md) — `Comment` (expand)
- [BusinessOpportunityActivities](../Sales/BusinessOpportunityActivity.md) — `CommentId` (FK)
- [BusinessOpportunityActivityTemplateRows](../Sales/BusinessOpportunityActivityTemplateRow.md) — `Comment` (expand)
- [BusinessOpportunityActivityTemplateRows](../Sales/BusinessOpportunityActivityTemplateRow.md) — `CommentId` (FK)
- [BusinessOpportunityReferences](../Sales/BusinessOpportunityReference.md) — `Comment` (expand)
- [BusinessOpportunityReferences](../Sales/BusinessOpportunityReference.md) — `CommentId` (FK)
- [BusinessOpportunityTypes](../Sales/BusinessOpportunityType.md) — `Comment` (expand)
- [BusinessOpportunityTypes](../Sales/BusinessOpportunityType.md) — `CommentId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `ExternalComment` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `ExternalCommentId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `InternalComment` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `InternalCommentId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `PickInstruction` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `PickInstructionId` (FK)
- [CustomerPartLinks](../Sales/CustomerPartLink.md) — `OverrideSalesComment` (expand)
- [CustomerPartLinks](../Sales/CustomerPartLink.md) — `OverrideSalesCommentId` (FK)
- [CustomerPartLinks](../Sales/CustomerPartLink.md) — `PickingComment` (expand)
- [CustomerPartLinks](../Sales/CustomerPartLink.md) — `PickingCommentId` (FK)
- [CustomerPartLinks](../Sales/CustomerPartLink.md) — `PriceComment` (expand)
- [CustomerPartLinks](../Sales/CustomerPartLink.md) — `PriceCommentId` (FK)
- [CustomerRelationshipManagementActivities](../Sales/CustomerRelationshipManagementActivity.md) — `Comment` (expand)
- [CustomerRelationshipManagementActivities](../Sales/CustomerRelationshipManagementActivity.md) — `CommentId` (FK)
- [Customers](../Sales/Customer.md) — `BlockMessage` (expand)
- [Customers](../Sales/Customer.md) — `BlockMessageId` (FK)
- [Customers](../Sales/Customer.md) — `Comment` (expand)
- [Customers](../Sales/Customer.md) — `CommentId` (FK)
- [Customers](../Sales/Customer.md) — `PickingListComment` (expand)
- [Customers](../Sales/Customer.md) — `PickingListCommentId` (FK)
- [PackageRows](../Sales/PackageRow.md) — `ExternalComment` (expand)
- [PackageRows](../Sales/PackageRow.md) — `ExternalCommentId` (FK)
- [PackageRows](../Sales/PackageRow.md) — `InternalComment` (expand)
- [PackageRows](../Sales/PackageRow.md) — `InternalCommentId` (FK)
- [QuoteActivities](../Sales/QuoteActivity.md) — `Comment` (expand)
- [QuoteActivities](../Sales/QuoteActivity.md) — `CommentId` (FK)
- [Quotes](../Sales/Quote.md) — `ExternalComment` (expand)
- [Quotes](../Sales/Quote.md) — `ExternalCommentId` (FK)
- [Quotes](../Sales/Quote.md) — `InternalComment` (expand)
- [Quotes](../Sales/Quote.md) — `InternalCommentId` (FK)
- [Quotes](../Sales/Quote.md) — `ReasonLostComment` (expand)
- [Quotes](../Sales/Quote.md) — `ReasonLostCommentId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `ExternalComment` (expand)
- [SalesAgreements](../Sales/SalesAgreement.md) — `ExternalCommentId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `InternalComment` (expand)
- [SalesAgreements](../Sales/SalesAgreement.md) — `InternalCommentId` (FK)
- [SalesPrices](../Sales/SalesPrice.md) — `Comment` (expand)
- [SalesPrices](../Sales/SalesPrice.md) — `CommentId` (FK)

**TimeRecording**

- [AdditionRecordings](../TimeRecording/AdditionRecording.md) — `Comment` (expand)
- [Schedules](../TimeRecording/Schedule.md) — `BlockMessage` (expand)
- [Schedules](../TimeRecording/Schedule.md) — `BlockMessageId` (FK)
- [WorkIntervals](../TimeRecording/WorkInterval.md) — `Comment` (expand)
- [WorkIntervals](../TimeRecording/WorkInterval.md) — `CommentId` (FK)


## Example

```json
{
  "Id": 0,
  "Text": null,
  "RawText": null,
  "HasFileLinks": false,
  "FileLinks": null
}
```
