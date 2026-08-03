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
| `OperationRowId` | `Int64` | no | [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow) |
| `WorkCenterId` | `Int64` | no | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |
| `UnitStaffingFactor` | `Decimal?` | yes |  |
| `SetupStaffingFactor` | `Decimal?` | yes |  |
| `QueueTime` | `TimeSpan?` | yes |  |
| `SetupTime` | `TimeSpan?` | yes |  |
| `UnitTime` | `TimeSpan?` | yes |  |
| `CycleTime` | `TimeSpan?` | yes |  |

**References out:** [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow)

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
| `ParentId` | `Int64?` | yes | [Drawings](/modules/Manufacturing.md#Manufacturing.Drawing) |
| `RevisionCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `RevisionComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

**References out:** [Comments](/modules/Common.md#Common.Comment), [Drawings](/modules/Manufacturing.md#Manufacturing.Drawing)
**Referenced by:** [Drawings](/modules/Manufacturing.md#Manufacturing.Drawing)

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
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Revisions` | `DrawingRevisions[]` | no | [DrawingRevisions](/modules/Manufacturing.md#Manufacturing.DrawingRevision) |
| `ActiveDrawingRevisionId` | `Int64?` | yes | [DrawingRevisions](/modules/Manufacturing.md#Manufacturing.DrawingRevision) |

**References out:** [DrawingRevisions](/modules/Manufacturing.md#Manufacturing.DrawingRevision), [Parts](/modules/Inventory.md#Inventory.Part)
**Referenced by:** [DrawingRevisions](/modules/Manufacturing.md#Manufacturing.DrawingRevision), [Parts](/modules/Inventory.md#Inventory.Part)

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
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Instruction` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `InstructionId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Description` | `String` | no |  |
| `MaintenanceReportingSelectionRowId` | `Int64` | no | [MaintenanceReportingSelectionRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow) |
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
| `MasterToolId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `MasterToolProductRecordId` | `Int64?` | yes | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `UnitId` | `Int64?` | yes | [Units](/modules/Common.md#Common.Unit) |

- `Type` — Decimal=0, Text=1, CheckBox=2, Date=3
- `ReportingStatus` — Ok=0, NotOk=1, OkWithAction=2

**References out:** [Comments](/modules/Common.md#Common.Comment), [MaintenanceReportingSelectionRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow), [Parts](/modules/Inventory.md#Inventory.Part), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [Units](/modules/Common.md#Common.Unit)
**Referenced by:** [MaintenanceReportingSelectionRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow)

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
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ManufacturingOrder` | `ManufacturingOrders` | no | [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ProductRecordId` | `Int64` | no |  |
| `ProductRecord` | `ProductRecords` | no | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `MaintenanceRowId` | `Int64` | no |  |
| `ShortComment` | `String` | no |  |
| `CommentId` | `Int64` | no | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `MaintenanceStatus` | `Int32?` | yes |  |
| `ReportedById` | `Int64` | no | [Persons](/modules/Common.md#Common.Person) |
| `ReportedBy` | `Persons` | no | [Persons](/modules/Common.md#Common.Person) |
| `ReportingStatus` | `Int32` | no |  |
| `ActualDate` | `DateTimeOffset?` | yes |  |
| `Status` | `Int32` | no |  |
| `NextOccurrence` | `DateTimeOffset?` | yes |  |
| `ColorCode` | `Int32?` | yes |  |
| `InstructionId` | `Int64` | no |  |
| `Instruction` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `MaintenanceReportingSelectionRows` | `MaintenanceReportingSelectionRows[]` | no | [MaintenanceReportingSelectionRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow) |

- `MaintenanceStatus` — Ok=0, NotOk=1, OkWithAction=2
- `ReportingStatus` — New=0, InProgress=1, Finished=2
- `Status` — ApprovalForUse=0, NonApproval=1, ServicePastDue=2, UnderServiceOrCalibration=3, Rejected=4, ServiceOrCalibrationBeforeUse=5, Missing=6, Scrapped=7

**References out:** [Comments](/modules/Common.md#Common.Comment), [MaintenanceReportingSelectionRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [Persons](/modules/Common.md#Common.Person), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord)
**Referenced by:** [MaintenanceReportingSelectionRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow)

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
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Description` | `String` | no |  |
| `MaintenanceReportingId` | `Int64` | no | [MaintenanceReportings](/modules/Manufacturing.md#Manufacturing.MaintenanceReporting) |
| `RowIndex` | `Int32?` | yes |  |
| `MaintenanceReportingRows` | `MaintenanceReportingRows[]` | no | [MaintenanceReportingRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingRow) |

**References out:** [Comments](/modules/Common.md#Common.Comment), [MaintenanceReportingRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingRow), [MaintenanceReportings](/modules/Manufacturing.md#Manufacturing.MaintenanceReporting)
**Referenced by:** [MaintenanceReportingRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingRow), [MaintenanceReportings](/modules/Manufacturing.md#Manufacturing.MaintenanceReporting)

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

**Referenced by:** [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation)

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
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `ToOperationNumber` | `Int32` | no |  |
| `ReportedQuantity` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `PlannedQuantity` | `Decimal` | no |  |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode) |
| `PositionNumber` | `String` | no |  |
| `InstructionCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `InstructionComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `QuantityPerUnit` | `Decimal` | no |  |
| `CycleTime` | `TimeSpan?` | yes |  |
| `EditedStatus` | `Int32` | no |  |
| `ExtraQuantityProcent` | `Decimal` | no |  |
| `LinkedPurchaseOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow) |
| `LockedToBatchNo` | `String` | no |  |
| `QuantityPerCycle` | `Decimal?` | yes |  |
| `RejectedQuantity` | `Decimal` | no |  |
| `ReportedSetupQuantity` | `Decimal` | no |  |
| `RestSetupQuantity` | `Decimal` | no |  |
| `SetupQuantity` | `Decimal` | no |  |
| `MaterialRowOriginId` | `Int64?` | yes |  |

- `EditedStatus` (bitmask) — NotEdited=0, Edited=1, Synchronized=2

**References out:** [Comments](/modules/Common.md#Common.Comment), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](/modules/Inventory.md#Inventory.Part), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow)
**Referenced by:** [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [ManufacturingPickingListMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingPickingListMaterial)

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
| `ParentId` | `Int64?` | yes | [ManufacturingOrderNodeDrawings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing) |
| `RevisionCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `RevisionComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

**References out:** [Comments](/modules/Common.md#Common.Comment), [ManufacturingOrderNodeDrawings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing)
**Referenced by:** [ManufacturingOrderNodeDrawings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing)

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
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode) |
| `Revisions` | `ManufacturingOrderNodeDrawingRevisions[]` | no | [ManufacturingOrderNodeDrawingRevisions](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision) |
| `ActiveDrawingRevisionId` | `Int64?` | yes | [ManufacturingOrderNodeDrawingRevisions](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision) |

**References out:** [ManufacturingOrderNodeDrawingRevisions](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode)
**Referenced by:** [ManufacturingOrderNodeDrawingRevisions](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode)

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
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `ReportedQuantity` | `Decimal` | no |  |
| `PlannedQuantity` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `StartDate` | `DateTimeOffset` | no |  |
| `EndDate` | `DateTimeOffset` | no |  |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Status` | `Int32` | no |  |
| `ManufacturingOrderNodeId` | `Int64?` | yes | [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode) |
| `Drawings` | `ManufacturingOrderNodeDrawings[]` | no | [ManufacturingOrderNodeDrawings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing) |
| `RevisionId` | `Int64?` | yes | [Revisions](/modules/Common.md#Common.Revision) |
| `Revision` | `Revisions` | no | [Revisions](/modules/Common.md#Common.Revision) |
| `SerialNumberProductRecords` | `ProductRecords[]` | no | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |

- `Status` — NotInitialized=0, Registrered=1, Printed=2, Started=3, Finished=4, PostCalculated=5, Delivered=6, Historical=9

**References out:** [ManufacturingOrderNodeDrawings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode), [Parts](/modules/Inventory.md#Inventory.Part), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [Revisions](/modules/Common.md#Common.Revision), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodeDrawings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder)

<a id="Manufacturing.ManufacturingOrderOperationControlDataRow"></a>
### ManufacturingOrderOperationControlDataRows

Represents a measuring plan for a manufacturing order operation.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderOperationControlDataRows`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ManufacturingOrderOperationId` | `Int64` | no | [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](/modules/Common.md#Common.MeasuringTemplate) |
| `OverridenFormTemplateId` | `Int64` | no | [FormTemplates](/modules/Common.md#Common.FormTemplate) |
| `OverridenFrequencyText` | `String` | no |  |
| `OverridenIntervalAmount` | `Int32?` | yes |  |
| `OverridenInterval` | `Int32?` | yes |  |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |

**References out:** [FormTemplates](/modules/Common.md#Common.FormTemplate), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [MeasuringTemplates](/modules/Common.md#Common.MeasuringTemplate), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation)

<a id="Manufacturing.ManufacturingOrderOperationReporting"></a>
### ManufacturingOrderOperationReportings

Represents a manufacturing order operation reporting.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderOperationReportings`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 24.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OperationId` | `Int64` | no | [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `Quantity` | `Decimal` | no |  |
| `SetupTime` | `TimeSpan?` | yes |  |
| `UnitTime` | `TimeSpan?` | yes |  |
| `WorkCenterId` | `Int64` | no | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |
| `EmployeeId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `ReportingEmployeeId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
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
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `ReasonCodeTimeConsumptionId` | `Int64?` | yes | [ReasonCodeTimeConsumptions](/modules/Manufacturing.md#Manufacturing.ReasonCodeTimeConsumption) |
| `ReasonCodeTimeConsumption` | `ReasonCodeTimeConsumptions` | no | [ReasonCodeTimeConsumptions](/modules/Manufacturing.md#Manufacturing.ReasonCodeTimeConsumption) |
| `AutomaticMaterialReporting` | `Boolean` | no |  |
| `PurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](/modules/Purchase.md#Purchase.PurchaseOrderDeliveryRow) |
| `PreviousNodeStatus` | `Int32` | no |  |
| `OriginalApprovedQuantityFromDeliveryRow` | `Decimal?` | yes |  |
| `ReportingId` | `Int64?` | yes |  |
| `ReportingTimestamp` | `DateTimeOffset` | no |  |
| `RowNumber` | `Int32` | no |  |

- `Type` — Regular=0, SendToSubcontractor=1, ReceiveFromSubcontractor=2, CancelRest=3, MaterialOnly=4, SubcontractorInvoicePrice=5, RecordingTerminal=6, AdjustRecording=7, UndoRegular=8, UndoRecordingTerminal=9, UndoAdjustRecording=10, SubcontractorPosteriorReport=11, SubcontractorCostsManualReport=12, PickWorkCenter=13
- `PreviousNodeStatus` — NotInitialized=0, Registrered=1, Printed=2, Started=3, Finished=4, PostCalculated=5, Delivered=6, Historical=9

**References out:** [Comments](/modules/Common.md#Common.Comment), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [Persons](/modules/Common.md#Common.Person), [PurchaseOrderDeliveryRows](/modules/Purchase.md#Purchase.PurchaseOrderDeliveryRow), [ReasonCodeTimeConsumptions](/modules/Manufacturing.md#Manufacturing.ReasonCodeTimeConsumption), [Warehouses](/modules/Common.md#Common.Warehouse), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [Locations](/modules/Inventory.md#Inventory.Location)

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
| `WorkCenterId` | `Int64` | no | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `PlannedQuantity` | `Decimal` | no |  |
| `ReportedQuantity` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `ReportedSetupTime` | `TimeSpan` | no |  |
| `ReportedUnitTime` | `TimeSpan` | no |  |
| `RejectedQuantity` | `Decimal` | no |  |
| `WipLocation` | `String` | no |  |
| `ReportNumber` | `Int64` | no |  |
| `InstructionCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `InstructionComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode) |
| `OperationNumber` | `Int32` | no |  |
| `PlannedSetupTime` | `TimeSpan` | no |  |
| `PlannedUnitTime` | `TimeSpan` | no |  |
| `PlannedStartDate` | `DateTimeOffset` | no |  |
| `PlannedFinishDate` | `DateTimeOffset` | no |  |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |
| `ActualFinishDate` | `DateTimeOffset?` | yes |  |
| `OperationRowId` | `Int64?` | yes | [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow) |
| `OperationRow` | `OperationRows` | no | [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow) |
| `Status` | `Int32` | no |  |
| `WorkshopOperationStatus` | `Int32` | no |  |
| `BundleId` | `Int64?` | yes |  |
| `Description` | `String` | no |  |
| `ControlDataRows` | `ManufacturingOrderOperationControlDataRows[]` | no | [ManufacturingOrderOperationControlDataRows](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow) |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrderOperation) |
| `OrderQuantity` | `OrderQuantityManufacturingOrderOperations` | no | [OrderQuantityManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrderOperation) |
| `ClearedStatus` | `Boolean` | no |  |
| `OnPriorityPlan` | `Boolean` | no |  |
| `ManualOperationStatusId` | `Int64?` | yes | [ManualOperationStatuses](/modules/Manufacturing.md#Manufacturing.ManualOperationStatus) |
| `ManualOperationStatus` | `ManualOperationStatuses` | no | [ManualOperationStatuses](/modules/Manufacturing.md#Manufacturing.ManualOperationStatus) |
| `Materials` | `ManufacturingOrderMaterials[]` | no | [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) |
| `FixedLeadTime` | `TimeSpan?` | yes |  |
| `UnitStaffingFactor` | `Decimal?` | yes |  |
| `SetupStaffingFactor` | `Decimal?` | yes |  |
| `IsPlannedTimeCalculated` | `Boolean` | no |  |

- `Status` — None=0, Started=1, PartiallyShipped=2, FullyShipped=3, PartiallyReported=4, Finished=5
- `WorkshopOperationStatus` — NotInitialized=0, InProgress=1, ClockedOut=2, Interrupted=3, PartiallyReported=4, SetupTime=5, IsStandingBy=6, Finished=9

**References out:** [Comments](/modules/Common.md#Common.Comment), [ManualOperationStatuses](/modules/Manufacturing.md#Manufacturing.ManualOperationStatus), [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperationControlDataRows](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow), [OrderQuantityManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrderOperation), [Parts](/modules/Inventory.md#Inventory.Part), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [DelegatedWork](/modules/Common.md#Common.DelegatedWork), [IndirectWorkCodes](/modules/TimeRecording.md#TimeRecording.IndirectWorkCode), [ManufacturingOrderOperationControlDataRows](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow), [ManufacturingOrderOperationReportings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow), [StandbyWorks](/modules/TimeRecording.md#TimeRecording.StandbyWork), [WorkIntervals](/modules/TimeRecording.md#TimeRecording.WorkInterval)

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
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `ReportedQuantity` | `Decimal` | no |  |
| `PlannedQuantity` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `StartDate` | `DateTimeOffset` | no |  |
| `FinishDate` | `DateTimeOffset` | no |  |
| `Priority` | `Int32` | no |  |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `Operations` | `ManufacturingOrderOperations[]` | no | [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `Materials` | `ManufacturingOrderMaterials[]` | no | [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) |
| `Nodes` | `ManufacturingOrderNodes[]` | no | [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode) |
| `ProjectId` | `Int64?` | yes | [Projects](/modules/Common.md#Common.Project) |
| `Project` | `Projects` | no | [Projects](/modules/Common.md#Common.Project) |
| `CategoryString` | `String` | no |  |
| `VariantCode` | `String` | no |  |
| `CustomerId` | `Int64?` | yes | [Customers](/modules/Sales.md#Sales.Customer) |
| `InitialFinishDate` | `DateTimeOffset` | no |  |
| `PartConfigurationId` | `Int64?` | yes | [PartConfigurations](/modules/Common.md#Common.PartConfiguration) |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityManufacturingOrders](/modules/Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder) |
| `OrderQuantity` | `OrderQuantityManufacturingOrders` | no | [OrderQuantityManufacturingOrders](/modules/Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder) |
| `OrderTypeId` | `Int64?` | yes | [ManufacturingOrderTypes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderType) |
| `OrderType` | `ManufacturingOrderTypes` | no | [ManufacturingOrderTypes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderType) |

- `Status` — NotInitialized=0, Registrered=1, Printed=2, Started=3, Finished=4, PostCalculated=5, Delivered=6, Historical=9

**References out:** [Comments](/modules/Common.md#Common.Comment), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [Customers](/modules/Sales.md#Sales.Customer), [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrderTypes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderType), [OrderQuantityManufacturingOrders](/modules/Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder), [PartConfigurations](/modules/Common.md#Common.PartConfiguration), [Parts](/modules/Inventory.md#Inventory.Part), [Projects](/modules/Common.md#Common.Project), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [Locations](/modules/Inventory.md#Inventory.Location), [MaintenanceReportings](/modules/Manufacturing.md#Manufacturing.MaintenanceReporting), [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord)

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

**Referenced by:** [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder)

<a id="Manufacturing.ManufacturingPickingListMaterial"></a>
### ManufacturingPickingListMaterials

Represents a manufacturing picking list material.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingPickingListMaterials`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.48

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `MaterialId` | `Int64` | no | [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) |
| `Material` | `ManufacturingOrderMaterials` | no | [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) |
| `QuantityChangeId` | `Int64` | no | [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange) |
| `QuantityChange` | `QuantityChanges` | no | [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange) |

**References out:** [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange)
**Referenced by:** [ManufacturingPickingLists](/modules/Manufacturing.md#Manufacturing.ManufacturingPickingList)

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
| `CreatedByApplicationUserId` | `Int64` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `CreatedByPersonId` | `Int64` | no | [Persons](/modules/Common.md#Common.Person) |
| `CreatedTimestamp` | `DateTimeOffset` | no |  |
| `PrintedByApplicationUserId` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `PrintedByPersonId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `PrintedTimestamp` | `DateTimeOffset?` | yes |  |
| `Status` | `Int32` | no |  |
| `Grouping` | `Int32` | no |  |
| `Sorting` | `Int32` | no |  |
| `WarehouseId` | `Int64?` | yes | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Type` | `Int32` | no |  |
| `Materials` | `ManufacturingPickingListMaterials[]` | no | [ManufacturingPickingListMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingPickingListMaterial) |

- `Status` — Registered=1, Printed=2, Reported=5, History=9
- `Grouping` — Order=0, Material=1, NoGrouping=2
- `Sorting` — Location=0, MainLocation=1, MaterialPartNumber=2, LocationSortingOrder=3, MainLocationSortingOrder=4
- `Type` — Regular=0, Equipment=1

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [ManufacturingPickingListMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingPickingListMaterial), [Persons](/modules/Common.md#Common.Person), [Warehouses](/modules/Common.md#Common.Warehouse)

<a id="Manufacturing.ReferenceNumber"></a>
### MaterialRowReferenceNumbers

Represents a reference number attached to a material row.

- **Endpoint:** `GET /api/v1/Manufacturing/MaterialRowReferenceNumbers`
- **Required permission:** Show part
- **Introduced in:** 26.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `MaterialRowId` | `Int64` | no | [MaterialRows](/modules/Manufacturing.md#Manufacturing.MaterialRow) |
| `Prefix` | `String` | no |  |
| `From` | `String` | no |  |
| `To` | `String` | no |  |
| `Suffix` | `String` | no |  |
| `Remark` | `String` | no |  |
| `Quantity` | `Decimal` | no |  |
| `RowIndex` | `Int32?` | yes |  |

**References out:** [MaterialRows](/modules/Manufacturing.md#Manufacturing.MaterialRow)
**Referenced by:** [MaterialRows](/modules/Manufacturing.md#Manufacturing.MaterialRow)

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
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
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
| `ReferenceNumbers` | `MaterialRowReferenceNumbers[]` | no | [MaterialRowReferenceNumbers](/modules/Manufacturing.md#Manufacturing.ReferenceNumber) |

**References out:** [Comments](/modules/Common.md#Common.Comment), [MaterialRowReferenceNumbers](/modules/Manufacturing.md#Manufacturing.ReferenceNumber)
**Referenced by:** [MaterialRowReferenceNumbers](/modules/Manufacturing.md#Manufacturing.ReferenceNumber), [Preparations](/modules/Manufacturing.md#Manufacturing.Preparation)

<a id="Manufacturing.OperationRowControlDataRow"></a>
### OperationRowControlDataRows

Represents a measuring plan for an operation row.

- **Endpoint:** `GET /api/v1/Manufacturing/OperationRowControlDataRows`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OperationRowId` | `Int64` | no | [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow) |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](/modules/Common.md#Common.MeasuringTemplate) |
| `OverriddenFormTemplateId` | `Int64?` | yes | [FormTemplates](/modules/Common.md#Common.FormTemplate) |
| `OverriddenFrequencyText` | `String` | no |  |
| `OverriddenIntervalAmount` | `Int32?` | yes |  |
| `OverriddenInterval` | `Int32?` | yes |  |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |

**References out:** [FormTemplates](/modules/Common.md#Common.FormTemplate), [MeasuringTemplates](/modules/Common.md#Common.MeasuringTemplate), [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow)

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
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
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
| `SetupCostCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `UnitCost` | `Decimal?` | yes |  |
| `UnitCostCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `TransportCost` | `Decimal?` | yes |  |
| `SupplierPartNumber` | `String` | no |  |
| `DeliverToEndCustomer` | `Boolean` | no |  |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](/modules/Common.md#Common.ExtraField) |
| `ControlDataRows` | `OperationRowControlDataRows[]` | no | [OperationRowControlDataRows](/modules/Manufacturing.md#Manufacturing.OperationRowControlDataRow) |
| `AlternativeOperationRows` | `AlternativeOperationRows[]` | no | [AlternativeOperationRows](/modules/Manufacturing.md#Manufacturing.AlternativeOperationRow) |
| `PreparationTermType` | `Int32?` | yes |  |
| `PreparationTermFromValue` | `String` | no |  |
| `PreparationTermToValue` | `String` | no |  |

- `TimeCode` — NotInitialized=0, Calculated=1, Studied=2
- `TimeUnit` — Hours=0, Minutes=1, Seconds=2, QuantityPerHour=3, QuantityPerMinute=4, QuantityPerSecond=5

**References out:** [AlternativeOperationRows](/modules/Manufacturing.md#Manufacturing.AlternativeOperationRow), [Comments](/modules/Common.md#Common.Comment), [Currencies](/modules/Common.md#Common.Currency), [ExtraFields](/modules/Common.md#Common.ExtraField), [OperationRowControlDataRows](/modules/Manufacturing.md#Manufacturing.OperationRowControlDataRow)
**Referenced by:** [AlternativeOperationRows](/modules/Manufacturing.md#Manufacturing.AlternativeOperationRow), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [OperationRowControlDataRows](/modules/Manufacturing.md#Manufacturing.OperationRowControlDataRow), [Preparations](/modules/Manufacturing.md#Manufacturing.Preparation)

<a id="Manufacturing.OrderQuantityManufacturingOrderOperation"></a>
### OrderQuantityManufacturingOrderOperations

Represents a order quantity template on part that holds many partial quantities.

- **Endpoint:** `GET /api/v1/Manufacturing/OrderQuantityManufacturingOrderOperations`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](/modules/Common.md#Common.PartialQuantity) |

**References out:** [PartialQuantities](/modules/Common.md#Common.PartialQuantity)
**Referenced by:** [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation)

<a id="Manufacturing.OrderQuantityManufacturingOrder"></a>
### OrderQuantityManufacturingOrders

Represents a order quantity template on part that holds many partial quantities.

- **Endpoint:** `GET /api/v1/Manufacturing/OrderQuantityManufacturingOrders`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](/modules/Common.md#Common.PartialQuantity) |

**References out:** [PartialQuantities](/modules/Common.md#Common.PartialQuantity)
**Referenced by:** [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder)

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
| `VariantXAxisId` | `Int64?` | yes | [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate) |
| `VariantXAxis` | `ExtraFieldTemplates` | no | [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate) |
| `VariantYAxisId` | `Int64?` | yes | [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate) |
| `VariantYAxis` | `ExtraFieldTemplates` | no | [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate) |
| `Materials` | `MaterialRows[]` | no | [MaterialRows](/modules/Manufacturing.md#Manufacturing.MaterialRow) |
| `Operations` | `OperationRows[]` | no | [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow) |

**References out:** [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate), [MaterialRows](/modules/Manufacturing.md#Manufacturing.MaterialRow), [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow)
**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Manufacturing.ProductionCalendarException"></a>
### ProductionCalendarExceptions

Represents a table that contains exceptions from the production calendar. Only used when using daily planning.

- **Endpoint:** `GET /api/v1/Manufacturing/ProductionCalendarExceptions`
- **Required permission:** Show work center
- **Introduced in:** 24.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `WorkCenterId` | `Int64` | no | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |
| `NumberOfPlanningUnits` | `Decimal?` | yes |  |
| `ExceptionDate` | `DateTime` | no |  |
| `BasicTime` | `TimeSpan?` | yes |  |
| `ScheduleId` | `Int64?` | yes | [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule) |

**References out:** [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)

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

**Referenced by:** [ManufacturingOrderOperationReportings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting)

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
| `ParentId` | `Int64` | no | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |
| `RowIndex` | `Int32` | no |  |

- `Type` (bitmask) — None=0, SetupCost=1, UnitCost=2

**References out:** [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)

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

**Referenced by:** [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)

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
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Warehouse` | `Warehouses` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `ManufacturingPrintSettings` | `WorkCenterManufacturingPrintSettings[]` | no | [WorkCenterManufacturingPrintSettings](/modules/Manufacturing.md#Manufacturing.WorkCenterManufacturingPrintSettings) |
| `CostFactorGroups` | `WorkCenterCostFactorGroups[]` | no | [WorkCenterCostFactorGroups](/modules/Manufacturing.md#Manufacturing.WorkCenterCostFactorGroup) |
| `TimePrecision` | `Int32` | no |  |
| `BasicTime` | `TimeSpan` | no |  |
| `NumberOfPlanningUnits` | `Decimal` | no |  |
| `NumberOfFlows` | `Decimal` | no |  |
| `AvailabilityFactor` | `Decimal` | no |  |
| `SimulationFactor` | `Decimal` | no |  |
| `UnitStaffFactor` | `Decimal` | no |  |
| `SetupStaffFactor` | `Decimal` | no |  |
| `Employees` | `PersonWorkCenters[]` | no | [PersonWorkCenters](/modules/TimeRecording.md#TimeRecording.PersonWorkCenter) |
| `ProductionCalendarExceptions` | `ProductionCalendarExceptions[]` | no | [ProductionCalendarExceptions](/modules/Manufacturing.md#Manufacturing.ProductionCalendarException) |

- `Type` — Machine=0, ManualWork=1, SubContract=2, Pool=3, Pick=4, Staffing=5
- `TimePrecision` — Day=0, Schedule=1, Hourly=2

**References out:** [Comments](/modules/Common.md#Common.Comment), [PersonWorkCenters](/modules/TimeRecording.md#TimeRecording.PersonWorkCenter), [ProductionCalendarExceptions](/modules/Manufacturing.md#Manufacturing.ProductionCalendarException), [Warehouses](/modules/Common.md#Common.Warehouse), [WorkCenterCostFactorGroups](/modules/Manufacturing.md#Manufacturing.WorkCenterCostFactorGroup), [WorkCenterManufacturingPrintSettings](/modules/Manufacturing.md#Manufacturing.WorkCenterManufacturingPrintSettings)
**Referenced by:** [AlternativeOperationRows](/modules/Manufacturing.md#Manufacturing.AlternativeOperationRow), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [FixedAssets](/modules/Accounting.md#Accounting.FixedAsset), [ManufacturingOrderOperationControlDataRows](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow), [ManufacturingOrderOperationReportings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [OperationRowControlDataRows](/modules/Manufacturing.md#Manufacturing.OperationRowControlDataRow), [PersonWorkCenters](/modules/TimeRecording.md#TimeRecording.PersonWorkCenter), [ProductionCalendarExceptions](/modules/Manufacturing.md#Manufacturing.ProductionCalendarException), [WorkCenterCostFactorGroups](/modules/Manufacturing.md#Manufacturing.WorkCenterCostFactorGroup), [WorkIntervals](/modules/TimeRecording.md#TimeRecording.WorkInterval)


## Depends on other modules

- [Common](/modules/Common.md): [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Comments](/modules/Common.md#Common.Comment), [Currencies](/modules/Common.md#Common.Currency), [ExtraFields](/modules/Common.md#Common.ExtraField), [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate), [FormTemplates](/modules/Common.md#Common.FormTemplate), [MeasuringTemplates](/modules/Common.md#Common.MeasuringTemplate), [PartConfigurations](/modules/Common.md#Common.PartConfiguration), [PartialQuantities](/modules/Common.md#Common.PartialQuantity), [Persons](/modules/Common.md#Common.Person), [Projects](/modules/Common.md#Common.Project), [Revisions](/modules/Common.md#Common.Revision), [Units](/modules/Common.md#Common.Unit), [Warehouses](/modules/Common.md#Common.Warehouse)
- [Inventory](/modules/Inventory.md): [Parts](/modules/Inventory.md#Inventory.Part), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange)
- [Purchase](/modules/Purchase.md): [PurchaseOrderDeliveryRows](/modules/Purchase.md#Purchase.PurchaseOrderDeliveryRow), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow)
- [Sales](/modules/Sales.md): [Customers](/modules/Sales.md#Sales.Customer), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder)
- [TimeRecording](/modules/TimeRecording.md): [PersonWorkCenters](/modules/TimeRecording.md#TimeRecording.PersonWorkCenter), [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule)
