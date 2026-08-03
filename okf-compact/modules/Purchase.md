# Purchase

Monitor API module `Purchase`: 30 queryable entities, 0 commands, 0 payload types.

## Queryable entities

<a id="Purchase.BlanketOrderPurchaseRow"></a>
### BlanketOrderPurchaseRows

Represents a blanket order row for purchase.

- **Endpoint:** `GET /api/v1/Purchase/BlanketOrderPurchaseRows`
- **Required permission:** Show blanket order
- **Introduced in:** 23.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `LifeCycleState` | `Int32` | no |  |
| `ParentOrderId` | `Int64?` | yes | [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase) |
| `ParentRowId` | `Int64?` | yes | [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow) |
| `SupplierPartNumber` | `String` | no |  |
| `Position` | `Int64?` | yes |  |
| `OrderRowType` | `Int32` | no |  |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) |
| `PartRowType` | `Int32` | no |  |
| `Quantity` | `Decimal` | no |  |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) |
| `Price` | `Decimal?` | yes |  |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `PriceOriginPriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) |
| `PriceLockedFromAutomaticChanges` | `Boolean?` | yes |  |
| `PriceIsFuturePrice` | `Boolean?` | yes |  |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `Discount` | `Decimal` | no |  |
| `SetupPrice` | `Decimal?` | yes |  |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) |
| `VatRate` | `VatRates` | no | [VatRates](Common.md#Common.VatRate) |
| `ShowFreeTextIn` | `Int32` | no |  |
| `ValidThrough` | `DateTimeOffset?` | yes |  |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) |
| `FreeTextHtml` | `String` | no |  |
| `FreeText` | `String` | no |  |
| `ConversionFactor` | `Decimal` | no |  |
| `QuantityRatio` | `Decimal?` | yes |  |
| `AdditionalRowDescription` | `String` | no |  |

- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4
- `PartRowType` — NotPartRow=0, RegularRow=1, SubPartRow=2, SetupPriceRow=3, AlloyCostRow=4, PaymentPlanRow=5, PackagingRow=6
- `ShowFreeTextIn` (bitmask) — Internal=0, Inquiry=1, Order=2, DeliverySchedule=4

**References out:** [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase), [Currencies](Common.md#Common.Currency), [Parts](Inventory.md#Inventory.Part), [PriceLists](Common.md#Common.PriceList), [Revisions](Common.md#Common.Revision), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)

<a id="Purchase.BlanketOrderPurchase"></a>
### BlanketOrderPurchases

Represents a blanket order for purchase.

- **Endpoint:** `GET /api/v1/Purchase/BlanketOrderPurchases`
- **Required permission:** Show blanket order
- **Introduced in:** 23.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `LifeCycleState` | `Int32` | no |  |
| `OrderNumber` | `String` | no |  |
| `OrderTypeId` | `Int64?` | yes | [BlanketOrderPurchaseTypes](Purchase.md#Purchase.BlanketOrderPurchaseType) |
| `BusinessContactId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `SuppliersOrderNumber` | `String` | no |  |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `BusinessContactReferenceName` | `String` | no |  |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `OurReference` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `OurReferenceName` | `String` | no |  |
| `ValidationPeriod` | `Int32` | no |  |
| `ValidFrom` | `DateTimeOffset` | no |  |
| `ValidThrough` | `DateTimeOffset` | no |  |
| `Priority` | `Int32` | no |  |
| `Status` | `Int32` | no |  |
| `CategoryString` | `String` | no |  |
| `UseForwardRate` | `Boolean` | no |  |
| `ExchangeRate` | `Decimal` | no |  |
| `CurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `OrderDate` | `DateTimeOffset` | no |  |
| `DefaultOrderPrintoutVia` | `Int32` | no |  |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `CurrencyExchangeType` | `CurrencyExchangeTypes` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `Rows` | `BlanketOrderPurchaseRows[]` | no | [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow) |

- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `ValidationPeriod` — OrderDate=0, DeliveryDate=1
- `Status` — Registered=1, Printed=2, PartiallyCalledOf=7, FullyCalledOf=8, History=9
- `DefaultOrderPrintoutVia` — Printer=0, Email=1, Edi=2, None=9

**References out:** [Addresses](Common.md#Common.Address), [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderPurchaseTypes](Purchase.md#Purchase.BlanketOrderPurchaseType), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [Persons](Common.md#Common.Person), [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow)

<a id="Purchase.BlanketOrderPurchaseType"></a>
### BlanketOrderPurchaseTypes

Represents a blanket order type for purchase.

- **Endpoint:** `GET /api/v1/Purchase/BlanketOrderPurchaseTypes`
- **Required permission:** Show blanket order
- **Introduced in:** 26.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Prefix` | `String` | no |  |
| `Description` | `String` | no |  |
| `Priority` | `Int32` | no |  |
| `Visible` | `Boolean` | no |  |
| `IsPreset` | `Boolean` | no |  |
| `BaseType` | `Int32` | no |  |
| `BlanketOrderPurchaseActivityTemplateId` | `Int64?` | yes |  |
| `RateTypeSetting` | `Int32` | no |  |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `DefaultValidDays` | `Int32` | no |  |

- `BaseType` — BlanketOrder=0
- `RateTypeSetting` — Supplier=1, OrderType=2

**References out:** [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType)
**Referenced by:** [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase)

<a id="Purchase.EimDocument"></a>
### EimDocuments

Represents an EimDocument.

