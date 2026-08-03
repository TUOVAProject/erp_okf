# Manufacturing

Monitor API module `Manufacturing`: 30 queryable entities, 0 commands, 0 payload types.

## Queryable entities

<a id="Manufacturing.AlternativeOperationRow"></a>
### AlternativeOperationRows

Represents an alternative work center on an operation row.

- **Endpoint:** `GET /api/v1/Manufacturing/AlternativeOperationRows`
- **Required permission:** Show part
- **Introduced in:** 26.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OperationRowId` | `Int64` | no | [OperationRows](Manufacturing.md#Manufacturing.OperationRow) |
| `WorkCenterId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) |
| `UnitStaffingFactor` | `Decimal?` | yes |  |
| `SetupStaffingFactor` | `Decimal?` | yes |  |
| `QueueTime` | `TimeSpan?` | yes |  |
| `SetupTime` | `TimeSpan?` | yes |  |
| `UnitTime` | `TimeSpan?` | yes |  |
| `CycleTime` | `TimeSpan?` | yes |  |

**References out:** [OperationRows](Manufacturing.md#Manufacturing.OperationRow), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [OperationRows](Manufacturing.md#Manufacturing.OperationRow)

<a id="Manufacturing.DrawingRevision"></a>
### DrawingRevisions

Represents a drawing revision.

- **Endpoint:** `GET /api/v1/Manufacturing/DrawingRevisions`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `ParentId` | `Int64?` | yes | [Drawings](Manufacturing.md#Manufacturing.Drawing) |
| `RevisionCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `RevisionComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |

**References out:** [Comments](Common.md#Common.Comment), [Drawings](Manufacturing.md#Manufacturing.Drawing)
**Referenced by:** [Drawings](Manufacturing.md#Manufacturing.Drawing)

<a id="Manufacturing.Drawing"></a>
### Drawings

Represents a drawing.

- **Endpoint:** `GET /api/v1/Manufacturing/Drawings`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `DrawingNumber` | `String` | no |  |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) |
| `Revisions` | `DrawingRevisions[]` | no | [DrawingRevisions](Manufacturing.md#Manufacturing.DrawingRevision) |
| `ActiveDrawingRevisionId` | `Int64?` | yes | [DrawingRevisions](Manufacturing.md#Manufacturing.DrawingRevision) |

**References out:** [DrawingRevisions](Manufacturing.md#Manufacturing.DrawingRevision), [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [DrawingRevisions](Manufacturing.md#Manufacturing.DrawingRevision), [Parts](Inventory.md#Inventory.Part)

<a id="Manufacturing.MaintenanceReportingRow"></a>
### MaintenanceReportingRows

Represents a maintenance reporting row.

- **Endpoint:** `GET /api/v1/Manufacturing/MaintenanceReportingRows`
- **Required permission:** Show maintenance plan
- **Introduced in:** 25.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Instruction` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `InstructionId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Description` | `String` | no |  |
| `MaintenanceReportingSelectionRowId` | `Int64` | no | [MaintenanceReportingSelectionRows](Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow) |
| `RowIndex` | `Int32?` | yes |  |
| `Checkbox` | `Boolean` | no |  |
| `DateTimeValue` | `DateTimeOffset?` | yes |  |
| `Number` | `Decimal?` | yes |  |
| `TextValue` | `String` | no |  |
| `Type` | `Int32` | no |  |
| `ReportingStatus` | `Int32?` | yes |  |
| `MinValue` | `Decimal?` | yes |  |
| `MaxValue` | `Decimal?` | yes |  |
| `Value` | `Decimal?` | yes |  |
| `MasterToolId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `MasterToolProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) |

- `Type` — Decimal=0, Text=1, CheckBox=2, Date=3
- `ReportingStatus` — Ok=0, NotOk=1, OkWithAction=2

**References out:** [Comments](Common.md#Common.Comment), [MaintenanceReportingSelectionRows](Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow), [Parts](Inventory.md#Inventory.Part), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Units](Common.md#Common.Unit)
**Referenced by:** [MaintenanceReportingSelectionRows](Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow)

<a id="Manufacturing.MaintenanceReporting"></a>
### MaintenanceReportings

Represents a maintenance reporting.

- **Endpoint:** `GET /api/v1/Manufacturing/MaintenanceReportings`
- **Required permission:** Show maintenance plan
- **Introduced in:** 24.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `SerialNumber` | `String` | no |  |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ManufacturingOrder` | `ManufacturingOrders` | no | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ProductRecordId` | `Int64` | no |  |
| `ProductRecord` | `ProductRecords` | no | [ProductRecords](Inventory.md#Inventory.ProductRecord) |
| `MaintenanceRowId` | `Int64` | no |  |
| `ShortComment` | `String` | no |  |
| `CommentId` | `Int64` | no | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `MaintenanceStatus` | `Int32?` | yes |  |
| `ReportedById` | `Int64` | no | [Persons](Common.md#Common.Person) |
| `ReportedBy` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `ReportingStatus` | `Int32` | no |  |
| `ActualDate` | `DateTimeOffset?` | yes |  |
| `Status` | `Int32` | no |  |
| `NextOccurrence` | `DateTimeOffset?` | yes |  |
| `ColorCode` | `Int32?` | yes |  |
| `InstructionId` | `Int64` | no |  |
| `Instruction` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `MaintenanceReportingSelectionRows` | `MaintenanceReportingSelectionRows[]` | no | [MaintenanceReportingSelectionRows](Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow) |

- `MaintenanceStatus` — Ok=0, NotOk=1, OkWithAction=2
- `ReportingStatus` — New=0, InProgress=1, Finished=2
- `Status` — ApprovalForUse=0, NonApproval=1, ServicePastDue=2, UnderServiceOrCalibration=3, Rejected=4, ServiceOrCalibrationBeforeUse=5, Missing=6, Scrapped=7

**References out:** [Comments](Common.md#Common.Comment), [MaintenanceReportingSelectionRows](Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [Persons](Common.md#Common.Person), [ProductRecords](Inventory.md#Inventory.ProductRecord)
**Referenced by:** [MaintenanceReportingSelectionRows](Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow)

<a id="Manufacturing.MaintenanceReportingSelectionRow"></a>
### MaintenanceReportingSelectionRows

Represents a maintenance reporting selection row.

- **Endpoint:** `GET /api/v1/Manufacturing/MaintenanceReportingSelectionRows`
- **Required permission:** Show maintenance plan
- **Introduced in:** 25.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Description` | `String` | no |  |
| `MaintenanceReportingId` | `Int64` | no | [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting) |
| `RowIndex` | `Int32?` | yes |  |
| `MaintenanceReportingRows` | `MaintenanceReportingRows[]` | no | [MaintenanceReportingRows](Manufacturing.md#Manufacturing.MaintenanceReportingRow) |

**References out:** [Comments](Common.md#Common.Comment), [MaintenanceReportingRows](Manufacturing.md#Manufacturing.MaintenanceReportingRow), [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting)
**Referenced by:** [MaintenanceReportingRows](Manufacturing.md#Manufacturing.MaintenanceReportingRow), [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting)

<a id="Manufacturing.ManualOperationStatus"></a>
### ManualOperationStatuses

Represents a manual operation status.

- **Endpoint:** `GET /api/v1/Manufacturing/ManualOperationStatuses`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 25.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation)

<a id="Manufacturing.ManufacturingOrderMaterial"></a>
### ManufacturingOrderMaterials

Represents a manufacturing order material.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderMaterials`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ReportNumber` | `Int64` | no |  |
| `RowNumber` | `Int32` | no |  |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) |
| `ToOperationNumber` | `Int32` | no |  |
| `ReportedQuantity` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `PlannedQuantity` | `Decimal` | no |  |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode) |
| `PositionNumber` | `String` | no |  |
| `InstructionCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `InstructionComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `QuantityPerUnit` | `Decimal` | no |  |
| `CycleTime` | `TimeSpan?` | yes |  |
| `EditedStatus` | `Int32` | no |  |
| `ExtraQuantityProcent` | `Decimal` | no |  |
| `LinkedPurchaseOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `LockedToBatchNo` | `String` | no |  |
| `QuantityPerCycle` | `Decimal?` | yes |  |
| `RejectedQuantity` | `Decimal` | no |  |
| `ReportedSetupQuantity` | `Decimal` | no |  |
| `RestSetupQuantity` | `Decimal` | no |  |
| `SetupQuantity` | `Decimal` | no |  |
| `MaterialRowOriginId` | `Int64?` | yes |  |

- `EditedStatus` (bitmask) — NotEdited=0, Edited=1, Synchronized=2

**References out:** [Comments](Common.md#Common.Comment), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](Inventory.md#Inventory.Part), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)
**Referenced by:** [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [ManufacturingPickingListMaterials](Manufacturing.md#Manufacturing.ManufacturingPickingListMaterial)

<a id="Manufacturing.ManufacturingOrderNodeDrawingRevision"></a>
### ManufacturingOrderNodeDrawingRevisions

Represents a drawing revision for manufacturing order node.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderNodeDrawingRevisions`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 24.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `ParentId` | `Int64?` | yes | [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing) |
| `RevisionCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `RevisionComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |

**References out:** [Comments](Common.md#Common.Comment), [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing)
**Referenced by:** [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing)

<a id="Manufacturing.ManufacturingOrderNodeDrawing"></a>
### ManufacturingOrderNodeDrawings

Represents a drawing for manufacturing order node.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderNodeDrawings`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 24.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `DrawingNumber` | `String` | no |  |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode) |
| `Revisions` | `ManufacturingOrderNodeDrawingRevisions[]` | no | [ManufacturingOrderNodeDrawingRevisions](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision) |
| `ActiveDrawingRevisionId` | `Int64?` | yes | [ManufacturingOrderNodeDrawingRevisions](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision) |

**References out:** [ManufacturingOrderNodeDrawingRevisions](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode)
**Referenced by:** [ManufacturingOrderNodeDrawingRevisions](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode)

<a id="Manufacturing.ManufacturingOrderNode"></a>
### ManufacturingOrderNodes

Represents a manufacturing order node.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderNodes`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `IsMainNode` | `Boolean` | no |  |
| `IsRootNode` | `Boolean` | no |  |
| `Level` | `Int32` | no |  |
| `Number` | `Int32` | no |  |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) |
| `ReportedQuantity` | `Decimal` | no |  |
| `PlannedQuantity` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `StartDate` | `DateTimeOffset` | no |  |
| `EndDate` | `DateTimeOffset` | no |  |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `Status` | `Int32` | no |  |
| `ManufacturingOrderNodeId` | `Int64?` | yes | [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode) |
| `Drawings` | `ManufacturingOrderNodeDrawings[]` | no | [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing) |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) |
| `SerialNumberProductRecords` | `ProductRecords[]` | no | [ProductRecords](Inventory.md#Inventory.ProductRecord) |

- `Status` — NotInitialized=0, Registrered=1, Printed=2, Started=3, Finished=4, PostCalculated=5, Delivered=6, Historical=9

**References out:** [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [Parts](Inventory.md#Inventory.Part), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Revisions](Common.md#Common.Revision), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder)

<a id="Manufacturing.ManufacturingOrderOperationControlDataRow"></a>
### ManufacturingOrderOperationControlDataRows

Represents a measuring plan for a manufacturing order operation.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderOperationControlDataRows`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ManufacturingOrderOperationId` | `Int64` | no | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](Common.md#Common.MeasuringTemplate) |
| `OverridenFormTemplateId` | `Int64` | no | [FormTemplates](Common.md#Common.FormTemplate) |
| `OverridenFrequencyText` | `String` | no |  |
| `OverridenIntervalAmount` | `Int32?` | yes |  |
| `OverridenInterval` | `Int32?` | yes |  |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) |

**References out:** [FormTemplates](Common.md#Common.FormTemplate), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [MeasuringTemplates](Common.md#Common.MeasuringTemplate), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation)

<a id="Manufacturing.ManufacturingOrderOperationReporting"></a>
### ManufacturingOrderOperationReportings

Represents a manufacturing order operation reporting.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderOperationReportings`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 24.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OperationId` | `Int64` | no | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `Quantity` | `Decimal` | no |  |
| `SetupTime` | `TimeSpan?` | yes |  |
| `UnitTime` | `TimeSpan?` | yes |  |
| `WorkCenterId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) |
| `EmployeeId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `ReportingEmployeeId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `ActualReportedDate` | `DateTimeOffset` | no |  |
| `PreviousRestQuantity` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `OverReceiveQuantity` | `Decimal` | no |  |
| `SetupCost` | `Decimal?` | yes |  |
| `SetupCostCurrencyId` | `Int64?` | yes |  |
| `SetupCostFactor1` | `Decimal` | no |  |
| `SetupCostFactor2` | `Decimal` | no |  |
| `SetupCostFactor3` | `Decimal` | no |  |
| `SetupCostInForeignCurrency` | `Decimal?` | yes |  |
| `SetupCostInForeignCurrencyCurrencyId` | `Int64?` | yes |  |
| `UnitCost` | `Decimal?` | yes |  |
| `UnitCostCurrencyId` | `Int64?` | yes |  |
| `UnitCostFactor1` | `Decimal` | no |  |
| `UnitCostFactor2` | `Decimal` | no |  |
| `UnitCostFactor3` | `Decimal` | no |  |
| `UnitCostInForeignCurrency` | `Decimal?` | yes |  |
| `UnitCostInForeignCurrencyCurrencyId` | `Int64?` | yes |  |
| `IsSubcontractor` | `Boolean` | no |  |
| `Type` | `Int32` | no |  |
| `SubcontractorRequestedDeliveryDate` | `DateTimeOffset?` | yes |  |
| `SubcontractorActualDeliveryDate` | `DateTimeOffset?` | yes |  |
| `ReportRestQuantitiesOnSubsequentOperations` | `Boolean` | no |  |
| `IsExportedToManagementAccounting` | `Boolean` | no |  |
| `WipLocation` | `String` | no |  |
| `PreviousWipLocation` | `String` | no |  |
| `OfWichTime` | `TimeSpan?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ReasonCodeTimeConsumptionId` | `Int64?` | yes | [ReasonCodeTimeConsumptions](Manufacturing.md#Manufacturing.ReasonCodeTimeConsumption) |
| `ReasonCodeTimeConsumption` | `ReasonCodeTimeConsumptions` | no | [ReasonCodeTimeConsumptions](Manufacturing.md#Manufacturing.ReasonCodeTimeConsumption) |
| `AutomaticMaterialReporting` | `Boolean` | no |  |
| `PurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) |
| `PreviousNodeStatus` | `Int32` | no |  |
| `OriginalApprovedQuantityFromDeliveryRow` | `Decimal?` | yes |  |
| `ReportingId` | `Int64?` | yes |  |
| `ReportingTimestamp` | `DateTimeOffset` | no |  |
| `RowNumber` | `Int32` | no |  |

- `Type` — Regular=0, SendToSubcontractor=1, ReceiveFromSubcontractor=2, CancelRest=3, MaterialOnly=4, SubcontractorInvoicePrice=5, RecordingTerminal=6, AdjustRecording=7, UndoRegular=8, UndoRecordingTerminal=9, UndoAdjustRecording=10, SubcontractorPosteriorReport=11, SubcontractorCostsManualReport=12, PickWorkCenter=13
- `PreviousNodeStatus` — NotInitialized=0, Registrered=1, Printed=2, Started=3, Finished=4, PostCalculated=5, Delivered=6, Historical=9

**References out:** [Comments](Common.md#Common.Comment), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [Persons](Common.md#Common.Person), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [ReasonCodeTimeConsumptions](Manufacturing.md#Manufacturing.ReasonCodeTimeConsumption), [Warehouses](Common.md#Common.Warehouse), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [Locations](Inventory.md#Inventory.Location)

<a id="Manufacturing.ManufacturingOrderOperation"></a>
### ManufacturingOrderOperations

Represents a manufacturing order operation.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderOperations`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Priority` | `Int32?` | yes |  |
| `WorkCenterId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) |
| `PlannedQuantity` | `Decimal` | no |  |
| `ReportedQuantity` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `ReportedSetupTime` | `TimeSpan` | no |  |
| `ReportedUnitTime` | `TimeSpan` | no |  |
| `RejectedQuantity` | `Decimal` | no |  |
| `WipLocation` | `String` | no |  |
| `ReportNumber` | `Int64` | no |  |
| `InstructionCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `InstructionComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode) |
| `OperationNumber` | `Int32` | no |  |
| `PlannedSetupTime` | `TimeSpan` | no |  |
| `PlannedUnitTime` | `TimeSpan` | no |  |
| `PlannedStartDate` | `DateTimeOffset` | no |  |
| `PlannedFinishDate` | `DateTimeOffset` | no |  |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |
| `ActualFinishDate` | `DateTimeOffset?` | yes |  |
| `OperationRowId` | `Int64?` | yes | [OperationRows](Manufacturing.md#Manufacturing.OperationRow) |
| `OperationRow` | `OperationRows` | no | [OperationRows](Manufacturing.md#Manufacturing.OperationRow) |
| `Status` | `Int32` | no |  |
| `WorkshopOperationStatus` | `Int32` | no |  |
| `BundleId` | `Int64?` | yes |  |
| `Description` | `String` | no |  |
| `ControlDataRows` | `ManufacturingOrderOperationControlDataRows[]` | no | [ManufacturingOrderOperationControlDataRows](Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow) |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityManufacturingOrderOperations](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrderOperation) |
| `OrderQuantity` | `OrderQuantityManufacturingOrderOperations` | no | [OrderQuantityManufacturingOrderOperations](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrderOperation) |
| `ClearedStatus` | `Boolean` | no |  |
| `OnPriorityPlan` | `Boolean` | no |  |
| `ManualOperationStatusId` | `Int64?` | yes | [ManualOperationStatuses](Manufacturing.md#Manufacturing.ManualOperationStatus) |
| `ManualOperationStatus` | `ManualOperationStatuses` | no | [ManualOperationStatuses](Manufacturing.md#Manufacturing.ManualOperationStatus) |
| `Materials` | `ManufacturingOrderMaterials[]` | no | [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) |
| `FixedLeadTime` | `TimeSpan?` | yes |  |
| `UnitStaffingFactor` | `Decimal?` | yes |  |
| `SetupStaffingFactor` | `Decimal?` | yes |  |
| `IsPlannedTimeCalculated` | `Boolean` | no |  |

- `Status` — None=0, Started=1, PartiallyShipped=2, FullyShipped=3, PartiallyReported=4, Finished=5
- `WorkshopOperationStatus` — NotInitialized=0, InProgress=1, ClockedOut=2, Interrupted=3, PartiallyReported=4, SetupTime=5, IsStandingBy=6, Finished=9

**References out:** [Comments](Common.md#Common.Comment), [ManualOperationStatuses](Manufacturing.md#Manufacturing.ManualOperationStatus), [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperationControlDataRows](Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [OperationRows](Manufacturing.md#Manufacturing.OperationRow), [OrderQuantityManufacturingOrderOperations](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrderOperation), [Parts](Inventory.md#Inventory.Part), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [DelegatedWork](Common.md#Common.DelegatedWork), [IndirectWorkCodes](TimeRecording.md#TimeRecording.IndirectWorkCode), [ManufacturingOrderOperationControlDataRows](Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow), [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [StandbyWorks](TimeRecording.md#TimeRecording.StandbyWork), [WorkIntervals](TimeRecording.md#TimeRecording.WorkInterval)

<a id="Manufacturing.ManufacturingOrder"></a>
### ManufacturingOrders

Represents a manufacturing order.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrders`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OrderNumber` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) |
| `ReportedQuantity` | `Decimal` | no |  |
| `PlannedQuantity` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `StartDate` | `DateTimeOffset` | no |  |
| `FinishDate` | `DateTimeOffset` | no |  |
| `Priority` | `Int32` | no |  |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `Operations` | `ManufacturingOrderOperations[]` | no | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `Materials` | `ManufacturingOrderMaterials[]` | no | [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) |
| `Nodes` | `ManufacturingOrderNodes[]` | no | [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode) |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) |
| `Project` | `Projects` | no | [Projects](Common.md#Common.Project) |
| `CategoryString` | `String` | no |  |
| `VariantCode` | `String` | no |  |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `InitialFinishDate` | `DateTimeOffset` | no |  |
| `PartConfigurationId` | `Int64?` | yes | [PartConfigurations](Common.md#Common.PartConfiguration) |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityManufacturingOrders](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder) |
| `OrderQuantity` | `OrderQuantityManufacturingOrders` | no | [OrderQuantityManufacturingOrders](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder) |
| `OrderTypeId` | `Int64?` | yes | [ManufacturingOrderTypes](Manufacturing.md#Manufacturing.ManufacturingOrderType) |
| `OrderType` | `ManufacturingOrderTypes` | no | [ManufacturingOrderTypes](Manufacturing.md#Manufacturing.ManufacturingOrderType) |

- `Status` — NotInitialized=0, Registrered=1, Printed=2, Started=3, Finished=4, PostCalculated=5, Delivered=6, Historical=9

**References out:** [Comments](Common.md#Common.Comment), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrderTypes](Manufacturing.md#Manufacturing.ManufacturingOrderType), [OrderQuantityManufacturingOrders](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder), [PartConfigurations](Common.md#Common.PartConfiguration), [Parts](Inventory.md#Inventory.Part), [Projects](Common.md#Common.Project), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [CaseEntry](Inventory.md#Inventory.CaseEntry), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [Locations](Inventory.md#Inventory.Location), [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting), [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ProductRecords](Inventory.md#Inventory.ProductRecord)

<a id="Manufacturing.ManufacturingOrderType"></a>
### ManufacturingOrderTypes

Represents a manufacturing order type.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderTypes`
- **Required permission:** Show order types
- **Introduced in:** 2.35

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Prefix` | `String` | no |  |
| `Description` | `String` | no |  |
| `BaseType` | `Int32` | no |  |

- `BaseType` — InventoryControlled=0, CustomerOrderControlled=1, MaintenanceControlled=2

**Referenced by:** [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder)

<a id="Manufacturing.ManufacturingPickingListMaterial"></a>
### ManufacturingPickingListMaterials

Represents a manufacturing picking list material.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingPickingListMaterials`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.48

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `MaterialId` | `Int64` | no | [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) |
| `Material` | `ManufacturingOrderMaterials` | no | [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) |
| `QuantityChangeId` | `Int64` | no | [QuantityChanges](Inventory.md#Inventory.QuantityChange) |
| `QuantityChange` | `QuantityChanges` | no | [QuantityChanges](Inventory.md#Inventory.QuantityChange) |

**References out:** [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [QuantityChanges](Inventory.md#Inventory.QuantityChange)
**Referenced by:** [ManufacturingPickingLists](Manufacturing.md#Manufacturing.ManufacturingPickingList)

<a id="Manufacturing.ManufacturingPickingList"></a>
### ManufacturingPickingLists

Represents a manufacturing picking list.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingPickingLists`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.48

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `CreatedByApplicationUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `CreatedByPersonId` | `Int64` | no | [Persons](Common.md#Common.Person) |
| `CreatedTimestamp` | `DateTimeOffset` | no |  |
| `PrintedByApplicationUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `PrintedByPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `PrintedTimestamp` | `DateTimeOffset?` | yes |  |
| `Status` | `Int32` | no |  |
| `Grouping` | `Int32` | no |  |
| `Sorting` | `Int32` | no |  |
| `WarehouseId` | `Int64?` | yes | [Warehouses](Common.md#Common.Warehouse) |
| `Type` | `Int32` | no |  |
| `Materials` | `ManufacturingPickingListMaterials[]` | no | [ManufacturingPickingListMaterials](Manufacturing.md#Manufacturing.ManufacturingPickingListMaterial) |

- `Status` — Registered=1, Printed=2, Reported=5, History=9
- `Grouping` — Order=0, Material=1, NoGrouping=2
- `Sorting` — Location=0, MainLocation=1, MaterialPartNumber=2, LocationSortingOrder=3, MainLocationSortingOrder=4
- `Type` — Regular=0, Equipment=1

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [ManufacturingPickingListMaterials](Manufacturing.md#Manufacturing.ManufacturingPickingListMaterial), [Persons](Common.md#Common.Person), [Warehouses](Common.md#Common.Warehouse)

<a id="Manufacturing.ReferenceNumber"></a>
### MaterialRowReferenceNumbers

Represents a reference number attached to a material row.

- **Endpoint:** `GET /api/v1/Manufacturing/MaterialRowReferenceNumbers`
- **Required permission:** Show part
- **Introduced in:** 26.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `MaterialRowId` | `Int64` | no | [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow) |
| `Prefix` | `String` | no |  |
| `From` | `String` | no |  |
| `To` | `String` | no |  |
| `Suffix` | `String` | no |  |
| `Remark` | `String` | no |  |
| `Quantity` | `Decimal` | no |  |
| `RowIndex` | `Int32?` | yes |  |

**References out:** [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow)
**Referenced by:** [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow)

<a id="Manufacturing.MaterialRow"></a>
### MaterialRows

Represents a material row.

- **Endpoint:** `GET /api/v1/Manufacturing/MaterialRows`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `Position` | `String` | no |  |
| `ToOperation` | `Int32` | no |  |
| `Quantity` | `Decimal` | no |  |
| `SetupQuantity` | `Decimal` | no |  |
| `ExtraPercent` | `Decimal` | no |  |
| `IsForCalculationOnly` | `Boolean` | no |  |
| `MainPartId` | `Int64` | no |  |
| `RowIndex` | `Int32` | no |  |
| `PreparationTermType` | `Int32?` | yes |  |
| `PreparationTermFromValue` | `String` | no |  |
| `PreparationTermToValue` | `String` | no |  |
| `ReferenceNumbers` | `MaterialRowReferenceNumbers[]` | no | [MaterialRowReferenceNumbers](Manufacturing.md#Manufacturing.ReferenceNumber) |

**References out:** [Comments](Common.md#Common.Comment), [MaterialRowReferenceNumbers](Manufacturing.md#Manufacturing.ReferenceNumber)
**Referenced by:** [MaterialRowReferenceNumbers](Manufacturing.md#Manufacturing.ReferenceNumber), [Preparations](Manufacturing.md#Manufacturing.Preparation)

<a id="Manufacturing.OperationRowControlDataRow"></a>
### OperationRowControlDataRows

Represents a measuring plan for an operation row.

- **Endpoint:** `GET /api/v1/Manufacturing/OperationRowControlDataRows`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OperationRowId` | `Int64` | no | [OperationRows](Manufacturing.md#Manufacturing.OperationRow) |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](Common.md#Common.MeasuringTemplate) |
| `OverriddenFormTemplateId` | `Int64?` | yes | [FormTemplates](Common.md#Common.FormTemplate) |
| `OverriddenFrequencyText` | `String` | no |  |
| `OverriddenIntervalAmount` | `Int32?` | yes |  |
| `OverriddenInterval` | `Int32?` | yes |  |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) |

**References out:** [FormTemplates](Common.md#Common.FormTemplate), [MeasuringTemplates](Common.md#Common.MeasuringTemplate), [OperationRows](Manufacturing.md#Manufacturing.OperationRow), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [OperationRows](Manufacturing.md#Manufacturing.OperationRow)

<a id="Manufacturing.OperationRow"></a>
### OperationRows

Represents an operation row.

- **Endpoint:** `GET /api/v1/Manufacturing/OperationRows`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OperationNumber` | `Int32` | no |  |
| `SubcontractPartId` | `Int64?` | yes |  |
| `SupplierId` | `Int64?` | yes |  |
| `WorkCenterId` | `Int64` | no |  |
| `IsSubcontractor` | `Boolean` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `Description` | `String` | no |  |
| `TimeCode` | `Int32` | no |  |
| `TimeUnit` | `Int32` | no |  |
| `SetupTime` | `TimeSpan` | no |  |
| `UnitTime` | `TimeSpan` | no |  |
| `ExtraQuantityPercent` | `Decimal` | no |  |
| `NumberOfFlows` | `Decimal?` | yes |  |
| `OverlapPercent` | `Decimal` | no |  |
| `UnitStaffingFactor` | `Decimal?` | yes |  |
| `SetupStaffingFactor` | `Decimal?` | yes |  |
| `SetupQuantity` | `Decimal` | no |  |
| `IsForCalculationOnly` | `Boolean` | no |  |
| `QueueTime` | `TimeSpan?` | yes |  |
| `UseQueueTimeWholeDayRoundOf` | `Boolean?` | yes |  |
| `UnitCostFactorId` | `Int64?` | yes |  |
| `SetupCostFactorId` | `Int64?` | yes |  |
| `FixedLeadTime` | `TimeSpan?` | yes |  |
| `SetupCost` | `Decimal?` | yes |  |
| `SetupCostCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `UnitCost` | `Decimal?` | yes |  |
| `UnitCostCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `TransportCost` | `Decimal?` | yes |  |
| `SupplierPartNumber` | `String` | no |  |
| `DeliverToEndCustomer` | `Boolean` | no |  |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) |
| `ControlDataRows` | `OperationRowControlDataRows[]` | no | [OperationRowControlDataRows](Manufacturing.md#Manufacturing.OperationRowControlDataRow) |
| `AlternativeOperationRows` | `AlternativeOperationRows[]` | no | [AlternativeOperationRows](Manufacturing.md#Manufacturing.AlternativeOperationRow) |
| `PreparationTermType` | `Int32?` | yes |  |
| `PreparationTermFromValue` | `String` | no |  |
| `PreparationTermToValue` | `String` | no |  |

- `TimeCode` — NotInitialized=0, Calculated=1, Studied=2
- `TimeUnit` — Hours=0, Minutes=1, Seconds=2, QuantityPerHour=3, QuantityPerMinute=4, QuantityPerSecond=5

**References out:** [AlternativeOperationRows](Manufacturing.md#Manufacturing.AlternativeOperationRow), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [ExtraFields](Common.md#Common.ExtraField), [OperationRowControlDataRows](Manufacturing.md#Manufacturing.OperationRowControlDataRow)
**Referenced by:** [AlternativeOperationRows](Manufacturing.md#Manufacturing.AlternativeOperationRow), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [OperationRowControlDataRows](Manufacturing.md#Manufacturing.OperationRowControlDataRow), [Preparations](Manufacturing.md#Manufacturing.Preparation)

<a id="Manufacturing.OrderQuantityManufacturingOrderOperation"></a>
### OrderQuantityManufacturingOrderOperations

Represents a order quantity template on part that holds many partial quantities.

- **Endpoint:** `GET /api/v1/Manufacturing/OrderQuantityManufacturingOrderOperations`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](Common.md#Common.PartialQuantity) |

**References out:** [PartialQuantities](Common.md#Common.PartialQuantity)
**Referenced by:** [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation)

<a id="Manufacturing.OrderQuantityManufacturingOrder"></a>
### OrderQuantityManufacturingOrders

Represents a order quantity template on part that holds many partial quantities.

- **Endpoint:** `GET /api/v1/Manufacturing/OrderQuantityManufacturingOrders`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](Common.md#Common.PartialQuantity) |

**References out:** [PartialQuantities](Common.md#Common.PartialQuantity)
**Referenced by:** [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder)

<a id="Manufacturing.Preparation"></a>
### Preparations

Represents a part preparation

- **Endpoint:** `GET /api/v1/Manufacturing/Preparations`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartNumber` | `String` | no |  |
| `Description` | `String` | no |  |
| `UseVariantManagement` | `Boolean` | no |  |
| `VariantXAxisId` | `Int64?` | yes | [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate) |
| `VariantXAxis` | `ExtraFieldTemplates` | no | [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate) |
| `VariantYAxisId` | `Int64?` | yes | [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate) |
| `VariantYAxis` | `ExtraFieldTemplates` | no | [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate) |
| `Materials` | `MaterialRows[]` | no | [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow) |
| `Operations` | `OperationRows[]` | no | [OperationRows](Manufacturing.md#Manufacturing.OperationRow) |

**References out:** [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate), [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow), [OperationRows](Manufacturing.md#Manufacturing.OperationRow)
**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Manufacturing.ProductionCalendarException"></a>
### ProductionCalendarExceptions

Represents a table that contains exceptions from the production calendar. Only used when using daily planning.

- **Endpoint:** `GET /api/v1/Manufacturing/ProductionCalendarExceptions`
- **Required permission:** Show work center
- **Introduced in:** 24.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `WorkCenterId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) |
| `NumberOfPlanningUnits` | `Decimal?` | yes |  |
| `ExceptionDate` | `DateTime` | no |  |
| `BasicTime` | `TimeSpan?` | yes |  |
| `ScheduleId` | `Int64?` | yes | [Schedules](TimeRecording.md#TimeRecording.Schedule) |

**References out:** [Schedules](TimeRecording.md#TimeRecording.Schedule), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)

<a id="Manufacturing.ReasonCodeTimeConsumption"></a>
### ReasonCodeTimeConsumptions

Represents a reason code time consumption.

- **Endpoint:** `GET /api/v1/Manufacturing/ReasonCodeTimeConsumptions`
- **Required permission:** Show cause codes
- **Introduced in:** 24.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `CommentMandatory` | `Boolean` | no |  |
| `Active` | `Boolean` | no |  |
| `TimeConsumptionType` | `Int32` | no |  |

- `TimeConsumptionType` — TimeLoss=0, TimeGain=1

**Referenced by:** [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting)

<a id="Manufacturing.WorkCenterCostFactorGroup"></a>
### WorkCenterCostFactorGroups

Represents a cost factor group belonging to a work center. Note that all cost factors are represented in company currency per hour.

- **Endpoint:** `GET /api/v1/Manufacturing/WorkCenterCostFactorGroups`
- **Required permission:** Show work center
- **Introduced in:** 2.46

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Type` | `Int32` | no |  |
| `CostFactor1` | `Decimal?` | yes |  |
| `CostFactor2` | `Decimal?` | yes |  |
| `CostFactor3` | `Decimal?` | yes |  |
| `FutureCostFactor1` | `Decimal?` | yes |  |
| `FutureCostFactor2` | `Decimal?` | yes |  |
| `FutureCostFactor3` | `Decimal?` | yes |  |
| `IsDefaultSetupCost` | `Boolean` | no |  |
| `IsDefaultUnitCost` | `Boolean` | no |  |
| `ParentId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) |
| `RowIndex` | `Int32` | no |  |

- `Type` (bitmask) — None=0, SetupCost=1, UnitCost=2

**References out:** [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)

<a id="Manufacturing.WorkCenterManufacturingPrintSettings"></a>
### WorkCenterManufacturingPrintSettings

Represents manufacturing print settings for a work center.

- **Endpoint:** `GET /api/v1/Common/WorkCenterManufacturingPrintSettings`
- **Required permission:** Show work center
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Copies` | `Int32` | no |  |
| `PrintExternalDocuments` | `Boolean` | no |  |
| `FormReportId` | `Int64` | no |  |

**Referenced by:** [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)

<a id="Manufacturing.WorkCenter"></a>
### WorkCenters

Represents a manufacturing work center.

- **Endpoint:** `GET /api/v1/Manufacturing/WorkCenters`
- **Required permission:** Show work center
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `Description` | `String` | no |  |
| `OperationDescription` | `String` | no |  |
| `Type` | `Int32` | no |  |
| `DepartmentId` | `Int64` | no |  |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `Warehouse` | `Warehouses` | no | [Warehouses](Common.md#Common.Warehouse) |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ManufacturingPrintSettings` | `WorkCenterManufacturingPrintSettings[]` | no | [WorkCenterManufacturingPrintSettings](Manufacturing.md#Manufacturing.WorkCenterManufacturingPrintSettings) |
| `CostFactorGroups` | `WorkCenterCostFactorGroups[]` | no | [WorkCenterCostFactorGroups](Manufacturing.md#Manufacturing.WorkCenterCostFactorGroup) |
| `TimePrecision` | `Int32` | no |  |
| `BasicTime` | `TimeSpan` | no |  |
| `NumberOfPlanningUnits` | `Decimal` | no |  |
| `NumberOfFlows` | `Decimal` | no |  |
| `AvailabilityFactor` | `Decimal` | no |  |
| `SimulationFactor` | `Decimal` | no |  |
| `UnitStaffFactor` | `Decimal` | no |  |
| `SetupStaffFactor` | `Decimal` | no |  |
| `Employees` | `PersonWorkCenters[]` | no | [PersonWorkCenters](TimeRecording.md#TimeRecording.PersonWorkCenter) |
| `ProductionCalendarExceptions` | `ProductionCalendarExceptions[]` | no | [ProductionCalendarExceptions](Manufacturing.md#Manufacturing.ProductionCalendarException) |

- `Type` — Machine=0, ManualWork=1, SubContract=2, Pool=3, Pick=4, Staffing=5
- `TimePrecision` — Day=0, Schedule=1, Hourly=2

**References out:** [Comments](Common.md#Common.Comment), [PersonWorkCenters](TimeRecording.md#TimeRecording.PersonWorkCenter), [ProductionCalendarExceptions](Manufacturing.md#Manufacturing.ProductionCalendarException), [Warehouses](Common.md#Common.Warehouse), [WorkCenterCostFactorGroups](Manufacturing.md#Manufacturing.WorkCenterCostFactorGroup), [WorkCenterManufacturingPrintSettings](Manufacturing.md#Manufacturing.WorkCenterManufacturingPrintSettings)
**Referenced by:** [AlternativeOperationRows](Manufacturing.md#Manufacturing.AlternativeOperationRow), [CaseEntry](Inventory.md#Inventory.CaseEntry), [FixedAssets](Accounting.md#Accounting.FixedAsset), [ManufacturingOrderOperationControlDataRows](Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow), [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [OperationRowControlDataRows](Manufacturing.md#Manufacturing.OperationRowControlDataRow), [PersonWorkCenters](TimeRecording.md#TimeRecording.PersonWorkCenter), [ProductionCalendarExceptions](Manufacturing.md#Manufacturing.ProductionCalendarException), [WorkCenterCostFactorGroups](Manufacturing.md#Manufacturing.WorkCenterCostFactorGroup), [WorkIntervals](TimeRecording.md#TimeRecording.WorkInterval)


## Depends on other modules

- [Common](Common.md): [ApplicationUsers](Common.md#Common.ApplicationUser), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [ExtraFields](Common.md#Common.ExtraField), [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate), [FormTemplates](Common.md#Common.FormTemplate), [MeasuringTemplates](Common.md#Common.MeasuringTemplate), [PartConfigurations](Common.md#Common.PartConfiguration), [PartialQuantities](Common.md#Common.PartialQuantity), [Persons](Common.md#Common.Person), [Projects](Common.md#Common.Project), [Revisions](Common.md#Common.Revision), [Units](Common.md#Common.Unit), [Warehouses](Common.md#Common.Warehouse)
- [Inventory](Inventory.md): [Parts](Inventory.md#Inventory.Part), [ProductRecords](Inventory.md#Inventory.ProductRecord), [QuantityChanges](Inventory.md#Inventory.QuantityChange)
- [Purchase](Purchase.md): [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)
- [Sales](Sales.md): [Customers](Sales.md#Sales.Customer), [CustomerOrders](Sales.md#Sales.CustomerOrder)
- [TimeRecording](TimeRecording.md): [PersonWorkCenters](TimeRecording.md#TimeRecording.PersonWorkCenter), [Schedules](TimeRecording.md#TimeRecording.Schedule)
