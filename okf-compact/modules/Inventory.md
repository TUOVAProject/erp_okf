# Inventory

Monitor API module `Inventory`: 50 queryable entities, 0 commands, 0 payload types.

## Queryable entities

<a id="Inventory.AbcCode"></a>
### AbcCodes

Represents an ABC code.

- **Endpoint:** `GET /api/v1/Inventory/AbcCodes`
- **Required permission:** Show ABC codes
- **Introduced in:** 2.31

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [PartPlanningInformation](/modules/Inventory.md#Inventory.PartPlanningInformation), [PartTemplates](/modules/Inventory.md#Inventory.PartTemplate)

<a id="Inventory.AdditionalIdsRecord"></a>
### AdditionalIDsRecords

Represents an addtional ids record.

- **Endpoint:** `GET /api/v1/Inventory/AdditionalIDsRecords`
- **Required permission:** Show serial number
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ProductRecordId` | `Int64` | no | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `Code` | `String` | no |  |
| `Code2` | `String` | no |  |
| `Code3` | `String` | no |  |
| `Number` | `Int32?` | yes |  |
| `Number2` | `Decimal?` | yes |  |
| `Date` | `DateTimeOffset?` | yes |  |
| `Weight` | `Decimal?` | yes |  |

**References out:** [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord)

<a id="Inventory.AlloyQuantity"></a>
### AlloyQuantities

Represents Alloy Quantities of an alloy.

- **Endpoint:** `GET /api/v1/Inventory/AlloyQuantities`
- **Required permission:** Create new alloy codes
- **Introduced in:** 25.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AlloyId` | `Int64` | no | [Alloys](/modules/Inventory.md#Inventory.Alloy) |
| `Quantity` | `Decimal` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |

**References out:** [Alloys](/modules/Inventory.md#Inventory.Alloy), [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.Alloy"></a>
### Alloys

Represents an alloy.

- **Endpoint:** `GET /api/v1/Inventory/Alloys`
- **Required permission:** Show alloy codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `Price` | `Decimal` | no |  |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `UnitId` | `Int64` | no | [Units](/modules/Common.md#Common.Unit) |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |

**References out:** [Currencies](/modules/Common.md#Common.Currency), [Parts](/modules/Inventory.md#Inventory.Part), [Units](/modules/Common.md#Common.Unit)
**Referenced by:** [AlloyQuantities](/modules/Inventory.md#Inventory.AlloyQuantity), [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.CaseEntry"></a>
### CaseEntry

Represents a case entry.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntry`
- **Required permission:** Show case
- **Introduced in:** 2.22

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `ProjectId` | `Int64?` | yes | [Projects](/modules/Common.md#Common.Project) |
| `Project` | `Projects` | no | [Projects](/modules/Common.md#Common.Project) |
| `ContactCaseNumber` | `String` | no |  |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder) |
| `PurchaseOrder` | `PurchaseOrders` | no | [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder) |
| `ArrivalDate` | `DateTimeOffset?` | yes |  |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |
| `DeliveredQuantity` | `Decimal?` | yes |  |
| `ArrivedQuantity` | `Decimal?` | yes |  |
| `ReasonSupplierId` | `Int64?` | yes | [Suppliers](/modules/Purchase.md#Purchase.Supplier) |
| `ReasonWorkCenterId` | `Int64?` | yes | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |
| `ReasonDepartmentId` | `Int64?` | yes | [Departments](/modules/Common.md#Common.Department) |
| `ReasonRejectionCodeId` | `Int64?` | yes | [RejectionCodeItems](/modules/Common.md#Common.RejectionCodeItem) |
| `ReasonPartId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `InternalCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `InternalComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `ReasonCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `ReasonComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `ActualRejectionCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `ActualRejectionComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `Status` | `Int32` | no |  |
| `CaseTypeId` | `Int64` | no | [CaseManagementType](/modules/Inventory.md#Inventory.CaseManagementType) |
| `CaseType` | `CaseManagementType` | no | [CaseManagementType](/modules/Inventory.md#Inventory.CaseManagementType) |
| `CaseDate` | `DateTimeOffset` | no |  |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Warehouse` | `Warehouses` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `CustomerId` | `Int64?` | yes | [Customers](/modules/Sales.md#Sales.Customer) |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `ProductRecord` | `ProductRecords` | no | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `PartRevisionId` | `Int64?` | yes | [Revisions](/modules/Common.md#Common.Revision) |
| `PartRevision` | `Revisions` | no | [Revisions](/modules/Common.md#Common.Revision) |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `ManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ManufacturingOrder` | `ManufacturingOrders` | no | [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `SupplierId` | `Int64` | no | [Suppliers](/modules/Purchase.md#Purchase.Supplier) |
| `ActualRejectionCodeId` | `Int64?` | yes | [RejectionCodeItems](/modules/Common.md#Common.RejectionCodeItem) |
| `ActualRejectionCode` | `RejectionCodeItems` | no | [RejectionCodeItems](/modules/Common.md#Common.RejectionCodeItem) |
| `RejectionCodeItemId` | `Int64` | no | [RejectionCodeItems](/modules/Common.md#Common.RejectionCodeItem) |
| `RejectionCodeItem` | `RejectionCodeItems` | no | [RejectionCodeItems](/modules/Common.md#Common.RejectionCodeItem) |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](/modules/Common.md#Common.ExtraField) |
| `Costs` | `CaseEntryAdditionalCost[]` | no | [CaseEntryAdditionalCost](/modules/Inventory.md#Inventory.CaseEntryAdditionalCost) |
| `OurReferenceId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `OurReferenceName` | `String` | no |  |
| `Phases` | `CaseEntryPhases[]` | no | [CaseEntryPhases](/modules/Inventory.md#Inventory.CaseEntryPhase) |
| `RejectionDescription` | `String` | no |  |
| `Notes` | `BusinessContactNoteHistories[]` | no | [BusinessContactNoteHistories](/modules/Common.md#Common.BusinessContactNoteHistory) |
| `ContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference) |
| `ContactName` | `String` | no |  |
| `AccountReciveableId` | `Int64?` | yes | [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable) |
| `AccountsReceivable` | `AccountsReceivables` | no | [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable) |
| `CategoryString` | `String` | no |  |
| `ExternalCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `ExternalComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `RejectedQuantity` | `Decimal` | no |  |
| `CasePartLinks` | `CaseEntryPartLinks[]` | no | [CaseEntryPartLinks](/modules/Inventory.md#Inventory.CasePartLink) |

- `Status` — Registered=1, Printed=2, Started=3, Finished=4, History=9, Rejected=99

**References out:** [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [BusinessContactNoteHistories](/modules/Common.md#Common.BusinessContactNoteHistory), [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference), [CaseEntryAdditionalCost](/modules/Inventory.md#Inventory.CaseEntryAdditionalCost), [CaseEntryPartLinks](/modules/Inventory.md#Inventory.CasePartLink), [CaseEntryPhases](/modules/Inventory.md#Inventory.CaseEntryPhase), [CaseManagementType](/modules/Inventory.md#Inventory.CaseManagementType), [Comments](/modules/Common.md#Common.Comment), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [Customers](/modules/Sales.md#Sales.Customer), [Departments](/modules/Common.md#Common.Department), [ExtraFields](/modules/Common.md#Common.ExtraField), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](/modules/Inventory.md#Inventory.Part), [Persons](/modules/Common.md#Common.Person), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [Projects](/modules/Common.md#Common.Project), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [RejectionCodeItems](/modules/Common.md#Common.RejectionCodeItem), [Revisions](/modules/Common.md#Common.Revision), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [Warehouses](/modules/Common.md#Common.Warehouse), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [CaseEntryActivities](/modules/Inventory.md#Inventory.CaseEntryActivity), [CaseEntryAdditionalCost](/modules/Inventory.md#Inventory.CaseEntryAdditionalCost), [CaseEntryLinks](/modules/Inventory.md#Inventory.CaseEntryLink), [CaseEntryPartLinks](/modules/Inventory.md#Inventory.CasePartLink), [CaseEntryPhases](/modules/Inventory.md#Inventory.CaseEntryPhase), [Customers](/modules/Sales.md#Sales.Customer), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Inventory.CaseEntryActivity"></a>
### CaseEntryActivities

Represents a case entry activity.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntryActivities`
- **Required permission:** Show case
- **Introduced in:** 2.45

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CaseEntryId` | `Int64` | no | [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry) |
| `PlannedTime` | `TimeSpan` | no |  |
| `ReportedTime` | `TimeSpan?` | yes |  |
| `ShowOnDocuments` | `Boolean` | no |  |
| `ReportingType` | `Int32` | no |  |
| `Mandatory` | `Boolean` | no |  |
| `CostPerHour` | `Decimal?` | yes |  |
| `CostPerHourCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `Chargeable` | `Boolean` | no |  |
| `ActivityTypeId` | `Int64` | no | [CaseManagementActivities](/modules/Inventory.md#Inventory.CaseManagementActivity) |
| `CalendarAppointmentId` | `String` | no |  |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `Description` | `String` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `Status` | `Int32` | no |  |
| `ReminderId` | `Int64?` | yes |  |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |
| `CompletionDate` | `DateTimeOffset?` | yes |  |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |

- `ReportingType` — Manual=0, Automatic=1
- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CaseManagementActivities](/modules/Inventory.md#Inventory.CaseManagementActivity), [Comments](/modules/Common.md#Common.Comment), [Currencies](/modules/Common.md#Common.Currency)
**Referenced by:** [CaseEntryPhases](/modules/Inventory.md#Inventory.CaseEntryPhase)

<a id="Inventory.CaseEntryAdditionalCost"></a>
### CaseEntryAdditionalCost

Represents a case entry additional cost.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntryAdditionalCost`
- **Required permission:** Show basic data for case
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CaseEntryId` | `Int64` | no | [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry) |
| `CaseManagementCostId` | `Int64` | no | [CaseManagementCost](/modules/Inventory.md#Inventory.CaseManagementCost) |
| `CaseManagementCost` | `CaseManagementCost` | no | [CaseManagementCost](/modules/Inventory.md#Inventory.CaseManagementCost) |
| `Cost` | `Decimal` | no |  |
| `CostCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `CostType` | `Int32` | no |  |
| `Chargeable` | `Boolean` | no |  |
| `CostPerEach` | `Decimal?` | yes |  |
| `Quantity` | `Decimal?` | yes |  |
| `PartId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](/modules/Inventory.md#Inventory.Part) |

- `CostType` — Planned=0, Actual=1

**References out:** [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CaseManagementCost](/modules/Inventory.md#Inventory.CaseManagementCost), [Currencies](/modules/Common.md#Common.Currency), [Parts](/modules/Inventory.md#Inventory.Part)
**Referenced by:** [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry)

<a id="Inventory.CaseEntryLink"></a>
### CaseEntryLinks

Represents a case link.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntryLinks`
- **Required permission:** Show case
- **Introduced in:** 25.1

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no | [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry) |
| `ChildId` | `Int64` | no | [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry) |

**References out:** [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry)

<a id="Inventory.CasePartLink"></a>
### CaseEntryPartLinks

Represents a case part link.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntryPartLinks`
- **Required permission:** Show case
- **Introduced in:** 24.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CaseId` | `Int64` | no | [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry) |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `IsDefault` | `Boolean` | no |  |
| `PartRevisionId` | `Int64?` | yes | [Revisions](/modules/Common.md#Common.Revision) |
| `RejectionCodeItemId` | `Int64` | no | [RejectionCodeItems](/modules/Common.md#Common.RejectionCodeItem) |
| `RejectedQuantity` | `Decimal` | no |  |
| `RejectionDescription` | `String` | no |  |
| `ProductRecordBatchId` | `Int64?` | yes | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `CompensationCustomerOrderId` | `Int64?` | yes | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `CompensationAccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable) |
| `CompensationPurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder) |
| `CompensationAccountsPayableId` | `Int64?` | yes | [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable) |

**References out:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [Parts](/modules/Inventory.md#Inventory.Part), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [RejectionCodeItems](/modules/Common.md#Common.RejectionCodeItem), [Revisions](/modules/Common.md#Common.Revision)
**Referenced by:** [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry)

<a id="Inventory.CaseEntryPhase"></a>
### CaseEntryPhases

Represents a case entry phase.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntryPhases`
- **Required permission:** Show case
- **Introduced in:** 2.45

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CaseManagementPhaseId` | `Int64` | no |  |
| `CaseManagementPhase` | `CaseManagementPhases` | no | [CaseManagementPhases](/modules/Inventory.md#Inventory.CaseManagementPhase) |
| `Description` | `String` | no |  |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `ParentId` | `Int64` | no | [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry) |
| `RowIndex` | `Int32` | no |  |
| `Activities` | `CaseEntryActivities[]` | no | [CaseEntryActivities](/modules/Inventory.md#Inventory.CaseEntryActivity) |

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CaseEntryActivities](/modules/Inventory.md#Inventory.CaseEntryActivity), [CaseManagementPhases](/modules/Inventory.md#Inventory.CaseManagementPhase)
**Referenced by:** [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry)

<a id="Inventory.CaseManagementActivity"></a>
### CaseManagementActivities

Represents a case management activity.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementActivities`
- **Required permission:** Show case
- **Introduced in:** 2.45

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PlannedTime` | `TimeSpan` | no |  |
| `CostPerHour` | `Decimal` | no |  |
| `CostPerHourCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `Chargeable` | `Boolean` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |

**References out:** [Currencies](/modules/Common.md#Common.Currency)
**Referenced by:** [CaseEntryActivities](/modules/Inventory.md#Inventory.CaseEntryActivity), [CaseManagementTemplateNodes](/modules/Inventory.md#Inventory.CaseManagementTemplateNode)

<a id="Inventory.CaseManagementCost"></a>
### CaseManagementCost

Represents a case management cost.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementCost`
- **Required permission:** Show basic data for case
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `Cost` | `Decimal` | no |  |
| `CostCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `Chargeable` | `Boolean` | no |  |

**References out:** [Currencies](/modules/Common.md#Common.Currency)
**Referenced by:** [CaseEntryAdditionalCost](/modules/Inventory.md#Inventory.CaseEntryAdditionalCost), [CaseManagementTemplateCosts](/modules/Inventory.md#Inventory.CaseManagementTemplateCost)

<a id="Inventory.CaseManagementPhase"></a>
### CaseManagementPhases

Represents a case management phase.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementPhases`
- **Required permission:** Show case
- **Introduced in:** 2.45

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int32` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [CaseEntryPhases](/modules/Inventory.md#Inventory.CaseEntryPhase), [CaseManagementTemplateNodes](/modules/Inventory.md#Inventory.CaseManagementTemplateNode)

<a id="Inventory.CaseManagementTemplateCost"></a>
### CaseManagementTemplateCosts

Represents a case management template cost.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementTemplateCosts`
- **Required permission:** Show basic data for case
- **Introduced in:** 23.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Cost` | `Decimal` | no |  |
| `CostCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `CostId` | `Int64?` | yes | [CaseManagementCost](/modules/Inventory.md#Inventory.CaseManagementCost) |
| `ParentId` | `Int64?` | yes | [CaseManagementTemplates](/modules/Inventory.md#Inventory.CaseManagementTemplate) |
| `IsChargeable` | `Boolean` | no |  |
| `RowIndex` | `Int32?` | yes |  |

**References out:** [CaseManagementCost](/modules/Inventory.md#Inventory.CaseManagementCost), [CaseManagementTemplates](/modules/Inventory.md#Inventory.CaseManagementTemplate), [Currencies](/modules/Common.md#Common.Currency)
**Referenced by:** [CaseManagementTemplates](/modules/Inventory.md#Inventory.CaseManagementTemplate)

<a id="Inventory.CaseManagementTemplateNode"></a>
### CaseManagementTemplateNodes

Represents a case management template node.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementTemplateNodes`
- **Required permission:** Show basic data for case
- **Introduced in:** 23.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ActivityId` | `Int64?` | yes | [CaseManagementActivities](/modules/Inventory.md#Inventory.CaseManagementActivity) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `PlannedTime` | `TimeSpan?` | yes |  |
| `LeadTime` | `Int32?` | yes |  |
| `Status` | `Int32` | no |  |
| `IsReminder` | `Boolean` | no |  |
| `IsMandatory` | `Boolean` | no |  |
| `IsIncludeActivityOnDocument` | `Boolean` | no |  |
| `IsChargeable` | `Boolean` | no |  |
| `UserId` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `PhaseId` | `Int64?` | yes | [CaseManagementPhases](/modules/Inventory.md#Inventory.CaseManagementPhase) |
| `ParentId` | `Int64?` | yes | [CaseManagementTemplates](/modules/Inventory.md#Inventory.CaseManagementTemplate) |
| `ParentNodeId` | `Int64?` | yes |  |
| `RowIndex` | `Int32?` | yes |  |

- `Status` — NotStarted=0, Started=1

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [CaseManagementActivities](/modules/Inventory.md#Inventory.CaseManagementActivity), [CaseManagementPhases](/modules/Inventory.md#Inventory.CaseManagementPhase), [CaseManagementTemplates](/modules/Inventory.md#Inventory.CaseManagementTemplate), [Comments](/modules/Common.md#Common.Comment)
**Referenced by:** [CaseManagementTemplates](/modules/Inventory.md#Inventory.CaseManagementTemplate)

<a id="Inventory.CaseManagementTemplate"></a>
### CaseManagementTemplates

Represents a case management template.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementTemplates`
- **Required permission:** Show basic data for case
- **Introduced in:** 23.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `CaseManagementTypeId` | `Int64?` | yes | [CaseManagementType](/modules/Inventory.md#Inventory.CaseManagementType) |
| `CaseManagementTemplateNode` | `CaseManagementTemplateNodes[]` | no | [CaseManagementTemplateNodes](/modules/Inventory.md#Inventory.CaseManagementTemplateNode) |
| `CaseManagementTemplateCost` | `CaseManagementTemplateCosts[]` | no | [CaseManagementTemplateCosts](/modules/Inventory.md#Inventory.CaseManagementTemplateCost) |

**References out:** [CaseManagementTemplateCosts](/modules/Inventory.md#Inventory.CaseManagementTemplateCost), [CaseManagementTemplateNodes](/modules/Inventory.md#Inventory.CaseManagementTemplateNode), [CaseManagementType](/modules/Inventory.md#Inventory.CaseManagementType)
**Referenced by:** [CaseManagementTemplateCosts](/modules/Inventory.md#Inventory.CaseManagementTemplateCost), [CaseManagementTemplateNodes](/modules/Inventory.md#Inventory.CaseManagementTemplateNode)

<a id="Inventory.CaseManagementType"></a>
### CaseManagementType

Represents a case management type.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementType`
- **Required permission:** Show basic data for case
- **Introduced in:** 2.22

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `IsPreset` | `Boolean` | no |  |
| `Number` | `Int64` | no |  |
| `Prefix` | `String` | no |  |
| `Priority` | `Int32` | no |  |
| `Visible` | `Boolean` | no |  |
| `Type` | `Int32` | no |  |

- `Type` — CustomerNonconformity=1, SupplierNonconformity=2, InternalNonconformity=3, Standard8D=4

**Referenced by:** [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CaseManagementTemplates](/modules/Inventory.md#Inventory.CaseManagementTemplate)

<a id="Inventory.GoodsType"></a>
### GoodsTypes

Represents a goods type.

- **Endpoint:** `GET /api/v1/Inventory/GoodsTypes`
- **Required permission:** Show package type/goods type
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `IsActive` | `Boolean` | no |  |

**Referenced by:** [CustomerOrderShippingInformationRows](/modules/Sales.md#Sales.CustomerOrderShippingInformationRow), [Parts](/modules/Inventory.md#Inventory.Part), [ShipmentPackageInformations](/modules/Sales.md#Sales.ShipmentPackageInformation)

<a id="Inventory.HyperLink"></a>
### HyperLinks

Represents a part hyperlink.

- **Endpoint:** `GET /api/v1/Inventory/HyperLinks`
- **Required permission:** Show part
- **Introduced in:** 2.55

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Link` | `String` | no |  |
| `Description` | `String` | no |  |

**References out:** [Parts](/modules/Inventory.md#Inventory.Part)
**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.Location"></a>
### Locations

Represents a location (so called generated location) Can also represent a stock package)

- **Endpoint:** `GET /api/v1/Inventory/Locations`
- **Required permission:** Show locations
- **Introduced in:** 24.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64?` | yes | [Locations](/modules/Inventory.md#Inventory.Location) |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Warehouse` | `Warehouses` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Name` | `String` | no |  |
| `StorageType` | `Int32` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `BlockedStatus` | `Int32` | no |  |
| `BlockMessageId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `BlockMessage` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |
| `SortingOrder` | `Int64?` | yes |  |
| `IsPackage` | `Boolean` | no |  |
| `MaxWidth` | `Decimal?` | yes |  |
| `MinWidth` | `Decimal?` | yes |  |
| `MaxLength` | `Decimal?` | yes |  |
| `MinLength` | `Decimal?` | yes |  |
| `MaxHeight` | `Decimal?` | yes |  |
| `MinHeight` | `Decimal?` | yes |  |
| `LoadCapacity` | `Decimal?` | yes |  |
| `PackagingPartId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `PackagingPart` | `Parts` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `ManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ManufacturingOrderMaterialId` | `Int64?` | yes | [ManufacturingOrderOperationReportings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting) |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder) |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `Rfid` | `String` | no |  |

- `StorageType` — SinglePartStorage=0, MultiplePartStorage=1
- `BlockedStatus` — None=0, Message=1, Blocked=2

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Comments](/modules/Common.md#Common.Comment), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [Locations](/modules/Inventory.md#Inventory.Location), [ManufacturingOrderOperationReportings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](/modules/Inventory.md#Inventory.Part), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [Locations](/modules/Inventory.md#Inventory.Location)

<a id="Inventory.OrderQuantityTemplate"></a>
### OrderQuantityTemplates

Represents a order quantity template on part that holds many partial quantities.

- **Endpoint:** `GET /api/v1/Inventory/OrderQuantityTemplates`
- **Required permission:** Show part
- **Introduced in:** 22.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](/modules/Common.md#Common.PartialQuantity) |

**References out:** [PartialQuantities](/modules/Common.md#Common.PartialQuantity)
**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.PackageType"></a>
### PackageTypes

Represents a package type.

- **Endpoint:** `GET /api/v1/Inventory/PackageTypes`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `IsActive` | `Boolean` | no |  |
| `Description` | `String` | no |  |
| `DefaultCode` | `String` | no |  |

**Referenced by:** [CustomerOrderShippingInformationRows](/modules/Sales.md#Sales.CustomerOrderShippingInformationRow), [Parts](/modules/Inventory.md#Inventory.Part), [ShipmentPackageInformations](/modules/Sales.md#Sales.ShipmentPackageInformation)

<a id="Inventory.PartActivity"></a>
### PartActivities

Represents an part activity.

- **Endpoint:** `GET /api/v1/Inventory/PartActivities`
- **Required permission:** Show part
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `ActivityTypeId` | `Int64` | no | [PartActivityTypes](/modules/Inventory.md#Inventory.PartActivityType) |
| `Description` | `String` | no |  |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `ReminderId` | `Int64` | no |  |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |
| `Status` | `Int32` | no |  |

- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Comments](/modules/Common.md#Common.Comment), [PartActivityTypes](/modules/Inventory.md#Inventory.PartActivityType), [Parts](/modules/Inventory.md#Inventory.Part)
**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.PartActivityType"></a>
### PartActivityTypes

Represents an part activity type.

- **Endpoint:** `GET /api/v1/Inventory/PartActivityTypes`
- **Required permission:** Show basic data for part
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [PartActivities](/modules/Inventory.md#Inventory.PartActivity)

<a id="Inventory.PartCode"></a>
### PartCodes

Represents a part code.

- **Endpoint:** `GET /api/v1/Inventory/PartCodes`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `Alias` | `String` | no |  |

**Referenced by:** [DiscountCategoryRows](/modules/Common.md#Common.DiscountCategoryRow), [Parts](/modules/Inventory.md#Inventory.Part), [PartTemplates](/modules/Inventory.md#Inventory.PartTemplate)

<a id="Inventory.PartDefaultTransportLabel"></a>
### PartDefaultTransportLabels

Represents a part's default transport label.

- **Endpoint:** `GET /api/v1/Inventory/PartDefaultTransportLabels`
- **Required permission:** Show part
- **Introduced in:** 23.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `FormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](/modules/Common.md#Common.FormReportConfiguration) |
| `Type` | `Int32` | no |  |
| `FormReportTypeId` | `Guid` | no |  |

- `Type` — NodeToStock=0, Rejection=1, OperationInProgress=2, OperationBeforeReporting=3, Subcontract=4, SalesTransportLabel=5, PurchaseTransportLabel=6, PurchaseRejectionTransportLabel=7, PurchaseReturnOrderTransportLabel=8

**References out:** [FormReportConfigurations](/modules/Common.md#Common.FormReportConfiguration), [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.PartIdentityType"></a>
### PartIdentityTypes

Represents a part identity type.

- **Endpoint:** `GET /api/v1/Inventory/PartIdentityTypes`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.47

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `IsActive` | `Boolean` | no |  |
| `Type` | `Int32?` | yes |  |

- `Type` — None=0, GTIN8=1, GTIN12=2, GTIN13=3, GTIN14=4, SGTIN=5

**Referenced by:** [PartOtherIdentities](/modules/Inventory.md#Inventory.PartOtherIdentity)

<a id="Inventory.PartImage"></a>
### PartImages

Represents a part image.

- **Endpoint:** `GET /api/v1/Inventory/PartImages`
- **Required permission:** Show part
- **Introduced in:** 25.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `PhotoThumbnailId` | `Int64` | no | [BlobData](/modules/Common.md#Common.BlobData) |
| `PhotoThumbnail` | `BlobData` | no | [BlobData](/modules/Common.md#Common.BlobData) |
| `ExternalVisible` | `Boolean` | no |  |

**References out:** [BlobData](/modules/Common.md#Common.BlobData), [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.PartLocationProductRecord"></a>
### PartLocationProductRecords

Represents a location quantity item where the quantity and possible product record is to be found.

- **Endpoint:** `GET /api/v1/Inventory/PartLocationProductRecords`
- **Required permission:** Show part
- **Introduced in:** 2.29

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartLocationId` | `Int64` | no | [PartLocations](/modules/Inventory.md#Inventory.PartLocation) |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `Quantity` | `Decimal` | no |  |

**References out:** [PartLocations](/modules/Inventory.md#Inventory.PartLocation), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord)
**Referenced by:** [PartLocations](/modules/Inventory.md#Inventory.PartLocation)

<a id="Inventory.PartLocation"></a>
### PartLocations

Represents a part location.

- **Endpoint:** `GET /api/v1/Inventory/PartLocations`
- **Required permission:** Show part
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Warehouse` | `Warehouses` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Name` | `String` | no |  |
| `Balance` | `Decimal` | no |  |
| `LifeCycleState` | `Int32` | no |  |
| `LatestArrivalDate` | `DateTimeOffset` | no |  |
| `WorkCenterPickingLocation` | `Boolean` | no |  |
| `WorkCenterPickingLocationFillingQuantity` | `Decimal` | no |  |
| `OutgoingPickLocation` | `Boolean` | no |  |
| `ArrivalLocation` | `Boolean` | no |  |
| `Priority` | `Int32?` | yes |  |
| `OutgoingPickLocationReorderPoint` | `Decimal` | no |  |
| `BatchNumber` | `String` | no |  |
| `SerialNumber` | `String` | no |  |
| `InventoryStatus` | `Int32` | no |  |
| `IsOngoingRefill` | `Boolean` | no |  |
| `RevisionId` | `Int64?` | yes | [Revisions](/modules/Common.md#Common.Revision) |
| `Revision` | `Revisions` | no | [Revisions](/modules/Common.md#Common.Revision) |
| `IgnoredBalance` | `Boolean` | no |  |
| `PartLocationProductRecords` | `PartLocationProductRecords[]` | no | [PartLocationProductRecords](/modules/Inventory.md#Inventory.PartLocationProductRecord) |

- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `InventoryStatus` — None=0, UnderInventory=1, UnderInventoryWithBalanceCheckpoint=2

**References out:** [PartLocationProductRecords](/modules/Inventory.md#Inventory.PartLocationProductRecord), [Parts](/modules/Inventory.md#Inventory.Part), [Revisions](/modules/Common.md#Common.Revision), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [PackageRowPartLocations](/modules/Sales.md#Sales.PackageRowPartLocation), [PartLocationProductRecords](/modules/Inventory.md#Inventory.PartLocationProductRecord), [Parts](/modules/Inventory.md#Inventory.Part), [PhysicalInventoryRows](/modules/Inventory.md#Inventory.PhysicalInventoryRow), [SalesPickingListRowQuantities](/modules/Sales.md#Sales.SalesPickingListRowQuantity), [StockBalanceChanges](/modules/Inventory.md#Inventory.StockBalanceChange), [StockTransactions](/modules/Inventory.md#Inventory.StockTransaction), [WithdrawalInformationLocation](/modules/Sales.md#Sales.WithdrawalInformationLocation)

<a id="Inventory.PartOtherIdentity"></a>
### PartOtherIdentities

Represents an alternate identity for a part.

- **Endpoint:** `GET /api/v1/Inventory/PartOtherIdentities`
- **Required permission:** Show part
- **Introduced in:** 2.47

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `TypeId` | `Int64` | no | [PartIdentityTypes](/modules/Inventory.md#Inventory.PartIdentityType) |
| `Value` | `String` | no |  |
| `IsActive` | `Boolean` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |

**References out:** [PartIdentityTypes](/modules/Inventory.md#Inventory.PartIdentityType), [Parts](/modules/Inventory.md#Inventory.Part)
**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.PartPlanningInformation"></a>
### PartPlanningInformation

Represents part planning information for a warehouse.

- **Endpoint:** `GET /api/v1/Inventory/PartPlanningInformation`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ContactId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `AbcCodeId` | `Int64?` | yes | [AbcCodes](/modules/Inventory.md#Inventory.AbcCode) |
| `AcquisitionWarehouseId` | `Int64?` | yes | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Eoq` | `Decimal` | no |  |
| `RoundingBase` | `Decimal` | no |  |
| `SafetyStock` | `Decimal` | no |  |
| `AnnualVolume` | `Decimal` | no |  |
| `LeadTime` | `TimeSpan?` | yes |  |
| `MinQuantity` | `Decimal` | no |  |
| `MaxQuantity` | `Decimal` | no |  |
| `ReorderPoint` | `Decimal` | no |  |
| `PalletQuantity` | `Decimal` | no |  |
| `AnnualVolumePace` | `Decimal` | no |  |
| `EoqPace` | `Decimal` | no |  |
| `LotSizingRule` | `Int32` | no |  |
| `LotSizingPeriod` | `TimeSpan` | no |  |
| `AllowOrderCreationFromCustomerOrder` | `Boolean` | no |  |
| `SafetyTime` | `TimeSpan` | no |  |
| `DeductSalesForecast` | `Int32` | no |  |
| `DeductionMethod` | `Int32` | no |  |
| `ActiveSupplierPartLinkId` | `Int64?` | yes | [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink) |
| `ActiveSupplierPartLink` | `SupplierPartLinks` | no | [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink) |
| `DefaultTransferProfileId` | `Int64?` | yes | [TransferProfiles](/modules/Common.md#Common.TransferProfile) |
| `PlanningMethod` | `Int32` | no |  |

- `LotSizingRule` — LotForLot=1, FixedQuantity=2, PeriodRequirement=3, Bucketpart=4, Linked=5
- `DeductSalesForecast` — None=0, LeadTime=1, Now=2
- `DeductionMethod` — Percent=0, TimeOrder=1, Closest=2, ClosestBefore=3, PeriodicIntervals=4
- `PlanningMethod` — Netting=0, StockRefill=1, Physical=2

**References out:** [AbcCodes](/modules/Inventory.md#Inventory.AbcCode), [Persons](/modules/Common.md#Common.Person), [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink), [TransferProfiles](/modules/Common.md#Common.TransferProfile), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.PartPurchaseControlDataRow"></a>
### PartPurchaseControlDataRows

Represents a purchase measuring plan for a part.

- **Endpoint:** `GET /api/v1/Inventory/PartPurchaseControlDataRows`
- **Required permission:** Show part
- **Introduced in:** 26.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](/modules/Common.md#Common.MeasuringTemplate) |
| `OverriddenFormTemplateId` | `Int64?` | yes | [FormTemplates](/modules/Common.md#Common.FormTemplate) |
| `OverriddenFrequencyText` | `String` | no |  |
| `OverriddenIntervalAmount` | `Int32?` | yes |  |
| `OverriddenInterval` | `Int32?` | yes |  |
| `SupplierId` | `Int64?` | yes | [Suppliers](/modules/Purchase.md#Purchase.Supplier) |

**References out:** [FormTemplates](/modules/Common.md#Common.FormTemplate), [MeasuringTemplates](/modules/Common.md#Common.MeasuringTemplate), [Parts](/modules/Inventory.md#Inventory.Part), [Suppliers](/modules/Purchase.md#Purchase.Supplier)
**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.PartPurchaseExpenseValues"></a>
### PartPurchaseExpenseValues

Represents a part purchase expense values entity.

- **Endpoint:** `GET /api/v1/Inventory/PartPurchaseExpenseValues`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.48

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no |  |
| `Expense1PercentOfPriceValue` | `Decimal` | no |  |
| `Expense1PerEachValue` | `Decimal` | no |  |
| `Expense2PercentOfPriceValue` | `Decimal` | no |  |
| `Expense2PerEachValue` | `Decimal` | no |  |
| `Expense3PercentOfPriceValue` | `Decimal` | no |  |
| `Expense3PerEachValue` | `Decimal` | no |  |
| `CertificatePercentOfPriceValue` | `Decimal` | no |  |
| `CertificatePerEachValue` | `Decimal` | no |  |
| `CertificatePerKgValue` | `Decimal` | no |  |
| `CertificatePerPackageValue` | `Decimal` | no |  |
| `CertificatePerOrderValue` | `Decimal` | no |  |
| `CertificatePerQuantityValue` | `Decimal` | no |  |
| `CertificateQuantityValue` | `Decimal` | no |  |
| `Expense1PerKgValue` | `Decimal` | no |  |
| `Expense1PerPackageValue` | `Decimal` | no |  |
| `Expense1PerOrderValue` | `Decimal` | no |  |
| `Expense1PerQuantityValue` | `Decimal` | no |  |
| `Expense1QuantityValue` | `Decimal` | no |  |
| `Expense2PerKgValue` | `Decimal` | no |  |
| `Expense2PerPackageValue` | `Decimal` | no |  |
| `Expense2PerOrderValue` | `Decimal` | no |  |
| `Expense2PerQuantityValue` | `Decimal` | no |  |
| `Expense2QuantityValue` | `Decimal` | no |  |
| `Expense3PerKgValue` | `Decimal` | no |  |
| `Expense3PerPackageValue` | `Decimal` | no |  |
| `Expense3PerOrderValue` | `Decimal` | no |  |
| `Expense3PerQuantityValue` | `Decimal` | no |  |
| `Expense3QuantityValue` | `Decimal` | no |  |
| `Expense4PercentOfPriceValue` | `Decimal` | no |  |
| `Expense4PerEachValue` | `Decimal` | no |  |
| `Expense4PerKgValue` | `Decimal` | no |  |
| `Expense4PerPackageValue` | `Decimal` | no |  |
| `Expense4PerOrderValue` | `Decimal` | no |  |
| `Expense4PerQuantityValue` | `Decimal` | no |  |
| `Expense4QuantityValue` | `Decimal` | no |  |
| `Expense5PercentOfPriceValue` | `Decimal` | no |  |
| `Expense5PerEachValue` | `Decimal` | no |  |
| `Expense5PerKgValue` | `Decimal` | no |  |
| `Expense5PerPackageValue` | `Decimal` | no |  |
| `Expense5PerOrderValue` | `Decimal` | no |  |
| `Expense5PerQuantityValue` | `Decimal` | no |  |
| `Expense5QuantityValue` | `Decimal` | no |  |

**Referenced by:** [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink)

<a id="Inventory.Part"></a>
### Parts

Represents a part.

- **Endpoint:** `GET /api/v1/Inventory/Parts`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartNumber` | `String` | no |  |
| `Description` | `String` | no |  |
| `ExtraDescription` | `String` | no |  |
| `CompanyId` | `Int64` | no |  |
| `Length` | `Decimal?` | yes |  |
| `Width` | `Decimal?` | yes |  |
| `Height` | `Decimal?` | yes |  |
| `PackagingType` | `Int32` | no |  |
| `PackageVolumeConsistsOf` | `Int32` | no |  |
| `PackageTypeId` | `Int64?` | yes | [PackageTypes](/modules/Inventory.md#Inventory.PackageType) |
| `PackageType` | `PackageTypes` | no | [PackageTypes](/modules/Inventory.md#Inventory.PackageType) |
| `PartPlanningInformations` | `PartPlanningInformation[]` | no | [PartPlanningInformation](/modules/Inventory.md#Inventory.PartPlanningInformation) |
| `UseRandomLocationStorage` | `Boolean` | no |  |
| `ShowFictiousStructureOnOrderRegistration` | `Boolean` | no |  |
| `TraceabilityMode` | `Int32` | no |  |
| `UseBestBeforeDate` | `Boolean` | no |  |
| `DaysToAddToBestBeforeDate` | `Int32?` | yes |  |
| `SuggestBestBeforeDate` | `Int32` | no |  |
| `ManageStockBalance` | `Boolean` | no |  |
| `StandardPrice` | `Decimal` | no |  |
| `StandardPriceCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `FutureStandardPrice` | `Decimal?` | yes |  |
| `FutureStandardPriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `PostCalculatedAveragePrice` | `Decimal?` | yes |  |
| `PostCalculatedAveragePriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `Type` | `Int32` | no |  |
| `ProductGroupId` | `Int64` | no | [ProductGroups](/modules/Common.md#Common.ProductGroup) |
| `ProductGroup` | `ProductGroups` | no | [ProductGroups](/modules/Common.md#Common.ProductGroup) |
| `WeightPerUnit` | `Decimal?` | yes |  |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](/modules/Common.md#Common.StatisticalGoodsCode) |
| `StatisticalGoodsCode` | `StatisticalGoodsCodes` | no | [StatisticalGoodsCodes](/modules/Common.md#Common.StatisticalGoodsCode) |
| `StatisticalGoodsValue` | `Decimal?` | yes |  |
| `CountryOfOriginId` | `Int64?` | yes | [Countries](/modules/Common.md#Common.Country) |
| `CountryOfOrigin` | `Countries` | no | [Countries](/modules/Common.md#Common.Country) |
| `PartCodeId` | `Int64?` | yes | [PartCodes](/modules/Inventory.md#Inventory.PartCode) |
| `PartCode` | `PartCodes` | no | [PartCodes](/modules/Inventory.md#Inventory.PartCode) |
| `CategoryString` | `String` | no |  |
| `StorageOverheadMarkupId` | `Int64` | no | [StorageOverheadMarkups](/modules/Inventory.md#Inventory.StorageOverheadMarkup) |
| `StorageOverheadMarkup` | `StorageOverheadMarkups` | no | [StorageOverheadMarkups](/modules/Inventory.md#Inventory.StorageOverheadMarkup) |
| `SalesOverheadMarkupId` | `Int64` | no | [SalesOverheadMarkups](/modules/Inventory.md#Inventory.SalesOverheadMarkup) |
| `SalesOverheadMarkup` | `SalesOverheadMarkups` | no | [SalesOverheadMarkups](/modules/Inventory.md#Inventory.SalesOverheadMarkup) |
| `ProfitMarkupId` | `Int64` | no | [ProfitMarkups](/modules/Inventory.md#Inventory.ProfitMarkup) |
| `ProfitMarkup` | `ProfitMarkups` | no | [ProfitMarkups](/modules/Inventory.md#Inventory.ProfitMarkup) |
| `VolumePerUnit` | `Decimal?` | yes |  |
| `AveragePrice` | `Decimal?` | yes |  |
| `AveragePriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `LastPurchasePrice` | `Decimal?` | yes |  |
| `LastPurchasePriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `AveragePriceTimestamp` | `DateTimeOffset?` | yes |  |
| `PurchaseLabelType` | `Int32` | no |  |
| `CurrentAlloyId` | `Int64?` | yes | [Alloys](/modules/Inventory.md#Inventory.Alloy) |
| `CurrentAlloy` | `Alloys` | no | [Alloys](/modules/Inventory.md#Inventory.Alloy) |
| `PurchaseQuantityPerPackage` | `Decimal?` | yes |  |
| `IsPackaging` | `Boolean` | no |  |
| `Status` | `Int32` | no |  |
| `PurchaseAndManufactureOnProject` | `Int32` | no |  |
| `ServiceType` | `Int32` | no |  |
| `QuantityPerPackage` | `Decimal?` | yes |  |
| `PackagingWeightPerPackage` | `Decimal?` | yes |  |
| `PackagingPartId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `PackagingPart` | `Parts` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `LoadingMetersPerUnit` | `Decimal?` | yes |  |
| `PackingReference` | `String` | no |  |
| `Gs1Code` | `String` | no |  |
| `VatRateId` | `Int64?` | yes | [VatRates](/modules/Common.md#Common.VatRate) |
| `VatRate` | `VatRates` | no | [VatRates](/modules/Common.md#Common.VatRate) |
| `LastSalesPrice` | `Decimal?` | yes |  |
| `LastSalesPriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `TransportCost` | `Decimal?` | yes |  |
| `SerialNumberGeneration` | `Int32` | no |  |
| `SerialNumberGenerationSource` | `Int32` | no |  |
| `GoodsType` | `String` | no |  |
| `LeadTimeToCustomer` | `TimeSpan?` | yes |  |
| `QuantityForLeadtimeToCustomer` | `Decimal?` | yes |  |
| `SalesLabelType` | `Int32` | no |  |
| `DefaultCustomerOrderWarehouseId` | `Int64?` | yes | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `ManufacturingLabelType` | `Int32` | no |  |
| `PreparerId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `Preparer` | `Persons` | no | [Persons](/modules/Common.md#Common.Person) |
| `GoodsTypeId` | `Int64?` | yes | [GoodsTypes](/modules/Inventory.md#Inventory.GoodsType) |
| `ExpGoodsType` | `GoodsTypes` | no | [GoodsTypes](/modules/Inventory.md#Inventory.GoodsType) |
| `CalculatedQuantity` | `Decimal` | no |  |
| `Alias` | `String` | no |  |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `BlockedStatus` | `Int32` | no |  |
| `BlockedContextType` | `Int32` | no |  |
| `BlockMessageId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `BlockMessage` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |
| `ReceivingInspectionType` | `Int32` | no |  |
| `StandardUnitId` | `Int64` | no | [Units](/modules/Common.md#Common.Unit) |
| `StandardPartUnitUsageId` | `Int64` | no | [PartUnitUsages](/modules/Common.md#Common.PartUnitUsage) |
| `StandardPartUnitUsage` | `PartUnitUsages` | no | [PartUnitUsages](/modules/Common.md#Common.PartUnitUsage) |
| `PartUnitUsages` | `PartUnitUsages[]` | no | [PartUnitUsages](/modules/Common.md#Common.PartUnitUsage) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `ActiveRevisionId` | `Int64?` | yes | [Revisions](/modules/Common.md#Common.Revision) |
| `ActiveRevision` | `Revisions` | no | [Revisions](/modules/Common.md#Common.Revision) |
| `LatestCalculationId` | `Int64?` | yes |  |
| `ReceivingInstructionId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `ReceivingInstruction` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `PurchaseCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `PurchaseComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `PickingInstructionId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `PickingInstruction` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `SalesCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `SalesComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `ManufacturingCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `ManufacturingComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `PreparationId` | `Int64?` | yes | [Preparations](/modules/Manufacturing.md#Manufacturing.Preparation) |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](/modules/Common.md#Common.ExtraField) |
| `CustomerPartLinks` | `CustomerPartLinks[]` | no | [CustomerPartLinks](/modules/Sales.md#Sales.CustomerPartLink) |
| `SupplierPartLinks` | `SupplierPartLinks[]` | no | [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink) |
| `Revisions` | `Revisions[]` | no | [Revisions](/modules/Common.md#Common.Revision) |
| `Drawings` | `Drawings[]` | no | [Drawings](/modules/Manufacturing.md#Manufacturing.Drawing) |
| `PartLocations` | `PartLocations[]` | no | [PartLocations](/modules/Inventory.md#Inventory.PartLocation) |
| `HyperLinks` | `HyperLinks[]` | no | [HyperLinks](/modules/Inventory.md#Inventory.HyperLink) |
| `PartActivities` | `PartActivities[]` | no | [PartActivities](/modules/Inventory.md#Inventory.PartActivity) |
| `ConfigurationTemplateId` | `Int64?` | yes |  |
| `ConfigurationTemplate` | `PartConfigurationTemplates` | no | [PartConfigurationTemplates](/modules/Common.md#Common.PartConfigurationTemplate) |
| `OtherIdentities` | `PartOtherIdentities[]` | no | [PartOtherIdentities](/modules/Inventory.md#Inventory.PartOtherIdentity) |
| `Notes` | `BusinessContactNoteHistories[]` | no | [BusinessContactNoteHistories](/modules/Common.md#Common.BusinessContactNoteHistory) |
| `ConfigurationSelectionDescription` | `String` | no |  |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityTemplates](/modules/Inventory.md#Inventory.OrderQuantityTemplate) |
| `OrderQuantity` | `OrderQuantityTemplates` | no | [OrderQuantityTemplates](/modules/Inventory.md#Inventory.OrderQuantityTemplate) |
| `ProjectId` | `Int64?` | yes | [Projects](/modules/Common.md#Common.Project) |
| `PartTemplateId` | `Int64?` | yes | [PartTemplates](/modules/Inventory.md#Inventory.PartTemplate) |
| `PartTemplate` | `PartTemplates` | no | [PartTemplates](/modules/Inventory.md#Inventory.PartTemplate) |
| `IsFixedWeight` | `Boolean` | no |  |
| `MaterialValidationSetting` | `Int32` | no |  |
| `AutomaticReportingMode` | `Int32` | no |  |
| `EmissionFactorId` | `Int64?` | yes |  |
| `EmissionFactor` | `EmissionFactors` | no |  |
| `Emissions` | `Decimal?` | yes |  |
| `ControlDataRows` | `PartPurchaseControlDataRows[]` | no | [PartPurchaseControlDataRows](/modules/Inventory.md#Inventory.PartPurchaseControlDataRow) |

- `PackagingType` — Unspecified=0, OuterPackaging=1, EurPallets=2, InnerPackaging=3, CoverPackaging=4
- `PackageVolumeConsistsOf` — SurroundingPackagingVolume=0, PackagingVolumeAndPartVolume=1
- `TraceabilityMode` — None=0, Batch=1, Individual=2, IndividualOnlyWithdrawal=4
- `SuggestBestBeforeDate` — No=0, AddDays=1, ShortestFromReportedMaterial=2
- `Type` — Purchased=0, Manufactured=1, Fictitious=2, Service=5, Subcontract=6
- `PurchaseLabelType` — None=0, Transport=1, Label=2, SmallLabel=3, MultiLabel=4, SelectAtPrintout=5
- `Status` — Quote=1, Prototype=2, New=3, Normal=4, NewRevision=5, PhasingOut=6, Expired=9, Inactive=99
- `PurchaseAndManufactureOnProject` — No=0, Yes=1, PickFromStockFirst=2
- `ServiceType` — Unspecified=0, Freight=1, AlloyCost=2
- `SerialNumberGeneration` — Never=0, CustomerOrderRegistration=1, ManufacturingOrderRegistration=2, DeliveryReporting=3
- `SerialNumberGenerationSource` — NumberSeries=0, Manual=1
- `SalesLabelType` — None=0, Transport=1, Label=2, SmallLabel=3, MultiLabel=4, SelectAtPrintout=5
- `ManufacturingLabelType` — None=0, Transport=1, Label=2, SmallLabel=3, MultiLabel=4, SelectAtPrintout=5
- `BlockedStatus` — None=0, Message=1, Blocked=2
- `BlockedContextType` (bitmask) — None=0, RegisterManufacturingOrder=1, RegisterPurchaseOrder=2, RegisterCustomerOrder=4, ReportManufacturingOrder=8, ReportPurchaseOrder=16, ReportCustomerOrder=32, WithdrawalManufacturingOrder=64, Preparation=128, ConfigurationSelection=256, RegisterAgreement=512, RegisterBlanketOrderPurchase=1024, RegisterBlanketOrderSales=2048, RegisterQuote=4096
- `ReceivingInspectionType` — None=0, Always=1, VariableInspection=2
- `MaterialValidationSetting` (bitmask) — ActualOperation=0, AnyOperation=1
- `AutomaticReportingMode` (bitmask) — PickingLocation=1, Cleared=2, BufferLocation=4, Project=8

**References out:** [Alloys](/modules/Inventory.md#Inventory.Alloy), [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [BusinessContactNoteHistories](/modules/Common.md#Common.BusinessContactNoteHistory), [Comments](/modules/Common.md#Common.Comment), [Countries](/modules/Common.md#Common.Country), [Currencies](/modules/Common.md#Common.Currency), [CustomerPartLinks](/modules/Sales.md#Sales.CustomerPartLink), [Drawings](/modules/Manufacturing.md#Manufacturing.Drawing), [ExtraFields](/modules/Common.md#Common.ExtraField), [GoodsTypes](/modules/Inventory.md#Inventory.GoodsType), [HyperLinks](/modules/Inventory.md#Inventory.HyperLink), [OrderQuantityTemplates](/modules/Inventory.md#Inventory.OrderQuantityTemplate), [PackageTypes](/modules/Inventory.md#Inventory.PackageType), [PartActivities](/modules/Inventory.md#Inventory.PartActivity), [PartCodes](/modules/Inventory.md#Inventory.PartCode), [PartConfigurationTemplates](/modules/Common.md#Common.PartConfigurationTemplate), [PartLocations](/modules/Inventory.md#Inventory.PartLocation), [PartOtherIdentities](/modules/Inventory.md#Inventory.PartOtherIdentity), [PartPlanningInformation](/modules/Inventory.md#Inventory.PartPlanningInformation), [PartPurchaseControlDataRows](/modules/Inventory.md#Inventory.PartPurchaseControlDataRow), [Parts](/modules/Inventory.md#Inventory.Part), [PartTemplates](/modules/Inventory.md#Inventory.PartTemplate), [PartUnitUsages](/modules/Common.md#Common.PartUnitUsage), [Persons](/modules/Common.md#Common.Person), [Preparations](/modules/Manufacturing.md#Manufacturing.Preparation), [ProductGroups](/modules/Common.md#Common.ProductGroup), [ProfitMarkups](/modules/Inventory.md#Inventory.ProfitMarkup), [Projects](/modules/Common.md#Common.Project), [Revisions](/modules/Common.md#Common.Revision), [SalesOverheadMarkups](/modules/Inventory.md#Inventory.SalesOverheadMarkup), [StatisticalGoodsCodes](/modules/Common.md#Common.StatisticalGoodsCode), [StorageOverheadMarkups](/modules/Inventory.md#Inventory.StorageOverheadMarkup), [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink), [Units](/modules/Common.md#Common.Unit), [VatRates](/modules/Common.md#Common.VatRate), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [AlloyQuantities](/modules/Inventory.md#Inventory.AlloyQuantity), [Alloys](/modules/Inventory.md#Inventory.Alloy), [BlanketOrderPurchaseRows](/modules/Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderSalesRows](/modules/Sales.md#Sales.BlanketOrderSalesRow), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CaseEntryAdditionalCost](/modules/Inventory.md#Inventory.CaseEntryAdditionalCost), [CaseEntryPartLinks](/modules/Inventory.md#Inventory.CasePartLink), [CustomerOrderPaymentPlanRows](/modules/Sales.md#Sales.CustomerOrderPaymentPlanRow), [CustomerOrderRowInflows](/modules/Sales.md#Sales.CustomerOrderRowInflow), [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [CustomerOrderShippingInformationRows](/modules/Sales.md#Sales.CustomerOrderShippingInformationRow), [CustomerPartLinks](/modules/Sales.md#Sales.CustomerPartLink), [Drawings](/modules/Manufacturing.md#Manufacturing.Drawing), [FormTemplateRows](/modules/Common.md#Common.FormTemplateRow), [HyperLinks](/modules/Inventory.md#Inventory.HyperLink), [InquiryRows](/modules/Purchase.md#Purchase.InquiryRow), [InvoiceLogs](/modules/Sales.md#Sales.InvoiceLog), [Locations](/modules/Inventory.md#Inventory.Location), [MaintenanceReportingRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingRow), [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [PackageRows](/modules/Sales.md#Sales.PackageRow), [PartActivities](/modules/Inventory.md#Inventory.PartActivity), [PartConfigurationResults](/modules/Common.md#Common.PartConfigurationResult), [PartConfigurationSelectionGroupResults](/modules/Common.md#Common.PartConfigurationSelectionGroupResult), [PartDefaultTransportLabels](/modules/Inventory.md#Inventory.PartDefaultTransportLabel), [PartialQuantities](/modules/Common.md#Common.PartialQuantity), [PartImages](/modules/Inventory.md#Inventory.PartImage), [PartLocations](/modules/Inventory.md#Inventory.PartLocation), [PartOtherIdentities](/modules/Inventory.md#Inventory.PartOtherIdentity), [PartPurchaseControlDataRows](/modules/Inventory.md#Inventory.PartPurchaseControlDataRow), [Parts](/modules/Inventory.md#Inventory.Part), [PartUnitUsages](/modules/Common.md#Common.PartUnitUsage), [PaymentPlanTemplateRows](/modules/Common.md#Common.PaymentPlanTemplateRow), [PhysicalInventoryRows](/modules/Inventory.md#Inventory.PhysicalInventoryRow), [PriceChangeLogs](/modules/Inventory.md#Inventory.PriceChangeLog), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow), [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange), [QuoteRows](/modules/Sales.md#Sales.QuoteRow), [Revisions](/modules/Common.md#Common.Revision), [SalesAgreementBasisRows](/modules/Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRowInflows](/modules/Sales.md#Sales.SalesAgreementRowInflow), [SalesAgreementRows](/modules/Sales.md#Sales.SalesAgreementRow), [SalesForecastRows](/modules/Inventory.md#Inventory.SalesForecastRow), [SalesPickingListRowQuantities](/modules/Sales.md#Sales.SalesPickingListRowQuantity), [SalesPrices](/modules/Sales.md#Sales.SalesPrice), [StaggeredPrices](/modules/Common.md#Common.StaggeredPrice), [StockTransactions](/modules/Inventory.md#Inventory.StockTransaction), [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink)

<a id="Inventory.PartTemplate"></a>
### PartTemplates

Represents a part template.

- **Endpoint:** `GET /api/v1/Inventory/PartTemplates`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.47

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AbcCodeId` | `Int64?` | yes | [AbcCodes](/modules/Inventory.md#Inventory.AbcCode) |
| `AnnualVolume` | `Decimal?` | yes |  |
| `AutomaticReportingMode` | `Int32?` | yes |  |
| `CategoryString` | `String` | no |  |
| `Code` | `String` | no |  |
| `CountryOfOriginId` | `Int64?` | yes | [Countries](/modules/Common.md#Common.Country) |
| `DeductSalesForecast` | `Int32?` | yes |  |
| `DeductionMethod` | `Int32?` | yes |  |
| `Description` | `String` | no |  |
| `Eoq` | `Decimal?` | yes |  |
| `IsActive` | `Boolean` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `IsPreset` | `Boolean` | no |  |
| `LotSizingRule` | `Int32?` | yes |  |
| `ManageStockBalance` | `Boolean?` | yes |  |
| `UseRandomLocationStorage` | `Boolean?` | yes |  |
| `AllowOrderCreationFromCustomerOrder` | `Boolean?` | yes |  |
| `RoundingBase` | `Decimal?` | yes |  |
| `LeadTime` | `TimeSpan?` | yes |  |
| `ManufacturingLabelType` | `Int32?` | yes |  |
| `SalesLabelType` | `Int32?` | yes |  |
| `PurchaseLabelType` | `Int32?` | yes |  |
| `UseInCalculation` | `Boolean` | no |  |
| `PartCodeId` | `Int64?` | yes | [PartCodes](/modules/Inventory.md#Inventory.PartCode) |
| `PartType` | `Int32?` | yes |  |
| `PreparerId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `ProductGroupId` | `Int64?` | yes | [ProductGroups](/modules/Common.md#Common.ProductGroup) |
| `ReorderPoint` | `Decimal?` | yes |  |
| `SafetyStock` | `Decimal?` | yes |  |
| `SafetyTime` | `TimeSpan?` | yes |  |
| `SerialNumberGeneration` | `Int32?` | yes |  |
| `SerialNumberGenerationSource` | `Int32?` | yes |  |
| `TemplateType` | `Int32` | no |  |
| `TraceabilityMode` | `Int32?` | yes |  |
| `ProfitMarkupId` | `Int64?` | yes | [ProfitMarkups](/modules/Inventory.md#Inventory.ProfitMarkup) |
| `SalesOverheadMarkupId` | `Int64?` | yes | [SalesOverheadMarkups](/modules/Inventory.md#Inventory.SalesOverheadMarkup) |
| `PartActivityTemplateId` | `Int64?` | yes |  |
| `PartStatus` | `Int32?` | yes |  |
| `LithuanianCountyOfOrigin` | `Int32?` | yes |  |

- `AutomaticReportingMode` — PickingLocation=1, Cleared=2, BufferLocation=4, Project=8
- `DeductSalesForecast` — None=0, LeadTime=1, Now=2
- `DeductionMethod` — Percent=0, TimeOrder=1, Closest=2, ClosestBefore=3, PeriodicIntervals=4
- `LotSizingRule` — LotForLot=1, FixedQuantity=2, PeriodRequirement=3, Bucketpart=4, Linked=5
- `ManufacturingLabelType` — None=0, Transport=1, Label=2, SmallLabel=3, MultiLabel=4, SelectAtPrintout=5
- `SalesLabelType` — None=0, Transport=1, Label=2, SmallLabel=3, MultiLabel=4, SelectAtPrintout=5
- `PurchaseLabelType` — None=0, Transport=1, Label=2, SmallLabel=3, MultiLabel=4, SelectAtPrintout=5
- `PartType` — Purchased=0, Manufactured=1, Fictitious=2, Service=5, Subcontract=6
- `SerialNumberGeneration` — Never=0, CustomerOrderRegistration=1, ManufacturingOrderRegistration=2, DeliveryReporting=3
- `SerialNumberGenerationSource` — NumberSeries=0, Manual=1
- `TemplateType` — Part=0, ConsumableEquipment=1, ReusableEquipment=2, EquipmentList=3
- `TraceabilityMode` — None=0, Batch=1, Individual=2, IndividualOnlyWithdrawal=4
- `PartStatus` — Quote=1, Prototype=2, New=3, Normal=4, NewRevision=5, PhasingOut=6, Expired=9, Inactive=99
- `LithuanianCountyOfOrigin` — A=1, K=2, L=3, M=4, P=5, S=6, J=7, T=8, U=9, V=10

**References out:** [AbcCodes](/modules/Inventory.md#Inventory.AbcCode), [Countries](/modules/Common.md#Common.Country), [PartCodes](/modules/Inventory.md#Inventory.PartCode), [Persons](/modules/Common.md#Common.Person), [ProductGroups](/modules/Common.md#Common.ProductGroup), [ProfitMarkups](/modules/Inventory.md#Inventory.ProfitMarkup), [SalesOverheadMarkups](/modules/Inventory.md#Inventory.SalesOverheadMarkup)
**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.PhysicalInventoryList"></a>
### PhysicalInventoryLists

Represents a physical inventory list.

- **Endpoint:** `GET /api/v1/Inventory/PhysicalInventoryLists`
- **Required permission:** Report stock count
- **Introduced in:** 22.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Number` | `Int64` | no |  |
| `Version` | `Int32` | no |  |
| `Name` | `String` | no |  |
| `InventoryStatus` | `Int32` | no |  |
| `State` | `Int32` | no |  |
| `CreatedWhen` | `DateTimeOffset` | no |  |
| `PrintedWhen` | `DateTimeOffset?` | yes |  |

- `InventoryStatus` — None=0, UnderInventory=1, UnderInventoryWithBalanceCheckpoint=2
- `State` — NotStarted=0, Started=1, Paused=2, Finished=3, FinishedWithPendingApproval=4

**References out:** [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [PhysicalInventoryRows](/modules/Inventory.md#Inventory.PhysicalInventoryRow)

<a id="Inventory.PhysicalInventoryRow"></a>
### PhysicalInventoryRows

Represents a physical inventory row.

- **Endpoint:** `GET /api/v1/Inventory/PhysicalInventoryRows`
- **Required permission:** Report stock count
- **Introduced in:** 22.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PhysicalInventoryListId` | `Int64` | no | [PhysicalInventoryLists](/modules/Inventory.md#Inventory.PhysicalInventoryList) |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `LocationId` | `Int64` | no | [PartLocations](/modules/Inventory.md#Inventory.PartLocation) |
| `ProductRecordId` | `Int64` | no | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `Reported` | `Boolean` | no |  |
| `ReportingState` | `Int32` | no |  |
| `Version` | `Int32` | no |  |
| `ReportedQuantity` | `Decimal?` | yes |  |

- `ReportingState` — NotReported=0, Reported=1, PendingApproval=2, ApprovalRejected=3, Discarded=4

**References out:** [PartLocations](/modules/Inventory.md#Inventory.PartLocation), [Parts](/modules/Inventory.md#Inventory.Part), [PhysicalInventoryLists](/modules/Inventory.md#Inventory.PhysicalInventoryList), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord)

<a id="Inventory.PriceChangeLog"></a>
### PriceChangeLogs

Represents a price change log entity.

- **Endpoint:** `GET /api/v1/Inventory/PriceChangeLogs`
- **Required permission:** Show part
- **Introduced in:** 2.51

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Context` | `Int32` | no |  |
| `PriceType` | `Int32` | no |  |
| `PriceListId` | `Int64?` | yes | [PriceLists](/modules/Common.md#Common.PriceList) |
| `Timestamp` | `DateTimeOffset` | no |  |
| `UserCode` | `String` | no |  |
| `NewPriceAmount` | `Decimal?` | yes |  |
| `NewPriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `OldPriceAmount` | `Decimal?` | yes |  |
| `OldPriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `Balance` | `Decimal?` | yes |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `CalculationId` | `Int64?` | yes |  |
| `SupplierId` | `Int64?` | yes | [Suppliers](/modules/Purchase.md#Purchase.Supplier) |
| `CustomerId` | `Int64?` | yes | [Customers](/modules/Sales.md#Sales.Customer) |
| `StaggeredQuantity` | `Decimal?` | yes |  |
| `IsSetupPrice` | `Boolean` | no |  |
| `Discount` | `Decimal?` | yes |  |
| `IsExportedToManagementAccounting` | `Boolean` | no |  |

- `Context` — Manual=0, PreCalculation=1, PostCalculation=2, ManualFromList=3, PriceImport=4, PurchaseCalculation=5, PartSynchronization=6, CancelInvoice=7, CreditInvoice=8, Invoice=9, ExpenseInvoice=10, UndoExpenseInvoice=11, SubcontractingCostReport=12, AutoUpdateFromFuturePrice=13, PriceCorrectionInvoice=14, ReportingOfReturnOrder=15, FinalRecordingOfCorrectionInvoice=16, FullReturnToSupplier=17, AutomaticMovingAveragePriceCalculation=18
- `PriceType` — Standard=0, PriceList=3, FuturePriceList=4, PriceFromInvoiceOrCustomerOrderRow=5, Invoice=6, PriceListStaggered=7, FuturePriceListStaggered=8, CustomerStaggered=9, FutureCustomerStaggered=10, SupplierStaggered=11, FutureSupplierStaggered=12, StandardPriceFromCustomerOrderRowWithFallbackToPartStandardPrice=13, CustomerWithFallbackPriceListOnCustomer=14, FutureSetupPrice=15, StandardPriceOnDelivery=16, StandardPriceOnInvoicing=17, StandardPriceOnFinalBookingAccountsPayable=18, PurchaseOrder=19, FifoAtInvoicing=20, LinkedConfiguredCustomOrderRow=21, HistoricalFifoPrice=22, ComparativePrice=23, ProductRecordStandardPrice=24, MovingAveragePrice=25, MovingAveragePriceAtInvoicing=26, FutureSupplier=-9998, FutureCustomer=-9997, None=-99, ReportedStandard=-20, MaterialCost=-19, HistoricalStandard=-18, DiscountedCustomer=-17, DiscountedSupplier=-16, PostCalculatedAverage=-15, SavedAverage=-14, Lowest=-9, FIFO=-8, AvarageSales=-7, LatestSales=-6, AveragePurchase=-5, LatestPurchase=-4, Customer=-3, Supplier=-2, FutureStandard=-1

**References out:** [Currencies](/modules/Common.md#Common.Currency), [Customers](/modules/Sales.md#Sales.Customer), [Parts](/modules/Inventory.md#Inventory.Part), [PriceLists](/modules/Common.md#Common.PriceList), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Inventory.ProductRecordOperationReporting"></a>
### ProductRecordOperationReportings

Represents a product record operation reporting.

- **Endpoint:** `GET /api/v1/Inventory/ProductRecordOperationReportings`
- **Required permission:** Show serial number
- **Introduced in:** 2.49

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  |
| `ReportingType` | `Int32` | no |  |
| `ProductRecordId` | `Int64` | no | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `OperationReportingId` | `Int64?` | yes |  |
| `OrderNumber` | `String` | no |  |
| `ReportedTime` | `TimeSpan?` | yes |  |
| `ReportedQuantity` | `Decimal?` | yes |  |
| `QuantityPerCycle` | `Decimal?` | yes |  |
| `CycleTime` | `TimeSpan?` | yes |  |
| `TotalTime` | `TimeSpan?` | yes |  |
| `TotalCycles` | `Decimal` | no |  |
| `TotalMeasurementSetting` | `Decimal` | no |  |
| `ReportedMeasurementSetting` | `Decimal?` | yes |  |

- `ReportingType` — OperationReporting=0, Inventory=1, Rejection=2

**References out:** [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord)
**Referenced by:** [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord)

<a id="Inventory.ProductRecord"></a>
### ProductRecords

Represents a product record.

- **Endpoint:** `GET /api/v1/Inventory/ProductRecords`
- **Required permission:** Show serial number
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ProductRecordType` | `Int32` | no |  |
| `SerialNumberWithPartNumber` | `String` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CertificateId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Certificate` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `WarrantyCommitmentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `WarrantyCommitment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `InstallationCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `InstallationComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `SerialNumber` | `String` | no |  |
| `ChargeNumber` | `String` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `ManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ManufacturingOrder` | `ManufacturingOrders` | no | [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](/modules/Common.md#Common.ExtraField) |
| `HasWarranty` | `Boolean` | no |  |
| `WarrantyStartDate` | `DateTimeOffset?` | yes |  |
| `WarrantyEndDate` | `DateTimeOffset?` | yes |  |
| `WarrantyMonths` | `Int32` | no |  |
| `OwnerId` | `Int64?` | yes | [Customers](/modules/Sales.md#Sales.Customer) |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `CustomerOrderDeliveryRowId` | `Int64?` | yes | [CustomerOrderDeliveryRows](/modules/Sales.md#Sales.CustomerOrderDeliveryRow) |
| `CustomerOrderDeliveryRow` | `CustomerOrderDeliveryRows` | no | [CustomerOrderDeliveryRows](/modules/Sales.md#Sales.CustomerOrderDeliveryRow) |
| `DeliveryAddressId` | `Int64?` | yes | [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress) |
| `DeliveryAddress` | `Addresses` | no | [Addresses](/modules/Common.md#Common.Address) |
| `BlockMessageId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `BlockMessage` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `LifeCycleState` | `Int32` | no |  |
| `BlockContext` | `Int32` | no |  |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |
| `MeasurementSetting` | `Decimal?` | yes |  |
| `OperationTime` | `TimeSpan?` | yes |  |
| `NumberOfCycles` | `Decimal?` | yes |  |
| `OperationReportings` | `ProductRecordOperationReportings[]` | no | [ProductRecordOperationReportings](/modules/Inventory.md#Inventory.ProductRecordOperationReporting) |
| `CustomerOrderOurReferenceId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference) |
| `CustomerOrderPartRevisionId` | `Int64?` | yes | [Revisions](/modules/Common.md#Common.Revision) |
| `PartRevisionId` | `Int64?` | yes | [Revisions](/modules/Common.md#Common.Revision) |
| `PlannedDeliveryDate` | `DateTimeOffset?` | yes |  |
| `ActualDeliveryDate` | `DateTimeOffset?` | yes |  |
| `MeasurementSettingWarranty` | `Decimal?` | yes |  |
| `OperationTimeWarranty` | `TimeSpan?` | yes |  |
| `NumberOfCyclesWarranty` | `Decimal?` | yes |  |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder) |
| `ActualArrivalDate` | `DateTimeOffset?` | yes |  |
| `ManufactureDate` | `DateTimeOffset?` | yes |  |
| `InstallationOrderId` | `Int64?` | yes | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `InstalledBy` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `InstallationDate` | `DateTimeOffset?` | yes |  |
| `InstallationCode` | `String` | no |  |
| `WarrantyCode` | `String` | no |  |
| `RegistrationNo` | `String` | no |  |
| `TypeDescription` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `BestBeforeDate` | `DateTimeOffset?` | yes |  |
| `ProductRecordBatchId` | `Int64?` | yes |  |

- `ProductRecordType` — ProductRecord=0, Batch=1
- `LifeCycleState` — ApprovalForUse=0, NonApproval=1, ServicePastDue=2, UnderServiceOrCalibration=3, Rejected=4, ServiceOrCalibrationBeforeUse=5, Missing=6, Scrapped=7
- `BlockContext` (bitmask) — None=0, ManufacturingOrderWithdrawal=1, ManufacturingOrderClearance=2, CustomerOrderDelivery=4, CustomerOrderClearance=8, RequirementCalculation=16
- `Status` — NotInitialized=0, Registrered=1, Manufacturing=2, ManufacturingPending=3, Inventory=4, Blocked=5, Packed=6, PackedAndMarked=7, Historical=9

**References out:** [Addresses](/modules/Common.md#Common.Address), [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference), [Comments](/modules/Common.md#Common.Comment), [CustomerOrderDeliveryRows](/modules/Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [Customers](/modules/Sales.md#Sales.Customer), [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress), [ExtraFields](/modules/Common.md#Common.ExtraField), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](/modules/Inventory.md#Inventory.Part), [Persons](/modules/Common.md#Common.Person), [ProductRecordOperationReportings](/modules/Inventory.md#Inventory.ProductRecordOperationReporting), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [Revisions](/modules/Common.md#Common.Revision)
**Referenced by:** [AdditionalIDsRecords](/modules/Inventory.md#Inventory.AdditionalIdsRecord), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CaseEntryPartLinks](/modules/Inventory.md#Inventory.CasePartLink), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [MaintenanceReportingRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingRow), [MaintenanceReportings](/modules/Manufacturing.md#Manufacturing.MaintenanceReporting), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode), [PackageRowPartLocations](/modules/Sales.md#Sales.PackageRowPartLocation), [PartLocationProductRecords](/modules/Inventory.md#Inventory.PartLocationProductRecord), [PhysicalInventoryRows](/modules/Inventory.md#Inventory.PhysicalInventoryRow), [ProductRecordOperationReportings](/modules/Inventory.md#Inventory.ProductRecordOperationReporting), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement), [SalesPickingListRowQuantities](/modules/Sales.md#Sales.SalesPickingListRowQuantity), [StockBalanceChanges](/modules/Inventory.md#Inventory.StockBalanceChange), [StockTransactions](/modules/Inventory.md#Inventory.StockTransaction)

<a id="Inventory.ProfitMarkup"></a>
### ProfitMarkups

Represents profit markup.

- **Endpoint:** `GET /api/v1/Inventory/ProfitMarkups`
- **Required permission:** Show calculation mark-up
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `Markup` | `Decimal` | no |  |

**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part), [PartTemplates](/modules/Inventory.md#Inventory.PartTemplate)

<a id="Inventory.QuantityChange"></a>
### QuantityChanges

Represents a quantity change.

- **Endpoint:** `GET /api/v1/Inventory/QuantityChanges`
- **Required permission:** Show part
- **Introduced in:** 2.48

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ActualDeliveryDate` | `DateTimeOffset` | no |  |
| `PartId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `BalanceChange` | `Decimal` | no |  |
| `AvailableBalance` | `Decimal` | no |  |
| `PickingByUserId` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `PickingByPersonId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `DeliveredByUserId` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `DeliveredByPersonId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `StockBalanceChanges` | `StockBalanceChanges[]` | no | [StockBalanceChanges](/modules/Inventory.md#Inventory.StockBalanceChange) |
| `Status` | `Int32` | no |  |
| `ClearingTimeStamp` | `DateTimeOffset?` | yes |  |
| `PickingTimeStamp` | `DateTimeOffset?` | yes |  |
| `IsOriginalReceivingInspectionQuantity` | `Boolean` | no |  |
| `Price` | `Decimal?` | yes |  |
| `CanceledQuantity` | `Decimal` | no |  |
| `IsExportedToManagementAccounting` | `Boolean` | no |  |
| `CanceledTimestamp` | `DateTimeOffset?` | yes |  |
| `UndoneTimestamp` | `DateTimeOffset?` | yes |  |
| `ReservationId` | `Int64?` | yes |  |

- `Status` — Cleared=1, Picking=2, OutgoingDelivery=3, Adviced=4, ReceivingInspection=5, IncomingDelivery=6, CanceledOutgoingDelivery=7, CanceledIncomingDelivery=8, WithdrawInspection=9, InspectionCompleted=10, InspectionRejection=11

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Parts](/modules/Inventory.md#Inventory.Part), [Persons](/modules/Common.md#Common.Person), [StockBalanceChanges](/modules/Inventory.md#Inventory.StockBalanceChange), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [ManufacturingPickingListMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingPickingListMaterial), [PurchaseOrderDeliveryRowQuantities](/modules/Purchase.md#Purchase.PurchaseOrderDeliveryRowQuantity), [StockBalanceChanges](/modules/Inventory.md#Inventory.StockBalanceChange)

<a id="Inventory.SalesForecastRow"></a>
### SalesForecastRows

Represents a sales forecast row.

- **Endpoint:** `GET /api/v1/Inventory/SalesForecastRows`
- **Required permission:** Show basic data for part
- **Introduced in:** 22.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Quantity` | `Decimal` | no |  |
| `UnitId` | `Int64` | no | [Units](/modules/Common.md#Common.Unit) |
| `DeliveryDate` | `DateTimeOffset` | no |  |
| `SalesForecastId` | `Int64` | no | [SalesForecasts](/modules/Inventory.md#Inventory.SalesForecast) |

**References out:** [Parts](/modules/Inventory.md#Inventory.Part), [SalesForecasts](/modules/Inventory.md#Inventory.SalesForecast), [Units](/modules/Common.md#Common.Unit)
**Referenced by:** [SalesForecasts](/modules/Inventory.md#Inventory.SalesForecast)

<a id="Inventory.SalesForecast"></a>
### SalesForecasts

Represents a sales forecast.

- **Endpoint:** `GET /api/v1/Inventory/SalesForecasts`
- **Required permission:** Show basic data for part
- **Introduced in:** 22.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ForecastCode` | `String` | no |  |
| `Description` | `String` | no |  |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `TimeSpan` | `TimeSpan` | no |  |
| `IsActive` | `Boolean` | no |  |
| `CustomerId` | `Int64?` | yes | [Customers](/modules/Sales.md#Sales.Customer) |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup) |
| `CustomerDistrictId` | `Int64?` | yes | [CustomerDistricts](/modules/Sales.md#Sales.CustomerDistrict) |
| `SalesForecastRows` | `SalesForecastRows[]` | no | [SalesForecastRows](/modules/Inventory.md#Inventory.SalesForecastRow) |

**References out:** [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup), [CustomerDistricts](/modules/Sales.md#Sales.CustomerDistrict), [Customers](/modules/Sales.md#Sales.Customer), [SalesForecastRows](/modules/Inventory.md#Inventory.SalesForecastRow), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [SalesForecastRows](/modules/Inventory.md#Inventory.SalesForecastRow)

<a id="Inventory.SalesOverheadMarkup"></a>
### SalesOverheadMarkups

Represents sales overhead markup.

- **Endpoint:** `GET /api/v1/Inventory/SalesOverheadMarkups`
- **Required permission:** Show calculation mark-up
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `Markup` | `Decimal` | no |  |

**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part), [PartTemplates](/modules/Inventory.md#Inventory.PartTemplate)

<a id="Inventory.StockBalanceChange"></a>
### StockBalanceChanges

Represents a stock balance change.

- **Endpoint:** `GET /api/v1/Inventory/StockBalanceChanges`
- **Required permission:** Show part
- **Introduced in:** 2.48

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartLocationId` | `Int64?` | yes | [PartLocations](/modules/Inventory.md#Inventory.PartLocation) |
| `BalanceChange` | `Decimal` | no |  |
| `AvailableBalance` | `Decimal` | no |  |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `QuantityChangeId` | `Int64` | no | [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange) |

**References out:** [PartLocations](/modules/Inventory.md#Inventory.PartLocation), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange)
**Referenced by:** [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange)

<a id="Inventory.StockTransaction"></a>
### StockTransactions

Represents a stock transaction.

- **Endpoint:** `GET /api/v1/Inventory/StockTransactions`
- **Required permission:** Show basic data for part
- **Introduced in:** 22.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartNumber` | `String` | no |  |
| `PartId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `BalanceChange` | `Decimal` | no |  |
| `BalanceOnPartAfterChange` | `Decimal` | no |  |
| `BalanceOnLocationAfterChange` | `Decimal` | no |  |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  |
| `DeliveryDate` | `DateTimeOffset` | no |  |
| `LocationName` | `String` | no |  |
| `BusinessTransactionId` | `Int64` | no |  |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `PhysicalInventoryListNumber` | `Int64?` | yes |  |
| `PartLocationId` | `Int64?` | yes | [PartLocations](/modules/Inventory.md#Inventory.PartLocation) |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) |
| `BatchNumber` | `String` | no |  |
| `OrderNumber` | `String` | no |  |
| `BusinessTransactionContextType` | `Int32` | no |  |
| `StandardPrice` | `Decimal` | no |  |
| `Price` | `Decimal?` | yes |  |
| `ReportedPrice` | `Decimal` | no |  |
| `Amount` | `Decimal` | no |  |

- `BusinessTransactionContextType` — NotInitialized=0, ArrivalReporting=1, ManufacturingOrderReporting=2, DeliveryReporting=3, PhysicalInventory=4, UnplannedStockWithdrawal=5, MoveBetweenWarehouse=6, MoveStockBalance=7, NonconformityPosteriorRejection=8, DirectlyRegisteredInvoice=9, RemovalOfPartLocation=10, ManufacturingOrderMaterialReporting=11, UnplannedStockArrivalReporting=12, StockImport=13, DeliveryReportingStockOrder=14, ArrivalReportingStockOrder=15, UndoManufacturingOrderMaterialReporting=16, UndoManufacturingOrderReporting=17, UndoArrivalReporting=18, UndoDeliveryReporting=19, UndoArrivalReportingStockOrder=20, UndoDeliveryReportingStockOrder=21, OutgoingReusable=22, ArrivalReusable=23, UndoOutgoingReusable=24, UndoArrivalReusable=25, ToolWithdrawal=26, ToolReturn=27, CreditSupplierInvoice=28, CreditCustomerInvoice=29, ReturnPurchaseOrder=30, SplitInvoiceBasis=31, CreationOfPartLocation=32, ArrivalsCorrection=33, ArrivalRejection=34, UndoReturnPurchaseOrder=35

**References out:** [PartLocations](/modules/Inventory.md#Inventory.PartLocation), [Parts](/modules/Inventory.md#Inventory.Part), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [Warehouses](/modules/Common.md#Common.Warehouse)

<a id="Inventory.StorageOverheadMarkup"></a>
### StorageOverheadMarkups

Represents storage overhead markup.

- **Endpoint:** `GET /api/v1/Inventory/StorageOverheadMarkups`
- **Required permission:** Show calculation mark-up
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `Markup` | `Decimal` | no |  |
| `Type` | `Int32` | no |  |

- `Type` — StorageOverhead=0, SubContract=1, Both=2

**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Inventory.UnplannedStockMovementReasonCode"></a>
### UnplannedStockMovementReasonCodes

Represents a queryable unplanned stock movement reason code.

- **Endpoint:** `GET /api/v1/Inventory/UnplannedStockMovementReasonCodes`
- **Required permission:** Show cause codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `CommentMandatory` | `Boolean` | no |  |
| `Active` | `Boolean` | no |  |



## Depends on other modules

- [Accounting](/modules/Accounting.md): [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable)
- [Common](/modules/Common.md): [Addresses](/modules/Common.md#Common.Address), [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [BlobData](/modules/Common.md#Common.BlobData), [BusinessContactNoteHistories](/modules/Common.md#Common.BusinessContactNoteHistory), [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference), [Comments](/modules/Common.md#Common.Comment), [Countries](/modules/Common.md#Common.Country), [Currencies](/modules/Common.md#Common.Currency), [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress), [Departments](/modules/Common.md#Common.Department), [ExtraFields](/modules/Common.md#Common.ExtraField), [FormReportConfigurations](/modules/Common.md#Common.FormReportConfiguration), [FormTemplates](/modules/Common.md#Common.FormTemplate), [MeasuringTemplates](/modules/Common.md#Common.MeasuringTemplate), [PartConfigurationTemplates](/modules/Common.md#Common.PartConfigurationTemplate), [PartUnitUsages](/modules/Common.md#Common.PartUnitUsage), [PartialQuantities](/modules/Common.md#Common.PartialQuantity), [Persons](/modules/Common.md#Common.Person), [PriceLists](/modules/Common.md#Common.PriceList), [ProductGroups](/modules/Common.md#Common.ProductGroup), [Projects](/modules/Common.md#Common.Project), [RejectionCodeItems](/modules/Common.md#Common.RejectionCodeItem), [Revisions](/modules/Common.md#Common.Revision), [StatisticalGoodsCodes](/modules/Common.md#Common.StatisticalGoodsCode), [TransferProfiles](/modules/Common.md#Common.TransferProfile), [Units](/modules/Common.md#Common.Unit), [VatRates](/modules/Common.md#Common.VatRate), [Warehouses](/modules/Common.md#Common.Warehouse)
- [Manufacturing](/modules/Manufacturing.md): [Drawings](/modules/Manufacturing.md#Manufacturing.Drawing), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [ManufacturingOrderOperationReportings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [Preparations](/modules/Manufacturing.md#Manufacturing.Preparation), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
- [Purchase](/modules/Purchase.md): [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink)
- [Sales](/modules/Sales.md): [Customers](/modules/Sales.md#Sales.Customer), [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup), [CustomerDistricts](/modules/Sales.md#Sales.CustomerDistrict), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [CustomerOrderDeliveryRows](/modules/Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerPartLinks](/modules/Sales.md#Sales.CustomerPartLink)
