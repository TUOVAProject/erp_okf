---
type: API Module
title: Manufacturing
description: Monitor ERP API module Manufacturing.
tags:
- Manufacturing
- module
generated:
  by: process:monitor-okf-build
  from: 677a27684767
entity_count: 30
queryable_count: 30
---

# Manufacturing

Monitor API module `Manufacturing`: 30 queryable entities, 0 commands, 0 payload types.

Full listing: [Manufacturing entities](/entities/Manufacturing/index.md)

## Queryable entities

| Entity | Endpoint | Description |
| --- | --- | --- |
| [AlternativeOperationRows](/entities/Manufacturing/AlternativeOperationRow.md) | `/api/v1/Manufacturing/AlternativeOperationRows` | Represents an alternative work center on an operation row. |
| [DrawingRevisions](/entities/Manufacturing/DrawingRevision.md) | `/api/v1/Manufacturing/DrawingRevisions` | Represents a drawing revision. |
| [Drawings](/entities/Manufacturing/Drawing.md) | `/api/v1/Manufacturing/Drawings` | Represents a drawing. |
| [MaintenanceReportingRows](/entities/Manufacturing/MaintenanceReportingRow.md) | `/api/v1/Manufacturing/MaintenanceReportingRows` | Represents a maintenance reporting row. |
| [MaintenanceReportings](/entities/Manufacturing/MaintenanceReporting.md) | `/api/v1/Manufacturing/MaintenanceReportings` | Represents a maintenance reporting. |
| [MaintenanceReportingSelectionRows](/entities/Manufacturing/MaintenanceReportingSelectionRow.md) | `/api/v1/Manufacturing/MaintenanceReportingSelectionRows` | Represents a maintenance reporting selection row. |
| [ManualOperationStatuses](/entities/Manufacturing/ManualOperationStatus.md) | `/api/v1/Manufacturing/ManualOperationStatuses` | Represents a manual operation status. |
| [ManufacturingOrderMaterials](/entities/Manufacturing/ManufacturingOrderMaterial.md) | `/api/v1/Manufacturing/ManufacturingOrderMaterials` | Represents a manufacturing order material. |
| [ManufacturingOrderNodeDrawingRevisions](/entities/Manufacturing/ManufacturingOrderNodeDrawingRevision.md) | `/api/v1/Manufacturing/ManufacturingOrderNodeDrawingRevisions` | Represents a drawing revision for manufacturing order node. |
| [ManufacturingOrderNodeDrawings](/entities/Manufacturing/ManufacturingOrderNodeDrawing.md) | `/api/v1/Manufacturing/ManufacturingOrderNodeDrawings` | Represents a drawing for manufacturing order node. |
| [ManufacturingOrderNodes](/entities/Manufacturing/ManufacturingOrderNode.md) | `/api/v1/Manufacturing/ManufacturingOrderNodes` | Represents a manufacturing order node. |
| [ManufacturingOrderOperationControlDataRows](/entities/Manufacturing/ManufacturingOrderOperationControlDataRow.md) | `/api/v1/Manufacturing/ManufacturingOrderOperationControlDataRows` | Represents a measuring plan for a manufacturing order operation. |
| [ManufacturingOrderOperationReportings](/entities/Manufacturing/ManufacturingOrderOperationReporting.md) | `/api/v1/Manufacturing/ManufacturingOrderOperationReportings` | Represents a manufacturing order operation reporting. |
| [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) | `/api/v1/Manufacturing/ManufacturingOrderOperations` | Represents a manufacturing order operation. |
| [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) | `/api/v1/Manufacturing/ManufacturingOrders` | Represents a manufacturing order. |
| [ManufacturingOrderTypes](/entities/Manufacturing/ManufacturingOrderType.md) | `/api/v1/Manufacturing/ManufacturingOrderTypes` | Represents a manufacturing order type. |
| [ManufacturingPickingListMaterials](/entities/Manufacturing/ManufacturingPickingListMaterial.md) | `/api/v1/Manufacturing/ManufacturingPickingListMaterials` | Represents a manufacturing picking list material. |
| [ManufacturingPickingLists](/entities/Manufacturing/ManufacturingPickingList.md) | `/api/v1/Manufacturing/ManufacturingPickingLists` | Represents a manufacturing picking list. |
| [MaterialRowReferenceNumbers](/entities/Manufacturing/ReferenceNumber.md) | `/api/v1/Manufacturing/MaterialRowReferenceNumbers` | Represents a reference number attached to a material row. |
| [MaterialRows](/entities/Manufacturing/MaterialRow.md) | `/api/v1/Manufacturing/MaterialRows` | Represents a material row. |
| [OperationRowControlDataRows](/entities/Manufacturing/OperationRowControlDataRow.md) | `/api/v1/Manufacturing/OperationRowControlDataRows` | Represents a measuring plan for an operation row. |
| [OperationRows](/entities/Manufacturing/OperationRow.md) | `/api/v1/Manufacturing/OperationRows` | Represents an operation row. |
| [OrderQuantityManufacturingOrderOperations](/entities/Manufacturing/OrderQuantityManufacturingOrderOperation.md) | `/api/v1/Manufacturing/OrderQuantityManufacturingOrderOperations` | Represents a order quantity template on part that holds many partial quantities. |
| [OrderQuantityManufacturingOrders](/entities/Manufacturing/OrderQuantityManufacturingOrder.md) | `/api/v1/Manufacturing/OrderQuantityManufacturingOrders` | Represents a order quantity template on part that holds many partial quantities. |
| [Preparations](/entities/Manufacturing/Preparation.md) | `/api/v1/Manufacturing/Preparations` | Represents a part preparation |
| [ProductionCalendarExceptions](/entities/Manufacturing/ProductionCalendarException.md) | `/api/v1/Manufacturing/ProductionCalendarExceptions` | Represents a table that contains exceptions from the production calendar. Only used when using daily planning. |
| [ReasonCodeTimeConsumptions](/entities/Manufacturing/ReasonCodeTimeConsumption.md) | `/api/v1/Manufacturing/ReasonCodeTimeConsumptions` | Represents a reason code time consumption. |
| [WorkCenterCostFactorGroups](/entities/Manufacturing/WorkCenterCostFactorGroup.md) | `/api/v1/Manufacturing/WorkCenterCostFactorGroups` | Represents a cost factor group belonging to a work center. Note that all cost factors are represented in company currency per hour. |
| [WorkCenterManufacturingPrintSettings](/entities/Manufacturing/WorkCenterManufacturingPrintSettings.md) | `/api/v1/Common/WorkCenterManufacturingPrintSettings` | Represents manufacturing print settings for a work center. |
| [WorkCenters](/entities/Manufacturing/WorkCenter.md) | `/api/v1/Manufacturing/WorkCenters` | Represents a manufacturing work center. |

