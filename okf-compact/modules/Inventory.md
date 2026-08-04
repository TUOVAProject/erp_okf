# Inventory

Monitor API module `Inventory`: 50 queryable entities, 0 commands, 0 payload types.

## Queryable entities

<a id="Inventory.AbcCode"></a>
### AbcCodes

Represents an ABC code.

- **Endpoint:** `GET /api/v1/Inventory/AbcCodes`
- **Required permission:** Show ABC codes
- **Introduced in:** 2.31

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the ABC code. |
| `Code` | `String` | no |  | The human readable identifier (single letter) of the ABC code. |
| `Description` | `String` | no |  | The description of the ABC code. |

**Referenced by:** [PartPlanningInformation](Inventory.md#Inventory.PartPlanningInformation), [PartTemplates](Inventory.md#Inventory.PartTemplate)

<a id="Inventory.AdditionalIdsRecord"></a>
### AdditionalIDsRecords

Represents an addtional ids record.

- **Endpoint:** `GET /api/v1/Inventory/AdditionalIDsRecords`
- **Required permission:** Show serial number
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the additional ids. |
| `ProductRecordId` | `Int64` | no | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the product record that the addtional ids belong to. |
| `Code` | `String` | no |  | Code value of the additional ids. |
| `Code2` | `String` | no |  | Code2 value of the additional ids. |
| `Code3` | `String` | no |  | Code3 value of the additional ids. |
| `Number` | `Int32?` | yes |  | Number value of the additional ids. |
| `Number2` | `Decimal?` | yes |  | Number2 value of the additional ids. |
| `Date` | `DateTimeOffset?` | yes |  | The date of the additional ids. |
| `Weight` | `Decimal?` | yes |  | The weight of the additional ids. |

**References out:** [ProductRecords](Inventory.md#Inventory.ProductRecord)

<a id="Inventory.AlloyQuantity"></a>
### AlloyQuantities

Represents Alloy Quantities of an alloy.

- **Endpoint:** `GET /api/v1/Inventory/AlloyQuantities`
- **Required permission:** Create new alloy codes
- **Introduced in:** 25.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the alloy quantity. |
| `AlloyId` | `Int64` | no | [Alloys](Inventory.md#Inventory.Alloy) | The business key identifier of the alloy quantity. |
| `Quantity` | `Decimal` | no |  | The quantity of the alloy. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the alloy part. |

**References out:** [Alloys](Inventory.md#Inventory.Alloy), [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.Alloy"></a>
### Alloys

Represents an alloy.

- **Endpoint:** `GET /api/v1/Inventory/Alloys`
- **Required permission:** Show alloy codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the alloy. |
| `Code` | `String` | no |  | The human readable identifier of the alloy. |
| `Description` | `String` | no |  | The translated description of the alloy. |
| `Price` | `Decimal` | no |  | The price of the alloy. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency that the alloy price is specified in. |
| `UnitId` | `Int64` | no | [Units](Common.md#Common.Unit) | The business key identifier of the alloy unit. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the alloy part. |

**References out:** [Currencies](Common.md#Common.Currency), [Parts](Inventory.md#Inventory.Part), [Units](Common.md#Common.Unit)
**Referenced by:** [AlloyQuantities](Inventory.md#Inventory.AlloyQuantity), [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.CaseEntry"></a>
### CaseEntry

Represents a case entry.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntry`
- **Required permission:** Show case
- **Introduced in:** 2.22

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case entry. |
| `Number` | `String` | no |  | The human readable identifier of the case entry. |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of the project that belongs to the case entry. |
| `Project` | `Projects` | no | [Projects](Common.md#Common.Project) | The project that belongs to the case entry |
| `ContactCaseNumber` | `String` | no |  | The customer's or the supplier's case number (depending on case type) |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order that is linked to the case entry. |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The customer order that is linked to the case entry. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of the purchase order that is linked to the case entry. |
| `PurchaseOrder` | `PurchaseOrders` | no | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The purchase order that is linked to the case entry. |
| `ArrivalDate` | `DateTimeOffset?` | yes |  | Date when delivery arrived. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  | Date when delivery was made. |
| `DeliveredQuantity` | `Decimal?` | yes |  | The quantity the delivery consisted of. |
| `ArrivedQuantity` | `Decimal?` | yes |  | The quantity the arrival consisted of. |
| `ReasonSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier that caused the nonconformity. References Suppliers . |
| `ReasonWorkCenterId` | `Int64?` | yes | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier of the work center that caused the nonconformity. References WorkCenters . |
| `ReasonDepartmentId` | `Int64?` | yes | [Departments](Common.md#Common.Department) | The business key identifier of the department that caused the nonconformity. References Departments . |
| `ReasonRejectionCodeId` | `Int64?` | yes | [RejectionCodeItems](Common.md#Common.RejectionCodeItem) | The business key identifier of the rejection that caused the nonconformity. |
| `ReasonPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that caused the nonconformity. |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the case internal comment. |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the case. |
| `ReasonCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the reason comment. |
| `ReasonComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The reason comment of the case. |
| `ActualRejectionCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the actual rejections description. |
| `ActualRejectionComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The actual rejections description. |
| `Status` | `Int32` | no |  | The status of the case. |
| `CaseTypeId` | `Int64` | no | [CaseManagementType](Inventory.md#Inventory.CaseManagementType) | The business key identifier of the case management type. |
| `CaseType` | `CaseManagementType` | no | [CaseManagementType](Inventory.md#Inventory.CaseManagementType) | The case management type of the case. |
| `CaseDate` | `DateTimeOffset` | no |  | The case date of the case. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse where the case is registered. |
| `Warehouse` | `Warehouses` | no | [Warehouses](Common.md#Common.Warehouse) | The warehouse of the case. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the used product record for the case. |
| `ProductRecord` | `ProductRecords` | no | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The product record of the case. |
| `PartRevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the part revision used for the case. |
| `PartRevision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) | The part revision of the case. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the used part for the case. |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The part of the case. |
| `ManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) | The business key identifier of the manufacturing order. |
| `ManufacturingOrder` | `ManufacturingOrders` | no | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) | The manufacturing order of the case. |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier. |
| `ActualRejectionCodeId` | `Int64?` | yes | [RejectionCodeItems](Common.md#Common.RejectionCodeItem) | The business key identifier of the actual rejection code for the case. |
| `ActualRejectionCode` | `RejectionCodeItems` | no | [RejectionCodeItems](Common.md#Common.RejectionCodeItem) | The actual rejection code for the case. |
| `RejectionCodeItemId` | `Int64` | no | [RejectionCodeItems](Common.md#Common.RejectionCodeItem) | The business key identifier of the planned rejection code item for the case. |
| `RejectionCodeItem` | `RejectionCodeItems` | no | [RejectionCodeItems](Common.md#Common.RejectionCodeItem) | The rejection code item of the case. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) | A collection of extra field values for the case. |
| `Costs` | `CaseEntryAdditionalCost[]` | no | [CaseEntryAdditionalCost](Inventory.md#Inventory.CaseEntryAdditionalCost) | A collection of case entry additional cost values for the case. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of our reference for the case entry. Reference Persons |
| `OurReferenceName` | `String` | no |  | The name of our reference for the case entry. |
| `Phases` | `CaseEntryPhases[]` | no | [CaseEntryPhases](Inventory.md#Inventory.CaseEntryPhase) | The phases that belong to the case entry |
| `RejectionDescription` | `String` | no |  | The rejection description of the case entry. |
| `Notes` | `BusinessContactNoteHistories[]` | no | [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory) | Rows of business contact notes. |
| `ContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of business contact reference. |
| `ContactName` | `String` | no |  | The customer's or supplier's reference name. Only set when ContactReferenceId is not set. |
| `AccountReciveableId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) | The business key identifier of the accounts receiveable. |
| `AccountsReceivable` | `AccountsReceivables` | no | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) | The accounts receiveable that is linked on the case entry |
| `CategoryString` | `String` | no |  | Category string. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the case entry external comment. |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The case entry external comment. |
| `RejectedQuantity` | `Decimal` | no |  | The case entry rejected quantity. |
| `CasePartLinks` | `CaseEntryPartLinks[]` | no | [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink) | Case part links that reference the parts included in this case. |

- `Status` — Registered=1, Printed=2, Started=3, Finished=4, History=9, Rejected=99

**References out:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [CaseEntryAdditionalCost](Inventory.md#Inventory.CaseEntryAdditionalCost), [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink), [CaseEntryPhases](Inventory.md#Inventory.CaseEntryPhase), [CaseManagementType](Inventory.md#Inventory.CaseManagementType), [Comments](Common.md#Common.Comment), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [Departments](Common.md#Common.Department), [ExtraFields](Common.md#Common.ExtraField), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](Inventory.md#Inventory.Part), [Persons](Common.md#Common.Person), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Projects](Common.md#Common.Project), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [RejectionCodeItems](Common.md#Common.RejectionCodeItem), [Revisions](Common.md#Common.Revision), [Suppliers](Purchase.md#Purchase.Supplier), [Warehouses](Common.md#Common.Warehouse), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [CaseEntryActivities](Inventory.md#Inventory.CaseEntryActivity), [CaseEntryAdditionalCost](Inventory.md#Inventory.CaseEntryAdditionalCost), [CaseEntryLinks](Inventory.md#Inventory.CaseEntryLink), [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink), [CaseEntryPhases](Inventory.md#Inventory.CaseEntryPhase), [Customers](Sales.md#Sales.Customer), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Inventory.CaseEntryActivity"></a>
### CaseEntryActivities

Represents a case entry activity.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntryActivities`
- **Required permission:** Show case
- **Introduced in:** 2.45

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the activity. |
| `CaseEntryId` | `Int64` | no | [CaseEntry](Inventory.md#Inventory.CaseEntry) | The business key identifier of the case entry that the activity belongs to. |
| `PlannedTime` | `TimeSpan` | no |  | The planned time of the activity. |
| `ReportedTime` | `TimeSpan?` | yes |  | The reported time of the activity. |
| `ShowOnDocuments` | `Boolean` | no |  | Specifies if the activity should be shown on documents or not. |
| `ReportingType` | `Int32` | no |  | The reporting type specified for the activity. |
| `Mandatory` | `Boolean` | no |  | Specifies whether or not the activity is mandatory. |
| `CostPerHour` | `Decimal?` | yes |  | The cost per hour of the activity. |
| `CostPerHourCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency that the cost per hour is specified in. |
| `Chargeable` | `Boolean` | no |  | Specifies whether or not the activity is chargeable. |
| `ActivityTypeId` | `Int64` | no | [CaseManagementActivities](Inventory.md#Inventory.CaseManagementActivity) | The business key identifier of the case management activity that the activity is based on. |
| `CalendarAppointmentId` | `String` | no |  | The calendar appointment id of the activity. |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the user that completed the activity. |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the user that is responsible for the activity. |
| `Description` | `String` | no |  | The description of the activity. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the activity's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The activity's comment. |
| `Status` | `Int32` | no |  | The status of the activity. |
| `ReminderId` | `Int64?` | yes |  | The business key identifier of the reminder that is linked with the activity. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  | The planned completion date of the activity. |
| `CompletionDate` | `DateTimeOffset?` | yes |  | The completion date of the activity. |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  | The planned start date of the activity. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  | The actual start date of the activity. |

- `ReportingType` — Manual=0, Automatic=1
- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseManagementActivities](Inventory.md#Inventory.CaseManagementActivity), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency)
**Referenced by:** [CaseEntryPhases](Inventory.md#Inventory.CaseEntryPhase)

<a id="Inventory.CaseEntryAdditionalCost"></a>
### CaseEntryAdditionalCost

Represents a case entry additional cost.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntryAdditionalCost`
- **Required permission:** Show basic data for case
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case entry additional cost. |
| `CaseEntryId` | `Int64` | no | [CaseEntry](Inventory.md#Inventory.CaseEntry) | The business key identifier of the case entry. |
| `CaseManagementCostId` | `Int64` | no | [CaseManagementCost](Inventory.md#Inventory.CaseManagementCost) | The business key identifier of the case management cost for the case entry additional cost. |
| `CaseManagementCost` | `CaseManagementCost` | no | [CaseManagementCost](Inventory.md#Inventory.CaseManagementCost) | The case management cost of the case entry additional cost. |
| `Cost` | `Decimal` | no |  | The cost of the case entry additional cost. |
| `CostCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the case entry additional cost currency. |
| `CostType` | `Int32` | no |  | The cost type of the case additional cost. |
| `Chargeable` | `Boolean` | no |  | Specifies if the case additional cost is chargeable. |
| `CostPerEach` | `Decimal?` | yes |  | The cost per unit of the case entry additional. |
| `Quantity` | `Decimal?` | yes |  | The quantity of the case entry additional cost. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part for the case entry additional cost. |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The part of the case entry additional cost. |

- `CostType` — Planned=0, Actual=1

**References out:** [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseManagementCost](Inventory.md#Inventory.CaseManagementCost), [Currencies](Common.md#Common.Currency), [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [CaseEntry](Inventory.md#Inventory.CaseEntry)

<a id="Inventory.CaseEntryLink"></a>
### CaseEntryLinks

Represents a case link.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntryLinks`
- **Required permission:** Show case
- **Introduced in:** 25.1

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case link. |
| `ParentId` | `Int64` | no | [CaseEntry](Inventory.md#Inventory.CaseEntry) | The business key identifier of the parent case entry of this case link. |
| `ChildId` | `Int64` | no | [CaseEntry](Inventory.md#Inventory.CaseEntry) | The business key identifier of the child case entry of this case link. |

**References out:** [CaseEntry](Inventory.md#Inventory.CaseEntry)

<a id="Inventory.CasePartLink"></a>
### CaseEntryPartLinks

Represents a case part link.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntryPartLinks`
- **Required permission:** Show case
- **Introduced in:** 24.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case part link. |
| `CaseId` | `Int64` | no | [CaseEntry](Inventory.md#Inventory.CaseEntry) | The business key identifier of the case entry this case part link belongs to. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the referenced part. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the referenced product record. |
| `IsDefault` | `Boolean` | no |  | Defines if the part is considered default part on this case. Can only be set on one part in a case. |
| `PartRevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the revision on part. |
| `RejectionCodeItemId` | `Int64` | no | [RejectionCodeItems](Common.md#Common.RejectionCodeItem) | The business key identifier of the rejection code for this case part link. |
| `RejectedQuantity` | `Decimal` | no |  | Quantity rejected for this case part link. |
| `RejectionDescription` | `String` | no |  | The rejection description for this case part link. |
| `ProductRecordBatchId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the referenced product record batch. |
| `CompensationCustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of compensation customer order for this part case link. |
| `CompensationAccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) | The business key identifier of compensation accounts receivable for this part case link. |
| `CompensationPurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of compensation purchase order for this part case link. |
| `CompensationAccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of compensation accounts payable for this part case link. |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Parts](Inventory.md#Inventory.Part), [ProductRecords](Inventory.md#Inventory.ProductRecord), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [RejectionCodeItems](Common.md#Common.RejectionCodeItem), [Revisions](Common.md#Common.Revision)
**Referenced by:** [CaseEntry](Inventory.md#Inventory.CaseEntry)

<a id="Inventory.CaseEntryPhase"></a>
### CaseEntryPhases

Represents a case entry phase.

- **Endpoint:** `GET /api/v1/Inventory/CaseEntryPhases`
- **Required permission:** Show case
- **Introduced in:** 2.45

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the phase. |
| `CaseManagementPhaseId` | `Int64` | no |  | The business key identifier of the case management phase that the phase is based on. |
| `CaseManagementPhase` | `CaseManagementPhases` | no | [CaseManagementPhases](Inventory.md#Inventory.CaseManagementPhase) | The case management phase that the phase is based on. |
| `Description` | `String` | no |  | The description of the phase. |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that is responsible for the phase. |
| `ParentId` | `Int64` | no | [CaseEntry](Inventory.md#Inventory.CaseEntry) | The business key identifier of the parent of the phase. |
| `RowIndex` | `Int32` | no |  | Determines where the phase is placed in relation to the other phases belonging to the same parent. |
| `Activities` | `CaseEntryActivities[]` | no | [CaseEntryActivities](Inventory.md#Inventory.CaseEntryActivity) | The activities that are linked to the phase. |

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseEntryActivities](Inventory.md#Inventory.CaseEntryActivity), [CaseManagementPhases](Inventory.md#Inventory.CaseManagementPhase)
**Referenced by:** [CaseEntry](Inventory.md#Inventory.CaseEntry)

<a id="Inventory.CaseManagementActivity"></a>
### CaseManagementActivities

Represents a case management activity.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementActivities`
- **Required permission:** Show case
- **Introduced in:** 2.45

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case management activity. |
| `PlannedTime` | `TimeSpan` | no |  | The planned time of the case management activity. |
| `CostPerHour` | `Decimal` | no |  | The cost per hour of the case management activity. |
| `CostPerHourCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency that applies to the cost per hour of the case management activity. |
| `Chargeable` | `Boolean` | no |  | Specifies if the case management activity is chargeable or not. |
| `Code` | `Int64` | no |  | The human readable identifier of the case management activity. |
| `Description` | `String` | no |  | The description of the case management activity. |

**References out:** [Currencies](Common.md#Common.Currency)
**Referenced by:** [CaseEntryActivities](Inventory.md#Inventory.CaseEntryActivity), [CaseManagementTemplateNodes](Inventory.md#Inventory.CaseManagementTemplateNode)

<a id="Inventory.CaseManagementCost"></a>
### CaseManagementCost

Represents a case management cost.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementCost`
- **Required permission:** Show basic data for case
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case management cost. |
| `Number` | `Int32` | no |  | The human readable identifier of the case management cost. |
| `Description` | `String` | no |  | The translated description of the case management cost. |
| `Cost` | `Decimal` | no |  | The cost of the case management. |
| `CostCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the case management cost currency. |
| `Chargeable` | `Boolean` | no |  | Specifies if the case management cost is chargeable. |

**References out:** [Currencies](Common.md#Common.Currency)
**Referenced by:** [CaseEntryAdditionalCost](Inventory.md#Inventory.CaseEntryAdditionalCost), [CaseManagementTemplateCosts](Inventory.md#Inventory.CaseManagementTemplateCost)

<a id="Inventory.CaseManagementPhase"></a>
### CaseManagementPhases

Represents a case management phase.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementPhases`
- **Required permission:** Show case
- **Introduced in:** 2.45

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case management phase. |
| `Number` | `Int32` | no |  | The human readable identifier of the case management phase. |
| `Description` | `String` | no |  | The description of the case management phase. |

**Referenced by:** [CaseEntryPhases](Inventory.md#Inventory.CaseEntryPhase), [CaseManagementTemplateNodes](Inventory.md#Inventory.CaseManagementTemplateNode)

<a id="Inventory.CaseManagementTemplateCost"></a>
### CaseManagementTemplateCosts

Represents a case management template cost.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementTemplateCosts`
- **Required permission:** Show basic data for case
- **Introduced in:** 23.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case management template cost. |
| `Description` | `String` | no |  | The description of the case management template cost. |
| `Cost` | `Decimal` | no |  | The cost of the case management template cost. |
| `CostCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the case management template cost currency. |
| `CostId` | `Int64?` | yes | [CaseManagementCost](Inventory.md#Inventory.CaseManagementCost) | The business key identifier of the case management cost. |
| `ParentId` | `Int64?` | yes | [CaseManagementTemplates](Inventory.md#Inventory.CaseManagementTemplate) | The business key identifier of the case management template. |
| `IsChargeable` | `Boolean` | no |  | Specifies if the case management template cost is chargeable. |
| `RowIndex` | `Int32?` | yes |  | The row index of the case management template cost. |

**References out:** [CaseManagementCost](Inventory.md#Inventory.CaseManagementCost), [CaseManagementTemplates](Inventory.md#Inventory.CaseManagementTemplate), [Currencies](Common.md#Common.Currency)
**Referenced by:** [CaseManagementTemplates](Inventory.md#Inventory.CaseManagementTemplate)

<a id="Inventory.CaseManagementTemplateNode"></a>
### CaseManagementTemplateNodes

Represents a case management template node.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementTemplateNodes`
- **Required permission:** Show basic data for case
- **Introduced in:** 23.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case management template node. |
| `ActivityId` | `Int64?` | yes | [CaseManagementActivities](Inventory.md#Inventory.CaseManagementActivity) | The business key identifier of the case management activity. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the case management template node comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the case management template node. |
| `PlannedTime` | `TimeSpan?` | yes |  | The planned time of the case management template node. |
| `LeadTime` | `Int32?` | yes |  | The lead time of the case management template node in work days. |
| `Status` | `Int32` | no |  | The status for the case management template node. |
| `IsReminder` | `Boolean` | no |  | Whether or not to create a reminder for the case management template node. |
| `IsMandatory` | `Boolean` | no |  | Specifies if the case management template node is mandatory. |
| `IsIncludeActivityOnDocument` | `Boolean` | no |  | Whether or not to include activity on document for the case management template node. |
| `IsChargeable` | `Boolean` | no |  | Specifies if the case management template node is chargeable. |
| `UserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier for the application user of the case management template node. |
| `PhaseId` | `Int64?` | yes | [CaseManagementPhases](Inventory.md#Inventory.CaseManagementPhase) | The business key identifier for the case management phase of the case management template node. |
| `ParentId` | `Int64?` | yes | [CaseManagementTemplates](Inventory.md#Inventory.CaseManagementTemplate) | The business key identifier of the case management template. |
| `ParentNodeId` | `Int64?` | yes |  | The business key identifier of the case management template node's parent that the case management template node belongs to. |
| `RowIndex` | `Int32?` | yes |  | The row index of the case management template node. |

- `Status` — NotStarted=0, Started=1

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [CaseManagementActivities](Inventory.md#Inventory.CaseManagementActivity), [CaseManagementPhases](Inventory.md#Inventory.CaseManagementPhase), [CaseManagementTemplates](Inventory.md#Inventory.CaseManagementTemplate), [Comments](Common.md#Common.Comment)
**Referenced by:** [CaseManagementTemplates](Inventory.md#Inventory.CaseManagementTemplate)

<a id="Inventory.CaseManagementTemplate"></a>
### CaseManagementTemplates

Represents a case management template.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementTemplates`
- **Required permission:** Show basic data for case
- **Introduced in:** 23.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case management template. |
| `Number` | `Int32` | no |  | The human readable identifier of the case management template. |
| `Description` | `String` | no |  | The description of the case management template. |
| `IsDefault` | `Boolean` | no |  | Specifies if the case management template is default. |
| `CaseManagementTypeId` | `Int64?` | yes | [CaseManagementType](Inventory.md#Inventory.CaseManagementType) | The business key identifier of the case management type. |
| `CaseManagementTemplateNode` | `CaseManagementTemplateNodes[]` | no | [CaseManagementTemplateNodes](Inventory.md#Inventory.CaseManagementTemplateNode) | The case management template node of the case management template. |
| `CaseManagementTemplateCost` | `CaseManagementTemplateCosts[]` | no | [CaseManagementTemplateCosts](Inventory.md#Inventory.CaseManagementTemplateCost) | The case management template cost of the case management template. |

**References out:** [CaseManagementTemplateCosts](Inventory.md#Inventory.CaseManagementTemplateCost), [CaseManagementTemplateNodes](Inventory.md#Inventory.CaseManagementTemplateNode), [CaseManagementType](Inventory.md#Inventory.CaseManagementType)
**Referenced by:** [CaseManagementTemplateCosts](Inventory.md#Inventory.CaseManagementTemplateCost), [CaseManagementTemplateNodes](Inventory.md#Inventory.CaseManagementTemplateNode)

<a id="Inventory.CaseManagementType"></a>
### CaseManagementType

Represents a case management type.

- **Endpoint:** `GET /api/v1/Inventory/CaseManagementType`
- **Required permission:** Show basic data for case
- **Introduced in:** 2.22

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the case management type. |
| `Description` | `String` | no |  | The description of the case management type. |
| `IsPreset` | `Boolean` | no |  | Specifies if the case management type is preset. |
| `Number` | `Int64` | no |  | The human readable identifier of the case management type. |
| `Prefix` | `String` | no |  | The prefix of the case management type. |
| `Priority` | `Int32` | no |  | The priority of the case management type. |
| `Visible` | `Boolean` | no |  | Specifies if the case management type is visible. |
| `Type` | `Int32` | no |  | The base type of the case management type. |

- `Type` — CustomerNonconformity=1, SupplierNonconformity=2, InternalNonconformity=3, Standard8D=4

**Referenced by:** [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseManagementTemplates](Inventory.md#Inventory.CaseManagementTemplate)

<a id="Inventory.GoodsType"></a>
### GoodsTypes

Represents a goods type.

- **Endpoint:** `GET /api/v1/Inventory/GoodsTypes`
- **Required permission:** Show package type/goods type
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the goods type. |
| `Number` | `Int64` | no |  | The human readable identifier of the goods type. |
| `Description` | `String` | no |  | The translated description of the goods type. |
| `IsActive` | `Boolean` | no |  | Specifies if the goods type is active in the system. |

**Referenced by:** [CustomerOrderShippingInformationRows](Sales.md#Sales.CustomerOrderShippingInformationRow), [Parts](Inventory.md#Inventory.Part), [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation)

<a id="Inventory.HyperLink"></a>
### HyperLinks

Represents a part hyperlink.

- **Endpoint:** `GET /api/v1/Inventory/HyperLinks`
- **Required permission:** Show part
- **Introduced in:** 2.55

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the hyperlink. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the hyperlink belongs to. |
| `Link` | `String` | no |  | The link (url) of the hyperlink. |
| `Description` | `String` | no |  | The description of the hyperlink. |

**References out:** [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.Location"></a>
### Locations

Represents a location (so called generated location) Can also represent a stock package)

- **Endpoint:** `GET /api/v1/Inventory/Locations`
- **Required permission:** Show locations
- **Introduced in:** 24.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the location. |
| `ParentId` | `Int64?` | yes | [Locations](Inventory.md#Inventory.Location) | The business key identifier of the location's parent location. Applicable for locations that represents a stock package. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse where the location is located. |
| `Warehouse` | `Warehouses` | no | [Warehouses](Common.md#Common.Warehouse) | The warehouse of the location. |
| `Name` | `String` | no |  | The name of the location or the package number. |
| `StorageType` | `Int32` | no |  | The type of the location. (Single- or multipart storage) |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the comment |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the location. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that blocked the entity. |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The application user that blocked the location. |
| `BlockedStatus` | `Int32` | no |  | The block status of the entity. |
| `BlockMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) | The block message of the location. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  | The date when the entity stops being blocked. |
| `SortingOrder` | `Int64?` | yes |  | The route sorting order. |
| `IsPackage` | `Boolean` | no |  | Whether this location represents a stock package |
| `MaxWidth` | `Decimal?` | yes |  | The max width of the location. |
| `MinWidth` | `Decimal?` | yes |  | The min width of the location. |
| `MaxLength` | `Decimal?` | yes |  | The max length of the location. |
| `MinLength` | `Decimal?` | yes |  | The min length of the location. |
| `MaxHeight` | `Decimal?` | yes |  | The max height of the location. |
| `MinHeight` | `Decimal?` | yes |  | The min height of the location. |
| `LoadCapacity` | `Decimal?` | yes |  | The max weight load capacity of the location. |
| `PackagingPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the packaging part that defines the packaging type of this location. Applicable for locations that represents a stock package. |
| `PackagingPart` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The packaging part that defines the packaging type of this location. Applicable for locations that represents a stock package. |
| `ManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) | The business key identifier of the manufacturing order that the package were created for. Applicable for locations that represents a stock package. |
| `ManufacturingOrderMaterialId` | `Int64?` | yes | [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting) | The business key identifier of the reported material that is linked to the package. Applicable for locations that represents a stock package. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of the purchase order that the package were created for. Applicable for locations that represents a stock package. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order that the package were created for. Applicable for locations that represents a stock package. |
| `Rfid` | `String` | no |  | The RFID of the package. Applicable for locations that represents a stock package. |

- `StorageType` — SinglePartStorage=0, MultiplePartStorage=1
- `BlockedStatus` — None=0, Message=1, Blocked=2

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Comments](Common.md#Common.Comment), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Locations](Inventory.md#Inventory.Location), [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](Inventory.md#Inventory.Part), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [Locations](Inventory.md#Inventory.Location)

<a id="Inventory.OrderQuantityTemplate"></a>
### OrderQuantityTemplates

Represents a order quantity template on part that holds many partial quantities.

- **Endpoint:** `GET /api/v1/Inventory/OrderQuantityTemplates`
- **Required permission:** Show part
- **Introduced in:** 22.6

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](Common.md#Common.PartialQuantity) | The partial quantities for the order quantity. |

**References out:** [PartialQuantities](Common.md#Common.PartialQuantity)
**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.PackageType"></a>
### PackageTypes

Represents a package type.

- **Endpoint:** `GET /api/v1/Inventory/PackageTypes`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the package type. |
| `Number` | `Int64` | no |  | The human readable identifier of the package type. |
| `IsActive` | `Boolean` | no |  | Specifies if the package type is active in the system. |
| `Description` | `String` | no |  | The translated description of the package type. |
| `DefaultCode` | `String` | no |  | The default code of the package type. |

**Referenced by:** [CustomerOrderShippingInformationRows](Sales.md#Sales.CustomerOrderShippingInformationRow), [Parts](Inventory.md#Inventory.Part), [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation)

<a id="Inventory.PartActivity"></a>
### PartActivities

Represents an part activity.

- **Endpoint:** `GET /api/v1/Inventory/PartActivities`
- **Required permission:** Show part
- **Introduced in:** 22.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part activity. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the activity belongs to. |
| `ActivityTypeId` | `Int64` | no | [PartActivityTypes](Inventory.md#Inventory.PartActivityType) | The business key identifier of the part activity type. |
| `Description` | `String` | no |  | The description of the activity. |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the user that is responsible for the activity. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the activity's comment. |
| `ReminderId` | `Int64` | no |  | The business key identifier of the reminder that is linked with the activity. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  | The planned completion date of the activity. |
| `Status` | `Int32` | no |  | The status of the the activity. |

- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Comments](Common.md#Common.Comment), [PartActivityTypes](Inventory.md#Inventory.PartActivityType), [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.PartActivityType"></a>
### PartActivityTypes

Represents an part activity type.

- **Endpoint:** `GET /api/v1/Inventory/PartActivityTypes`
- **Required permission:** Show basic data for part
- **Introduced in:** 22.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part activity type. |
| `Code` | `Int64` | no |  | he human readable identifier of the activity type. |
| `Description` | `String` | no |  | The description of the activity type. |

**Referenced by:** [PartActivities](Inventory.md#Inventory.PartActivity)

<a id="Inventory.PartCode"></a>
### PartCodes

Represents a part code.

- **Endpoint:** `GET /api/v1/Inventory/PartCodes`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part code. |
| `Code` | `String` | no |  | The human readable identifier of the part code. |
| `Description` | `String` | no |  | The translated description of the part code. |
| `Alias` | `String` | no |  | The human readable alias code of the part code. |

**Referenced by:** [DiscountCategoryRows](Common.md#Common.DiscountCategoryRow), [Parts](Inventory.md#Inventory.Part), [PartTemplates](Inventory.md#Inventory.PartTemplate)

<a id="Inventory.PartDefaultTransportLabel"></a>
### PartDefaultTransportLabels

Represents a part's default transport label.

- **Endpoint:** `GET /api/v1/Inventory/PartDefaultTransportLabels`
- **Required permission:** Show part
- **Introduced in:** 23.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the default transport label. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part to which the transport label is set as default for. |
| `FormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](Common.md#Common.FormReportConfiguration) | The business key identifier of the transport label's form report configuration. |
| `Type` | `Int32` | no |  | The transport label's type. |
| `FormReportTypeId` | `Guid` | no |  | The form report type id of the transport label. |

- `Type` — NodeToStock=0, Rejection=1, OperationInProgress=2, OperationBeforeReporting=3, Subcontract=4, SalesTransportLabel=5, PurchaseTransportLabel=6, PurchaseRejectionTransportLabel=7, PurchaseReturnOrderTransportLabel=8

**References out:** [FormReportConfigurations](Common.md#Common.FormReportConfiguration), [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.PartIdentityType"></a>
### PartIdentityTypes

Represents a part identity type.

- **Endpoint:** `GET /api/v1/Inventory/PartIdentityTypes`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.47

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part identity type. |
| `Code` | `String` | no |  | The human readable identifier of the part identity type. |
| `Description` | `String` | no |  | The translated description of the part identity type. |
| `IsActive` | `Boolean` | no |  | Specifies whether or not the part identity type is active. |
| `Type` | `Int32?` | yes |  | The type of code that the part identity type defines. |

- `Type` — None=0, GTIN8=1, GTIN12=2, GTIN13=3, GTIN14=4, SGTIN=5

**Referenced by:** [PartOtherIdentities](Inventory.md#Inventory.PartOtherIdentity)

<a id="Inventory.PartImage"></a>
### PartImages

Represents a part image.

- **Endpoint:** `GET /api/v1/Inventory/PartImages`
- **Required permission:** Show part
- **Introduced in:** 25.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part image. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the image belongs to. |
| `PhotoThumbnailId` | `Int64` | no | [BlobData](Common.md#Common.BlobData) | The business key identifier of entity downscaled thumbnail blob data. |
| `PhotoThumbnail` | `BlobData` | no | [BlobData](Common.md#Common.BlobData) | The entity thumbnail blob data |
| `ExternalVisible` | `Boolean` | no |  | Whether the part image should be shown externally. |

**References out:** [BlobData](Common.md#Common.BlobData), [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.PartLocationProductRecord"></a>
### PartLocationProductRecords

Represents a location quantity item where the quantity and possible product record is to be found.

- **Endpoint:** `GET /api/v1/Inventory/PartLocationProductRecords`
- **Required permission:** Show part
- **Introduced in:** 2.29

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the location quantity item. |
| `PartLocationId` | `Int64` | no | [PartLocations](Inventory.md#Inventory.PartLocation) | The business key identifier of the location to which the location quantity item belong. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the product record of the location quantity item. |
| `Quantity` | `Decimal` | no |  | The quantity in standard unit. |

**References out:** [PartLocations](Inventory.md#Inventory.PartLocation), [ProductRecords](Inventory.md#Inventory.ProductRecord)
**Referenced by:** [PartLocations](Inventory.md#Inventory.PartLocation)

<a id="Inventory.PartLocation"></a>
### PartLocations

Represents a part location.

- **Endpoint:** `GET /api/v1/Inventory/PartLocations`
- **Required permission:** Show part
- **Introduced in:** 2.28

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the location. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part to which the location belong. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse where the location is located. |
| `Warehouse` | `Warehouses` | no | [Warehouses](Common.md#Common.Warehouse) | The warehouse of the location. |
| `Name` | `String` | no |  | The name of the location. |
| `Balance` | `Decimal` | no |  | The balance in standard unit. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the location. |
| `LatestArrivalDate` | `DateTimeOffset` | no |  | Latest arrival date for the location. |
| `WorkCenterPickingLocation` | `Boolean` | no |  | Whether the location is a work center picking location. |
| `WorkCenterPickingLocationFillingQuantity` | `Decimal` | no |  | Specifies the filling quantity when the location is a work center picking location. |
| `OutgoingPickLocation` | `Boolean` | no |  | Specifies whether the location is of type pick location. |
| `ArrivalLocation` | `Boolean` | no |  | Specifies whether the location is of type arrival location. |
| `Priority` | `Int32?` | yes |  | Specifies the priority of the location. |
| `OutgoingPickLocationReorderPoint` | `Decimal` | no |  | Specifies the pick location reordering point, quantity used when filling pick location. |
| `BatchNumber` | `String` | no |  | Batch number when part has traceability of type batch. |
| `SerialNumber` | `String` | no |  | Serial number when part has traceability of type serial number. |
| `InventoryStatus` | `Int32` | no |  | The inventory status of the location. |
| `IsOngoingRefill` | `Boolean` | no |  | Specifies if the location is currently being refilled. |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the revision of the location. |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) | The revision of the location. |
| `IgnoredBalance` | `Boolean` | no |  | Specifies if the balance of the location is to be ignored when calculating Net Requirement and CDT. |
| `PartLocationProductRecords` | `PartLocationProductRecords[]` | no | [PartLocationProductRecords](Inventory.md#Inventory.PartLocationProductRecord) | A collection of quantity items that holds the quantity of each batch/serial number. |

- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `InventoryStatus` — None=0, UnderInventory=1, UnderInventoryWithBalanceCheckpoint=2

**References out:** [PartLocationProductRecords](Inventory.md#Inventory.PartLocationProductRecord), [Parts](Inventory.md#Inventory.Part), [Revisions](Common.md#Common.Revision), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [PackageRowPartLocations](Sales.md#Sales.PackageRowPartLocation), [PartLocationProductRecords](Inventory.md#Inventory.PartLocationProductRecord), [Parts](Inventory.md#Inventory.Part), [PhysicalInventoryRows](Inventory.md#Inventory.PhysicalInventoryRow), [SalesPickingListRowQuantities](Sales.md#Sales.SalesPickingListRowQuantity), [StockBalanceChanges](Inventory.md#Inventory.StockBalanceChange), [StockTransactions](Inventory.md#Inventory.StockTransaction), [WithdrawalInformationLocation](Sales.md#Sales.WithdrawalInformationLocation)

<a id="Inventory.PartOtherIdentity"></a>
### PartOtherIdentities

Represents an alternate identity for a part.

- **Endpoint:** `GET /api/v1/Inventory/PartOtherIdentities`
- **Required permission:** Show part
- **Introduced in:** 2.47

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the alternate identity. |
| `TypeId` | `Int64` | no | [PartIdentityTypes](Inventory.md#Inventory.PartIdentityType) | The business key identifier of the identity type of the alternate identity. |
| `Value` | `String` | no |  | The value of the alternate identity. |
| `IsActive` | `Boolean` | no |  | Whether or not the alternate identity is active. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the alternate identity belongs to. |

**References out:** [PartIdentityTypes](Inventory.md#Inventory.PartIdentityType), [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.PartPlanningInformation"></a>
### PartPlanningInformation

Represents part planning information for a warehouse.

- **Endpoint:** `GET /api/v1/Inventory/PartPlanningInformation`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part planning information. |
| `ContactId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the contact person of the part planning information. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the part planning information is defined for. |
| `AbcCodeId` | `Int64?` | yes | [AbcCodes](Inventory.md#Inventory.AbcCode) | The business key identifier of the AbcCode used. |
| `AcquisitionWarehouseId` | `Int64?` | yes | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse to refill from. |
| `Eoq` | `Decimal` | no |  | The economic order quantity. |
| `RoundingBase` | `Decimal` | no |  | The rounding quantity for orders. |
| `SafetyStock` | `Decimal` | no |  | The safety stock for the part . |
| `AnnualVolume` | `Decimal` | no |  | The annual volume for the part. |
| `LeadTime` | `TimeSpan?` | yes |  | The lead time for the part. |
| `MinQuantity` | `Decimal` | no |  | The minimum order quantity (both purchase and manufacturing). |
| `MaxQuantity` | `Decimal` | no |  | The maximum quantity per order when manufacturing. |
| `ReorderPoint` | `Decimal` | no |  | The reorder quantity for the part. |
| `PalletQuantity` | `Decimal` | no |  | The quantity per packet when manufacturing. |
| `AnnualVolumePace` | `Decimal` | no |  | The annual volume, current pace. |
| `EoqPace` | `Decimal` | no |  | Order quantity current pace. |
| `LotSizingRule` | `Int32` | no |  | The lot sizing rule for the part. |
| `LotSizingPeriod` | `TimeSpan` | no |  | The length of the period when using period requirement as lot sizing rule. |
| `AllowOrderCreationFromCustomerOrder` | `Boolean` | no |  | Allow to create orders from customer order (manufacturing order for manufactured parts and purchase orders for purchased parts). |
| `SafetyTime` | `TimeSpan` | no |  | Safety time. |
| `DeductSalesForecast` | `Int32` | no |  | The type of forecast deduction used. |
| `DeductionMethod` | `Int32` | no |  | The method of forecast deduction used. |
| `ActiveSupplierPartLinkId` | `Int64?` | yes | [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink) | The business key identifier of the active supplier part link of the part planning information. |
| `ActiveSupplierPartLink` | `SupplierPartLinks` | no | [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink) | The active supplier part link of the part planning information. |
| `DefaultTransferProfileId` | `Int64?` | yes | [TransferProfiles](Common.md#Common.TransferProfile) | The business key identifier of the default transfer profile. |
| `PlanningMethod` | `Int32` | no |  | The planning method of the part planning information. |

- `LotSizingRule` — LotForLot=1, FixedQuantity=2, PeriodRequirement=3, Bucketpart=4, Linked=5
- `DeductSalesForecast` — None=0, LeadTime=1, Now=2
- `DeductionMethod` — Percent=0, TimeOrder=1, Closest=2, ClosestBefore=3, PeriodicIntervals=4
- `PlanningMethod` — Netting=0, StockRefill=1, Physical=2

**References out:** [AbcCodes](Inventory.md#Inventory.AbcCode), [Persons](Common.md#Common.Person), [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink), [TransferProfiles](Common.md#Common.TransferProfile), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.PartPurchaseControlDataRow"></a>
### PartPurchaseControlDataRows

Represents a purchase measuring plan for a part.

- **Endpoint:** `GET /api/v1/Inventory/PartPurchaseControlDataRows`
- **Required permission:** Show part
- **Introduced in:** 26.6

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the row relates to. |
| `MeasuringTemplateId` | `Int64` | no | [MeasuringTemplates](Common.md#Common.MeasuringTemplate) | The business key identifier of the measuring template that the row relates to. |
| `OverriddenFormTemplateId` | `Int64?` | yes | [FormTemplates](Common.md#Common.FormTemplate) | The business key identifier of the form template specified for this row. |
| `OverriddenFrequencyText` | `String` | no |  | The frequency text specified for this row. |
| `OverriddenIntervalAmount` | `Int32?` | yes |  | The quantity value specified for this row. |
| `OverriddenInterval` | `Int32?` | yes |  | The interval value specified for this row. |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier that the row relates to. |

**References out:** [FormTemplates](Common.md#Common.FormTemplate), [MeasuringTemplates](Common.md#Common.MeasuringTemplate), [Parts](Inventory.md#Inventory.Part), [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.PartPurchaseExpenseValues"></a>
### PartPurchaseExpenseValues

Represents a part purchase expense values entity.

- **Endpoint:** `GET /api/v1/Inventory/PartPurchaseExpenseValues`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.48

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part purchase expense values. |
| `PartId` | `Int64` | no |  | The business key identifier of the part that part purchase expense values belongs to. |
| `Expense1PercentOfPriceValue` | `Decimal` | no |  | Expense1 (default name: Packaging) - percent of price. |
| `Expense1PerEachValue` | `Decimal` | no |  | Expense1 (default name: Packaging) - per each. |
| `Expense2PercentOfPriceValue` | `Decimal` | no |  | Expense2 (default name: Freight) - percent of price. |
| `Expense2PerEachValue` | `Decimal` | no |  | Expense2 (default name: Freight) - per each. |
| `Expense3PercentOfPriceValue` | `Decimal` | no |  | Expense3 (default name: Customs duty) - percent of price. |
| `Expense3PerEachValue` | `Decimal` | no |  | Expense3 (default name: Customs duty) - per each. |
| `CertificatePercentOfPriceValue` | `Decimal` | no |  | Certificate - percent of price. |
| `CertificatePerEachValue` | `Decimal` | no |  | Certificate - per each. |
| `CertificatePerKgValue` | `Decimal` | no |  | Certificate - per kg. |
| `CertificatePerPackageValue` | `Decimal` | no |  | Certificate - per package. |
| `CertificatePerOrderValue` | `Decimal` | no |  | Certificate - per order. |
| `CertificatePerQuantityValue` | `Decimal` | no |  | Certificate - per quantity. |
| `CertificateQuantityValue` | `Decimal` | no |  | Certificate - quantity. |
| `Expense1PerKgValue` | `Decimal` | no |  | Expense1 (default name: Packaging) - per kg. |
| `Expense1PerPackageValue` | `Decimal` | no |  | Expense1 (default name: Packaging) - per package. |
| `Expense1PerOrderValue` | `Decimal` | no |  | Expense1 (default name: Packaging) - per order. |
| `Expense1PerQuantityValue` | `Decimal` | no |  | Expense1 (default name: Packaging) - per quantity. |
| `Expense1QuantityValue` | `Decimal` | no |  | Expense1 (default name: Packaging) - quantity. |
| `Expense2PerKgValue` | `Decimal` | no |  | Expense2 (default name: Freight) - per kg. |
| `Expense2PerPackageValue` | `Decimal` | no |  | Expense2 (default name: Freight) - per package. |
| `Expense2PerOrderValue` | `Decimal` | no |  | Expense2 (default name: Freight) - per order. |
| `Expense2PerQuantityValue` | `Decimal` | no |  | Expense2 (default name: Freight) - per quantity. |
| `Expense2QuantityValue` | `Decimal` | no |  | Expense2 (default name: Freight) - quantity. |
| `Expense3PerKgValue` | `Decimal` | no |  | Expense3 (default name: Customs duty) - per kg. |
| `Expense3PerPackageValue` | `Decimal` | no |  | Expense3 (default name: Customs duty) - per package. |
| `Expense3PerOrderValue` | `Decimal` | no |  | Expense3 (default name: Customs duty) - per order. |
| `Expense3PerQuantityValue` | `Decimal` | no |  | Expense3 (default name: Customs duty) - per quantity. |
| `Expense3QuantityValue` | `Decimal` | no |  | Expense3 (default name: Customs duty) - quantity. |
| `Expense4PercentOfPriceValue` | `Decimal` | no |  | Expense4 (default name: Tooling) - percent of price. |
| `Expense4PerEachValue` | `Decimal` | no |  | Expense4 (default name: Tooling) - per each. |
| `Expense4PerKgValue` | `Decimal` | no |  | Expense4 (default name: Tooling) - per kg. |
| `Expense4PerPackageValue` | `Decimal` | no |  | Expense4 (default name: Tooling) - per package. |
| `Expense4PerOrderValue` | `Decimal` | no |  | Expense4 (default name: Tooling) - per order. |
| `Expense4PerQuantityValue` | `Decimal` | no |  | Expense4 (default name: Tooling) - per quantity. |
| `Expense4QuantityValue` | `Decimal` | no |  | Expense4 (default name: Tooling) - quantity. |
| `Expense5PercentOfPriceValue` | `Decimal` | no |  | Expense5 (default name: Other) - percent of price. |
| `Expense5PerEachValue` | `Decimal` | no |  | Expense5 (default name: Other) - per each. |
| `Expense5PerKgValue` | `Decimal` | no |  | Expense5 (default name: Other) - per kg. |
| `Expense5PerPackageValue` | `Decimal` | no |  | Expense5 (default name: Other) - per package. |
| `Expense5PerOrderValue` | `Decimal` | no |  | Expense5 (default name: Other) - per order. |
| `Expense5PerQuantityValue` | `Decimal` | no |  | Expense5 (default name: Other) - per quantity. |
| `Expense5QuantityValue` | `Decimal` | no |  | Expense5 (default name: Other) - quantity. |

**Referenced by:** [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink)

<a id="Inventory.Part"></a>
### Parts

Represents a part.

- **Endpoint:** `GET /api/v1/Inventory/Parts`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part. |
| `PartNumber` | `String` | no |  | The human readable identifier of the part. |
| `Description` | `String` | no |  | The translated description of the part. |
| `ExtraDescription` | `String` | no |  | The translated extra description of the part. |
| `CompanyId` | `Int64` | no |  | The business key identifier of the company that the part is defined for. |
| `Length` | `Decimal?` | yes |  | The physical length of the part in metres. |
| `Width` | `Decimal?` | yes |  | The physical width of the part in metres. |
| `Height` | `Decimal?` | yes |  | The physical height of the part in metres. |
| `PackagingType` | `Int32` | no |  | The packaging type that the part specifies. |
| `PackageVolumeConsistsOf` | `Int32` | no |  | Specifies how package volume of the part has been specified. |
| `PackageTypeId` | `Int64?` | yes | [PackageTypes](Inventory.md#Inventory.PackageType) | The business key identifier of the package type specified by the part. |
| `PackageType` | `PackageTypes` | no | [PackageTypes](Inventory.md#Inventory.PackageType) | The package type specified by the part. |
| `PartPlanningInformations` | `PartPlanningInformation[]` | no | [PartPlanningInformation](Inventory.md#Inventory.PartPlanningInformation) | A collection of part planning information for the part. |
| `UseRandomLocationStorage` | `Boolean` | no |  | Specifies if the part employs random location storage. |
| `ShowFictiousStructureOnOrderRegistration` | `Boolean` | no |  | Specifies if the part should show its fictitious structure when registering orders. |
| `TraceabilityMode` | `Int32` | no |  | The traceability mode that is employed by the part. |
| `UseBestBeforeDate` | `Boolean` | no |  | Specifies whether or not best before date applies to the part. |
| `DaysToAddToBestBeforeDate` | `Int32?` | yes |  | Days to use when best before date is active. |
| `SuggestBestBeforeDate` | `Int32` | no |  | Specifies whether or not a best before date should be suggested for the part. |
| `ManageStockBalance` | `Boolean` | no |  | Specifies if stock balance management is enabled for the part. |
| `StandardPrice` | `Decimal` | no |  | The standard price of the part. |
| `StandardPriceCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency that the standard price is specified in. |
| `FutureStandardPrice` | `Decimal?` | yes |  | The future standard price of the part. |
| `FutureStandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency that the future standard price is specified in. |
| `PostCalculatedAveragePrice` | `Decimal?` | yes |  | The post calculated average price of the part. |
| `PostCalculatedAveragePriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency that the post calculated average price is specified in. |
| `Type` | `Int32` | no |  | The part type. |
| `ProductGroupId` | `Int64` | no | [ProductGroups](Common.md#Common.ProductGroup) | The business key identifier of the product group that the part belongs to. |
| `ProductGroup` | `ProductGroups` | no | [ProductGroups](Common.md#Common.ProductGroup) | The product group that the part belongs to. |
| `WeightPerUnit` | `Decimal?` | yes |  | The weight of the part per unit in kilograms. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) | The business key identifier of the statistical goods code that the part is organized under. References a StatisticalGoodsCodes |
| `StatisticalGoodsCode` | `StatisticalGoodsCodes` | no | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) | The statistical goods code that the part is organized under. |
| `StatisticalGoodsValue` | `Decimal?` | yes |  | The statistical goods value of the part. |
| `CountryOfOriginId` | `Int64?` | yes | [Countries](Common.md#Common.Country) | The business key identifier of the part's country of origin. |
| `CountryOfOrigin` | `Countries` | no | [Countries](Common.md#Common.Country) | The part's country of origin. |
| `PartCodeId` | `Int64?` | yes | [PartCodes](Inventory.md#Inventory.PartCode) | The business key identifier of the part's part code. |
| `PartCode` | `PartCodes` | no | [PartCodes](Inventory.md#Inventory.PartCode) | The part's part code. |
| `CategoryString` | `String` | no |  | The category of the part. |
| `StorageOverheadMarkupId` | `Int64` | no | [StorageOverheadMarkups](Inventory.md#Inventory.StorageOverheadMarkup) | The business key identifier of the storage overhead markup of the part. |
| `StorageOverheadMarkup` | `StorageOverheadMarkups` | no | [StorageOverheadMarkups](Inventory.md#Inventory.StorageOverheadMarkup) | The storage overhead markup of the part. |
| `SalesOverheadMarkupId` | `Int64` | no | [SalesOverheadMarkups](Inventory.md#Inventory.SalesOverheadMarkup) | The business key identifier of the sales overhead markup of the part. |
| `SalesOverheadMarkup` | `SalesOverheadMarkups` | no | [SalesOverheadMarkups](Inventory.md#Inventory.SalesOverheadMarkup) | The sales overhead markup of the part. |
| `ProfitMarkupId` | `Int64` | no | [ProfitMarkups](Inventory.md#Inventory.ProfitMarkup) | The business key identifier of the part's profit markup. |
| `ProfitMarkup` | `ProfitMarkups` | no | [ProfitMarkups](Inventory.md#Inventory.ProfitMarkup) | The part's profit markup. |
| `VolumePerUnit` | `Decimal?` | yes |  | The volume per unit of the part in cubic metres. |
| `AveragePrice` | `Decimal?` | yes |  | The average price of the part. |
| `AveragePriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency that the part's average price is specified in. |
| `LastPurchasePrice` | `Decimal?` | yes |  | The last purchase price of the part. |
| `LastPurchasePriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the part's last purchase price. |
| `AveragePriceTimestamp` | `DateTimeOffset?` | yes |  | The timestamp of the part's average price. |
| `PurchaseLabelType` | `Int32` | no |  | The type of transport label that is used for the part when purchasing. |
| `CurrentAlloyId` | `Int64?` | yes | [Alloys](Inventory.md#Inventory.Alloy) | The business key identifier of the current part alloy. |
| `CurrentAlloy` | `Alloys` | no | [Alloys](Inventory.md#Inventory.Alloy) | The part's current alloy. |
| `PurchaseQuantityPerPackage` | `Decimal?` | yes |  | The quantity per package of the part when purchasing. |
| `IsPackaging` | `Boolean` | no |  | Specifies if the part is used for packaging. |
| `Status` | `Int32` | no |  | The status of the part. |
| `PurchaseAndManufactureOnProject` | `Int32` | no |  | Specifies if the part is purchased and manufactured on a project. |
| `ServiceType` | `Int32` | no |  | The service type of the part. |
| `QuantityPerPackage` | `Decimal?` | yes |  | The quantity per package of the part. |
| `PackagingWeightPerPackage` | `Decimal?` | yes |  | The packaging weight per package. |
| `PackagingPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the packaging part used for this part. |
| `PackagingPart` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The packaging part used for this part. |
| `LoadingMetersPerUnit` | `Decimal?` | yes |  | The loading metres per unit. |
| `PackingReference` | `String` | no |  | The packing reference of the part. |
| `Gs1Code` | `String` | no |  | The GS1 code of the part. |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) | The business key identifier of the part's VAT rate. |
| `VatRate` | `VatRates` | no | [VatRates](Common.md#Common.VatRate) | The part's VAT rate. |
| `LastSalesPrice` | `Decimal?` | yes |  | The last sales price of the part. |
| `LastSalesPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency that the last sales price was specified in. |
| `TransportCost` | `Decimal?` | yes |  | The transport cost of the part. |
| `SerialNumberGeneration` | `Int32` | no |  | The serial number generation method of the part. |
| `SerialNumberGenerationSource` | `Int32` | no |  | The serial number generation source of the part. |
| `GoodsType` | `String` | no |  | The goods type of the part. |
| `LeadTimeToCustomer` | `TimeSpan?` | yes |  | The lead time to the customer for the part. |
| `QuantityForLeadtimeToCustomer` | `Decimal?` | yes |  | The quantity for the lead time to the customer for the part. |
| `SalesLabelType` | `Int32` | no |  | The type of transport label to use for the part when selling. |
| `DefaultCustomerOrderWarehouseId` | `Int64?` | yes | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the default customer order warehouse to use for the part. |
| `ManufacturingLabelType` | `Int32` | no |  | The type of transport label to use for the part when manufacturing. |
| `PreparerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the person that prepares the part. |
| `Preparer` | `Persons` | no | [Persons](Common.md#Common.Person) | The person that prepares the part. |
| `GoodsTypeId` | `Int64?` | yes | [GoodsTypes](Inventory.md#Inventory.GoodsType) | The business key identifier of the goods type of the part. |
| `ExpGoodsType` | `GoodsTypes` | no | [GoodsTypes](Inventory.md#Inventory.GoodsType) | The goods type of the part. |
| `CalculatedQuantity` | `Decimal` | no |  | The calculated quantity of the part. |
| `Alias` | `String` | no |  | The part alias. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that blocked the entity. |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The application user that blocked the part. |
| `BlockedStatus` | `Int32` | no |  | The block status of the entity. |
| `BlockedContextType` | `Int32` | no |  | Specifies which contexts the block applies for. |
| `BlockMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) | The block message of the part. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  | The date when the entity stops being blocked. |
| `ReceivingInspectionType` | `Int32` | no |  | Specifies when reception inspection of the type occurs. |
| `StandardUnitId` | `Int64` | no | [Units](Common.md#Common.Unit) | The business key identifier of the standard unit of the part. |
| `StandardPartUnitUsageId` | `Int64` | no | [PartUnitUsages](Common.md#Common.PartUnitUsage) | The business key identifier of the standard part unit usage. |
| `StandardPartUnitUsage` | `PartUnitUsages` | no | [PartUnitUsages](Common.md#Common.PartUnitUsage) | The standard part unit usage. |
| `PartUnitUsages` | `PartUnitUsages[]` | no | [PartUnitUsages](Common.md#Common.PartUnitUsage) | A collection of part unit usages for the part. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the part comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The part comment. |
| `ActiveRevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the part's active revision. |
| `ActiveRevision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) | The active revision of the part. |
| `LatestCalculationId` | `Int64?` | yes |  | The business key identifier of the latest part calculation. |
| `ReceivingInstructionId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the receiving instruction of the part. |
| `ReceivingInstruction` | `Comments` | no | [Comments](Common.md#Common.Comment) | The receiving instruction of the part. |
| `PurchaseCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the part's purchase comment. |
| `PurchaseComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The purchase comment of the part. |
| `PickingInstructionId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the part's picking instruction. |
| `PickingInstruction` | `Comments` | no | [Comments](Common.md#Common.Comment) | The picking instruction of the part. |
| `SalesCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the part's sales comment. |
| `SalesComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The sales comment of the part. |
| `ManufacturingCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the part's manufacturing comment. |
| `ManufacturingComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The manufacturing comment of the part. |
| `PreparationId` | `Int64?` | yes | [Preparations](Manufacturing.md#Manufacturing.Preparation) | The business key identifier of the part's preparation. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) | A collection of extra field values for the part. |
| `CustomerPartLinks` | `CustomerPartLinks[]` | no | [CustomerPartLinks](Sales.md#Sales.CustomerPartLink) | A collection of customer part links for the part. |
| `SupplierPartLinks` | `SupplierPartLinks[]` | no | [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink) | A collection of supplier part links for the part. |
| `Revisions` | `Revisions[]` | no | [Revisions](Common.md#Common.Revision) | A collection of revisions that belong to the part. |
| `Drawings` | `Drawings[]` | no | [Drawings](Manufacturing.md#Manufacturing.Drawing) | A collection of drawings that belong to the part. |
| `PartLocations` | `PartLocations[]` | no | [PartLocations](Inventory.md#Inventory.PartLocation) | A collection of locations that belong to the part. |
| `HyperLinks` | `HyperLinks[]` | no | [HyperLinks](Inventory.md#Inventory.HyperLink) | A collection of hyperlinks that belong to the part. |
| `PartActivities` | `PartActivities[]` | no | [PartActivities](Inventory.md#Inventory.PartActivity) | A collection of activities that belong to the part. |
| `ConfigurationTemplateId` | `Int64?` | yes |  | The business key identifier of the part configuration template that the part uses for part configuration. |
| `ConfigurationTemplate` | `PartConfigurationTemplates` | no | [PartConfigurationTemplates](Common.md#Common.PartConfigurationTemplate) | The part configuration template that the part uses for part configuration. |
| `OtherIdentities` | `PartOtherIdentities[]` | no | [PartOtherIdentities](Inventory.md#Inventory.PartOtherIdentity) | The "other" identities of the part. |
| `Notes` | `BusinessContactNoteHistories[]` | no | [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory) | Rows of business contact notes. |
| `ConfigurationSelectionDescription` | `String` | no |  | The selected configuration description of the part. |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityTemplates](Inventory.md#Inventory.OrderQuantityTemplate) | The business key identifier of order quantity. |
| `OrderQuantity` | `OrderQuantityTemplates` | no | [OrderQuantityTemplates](Inventory.md#Inventory.OrderQuantityTemplate) | Order quantity template that holds the partial quantities, that acts as a default for the order equivalent order quantities. |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of the project that the part belongs to. |
| `PartTemplateId` | `Int64?` | yes | [PartTemplates](Inventory.md#Inventory.PartTemplate) | The business key identifier of the part template. |
| `PartTemplate` | `PartTemplates` | no | [PartTemplates](Inventory.md#Inventory.PartTemplate) | A part template information for the part. |
| `IsFixedWeight` | `Boolean` | no |  | Information whether the part has a fixed weight. |
| `MaterialValidationSetting` | `Int32` | no |  | The settings for serial number linked to which operation. |
| `AutomaticReportingMode` | `Int32` | no |  | The automatic reporting mode that the part applies. |
| `EmissionFactorId` | `Int64?` | yes |  | The business key identifier of the material type of the part. |
| `EmissionFactor` | `EmissionFactors` | no |  | The emission factor for the part. |
| `Emissions` | `Decimal?` | yes |  | The emission factor registered for the material type of the part. |
| `ControlDataRows` | `PartPurchaseControlDataRows[]` | no | [PartPurchaseControlDataRows](Inventory.md#Inventory.PartPurchaseControlDataRow) | A collection of purchase control data rows for the part. |

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

**References out:** [Alloys](Inventory.md#Inventory.Alloy), [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory), [Comments](Common.md#Common.Comment), [Countries](Common.md#Common.Country), [Currencies](Common.md#Common.Currency), [CustomerPartLinks](Sales.md#Sales.CustomerPartLink), [Drawings](Manufacturing.md#Manufacturing.Drawing), [ExtraFields](Common.md#Common.ExtraField), [GoodsTypes](Inventory.md#Inventory.GoodsType), [HyperLinks](Inventory.md#Inventory.HyperLink), [OrderQuantityTemplates](Inventory.md#Inventory.OrderQuantityTemplate), [PackageTypes](Inventory.md#Inventory.PackageType), [PartActivities](Inventory.md#Inventory.PartActivity), [PartCodes](Inventory.md#Inventory.PartCode), [PartConfigurationTemplates](Common.md#Common.PartConfigurationTemplate), [PartLocations](Inventory.md#Inventory.PartLocation), [PartOtherIdentities](Inventory.md#Inventory.PartOtherIdentity), [PartPlanningInformation](Inventory.md#Inventory.PartPlanningInformation), [PartPurchaseControlDataRows](Inventory.md#Inventory.PartPurchaseControlDataRow), [Parts](Inventory.md#Inventory.Part), [PartTemplates](Inventory.md#Inventory.PartTemplate), [PartUnitUsages](Common.md#Common.PartUnitUsage), [Persons](Common.md#Common.Person), [Preparations](Manufacturing.md#Manufacturing.Preparation), [ProductGroups](Common.md#Common.ProductGroup), [ProfitMarkups](Inventory.md#Inventory.ProfitMarkup), [Projects](Common.md#Common.Project), [Revisions](Common.md#Common.Revision), [SalesOverheadMarkups](Inventory.md#Inventory.SalesOverheadMarkup), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [StorageOverheadMarkups](Inventory.md#Inventory.StorageOverheadMarkup), [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [AlloyQuantities](Inventory.md#Inventory.AlloyQuantity), [Alloys](Inventory.md#Inventory.Alloy), [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseEntryAdditionalCost](Inventory.md#Inventory.CaseEntryAdditionalCost), [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink), [CustomerOrderPaymentPlanRows](Sales.md#Sales.CustomerOrderPaymentPlanRow), [CustomerOrderRowInflows](Sales.md#Sales.CustomerOrderRowInflow), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerOrderShippingInformationRows](Sales.md#Sales.CustomerOrderShippingInformationRow), [CustomerPartLinks](Sales.md#Sales.CustomerPartLink), [Drawings](Manufacturing.md#Manufacturing.Drawing), [FormTemplateRows](Common.md#Common.FormTemplateRow), [HyperLinks](Inventory.md#Inventory.HyperLink), [InquiryRows](Purchase.md#Purchase.InquiryRow), [InvoiceLogs](Sales.md#Sales.InvoiceLog), [Locations](Inventory.md#Inventory.Location), [MaintenanceReportingRows](Manufacturing.md#Manufacturing.MaintenanceReportingRow), [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [PackageRows](Sales.md#Sales.PackageRow), [PartActivities](Inventory.md#Inventory.PartActivity), [PartConfigurationResults](Common.md#Common.PartConfigurationResult), [PartConfigurationSelectionGroupResults](Common.md#Common.PartConfigurationSelectionGroupResult), [PartDefaultTransportLabels](Inventory.md#Inventory.PartDefaultTransportLabel), [PartialQuantities](Common.md#Common.PartialQuantity), [PartImages](Inventory.md#Inventory.PartImage), [PartLocations](Inventory.md#Inventory.PartLocation), [PartOtherIdentities](Inventory.md#Inventory.PartOtherIdentity), [PartPurchaseControlDataRows](Inventory.md#Inventory.PartPurchaseControlDataRow), [Parts](Inventory.md#Inventory.Part), [PartUnitUsages](Common.md#Common.PartUnitUsage), [PaymentPlanTemplateRows](Common.md#Common.PaymentPlanTemplateRow), [PhysicalInventoryRows](Inventory.md#Inventory.PhysicalInventoryRow), [PriceChangeLogs](Inventory.md#Inventory.PriceChangeLog), [ProductRecords](Inventory.md#Inventory.ProductRecord), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [QuantityChanges](Inventory.md#Inventory.QuantityChange), [QuoteRows](Sales.md#Sales.QuoteRow), [Revisions](Common.md#Common.Revision), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRowInflows](Sales.md#Sales.SalesAgreementRowInflow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow), [SalesForecastRows](Inventory.md#Inventory.SalesForecastRow), [SalesPickingListRowQuantities](Sales.md#Sales.SalesPickingListRowQuantity), [SalesPrices](Sales.md#Sales.SalesPrice), [StaggeredPrices](Common.md#Common.StaggeredPrice), [StockTransactions](Inventory.md#Inventory.StockTransaction), [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink)

<a id="Inventory.PartTemplate"></a>
### PartTemplates

Represents a part template.

- **Endpoint:** `GET /api/v1/Inventory/PartTemplates`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.47

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part template. |
| `AbcCodeId` | `Int64?` | yes | [AbcCodes](Inventory.md#Inventory.AbcCode) | The business key identifier of the ABC code that the part template applies. |
| `AnnualVolume` | `Decimal?` | yes |  | The annual volume that the part template applies. |
| `AutomaticReportingMode` | `Int32?` | yes |  | The automatic reporting mode that the part template applies. |
| `CategoryString` | `String` | no |  | The category string that the part template applies. |
| `Code` | `String` | no |  | The human readable identifier of the part template. |
| `CountryOfOriginId` | `Int64?` | yes | [Countries](Common.md#Common.Country) | The business key identifier of the country of origin that the part template applies. |
| `DeductSalesForecast` | `Int32?` | yes |  | The sales forecast deduction type that the part template applies. |
| `DeductionMethod` | `Int32?` | yes |  | The sales deduction method that the part template applies if a deduct sales forecast type is defined. |
| `Description` | `String` | no |  | The description of the part template. |
| `Eoq` | `Decimal?` | yes |  | The EOQ that the part template applies. |
| `IsActive` | `Boolean` | no |  | Specifies whether or not the part template is active. |
| `IsDefault` | `Boolean` | no |  | Specifies whether or not the part template is the default part template. |
| `IsPreset` | `Boolean` | no |  | Specifies whether or not the part template is a preset. |
| `LotSizingRule` | `Int32?` | yes |  | The lot sizing rule that the part template applies. |
| `ManageStockBalance` | `Boolean?` | yes |  | The stock balance management strategy that the part template applies. |
| `UseRandomLocationStorage` | `Boolean?` | yes |  | The random location storage strategy that the part template applies. |
| `AllowOrderCreationFromCustomerOrder` | `Boolean?` | yes |  | The customer order creation permission that the part template applies. |
| `RoundingBase` | `Decimal?` | yes |  | The rounding base that the part template applies. |
| `LeadTime` | `TimeSpan?` | yes |  | The lead time that the part template applies. |
| `ManufacturingLabelType` | `Int32?` | yes |  | The manufacturing transport label type that the part template applies. |
| `SalesLabelType` | `Int32?` | yes |  | The sales transport label type that the part template applies. |
| `PurchaseLabelType` | `Int32?` | yes |  | The purchase transport label type that the part template applies. |
| `UseInCalculation` | `Boolean` | no |  | Whether or not the parts that derive from the part template should be used in calculations. |
| `PartCodeId` | `Int64?` | yes | [PartCodes](Inventory.md#Inventory.PartCode) | The business key identifier of the part code that the part template applies. |
| `PartType` | `Int32?` | yes |  | The part template type that the part template applies. |
| `PreparerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the preparer that the part template applies. |
| `ProductGroupId` | `Int64?` | yes | [ProductGroups](Common.md#Common.ProductGroup) | The business key identifier of the product group that the part template applies. |
| `ReorderPoint` | `Decimal?` | yes |  | The reorder point that the part template applies. |
| `SafetyStock` | `Decimal?` | yes |  | The safety stock that the part template applies. |
| `SafetyTime` | `TimeSpan?` | yes |  | The safety time that the part template applies. |
| `SerialNumberGeneration` | `Int32?` | yes |  | The serial number generation strategy that the part template applies. |
| `SerialNumberGenerationSource` | `Int32?` | yes |  | The serial number generation source that the part template applies. |
| `TemplateType` | `Int32` | no |  | The template type of the part template. |
| `TraceabilityMode` | `Int32?` | yes |  | The traceability mode that the part template applies. |
| `ProfitMarkupId` | `Int64?` | yes | [ProfitMarkups](Inventory.md#Inventory.ProfitMarkup) | The business key identifier of the profit markup that the part template applies. |
| `SalesOverheadMarkupId` | `Int64?` | yes | [SalesOverheadMarkups](Inventory.md#Inventory.SalesOverheadMarkup) | The business key identifier of the sales overhead markup that the part template applies. |
| `PartActivityTemplateId` | `Int64?` | yes |  | The business key identifier of the part activity template that the part template applies. References PartActivityTemplate. |
| `PartStatus` | `Int32?` | yes |  | The part status that the part template applies. |
| `LithuanianCountyOfOrigin` | `Int32?` | yes |  | The county of origin that the part template applies. Only used in the Lithuanian country package. |

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

**References out:** [AbcCodes](Inventory.md#Inventory.AbcCode), [Countries](Common.md#Common.Country), [PartCodes](Inventory.md#Inventory.PartCode), [Persons](Common.md#Common.Person), [ProductGroups](Common.md#Common.ProductGroup), [ProfitMarkups](Inventory.md#Inventory.ProfitMarkup), [SalesOverheadMarkups](Inventory.md#Inventory.SalesOverheadMarkup)
**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.PhysicalInventoryList"></a>
### PhysicalInventoryLists

Represents a physical inventory list.

- **Endpoint:** `GET /api/v1/Inventory/PhysicalInventoryLists`
- **Required permission:** Report stock count
- **Introduced in:** 22.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the physical inventory list. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse for the physical inventory list. |
| `Number` | `Int64` | no |  | The number of the physical inventory list. |
| `Version` | `Int32` | no |  | The version of the physical inventory list. |
| `Name` | `String` | no |  | The name of the physical inventory list. |
| `InventoryStatus` | `Int32` | no |  | The status for the physical inventory list. |
| `State` | `Int32` | no |  | The state for the physical inventory list. |
| `CreatedWhen` | `DateTimeOffset` | no |  | The date when the physical inventory list was created. |
| `PrintedWhen` | `DateTimeOffset?` | yes |  | The date when the physical inventory list was printed. |

- `InventoryStatus` — None=0, UnderInventory=1, UnderInventoryWithBalanceCheckpoint=2
- `State` — NotStarted=0, Started=1, Paused=2, Finished=3, FinishedWithPendingApproval=4

**References out:** [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [PhysicalInventoryRows](Inventory.md#Inventory.PhysicalInventoryRow)

<a id="Inventory.PhysicalInventoryRow"></a>
### PhysicalInventoryRows

Represents a physical inventory row.

- **Endpoint:** `GET /api/v1/Inventory/PhysicalInventoryRows`
- **Required permission:** Report stock count
- **Introduced in:** 22.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the physical inventory row. |
| `PhysicalInventoryListId` | `Int64` | no | [PhysicalInventoryLists](Inventory.md#Inventory.PhysicalInventoryList) | The business key identifier of the physical inventory list that the row belongs to. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part of the physical inventory row. |
| `LocationId` | `Int64` | no | [PartLocations](Inventory.md#Inventory.PartLocation) | The business key identifier of the part location of the physical inventory row. |
| `ProductRecordId` | `Int64` | no | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the product record of the physical inventory row. |
| `Reported` | `Boolean` | no |  | Indicates if the physical inventory row is reported. _(Use ReportingState to get current state and see if row is reported, pending approval or rejected)_ |
| `ReportingState` | `Int32` | no |  | Reporting state of the physical inventory row. |
| `Version` | `Int32` | no |  | The version of the physical inventory row. |
| `ReportedQuantity` | `Decimal?` | yes |  | The reported quantity for the physical inventory row. |

- `ReportingState` — NotReported=0, Reported=1, PendingApproval=2, ApprovalRejected=3, Discarded=4

**References out:** [PartLocations](Inventory.md#Inventory.PartLocation), [Parts](Inventory.md#Inventory.Part), [PhysicalInventoryLists](Inventory.md#Inventory.PhysicalInventoryList), [ProductRecords](Inventory.md#Inventory.ProductRecord)

<a id="Inventory.PriceChangeLog"></a>
### PriceChangeLogs

Represents a price change log entity.

- **Endpoint:** `GET /api/v1/Inventory/PriceChangeLogs`
- **Required permission:** Show part
- **Introduced in:** 2.51

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the price change log. |
| `Context` | `Int32` | no |  | The context of the price change in the price change log. |
| `PriceType` | `Int32` | no |  | The type of the price in the price change log. |
| `PriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) | The business key identifier of the price changes log's price list. |
| `Timestamp` | `DateTimeOffset` | no |  | The timestamp of the price change log. |
| `UserCode` | `String` | no |  | The user code of the price change log. |
| `NewPriceAmount` | `Decimal?` | yes |  | The new price amount of the price change log. |
| `NewPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier for the new price currency of the price change log. |
| `OldPriceAmount` | `Decimal?` | yes |  | The old price amount of the price change log. |
| `OldPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier for the old price currency of the price change log. |
| `Balance` | `Decimal?` | yes |  | The balance of the price change log. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The part id of the price change log. |
| `CalculationId` | `Int64?` | yes |  | The calculation id of the price change log. |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The supplier id of the price change log. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The customer id of the price change log. |
| `StaggeredQuantity` | `Decimal?` | yes |  | The staggered quantity of the price change log. |
| `IsSetupPrice` | `Boolean` | no |  | Is the price in the price change log a setup price. |
| `Discount` | `Decimal?` | yes |  | The discount of the price change log. |
| `IsExportedToManagementAccounting` | `Boolean` | no |  | Is exported to management accounting. |

- `Context` — Manual=0, PreCalculation=1, PostCalculation=2, ManualFromList=3, PriceImport=4, PurchaseCalculation=5, PartSynchronization=6, CancelInvoice=7, CreditInvoice=8, Invoice=9, ExpenseInvoice=10, UndoExpenseInvoice=11, SubcontractingCostReport=12, AutoUpdateFromFuturePrice=13, PriceCorrectionInvoice=14, ReportingOfReturnOrder=15, FinalRecordingOfCorrectionInvoice=16, FullReturnToSupplier=17, AutomaticMovingAveragePriceCalculation=18
- `PriceType` — Standard=0, PriceList=3, FuturePriceList=4, PriceFromInvoiceOrCustomerOrderRow=5, Invoice=6, PriceListStaggered=7, FuturePriceListStaggered=8, CustomerStaggered=9, FutureCustomerStaggered=10, SupplierStaggered=11, FutureSupplierStaggered=12, StandardPriceFromCustomerOrderRowWithFallbackToPartStandardPrice=13, CustomerWithFallbackPriceListOnCustomer=14, FutureSetupPrice=15, StandardPriceOnDelivery=16, StandardPriceOnInvoicing=17, StandardPriceOnFinalBookingAccountsPayable=18, PurchaseOrder=19, FifoAtInvoicing=20, LinkedConfiguredCustomOrderRow=21, HistoricalFifoPrice=22, ComparativePrice=23, ProductRecordStandardPrice=24, MovingAveragePrice=25, MovingAveragePriceAtInvoicing=26, FutureSupplier=-9998, FutureCustomer=-9997, None=-99, ReportedStandard=-20, MaterialCost=-19, HistoricalStandard=-18, DiscountedCustomer=-17, DiscountedSupplier=-16, PostCalculatedAverage=-15, SavedAverage=-14, Lowest=-9, FIFO=-8, AvarageSales=-7, LatestSales=-6, AveragePurchase=-5, LatestPurchase=-4, Customer=-3, Supplier=-2, FutureStandard=-1

**References out:** [Currencies](Common.md#Common.Currency), [Customers](Sales.md#Sales.Customer), [Parts](Inventory.md#Inventory.Part), [PriceLists](Common.md#Common.PriceList), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Inventory.ProductRecordOperationReporting"></a>
### ProductRecordOperationReportings

Represents a product record operation reporting.

- **Endpoint:** `GET /api/v1/Inventory/ProductRecordOperationReportings`
- **Required permission:** Show serial number
- **Introduced in:** 2.49

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the product record operation reporting. |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  | The time when the product record operation reporting was reported. |
| `ReportingType` | `Int32` | no |  | The type that the product record operation reporting is. |
| `ProductRecordId` | `Int64` | no | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the product record that the product record operation reporting applies. |
| `OperationReportingId` | `Int64?` | yes |  | The business key identifier of the manufacturing order operation reporting that the product record operation reporting applies. |
| `OrderNumber` | `String` | no |  | The product record operation reportings order number. |
| `ReportedTime` | `TimeSpan?` | yes |  | The product record operation reportings reported time. |
| `ReportedQuantity` | `Decimal?` | yes |  | The product record operation reportings reported quantity. |
| `QuantityPerCycle` | `Decimal?` | yes |  | The product record operation reportings quantity per cycle. |
| `CycleTime` | `TimeSpan?` | yes |  | The product record operation reportings cycle time. |
| `TotalTime` | `TimeSpan?` | yes |  | The product record operation reportings total time. |
| `TotalCycles` | `Decimal` | no |  | The product record operation reportings total cycle. |
| `TotalMeasurementSetting` | `Decimal` | no |  | The product record operation reportings total seasurement setting. |
| `ReportedMeasurementSetting` | `Decimal?` | yes |  | The product record operation reportings reported measurement setting. |

- `ReportingType` — OperationReporting=0, Inventory=1, Rejection=2

**References out:** [ProductRecords](Inventory.md#Inventory.ProductRecord)
**Referenced by:** [ProductRecords](Inventory.md#Inventory.ProductRecord)

<a id="Inventory.ProductRecord"></a>
### ProductRecords

Represents a product record.

- **Endpoint:** `GET /api/v1/Inventory/ProductRecords`
- **Required permission:** Show serial number
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the product record. |
| `ProductRecordType` | `Int32` | no |  | The type of the product record. |
| `SerialNumberWithPartNumber` | `String` | no |  | The batch or serial number along with the part number of the product record. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the product record's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The product record comment. |
| `CertificateId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the product record's certificate. |
| `Certificate` | `Comments` | no | [Comments](Common.md#Common.Comment) | The certificate of the product record. |
| `WarrantyCommitmentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the product record's warranty commitment. |
| `WarrantyCommitment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The warranty commitment of the product record. |
| `InstallationCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the product record's installation comment. |
| `InstallationComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The installation comment of the product record. |
| `SerialNumber` | `String` | no |  | The batch or serial number of the product record. |
| `ChargeNumber` | `String` | no |  | The charge number of the product record. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the product record belongs to. |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The part that the product record belongs to. |
| `ManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) | The business key identifier of the manufacturing order that the product record is linked to. |
| `ManufacturingOrder` | `ManufacturingOrders` | no | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) | The manufacturing order that the product record is linked to. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) | A collection of extra field values for the product record. |
| `HasWarranty` | `Boolean` | no |  | Specifies if the product is covered by warranty. |
| `WarrantyStartDate` | `DateTimeOffset?` | yes |  | The date when the warranty started. |
| `WarrantyEndDate` | `DateTimeOffset?` | yes |  | The date when the warranty expires. |
| `WarrantyMonths` | `Int32` | no |  | The length of the warranty period in months. |
| `OwnerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the product record owner. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order of the product record. |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The customer order of the product record. |
| `CustomerOrderDeliveryRowId` | `Int64?` | yes | [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow) | The business key identifier of the customer order delivery row of the product record. |
| `CustomerOrderDeliveryRow` | `CustomerOrderDeliveryRows` | no | [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow) | The customer order of the product record. |
| `DeliveryAddressId` | `Int64?` | yes | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The business key identifier of the delivery address of the product record. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The delivery address of the product record. |
| `BlockMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the message for the life cycle state of the product record. |
| `BlockMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) | The message for the life cycle state of the product record. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The identifier of the application user that has set the product record to blocked or message. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the product record. |
| `BlockContext` | `Int32` | no |  | The block context which the product records life cycle state is used for. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  | The date from which the product record has been blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  | The date from which the product record has been unblocked. |
| `MeasurementSetting` | `Decimal?` | yes |  | The measurement setting for a product record. |
| `OperationTime` | `TimeSpan?` | yes |  | The operation time for a product record. |
| `NumberOfCycles` | `Decimal?` | yes |  | The number of cycles for a product record. |
| `OperationReportings` | `ProductRecordOperationReportings[]` | no | [ProductRecordOperationReportings](Inventory.md#Inventory.ProductRecordOperationReporting) | The list of product record operation reporting logs. |
| `CustomerOrderOurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the customer order our reference person of the product record. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the customer's reference of the product record. |
| `CustomerOrderPartRevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the revision for the part of the product record. Has been replaced by the more general PartRevisionId _(Replaced by PartRevisionId)_ |
| `PartRevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the revision for the part of the product record. |
| `PlannedDeliveryDate` | `DateTimeOffset?` | yes |  | The planned delivery date for the customer order of the product record. |
| `ActualDeliveryDate` | `DateTimeOffset?` | yes |  | The actual delivery date for the customer order of the product record. |
| `MeasurementSettingWarranty` | `Decimal?` | yes |  | The meter reading for warranty of the product record. |
| `OperationTimeWarranty` | `TimeSpan?` | yes |  | The operation time for warranty of the product record. |
| `NumberOfCyclesWarranty` | `Decimal?` | yes |  | The number of cycles for warranty of the product record. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of the purchase order of the product record. |
| `ActualArrivalDate` | `DateTimeOffset?` | yes |  | The actual delivery date for the purchase order of the product record. |
| `ManufactureDate` | `DateTimeOffset?` | yes |  | The finish date for the manufacturing order of the product record. |
| `InstallationOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order which the installation is linked to. |
| `InstalledBy` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the person that is linked to the installation of the product record. |
| `InstallationDate` | `DateTimeOffset?` | yes |  | The date when the installation of the product record will take place. |
| `InstallationCode` | `String` | no |  | The code that is applying to the installation of the product record. |
| `WarrantyCode` | `String` | no |  | The code that is applying to the installation of the product record. |
| `RegistrationNo` | `String` | no |  | The registration number for the manufacturing order of the product record. |
| `TypeDescription` | `String` | no |  | The type description for the customer order of the product record. |
| `Status` | `Int32` | no |  | The status of the product record. |
| `BestBeforeDate` | `DateTimeOffset?` | yes |  | The best before date of the product record. |
| `ProductRecordBatchId` | `Int64?` | yes |  | The business key identifier of the batch number. |

- `ProductRecordType` — ProductRecord=0, Batch=1
- `LifeCycleState` — ApprovalForUse=0, NonApproval=1, ServicePastDue=2, UnderServiceOrCalibration=3, Rejected=4, ServiceOrCalibrationBeforeUse=5, Missing=6, Scrapped=7
- `BlockContext` (bitmask) — None=0, ManufacturingOrderWithdrawal=1, ManufacturingOrderClearance=2, CustomerOrderDelivery=4, CustomerOrderClearance=8, RequirementCalculation=16
- `Status` — NotInitialized=0, Registrered=1, Manufacturing=2, ManufacturingPending=3, Inventory=4, Blocked=5, Packed=6, PackedAndMarked=7, Historical=9

**References out:** [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [ExtraFields](Common.md#Common.ExtraField), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](Inventory.md#Inventory.Part), [Persons](Common.md#Common.Person), [ProductRecordOperationReportings](Inventory.md#Inventory.ProductRecordOperationReporting), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Revisions](Common.md#Common.Revision)
**Referenced by:** [AdditionalIDsRecords](Inventory.md#Inventory.AdditionalIdsRecord), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink), [CustomerOrders](Sales.md#Sales.CustomerOrder), [MaintenanceReportingRows](Manufacturing.md#Manufacturing.MaintenanceReportingRow), [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [PackageRowPartLocations](Sales.md#Sales.PackageRowPartLocation), [PartLocationProductRecords](Inventory.md#Inventory.PartLocationProductRecord), [PhysicalInventoryRows](Inventory.md#Inventory.PhysicalInventoryRow), [ProductRecordOperationReportings](Inventory.md#Inventory.ProductRecordOperationReporting), [SalesAgreements](Sales.md#Sales.SalesAgreement), [SalesPickingListRowQuantities](Sales.md#Sales.SalesPickingListRowQuantity), [StockBalanceChanges](Inventory.md#Inventory.StockBalanceChange), [StockTransactions](Inventory.md#Inventory.StockTransaction)

<a id="Inventory.ProfitMarkup"></a>
### ProfitMarkups

Represents profit markup.

- **Endpoint:** `GET /api/v1/Inventory/ProfitMarkups`
- **Required permission:** Show calculation mark-up
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the profit markup. |
| `Number` | `Int32` | no |  | The human readable number of the profit markup. |
| `Description` | `String` | no |  | The translated description of the profit markup. |
| `Markup` | `Decimal` | no |  | The markup defined by the profit markup. |

**Referenced by:** [Parts](Inventory.md#Inventory.Part), [PartTemplates](Inventory.md#Inventory.PartTemplate)

<a id="Inventory.QuantityChange"></a>
### QuantityChanges

Represents a quantity change.

- **Endpoint:** `GET /api/v1/Inventory/QuantityChanges`
- **Required permission:** Show part
- **Introduced in:** 2.48

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the quantity change. |
| `ActualDeliveryDate` | `DateTimeOffset` | no |  | The date that the delivery was performed. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The part that the quantity change was made for. |
| `BalanceChange` | `Decimal` | no |  | The total balance change. |
| `AvailableBalance` | `Decimal` | no |  | The total available balance in the warehouse before the quantity change was performed. Note that this only provides a value for quantity changes that have status "Cleared" and are created in the outgoing delivery planning. This property is not suitable for looking at the historical balance of a part. |
| `PickingByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The user that performed the picking. |
| `PickingByPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The person that performed the picking. |
| `DeliveredByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The user that performed the delivery. |
| `DeliveredByPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The person that performed the delivery. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The warehouse where the quantity change was performed. |
| `StockBalanceChanges` | `StockBalanceChanges[]` | no | [StockBalanceChanges](Inventory.md#Inventory.StockBalanceChange) | The stock balance changes that belong to the quantity change. |
| `Status` | `Int32` | no |  | This determines which way the quantity change is going. |
| `ClearingTimeStamp` | `DateTimeOffset?` | yes |  | The date when clearing was performed. |
| `PickingTimeStamp` | `DateTimeOffset?` | yes |  | The date when picking was performed. |
| `IsOriginalReceivingInspectionQuantity` | `Boolean` | no |  | Tells if quantity change is original receiving inspection quantity. |
| `Price` | `Decimal?` | yes |  | Price of the row when the transaction was made. |
| `CanceledQuantity` | `Decimal` | no |  | The quantity that was cancelled. |
| `IsExportedToManagementAccounting` | `Boolean` | no |  | Is exported to management accounting |
| `CanceledTimestamp` | `DateTimeOffset?` | yes |  | The date when cancel was performed. |
| `UndoneTimestamp` | `DateTimeOffset?` | yes |  | The date when undo was performed. |
| `ReservationId` | `Int64?` | yes |  | The reservation that is linked to the quantity change. |

- `Status` — Cleared=1, Picking=2, OutgoingDelivery=3, Adviced=4, ReceivingInspection=5, IncomingDelivery=6, CanceledOutgoingDelivery=7, CanceledIncomingDelivery=8, WithdrawInspection=9, InspectionCompleted=10, InspectionRejection=11

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Parts](Inventory.md#Inventory.Part), [Persons](Common.md#Common.Person), [StockBalanceChanges](Inventory.md#Inventory.StockBalanceChange), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [ManufacturingPickingListMaterials](Manufacturing.md#Manufacturing.ManufacturingPickingListMaterial), [PurchaseOrderDeliveryRowQuantities](Purchase.md#Purchase.PurchaseOrderDeliveryRowQuantity), [StockBalanceChanges](Inventory.md#Inventory.StockBalanceChange)

<a id="Inventory.SalesForecastRow"></a>
### SalesForecastRows

Represents a sales forecast row.

- **Endpoint:** `GET /api/v1/Inventory/SalesForecastRows`
- **Required permission:** Show basic data for part
- **Introduced in:** 22.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the sales forecast row. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier for the part of the sales forecast row. |
| `Quantity` | `Decimal` | no |  | The quantity of the sales forecast row. |
| `UnitId` | `Int64` | no | [Units](Common.md#Common.Unit) | The business key identifier for the unit of the sales forecast row. |
| `DeliveryDate` | `DateTimeOffset` | no |  | The delivery date of the sales forecast row. |
| `SalesForecastId` | `Int64` | no | [SalesForecasts](Inventory.md#Inventory.SalesForecast) | The business key identifier of the sales forecast that the row belongs to. |

**References out:** [Parts](Inventory.md#Inventory.Part), [SalesForecasts](Inventory.md#Inventory.SalesForecast), [Units](Common.md#Common.Unit)
**Referenced by:** [SalesForecasts](Inventory.md#Inventory.SalesForecast)

<a id="Inventory.SalesForecast"></a>
### SalesForecasts

Represents a sales forecast.

- **Endpoint:** `GET /api/v1/Inventory/SalesForecasts`
- **Required permission:** Show basic data for part
- **Introduced in:** 22.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the sales forecast. |
| `ForecastCode` | `String` | no |  | The human readbale identifier of the sales forecast. |
| `Description` | `String` | no |  | The translated description of the sales forecast. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the sales forecast belongs to. |
| `TimeSpan` | `TimeSpan` | no |  | The interval time span of the sales forecast. |
| `IsActive` | `Boolean` | no |  | The flag that indicates if the sales forecast is active. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier for the customer of the sales forecast. |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The business key identifier for the customer account group of the sales forecast. |
| `CustomerDistrictId` | `Int64?` | yes | [CustomerDistricts](Sales.md#Sales.CustomerDistrict) | The business key identifier for the customer district of the sales forecast. |
| `SalesForecastRows` | `SalesForecastRows[]` | no | [SalesForecastRows](Inventory.md#Inventory.SalesForecastRow) | The rows of the sales forecast. |

**References out:** [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [CustomerDistricts](Sales.md#Sales.CustomerDistrict), [Customers](Sales.md#Sales.Customer), [SalesForecastRows](Inventory.md#Inventory.SalesForecastRow), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [SalesForecastRows](Inventory.md#Inventory.SalesForecastRow)

<a id="Inventory.SalesOverheadMarkup"></a>
### SalesOverheadMarkups

Represents sales overhead markup.

- **Endpoint:** `GET /api/v1/Inventory/SalesOverheadMarkups`
- **Required permission:** Show calculation mark-up
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the sales overhead markup. |
| `Number` | `Int32` | no |  | The human readable number of the sales overhead markup. |
| `Description` | `String` | no |  | The translated description of the sales overhead markup. |
| `Markup` | `Decimal` | no |  | The markup defined by the sales overhead markup. |

**Referenced by:** [Parts](Inventory.md#Inventory.Part), [PartTemplates](Inventory.md#Inventory.PartTemplate)

<a id="Inventory.StockBalanceChange"></a>
### StockBalanceChanges

Represents a stock balance change.

- **Endpoint:** `GET /api/v1/Inventory/StockBalanceChanges`
- **Required permission:** Show part
- **Introduced in:** 2.48

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the stock balance change. |
| `PartLocationId` | `Int64?` | yes | [PartLocations](Inventory.md#Inventory.PartLocation) | The part location that the balance change effects. |
| `BalanceChange` | `Decimal` | no |  | The balance change for this part location. |
| `AvailableBalance` | `Decimal` | no |  | The available balance for the part location before the balance change was performed. NOTE: This only produces a value for arrival reporting and manufacturing reportings. This property is not suitable for looking at the historical balance of a part location. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The product record that is used for this balance change. |
| `QuantityChangeId` | `Int64` | no | [QuantityChanges](Inventory.md#Inventory.QuantityChange) | The parent quantity change of the stock balance change. |

**References out:** [PartLocations](Inventory.md#Inventory.PartLocation), [ProductRecords](Inventory.md#Inventory.ProductRecord), [QuantityChanges](Inventory.md#Inventory.QuantityChange)
**Referenced by:** [QuantityChanges](Inventory.md#Inventory.QuantityChange)

<a id="Inventory.StockTransaction"></a>
### StockTransactions

Represents a stock transaction.

- **Endpoint:** `GET /api/v1/Inventory/StockTransactions`
- **Required permission:** Show basic data for part
- **Introduced in:** 22.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the stock transaction. |
| `PartNumber` | `String` | no |  | The part number of the stock transaction. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that was involved in the stock transaction. This value might not be set even though a part always is involved in a stock transaction, read part number to identify involved part in that case. |
| `BalanceChange` | `Decimal` | no |  | The balance change of the stock transaction. |
| `BalanceOnPartAfterChange` | `Decimal` | no |  | The balance on the part after the stock transaction. |
| `BalanceOnLocationAfterChange` | `Decimal` | no |  | The balance on the location after the stock transaction. |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  | The logging timestamp of the stock transaction. |
| `DeliveryDate` | `DateTimeOffset` | no |  | The delivery date of the stock transaction. |
| `LocationName` | `String` | no |  | The location name of the stock transaction. |
| `BusinessTransactionId` | `Int64` | no |  | The business transaction identity of the stock transaction. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse where the stock transaction occured. |
| `PhysicalInventoryListNumber` | `Int64?` | yes |  | The physical inventory list number of the stock transaction. |
| `PartLocationId` | `Int64?` | yes | [PartLocations](Inventory.md#Inventory.PartLocation) | The business key identifier of the part location where the stock transaction occured. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the product record used in the stock transaction. |
| `BatchNumber` | `String` | no |  | The batch number of the product record in this stock transaction. |
| `OrderNumber` | `String` | no |  | The order number associated to this stock transaction. |
| `BusinessTransactionContextType` | `Int32` | no |  | The type of the business transaction context of this stock transaction. |
| `StandardPrice` | `Decimal` | no |  | The standard price of the stock transaction. |
| `Price` | `Decimal?` | yes |  | The price of the stock transaction. |
| `ReportedPrice` | `Decimal` | no |  | The reported price of the stock transaction. |
| `Amount` | `Decimal` | no |  | The calculated amount based on Price multiplied by BalanceChange of the stock transaction. |

- `BusinessTransactionContextType` — NotInitialized=0, ArrivalReporting=1, ManufacturingOrderReporting=2, DeliveryReporting=3, PhysicalInventory=4, UnplannedStockWithdrawal=5, MoveBetweenWarehouse=6, MoveStockBalance=7, NonconformityPosteriorRejection=8, DirectlyRegisteredInvoice=9, RemovalOfPartLocation=10, ManufacturingOrderMaterialReporting=11, UnplannedStockArrivalReporting=12, StockImport=13, DeliveryReportingStockOrder=14, ArrivalReportingStockOrder=15, UndoManufacturingOrderMaterialReporting=16, UndoManufacturingOrderReporting=17, UndoArrivalReporting=18, UndoDeliveryReporting=19, UndoArrivalReportingStockOrder=20, UndoDeliveryReportingStockOrder=21, OutgoingReusable=22, ArrivalReusable=23, UndoOutgoingReusable=24, UndoArrivalReusable=25, ToolWithdrawal=26, ToolReturn=27, CreditSupplierInvoice=28, CreditCustomerInvoice=29, ReturnPurchaseOrder=30, SplitInvoiceBasis=31, CreationOfPartLocation=32, ArrivalsCorrection=33, ArrivalRejection=34, UndoReturnPurchaseOrder=35

**References out:** [PartLocations](Inventory.md#Inventory.PartLocation), [Parts](Inventory.md#Inventory.Part), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Warehouses](Common.md#Common.Warehouse)

<a id="Inventory.StorageOverheadMarkup"></a>
### StorageOverheadMarkups

Represents storage overhead markup.

- **Endpoint:** `GET /api/v1/Inventory/StorageOverheadMarkups`
- **Required permission:** Show calculation mark-up
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the storage overhead markup. |
| `Number` | `Int32` | no |  | The human readable number of the storage overhead markup. |
| `Description` | `String` | no |  | The translated description of the storage overhead markup. |
| `Markup` | `Decimal` | no |  | The markup defined by the storage overhead markup. |
| `Type` | `Int32` | no |  | The type of storage overhead markup. |

- `Type` — StorageOverhead=0, SubContract=1, Both=2

**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Inventory.UnplannedStockMovementReasonCode"></a>
### UnplannedStockMovementReasonCodes

Represents a queryable unplanned stock movement reason code.

- **Endpoint:** `GET /api/v1/Inventory/UnplannedStockMovementReasonCodes`
- **Required permission:** Show cause codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the unplanned stock movement reason code. |
| `Code` | `String` | no |  | The alphanumeric code of the reason code. |
| `Description` | `String` | no |  | The translated description of the reason code. |
| `CommentMandatory` | `Boolean` | no |  | Specifies if a comment is mandatory for the reason code. |
| `Active` | `Boolean` | no |  | Specifies if the reason code is active in the system. |



## Depends on other modules

- [Accounting](Accounting.md): [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable)
- [Common](Common.md): [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BlobData](Common.md#Common.BlobData), [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [Countries](Common.md#Common.Country), [Currencies](Common.md#Common.Currency), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [Departments](Common.md#Common.Department), [ExtraFields](Common.md#Common.ExtraField), [FormReportConfigurations](Common.md#Common.FormReportConfiguration), [FormTemplates](Common.md#Common.FormTemplate), [MeasuringTemplates](Common.md#Common.MeasuringTemplate), [PartConfigurationTemplates](Common.md#Common.PartConfigurationTemplate), [PartUnitUsages](Common.md#Common.PartUnitUsage), [PartialQuantities](Common.md#Common.PartialQuantity), [Persons](Common.md#Common.Person), [PriceLists](Common.md#Common.PriceList), [ProductGroups](Common.md#Common.ProductGroup), [Projects](Common.md#Common.Project), [RejectionCodeItems](Common.md#Common.RejectionCodeItem), [Revisions](Common.md#Common.Revision), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [TransferProfiles](Common.md#Common.TransferProfile), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse)
- [Manufacturing](Manufacturing.md): [Drawings](Manufacturing.md#Manufacturing.Drawing), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [Preparations](Manufacturing.md#Manufacturing.Preparation), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
- [Purchase](Purchase.md): [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Suppliers](Purchase.md#Purchase.Supplier), [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink)
- [Sales](Sales.md): [Customers](Sales.md#Sales.Customer), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [CustomerDistricts](Sales.md#Sales.CustomerDistrict), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerPartLinks](Sales.md#Sales.CustomerPartLink)
