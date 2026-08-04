# Manufacturing

Monitor API module `Manufacturing`: 30 queryable entities, 0 commands, 0 payload types.

## Queryable entities

<a id="Manufacturing.AlternativeOperationRow"></a>
### AlternativeOperationRows

Represents an alternative work center on an operation row.

- **Endpoint:** `GET /api/v1/Manufacturing/AlternativeOperationRows`
- **Required permission:** Show part
- **Introduced in:** 26.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the alternative operation row. |
| `OperationRowId` | `Int64` | no | [OperationRows](Manufacturing.md#Manufacturing.OperationRow) | The business key identifier of the operation row that owns this alternative. |
| `WorkCenterId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier of the alternative work center. |
| `UnitStaffingFactor` | `Decimal?` | yes |  | The unit staffing factor of the alternative operation row. |
| `SetupStaffingFactor` | `Decimal?` | yes |  | The setup staffing factor of the alternative operation row. |
| `QueueTime` | `TimeSpan?` | yes |  | The queue time of the alternative operation row. |
| `SetupTime` | `TimeSpan?` | yes |  | The setup time of the alternative operation row. |
| `UnitTime` | `TimeSpan?` | yes |  | The unit time of the alternative operation row. |
| `CycleTime` | `TimeSpan?` | yes |  | The cycle time of the alternative operation row. |

**References out:** [OperationRows](Manufacturing.md#Manufacturing.OperationRow), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [OperationRows](Manufacturing.md#Manufacturing.OperationRow)

<a id="Manufacturing.DrawingRevision"></a>
### DrawingRevisions

Represents a drawing revision.

- **Endpoint:** `GET /api/v1/Manufacturing/DrawingRevisions`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the revision. |
| `Number` | `String` | no |  | The human readable number of the revision. |
| `ParentId` | `Int64?` | yes | [Drawings](Manufacturing.md#Manufacturing.Drawing) | The business key identifier of the drawing that the revision belongs to. |
| `RevisionCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the revision comment. |
| `RevisionComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The revision comment. |

**References out:** [Comments](Common.md#Common.Comment), [Drawings](Manufacturing.md#Manufacturing.Drawing)
**Referenced by:** [Drawings](Manufacturing.md#Manufacturing.Drawing)

<a id="Manufacturing.Drawing"></a>
### Drawings

Represents a drawing.

- **Endpoint:** `GET /api/v1/Manufacturing/Drawings`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the drawing. |
| `DrawingNumber` | `String` | no |  | The human readable number of the drawing. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the drawing belongs to. |
| `Revisions` | `DrawingRevisions[]` | no | [DrawingRevisions](Manufacturing.md#Manufacturing.DrawingRevision) | A collection of revisions that belong the the drawing. |
| `ActiveDrawingRevisionId` | `Int64?` | yes | [DrawingRevisions](Manufacturing.md#Manufacturing.DrawingRevision) | The business key identifier of the active drawing revision. |

**References out:** [DrawingRevisions](Manufacturing.md#Manufacturing.DrawingRevision), [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [DrawingRevisions](Manufacturing.md#Manufacturing.DrawingRevision), [Parts](Inventory.md#Inventory.Part)

<a id="Manufacturing.MaintenanceReportingRow"></a>
### MaintenanceReportingRows

Represents a maintenance reporting row.

- **Endpoint:** `GET /api/v1/Manufacturing/MaintenanceReportingRows`
- **Required permission:** Show maintenance plan
- **Introduced in:** 25.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `Code` | `String` | no |  | The human readable identifier of the maintenance reporting row. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the maintenance reporting row. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the maintenance reporting row's comment. |
| `Instruction` | `Comments` | no | [Comments](Common.md#Common.Comment) | The instruction of the maintenance reporting row. |
| `InstructionId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the maintenance reporting row's instruction. |
| `Description` | `String` | no |  | The translated description of the maintenance reporting row. |
| `MaintenanceReportingSelectionRowId` | `Int64` | no | [MaintenanceReportingSelectionRows](Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow) | The business key identifier of the maintenance reporting selection row that the maintenance reporting row relates to. |
| `RowIndex` | `Int32?` | yes |  | The row index of the maintenance reporting row. |
| `Checkbox` | `Boolean` | no |  | The boolean value of the maintenance reporting row. |
| `DateTimeValue` | `DateTimeOffset?` | yes |  | The timestamp of the maintenance reporting row. |
| `Number` | `Decimal?` | yes |  | The numeric value of the maintenance reporting row. |
| `TextValue` | `String` | no |  | The text value of the maintenance reporting row. |
| `Type` | `Int32` | no |  | The type of the value stored in the maintenance reporting row. |
| `ReportingStatus` | `Int32?` | yes |  | The status of the value stored in the maintenance reporting row. |
| `MinValue` | `Decimal?` | yes |  | The minimum tolerance value of the maintenance reporting row. |
| `MaxValue` | `Decimal?` | yes |  | The maximum tolerance value of the maintenance reporting row. |
| `Value` | `Decimal?` | yes |  | The setpoint value of the maintenance reporting row. |
| `MasterToolId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the tool that the maintenance reporting row relates to. |
| `MasterToolProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the tool's product record that the maintenance reporting row relates to. |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the unit of the maintenance reporting row's value. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the maintenance reporting. |
| `SerialNumber` | `String` | no |  | The serial number of the maintenance reporting. |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) | The business key identifier of the manufacturing order. |
| `ManufacturingOrder` | `ManufacturingOrders` | no | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) | The maintenance reporting manufacturing order. |
| `ProductRecordId` | `Int64` | no |  | The business key identifier of product record. |
| `ProductRecord` | `ProductRecords` | no | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The product record of the maintenance reporting. |
| `MaintenanceRowId` | `Int64` | no |  | The business key identifier of the maintenance row. |
| `ShortComment` | `String` | no |  | The short comment of the maintenance reporting. |
| `CommentId` | `Int64` | no | [Comments](Common.md#Common.Comment) | The business key identifier of the comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the maintenance reporting. |
| `MaintenanceStatus` | `Int32?` | yes |  | The maintenance status of the maintenance reporting. |
| `ReportedById` | `Int64` | no | [Persons](Common.md#Common.Person) | The business key identifier of person that reported on the maintenance reporting. |
| `ReportedBy` | `Persons` | no | [Persons](Common.md#Common.Person) | The person that reported in the maintenance reporting. |
| `ReportingStatus` | `Int32` | no |  | The reporting status of the maintenance reporting. |
| `ActualDate` | `DateTimeOffset?` | yes |  | The actual date of the maintenance reporting. |
| `Status` | `Int32` | no |  | The serial number status of the maintenance reporting. |
| `NextOccurrence` | `DateTimeOffset?` | yes |  | The next occurrence of the maintenance reporting. |
| `ColorCode` | `Int32?` | yes |  | The color code of the maintenance reporting. |
| `InstructionId` | `Int64` | no |  | The business key identifier of the instruction. |
| `Instruction` | `Comments` | no | [Comments](Common.md#Common.Comment) | The instruction of the maintenance reporting. |
| `MaintenanceReportingSelectionRows` | `MaintenanceReportingSelectionRows[]` | no | [MaintenanceReportingSelectionRows](Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow) | The maintenance reporting selection rows. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `Code` | `String` | no |  | The human readable identifier of the maintenance reporting selection row. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the maintenance reporting selection row. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the maintenance reporting selection row's comment. |
| `Description` | `String` | no |  | The translated description of the maintenance reporting selection row. |
| `MaintenanceReportingId` | `Int64` | no | [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting) | The business key identifier of the maintenance reporting that the maintenance reporting selection row relates to. |
| `RowIndex` | `Int32?` | yes |  | The row index of the maintenance reporting selection row. |
| `MaintenanceReportingRows` | `MaintenanceReportingRows[]` | no | [MaintenanceReportingRows](Manufacturing.md#Manufacturing.MaintenanceReportingRow) | The maintenance reporting rows. |

**References out:** [Comments](Common.md#Common.Comment), [MaintenanceReportingRows](Manufacturing.md#Manufacturing.MaintenanceReportingRow), [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting)
**Referenced by:** [MaintenanceReportingRows](Manufacturing.md#Manufacturing.MaintenanceReportingRow), [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting)

<a id="Manufacturing.ManualOperationStatus"></a>
### ManualOperationStatuses

Represents a manual operation status.

- **Endpoint:** `GET /api/v1/Manufacturing/ManualOperationStatuses`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 25.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the manual operation status. |
| `Code` | `String` | no |  | The human readable identifier of the manual operation status. |
| `Description` | `String` | no |  | The translated description of the manual operation status. |

**Referenced by:** [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation)

<a id="Manufacturing.ManufacturingOrderMaterial"></a>
### ManufacturingOrderMaterials

Represents a manufacturing order material.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderMaterials`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the manufacturing order material. |
| `ReportNumber` | `Int64` | no |  | The report number of the manufacturing order material. |
| `RowNumber` | `Int32` | no |  | The row number of the manufacturing order material. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the manufacturing order material part. |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The manufacturing order material part. |
| `ToOperationNumber` | `Int32` | no |  | The manufacturing order operation number that the manufacturing order material belongs to. |
| `ReportedQuantity` | `Decimal` | no |  | The reported quantity of the manufacturing order material. |
| `RestQuantity` | `Decimal` | no |  | The remaining quantity of the manufacturing order material. |
| `PlannedQuantity` | `Decimal` | no |  | The planned quantity of the manufacturing order material. |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) | The business key identifier of the manufacturing order that the manufacturing order material belongs to. |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode) | The business key identifier of the manufacturing order node that the manufacturing order material belongs to. |
| `PositionNumber` | `String` | no |  | The position number of the material. |
| `InstructionCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the manufacturing order material's instruction comment. |
| `InstructionComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The manufacturing order material's instruction comment. |
| `QuantityPerUnit` | `Decimal` | no |  | Quantity per unit of the manufacturing order material. |
| `CycleTime` | `TimeSpan?` | yes |  | Cycle time of the manufacturing order material. |
| `EditedStatus` | `Int32` | no |  | Edited status of the manufacturing order material. |
| `ExtraQuantityProcent` | `Decimal` | no |  | Extra quantity procent of the manufacturing order material. |
| `LinkedPurchaseOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The business key identifier of the purchase order row that the manufacturing order material belongs to. |
| `LockedToBatchNo` | `String` | no |  | Locked To batch number of the manufacturing order material. |
| `QuantityPerCycle` | `Decimal?` | yes |  | Quantity per cycle of the manufacturing order material. |
| `RejectedQuantity` | `Decimal` | no |  | Rejected quantity of the manufacturing order material. |
| `ReportedSetupQuantity` | `Decimal` | no |  | Reported setup quantity of the manufacturing order material. |
| `RestSetupQuantity` | `Decimal` | no |  | Rest setup quantity of the manufacturing order material. |
| `SetupQuantity` | `Decimal` | no |  | Setup quantity of the manufacturing order material. |
| `MaterialRowOriginId` | `Int64?` | yes |  | Material row origin id of the manufacturing order material. |

- `EditedStatus` (bitmask) — NotEdited=0, Edited=1, Synchronized=2

**References out:** [Comments](Common.md#Common.Comment), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](Inventory.md#Inventory.Part), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)
**Referenced by:** [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [ManufacturingPickingListMaterials](Manufacturing.md#Manufacturing.ManufacturingPickingListMaterial)

<a id="Manufacturing.ManufacturingOrderNodeDrawingRevision"></a>
### ManufacturingOrderNodeDrawingRevisions

Represents a drawing revision for manufacturing order node.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderNodeDrawingRevisions`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 24.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the revision. |
| `Number` | `String` | no |  | The human readable number of the revision. |
| `ParentId` | `Int64?` | yes | [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing) | The business key identifier of the drawing that the revision belongs to. |
| `RevisionCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the revision comment. |
| `RevisionComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The revision comment. |

**References out:** [Comments](Common.md#Common.Comment), [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing)
**Referenced by:** [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing)

<a id="Manufacturing.ManufacturingOrderNodeDrawing"></a>
### ManufacturingOrderNodeDrawings

Represents a drawing for manufacturing order node.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderNodeDrawings`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 24.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the drawing. |
| `DrawingNumber` | `String` | no |  | The human readable number of the drawing. |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode) | The business key identifier of the manufacturing order node that the drawing belongs to. |
| `Revisions` | `ManufacturingOrderNodeDrawingRevisions[]` | no | [ManufacturingOrderNodeDrawingRevisions](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision) | A collection of revisions that belong the the drawing. |
| `ActiveDrawingRevisionId` | `Int64?` | yes | [ManufacturingOrderNodeDrawingRevisions](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision) | The business key identifier of the active drawing revision. |

**References out:** [ManufacturingOrderNodeDrawingRevisions](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode)
**Referenced by:** [ManufacturingOrderNodeDrawingRevisions](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode)

<a id="Manufacturing.ManufacturingOrderNode"></a>
### ManufacturingOrderNodes

Represents a manufacturing order node.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderNodes`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.30

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the manufacturing order node. |
| `IsMainNode` | `Boolean` | no |  | Specifies if the node is the main node on manufacturing order. Only one of the root nodes on order can be the main node. |
| `IsRootNode` | `Boolean` | no |  | Specifies if the node is a root node on manufacturing order. It can be several root nodes. For example when splitting from max quantity or when coordinated parts exists. Only one of the root nodes on order can be the main node. |
| `Level` | `Int32` | no |  | Level in the node hierarchy |
| `Number` | `Int32` | no |  | Node number, a sequence number in exploding sort order. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the manufacturing order node is to produce. |
| `ReportedQuantity` | `Decimal` | no |  | The reported quantity. |
| `PlannedQuantity` | `Decimal` | no |  | The planned quantity. |
| `RestQuantity` | `Decimal` | no |  | The rest quantity. |
| `StartDate` | `DateTimeOffset` | no |  | The start date of the manufacturing order node. |
| `EndDate` | `DateTimeOffset` | no |  | The finish date of the manufacturing order node. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the node belongs to. |
| `Status` | `Int32` | no |  | The status of the manufacturing order node. |
| `ManufacturingOrderNodeId` | `Int64?` | yes | [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode) | The business key identifier of the manufacturing order node that the manufacturing order node belongs to. If id is null, it's a root node. |
| `Drawings` | `ManufacturingOrderNodeDrawings[]` | no | [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing) | A collection of drawings that belong to the manufacturing order node. |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the revision that the manufacturing order node has. |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) | The revision that the manufacturing order node has. |
| `SerialNumberProductRecords` | `ProductRecords[]` | no | [ProductRecords](Inventory.md#Inventory.ProductRecord) | A collection of product records with serial number traceability that belong to the manufacturing order node. |

- `Status` — NotInitialized=0, Registrered=1, Printed=2, Started=3, Finished=4, PostCalculated=5, Delivered=6, Historical=9

**References out:** [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [Parts](Inventory.md#Inventory.Part), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Revisions](Common.md#Common.Revision), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodeDrawings](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawing), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder)

<a id="Manufacturing.ManufacturingOrderOperationControlDataRow"></a>
### ManufacturingOrderOperationControlDataRows

Represents a measuring plan for a manufacturing order operation.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderOperationControlDataRows`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `ManufacturingOrderOperationId` | `Int64` | no | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) | The business key identifier of the manufacturing order operation that the row relates to. |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](Common.md#Common.MeasuringTemplate) | The business key identifier of the measuring template that the row relates to. |
| `OverridenFormTemplateId` | `Int64` | no | [FormTemplates](Common.md#Common.FormTemplate) | The business key identifier of the form template specified for this row. |
| `OverridenFrequencyText` | `String` | no |  | The frequency text specified for this row. |
| `OverridenIntervalAmount` | `Int32?` | yes |  | The quantity value specified for this row. |
| `OverridenInterval` | `Int32?` | yes |  | The interval value specified for this row. |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier of the work center that the row relates to. |

**References out:** [FormTemplates](Common.md#Common.FormTemplate), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [MeasuringTemplates](Common.md#Common.MeasuringTemplate), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation)

<a id="Manufacturing.ManufacturingOrderOperationReporting"></a>
### ManufacturingOrderOperationReportings

Represents a manufacturing order operation reporting.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderOperationReportings`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 24.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the manufacturing order operation reporting. |
| `OperationId` | `Int64` | no | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) | The business key identifier of the operation that the manufacturing order operation reporting applies. |
| `Quantity` | `Decimal` | no |  | The quantity of the manufacturing order operation reporting. |
| `SetupTime` | `TimeSpan?` | yes |  | The setup time of the manufacturing order operation reporting. |
| `UnitTime` | `TimeSpan?` | yes |  | The unit time of the manufacturing order operation reporting. |
| `WorkCenterId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier of the work center that the manufacturing order operation reporting applies. |
| `EmployeeId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the employee that make the manufacturing order operation reporting. |
| `ReportingEmployeeId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the employee to report as. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse the manufacturing order operation reporting applies to. |
| `ActualReportedDate` | `DateTimeOffset` | no |  | The actual reported date of the manufacturing order operation reporting. |
| `PreviousRestQuantity` | `Decimal` | no |  | The previous rest quantity of the manufacturing order operation reporting. |
| `RestQuantity` | `Decimal` | no |  | The rest quantity of the manufacturing order operation reporting. |
| `OverReceiveQuantity` | `Decimal` | no |  | The over receive quantity of the manufacturing order operation reporting. |
| `SetupCost` | `Decimal?` | yes |  | The setup cost of the manufacturing order operation reporting. |
| `SetupCostCurrencyId` | `Int64?` | yes |  | The business key identifier of the currency that the setup cost of the manufacturing order operation reporting applies to. |
| `SetupCostFactor1` | `Decimal` | no |  | The setup cost factor 1 of the manufacturing order operation reporting. |
| `SetupCostFactor2` | `Decimal` | no |  | The setup cost factor 2 of the manufacturing order operation reporting. |
| `SetupCostFactor3` | `Decimal` | no |  | The setup cost factor 3 of the manufacturing order operation reporting. |
| `SetupCostInForeignCurrency` | `Decimal?` | yes |  | The setup cost in foreign currency of the manufacturing order operation reporting. |
| `SetupCostInForeignCurrencyCurrencyId` | `Int64?` | yes |  | The business key identifier of the foreign currency that the setup cost of the manufacturing order operation reporting applies to. |
| `UnitCost` | `Decimal?` | yes |  | The unit cost of the manufacturing order operation reporting. |
| `UnitCostCurrencyId` | `Int64?` | yes |  | The business key identifier of the currency that the unit cost of the manufacturing order operation reporting applies to. |
| `UnitCostFactor1` | `Decimal` | no |  | The unit cost factor 1 of the manufacturing order operation reporting. |
| `UnitCostFactor2` | `Decimal` | no |  | The unit cost factor 2 of the manufacturing order operation reporting. |
| `UnitCostFactor3` | `Decimal` | no |  | The unit cost factor 3 of the manufacturing order operation reporting. |
| `UnitCostInForeignCurrency` | `Decimal?` | yes |  | The unit cost in foreign currency of the manufacturing order operation reporting. |
| `UnitCostInForeignCurrencyCurrencyId` | `Int64?` | yes |  | The business key identifier of the foreign currency that the unit cost of the manufacturing order operation reporting applies to. |
| `IsSubcontractor` | `Boolean` | no |  | Specifies if the operation is subcontracted. |
| `Type` | `Int32` | no |  | The type that the manufacturing order operation reporting is. |
| `SubcontractorRequestedDeliveryDate` | `DateTimeOffset?` | yes |  | The date requested by the subcontractor for delivering the manufacturing order operation reporting. |
| `SubcontractorActualDeliveryDate` | `DateTimeOffset?` | yes |  | The actual delivery date provided by the subcontractor for the manufacturing order operation reporting. |
| `ReportRestQuantitiesOnSubsequentOperations` | `Boolean` | no |  | Indicates whether to report remaining quantities on subsequent operations for the manufacturing order operation reporting. |
| `IsExportedToManagementAccounting` | `Boolean` | no |  | Indicates whether the data has been exported to management accounting for the manufacturing order operation reporting. |
| `WipLocation` | `String` | no |  | The work in progress location for the manufacturing order operation reporting. |
| `PreviousWipLocation` | `String` | no |  | The previous work in progress location for the manufacturing order operation reporting. |
| `OfWichTime` | `TimeSpan?` | yes |  | Represents the duration related to a specific event or process. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the manufacturing order operation reporting comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | Additional comments or remarks related to the manufacturing order operation reporting. |
| `ReasonCodeTimeConsumptionId` | `Int64?` | yes | [ReasonCodeTimeConsumptions](Manufacturing.md#Manufacturing.ReasonCodeTimeConsumption) | The business key identifier of the reason code associated with time consumption for the manufacturing order operation reporting applies to. |
| `ReasonCodeTimeConsumption` | `ReasonCodeTimeConsumptions` | no | [ReasonCodeTimeConsumptions](Manufacturing.md#Manufacturing.ReasonCodeTimeConsumption) | The reason code associated with time consumption for the manufacturing order operation reporting applies to. |
| `AutomaticMaterialReporting` | `Boolean` | no |  | Indicates whether material reporting is performed automatically for the manufacturing order operation reporting. |
| `PurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) | The business key identifier of the delivery row associated with a purchase order for the manufacturing order operation reporting applies to. |
| `PreviousNodeStatus` | `Int32` | no |  | The previous status of the manufacturing order node for the manufacturing order operation reporting applies to. |
| `OriginalApprovedQuantityFromDeliveryRow` | `Decimal?` | yes |  | The originally approved quantity from the delivery row for the manufacturing order operation reporting applies to. |
| `ReportingId` | `Int64?` | yes |  | The business key identifier of the manufacturing order operation that the reporting applies to. |
| `ReportingTimestamp` | `DateTimeOffset` | no |  | The timestamp where the manufacturing order operation reporting occurred. |
| `RowNumber` | `Int32` | no |  | The row number of the manufacturing order operation reporting. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the manufacturing order operation. |
| `Priority` | `Int32?` | yes |  | The priority of the manufacturing order operation. Can be null. |
| `WorkCenterId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier of the manufacturing order operation's work center. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the manufacturing order operation's part. |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The manufacturing order operation's part. |
| `PlannedQuantity` | `Decimal` | no |  | The planned quantity of the manufacturing order operation. |
| `ReportedQuantity` | `Decimal` | no |  | The reported quantity of the manufacturing order operation. |
| `RestQuantity` | `Decimal` | no |  | The remaining quantity of the manufacturing order operation. |
| `ReportedSetupTime` | `TimeSpan` | no |  | The reported setup time of the manufacturing order operation. |
| `ReportedUnitTime` | `TimeSpan` | no |  | The reported unit time of the manufacturing order operation. |
| `RejectedQuantity` | `Decimal` | no |  | The rejected quantity of the manufacturing order operation. |
| `WipLocation` | `String` | no |  | The work-in-progress location of the manufacturing order operation. |
| `ReportNumber` | `Int64` | no |  | The report number of the manufacturing order operation. |
| `InstructionCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the manufacturing order operation's instruction comment. |
| `InstructionComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The manufacturing order operation's instruction comment. |
| `ManufacturingOrderId` | `Int64` | no | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) | The business key identifier of the manufacturing order that the manufacturing order operation belongs to. |
| `ManufacturingOrderNodeId` | `Int64` | no | [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode) | The business key identifier of the manufacturing order node that the manufacturing order operation belongs to. |
| `OperationNumber` | `Int32` | no |  | The operation number of the manufacturing order operation. |
| `PlannedSetupTime` | `TimeSpan` | no |  | The planned setup time of the manufacturing order operation. |
| `PlannedUnitTime` | `TimeSpan` | no |  | The planned unit time of the manufacturing order operation. |
| `PlannedStartDate` | `DateTimeOffset` | no |  | The planned start date of the manufacturing order operation. |
| `PlannedFinishDate` | `DateTimeOffset` | no |  | The planned finish date of the manufacturing order operation. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  | The actual (reported) start date of the manufacturing order operation. |
| `ActualFinishDate` | `DateTimeOffset?` | yes |  | The actual (reported) finish date of the manufacturing order operation. |
| `OperationRowId` | `Int64?` | yes | [OperationRows](Manufacturing.md#Manufacturing.OperationRow) | The business key identifier of the operation row that the manufacturing order operation is based on. Can be null if the manufacturing order operation is added manually. |
| `OperationRow` | `OperationRows` | no | [OperationRows](Manufacturing.md#Manufacturing.OperationRow) | The operation row that the manufacturing order operation is based on. |
| `Status` | `Int32` | no |  | The status of the manufacturing order operation's status. |
| `WorkshopOperationStatus` | `Int32` | no |  | The workshop status of the manufacturing order operation's status. |
| `BundleId` | `Int64?` | yes |  | An generated id that is common for a collection of operations. |
| `Description` | `String` | no |  | The translated description of the manufacturing order operation. |
| `ControlDataRows` | `ManufacturingOrderOperationControlDataRows[]` | no | [ManufacturingOrderOperationControlDataRows](Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow) | The control data rows. |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityManufacturingOrderOperations](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrderOperation) | The business key identifier of order quantity. |
| `OrderQuantity` | `OrderQuantityManufacturingOrderOperations` | no | [OrderQuantityManufacturingOrderOperations](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrderOperation) | Order quantity that holds the partial quantities. |
| `ClearedStatus` | `Boolean` | no |  | Specifies if the status is cleared. |
| `OnPriorityPlan` | `Boolean` | no |  | Indicates if the operation is shown in priority plan. |
| `ManualOperationStatusId` | `Int64?` | yes | [ManualOperationStatuses](Manufacturing.md#Manufacturing.ManualOperationStatus) | The business key identifier of manual operation status. |
| `ManualOperationStatus` | `ManualOperationStatuses` | no | [ManualOperationStatuses](Manufacturing.md#Manufacturing.ManualOperationStatus) | The manual operation status. |
| `Materials` | `ManufacturingOrderMaterials[]` | no | [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) | The manufacturing order materials of the operation. |
| `FixedLeadTime` | `TimeSpan?` | yes |  | The fixed lead time of the manufacturing order operation. |
| `UnitStaffingFactor` | `Decimal?` | yes |  | The unit staffing factor of the manufacturing order operation. |
| `SetupStaffingFactor` | `Decimal?` | yes |  | The setup staffing factor of the manufacturing order operation. |
| `IsPlannedTimeCalculated` | `Boolean` | no |  | Indicates that the planned time of the operation was calculated at order creation (from a part-configurator formula or aggregated from fictitious sub-parts) and must not be overwritten when the work center is changed. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the manufacturing order. |
| `OrderNumber` | `String` | no |  | The order number of the manufacturing order. |
| `Status` | `Int32` | no |  | The status of the manufacturing order. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the manufacturing order belongs to. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the comment that belongs to the manufacturing order. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment that belongs to the manufacturing order. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the manufacturing order is to produce. |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The part that the manufacturing order is to produce. |
| `ReportedQuantity` | `Decimal` | no |  | The reported quantity of the main manufacturing order node. |
| `PlannedQuantity` | `Decimal` | no |  | The planned quantity of the main manufacturing order node. |
| `RestQuantity` | `Decimal` | no |  | The rest quantity of the main manufacturing order node. |
| `StartDate` | `DateTimeOffset` | no |  | The start date of the manufacturing order. |
| `FinishDate` | `DateTimeOffset` | no |  | The finish date of the manufacturing order. |
| `Priority` | `Int32` | no |  | The priority of the manufacturing order. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order that produced the manufacturing order. |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The customer order that produced the manufacturing order. |
| `Operations` | `ManufacturingOrderOperations[]` | no | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) | The manufacturing order operations that belong to the manufacturing order. |
| `Materials` | `ManufacturingOrderMaterials[]` | no | [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) | The manufacturing order materials that belong to the manufacturing order. |
| `Nodes` | `ManufacturingOrderNodes[]` | no | [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode) | The manufacturing order nodes that belong to the manufacturing order. It is flattened, not a structure. |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of the project that belongs to the manufacturing order. |
| `Project` | `Projects` | no | [Projects](Common.md#Common.Project) | The project that belongs to the manufacturing order. Can be null. |
| `CategoryString` | `String` | no |  | The category string of the manufacturing order. |
| `VariantCode` | `String` | no |  | The variant code on the manufacturing order. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer on the manufacturing order. |
| `InitialFinishDate` | `DateTimeOffset` | no |  | The initial finish date for the manufacturing order. |
| `PartConfigurationId` | `Int64?` | yes | [PartConfigurations](Common.md#Common.PartConfiguration) | The business key identifier of the manufacturing order's part configuration. |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityManufacturingOrders](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder) | The business key identifier of order quantity. |
| `OrderQuantity` | `OrderQuantityManufacturingOrders` | no | [OrderQuantityManufacturingOrders](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder) | Order quantity that holds the partial quantities. |
| `OrderTypeId` | `Int64?` | yes | [ManufacturingOrderTypes](Manufacturing.md#Manufacturing.ManufacturingOrderType) | The business key identifier of order type. |
| `OrderType` | `ManufacturingOrderTypes` | no | [ManufacturingOrderTypes](Manufacturing.md#Manufacturing.ManufacturingOrderType) | Order type of the Manufacturing Order. |

- `Status` — NotInitialized=0, Registrered=1, Printed=2, Started=3, Finished=4, PostCalculated=5, Delivered=6, Historical=9

**References out:** [Comments](Common.md#Common.Comment), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrderTypes](Manufacturing.md#Manufacturing.ManufacturingOrderType), [OrderQuantityManufacturingOrders](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder), [PartConfigurations](Common.md#Common.PartConfiguration), [Parts](Inventory.md#Inventory.Part), [Projects](Common.md#Common.Project), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [CaseEntry](Inventory.md#Inventory.CaseEntry), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [Locations](Inventory.md#Inventory.Location), [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting), [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ProductRecords](Inventory.md#Inventory.ProductRecord)

<a id="Manufacturing.ManufacturingOrderType"></a>
### ManufacturingOrderTypes

Represents a manufacturing order type.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingOrderTypes`
- **Required permission:** Show order types
- **Introduced in:** 2.35

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the type. |
| `Number` | `Int64` | no |  | The human readable identifier of the type. |
| `Prefix` | `String` | no |  | The prefix applied to manufacturing order numbers for this type. |
| `Description` | `String` | no |  | The translated description of the type. |
| `BaseType` | `Int32` | no |  | The base type of manufacturing orders created using this type. |

- `BaseType` — InventoryControlled=0, CustomerOrderControlled=1, MaintenanceControlled=2

**Referenced by:** [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder)

<a id="Manufacturing.ManufacturingPickingListMaterial"></a>
### ManufacturingPickingListMaterials

Represents a manufacturing picking list material.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingPickingListMaterials`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.48

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the manufacturing picking list material. |
| `MaterialId` | `Int64` | no | [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) | The business key identifier of the manufacturing order material. |
| `Material` | `ManufacturingOrderMaterials` | no | [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial) | The manufacturing order material in the manufacturing picking list. |
| `QuantityChangeId` | `Int64` | no | [QuantityChanges](Inventory.md#Inventory.QuantityChange) | The business key identifier of the manufacturing picking list materials quantity change. |
| `QuantityChange` | `QuantityChanges` | no | [QuantityChanges](Inventory.md#Inventory.QuantityChange) | The suggested quantity for withdrawal when creating the picking list. |

**References out:** [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [QuantityChanges](Inventory.md#Inventory.QuantityChange)
**Referenced by:** [ManufacturingPickingLists](Manufacturing.md#Manufacturing.ManufacturingPickingList)

<a id="Manufacturing.ManufacturingPickingList"></a>
### ManufacturingPickingLists

Represents a manufacturing picking list.

- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingPickingLists`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 2.48

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the picking list. |
| `Number` | `String` | no |  | The human readable identifier of the picking list. |
| `CreatedByApplicationUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that created the picking list. |
| `CreatedByPersonId` | `Int64` | no | [Persons](Common.md#Common.Person) | The business key identifier of the person that created the picking list. |
| `CreatedTimestamp` | `DateTimeOffset` | no |  | The date the picking list was created. |
| `PrintedByApplicationUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that printed the picking list. |
| `PrintedByPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the person that printed the picking list. |
| `PrintedTimestamp` | `DateTimeOffset?` | yes |  | The date the picking list was printed. |
| `Status` | `Int32` | no |  | The status of the picking list. |
| `Grouping` | `Int32` | no |  | The grouping for the picking list. |
| `Sorting` | `Int32` | no |  | The sorting for the picking list. |
| `WarehouseId` | `Int64?` | yes | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse for the picking list. |
| `Type` | `Int32` | no |  | The type of picking list. |
| `Materials` | `ManufacturingPickingListMaterials[]` | no | [ManufacturingPickingListMaterials](Manufacturing.md#Manufacturing.ManufacturingPickingListMaterial) | The picking lists materials |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the reference number. |
| `MaterialRowId` | `Int64` | no | [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow) | The business key identifier of the material row that the reference number belongs to. |
| `Prefix` | `String` | no |  | The prefix part of the reference number. |
| `From` | `String` | no |  | The starting value of the reference number range. |
| `To` | `String` | no |  | The ending value of the reference number range. Only valid when is numeric; otherwise this value is not persisted and the quantity is one. |
| `Suffix` | `String` | no |  | The suffix part of the reference number. |
| `Remark` | `String` | no |  | A free-text remark associated with the reference number. |
| `Quantity` | `Decimal` | no |  | The quantity represented by the reference number range. This value is calculated from and and cannot be set directly. |
| `RowIndex` | `Int32?` | yes |  | The display order of the reference number within the material row. |

**References out:** [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow)
**Referenced by:** [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow)

<a id="Manufacturing.MaterialRow"></a>
### MaterialRows

Represents a material row.

- **Endpoint:** `GET /api/v1/Manufacturing/MaterialRows`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the material row. |
| `PartId` | `Int64` | no |  | The business key identifier of material row part. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the material row's comment. References Comments /// |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the material row. |
| `Position` | `String` | no |  | The position of the material row. |
| `ToOperation` | `Int32` | no |  | The number of the operation row that the material row belongs to. |
| `Quantity` | `Decimal` | no |  | The quantity of the material row. |
| `SetupQuantity` | `Decimal` | no |  | The setup quantity of the material row. |
| `ExtraPercent` | `Decimal` | no |  | The extra percent of the material row. |
| `IsForCalculationOnly` | `Boolean` | no |  | Specifies if the material row is only used for calculation. |
| `MainPartId` | `Int64` | no |  | The business key identifier of the part that the material row belongs to. |
| `RowIndex` | `Int32` | no |  | The row index of the material row. |
| `PreparationTermType` | `Int32?` | yes |  | PreparationTermType of the Material Row. |
| `PreparationTermFromValue` | `String` | no |  | PreparationTermFromValue of the Material Row. |
| `PreparationTermToValue` | `String` | no |  | PreparationTermToValue of the Material Row. |
| `ReferenceNumbers` | `MaterialRowReferenceNumbers[]` | no | [MaterialRowReferenceNumbers](Manufacturing.md#Manufacturing.ReferenceNumber) | The reference numbers configured for this material row. |

**References out:** [Comments](Common.md#Common.Comment), [MaterialRowReferenceNumbers](Manufacturing.md#Manufacturing.ReferenceNumber)
**Referenced by:** [MaterialRowReferenceNumbers](Manufacturing.md#Manufacturing.ReferenceNumber), [Preparations](Manufacturing.md#Manufacturing.Preparation)

<a id="Manufacturing.OperationRowControlDataRow"></a>
### OperationRowControlDataRows

Represents a measuring plan for an operation row.

- **Endpoint:** `GET /api/v1/Manufacturing/OperationRowControlDataRows`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `OperationRowId` | `Int64` | no | [OperationRows](Manufacturing.md#Manufacturing.OperationRow) | The business key identifier of the operation row that the row relates to. |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](Common.md#Common.MeasuringTemplate) | The business key identifier of the measuring template that the row relates to. |
| `OverriddenFormTemplateId` | `Int64?` | yes | [FormTemplates](Common.md#Common.FormTemplate) | The business key identifier of the form template specified for this row. |
| `OverriddenFrequencyText` | `String` | no |  | The frequency text specified for this row. |
| `OverriddenIntervalAmount` | `Int32?` | yes |  | The quantity value specified for this row. |
| `OverriddenInterval` | `Int32?` | yes |  | The interval value specified for this row. |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier of the work center that the row relates to. |

**References out:** [FormTemplates](Common.md#Common.FormTemplate), [MeasuringTemplates](Common.md#Common.MeasuringTemplate), [OperationRows](Manufacturing.md#Manufacturing.OperationRow), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [OperationRows](Manufacturing.md#Manufacturing.OperationRow)

<a id="Manufacturing.OperationRow"></a>
### OperationRows

Represents an operation row.

- **Endpoint:** `GET /api/v1/Manufacturing/OperationRows`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the material row. |
| `OperationNumber` | `Int32` | no |  | The operation number of the operation row. |
| `SubcontractPartId` | `Int64?` | yes |  | The business key identifier of the operation row's subcontract part. |
| `SupplierId` | `Int64?` | yes |  | The business key identifier of the operation row's supplier. |
| `WorkCenterId` | `Int64` | no |  | The business key identifier of the operation's row work center. |
| `IsSubcontractor` | `Boolean` | no |  | Specifies if the operation is subcontracted. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the operation row's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the operation row. |
| `Description` | `String` | no |  | The translated description of the operation row. |
| `TimeCode` | `Int32` | no |  | The time code specified for the operation row. |
| `TimeUnit` | `Int32` | no |  | The time unit specified for the operation row. |
| `SetupTime` | `TimeSpan` | no |  | The setup time of the operation. |
| `UnitTime` | `TimeSpan` | no |  | The unit time of the operation. |
| `ExtraQuantityPercent` | `Decimal` | no |  | The extra quantity percentage of the operation row. |
| `NumberOfFlows` | `Decimal?` | yes |  | The number of flows specified for the operation row. |
| `OverlapPercent` | `Decimal` | no |  | The overlap percentage of the operation row. |
| `UnitStaffingFactor` | `Decimal?` | yes |  | The unit staffing factor of the operation row. |
| `SetupStaffingFactor` | `Decimal?` | yes |  | The setup staffing factor of the operation row. |
| `SetupQuantity` | `Decimal` | no |  | The setup quantity of the operation row. |
| `IsForCalculationOnly` | `Boolean` | no |  | Specifies if the operation row is to be used for calculations only. |
| `QueueTime` | `TimeSpan?` | yes |  | The queue time of the operation. |
| `UseQueueTimeWholeDayRoundOf` | `Boolean?` | yes |  | Specifies if queue time should be rounded to full day. |
| `UnitCostFactorId` | `Int64?` | yes |  | The business key identifier of the unit cost factor of the operation row. |
| `SetupCostFactorId` | `Int64?` | yes |  | The business key identifier of the setup cost factor of the operation row. |
| `FixedLeadTime` | `TimeSpan?` | yes |  | The fixed lead time of the operation row. |
| `SetupCost` | `Decimal?` | yes |  | The setup cost of the operation row. This value is only available if the operation is a subcontract. |
| `SetupCostCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the setup cost currency. |
| `UnitCost` | `Decimal?` | yes |  | The unit cost of the operation row. This value is only available if the operation is a subcontract. |
| `UnitCostCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the unit cost currency. |
| `TransportCost` | `Decimal?` | yes |  | The transport cost of the operation represented in the company currency. This value is only available if the operation is a subcontract. |
| `SupplierPartNumber` | `String` | no |  | The supplier part number of the operation subcontractor part. This value is only available if the operation is a subcontract. |
| `DeliverToEndCustomer` | `Boolean` | no |  | Whether the subcontractor will deliver straight to the end customer or not. This value is only available if the operation is a subcontract. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) | The extra fields of the operation row. |
| `ControlDataRows` | `OperationRowControlDataRows[]` | no | [OperationRowControlDataRows](Manufacturing.md#Manufacturing.OperationRowControlDataRow) | The control data rows. |
| `AlternativeOperationRows` | `AlternativeOperationRows[]` | no | [AlternativeOperationRows](Manufacturing.md#Manufacturing.AlternativeOperationRow) | The alternative operation rows (alternative work centers) of the operation row. |
| `PreparationTermType` | `Int32?` | yes |  | PreparationTermType of the Operation Row. |
| `PreparationTermFromValue` | `String` | no |  | PreparationTermFromValue of the Operation Row. |
| `PreparationTermToValue` | `String` | no |  | PreparationTermToValue of the Operation Row. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](Common.md#Common.PartialQuantity) | The partial quantities for the order quantity. |

**References out:** [PartialQuantities](Common.md#Common.PartialQuantity)
**Referenced by:** [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation)

<a id="Manufacturing.OrderQuantityManufacturingOrder"></a>
### OrderQuantityManufacturingOrders

Represents a order quantity template on part that holds many partial quantities.

- **Endpoint:** `GET /api/v1/Manufacturing/OrderQuantityManufacturingOrders`
- **Required permission:** Show manufacturing orders
- **Introduced in:** 22.6

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](Common.md#Common.PartialQuantity) | The partial quantities for the order quantity. |

**References out:** [PartialQuantities](Common.md#Common.PartialQuantity)
**Referenced by:** [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder)

<a id="Manufacturing.Preparation"></a>
### Preparations

Represents a part preparation

- **Endpoint:** `GET /api/v1/Manufacturing/Preparations`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part preparation. |
| `PartNumber` | `String` | no |  | The part number of the part that the part preparation represents. |
| `Description` | `String` | no |  | The translated description of the part preparation. |
| `UseVariantManagement` | `Boolean` | no |  | Specifies if variant management is applied for the preparation. |
| `VariantXAxisId` | `Int64?` | yes | [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate) | The business key identifier of the extra field template used for the X axis of the variant management system. |
| `VariantXAxis` | `ExtraFieldTemplates` | no | [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate) | The extra field template that is applied for the X axis of the variant management system. |
| `VariantYAxisId` | `Int64?` | yes | [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate) | The business key identifier of the extra field template used for the Y axis of the variant management system. References ExtraFieldTemplates . |
| `VariantYAxis` | `ExtraFieldTemplates` | no | [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate) | The extra field template that is applied for the Y axis of the variant management system. |
| `Materials` | `MaterialRows[]` | no | [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow) | The material rows of the preparation. |
| `Operations` | `OperationRows[]` | no | [OperationRows](Manufacturing.md#Manufacturing.OperationRow) | The operation rows of the preparation. |

**References out:** [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate), [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow), [OperationRows](Manufacturing.md#Manufacturing.OperationRow)
**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Manufacturing.ProductionCalendarException"></a>
### ProductionCalendarExceptions

Represents a table that contains exceptions from the production calendar. Only used when using daily planning.

- **Endpoint:** `GET /api/v1/Manufacturing/ProductionCalendarExceptions`
- **Required permission:** Show work center
- **Introduced in:** 24.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the production calendar exception. |
| `WorkCenterId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier of the work center that is linked to the production calendar exception. |
| `NumberOfPlanningUnits` | `Decimal?` | yes |  | Number of persons or number of machines depending on the work center type. |
| `ExceptionDate` | `DateTime` | no |  | Day of the production calendar exception. |
| `BasicTime` | `TimeSpan?` | yes |  | Basic time used on this production calendar exception date. |
| `ScheduleId` | `Int64?` | yes | [Schedules](TimeRecording.md#TimeRecording.Schedule) | The business key identifier of the schedule used on this production calendar exception date. |

**References out:** [Schedules](TimeRecording.md#TimeRecording.Schedule), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)

<a id="Manufacturing.ReasonCodeTimeConsumption"></a>
### ReasonCodeTimeConsumptions

Represents a reason code time consumption.

- **Endpoint:** `GET /api/v1/Manufacturing/ReasonCodeTimeConsumptions`
- **Required permission:** Show cause codes
- **Introduced in:** 24.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the reason code time consumption. |
| `Code` | `String` | no |  | The alphanumeric code of the reason code time consumption. |
| `Description` | `String` | no |  | The translated description of the reason code time consumption. |
| `CommentMandatory` | `Boolean` | no |  | Specifies if a comment is mandatory for the reason code time consumption. |
| `Active` | `Boolean` | no |  | Specifies if the reason code time consumption is active in the system. |
| `TimeConsumptionType` | `Int32` | no |  | The type of the reason code time consumption. |

- `TimeConsumptionType` — TimeLoss=0, TimeGain=1

**Referenced by:** [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting)

<a id="Manufacturing.WorkCenterCostFactorGroup"></a>
### WorkCenterCostFactorGroups

Represents a cost factor group belonging to a work center. Note that all cost factors are represented in company currency per hour.

- **Endpoint:** `GET /api/v1/Manufacturing/WorkCenterCostFactorGroups`
- **Required permission:** Show work center
- **Introduced in:** 2.46

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the work center cost factor group. |
| `Description` | `String` | no |  | The translated description of the work center cost factor group. |
| `Type` | `Int32` | no |  | The types that apply to the work center cost factor group. |
| `CostFactor1` | `Decimal?` | yes |  | The first cost factor of the group. |
| `CostFactor2` | `Decimal?` | yes |  | The second cost factor of the group. |
| `CostFactor3` | `Decimal?` | yes |  | The third cost factor of the group. |
| `FutureCostFactor1` | `Decimal?` | yes |  | The future first cost factor of the group. |
| `FutureCostFactor2` | `Decimal?` | yes |  | The future second cost factor of the group. |
| `FutureCostFactor3` | `Decimal?` | yes |  | The future third cost factor of the group. |
| `IsDefaultSetupCost` | `Boolean` | no |  | Specifies if the cost factor group is used as the default group for setup costs for its parent work center. |
| `IsDefaultUnitCost` | `Boolean` | no |  | Specifies if the cost factor group is used as the default group for unit costs for its parent work center. |
| `ParentId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier of the work center that the cost factor group belongs to. |
| `RowIndex` | `Int32` | no |  | The row index of the work center cost factor group in relation to the other groups that belong to the parent work center. |

- `Type` (bitmask) — None=0, SetupCost=1, UnitCost=2

**References out:** [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)

<a id="Manufacturing.WorkCenterManufacturingPrintSettings"></a>
### WorkCenterManufacturingPrintSettings

Represents manufacturing print settings for a work center.

- **Endpoint:** `GET /api/v1/Common/WorkCenterManufacturingPrintSettings`
- **Required permission:** Show work center
- **Introduced in:** 2.28

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the workcenter manufacturing print settings. |
| `Copies` | `Int32` | no |  | Number of copies of the document. |
| `PrintExternalDocuments` | `Boolean` | no |  | Specifies if external documents should be included in the printout. |
| `FormReportId` | `Int64` | no |  | The business key identifier of the form report the settings applies to. |

**Referenced by:** [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)

<a id="Manufacturing.WorkCenter"></a>
### WorkCenters

Represents a manufacturing work center.

- **Endpoint:** `GET /api/v1/Manufacturing/WorkCenters`
- **Required permission:** Show work center
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the work center. |
| `Number` | `String` | no |  | The human readable identifier of the work center. |
| `Description` | `String` | no |  | The translated description of the work center. |
| `OperationDescription` | `String` | no |  | The translated operation description of the work center. |
| `Type` | `Int32` | no |  | The work center type. |
| `DepartmentId` | `Int64` | no |  | The business key identifier of the department that the work center belongs to. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the work center belongs to. References Warehouses . |
| `Warehouse` | `Warehouses` | no | [Warehouses](Common.md#Common.Warehouse) | The warehouse that the work center belongs to. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the work center comment. References Comments . |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The work center comment. |
| `ManufacturingPrintSettings` | `WorkCenterManufacturingPrintSettings[]` | no | [WorkCenterManufacturingPrintSettings](Manufacturing.md#Manufacturing.WorkCenterManufacturingPrintSettings) | The print settings for manufacturing order documents. |
| `CostFactorGroups` | `WorkCenterCostFactorGroups[]` | no | [WorkCenterCostFactorGroups](Manufacturing.md#Manufacturing.WorkCenterCostFactorGroup) | The cost factor groups that belong to the work center. |
| `TimePrecision` | `Int32` | no |  | Time precision for the work center |
| `BasicTime` | `TimeSpan` | no |  | Basic time (capacity per day) |
| `NumberOfPlanningUnits` | `Decimal` | no |  | Number of planning units, can be machines or persons depending on the work center type. |
| `NumberOfFlows` | `Decimal` | no |  | Number of machines per order or number of persons per order depending on the work center type. |
| `AvailabilityFactor` | `Decimal` | no |  | Availability factor in percent for the work center. |
| `SimulationFactor` | `Decimal` | no |  | Simulation factor in percent for the work center. |
| `UnitStaffFactor` | `Decimal` | no |  | Indicates how large (in percent) a share of the operating unit time that is staffed for the work center. |
| `SetupStaffFactor` | `Decimal` | no |  | Indicates how large (in percent) a share of the operating setup time that is staffed for the work center. |
| `Employees` | `PersonWorkCenters[]` | no | [PersonWorkCenters](TimeRecording.md#TimeRecording.PersonWorkCenter) | Specifies the persons that should be allowed to select work from this work center. |
| `ProductionCalendarExceptions` | `ProductionCalendarExceptions[]` | no | [ProductionCalendarExceptions](Manufacturing.md#Manufacturing.ProductionCalendarException) | Specifies the production calendar exceptions for this work center. |

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
