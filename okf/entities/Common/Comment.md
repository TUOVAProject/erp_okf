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

- **Module:** [Common](/modules/Common.md)
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
| `FileLinks` | `FileLink[]` | no | [FileLink](/entities/Common/FileLink.md) | expandable, collection | A collection of all file links that belong to the comment. |

## Referenced by

**Accounting**

- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `BlockMessage` (expand)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `BlockMessageId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `CancelComment` (expand)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `CancelCommentId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `Comment` (expand)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `CommentId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `CancelComment` (expand)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `CancelCommentId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `Comment` (expand)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `CommentId` (FK)
- [AccrualAccountings](/entities/Accounting/AccrualAccounting.md) — `CancelComment` (expand)
- [AccrualAccountings](/entities/Accounting/AccrualAccounting.md) — `CancelCommentId` (FK)
- [AccrualAccountings](/entities/Accounting/AccrualAccounting.md) — `Comment` (expand)
- [AccrualAccountings](/entities/Accounting/AccrualAccounting.md) — `CommentId` (FK)
- [FixedAssetSales](/entities/Accounting/FixedAssetSale.md) — `Comment` (expand)
- [FixedAssetSales](/entities/Accounting/FixedAssetSale.md) — `CommentId` (FK)
- [Vouchers](/entities/Accounting/Voucher.md) — `Comment` (expand)
- [Vouchers](/entities/Accounting/Voucher.md) — `CommentId` (FK)

**Common**

- [BusinessContactNoteHistories](/entities/Common/BusinessContactNoteHistory.md) — `Body` (expand)
- [BusinessContactReferences](/entities/Common/BusinessContactReference.md) — `Comment` (expand)
- [BusinessContactReferences](/entities/Common/BusinessContactReference.md) — `CommentId` (FK)
- [EmploymentPeriods](/entities/Common/EmploymentPeriod.md) — `Comment` (expand)
- [EmploymentPeriods](/entities/Common/EmploymentPeriod.md) — `CommentId` (FK)
- [ExtraFields](/entities/Common/ExtraField.md) — `Comment` (expand)
- [ExtraFields](/entities/Common/ExtraField.md) — `CommentId` (FK)
- [FormTemplateRows](/entities/Common/FormTemplateRow.md) — `Comment` (expand)
- [FormTemplateRows](/entities/Common/FormTemplateRow.md) — `CommentId` (FK)
- [FormTemplateSelectionRows](/entities/Common/FormTemplateSelectionRow.md) — `Comment` (expand)
- [FormTemplateSelectionRows](/entities/Common/FormTemplateSelectionRow.md) — `CommentId` (FK)
- [FormTemplates](/entities/Common/FormTemplate.md) — `Comment` (expand)
- [FormTemplates](/entities/Common/FormTemplate.md) — `CommentId` (FK)
- [MonitoringTasks](/entities/Common/MonitoringTask.md) — `Comment` (expand)
- [MonitoringTasks](/entities/Common/MonitoringTask.md) — `CommentId` (FK)
- [PartConfigurationTemplates](/entities/Common/PartConfigurationTemplate.md) — `Comment` (expand)
- [PartConfigurationTemplates](/entities/Common/PartConfigurationTemplate.md) — `CommentId` (FK)
- [PartConfigurations](/entities/Common/PartConfiguration.md) — `Comment` (expand)
- [PartConfigurations](/entities/Common/PartConfiguration.md) — `CommentId` (FK)
- [Persons](/entities/Common/Person.md) — `Comment` (expand)
- [Persons](/entities/Common/Person.md) — `CommentId` (FK)
- [ProjectActivities](/entities/Common/ProjectActivity.md) — `Comment` (expand)
- [ProjectActivities](/entities/Common/ProjectActivity.md) — `CommentId` (FK)
- [ProjectActivityTypes](/entities/Common/ProjectActivityType.md) — `Comment` (expand)
- [ProjectActivityTypes](/entities/Common/ProjectActivityType.md) — `CommentId` (FK)
- [ProjectCostBudgets](/entities/Common/ProjectCostBudget.md) — `Comment` (expand)
- [ProjectCostBudgets](/entities/Common/ProjectCostBudget.md) — `CommentId` (FK)
- [ProjectCostForecasts](/entities/Common/ProjectCostForecast.md) — `Comment` (expand)
- [ProjectCostForecasts](/entities/Common/ProjectCostForecast.md) — `CommentId` (FK)
- [ProjectCostReportingEntries](/entities/Common/ProjectCostReportingEntry.md) — `Comment` (expand)
- [ProjectCostReportingEntries](/entities/Common/ProjectCostReportingEntry.md) — `InternalComment` (expand)
- [Projects](/entities/Common/Project.md) — `ExternalComment` (expand)
- [Projects](/entities/Common/Project.md) — `ExternalCommentId` (FK)
- [Projects](/entities/Common/Project.md) — `InternalComment` (expand)
- [Projects](/entities/Common/Project.md) — `InternalCommentId` (FK)
- [Revisions](/entities/Common/Revision.md) — `Comment` (expand)
- [Revisions](/entities/Common/Revision.md) — `CommentId` (FK)
- [VatRates](/entities/Common/VatRate.md) — `ReferenceText` (expand)
- [VatRates](/entities/Common/VatRate.md) — `ReferenceTextId` (FK)