- **Endpoint:** `GET /api/v1/Purchase/EimDocuments`
- **Required permission:** Show supplier invoice
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `BlobDataId` | `Int64` | no | [BlobData](Common.md#Common.BlobData) |
| `RotationAngle` | `Int32` | no |  |
| `AccountsPayableId` | `Int64` | no | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `DocumentTypeId` | `Int64` | no | [EimDocumentTypes](Purchase.md#Purchase.EimDocumentType) |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [BlobData](Common.md#Common.BlobData), [EimDocumentTypes](Purchase.md#Purchase.EimDocumentType)

<a id="Purchase.EimDocumentType"></a>
### EimDocumentTypes

Represents an EIM document type.

- **Endpoint:** `GET /api/v1/Purchase/EimDocumentTypes`
- **Required permission:** Show attachment types
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `IsDefaultImportType` | `Boolean` | no |  |
| `IsDefaultMonitorExpenseType` | `Boolean` | no |  |
| `IsDefaultBankIntegrationType` | `Boolean` | no |  |

**Referenced by:** [EimDocuments](Purchase.md#Purchase.EimDocument)

<a id="Purchase.Inquiry"></a>
### Inquiries

Represents an inquiry.

- **Endpoint:** `GET /api/v1/Purchase/Inquiries`
- **Required permission:** Show inquiry
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PaymentTermDescription` | `String` | no |  |
| `GracePeriodInDays` | `Int32?` | yes |  |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) |
| `DeliveryTermDescription` | `String` | no |  |
| `DeliveryMethodDescription` | `String` | no |  |
| `BusinessContactOrderNumber` | `String` | no |  |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `OurReferenceName` | `String` | no |  |
| `BusinessContactReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `BusinessContactReferenceName` | `String` | no |  |
| `GoodsLabel` | `String` | no |  |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `Priority` | `Int32` | no |  |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) |
| `SendMethod` | `Int32` | no |  |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `TransportTime` | `Int32?` | yes |  |
| `LifeCycleState` | `Int32` | no |  |
| `Version` | `Int32` | no |  |
| `UseForwardRate` | `Boolean` | no |  |
| `ExchangeRate` | `Decimal` | no |  |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) |
| `OrderNumber` | `String` | no |  |
| `OrderDate` | `DateTimeOffset?` | yes |  |
| `Rows` | `InquiryRows[]` | no | [InquiryRows](Purchase.md#Purchase.InquiryRow) |
| `CreatedById` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `VatNumber` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) |
| `InquiryDate` | `DateTimeOffset` | no |  |
| `InquiryDescription` | `String` | no |  |
| `LatestContactDate` | `DateTimeOffset?` | yes |  |
| `ValidThroughDate` | `DateTimeOffset?` | yes |  |
| `OrderTypeId` | `Int64?` | yes | [InquiryTypes](Purchase.md#Purchase.InquiryType) |
| `OrderType` | `InquiryTypes` | no | [InquiryTypes](Purchase.md#Purchase.InquiryType) |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |

- `SendMethod` — Printer=0, Email=1, Edi=2, None=9
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `Status` — Registered=1, Printed=2, Responded=3, Closed=6, PartialOrder=7, OrderViaRelatedInquiry=8, Order=9

**References out:** [Addresses](Common.md#Common.Address), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [InquiryRows](Purchase.md#Purchase.InquiryRow), [InquiryTypes](Purchase.md#Purchase.InquiryType), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [Projects](Common.md#Common.Project), [Suppliers](Purchase.md#Purchase.Supplier), [VatGroups](Common.md#Common.VatGroup), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [InquiryRows](Purchase.md#Purchase.InquiryRow)

<a id="Purchase.InquiryRow"></a>
### InquiryRows

Represents an inquiry row.

- **Endpoint:** `GET /api/v1/Purchase/InquiryRows`
- **Required permission:** Show inquiry
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Position` | `Int64?` | yes |  |
| `OrderRowType` | `Int32` | no |  |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `EntityIdentityString` | `String` | no |  |
| `AdditionalRowDescription` | `String` | no |  |
| `FreeTextHtml` | `String` | no |  |
| `FreeText` | `String` | no |  |
| `ParentRowId` | `Int64?` | yes | [InquiryRows](Purchase.md#Purchase.InquiryRow) |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) |
| `OrderedQuantity` | `Decimal` | no |  |
| `Price` | `Decimal?` | yes |  |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `Discount` | `Decimal` | no |  |
| `ToolId` | `Int64?` | yes |  |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `WeightPerUnit` | `Decimal?` | yes |  |
| `OrderDate` | `DateTimeOffset` | no |  |
| `ConversionFactor` | `Decimal` | no |  |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `StandardPrice` | `Decimal?` | yes |  |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPrice` | `Decimal?` | yes |  |
| `SetupPriceCurrencyId` | `Int64?` | yes |  |
| `ShowPrice` | `Boolean` | no |  |
| `PartRowType` | `Int32` | no |  |
| `LifeCycleState` | `Int32` | no |  |
| `PartStatus` | `Int32?` | yes |  |
| `OrderedQuantityInOrderUnit` | `Decimal` | no |  |
| `ShowFreeTextIn` | `Int32` | no |  |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) |
| `ExemptFromStatistics` | `Boolean` | no |  |
| `ParentOrderId` | `Int64` | no | [Inquiries](Purchase.md#Purchase.Inquiry) |
| `CodingId` | `Int64?` | yes | [Codings](Accounting.md#Accounting.Coding) |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) |
| `RowIndex` | `Int32?` | yes |  |

- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4
- `PartRowType` — NotPartRow=0, RegularRow=1, SubPartRow=2, SetupPriceRow=3, AlloyCostRow=4, PaymentPlanRow=5, PackagingRow=6
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `PartStatus` — Quote=1, Prototype=2, New=3, Normal=4, NewRevision=5, PhasingOut=6, Expired=9, Inactive=99
- `ShowFreeTextIn` (bitmask) — Internal=0, Inquiry=1, Order=2, DeliverySchedule=4

**References out:** [Codings](Accounting.md#Accounting.Coding), [Currencies](Common.md#Common.Currency), [Inquiries](Purchase.md#Purchase.Inquiry), [InquiryRows](Purchase.md#Purchase.InquiryRow), [Parts](Inventory.md#Inventory.Part), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Revisions](Common.md#Common.Revision), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [Inquiries](Purchase.md#Purchase.Inquiry), [InquiryRows](Purchase.md#Purchase.InquiryRow)

<a id="Purchase.InquiryType"></a>
### InquiryTypes

Represents an inquiry type.

- **Endpoint:** `GET /api/v1/Purchase/InquiryTypes`
- **Required permission:** Show order types
- **Introduced in:** 2.31

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Prefix` | `String` | no |  |
| `Description` | `String` | no |  |
| `Priority` | `Int32` | no |  |
| `Visible` | `Boolean` | no |  |
| `IsPreset` | `Boolean` | no |  |
| `BaseType` | `Int32` | no |  |
| `CodingGroupId` | `Int64` | no |  |
| `RateTypeSetting` | `Int32` | no |  |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |

- `BaseType` — Inquiry=0
- `RateTypeSetting` — Supplier=1, OrderType=2

**References out:** [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType)
**Referenced by:** [Inquiries](Purchase.md#Purchase.Inquiry)

<a id="Purchase.OrderQuantityPurchaseOrder"></a>
### OrderQuantityPurchaseOrders

Represents a order quantity template on part that holds many partial quantities.

- **Endpoint:** `GET /api/v1/Purchase/OrderQuantityPurchaseOrders`
- **Required permission:** Show purchase orders
- **Introduced in:** 22.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](Common.md#Common.PartialQuantity) |

**References out:** [PartialQuantities](Common.md#Common.PartialQuantity)
**Referenced by:** [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)

<a id="Purchase.OtherSupplierNumber"></a>
### OtherSupplierNumbers

Represents an alternative supplier code mainly used for EDI.

- **Endpoint:** `GET /api/v1/Purchase/OtherSupplierNumbers`
- **Required permission:** Show supplier
- **Introduced in:** 2.32

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `Number` | `String` | no |  |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) |

**References out:** [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.PackingTerm"></a>
### PackingTerms

Represents a packing term.

- **Endpoint:** `GET /api/v1/Purchase/PackingTerms`
- **Required permission:** Show terms
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Number` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |

**Referenced by:** [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.PurchaseOrderAdviceRowProductRecord"></a>
### PurchaseOrderAdviceRowProductRecords

Represents a purchase order advice row product record.

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderAdviceRowProductRecords`
- **Required permission:** Show arrival
- **Introduced in:** 22.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64?` | yes | [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow) |
| `TraceabilityMode` | `Int32` | no |  |
| `BatchNumber` | `String` | no |  |
| `BatchQuantity` | `Decimal` | no |  |
| `BatchBestBeforeDate` | `DateTimeOffset?` | yes |  |
| `SerialNumberPrefix` | `String` | no |  |
| `SerialNumberStart` | `String` | no |  |
| `SerialNumberCount` | `Int32` | no |  |
| `ChargeNumber` | `String` | no |  |

- `TraceabilityMode` — None=0, Batch=1, Individual=2, IndividualOnlyWithdrawal=4

**References out:** [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow)

<a id="Purchase.PurchaseOrderAdviceRow"></a>
### PurchaseOrderAdviceRows

Represents a purchase order advice row.

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderAdviceRows`
- **Required permission:** Show arrival
- **Introduced in:** 22.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PurchaseOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `ParentId` | `Int64?` | yes | [PurchaseOrderAdvices](Purchase.md#Purchase.PurchaseOrderAdvice) |
| `Status` | `Int32` | no |  |
| `Quantity` | `Decimal` | no |  |
| `DeliveredQuantity` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) |
| `ConversionFactor` | `Decimal?` | yes |  |
| `ParentRowId` | `Int64?` | yes | [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow) |
| `SupplierPackageNumber` | `String` | no |  |
| `SupplierAgreementReference` | `String` | no |  |

- `Status` — Registered=1, PartiallyDelivered=5, History=9

**References out:** [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow), [PurchaseOrderAdvices](Purchase.md#Purchase.PurchaseOrderAdvice), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [Units](Common.md#Common.Unit)
**Referenced by:** [PurchaseOrderAdviceRowProductRecords](Purchase.md#Purchase.PurchaseOrderAdviceRowProductRecord), [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow)

<a id="Purchase.PurchaseOrderAdvice"></a>
### PurchaseOrderAdvices

Represents a purchase order advice.

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderAdvices`
- **Required permission:** Show arrival
- **Introduced in:** 22.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) |
| `Status` | `Int32` | no |  |
| `DispatchDate` | `DateTimeOffset` | no |  |
| `DeliveryNoteNumber` | `String` | no |  |
| `ShipmentNumber` | `String` | no |  |
| `GoodsTrackingUrl` | `String` | no |  |

- `Status` — Registered=1, PartiallyDelivered=5, History=9

**References out:** [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow)

<a id="Purchase.PurchaseOrderDelivery"></a>
### PurchaseOrderDeliveries

Represents a purchase order delivery entry

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderDeliveries`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PurchaseOrderId` | `Int64` | no | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) |
| `ConfirmationDate` | `DateTimeOffset?` | yes |  |
| `AdviceDate` | `DateTimeOffset?` | yes |  |
| `DeliveryNoteNumber` | `String` | no |  |
| `WayBillNumber` | `String` | no |  |
| `Rows` | `PurchaseOrderDeliveryRows[]` | no | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) |
| `ArrivalNoteNumber` | `Int64` | no |  |

**References out:** [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder)
**Referenced by:** [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice)

<a id="Purchase.PurchaseOrderDeliveryRowQuantity"></a>
### PurchaseOrderDeliveryRowQuantities

Represents a purchase order delivery row quantity entry

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderDeliveryRowQuantities`
- **Required permission:** Show purchase orders
- **Introduced in:** 26.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `QuantityChangeId` | `Int64` | no | [QuantityChanges](Inventory.md#Inventory.QuantityChange) |
| `QuantityChange` | `QuantityChanges` | no | [QuantityChanges](Inventory.md#Inventory.QuantityChange) |
| `BusinessTransactionContextType` | `Int32` | no |  |
| `ParentId` | `Int64` | no | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) |

- `BusinessTransactionContextType` — NotInitialized=0, ArrivalReporting=1, ManufacturingOrderReporting=2, DeliveryReporting=3, PhysicalInventory=4, UnplannedStockWithdrawal=5, MoveBetweenWarehouse=6, MoveStockBalance=7, NonconformityPosteriorRejection=8, DirectlyRegisteredInvoice=9, RemovalOfPartLocation=10, ManufacturingOrderMaterialReporting=11, UnplannedStockArrivalReporting=12, StockImport=13, DeliveryReportingStockOrder=14, ArrivalReportingStockOrder=15, UndoManufacturingOrderMaterialReporting=16, UndoManufacturingOrderReporting=17, UndoArrivalReporting=18, UndoDeliveryReporting=19, UndoArrivalReportingStockOrder=20, UndoDeliveryReportingStockOrder=21, OutgoingReusable=22, ArrivalReusable=23, UndoOutgoingReusable=24, UndoArrivalReusable=25, ToolWithdrawal=26, ToolReturn=27, CreditSupplierInvoice=28, CreditCustomerInvoice=29, ReturnPurchaseOrder=30, SplitInvoiceBasis=31, CreationOfPartLocation=32, ArrivalsCorrection=33, ArrivalRejection=34, UndoReturnPurchaseOrder=35

**References out:** [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [QuantityChanges](Inventory.md#Inventory.QuantityChange)
**Referenced by:** [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow)

<a id="Purchase.PurchaseOrderDeliveryRow"></a>
### PurchaseOrderDeliveryRows

Represents a purchase order delivery row entry

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderDeliveryRows`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Version` | `Int32` | no |  |
| `PurchaseOrderId` | `Int64` | no | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) |
| `PurchaseOrderRowId` | `Int64` | no | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `PurchaseOrderRow` | `PurchaseOrderRows` | no | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `DeliveryDate` | `DateTimeOffset` | no |  |
| `GoodsLocation` | `String` | no |  |
| `GoodsMessage` | `String` | no |  |
| `ArrivedQuantity` | `Decimal` | no |  |
| `ApprovedQuantity` | `Decimal` | no |  |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `PurchaseOrderDeliveryRowQuantities` | `PurchaseOrderDeliveryRowQuantities[]` | no | [PurchaseOrderDeliveryRowQuantities](Purchase.md#Purchase.PurchaseOrderDeliveryRowQuantity) |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [PurchaseOrderDeliveryRowQuantities](Purchase.md#Purchase.PurchaseOrderDeliveryRowQuantity), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder)
**Referenced by:** [BookingRows](Accounting.md#Accounting.BookingRow), [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [PurchaseOrderDeliveries](Purchase.md#Purchase.PurchaseOrderDelivery), [PurchaseOrderDeliveryRowQuantities](Purchase.md#Purchase.PurchaseOrderDeliveryRowQuantity), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)

<a id="Purchase.PurchaseOrderInvoiceRow"></a>
### PurchaseOrderInvoiceRows

Represents a purchase order invoice row entry

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderInvoiceRows`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PurchaseOrderDeliveryRowId` | `Int64` | no | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `Price` | `Decimal?` | yes |  |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceLockedFromAutomaticChanges` | `Boolean` | no |  |
| `PriceIsFuturePrice` | `Boolean` | no |  |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPrice` | `Decimal?` | yes |  |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) |
| `Discount` | `Decimal` | no |  |
| `StandardPrice` | `Decimal?` | yes |  |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `CodingId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) |
| `LedgerId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [CodingEntries](Accounting.md#Accounting.CodingEntry), [Codings](Accounting.md#Accounting.Coding), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice)

<a id="Purchase.PurchaseOrderInvoice"></a>
### PurchaseOrderInvoices

Represents a purchase order invoice entry

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderInvoices`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PurchaseOrderDeliveryId` | `Int64?` | yes | [PurchaseOrderDeliveries](Purchase.md#Purchase.PurchaseOrderDelivery) |
| `AccountGroupId` | `Int64?` | yes | [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup) |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PaymentTermDescription` | `String` | no |  |
| `GracePeriodInDays` | `Int32?` | yes |  |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) |
| `DeliveryTermDescription` | `String` | no |  |
| `DeliveryMethodDescription` | `String` | no |  |
| `ShipmentPayer` | `Int32` | no |  |
| `Rows` | `PurchaseOrderInvoiceRows[]` | no | [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow) |

- `ShipmentPayer` — BuyerPays=1, SellerPays=2, OtherPayer=3, Incoterms=4

**References out:** [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [PaymentTerms](Common.md#Common.PaymentTerm), [PurchaseOrderDeliveries](Purchase.md#Purchase.PurchaseOrderDelivery), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup), [VatGroups](Common.md#Common.VatGroup), [Warehouses](Common.md#Common.Warehouse)

<a id="Purchase.PurchaseOrderRow"></a>
### PurchaseOrderRows

Represents a purchase order row.

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderRows`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Position` | `Int64?` | yes |  |
| `OrderRowType` | `Int32` | no |  |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) |
| `EntityIdentityString` | `String` | no |  |
| `AdditionalRowDescription` | `String` | no |  |
| `FreeTextHtml` | `String` | no |  |
| `FreeText` | `String` | no |  |
| `ParentRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) |
| `OrderedQuantity` | `Decimal` | no |  |
| `Price` | `Decimal?` | yes |  |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `Discount` | `Decimal` | no |  |
| `ToolId` | `Int64?` | yes |  |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) |
| `VatRate` | `VatRates` | no | [VatRates](Common.md#Common.VatRate) |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `Warehouse` | `Warehouses` | no | [Warehouses](Common.md#Common.Warehouse) |
| `WeightPerUnit` | `Decimal?` | yes |  |
| `OrderDate` | `DateTimeOffset` | no |  |
| `ConversionFactor` | `Decimal` | no |  |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes |  |
| `StandardPrice` | `Decimal?` | yes |  |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `StandardPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `SetupPrice` | `Decimal?` | yes |  |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `ShowPrice` | `Boolean` | no |  |
| `PartRowType` | `Int32` | no |  |
| `LifeCycleState` | `Int32` | no |  |
| `PartStatus` | `Int32?` | yes |  |
| `OrderedQuantityInOrderUnit` | `Decimal` | no |  |
| `RestQuantity` | `Decimal` | no |  |
| `DeliveredQuantity` | `Decimal` | no |  |
| `InitialDeliveryDate` | `DateTimeOffset?` | yes |  |
| `DesiredDeliveryDate` | `DateTimeOffset?` | yes |  |
| `RestQuantityInOrderUnit` | `Decimal` | no |  |
| `DeliveredQuantityInOrderUnit` | `Decimal` | no |  |
| `CreationContext` | `Int32` | no |  |
| `ShowFreeTextIn` | `Int32` | no |  |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) |
| `StatisticalGoodsCode` | `StatisticalGoodsCodes` | no | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) |
| `RowStatus` | `Int32` | no |  |
| `Version` | `Int32` | no |  |
| `ArrivalReporting` | `Boolean` | no |  |
| `ConfirmedDelayed` | `Boolean` | no |  |
| `DelayCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `DelayComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `DelayReasonId` | `Int64?` | yes | [ReasonCodes](Common.md#Common.ReasonCode) |
| `DelayReason` | `ReasonCodes` | no | [ReasonCodes](Common.md#Common.ReasonCode) |
| `CodingId` | `Int64?` | yes |  |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) |
| `IsConfirmed` | `Boolean` | no |  |
| `ReceivingInspectionInstructionId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `ReceivingInspectionInstruction` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ReceivingInspectionType` | `Int32` | no |  |
| `ReceivingMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `ReceivingMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `RequiredForManufacturingOrderNode` | `Int64?` | yes |  |
| `Weight` | `Decimal` | no |  |
| `LinkedStockOrderRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
| `LinkedSubcontractingManufacturingOrderOperation` | `Int64?` | yes | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `OriginatingPurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) |
| `CausingTransType` | `Int32` | no |  |
| `CausingOrderRowId` | `Int64?` | yes |  |
| `RequirementDate` | `DateTimeOffset?` | yes |  |
| `PreviousOrderedQuantity` | `Decimal?` | yes |  |
| `PreviousDeliveryDate` | `DateTimeOffset?` | yes |  |
| `SubPartParentRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `QuantityRatio` | `Decimal?` | yes |  |
| `ParentOrderId` | `Int64` | no | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) |
| `RowIndex` | `Int32` | no |  |
| `SumRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `PriceOrigin` | `Int32` | no |  |
| `DiscountIsLockedFromAutomaticChanges` | `Boolean` | no |  |
| `IntrastatTransactionTypeId` | `Int64?` | yes | [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat) |
| `IntrastatTransactionType` | `TransactionTypeIntrastats` | no | [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat) |
| `TariffAndServiceCodeId` | `Int64?` | yes | [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode) |
| `TariffAndServiceCode` | `TariffAndServiceCodes` | no | [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode) |
| `PartConfigurationId` | `Int64?` | yes |  |
| `RowsGoodsLabel` | `String` | no |  |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityPurchaseOrders](Purchase.md#Purchase.OrderQuantityPurchaseOrder) |
| `OrderQuantity` | `OrderQuantityPurchaseOrders` | no | [OrderQuantityPurchaseOrders](Purchase.md#Purchase.OrderQuantityPurchaseOrder) |
| `SupplierDrawingNumber` | `String` | no |  |
| `SupplierRevisionNumber` | `String` | no |  |
| `RowNotes` | `String` | no |  |
| `BlanketOrderPurchaseRowId` | `Int64?` | yes | [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow) |
| `SupplierOrderNumber` | `String` | no |  |
| `SupplierOrderRowPosition` | `String` | no |  |
| `SupplierPartNumber` | `String` | no |  |

- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4
- `PartRowType` — NotPartRow=0, RegularRow=1, SubPartRow=2, SetupPriceRow=3, AlloyCostRow=4, PaymentPlanRow=5, PackagingRow=6
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `PartStatus` — Quote=1, Prototype=2, New=3, Normal=4, NewRevision=5, PhasingOut=6, Expired=9, Inactive=99
- `CreationContext` — OrderRegistration=0, DeliveryReporting=1, Invoicing=2, PartialInvoicing=3
- `ShowFreeTextIn` (bitmask) — Internal=0, Inquiry=1, Order=2, DeliverySchedule=4
- `RowStatus` — Registered=1, PurchaseOrderRowPrinted=2, PartiallyDelivered=5, Declined=8, History=9
- `ReceivingInspectionType` — None=0, Always=1, VariableInspection=2
- `CausingTransType` — StockBalanceRow=0, ReceivedPurchaseOrder=1, PurchaseOrder=2, PurchaseOrderSuggestion=3, ManufactureOrderNode=4, ManufactureOrderNodeSuggestion=5, ManufactureOrderNodeSimulation=6, CustomerOrder=7, SalesForecast=8, CustomerOrderForecast=9, MaterialRequirementFromManufactureOrderNode=10, MaterialRequirementFromManufactureOrderSuggestion=11, MaterialRequirementFromManufactureOrderSimulation=12, Quote=13, MaterialRequirementSuggestionFromQuoteSimulation=14, ArrivingStockOrder=15, DeliveringStockOrder=16, StockOrderArrivalSuggestion=17, StockOrderDeliverySuggestion=18, CustomerOrderFromDeliveryTimeControl=19, MaterialRequirementSuggestionFromDeliveryTimeControl=20, ManufactureOrderNodeFromDeliveryTimeControl=21, PurchaseOrderFromDeliveryTimeControl=22, PurchaseOrderAdvice=23, DeliveringStockOrderFromDeliveryTimeControl=24, CustomerOrderPreliminary=27, CustomerOrderRowMissingDeliveryDate=28, DeliveringStockOrderPreliminary=29, ServiceOrder=30, ReturnTool=33, WithdrawalTool=34, QuotePreliminary=35, QuoteMissingDeliveryDate=36, SalesBlanketOrder=40, PurchaseBlanketOrder=41, ReturnPurchaseOrder=42
- `PriceOrigin` — Undefined=0, UserDefined=1, PriceList=2, PriceListStaggered=3, BusinessPartLink=4, BusinessPartLinkStaggered=5, StandardPrice=6, PartConfiguration=7, PostCalculatedAverage=8, BusinessPartLinkFuturePrice=9

**References out:** [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow), [Codings](Accounting.md#Accounting.Coding), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [OrderQuantityPurchaseOrders](Purchase.md#Purchase.OrderQuantityPurchaseOrder), [Parts](Inventory.md#Inventory.Part), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [ReasonCodes](Common.md#Common.ReasonCode), [Revisions](Common.md#Common.Revision), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode), [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder)

<a id="Purchase.PurchaseOrder"></a>
### PurchaseOrders

Represents a purchase order.

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrders`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PaymentTermDescription` | `String` | no |  |
| `GracePeriodInDays` | `Int32?` | yes |  |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) |
| `DeliveryMethod` | `DeliveryMethods` | no | [DeliveryMethods](Common.md#Common.DeliveryMethod) |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) |
| `DeliveryTerm` | `DeliveryTerms` | no | [DeliveryTerms](Common.md#Common.DeliveryTerm) |
| `DeliveryTermDescription` | `String` | no |  |
| `DeliveryMethodDescription` | `String` | no |  |
| `ShipmentPayer` | `Int32` | no |  |
| `BusinessContactOrderNumber` | `String` | no |  |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `OurReference` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `OurReferenceName` | `String` | no |  |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `BusinessContactReferenceName` | `String` | no |  |
| `GoodsLabel` | `String` | no |  |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) |
| `VatGroup` | `VatGroups` | no | [VatGroups](Common.md#Common.VatGroup) |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `Warehouse` | `Warehouses` | no | [Warehouses](Common.md#Common.Warehouse) |
| `Priority` | `Int32` | no |  |
| `ProjectId` | `Int64?` | yes |  |
| `SendMethod` | `Int32` | no |  |
| `InvoicePrintoutMethod` | `Int32` | no |  |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `TransportTime` | `Int32?` | yes |  |
| `LifeCycleState` | `Int32` | no |  |
| `Version` | `Int32` | no |  |
| `UseForwardRate` | `Boolean` | no |  |
| `ExchangeRate` | `Decimal` | no |  |
| `OrderAmount` | `Decimal` | no |  |
| `OrderAmountInCompanyCurrency` | `Decimal` | no |  |
| `AgentSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `SuppliersQuoteNumber` | `String` | no |  |
| `IsStockOrder` | `Boolean` | no |  |
| `IsConfirmed` | `Boolean` | no |  |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `OrderNumber` | `String` | no |  |
| `OrderDate` | `DateTimeOffset` | no |  |
| `Rows` | `PurchaseOrderRows[]` | no | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `GoodsAddressNumber` | `String` | no |  |
| `FromInquiryNumber` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `InquiryId` | `Int64?` | yes |  |
| `PackingTermId` | `Int64?` | yes | [PackingTerms](Purchase.md#Purchase.PackingTerm) |
| `PackingTerm` | `PackingTerms` | no | [PackingTerms](Purchase.md#Purchase.PackingTerm) |
| `PackingTermDescription` | `String` | no |  |
| `ShowPriceInFormReport` | `Boolean` | no |  |
| `ShowTotalInFormReport` | `Boolean` | no |  |
| `IsCredit` | `Boolean` | no |  |
| `CausingCreditPurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) |
| `BusinessContactId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) |
| `InvoiceBusinessContactId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) |
| `OrderTypeId` | `Int64` | no | [PurchaseOrderTypes](Purchase.md#Purchase.PurchaseOrderType) |
| `OrderType` | `PurchaseOrderTypes` | no | [PurchaseOrderTypes](Purchase.md#Purchase.PurchaseOrderType) |
| `AccountGroupId` | `Int64` | no | [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup) |
| `AccountGroup` | `SupplierAccountGroups` | no | [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup) |
| `CategoryString` | `String` | no |  |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `DestinationForDeliveryTerm` | `String` | no |  |
| `TransportDistance` | `Int32?` | yes |  |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) |

- `ShipmentPayer` — BuyerPays=1, SellerPays=2, OtherPayer=3, Incoterms=4
- `SendMethod` — Printer=0, Email=1, Edi=2, None=9
- `InvoicePrintoutMethod` — Printer=0, Email=1, Edi=2, None=9
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `SourceOfAlternativeDeliveryAddresses` — CurrentCustomer=0, Customer=1, Supplier=2, Company=3, CurrentSupplier=4
- `Status` — PendingAuthorization=0, Registered=1, PurchaseOrderPrinted=2, PartiallyDelivered=5, Declined=8, History=9

**References out:** [Addresses](Common.md#Common.Address), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [PackingTerms](Purchase.md#Purchase.PackingTerm), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [PurchaseOrderTypes](Purchase.md#Purchase.PurchaseOrderType), [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup), [Suppliers](Purchase.md#Purchase.Supplier), [VatGroups](Common.md#Common.VatGroup), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink), [CustomerOrders](Sales.md#Sales.CustomerOrder), [InquiryRows](Purchase.md#Purchase.InquiryRow), [Locations](Inventory.md#Inventory.Location), [ProductRecords](Inventory.md#Inventory.ProductRecord), [PurchaseOrderDeliveries](Purchase.md#Purchase.PurchaseOrderDelivery), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder)

<a id="Purchase.PurchaseOrderType"></a>
### PurchaseOrderTypes

Represents a purchase order type.

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderTypes`
- **Required permission:** Show order types
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Prefix` | `String` | no |  |
| `Description` | `String` | no |  |
| `Priority` | `Int32` | no |  |
| `Visible` | `Boolean` | no |  |
| `IsPreset` | `Boolean` | no |  |
| `IncludeInPurchaseStatistics` | `Boolean` | no |  |
| `BaseType` | `Int32` | no |  |
| `CodingGroupId` | `Int64` | no |  |
| `RateTypeSetting` | `Int32` | no |  |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |

- `BaseType` — Acquisition=0, Subcontract=1, StockOrder=2, ReturnOrder=3, Agreement=4
- `RateTypeSetting` — Supplier=1, OrderType=2

**References out:** [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType)
**Referenced by:** [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder)

<a id="Purchase.ResponseTime"></a>
### ResponseTimes

Represents a response time.

- **Endpoint:** `GET /api/v1/Purchase/ResponseTimes`
- **Required permission:** Show terms
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Days` | `Int32?` | yes |  |
| `Description` | `String` | no |  |
| `Number` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |

**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.SupplierAccountGroup"></a>
### SupplierAccountGroups

Represents a supplier account group.

- **Endpoint:** `GET /api/v1/Purchase/SupplierAccountGroups`
- **Required permission:** Show chart of accounts
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `CompanyIds` | `Int64[]` | no |  |

**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.SupplierAccount"></a>
### SupplierAccounts

Represents a supplier account.

- **Endpoint:** `GET /api/v1/Purchase/SupplierAccounts`
- **Required permission:** Show supplier
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `StandardAccountId` | `Int64?` | yes | [StandardAccounts](Accounting.md#Accounting.StandardAccount) |
| `StandardAccount` | `StandardAccounts` | no | [StandardAccounts](Accounting.md#Accounting.StandardAccount) |
| `CodingEntryId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) |

**References out:** [CodingEntries](Accounting.md#Accounting.CodingEntry), [StandardAccounts](Accounting.md#Accounting.StandardAccount), [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.SupplierDistrict"></a>
### SupplierDistricts

Represents a supplier district.

- **Endpoint:** `GET /api/v1/Purchase/SupplierDistricts`
- **Required permission:** Show supplier
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.SupplierPartLink"></a>
### SupplierPartLinks

Represents a supplier part link.

- **Endpoint:** `GET /api/v1/Purchase/SupplierPartLinks`
- **Required permission:** Show supplier
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) |
| `SupplierPartNumber` | `String` | no |  |
| `PurchaseCommentShowInForms` | `Int32` | no |  |
| `IncludeAlloyCostOnPurchaseOrder` | `Boolean` | no |  |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) |
| `Price` | `Decimal?` | yes |  |
| `SetupPrice` | `Decimal?` | yes |  |
| `LeadTime` | `TimeSpan?` | yes |  |
| `Discount` | `Decimal?` | yes |  |
| `PriceValidThrough` | `DateTimeOffset?` | yes |  |
| `FuturePrice` | `Decimal?` | yes |  |
| `FuturePriceValidThrough` | `DateTimeOffset?` | yes |  |
| `FutureSetupPrice` | `Decimal?` | yes |  |
| `QuantityPerPackage` | `Decimal?` | yes |  |
| `OverridePurchaseCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `OverridePurchaseComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `UnitId` | `Int64` | no | [Units](Common.md#Common.Unit) |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) |
| `PriceCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `PriceCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `PriceComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `Brand` | `String` | no |  |
| `Storage` | `String` | no |  |
| `Dock` | `String` | no |  |
| `IsRemoteConfigured` | `Boolean` | no |  |
| `PartPurchaseExpenseValuesId` | `Int64?` | yes | [PartPurchaseExpenseValues](Inventory.md#Inventory.PartPurchaseExpenseValues) |
| `PartPurchaseExpenseValues` | `PartPurchaseExpenseValues` | no | [PartPurchaseExpenseValues](Inventory.md#Inventory.PartPurchaseExpenseValues) |

- `PurchaseCommentShowInForms` (bitmask) — Internal=0, Inquiry=1, Order=2, DeliverySchedule=4

**References out:** [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [PartPurchaseExpenseValues](Inventory.md#Inventory.PartPurchaseExpenseValues), [Parts](Inventory.md#Inventory.Part), [Suppliers](Purchase.md#Purchase.Supplier), [Units](Common.md#Common.Unit)
**Referenced by:** [PartPlanningInformation](Inventory.md#Inventory.PartPlanningInformation), [Parts](Inventory.md#Inventory.Part), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.Supplier"></a>
### Suppliers

Represents a supplier.

- **Endpoint:** `GET /api/v1/Purchase/Suppliers`
- **Required permission:** Show supplier
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `SupplierCode` | `String` | no |  |
| `Name` | `String` | no |  |
| `AlternativeName` | `String` | no |  |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `CorporationIdentificationNumber` | `String` | no |  |
| `VatNumber` | `String` | no |  |
| `ServiceTaxNumber` | `String` | no |  |
| `PersonalNumber` | `String` | no |  |
| `PackingTermId` | `Int64?` | yes | [PackingTerms](Purchase.md#Purchase.PackingTerm) |
| `PackingTerm` | `PackingTerms` | no | [PackingTerms](Purchase.md#Purchase.PackingTerm) |
| `GracePeriodOrderConfirmation` | `Int32?` | yes |  |
| `GracePeriodDelivery` | `Int32?` | yes |  |
| `InvoiceSupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) |
| `AuthorizedSignerPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `AuthorizedSignerPerson` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `BankIdNumber` | `String` | no |  |
| `CentralBankCode` | `String` | no |  |
| `ResponseTimeId` | `Int64?` | yes | [ResponseTimes](Purchase.md#Purchase.ResponseTime) |
| `ResponseTime` | `ResponseTimes` | no | [ResponseTimes](Purchase.md#Purchase.ResponseTime) |
| `InvoiceBasisException` | `Boolean` | no |  |
| `Role` | `Int32` | no |  |
| `AttachDatafileWithOrder` | `Boolean` | no |  |
| `AttachDatafileWithDeliverySchedule` | `Boolean` | no |  |
| `AttachDatafileWithCase` | `Boolean` | no |  |
| `ReceivingInspectionType` | `Int32` | no |  |
| `ArrivalReportingInstructionId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `ArrivalReportingInstruction` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `UseOCRNumber` | `Boolean` | no |  |
| `UseReferenceNumber` | `Boolean` | no |  |
| `FixedReferenceNumber` | `String` | no |  |
| `EInvoiceId` | `String` | no |  |
| `PurchaseManagerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `PurchaseManager` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `ShippingAgentCode` | `String` | no |  |
| `DefaultBusinessContactBankAccountId` | `Int64?` | yes | [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount) |
| `DefaultBusinessContactBankAccount` | `BusinessContactBankAccounts` | no | [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount) |
| `IsCasualSupplier` | `Boolean` | no |  |
| `ShippingAgentType` | `Int32?` | yes |  |
| `BookTransport` | `Boolean` | no |  |
| `ReturnLabel` | `Boolean` | no |  |
| `ShipmentPrintSetting` | `Int32` | no |  |
| `Url` | `String` | no |  |
| `Discount` | `Decimal?` | yes |  |
| `StatusId` | `Int64` | no | [SupplierStatuses](Purchase.md#Purchase.SupplierStatus) |
| `Status` | `SupplierStatuses` | no | [SupplierStatuses](Purchase.md#Purchase.SupplierStatus) |
| `TypeId` | `Int64?` | yes | [SupplierTypes](Purchase.md#Purchase.SupplierType) |
| `Type` | `SupplierTypes` | no | [SupplierTypes](Purchase.md#Purchase.SupplierType) |
| `DistrictId` | `Int64?` | yes | [SupplierDistricts](Purchase.md#Purchase.SupplierDistrict) |
| `District` | `SupplierDistricts` | no | [SupplierDistricts](Purchase.md#Purchase.SupplierDistrict) |
| `PayViaId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `DateForTransitionToActualContact` | `DateTimeOffset?` | yes |  |
| `PaymentTermId` | `Int64` | no | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `BankGiroNo` | `String` | no |  |
| `EdiCode` | `String` | no |  |
| `DefaultOrderPrintoutVia` | `Int32` | no |  |
| `PlusGiroNo` | `String` | no |  |
| `OurCodeByYou` | `String` | no |  |
| `DiscountCategoryId` | `Int64?` | yes | [DiscountCategories](Common.md#Common.DiscountCategory) |
| `DiscountCategory` | `DiscountCategories` | no | [DiscountCategories](Common.md#Common.DiscountCategory) |
| `ToleranceForEarlyDelivery` | `Int64?` | yes |  |
| `ToleranceForLateDelivery` | `Int64?` | yes |  |
| `Alias` | `String` | no |  |
| `BlockedContextType` | `Int32` | no |  |
| `IsInternal` | `Boolean` | no |  |
| `CompanyId` | `Int64` | no |  |
| `BlockedStatus` | `Int32` | no |  |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |
| `Priority` | `Int32` | no |  |
| `CategoryString` | `String` | no |  |
| `DeliveryInstruction` | `String` | no |  |
| `PaymentMethodId` | `Int64` | no | [PaymentMethods](Common.md#Common.PaymentMethod) |
| `LastChange` | `DateTimeOffset?` | yes |  |
| `PaymentMethod` | `PaymentMethods` | no | [PaymentMethods](Common.md#Common.PaymentMethod) |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) |
| `Language` | `LanguageCodes` | no | [LanguageCodes](Common.md#Common.LanguageCode) |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `VisitingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `VisitingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `BlockMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `BlockMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `DefaultReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `DefaultReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `DeliveryAddressId` | `Int64` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) |
| `DeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) |
| `SupplierPartLinks` | `SupplierPartLinks[]` | no | [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink) |
| `CaseEntries` | `CaseEntry[]` | no | [CaseEntry](Inventory.md#Inventory.CaseEntry) |
| `OtherSupplierNumbers` | `OtherSupplierNumbers[]` | no | [OtherSupplierNumbers](Purchase.md#Purchase.OtherSupplierNumber) |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) |
| `PurchaseAccountId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `PurchaseAccount` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `AccrualAccountingReverseAccountId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `AccrualAccountingReverseAccount` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `OutgoingPaymentsAccountId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `OutgoingPaymentsAccount` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `SupplierAccounts` | `SupplierAccounts[]` | no | [SupplierAccounts](Purchase.md#Purchase.SupplierAccount) |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `RootId` | `Int64` | no |  |
| `References` | `BusinessContactReferences[]` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `ReceivingInspecionFromDate` | `DateTimeOffset?` | yes |  |
| `ReceivingInspecionEndDate` | `DateTimeOffset?` | yes |  |
| `SupplierAccountGroupId` | `Int64` | no | [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup) |
| `IsPrivateSupplier` | `Boolean` | no |  |
| `EORINumber` | `String` | no |  |
| `DeliveryAddresses` | `DeliveryAddresses[]` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) |
| `AllBusinessContactBankAccountOfSupplier` | `BusinessContactBankAccounts[]` | no | [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount) |
| `TinNumber` | `String` | no |  |

- `Role` (bitmask) — MaterialSupplier=1, SubContractor=2, ShippingAgent=4, Miscelaneous=8, CustomsSupplier=16
- `ReceivingInspectionType` — None=0, Always=1, VariableInspection=2
- `ShippingAgentType` — Other=0, DHL=1, Schenker=2, PostNord=3, DSV=4
- `ShipmentPrintSetting` — WaybillAndParcel=0, Waybill=1, Parcel=2
- `DefaultOrderPrintoutVia` — Printer=0, Email=1, Edi=2, None=9
- `BlockedContextType` (bitmask) — None=0, Register=1, Report=2, RegisterSupplierInvoice=4, Payments=8
- `BlockedStatus` — None=0, Message=1, Blocked=2

**References out:** [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CodingEntries](Accounting.md#Accounting.CodingEntry), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [DiscountCategories](Common.md#Common.DiscountCategory), [ExtraFields](Common.md#Common.ExtraField), [LanguageCodes](Common.md#Common.LanguageCode), [OtherSupplierNumbers](Purchase.md#Purchase.OtherSupplierNumber), [PackingTerms](Purchase.md#Purchase.PackingTerm), [PaymentMethods](Common.md#Common.PaymentMethod), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [ResponseTimes](Purchase.md#Purchase.ResponseTime), [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup), [SupplierAccounts](Purchase.md#Purchase.SupplierAccount), [SupplierDistricts](Purchase.md#Purchase.SupplierDistrict), [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink), [Suppliers](Purchase.md#Purchase.Supplier), [SupplierStatuses](Purchase.md#Purchase.SupplierStatus), [SupplierTypes](Purchase.md#Purchase.SupplierType)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [DeliveryMethods](Common.md#Common.DeliveryMethod), [FixedAssets](Accounting.md#Accounting.FixedAsset), [Inquiries](Purchase.md#Purchase.Inquiry), [OtherSupplierNumbers](Purchase.md#Purchase.OtherSupplierNumber), [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment), [PartPurchaseControlDataRows](Inventory.md#Inventory.PartPurchaseControlDataRow), [PriceChangeLogs](Inventory.md#Inventory.PriceChangeLog), [PurchaseOrderAdvices](Purchase.md#Purchase.PurchaseOrderAdvice), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [ShipmentInformationSources](Sales.md#Sales.ShipmentInformationSource), [Shipments](Sales.md#Sales.Shipment), [ShippingServices](Sales.md#Sales.ShippingService), [ShippingTemplates](Sales.md#Sales.ShippingTemplate), [SupplierAccounts](Purchase.md#Purchase.SupplierAccount), [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink), [Suppliers](Purchase.md#Purchase.Supplier), [TransferProfiles](Common.md#Common.TransferProfile)

<a id="Purchase.SupplierStatus"></a>
### SupplierStatuses

Represents a supplier status.

- **Endpoint:** `GET /api/v1/Purchase/SupplierStatuses`
- **Required permission:** Show supplier
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.SupplierType"></a>
### SupplierTypes

Represents a supplier type.

- **Endpoint:** `GET /api/v1/Purchase/SupplierTypes`
- **Required permission:** Show supplier
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)


## Depends on other modules

- [Accounting](Accounting.md): [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [Codings](Accounting.md#Accounting.Coding), [CodingEntries](Accounting.md#Accounting.CodingEntry), [StandardAccounts](Accounting.md#Accounting.StandardAccount)
- [Common](Common.md): [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BlobData](Common.md#Common.BlobData), [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [DiscountCategories](Common.md#Common.DiscountCategory), [ExtraFields](Common.md#Common.ExtraField), [LanguageCodes](Common.md#Common.LanguageCode), [PartialQuantities](Common.md#Common.PartialQuantity), [PaymentMethods](Common.md#Common.PaymentMethod), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [PriceLists](Common.md#Common.PriceList), [Projects](Common.md#Common.Project), [ReasonCodes](Common.md#Common.ReasonCode), [Revisions](Common.md#Common.Revision), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode), [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat), [Units](Common.md#Common.Unit), [VatGroups](Common.md#Common.VatGroup), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse)
- [Inventory](Inventory.md): [CaseEntry](Inventory.md#Inventory.CaseEntry), [Parts](Inventory.md#Inventory.Part), [PartPurchaseExpenseValues](Inventory.md#Inventory.PartPurchaseExpenseValues), [QuantityChanges](Inventory.md#Inventory.QuantityChange)
- [Manufacturing](Manufacturing.md): [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation)
- [Sales](Sales.md): [Customers](Sales.md#Sales.Customer), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow)