## Depends on other modules

- [Common](/modules/Common.md): [ApplicationUsers](/entities/Common/ApplicationUser.md), [Comments](/entities/Common/Comment.md), [Currencies](/entities/Common/Currency.md), [ExtraFields](/entities/Common/ExtraField.md), [ExtraFieldTemplates](/entities/Common/ExtraFieldTemplate.md), [FormTemplates](/entities/Common/FormTemplate.md), [MeasuringTemplates](/entities/Common/MeasuringTemplate.md), [PartConfigurations](/entities/Common/PartConfiguration.md), [PartialQuantities](/entities/Common/PartialQuantity.md), [Persons](/entities/Common/Person.md), [Projects](/entities/Common/Project.md), [Revisions](/entities/Common/Revision.md), [Units](/entities/Common/Unit.md), [Warehouses](/entities/Common/Warehouse.md)
- [Inventory](/modules/Inventory.md): [Parts](/entities/Inventory/Part.md), [ProductRecords](/entities/Inventory/ProductRecord.md), [QuantityChanges](/entities/Inventory/QuantityChange.md)
- [Purchase](/modules/Purchase.md): [PurchaseOrderDeliveryRows](/entities/Purchase/PurchaseOrderDeliveryRow.md), [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md)
- [Sales](/modules/Sales.md): [CustomerOrders](/entities/Sales/CustomerOrder.md), [Customers](/entities/Sales/Customer.md)
- [TimeRecording](/modules/TimeRecording.md): [PersonWorkCenters](/entities/TimeRecording/PersonWorkCenter.md), [Schedules](/entities/TimeRecording/Schedule.md)