**Inventory**

- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ActualRejectionComment` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ActualRejectionCommentId` (FK)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ExternalComment` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ExternalCommentId` (FK)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `InternalComment` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `InternalCommentId` (FK)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ReasonComment` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ReasonCommentId` (FK)
- [CaseEntryActivities](/entities/Inventory/CaseEntryActivity.md) — `Comment` (expand)
- [CaseEntryActivities](/entities/Inventory/CaseEntryActivity.md) — `CommentId` (FK)
- [CaseManagementTemplateNodes](/entities/Inventory/CaseManagementTemplateNode.md) — `Comment` (expand)
- [CaseManagementTemplateNodes](/entities/Inventory/CaseManagementTemplateNode.md) — `CommentId` (FK)
- [Locations](/entities/Inventory/Location.md) — `BlockMessage` (expand)
- [Locations](/entities/Inventory/Location.md) — `BlockMessageId` (FK)
- [Locations](/entities/Inventory/Location.md) — `Comment` (expand)
- [Locations](/entities/Inventory/Location.md) — `CommentId` (FK)
- [PartActivities](/entities/Inventory/PartActivity.md) — `CommentId` (FK)
- [Parts](/entities/Inventory/Part.md) — `BlockMessage` (expand)
- [Parts](/entities/Inventory/Part.md) — `BlockMessageId` (FK)
- [Parts](/entities/Inventory/Part.md) — `Comment` (expand)
- [Parts](/entities/Inventory/Part.md) — `CommentId` (FK)
- [Parts](/entities/Inventory/Part.md) — `ManufacturingComment` (expand)
- [Parts](/entities/Inventory/Part.md) — `ManufacturingCommentId` (FK)
- [Parts](/entities/Inventory/Part.md) — `PickingInstruction` (expand)
- [Parts](/entities/Inventory/Part.md) — `PickingInstructionId` (FK)
- [Parts](/entities/Inventory/Part.md) — `PurchaseComment` (expand)
- [Parts](/entities/Inventory/Part.md) — `PurchaseCommentId` (FK)
- [Parts](/entities/Inventory/Part.md) — `ReceivingInstruction` (expand)
- [Parts](/entities/Inventory/Part.md) — `ReceivingInstructionId` (FK)
- [Parts](/entities/Inventory/Part.md) — `SalesComment` (expand)
- [Parts](/entities/Inventory/Part.md) — `SalesCommentId` (FK)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `BlockMessage` (expand)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `BlockMessageId` (FK)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `Certificate` (expand)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `CertificateId` (FK)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `Comment` (expand)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `CommentId` (FK)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `InstallationComment` (expand)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `InstallationCommentId` (FK)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `WarrantyCommitment` (expand)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `WarrantyCommitmentId` (FK)

**Manufacturing**

- [DrawingRevisions](/entities/Manufacturing/DrawingRevision.md) — `RevisionComment` (expand)
- [DrawingRevisions](/entities/Manufacturing/DrawingRevision.md) — `RevisionCommentId` (FK)
- [MaintenanceReportingRows](/entities/Manufacturing/MaintenanceReportingRow.md) — `Comment` (expand)
- [MaintenanceReportingRows](/entities/Manufacturing/MaintenanceReportingRow.md) — `CommentId` (FK)
- [MaintenanceReportingRows](/entities/Manufacturing/MaintenanceReportingRow.md) — `Instruction` (expand)
- [MaintenanceReportingRows](/entities/Manufacturing/MaintenanceReportingRow.md) — `InstructionId` (FK)
- [MaintenanceReportingSelectionRows](/entities/Manufacturing/MaintenanceReportingSelectionRow.md) — `Comment` (expand)
- [MaintenanceReportingSelectionRows](/entities/Manufacturing/MaintenanceReportingSelectionRow.md) — `CommentId` (FK)
- [MaintenanceReportings](/entities/Manufacturing/MaintenanceReporting.md) — `Comment` (expand)
- [MaintenanceReportings](/entities/Manufacturing/MaintenanceReporting.md) — `CommentId` (FK)
- [MaintenanceReportings](/entities/Manufacturing/MaintenanceReporting.md) — `Instruction` (expand)
- [ManufacturingOrderMaterials](/entities/Manufacturing/ManufacturingOrderMaterial.md) — `InstructionComment` (expand)
- [ManufacturingOrderMaterials](/entities/Manufacturing/ManufacturingOrderMaterial.md) — `InstructionCommentId` (FK)
- [ManufacturingOrderNodeDrawingRevisions](/entities/Manufacturing/ManufacturingOrderNodeDrawingRevision.md) — `RevisionComment` (expand)
- [ManufacturingOrderNodeDrawingRevisions](/entities/Manufacturing/ManufacturingOrderNodeDrawingRevision.md) — `RevisionCommentId` (FK)
- [ManufacturingOrderOperationReportings](/entities/Manufacturing/ManufacturingOrderOperationReporting.md) — `Comment` (expand)
- [ManufacturingOrderOperationReportings](/entities/Manufacturing/ManufacturingOrderOperationReporting.md) — `CommentId` (FK)
- [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) — `InstructionComment` (expand)
- [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) — `InstructionCommentId` (FK)
- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `Comment` (expand)
- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `CommentId` (FK)
- [MaterialRows](/entities/Manufacturing/MaterialRow.md) — `Comment` (expand)
- [MaterialRows](/entities/Manufacturing/MaterialRow.md) — `CommentId` (FK)
- [OperationRows](/entities/Manufacturing/OperationRow.md) — `Comment` (expand)
- [OperationRows](/entities/Manufacturing/OperationRow.md) — `CommentId` (FK)
- [WorkCenters](/entities/Manufacturing/WorkCenter.md) — `Comment` (expand)
- [WorkCenters](/entities/Manufacturing/WorkCenter.md) — `CommentId` (FK)

**Purchase**

- [BlanketOrderPurchases](/entities/Purchase/BlanketOrderPurchase.md) — `ExternalComment` (expand)
- [BlanketOrderPurchases](/entities/Purchase/BlanketOrderPurchase.md) — `ExternalCommentId` (FK)
- [BlanketOrderPurchases](/entities/Purchase/BlanketOrderPurchase.md) — `InternalComment` (expand)
- [BlanketOrderPurchases](/entities/Purchase/BlanketOrderPurchase.md) — `InternalCommentId` (FK)
- [Inquiries](/entities/Purchase/Inquiry.md) — `ExternalComment` (expand)
- [Inquiries](/entities/Purchase/Inquiry.md) — `ExternalCommentId` (FK)
- [Inquiries](/entities/Purchase/Inquiry.md) — `InternalComment` (expand)
- [Inquiries](/entities/Purchase/Inquiry.md) — `InternalCommentId` (FK)
- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `Comment` (expand)
- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `CommentId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `DelayComment` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `DelayCommentId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `ReceivingInspectionInstruction` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `ReceivingInspectionInstructionId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `ReceivingMessage` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `ReceivingMessageId` (FK)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `ExternalComment` (expand)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `ExternalCommentId` (FK)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `InternalComment` (expand)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `InternalCommentId` (FK)
- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `OverridePurchaseComment` (expand)
- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `OverridePurchaseCommentId` (FK)
- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `PriceComment` (expand)
- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `PriceCommentId` (FK)
- [Suppliers](/entities/Purchase/Supplier.md) — `ArrivalReportingInstruction` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `ArrivalReportingInstructionId` (FK)
- [Suppliers](/entities/Purchase/Supplier.md) — `BlockMessage` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `BlockMessageId` (FK)
- [Suppliers](/entities/Purchase/Supplier.md) — `Comment` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `CommentId` (FK)

**Sales**

- [BlanketOrderSales](/entities/Sales/BlanketOrderSales.md) — `ExternalComment` (expand)
- [BlanketOrderSales](/entities/Sales/BlanketOrderSales.md) — `ExternalCommentId` (FK)
- [BlanketOrderSales](/entities/Sales/BlanketOrderSales.md) — `InternalComment` (expand)
- [BlanketOrderSales](/entities/Sales/BlanketOrderSales.md) — `InternalCommentId` (FK)
- [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) — `Comment` (expand)
- [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) — `CommentId` (FK)
- [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) — `ReasonLostComment` (expand)
- [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) — `ReasonLostCommentId` (FK)
- [BusinessOpportunityActivities](/entities/Sales/BusinessOpportunityActivity.md) — `Comment` (expand)
- [BusinessOpportunityActivities](/entities/Sales/BusinessOpportunityActivity.md) — `CommentId` (FK)
- [BusinessOpportunityActivityTemplateRows](/entities/Sales/BusinessOpportunityActivityTemplateRow.md) — `Comment` (expand)
- [BusinessOpportunityActivityTemplateRows](/entities/Sales/BusinessOpportunityActivityTemplateRow.md) — `CommentId` (FK)
- [BusinessOpportunityReferences](/entities/Sales/BusinessOpportunityReference.md) — `Comment` (expand)
- [BusinessOpportunityReferences](/entities/Sales/BusinessOpportunityReference.md) — `CommentId` (FK)
- [BusinessOpportunityTypes](/entities/Sales/BusinessOpportunityType.md) — `Comment` (expand)
- [BusinessOpportunityTypes](/entities/Sales/BusinessOpportunityType.md) — `CommentId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `ExternalComment` (expand)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `ExternalCommentId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `InternalComment` (expand)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `InternalCommentId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `PickInstruction` (expand)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `PickInstructionId` (FK)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `OverrideSalesComment` (expand)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `OverrideSalesCommentId` (FK)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `PickingComment` (expand)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `PickingCommentId` (FK)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `PriceComment` (expand)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `PriceCommentId` (FK)
- [CustomerRelationshipManagementActivities](/entities/Sales/CustomerRelationshipManagementActivity.md) — `Comment` (expand)
- [CustomerRelationshipManagementActivities](/entities/Sales/CustomerRelationshipManagementActivity.md) — `CommentId` (FK)
- [Customers](/entities/Sales/Customer.md) — `BlockMessage` (expand)
- [Customers](/entities/Sales/Customer.md) — `BlockMessageId` (FK)
- [Customers](/entities/Sales/Customer.md) — `Comment` (expand)
- [Customers](/entities/Sales/Customer.md) — `CommentId` (FK)
- [Customers](/entities/Sales/Customer.md) — `PickingListComment` (expand)
- [Customers](/entities/Sales/Customer.md) — `PickingListCommentId` (FK)
- [PackageRows](/entities/Sales/PackageRow.md) — `ExternalComment` (expand)
- [PackageRows](/entities/Sales/PackageRow.md) — `ExternalCommentId` (FK)
- [PackageRows](/entities/Sales/PackageRow.md) — `InternalComment` (expand)
- [PackageRows](/entities/Sales/PackageRow.md) — `InternalCommentId` (FK)
- [QuoteActivities](/entities/Sales/QuoteActivity.md) — `Comment` (expand)
- [QuoteActivities](/entities/Sales/QuoteActivity.md) — `CommentId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `ExternalComment` (expand)
- [Quotes](/entities/Sales/Quote.md) — `ExternalCommentId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `InternalComment` (expand)
- [Quotes](/entities/Sales/Quote.md) — `InternalCommentId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `ReasonLostComment` (expand)
- [Quotes](/entities/Sales/Quote.md) — `ReasonLostCommentId` (FK)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `ExternalComment` (expand)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `ExternalCommentId` (FK)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `InternalComment` (expand)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `InternalCommentId` (FK)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `Comment` (expand)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `CommentId` (FK)

**TimeRecording**

- [AdditionRecordings](/entities/TimeRecording/AdditionRecording.md) — `Comment` (expand)
- [Schedules](/entities/TimeRecording/Schedule.md) — `BlockMessage` (expand)
- [Schedules](/entities/TimeRecording/Schedule.md) — `BlockMessageId` (FK)
- [WorkIntervals](/entities/TimeRecording/WorkInterval.md) — `Comment` (expand)
- [WorkIntervals](/entities/TimeRecording/WorkInterval.md) — `CommentId` (FK)


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
