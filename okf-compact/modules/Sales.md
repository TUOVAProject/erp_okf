# Sales

Monitor API module `Sales`: 70 queryable entities, 4 commands, 2 payload types.

## Queryable entities

<a id="Sales.BlanketOrderSales"></a>
### BlanketOrderSales

Represents a blanket order for sales.

- **Endpoint:** `GET /api/v1/Sales/BlanketOrderSales`
- **Required permission:** Show blanket order
- **Introduced in:** 23.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `LifeCycleState` | `Int32` | no |  |
| `OrderNumber` | `String` | no |  |
| `OrderTypeId` | `Int64?` | yes | [BlanketOrderSalesTypes](Sales.md#Sales.BlanketOrderSalesType) |
| `OrderType` | `BlanketOrderSalesTypes` | no | [BlanketOrderSalesTypes](Sales.md#Sales.BlanketOrderSalesType) |
| `BusinessContactId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `BusinessContact` | `Customers` | no | [Customers](Sales.md#Sales.Customer) |
| `CustomersOrderNumber` | `String` | no |  |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `IncludeInNetRequirementCalculation` | `Boolean` | no |  |
| `BusinessContactReferenceName` | `String` | no |  |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `OurReference` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `OurReferenceName` | `String` | no |  |
| `ValidationPeriod` | `Int32` | no |  |
| `ValidFrom` | `DateTimeOffset` | no |  |
| `ValidThrough` | `DateTimeOffset` | no |  |
| `RequirementDate` | `DateTimeOffset` | no |  |
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
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `Seller` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `CurrencyExchangeType` | `CurrencyExchangeTypes` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `Rows` | `BlanketOrderSalesRows[]` | no | [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow) |

- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `ValidationPeriod` — OrderDate=0, DeliveryDate=1
- `Status` — Registered=1, Printed=2, PartiallyCalledOf=7, FullyCalledOf=8, History=9
- `DefaultOrderPrintoutVia` — Printer=0, Email=1, Edi=2, None=9

**References out:** [Addresses](Common.md#Common.Address), [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow), [BlanketOrderSalesTypes](Sales.md#Sales.BlanketOrderSalesType), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [Customers](Sales.md#Sales.Customer), [Persons](Common.md#Common.Person)
**Referenced by:** [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow)

<a id="Sales.BlanketOrderSalesRow"></a>
### BlanketOrderSalesRows

Represents a blanket order row for sales.

- **Endpoint:** `GET /api/v1/Sales/BlanketOrderSalesRows`
- **Required permission:** Show blanket order
- **Introduced in:** 23.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `LifeCycleState` | `Int32` | no |  |
| `ParentOrderId` | `Int64?` | yes | [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales) |
| `ParentRowId` | `Int64?` | yes | [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow) |
| `CustomerPartNumber` | `String` | no |  |
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
| `AlternatePreparationCode` | `String` | no |  |
| `RowsGoodsLabel` | `String` | no |  |

- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4
- `PartRowType` — NotPartRow=0, RegularRow=1, SubPartRow=2, SetupPriceRow=3, AlloyCostRow=4, PaymentPlanRow=5, PackagingRow=6
- `ShowFreeTextIn` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16

**References out:** [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales), [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow), [Currencies](Common.md#Common.Currency), [Parts](Inventory.md#Inventory.Part), [PriceLists](Common.md#Common.PriceList), [Revisions](Common.md#Common.Revision), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales), [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow)

<a id="Sales.BlanketOrderSalesType"></a>
### BlanketOrderSalesTypes

Represents a blanket order type for sales.

- **Endpoint:** `GET /api/v1/Sales/BlanketOrderSalesTypes`
- **Required permission:** Show blanket order
- **Introduced in:** 23.4

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
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `PriceSetting` | `Int32` | no |  |
| `PriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) |
| `RateTypeSetting` | `Int32` | no |  |
| `BlanketOrderSalesActivityTemplateId` | `Int64?` | yes |  |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `DefaultValidDays` | `Int32` | no |  |

- `BaseType` — BlanketOrder=0
- `PriceSetting` — Customer=1, PriceList=2, StandardPrice=3
- `RateTypeSetting` — Customer=1, OrderType=2

**References out:** [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [PriceLists](Common.md#Common.PriceList), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales)

<a id="Sales.BusinessOpportunity"></a>
### BusinessOpportunities

Represents a business opportunity.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunities`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OpportunityNumber` | `String` | no |  |
| `StartDate` | `DateTimeOffset` | no |  |
| `PlannedEndDate` | `DateTimeOffset?` | yes |  |
| `ActualEndDate` | `DateTimeOffset?` | yes |  |
| `BusinessOpportunityGroupId` | `Int64?` | yes | [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup) |
| `BusinessOpportunityGroup` | `BusinessOpportunityGroups` | no | [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup) |
| `BusinessOpportunityCategory` | `String` | no |  |
| `SalesProcessTemplateId` | `Int64?` | yes | [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate) |
| `SalesProcessTemplate` | `SalesProcessTemplates` | no | [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate) |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `OurReference` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `Description` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `Priority` | `Int32` | no |  |
| `BusinessOpportunityTypeId` | `Int64?` | yes | [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType) |
| `BusinessOpportunityType` | `BusinessOpportunityTypes` | no | [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType) |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ReasonLostCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `ReasonLostComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `TotalValue` | `Decimal?` | yes |  |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `Seller` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `Name` | `String` | no |  |
| `ReferenceName` | `String` | no |  |
| `ReasonCodeLostQuoteId` | `Int64?` | yes | [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote) |
| `ReasonCodeLostQuote` | `ReasonCodeLostQuotes` | no | [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote) |
| `BusinessContactNoteHistories` | `BusinessContactNoteHistories[]` | no | [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory) |
| `Customers` | `Customers[]` | no | [Customers](Sales.md#Sales.Customer) |

- `Status` — Registered=1, InProgress=3, Finished=4, Cancelled=5, Pending=6, Historical=9

**References out:** [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory), [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup), [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType), [Comments](Common.md#Common.Comment), [Customers](Sales.md#Sales.Customer), [Persons](Common.md#Common.Person), [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote), [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate)
**Referenced by:** [BusinessOpportunityActivities](Sales.md#Sales.BusinessOpportunityActivity), [BusinessOpportunityReferences](Sales.md#Sales.BusinessOpportunityReference), [BusinessOpportunitySalesProcessSteps](Sales.md#Sales.BusinessOpportunitySalesProcessStep), [Quotes](Sales.md#Sales.Quote)

<a id="Sales.BusinessOpportunityActivity"></a>
### BusinessOpportunityActivities

Represents a business opportunity activity.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityActivities`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OrderId` | `Int64?` | yes | [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity) |
| `RowIndex` | `Int32?` | yes |  |
| `ActivityTypeId` | `Int64?` | yes |  |
| `IsMandatory` | `Boolean` | no |  |
| `IsDueDatePlannedCompletionDate` | `Boolean` | no |  |
| `IsAdministratorResponsibleUser` | `Boolean` | no |  |
| `Description` | `String` | no |  |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `ReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `DueDateType` | `Int32` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `Status` | `Int32` | no |  |
| `NumberDaysFromDueDate` | `Int32?` | yes |  |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |
| `CompletionDate` | `DateTimeOffset?` | yes |  |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `ReminderId` | `Int64?` | yes |  |
| `CalendarAppointmentId` | `String` | no |  |

- `DueDateType` — RegistrationDate=0, ValidThrough=1
- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [Comments](Common.md#Common.Comment), [Customers](Sales.md#Sales.Customer), [Persons](Common.md#Common.Person)

<a id="Sales.BusinessOpportunityActivityTemplateRow"></a>
### BusinessOpportunityActivityTemplateRows

Represents a business opportunity activity template row.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityActivityTemplateRows`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ActivityTemplateId` | `Int64?` | yes | [BusinessOpportunityActivityTemplates](Sales.md#Sales.BusinessOpportunityActivityTemplate) |
| `ActivityTypeId` | `Int64?` | yes | [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType) |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `Code` | `Int64` | no |  |
| `IsAdministratorResponsible` | `Boolean` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `DueDateType` | `Int32` | no |  |
| `NumberDaysFromDueDate` | `Int32` | no |  |
| `Status` | `Int32` | no |  |
| `IsMandatory` | `Boolean` | no |  |
| `IsReminder` | `Boolean` | no |  |
| `IsLoggedUserResponsible` | `Boolean` | no |  |

- `DueDateType` — RegistrationDate=0, ValidThrough=1
- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessOpportunityActivityTemplates](Sales.md#Sales.BusinessOpportunityActivityTemplate), [Comments](Common.md#Common.Comment), [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType)
**Referenced by:** [BusinessOpportunityActivityTemplates](Sales.md#Sales.BusinessOpportunityActivityTemplate)

<a id="Sales.BusinessOpportunityActivityTemplate"></a>
### BusinessOpportunityActivityTemplates

Represents a business opportunity activity template.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityActivityTemplates`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Rows` | `BusinessOpportunityActivityTemplateRows[]` | no | [BusinessOpportunityActivityTemplateRows](Sales.md#Sales.BusinessOpportunityActivityTemplateRow) |

**References out:** [BusinessOpportunityActivityTemplateRows](Sales.md#Sales.BusinessOpportunityActivityTemplateRow)
**Referenced by:** [BusinessOpportunityActivityTemplateRows](Sales.md#Sales.BusinessOpportunityActivityTemplateRow), [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType)

<a id="Sales.BusinessOpportunityGroup"></a>
### BusinessOpportunityGroups

Represents a business opportunity group.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityGroups`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `IsActive` | `Boolean` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType)

<a id="Sales.BusinessOpportunityReference"></a>
### BusinessOpportunityReferences

Represents a business opportunity reference.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityReferences`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `ParentId` | `Int64` | no | [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity) |
| `ShouldFilterLogPosts` | `Boolean` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `ReferenceCode` | `String` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `Remark` | `String` | no |  |
| `ReferenceCategory` | `String` | no |  |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) |

**References out:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Customers](Sales.md#Sales.Customer)

<a id="Sales.BusinessOpportunitySalesProcessStep"></a>
### BusinessOpportunitySalesProcessSteps

Represents a business opportunity sales process step.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunitySalesProcessSteps`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Probability` | `Int32` | no |  |
| `LeadTime` | `Int32` | no |  |
| `Responsibility` | `Int32` | no |  |
| `ResponsibleSellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `ResponsibleSellerGroupId` | `Int64?` | yes | [SellerGroups](Sales.md#Sales.SellerGroup) |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `ParentId` | `Int64?` | yes | [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity) |
| `RowIndex` | `Int32?` | yes |  |
| `Status` | `Int32` | no |  |
| `IsActive` | `Boolean` | no |  |

- `Responsibility` — Seller=0, Group=1
- `Status` — NotStarted=0, Started=1, Finished=2

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [Persons](Common.md#Common.Person), [SellerGroups](Sales.md#Sales.SellerGroup)

<a id="Sales.BusinessOpportunityType"></a>
### BusinessOpportunityTypes

Represents a business opportunity type.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityTypes`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `IsActive` | `Boolean` | no |  |
| `Description` | `String` | no |  |
| `Prefix` | `String` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `Priority` | `Int32` | no |  |
| `BusinessOpportunityGroupId` | `Int64?` | yes | [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup) |
| `BusinessOpportunityGroup` | `BusinessOpportunityGroups` | no | [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup) |
| `ResponsibleSellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `ResponsibleSeller` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `SalesProcessTemplateId` | `Int64?` | yes | [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate) |
| `SalesProcessTemplate` | `SalesProcessTemplates` | no | [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate) |
| `BusinessOpportunityActivityTemplateId` | `Int64?` | yes | [BusinessOpportunityActivityTemplates](Sales.md#Sales.BusinessOpportunityActivityTemplate) |
| `BusinessOpportunityActivityTemplate` | `BusinessOpportunityActivityTemplates` | no | [BusinessOpportunityActivityTemplates](Sales.md#Sales.BusinessOpportunityActivityTemplate) |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |

**References out:** [BusinessOpportunityActivityTemplates](Sales.md#Sales.BusinessOpportunityActivityTemplate), [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup), [Comments](Common.md#Common.Comment), [Persons](Common.md#Common.Person), [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate)
**Referenced by:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity)

<a id="Sales.CountryDocumentSettings"></a>
### CountryDocumentSettings

Represents a country document setting.

- **Endpoint:** `GET /api/v1/Sales/CountryDocumentSettings`
- **Required permission:** Modify settings for file viewer
- **Introduced in:** 26.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `RowIndex` | `Int32?` | yes |  |
| `CountryId` | `Int64` | no | [Countries](Common.md#Common.Country) |
| `ShowInSalesForm` | `Int32` | no |  |
| `ShowCountryOfOrigin` | `Boolean` | no |  |
| `ShowNetWeight` | `Boolean` | no |  |
| `ShowTradeClassificationName` | `Boolean` | no |  |
| `ShowCN` | `Boolean` | no |  |
| `ShowHS` | `Boolean` | no |  |
| `ShowTaric` | `Boolean` | no |  |
| `ShowHTS` | `Boolean` | no |  |
| `ShowNCM` | `Boolean` | no |  |
| `ShowECCN` | `Boolean` | no |  |
| `ShowSITC` | `Boolean` | no |  |
| `AmountExcludedDiscount` | `Boolean` | no |  |
| `TotalByCombCode` | `Int32` | no |  |

- `ShowInSalesForm` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16
- `TotalByCombCode` — CN=0, HS=1, Taric=2, HTS=3, NCM=4, ECCN=5, SITC=6

**References out:** [Countries](Common.md#Common.Country)

<a id="Sales.CustomerAccountGroup"></a>
### CustomerAccountGroups

Represents a customer account group.

- **Endpoint:** `GET /api/v1/Sales/CustomerAccountGroups`
- **Required permission:** Show chart of accounts
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `CompanyIds` | `Int64[]` | no |  |

**Referenced by:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [Countries](Common.md#Common.Country), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [Quotes](Sales.md#Sales.Quote), [SalesAgreements](Sales.md#Sales.SalesAgreement), [SalesForecasts](Inventory.md#Inventory.SalesForecast)

<a id="Sales.CustomerCountryDocumentSettings"></a>
### CustomerCountryDocumentSettings

Represents a customer country document setting.

- **Endpoint:** `GET /api/v1/Sales/CustomerCountryDocumentSettings`
- **Required permission:** Show customer
- **Introduced in:** 26.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `RowIndex` | `Int32?` | yes |  |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `CountryId` | `Int64` | no | [Countries](Common.md#Common.Country) |
| `ShowInSalesForm` | `Int32` | no |  |
| `ShowCountryOfOrigin` | `Boolean?` | yes |  |
| `ShowNetWeight` | `Boolean?` | yes |  |
| `ShowTradeClassificationName` | `Boolean?` | yes |  |
| `ShowCN` | `Boolean?` | yes |  |
| `ShowHS` | `Boolean?` | yes |  |
| `ShowTaric` | `Boolean?` | yes |  |
| `ShowHTS` | `Boolean?` | yes |  |
| `ShowNCM` | `Boolean?` | yes |  |
| `ShowECCN` | `Boolean?` | yes |  |
| `ShowSITC` | `Boolean?` | yes |  |
| `AmountExcludedDiscount` | `Boolean?` | yes |  |
| `TotalByCombCode` | `Int32?` | yes |  |

- `ShowInSalesForm` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16
- `TotalByCombCode` — CN=0, HS=1, Taric=2, HTS=3, NCM=4, ECCN=5, SITC=6

**References out:** [Countries](Common.md#Common.Country), [Customers](Sales.md#Sales.Customer)

<a id="Sales.CustomerDistrict"></a>
### CustomerDistricts

Represents a customer district.

- **Endpoint:** `GET /api/v1/Sales/CustomerDistricts`
- **Required permission:** Show customer
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `CompanyIds` | `Int64[]` | no |  |

**Referenced by:** [Customers](Sales.md#Sales.Customer), [Persons](Common.md#Common.Person), [SalesForecasts](Inventory.md#Inventory.SalesForecast)

<a id="Sales.CustomerEmployeeSpan"></a>
### CustomerEmployeeSpans

Represents a customer employee span.

- **Endpoint:** `GET /api/v1/Sales/CustomerEmployeeSpans`
- **Required permission:** Show customer
- **Introduced in:** 24.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [Customers](Sales.md#Sales.Customer)

<a id="Sales.CustomerOrderActivity"></a>
### CustomerOrderActivities

Represents a customer order activity.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderActivities`
- **Required permission:** Show customer orders
- **Introduced in:** 24.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OrderId` | `Int64` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `ActivityTypeId` | `Int64` | no | [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType) |
| `Description` | `String` | no |  |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |
| `Reminder` | `Boolean?` | yes |  |

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType)

<a id="Sales.CustomerOrderDeliveryRow"></a>
### CustomerOrderDeliveryRows

Represents a customer delivery order row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderDeliveryRows`
- **Required permission:** Show customer orders
- **Introduced in:** 2.36

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AffectStockBalance` | `Boolean` | no |  |
| `BusinessTransactionContextType` | `Int32` | no |  |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `CustomerOrderRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
| `DeliveryDate` | `DateTimeOffset` | no |  |
| `FreeTextHtml` | `String` | no |  |
| `FreeText` | `String` | no |  |
| `InvoiceId` | `Int64?` | yes | [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice) |
| `ParentId` | `Int64?` | yes |  |
| `ParentInvoiceId` | `Int64?` | yes |  |
| `PickListDeliveryDate` | `DateTimeOffset?` | yes |  |
| `QuantityChangeId` | `Int64?` | yes |  |
| `InvoiceRowId` | `Int64?` | yes | [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow) |
| `InvoiceRow` | `CustomerOrderInvoiceRows` | no | [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow) |

- `BusinessTransactionContextType` — NotInitialized=0, ArrivalReporting=1, ManufacturingOrderReporting=2, DeliveryReporting=3, PhysicalInventory=4, UnplannedStockWithdrawal=5, MoveBetweenWarehouse=6, MoveStockBalance=7, NonconformityPosteriorRejection=8, DirectlyRegisteredInvoice=9, RemovalOfPartLocation=10, ManufacturingOrderMaterialReporting=11, UnplannedStockArrivalReporting=12, StockImport=13, DeliveryReportingStockOrder=14, ArrivalReportingStockOrder=15, UndoManufacturingOrderMaterialReporting=16, UndoManufacturingOrderReporting=17, UndoArrivalReporting=18, UndoDeliveryReporting=19, UndoArrivalReportingStockOrder=20, UndoDeliveryReportingStockOrder=21, OutgoingReusable=22, ArrivalReusable=23, UndoOutgoingReusable=24, UndoArrivalReusable=25, ToolWithdrawal=26, ToolReturn=27, CreditSupplierInvoice=28, CreditCustomerInvoice=29, ReturnPurchaseOrder=30, SplitInvoiceBasis=31, CreationOfPartLocation=32, ArrivalsCorrection=33, ArrivalRejection=34, UndoReturnPurchaseOrder=35

**References out:** [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerOrders](Sales.md#Sales.CustomerOrder)
**Referenced by:** [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [InvoiceLogs](Sales.md#Sales.InvoiceLog), [PackageRows](Sales.md#Sales.PackageRow), [ProductRecords](Inventory.md#Inventory.ProductRecord), [SalesPickingListRowQuantities](Sales.md#Sales.SalesPickingListRowQuantity)

<a id="Sales.CustomerOrderInvoiceOrderRowDiscount"></a>
### CustomerOrderInvoiceOrderRowDiscounts

Represents a discount row for a customer order invoice row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderInvoiceOrderRowDiscounts`
- **Required permission:** Show customer orders
- **Introduced in:** 24.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OrderRowId` | `Int64` | no | [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow) |
| `DiscountId` | `Int64?` | yes | [Discounts](Common.md#Common.Discount) |
| `AsPercent` | `Decimal?` | yes |  |
| `DiscountLockedFromAutomaticChanges` | `Boolean` | no |  |
| `AsAmount` | `Decimal?` | yes |  |
| `AsAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `DiscountType` | `Int32` | no |  |
| `GrossPrice` | `Decimal?` | yes |  |
| `GrossPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `NetPrice` | `Decimal?` | yes |  |
| `NetPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `DiscountCalculationType` | `Int32` | no |  |
| `Priority` | `Int32` | no |  |
| `ReplacesDiscountFieldOnOrderRow` | `Boolean` | no |  |

- `DiscountType` — Discount=0, OrderDiscount=1, TotalRowDiscount=2, ProjectDiscount=3, CustomerDiscountOnDiscount=4, OrderTypeDiscount=5, ManualDiscount=99
- `DiscountCalculationType` — Percent=1, Amount=2

**References out:** [Currencies](Common.md#Common.Currency), [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow), [Discounts](Common.md#Common.Discount)
**Referenced by:** [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow)

<a id="Sales.CustomerOrderInvoiceRow"></a>
### CustomerOrderInvoiceRows

Represents a customer order invoice row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderInvoiceRows`
- **Required permission:** Show customer orders
- **Introduced in:** 2.36

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CodingId` | `Int64?` | yes |  |
| `Discount` | `Decimal?` | yes |  |
| `InterestInvoiceBasisId` | `Int64?` | yes |  |
| `LedgerId` | `Int64?` | yes |  |
| `OverrideStandardPrice` | `Decimal?` | yes |  |
| `OverrideStandardPriceCurrencyId` | `Int64?` | yes |  |
| `Price` | `Decimal?` | yes |  |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceIsFuturePrice` | `Boolean?` | yes |  |
| `PriceLockedFromAutomaticChanges` | `Boolean?` | yes |  |
| `PriceOrigin` | `Int32?` | yes |  |
| `PriceOriginPriceListId` | `Int64?` | yes |  |
| `SetupPrice` | `Decimal?` | yes |  |
| `SetupPriceCurrencyId` | `Int64?` | yes |  |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `StandardPrice` | `Decimal?` | yes |  |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) |
| `DiscountRows` | `CustomerOrderInvoiceOrderRowDiscounts[]` | no | [CustomerOrderInvoiceOrderRowDiscounts](Sales.md#Sales.CustomerOrderInvoiceOrderRowDiscount) |

- `PriceOrigin` — Undefined=0, UserDefined=1, PriceList=2, PriceListStaggered=3, BusinessPartLink=4, BusinessPartLinkStaggered=5, StandardPrice=6, PartConfiguration=7, PostCalculatedAverage=8, BusinessPartLinkFuturePrice=9

**References out:** [Currencies](Common.md#Common.Currency), [CustomerOrderInvoiceOrderRowDiscounts](Sales.md#Sales.CustomerOrderInvoiceOrderRowDiscount), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerOrderInvoiceOrderRowDiscounts](Sales.md#Sales.CustomerOrderInvoiceOrderRowDiscount)

<a id="Sales.CustomerOrderInvoice"></a>
### CustomerOrderInvoices

Represents a customer order invoice.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderInvoices`
- **Required permission:** Show customer orders
- **Introduced in:** 2.33

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Status` | `Int32` | no |  |
| `DeliveryNoteNumber` | `Int64` | no |  |
| `DeliveryIndex` | `Int32` | no |  |
| `OrderDeliveryNumber` | `String` | no |  |
| `PickingListId` | `Int64?` | yes |  |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `Version` | `Int32` | no |  |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  |
| `ConsigneeReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `ConsigneeReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `ProformaStatus` | `Int32` | no |  |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `InvoiceAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `InvoiceAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `OurReferenceName` | `String` | no |  |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `BusinessContactReferenceName` | `String` | no |  |
| `GoodsLabel` | `String` | no |  |
| `InvoiceStatusPending` | `Boolean` | no |  |
| `IsPartOfComprehensiveInvoice` | `Boolean` | no |  |
| `ComprehensiveInvoiceGroupingMode` | `Int32` | no |  |
| `HasInvoicingCharge` | `Boolean` | no |  |
| `IsFreeDeliveryMonth` | `Boolean` | no |  |
| `GoodsAddressNumber` | `String` | no |  |
| `VatNumber` | `String` | no |  |
| `Dock` | `String` | no |  |
| `DeliveryInstruction` | `String` | no |  |
| `InvoicePrintoutMethod` | `Int32?` | yes |  |
| `PrintProformaInvoiceVia` | `Int32?` | yes |  |
| `EInvoiceExportMode` | `Int32?` | yes |  |
| `Priority` | `Int32` | no |  |
| `DirectlyRegistered` | `Boolean` | no |  |
| `PartialInvoiceType` | `Int32?` | yes |  |
| `FormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](Common.md#Common.FormReportConfiguration) |
| `DeliveryNoteCreationDate` | `DateTimeOffset?` | yes |  |
| `ExcludeFromEdi` | `Boolean` | no |  |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `ShippingInformationId` | `Int64?` | yes |  |
| `ProformaNumber` | `Int64?` | yes |  |
| `ProformaDate` | `DateTimeOffset?` | yes |  |
| `DestinationForDeliveryTerm` | `String` | no |  |
| `CandidateDebitInvoiceId` | `Int64?` | yes |  |
| `ConsigneeReferenceName` | `String` | no |  |
| `LedgerId` | `Int64?` | yes |  |
| `BusinessContactOrderId` | `Int64` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `InvoiceBusinessContactId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) |
| `AccountGroupId` | `Int64` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `AccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
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
| `DeliveryRows` | `CustomerOrderDeliveryRows[]` | no | [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow) |
| `InvoiceType` | `Int32` | no |  |
| `EditedOrderAmountExcludingVat` | `Decimal?` | yes |  |
| `EditedOrderAmountExcludingVatCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `EditedOrderAmountDiscount` | `Decimal?` | yes |  |
| `TypeOfOrderAmountEntered` | `Int32?` | yes |  |
| `Factoring` | `Boolean` | no |  |

- `Status` — Canceled=0, Registered=1, Preliminary=2, Waiting=3, InvoiceApproved=8, InvoicePrinted=9
- `SourceOfAlternativeDeliveryAddresses` — CurrentCustomer=0, Customer=1, Supplier=2, Company=3, CurrentSupplier=4
- `ProformaStatus` — None=0, ApprovedForPrint=1, Printed=2
- `ComprehensiveInvoiceGroupingMode` — None=0, Customer=1, Order=2, DeliveryNote=3
- `InvoicePrintoutMethod` — Printer=0, Email=1, Edi=2, None=9
- `PrintProformaInvoiceVia` — Printer=0, Email=1, Edi=2, None=9
- `EInvoiceExportMode` — No=0, Yes=1, YesIncludingPrintoutOrEmail=2, SaveToFile=3
- `PartialInvoiceType` — NotInitialized=0, InAdvance=1, Delivery=2, InArrears=3, Text=4
- `ShipmentPayer` — BuyerPays=1, SellerPays=2, OtherPayer=3, Incoterms=4
- `InvoiceType` — Standard=1, Internal=2, CashReceipt=3, Interest=4, OnAccount=5, DebitNote=6, ServiceTax=7, CorrectionInvoice=8, CollectiveCorrectionInvoice=9
- `TypeOfOrderAmountEntered` — Percent=1, Amount=2

**References out:** [Addresses](Common.md#Common.Address), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Currencies](Common.md#Common.Currency), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [FormReportConfigurations](Common.md#Common.FormReportConfiguration), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [Projects](Common.md#Common.Project), [Suppliers](Purchase.md#Purchase.Supplier), [VatGroups](Common.md#Common.VatGroup), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [SalesPickingLists](Sales.md#Sales.SalesPickingList), [ShipmentInformationSources](Sales.md#Sales.ShipmentInformationSource)

<a id="Sales.CustomerOrderOrderRowDiscount"></a>
### CustomerOrderOrderRowDiscounts

Represents a discount row for a customer order row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderOrderRowDiscounts`
- **Required permission:** Show customer orders
- **Introduced in:** 24.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OrderRowId` | `Int64` | no | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
| `DiscountId` | `Int64?` | yes | [Discounts](Common.md#Common.Discount) |
| `AsPercent` | `Decimal?` | yes |  |
| `DiscountLockedFromAutomaticChanges` | `Boolean` | no |  |
| `AsAmount` | `Decimal?` | yes |  |
| `AsAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `DiscountType` | `Int32` | no |  |
| `GrossPrice` | `Decimal?` | yes |  |
| `GrossPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `NetPrice` | `Decimal?` | yes |  |
| `NetPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `DiscountCalculationType` | `Int32` | no |  |
| `Priority` | `Int32` | no |  |
| `ReplacesDiscountFieldOnOrderRow` | `Boolean` | no |  |

- `DiscountType` — Discount=0, OrderDiscount=1, TotalRowDiscount=2, ProjectDiscount=3, CustomerDiscountOnDiscount=4, OrderTypeDiscount=5, ManualDiscount=99
- `DiscountCalculationType` — Percent=1, Amount=2

**References out:** [Currencies](Common.md#Common.Currency), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [Discounts](Common.md#Common.Discount)
**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow)

<a id="Sales.CustomerOrderPaymentPlanRow"></a>
### CustomerOrderPaymentPlanRows

Represents a customer order payment plan row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderPaymentPlanRows`
- **Required permission:** Show customer orders
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CustomerOrderId` | `Int64` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `InvoicingPeriod` | `DateTimeOffset?` | yes |  |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) |
| `Amount` | `Decimal` | no |  |
| `AmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `AmountInCompanyCurrency` | `Decimal` | no |  |
| `AmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `ReducedAmountInCompanyCurrency` | `Decimal?` | yes |  |
| `ReducedAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `IsReset` | `Boolean` | no |  |
| `CodingEntryId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `PartialInvoiceType` | `Int32` | no |  |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `OverrideDescription` | `String` | no |  |
| `FractionOfTotal` | `Decimal` | no |  |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `RowIndex` | `Int32?` | yes |  |

- `PartialInvoiceType` — NotInitialized=0, InAdvance=1, Delivery=2, InArrears=3, Text=4

**References out:** [CodingEntries](Accounting.md#Accounting.CodingEntry), [Currencies](Common.md#Common.Currency), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Parts](Inventory.md#Inventory.Part), [PaymentTerms](Common.md#Common.PaymentTerm), [VatRates](Common.md#Common.VatRate)

<a id="Sales.CustomerOrderRowInflow"></a>
### CustomerOrderRowInflows

Represents a customer order inflow row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderRowInflows`
- **Required permission:** Show customer orders
- **Introduced in:** 23.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OrderRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
| `OrderRow` | `CustomerOrderRows` | no | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
| `BlanketOrderSalesRowId` | `Int64?` | yes |  |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) |
| `EntityIdentityString` | `String` | no |  |
| `AdditionalRowDescription` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  |
| `OrderedQuantityChange` | `Decimal?` | yes |  |
| `UnitId` | `Int64?` | yes |  |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) |
| `PriceChange` | `Decimal?` | yes |  |
| `PriceChangeCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceChangeCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `SetupPriceChange` | `Decimal?` | yes |  |
| `SetupPriceChangeCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPriceChangeCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `DiscountChange` | `Decimal?` | yes |  |
| `TotalValueChange` | `Decimal` | no |  |
| `TotalValueChangeCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `TotalValueChangeCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `OrderRowType` | `Int32` | no |  |

- `Status` — New=0, Changed=1, Removed=2
- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4

**References out:** [Currencies](Common.md#Common.Currency), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [Parts](Inventory.md#Inventory.Part), [Units](Common.md#Common.Unit)

<a id="Sales.CustomerOrderRow"></a>
### CustomerOrderRows

Represents a customer order row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderRows`
- **Required permission:** Show customer orders
- **Introduced in:** 2.18

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
| `ParentRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
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
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes |  |
| `StandardPrice` | `Decimal?` | yes |  |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPrice` | `Decimal?` | yes |  |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
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
| `CustomerCommitmentLevel` | `Int32` | no |  |
| `PickingQuantity` | `Decimal?` | yes |  |
| `AlternatePreparationCode` | `String` | no |  |
| `Storage` | `String` | no |  |
| `ShowFreeTextIn` | `Int32` | no |  |
| `CreateManufacturingOrder` | `Boolean` | no |  |
| `CreatePurchaseOrder` | `Boolean` | no |  |
| `LinkedPurchaseOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `LinkedManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) |
| `LinkedWithdrawalReservationId` | `Int64?` | yes |  |
| `PlannedDateOfArrival` | `DateTimeOffset?` | yes |  |
| `BacklogAmount` | `Decimal` | no |  |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) |
| `RowStatus` | `Int32` | no |  |
| `ParentOrderId` | `Int64` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `Dock` | `String` | no |  |
| `DockName` | `String` | no |  |
| `KanbanNumber` | `String` | no |  |
| `CustomerOrderRowPosition` | `String` | no |  |
| `ReferenceNumberManufacturing` | `String` | no |  |
| `ReferenceNumberDelivery` | `String` | no |  |
| `ShowDeliveryDate` | `Boolean` | no |  |
| `CreatedFrom` | `Int32` | no |  |
| `FixedAssetId` | `Int64?` | yes | [FixedAssets](Accounting.md#Accounting.FixedAsset) |
| `LinkedStockOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `LinkedStockOrderRow` | `PurchaseOrderRows` | no | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) |
| `NewFinishDate` | `DateTimeOffset?` | yes |  |
| `TransferStatus` | `Int32` | no |  |
| `TransferProfileId` | `Int64?` | yes | [TransferProfiles](Common.md#Common.TransferProfile) |
| `OrderNumberInRemoteCompany` | `String` | no |  |
| `PositionInRemoteCompany` | `Int64?` | yes |  |
| `CodingId` | `Int64?` | yes |  |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) |
| `PaymentPlanRowId` | `Int64?` | yes |  |
| `IsCreditedPaymentPlanRow` | `Boolean` | no |  |
| `IsIncludedInPaymentPlan` | `Boolean` | no |  |
| `Status` | `Int32` | no |  |
| `ProformaStatus` | `Int32` | no |  |
| `ProformaNumber` | `Int64?` | yes |  |
| `SubPartParentRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
| `QuantityRatio` | `Decimal?` | yes |  |
| `RowIndex` | `Int32?` | yes |  |
| `SumRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
| `PriceOrigin` | `Int32?` | yes |  |
| `PriceOriginPriceListId` | `Int64?` | yes |  |
| `DiscountIsLockedFromAutomaticChanges` | `Boolean` | no |  |
| `IntrastatTransactionTypeId` | `Int64?` | yes | [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat) |
| `IntrastatTransactionType` | `TransactionTypeIntrastats` | no | [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat) |
| `TariffAndServiceCodeId` | `Int64?` | yes | [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode) |
| `TariffAndServiceCode` | `TariffAndServiceCodes` | no | [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode) |
| `PartConfigurationId` | `Int64?` | yes |  |
| `RowsGoodsLabel` | `String` | no |  |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityCustomerOrders](Sales.md#Sales.OrderQuantityCustomerOrder) |
| `OrderQuantity` | `OrderQuantityCustomerOrders` | no | [OrderQuantityCustomerOrders](Sales.md#Sales.OrderQuantityCustomerOrder) |
| `CustomerOrderTransferRowIdentifier` | `Guid?` | yes |  |
| `PartConfigurationIdInRemoteCompany` | `Int64?` | yes | [PartConfigurations](Common.md#Common.PartConfiguration) |
| `PriceLockedFromAutomaticChanges` | `Boolean?` | yes |  |
| `SerialNumberInformation` | `SerialNumberOrderRowInformation[]` | no |  |
| `DiscountRows` | `CustomerOrderOrderRowDiscounts[]` | no | [CustomerOrderOrderRowDiscounts](Sales.md#Sales.CustomerOrderOrderRowDiscount) |
| `ComparativePrice` | `Decimal?` | yes |  |
| `ComparativePriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `BlanketOrderSalesRowId` | `Int64?` | yes | [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow) |

- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4
- `PartRowType` — NotPartRow=0, RegularRow=1, SubPartRow=2, SetupPriceRow=3, AlloyCostRow=4, PaymentPlanRow=5, PackagingRow=6
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `PartStatus` — Quote=1, Prototype=2, New=3, Normal=4, NewRevision=5, PhasingOut=6, Expired=9, Inactive=99
- `CreationContext` — OrderRegistration=0, DeliveryReporting=1, Invoicing=2, PartialInvoicing=3
- `CustomerCommitmentLevel` — FixedOrder=1, Manufacture=2, BuyMaterial=3, Forecast=4
- `ShowFreeTextIn` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16
- `RowStatus` (bitmask) — OrderConfirmationPrinted=1, DeliveryNotePrinted=2
- `CreatedFrom` — Client=0, M2M=1, EDI=2, DeliverySchedule=3, DeliveryScheduleCallOff=4
- `TransferStatus` — None=0, Partial=1, Fully=2
- `Status` — NotInitialized=0, Registered=1, OrderConfirmationPrinted=2, CanNotConfirmDeliveryTime=3, DeliveryNotePrinted=4, PartiallyDelivered=5, History=9
- `ProformaStatus` — None=0, ApprovedForPrint=1, Printed=2
- `PriceOrigin` — Undefined=0, UserDefined=1, PriceList=2, PriceListStaggered=3, BusinessPartLink=4, BusinessPartLinkStaggered=5, StandardPrice=6, PartConfiguration=7, PostCalculatedAverage=8, BusinessPartLinkFuturePrice=9

**References out:** [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow), [Codings](Accounting.md#Accounting.Coding), [Currencies](Common.md#Common.Currency), [CustomerOrderOrderRowDiscounts](Sales.md#Sales.CustomerOrderOrderRowDiscount), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerOrders](Sales.md#Sales.CustomerOrder), [FixedAssets](Accounting.md#Accounting.FixedAsset), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [OrderQuantityCustomerOrders](Sales.md#Sales.OrderQuantityCustomerOrder), [PartConfigurations](Common.md#Common.PartConfiguration), [Parts](Inventory.md#Inventory.Part), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [Revisions](Common.md#Common.Revision), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode), [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat), [TransferProfiles](Common.md#Common.TransferProfile), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerOrderOrderRowDiscounts](Sales.md#Sales.CustomerOrderOrderRowDiscount), [CustomerOrderRowInflows](Sales.md#Sales.CustomerOrderRowInflow), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerOrders](Sales.md#Sales.CustomerOrder), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [WithdrawalInformationRow](Sales.md#Sales.WithdrawalInformationRow)

<a id="Sales.CustomerOrder"></a>
### CustomerOrders

Represents a customer order.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrders`
- **Required permission:** Show customer orders
- **Introduced in:** 2.18

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
| `ShipmentPayer` | `Int32` | no |  |
| `BusinessContactOrderNumber` | `String` | no |  |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `OurReferenceName` | `String` | no |  |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `BusinessContactReferenceName` | `String` | no |  |
| `GoodsLabel` | `String` | no |  |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
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
| `CustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) |
| `InvoiceCustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) |
| `OrderNumber` | `String` | no |  |
| `OrderDate` | `DateTimeOffset` | no |  |
| `Rows` | `CustomerOrderRows[]` | no | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `ShowPriceInAcknowledgement` | `Boolean` | no |  |
| `ShowTotalInAcknowledgement` | `Boolean` | no |  |
| `ThirdPartyTrading` | `Boolean` | no |  |
| `DeliveryInstruction` | `String` | no |  |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  |
| `IsCredit` | `Boolean` | no |  |
| `InvoiceType` | `Int32` | no |  |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](Common.md#Common.PaymentMethod) |
| `PaymentMethod` | `PaymentMethods` | no | [PaymentMethods](Common.md#Common.PaymentMethod) |
| `PrintoutTimeStamp` | `DateTimeOffset` | no |  |
| `ConsigneeReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `ConsigneeReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `PrintoutBy` | `String` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `Preliminary` | `Boolean` | no |  |
| `ConsigneeReferenceName` | `String` | no |  |
| `DestinationForDeliveryTerm` | `String` | no |  |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `SupplierAccountGroupId` | `Int64?` | yes |  |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `InvoiceAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `InvoiceAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `InvoiceStatusPending` | `Boolean` | no |  |
| `IsPartOfComprehensiveInvoice` | `Boolean` | no |  |
| `ComprehensiveInvoiceGroupingMode` | `Int32` | no |  |
| `HasInvoicingCharge` | `Boolean` | no |  |
| `GoodsAddressNumber` | `String` | no |  |
| `VatNumber` | `String` | no |  |
| `Dock` | `String` | no |  |
| `FromQuoteNumber` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) |
| `PrintProformaInvoiceVia` | `Int32?` | yes |  |
| `OrderTypeId` | `Int64?` | yes | [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType) |
| `OrderType` | `CustomerOrderTypes` | no | [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType) |
| `IsStockOrder` | `Boolean` | no |  |
| `ExcludeFromEdi` | `Boolean` | no |  |
| `IncludeInDeliveryAnalysis` | `Boolean?` | yes |  |
| `PartialDeliveryType` | `Int32` | no |  |
| `DeliveryHorizon` | `TimeSpan?` | yes |  |
| `DeliveryNoteNumberWhenDeliveryPlanning` | `Boolean` | no |  |
| `AftermarketProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) |
| `PurchaseOrder` | `PurchaseOrders` | no | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) |
| `PaymentPlanTemplateId` | `Int64?` | yes | [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate) |
| `PaymentPlanTemplate` | `PaymentPlanTemplates` | no | [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate) |
| `UnpaidAdvanceWarningType` | `Int32` | no |  |
| `CreatedFrom` | `Int32` | no |  |
| `ShippingInformationId` | `Int64?` | yes |  |
| `ShippingInformationRows` | `CustomerOrderShippingInformationRows[]` | no | [CustomerOrderShippingInformationRows](Sales.md#Sales.CustomerOrderShippingInformationRow) |
| `ExcludeFromPaymentPlanReconciliation` | `Boolean` | no |  |
| `ResetPaymentPlanDifferenceAmount` | `Decimal?` | yes |  |
| `ResetPaymentPlanDifferenceAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `ResetPaymentPlanDifferenceAmountCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `TransferStatus` | `Int32` | no |  |
| `CreatedInCompanyWithRole` | `Int32?` | yes |  |
| `AccountGroupId` | `Int64` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `AccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `CategoryString` | `String` | no |  |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `EditedOrderAmountExcludingVat` | `Decimal?` | yes |  |
| `EditedOrderAmountExcludingVatCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `EditedOrderAmountDiscount` | `Decimal?` | yes |  |
| `TypeOfOrderAmountEntered` | `Int32?` | yes |  |
| `ReasonCodeDebitNoteId` | `Int64?` | yes | [ReasonCodeDebitNotes](Common.md#Common.ReasonCodeDebitNote) |
| `ReasonCodeDebitNote` | `ReasonCodeDebitNotes` | no | [ReasonCodeDebitNotes](Common.md#Common.ReasonCodeDebitNote) |
| `Factoring` | `Boolean` | no |  |
| `ReferenceCode` | `String` | no |  |
| `PickInstructionId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `PickInstruction` | `Comments` | no | [Comments](Common.md#Common.Comment) |

- `ShipmentPayer` — BuyerPays=1, SellerPays=2, OtherPayer=3, Incoterms=4
- `SendMethod` — Printer=0, Email=1, Edi=2, None=9
- `InvoicePrintoutMethod` — Printer=0, Email=1, Edi=2, None=9
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `SourceOfAlternativeDeliveryAddresses` — CurrentCustomer=0, Customer=1, Supplier=2, Company=3, CurrentSupplier=4
- `InvoiceType` — Standard=1, Internal=2, CashReceipt=3, Interest=4, OnAccount=5, DebitNote=6, ServiceTax=7, CorrectionInvoice=8, CollectiveCorrectionInvoice=9
- `ComprehensiveInvoiceGroupingMode` — None=0, Customer=1, Order=2, DeliveryNote=3
- `Status` — NotInitialized=0, Registered=1, OrderConfirmationPrinted=2, CanNotConfirmDeliveryTime=3, DeliveryNotePrinted=4, PartiallyDelivered=5, History=9
- `PrintProformaInvoiceVia` — Printer=0, Email=1, Edi=2, None=9
- `PartialDeliveryType` — None=0, PerOrder=1, PerRow=2, NoneDelete=3, PerDeliveryDate=4
- `UnpaidAdvanceWarningType` — NoAlert=0, Warning=1, PreventDelivery=2
- `CreatedFrom` — Client=0, M2M=1, EDI=2, DeliverySchedule=3, DeliveryScheduleCallOff=4
- `TransferStatus` — None=0, Partial=1, Fully=2
- `CreatedInCompanyWithRole` — ManufacturingCompany=0, SalesCompany=1
- `TypeOfOrderAmountEntered` — Percent=1, Amount=2

**References out:** [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerOrderShippingInformationRows](Sales.md#Sales.CustomerOrderShippingInformationRow), [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType), [Customers](Sales.md#Sales.Customer), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [PaymentMethods](Common.md#Common.PaymentMethod), [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [ProductRecords](Inventory.md#Inventory.ProductRecord), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [ReasonCodeDebitNotes](Common.md#Common.ReasonCodeDebitNote), [Suppliers](Purchase.md#Purchase.Supplier), [VatGroups](Common.md#Common.VatGroup), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink), [CustomerOrderActivities](Sales.md#Sales.CustomerOrderActivity), [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrderPaymentPlanRows](Sales.md#Sales.CustomerOrderPaymentPlanRow), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerRelationshipManagementActivities](Sales.md#Sales.CustomerRelationshipManagementActivity), [InvoiceLogs](Sales.md#Sales.InvoiceLog), [Locations](Inventory.md#Inventory.Location), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Projects](Common.md#Common.Project), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [QuoteRows](Sales.md#Sales.QuoteRow), [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [ShipmentInformationSources](Sales.md#Sales.ShipmentInformationSource)

<a id="Sales.CustomerOrderShippingInformationRow"></a>
### CustomerOrderShippingInformationRows

Represents a customer order shipping information row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderShippingInformationRows`
- **Required permission:** Show customer orders
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Quantity` | `Decimal` | no |  |
| `NetWeight` | `Decimal` | no |  |
| `Weight` | `Decimal` | no |  |
| `Volume` | `Decimal` | no |  |
| `LoadingMeters` | `Decimal` | no |  |
| `Length` | `Decimal` | no |  |
| `Width` | `Decimal` | no |  |
| `Height` | `Decimal` | no |  |
| `PackageTypeId` | `Int64` | no | [PackageTypes](Inventory.md#Inventory.PackageType) |
| `PackageType` | `PackageTypes` | no | [PackageTypes](Inventory.md#Inventory.PackageType) |
| `GoodsTypeId` | `Int64` | no | [GoodsTypes](Inventory.md#Inventory.GoodsType) |
| `GoodsType` | `GoodsTypes` | no | [GoodsTypes](Inventory.md#Inventory.GoodsType) |
| `PackagingPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `PackagingPart` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) |
| `ParentId` | `Int64?` | yes |  |

**References out:** [GoodsTypes](Inventory.md#Inventory.GoodsType), [PackageTypes](Inventory.md#Inventory.PackageType), [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [CustomerOrders](Sales.md#Sales.CustomerOrder)

<a id="Sales.CustomerOrderType"></a>
### CustomerOrderTypes

Represents a customer order type.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderTypes`
- **Required permission:** Show order types
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Prefix` | `String` | no |  |
| `Description` | `String` | no |  |
| `Priority` | `Int32` | no |  |
| `Visible` | `Boolean` | no |  |
| `IsPreset` | `Boolean` | no |  |
| `PriceSetting` | `Int32` | no |  |
| `PriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) |
| `IncludeInDeliveryAnalysis` | `Boolean` | no |  |
| `IncludeInStatistics` | `Boolean` | no |  |
| `InvoiceType` | `Int32?` | yes |  |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PurchaseOrderAddressStrategy` | `Int32` | no |  |
| `BaseType` | `Int32` | no |  |
| `CodingGroupId` | `Int64` | no |  |
| `RateTypeSetting` | `Int32` | no |  |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `DefaultTransferProfileId` | `Int64?` | yes | [TransferProfiles](Common.md#Common.TransferProfile) |

- `PriceSetting` — Customer=1, PriceList=2, StandardPrice=3
- `InvoiceType` — Standard=1, Internal=2, CashReceipt=3, Interest=4, OnAccount=5, DebitNote=6, ServiceTax=7, CorrectionInvoice=8, CollectiveCorrectionInvoice=9
- `PurchaseOrderAddressStrategy` — CustomerOrder=0, Company=1
- `BaseType` — NewSales=0, StockOrder=1, Agreement=2
- `RateTypeSetting` — Customer=1, OrderType=2

**References out:** [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [PaymentTerms](Common.md#Common.PaymentTerm), [PriceLists](Common.md#Common.PriceList), [TransferProfiles](Common.md#Common.TransferProfile)
**Referenced by:** [CustomerOrders](Sales.md#Sales.CustomerOrder), [QuoteTypes](Sales.md#Sales.QuoteType)

<a id="Sales.CustomerPartLink"></a>
### CustomerPartLinks

Represents a customer part link.

- **Endpoint:** `GET /api/v1/Sales/CustomerPartLinks`
- **Required permission:** Show customer
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) |
| `CustomerPartNumber` | `String` | no |  |
| `PackagingPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `Gs1Code` | `String` | no |  |
| `SalesCommentShowInForms` | `Int32` | no |  |
| `QuantityForLeadTimeToCustomer` | `Decimal?` | yes |  |
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
| `PickingCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `PickingComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `OverrideSalesCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `OverrideSalesComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `UnitId` | `Int64` | no | [Units](Common.md#Common.Unit) |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) |
| `PriceCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `PriceCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `PriceComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `StaggeredPrices` | `StaggeredPrices[]` | no | [StaggeredPrices](Common.md#Common.StaggeredPrice) |

- `SalesCommentShowInForms` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16

**References out:** [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [Customers](Sales.md#Sales.Customer), [Parts](Inventory.md#Inventory.Part), [StaggeredPrices](Common.md#Common.StaggeredPrice), [Units](Common.md#Common.Unit)
**Referenced by:** [Customers](Sales.md#Sales.Customer), [Parts](Inventory.md#Inventory.Part)

<a id="Sales.CustomerRelationshipActivityType"></a>
### CustomerRelationshipActivityTypes

Represents a customer relationship activity type.

- **Endpoint:** `GET /api/v1/Sales/CustomerRelationshipActivityTypes`
- **Required permission:** Show customer
- **Introduced in:** 2.55

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Sources` | `Int32` | no |  |

- `Sources` (bitmask) — Part=1, Quote=2, CustomerOrder=4, Customer=8, PurchaseOrder=16, Inquiry=32, BlanketOrderPurchase=64, Supplier=128, BlanketOrderSales=256, SalesAgreement=512, PurchaseAgreement=1024, BusinessOpportunity=2048

**Referenced by:** [BusinessOpportunityActivityTemplateRows](Sales.md#Sales.BusinessOpportunityActivityTemplateRow), [CustomerOrderActivities](Sales.md#Sales.CustomerOrderActivity), [CustomerRelationshipManagementActivities](Sales.md#Sales.CustomerRelationshipManagementActivity), [QuoteActivities](Sales.md#Sales.QuoteActivity)

<a id="Sales.CustomerRelationshipManagementActivity"></a>
### CustomerRelationshipManagementActivities

Represents a customer relationship management activity.

- **Endpoint:** `GET /api/v1/Sales/CustomerRelationshipManagementActivities`
- **Required permission:** Show customer
- **Introduced in:** 2.55

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) |
| `IsMandatory` | `Boolean` | no |  |
| `AdministratorType` | `Int32?` | yes |  |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `OrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `ActivityTypeId` | `Int64?` | yes | [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType) |
| `ActivityType` | `CustomerRelationshipActivityTypes` | no | [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType) |
| `CalendarAppointmentId` | `String` | no |  |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `Description` | `String` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `Status` | `Int32` | no |  |
| `ReminderId` | `Int64?` | yes |  |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |
| `CompletionDate` | `DateTimeOffset?` | yes |  |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |
| `IsAdministratorResponsibleUser` | `Boolean` | no |  |
| `IsAdministratorResponsibleUserRestorable` | `Boolean` | no |  |
| `IsDueDatePlannedCompletionDateRestorable` | `Boolean` | no |  |

- `AdministratorType` — CustomerResponsible=0, Seller=1
- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType), [Customers](Sales.md#Sales.Customer)

<a id="Sales.Customer"></a>
### Customers

Represents a customer.

- **Endpoint:** `GET /api/v1/Sales/Customers`
- **Required permission:** Show customer
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `Code` | `String` | no |  |
| `AlternativeName` | `String` | no |  |
| `CorporationIdentificationNumber` | `String` | no |  |
| `PersonalNumber` | `String` | no |  |
| `IsPrivateCustomer` | `Boolean` | no |  |
| `VatNumber` | `String` | no |  |
| `DeliveryAddresses` | `DeliveryAddresses[]` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) |
| `ActiveDeliveryAddressId` | `Int64` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) |
| `ActiveDeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) |
| `References` | `BusinessContactReferences[]` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `DefaultReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `DefaultReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `Alias` | `String` | no |  |
| `AlloyCost` | `Int32` | no |  |
| `ApplyBankCharge` | `Boolean` | no |  |
| `ApplyInvoicingCharge` | `Boolean` | no |  |
| `ApplyReminderCharge` | `Boolean` | no |  |
| `AccountManagerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `AccountManager` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `ActiveDeliveryAddressAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `ActiveDeliveryAddressAccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `ActualCustomerProbabilityId` | `Int64?` | yes | [Probabilities](Common.md#Common.Probability) |
| `ActualCustomerProbability` | `Probabilities` | no | [Probabilities](Common.md#Common.Probability) |
| `AttachDatafileWithOrder` | `Boolean` | no |  |
| `AttachDatafileWithInvoice` | `Boolean` | no |  |
| `AttachDatafileWithCase` | `Boolean` | no |  |
| `AttachDatafileWithPart` | `Boolean` | no |  |
| `AttachDatafileWithDispatchAdvice` | `Boolean` | no |  |
| `BankChargeAmount` | `Decimal` | no |  |
| `BankGiroNo` | `String` | no |  |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `BlockedStatus` | `Int32` | no |  |
| `BlockedContextType` | `Int32` | no |  |
| `BlockMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `BlockMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |
| `CategoryString` | `String` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `CompanyId` | `Int64` | no |  |
| `ConfigurationPriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) |
| `CreditLimit` | `Decimal` | no |  |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `DateDisplayFormat` | `Int32` | no |  |
| `DecimalSymbol` | `String` | no |  |
| `DeliveryHorizon` | `Int64?` | yes |  |
| `DeliveryNoteNumberWhenDeliveryPlanning` | `Boolean` | no |  |
| `DistrictId` | `Int64?` | yes | [CustomerDistricts](Sales.md#Sales.CustomerDistrict) |
| `District` | `CustomerDistricts` | no | [CustomerDistricts](Sales.md#Sales.CustomerDistrict) |
| `DateForTransitionToActualContact` | `DateTimeOffset?` | yes |  |
| `Discount` | `Decimal?` | yes |  |
| `DiscountCategoryId` | `Int64?` | yes | [DiscountCategories](Common.md#Common.DiscountCategory) |
| `DiscountCategory` | `DiscountCategories` | no | [DiscountCategories](Common.md#Common.DiscountCategory) |
| `DefaultOrderPrintoutVia` | `Int32` | no |  |
| `PrintProformaInvoiceVia` | `Int32` | no |  |
| `PrintPaymentReminderVia` | `Int32` | no |  |
| `DeliveryInstruction` | `String` | no |  |
| `DefaultInvoiceStatusPending` | `Boolean` | no |  |
| `EdiCode` | `String` | no |  |
| `EInvoiceElectronicAddressIdentifier` | `String` | no |  |
| `EInvoiceId` | `String` | no |  |
| `EInvoiceOperatorCode` | `String` | no |  |
| `Factoring` | `Boolean` | no |  |
| `GracePeriod` | `TimeSpan?` | yes |  |
| `HideDiscountOnProformaInvoice` | `Boolean` | no |  |
| `IncludeInDeliveryAnalysis` | `Boolean?` | yes |  |
| `InvoiceAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `InvoiceAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `InterestType` | `Int32` | no |  |
| `IsCasualCustomer` | `Boolean` | no |  |
| `InterestInvoiceDays` | `Int32?` | yes |  |
| `InsuranceCost` | `Decimal` | no |  |
| `InvoiceCustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `InvoicePrintoutMethod` | `Int32` | no |  |
| `InvoicePrintoutOccasion` | `Int32` | no |  |
| `IsInternal` | `Boolean` | no |  |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) |
| `Language` | `LanguageCodes` | no | [LanguageCodes](Common.md#Common.LanguageCode) |
| `LatePaymentFee` | `Decimal?` | yes |  |
| `MailingAddressId` | `Int64` | no | [Addresses](Common.md#Common.Address) |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `NumberOfInvoiceCopies` | `Int32?` | yes |  |
| `OurCodeByYou` | `String` | no |  |
| `PalletRegistrationNo` | `String` | no |  |
| `PartialDeliveryType` | `Int32` | no |  |
| `PaymentPlanTemplateId` | `Int64?` | yes | [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate) |
| `PaymentPlanTemplate` | `PaymentPlanTemplates` | no | [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate) |
| `PaymentTermId` | `Int64` | no | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PlusGiroNo` | `String` | no |  |
| `PriceListId` | `Int64` | no | [PriceLists](Common.md#Common.PriceList) |
| `Priority` | `Int32` | no |  |
| `PickingListCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `PickingListComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ProformaInvoicePrintoutOccasion` | `Int32` | no |  |
| `ResellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `Reseller` | `Resellers` | no | [Resellers](Common.md#Common.Reseller) |
| `RoundOff` | `Boolean` | no |  |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `Seller` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `ServiceAgreementId` | `Int64?` | yes |  |
| `ServiceTaxNumber` | `String` | no |  |
| `ShowPartStatisticalGoodsCodeAndCountryOfOriginInForms` | `Int32` | no |  |
| `ShowPartStatisticalGoodsCodeInForms` | `Int32` | no |  |
| `ShowCountryOfOriginInForms` | `Int32` | no |  |
| `ShowPartWeightInForms` | `Int32` | no |  |
| `StatusId` | `Int64` | no | [CustomerStatuses](Sales.md#Sales.CustomerStatus) |
| `Status` | `CustomerStatuses` | no | [CustomerStatuses](Sales.md#Sales.CustomerStatus) |
| `TimeZone` | `String` | no |  |
| `TimeZoneOffset` | `Decimal` | no |  |
| `ToleranceForLateDelivery` | `TimeSpan?` | yes |  |
| `ToleranceForEarlyDelivery` | `TimeSpan?` | yes |  |
| `TypeId` | `Int64?` | yes | [CustomerTypes](Sales.md#Sales.CustomerType) |
| `Type` | `CustomerTypes` | no | [CustomerTypes](Sales.md#Sales.CustomerType) |
| `Url` | `String` | no |  |
| `UseBundling` | `Boolean?` | yes |  |
| `UseComprehensiveInvoices` | `Boolean` | no |  |
| `ComprehensiveInvoiceGroupingMode` | `Int32` | no |  |
| `UseDeliveryNoteCollectionFormReport` | `Boolean` | no |  |
| `UseEInvoicing` | `Boolean` | no |  |
| `UseForwardRate` | `Boolean` | no |  |
| `UseInvoiceCustomersVatNumber` | `Boolean` | no |  |
| `UsePackageSpecification` | `Boolean?` | yes |  |
| `UseReminder` | `Boolean` | no |  |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) |
| `VatRate` | `VatRates` | no | [VatRates](Common.md#Common.VatRate) |
| `ValidityTimeId` | `Int64` | no | [ValidityTimes](Sales.md#Sales.ValidityTime) |
| `ValidityTime` | `ValidityTimes` | no | [ValidityTimes](Sales.md#Sales.ValidityTime) |
| `Version` | `Int32` | no |  |
| `VisitingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `VisitingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `CustomerPartLinks` | `CustomerPartLinks[]` | no | [CustomerPartLinks](Sales.md#Sales.CustomerPartLink) |
| `CaseEntries` | `CaseEntry[]` | no | [CaseEntry](Inventory.md#Inventory.CaseEntry) |
| `OtherCustomerNumbers` | `OtherCustomerNumbers[]` | no | [OtherCustomerNumbers](Sales.md#Sales.OtherCustomerNumber) |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) |
| `PreliminaryPickingList` | `Boolean` | no |  |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `RootId` | `Int64` | no |  |
| `EmployeeSpanId` | `Int64?` | yes |  |
| `EmployeeSpan` | `CustomerEmployeeSpans` | no | [CustomerEmployeeSpans](Sales.md#Sales.CustomerEmployeeSpan) |
| `TinNumber` | `String` | no |  |

- `BlockedStatus` — None=0, Message=1, Blocked=2
- `BlockedContextType` (bitmask) — None=0, Register=1, Report=2, RegisterSupplierInvoice=4, Payments=8
- `DateDisplayFormat` — YYYYMMDD_Dash=1, YYMMDD_Dash=2, DDMMYYYY_Dash=3, DDMMYY_Dash=4, YYYYMMDD_Slash=5, YYMMDD_Slash=6, MMDDYYYY_Slash=7, MMDDYY_Slash=8, MDYY_Slash=9, DDMMYYYY_Slash=10, DDMMYY_Slash=11, DMMYY_Slash=12, YYYYMMDD_Dot=13, DDMMYYYY_Dot=14, DDMMYY_Dot=15, DDMYY_Dot=16, DMMYYYY_Dot=17, DMMYY_Dot=18, DMYYYY_Dot=19, DMYY_Dot=20, YYWWD=21
- `DefaultOrderPrintoutVia` — Printer=0, Email=1, Edi=2, None=9
- `PrintProformaInvoiceVia` — Printer=0, Email=1, Edi=2, None=9
- `PrintPaymentReminderVia` — Printer=0, Email=1, Edi=2, None=9
- `InterestType` — InterestInvoice=0, NextRegularInvoice=1, None=2
- `InvoicePrintoutMethod` — Printer=0, Email=1, Edi=2, None=9
- `InvoicePrintoutOccasion` — AfterDeliveryReport=0, OnDeliveryReportPreliminary=1, OnDeliveryReportDefinite=2
- `PartialDeliveryType` — None=0, PerOrder=1, PerRow=2, NoneDelete=3, PerDeliveryDate=4
- `ProformaInvoicePrintoutOccasion` — AfterDeliveryReport=0, OnDeliveryReport=1
- `ShowPartStatisticalGoodsCodeAndCountryOfOriginInForms` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16
- `ShowPartStatisticalGoodsCodeInForms` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16
- `ShowCountryOfOriginInForms` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16
- `ShowPartWeightInForms` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16
- `ComprehensiveInvoiceGroupingMode` — None=0, Customer=1, Order=2, DeliveryNote=3

**References out:** [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [CaseEntry](Inventory.md#Inventory.CaseEntry), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [CustomerDistricts](Sales.md#Sales.CustomerDistrict), [CustomerEmployeeSpans](Sales.md#Sales.CustomerEmployeeSpan), [CustomerPartLinks](Sales.md#Sales.CustomerPartLink), [Customers](Sales.md#Sales.Customer), [CustomerStatuses](Sales.md#Sales.CustomerStatus), [CustomerTypes](Sales.md#Sales.CustomerType), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [DiscountCategories](Common.md#Common.DiscountCategory), [ExtraFields](Common.md#Common.ExtraField), [LanguageCodes](Common.md#Common.LanguageCode), [OtherCustomerNumbers](Sales.md#Sales.OtherCustomerNumber), [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [PriceLists](Common.md#Common.PriceList), [Probabilities](Common.md#Common.Probability), [Resellers](Common.md#Common.Reseller), [ValidityTimes](Sales.md#Sales.ValidityTime), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales), [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [BusinessOpportunityActivities](Sales.md#Sales.BusinessOpportunityActivity), [BusinessOpportunityReferences](Sales.md#Sales.BusinessOpportunityReference), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CustomerCountryDocumentSettings](Sales.md#Sales.CustomerCountryDocumentSettings), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerPartLinks](Sales.md#Sales.CustomerPartLink), [CustomerRelationshipManagementActivities](Sales.md#Sales.CustomerRelationshipManagementActivity), [Customers](Sales.md#Sales.Customer), [EdiBehaviors](Common.md#Common.EdiBehavior), [FixedAssetSales](Accounting.md#Accounting.FixedAssetSale), [InvoiceLogs](Sales.md#Sales.InvoiceLog), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [OtherCustomerNumbers](Sales.md#Sales.OtherCustomerNumber), [PriceChangeLogs](Inventory.md#Inventory.PriceChangeLog), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Projects](Common.md#Common.Project), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Quotes](Sales.md#Sales.Quote), [SalesAgreements](Sales.md#Sales.SalesAgreement), [SalesForecasts](Inventory.md#Inventory.SalesForecast), [ShipmentInformationSources](Sales.md#Sales.ShipmentInformationSource), [Shipments](Sales.md#Sales.Shipment)

<a id="Sales.CustomerStatus"></a>
### CustomerStatuses

Represents a customer status.

- **Endpoint:** `GET /api/v1/Sales/CustomerStatuses`
- **Required permission:** Show customer
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `CompanyIds` | `Int64[]` | no |  |

**Referenced by:** [Customers](Sales.md#Sales.Customer)

<a id="Sales.CustomerType"></a>
### CustomerTypes

Represents a customer type.

- **Endpoint:** `GET /api/v1/Sales/CustomerTypes`
- **Required permission:** Show customer
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `CompanyIds` | `Int64[]` | no |  |

**Referenced by:** [Customers](Sales.md#Sales.Customer)

<a id="Sales.InvoiceLog"></a>
### InvoiceLogs

Represents an invoice log entry.

- **Endpoint:** `GET /api/v1/Sales/InvoiceLogs`
- **Required permission:** Show customer orders
- **Introduced in:** 2.55

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `InvoiceId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) |
| `LoggingTimestamp` | `DateTimeOffset` | no |  |
| `InvoiceDate` | `DateTimeOffset` | no |  |
| `InvoiceNumber` | `Int64` | no |  |
| `DeliveryRowId` | `Int64?` | yes | [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow) |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `PartNumber` | `String` | no |  |
| `PartCategory` | `String` | no |  |
| `PartCode` | `String` | no |  |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `CustomerCode` | `String` | no |  |
| `CustomerGroup` | `Int64?` | yes |  |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `CustomerOrderNumber` | `String` | no |  |
| `WarehouseId` | `Int64?` | yes | [Warehouses](Common.md#Common.Warehouse) |
| `UserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `UserName` | `String` | no |  |
| `Seller` | `String` | no |  |
| `OrderedQuantity` | `Decimal` | no |  |
| `InvoicedQuantity` | `Decimal` | no |  |
| `UnitCode` | `String` | no |  |
| `Discount` | `Decimal` | no |  |
| `Price` | `Decimal?` | yes |  |
| `SetupPrice` | `Decimal?` | yes |  |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |
| `StandardPrice` | `Decimal?` | yes |  |
| `WeightPerUnit` | `Decimal?` | yes |  |
| `ProductGroupNumber` | `String` | no |  |
| `StatisticalGoodsCode` | `String` | no |  |
| `IntrastatTransactionType` | `Int64?` | yes |  |
| `TariffAndServiceCode` | `String` | no |  |
| `CurrencyCode` | `String` | no |  |
| `ExchangeRate` | `Decimal` | no |  |
| `CustomerOrderCategory` | `String` | no |  |
| `BusinessContactOrderNumber` | `String` | no |  |
| `OrderRowType` | `Int32` | no |  |
| `ConversionFactor` | `Decimal` | no |  |
| `DeliveryIndex` | `Int32` | no |  |
| `FifoPrice` | `Decimal?` | yes |  |
| `ServiceType` | `Int32?` | yes |  |
| `AccountNumber` | `String` | no |  |
| `DeliveryAddressAddressee` | `String` | no |  |
| `IsExportedToManagementAccounting` | `Boolean` | no |  |

- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4

**References out:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [ApplicationUsers](Common.md#Common.ApplicationUser), [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [Parts](Inventory.md#Inventory.Part), [Warehouses](Common.md#Common.Warehouse)

<a id="Sales.OrderQuantityCustomerOrder"></a>
### OrderQuantityCustomerOrders

Represents a order quantity template on part that holds many partial quantities.

- **Endpoint:** `GET /api/v1/Sales/OrderQuantityCustomerOrders`
- **Required permission:** Show purchase orders
- **Introduced in:** 22.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](Common.md#Common.PartialQuantity) |

**References out:** [PartialQuantities](Common.md#Common.PartialQuantity)
**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow)

<a id="Sales.OtherCustomerNumber"></a>
### OtherCustomerNumbers

Represents an alternative customer code mainly used for EDI.

- **Endpoint:** `GET /api/v1/Sales/OtherCustomerNumbers`
- **Required permission:** Show customer
- **Introduced in:** 2.32

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `Number` | `String` | no |  |
| `CustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) |
| `CompanyIds` | `Int64[]` | no |  |

**References out:** [Customers](Sales.md#Sales.Customer)
**Referenced by:** [Customers](Sales.md#Sales.Customer)

<a id="Sales.PackageRowPartLocation"></a>
### PackageRowPartLocations

Represents a package row's location.

- **Endpoint:** `GET /api/v1/Sales/PackageRowPartLocations`
- **Required permission:** Show customer orders
- **Introduced in:** 25.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentPackageRowId` | `Int64` | no | [PackageRows](Sales.md#Sales.PackageRow) |
| `PartLocationId` | `Int64` | no | [PartLocations](Inventory.md#Inventory.PartLocation) |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) |
| `BalanceChange` | `Decimal` | no |  |

**References out:** [PackageRows](Sales.md#Sales.PackageRow), [PartLocations](Inventory.md#Inventory.PartLocation), [ProductRecords](Inventory.md#Inventory.ProductRecord)

<a id="Sales.PackageRow"></a>
### PackageRows

Represents a package row.

- **Endpoint:** `GET /api/v1/Sales/PackageRows`
- **Required permission:** Show customer orders
- **Introduced in:** 25.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64?` | yes | [SalesPickingLists](Sales.md#Sales.SalesPickingList) |
| `ParentRowId` | `Int64?` | yes | [PackageRows](Sales.md#Sales.PackageRow) |
| `CustomerOrderDeliveryRowId` | `Int64?` | yes | [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow) |
| `PackagingPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `Cleared` | `Boolean` | no |  |
| `ContainerNumber` | `String` | no |  |
| `SealNumber` | `String` | no |  |
| `PackageNumber` | `String` | no |  |
| `OtherPackageNumber` | `String` | no |  |
| `OtherPackageNumberNumberSeriesType` | `Int32?` | yes |  |
| `ExternalPackageId` | `String` | no |  |
| `Length` | `Decimal?` | yes |  |
| `Width` | `Decimal?` | yes |  |
| `Height` | `Decimal?` | yes |  |
| `Volume` | `Decimal?` | yes |  |
| `VolumeCalculated` | `Decimal` | no |  |
| `GrossWeight` | `Decimal?` | yes |  |
| `GrossWeightCalculated` | `Decimal` | no |  |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `PackageComplete` | `Boolean` | no |  |
| `BalanceChange` | `Decimal` | no |  |
| `TemplateCode` | `String` | no |  |

- `OtherPackageNumberNumberSeriesType` — NotInitalized=0, CustomerOrderNumber=2, PurchaseOrderNumber=3, AccountsReceivableNumber=4, SupplierCode=5, CustomerCode=6, AccountsPayableNumber=7, InventoryLogPriceId=13, PickingListNumber=14, AccountsReceivableLedgerNumber=15, RejectionLogId=16, ReportNumberForMaterial=17, ReportNumberForOperation=18, ManufacturingOrderNumber=19, AccountsReceivableNumberCashReceipt=20, AccountsReceivableNumberInterest=21, AccountsReceivableNumberInternal=22, AccountsReceivableNumberCredit=23, ProformaInvoiceNumber=24, DeliveryNoteNumber=25, PhysicalInventoryList=27, VoucherNumber=28, AutoCoding=29, AutoAllocation=30, ManufacturingPickingListNumber=31, AccountsReceivableNumberOnAccount=32, IncomingPaymentsBundleNumber=33, AccrualAccountingNumber=34, ShipmentNumber=35, AccountsPayableNumberOnAccount=36, OutgoingPaymentsBundleNumber=37, CaseNumber=38, TransactionList=39, Quote=40, Inquiry=41, Project=43, ProjectCostReportingEntry=44, FixedAsset=45, EdiFileTransaction=46, ServerPrinterNumber=47, AgentTaskNumber=48, MonitoringTaskNumber=49, DeliverySchedule=50, AccountsReceivableNumberDebitNote=51, AccountsReceivableNumberServiceTax=52, CodingMethod=53, TransferTask=54, BlanketOrderPurchase=55, ArrivalNote=56, GS1Code=57, AccountsReceivableNumberCorrectionInvoice=58, PackageNumber=59, MaintenanceReportingServiceNumber=60, BlanketOrderSales=61, AccountingReport=62, VatReport=63, PaymentBundleNumber=64, PackagingTemplateNumber=65, AllocationKeyNumber=66, PurchaseDeliverySchedule=67, SalesAgreement=68, AccountsReceivableNumberAdvance=69, SsccPackage=70, SalesForecast=71, BankAccountReconciliationReport=72, AccountsReceivableNumberCollectiveCorrectionInvoice=73, OscarPackage=74, DunsPackage=75, JipdecPackage=76, AccountsPayableNumberCorrectionInvoice=77, BusinessOpportunity=78, DeliveryNoteSubcontract=79, SupplierAgreement=80

**References out:** [Comments](Common.md#Common.Comment), [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [PackageRows](Sales.md#Sales.PackageRow), [Parts](Inventory.md#Inventory.Part), [SalesPickingLists](Sales.md#Sales.SalesPickingList)
**Referenced by:** [PackageRowPartLocations](Sales.md#Sales.PackageRowPartLocation), [PackageRows](Sales.md#Sales.PackageRow)

<a id="Sales.QuoteActivity"></a>
### QuoteActivities

Represents a quote activity.

- **Endpoint:** `GET /api/v1/Sales/QuoteActivities`
- **Required permission:** Show quote
- **Introduced in:** 24.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `QuoteId` | `Int64` | no | [Quotes](Sales.md#Sales.Quote) |
| `IsMandatory` | `Boolean` | no |  |
| `ActivityTypeId` | `Int64` | no | [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType) |
| `CalendarAppointmentId` | `String` | no |  |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `Description` | `String` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `Status` | `Int32` | no |  |
| `ReminderId` | `Int64?` | yes |  |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  |
| `CompletionDate` | `DateTimeOffset?` | yes |  |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  |
| `ActualStartDate` | `DateTimeOffset?` | yes |  |
| `IsAdministratorResponsibleUser` | `Boolean` | no |  |
| `NumberDaysFromDueDate` | `Int32?` | yes |  |
| `IsDueDatePlannedCompletionDate` | `Boolean` | no |  |
| `DueDateType` | `Int32` | no |  |

- `Status` — Registered=1, InProgress=2, History=9
- `DueDateType` — RegistrationDate=0, ValidThrough=1

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Comments](Common.md#Common.Comment), [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType), [Quotes](Sales.md#Sales.Quote)

<a id="Sales.QuoteOrderRowDiscount"></a>
### QuoteOrderRowDiscounts

Represents a discount row for a quote row.

- **Endpoint:** `GET /api/v1/Sales/QuoteOrderRowDiscounts`
- **Required permission:** Show quote
- **Introduced in:** 24.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OrderRowId` | `Int64` | no | [QuoteRows](Sales.md#Sales.QuoteRow) |
| `DiscountId` | `Int64?` | yes | [Discounts](Common.md#Common.Discount) |
| `AsPercent` | `Decimal?` | yes |  |
| `DiscountLockedFromAutomaticChanges` | `Boolean` | no |  |
| `AsAmount` | `Decimal?` | yes |  |
| `AsAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `DiscountType` | `Int32` | no |  |
| `GrossPrice` | `Decimal?` | yes |  |
| `GrossPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `NetPrice` | `Decimal?` | yes |  |
| `NetPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `DiscountCalculationType` | `Int32` | no |  |
| `Priority` | `Int32` | no |  |
| `ReplacesDiscountFieldOnOrderRow` | `Boolean` | no |  |

- `DiscountType` — Discount=0, OrderDiscount=1, TotalRowDiscount=2, ProjectDiscount=3, CustomerDiscountOnDiscount=4, OrderTypeDiscount=5, ManualDiscount=99
- `DiscountCalculationType` — Percent=1, Amount=2

**References out:** [Currencies](Common.md#Common.Currency), [Discounts](Common.md#Common.Discount), [QuoteRows](Sales.md#Sales.QuoteRow)
**Referenced by:** [QuoteRows](Sales.md#Sales.QuoteRow)

<a id="Sales.QuoteRow"></a>
### QuoteRows

Represents a quote row.

- **Endpoint:** `GET /api/v1/Sales/QuoteRows`
- **Required permission:** Show quote
- **Introduced in:** 2.18

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
| `ParentRowId` | `Int64?` | yes | [QuoteRows](Sales.md#Sales.QuoteRow) |
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
| `AlternatePreparationCode` | `String` | no |  |
| `ShowFreeTextIn` | `Int32` | no |  |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `ExemptFromStatistics` | `Boolean` | no |  |
| `ParentOrderId` | `Int64` | no | [Quotes](Sales.md#Sales.Quote) |
| `CodingId` | `Int64?` | yes |  |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) |
| `RowsGoodsLabel` | `String` | no |  |
| `PartConfigurationId` | `Int64?` | yes |  |
| `RowIndex` | `Int32?` | yes |  |
| `TransferProfileId` | `Int64?` | yes | [TransferProfiles](Common.md#Common.TransferProfile) |
| `PartConfigurationIdInRemoteCompany` | `Int64?` | yes | [PartConfigurations](Common.md#Common.PartConfiguration) |
| `CreateCustomerOrder` | `Boolean` | no |  |
| `DiscountRows` | `QuoteOrderRowDiscounts[]` | no | [QuoteOrderRowDiscounts](Sales.md#Sales.QuoteOrderRowDiscount) |

- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4
- `PartRowType` — NotPartRow=0, RegularRow=1, SubPartRow=2, SetupPriceRow=3, AlloyCostRow=4, PaymentPlanRow=5, PackagingRow=6
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `PartStatus` — Quote=1, Prototype=2, New=3, Normal=4, NewRevision=5, PhasingOut=6, Expired=9, Inactive=99
- `ShowFreeTextIn` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16

**References out:** [Codings](Accounting.md#Accounting.Coding), [Currencies](Common.md#Common.Currency), [CustomerOrders](Sales.md#Sales.CustomerOrder), [PartConfigurations](Common.md#Common.PartConfiguration), [Parts](Inventory.md#Inventory.Part), [QuoteOrderRowDiscounts](Sales.md#Sales.QuoteOrderRowDiscount), [QuoteRows](Sales.md#Sales.QuoteRow), [Quotes](Sales.md#Sales.Quote), [Revisions](Common.md#Common.Revision), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [TransferProfiles](Common.md#Common.TransferProfile), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [QuoteOrderRowDiscounts](Sales.md#Sales.QuoteOrderRowDiscount), [QuoteRows](Sales.md#Sales.QuoteRow), [Quotes](Sales.md#Sales.Quote)

<a id="Sales.Quote"></a>
### Quotes

Represents a quote.

- **Endpoint:** `GET /api/v1/Sales/Quotes`
- **Required permission:** Show quote
- **Introduced in:** 2.18

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
| `ShipmentPayer` | `Int32` | no |  |
| `BusinessContactOrderNumber` | `String` | no |  |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `OurReferenceName` | `String` | no |  |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `BusinessContactReferenceName` | `String` | no |  |
| `GoodsLabel` | `String` | no |  |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
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
| `CustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) |
| `OrderNumber` | `String` | no |  |
| `OrderDate` | `DateTimeOffset?` | yes |  |
| `Rows` | `QuoteRows[]` | no | [QuoteRows](Sales.md#Sales.QuoteRow) |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `VatNumber` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) |
| `QuoteDate` | `DateTimeOffset` | no |  |
| `QuoteDescription` | `String` | no |  |
| `LatestContactDate` | `DateTimeOffset?` | yes |  |
| `RequestForQuoteDate` | `DateTimeOffset` | no |  |
| `ValidityTimeId` | `Int64?` | yes | [ValidityTimes](Sales.md#Sales.ValidityTime) |
| `ValidityTime` | `ValidityTimes` | no | [ValidityTimes](Sales.md#Sales.ValidityTime) |
| `ValidityTimeDescription` | `String` | no |  |
| `ValidityTimeInDays` | `Int32` | no |  |
| `ValidThroughDate` | `DateTimeOffset` | no |  |
| `ProbabilityId` | `Int64` | no | [Probabilities](Common.md#Common.Probability) |
| `Probability` | `Probabilities` | no | [Probabilities](Common.md#Common.Probability) |
| `ReasonCodeLostQuoteId` | `Int64?` | yes | [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote) |
| `ReasonCodeLostQuote` | `ReasonCodeLostQuotes` | no | [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote) |
| `ReasonLostCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `ReasonLostComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `OrderTypeId` | `Int64?` | yes | [QuoteTypes](Sales.md#Sales.QuoteType) |
| `OrderType` | `QuoteTypes` | no | [QuoteTypes](Sales.md#Sales.QuoteType) |
| `Preliminary` | `Boolean` | no |  |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `DeliveryTimeId` | `Int64?` | yes | [DeliveryTimes](Common.md#Common.DeliveryTime) |
| `DeliveryTime` | `DeliveryTimes` | no | [DeliveryTimes](Common.md#Common.DeliveryTime) |
| `DeliveryTimeInDays` | `Int32?` | yes |  |
| `AccountGroupId` | `Int64` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `AccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `CategoryString` | `String` | no |  |
| `DestinationForDeliveryTerm` | `String` | no |  |
| `EditedOrderAmountExcludingVat` | `Decimal?` | yes |  |
| `EditedOrderAmountExcludingVatCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `EditedOrderAmountDiscount` | `Decimal?` | yes |  |
| `TypeOfOrderAmountEntered` | `Int32?` | yes |  |
| `Factoring` | `Boolean` | no |  |
| `BusinessOpportunityId` | `Int64?` | yes | [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity) |
| `BusinessOpportunity` | `BusinessOpportunities` | no | [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity) |
| `RelatedQuotesId` | `Int64?` | yes | [RelatedQuotes](Sales.md#Sales.RelatedQuote) |

- `ShipmentPayer` — BuyerPays=1, SellerPays=2, OtherPayer=3, Incoterms=4
- `SendMethod` — Printer=0, Email=1, Edi=2, None=9
- `InvoicePrintoutMethod` — Printer=0, Email=1, Edi=2, None=9
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `Status` — Registered=1, Printed=2, Closed=6, PartialOrder=7, OrderViaRelatedQuote=8, Order=9
- `TypeOfOrderAmountEntered` — Percent=1, Amount=2

**References out:** [Addresses](Common.md#Common.Address), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [Customers](Sales.md#Sales.Customer), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [DeliveryTimes](Common.md#Common.DeliveryTime), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [Probabilities](Common.md#Common.Probability), [QuoteRows](Sales.md#Sales.QuoteRow), [QuoteTypes](Sales.md#Sales.QuoteType), [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote), [RelatedQuotes](Sales.md#Sales.RelatedQuote), [ValidityTimes](Sales.md#Sales.ValidityTime), [VatGroups](Common.md#Common.VatGroup), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [QuoteActivities](Sales.md#Sales.QuoteActivity), [QuoteRows](Sales.md#Sales.QuoteRow), [RelatedQuoteEntries](Sales.md#Sales.RelatedQuoteEntry)

<a id="Sales.QuoteType"></a>
### QuoteTypes

Represents a quote type.

- **Endpoint:** `GET /api/v1/Sales/QuoteTypes`
- **Required permission:** Show order types
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Prefix` | `String` | no |  |
| `Description` | `String` | no |  |
| `Priority` | `Int32` | no |  |
| `Visible` | `Boolean` | no |  |
| `IsPreset` | `Boolean` | no |  |
| `PriceSetting` | `Int32` | no |  |
| `PriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) |
| `BaseType` | `Int32` | no |  |
| `CodingGroupId` | `Int64` | no |  |
| `FormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](Common.md#Common.FormReportConfiguration) |
| `RateTypeSetting` | `Int32` | no |  |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `CustomerOrderTypeId` | `Int64?` | yes | [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType) |
| `CustomerOrderType` | `CustomerOrderTypes` | no | [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType) |

- `PriceSetting` — Customer=1, PriceList=2, StandardPrice=3
- `BaseType` — Quote=0
- `RateTypeSetting` — Customer=1, OrderType=2

**References out:** [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType), [FormReportConfigurations](Common.md#Common.FormReportConfiguration), [PriceLists](Common.md#Common.PriceList)
**Referenced by:** [Quotes](Sales.md#Sales.Quote)

<a id="Sales.ReasonCodeLostQuote"></a>
### ReasonCodeLostQuotes

Represents a reason code for a lost quote.

- **Endpoint:** `GET /api/v1/Sales/ReasonCodeLostQuotes`
- **Required permission:** Show cause codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `CommentMandatory` | `Boolean` | no |  |
| `Active` | `Boolean` | no |  |

**Referenced by:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [Quotes](Sales.md#Sales.Quote)

<a id="Sales.RelatedQuoteEntry"></a>
### RelatedQuoteEntries

Represents a related quote entry.

- **Endpoint:** `GET /api/v1/Sales/RelatedQuoteEntries`
- **Required permission:** Show quote
- **Introduced in:** 26.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `QuoteId` | `Int64?` | yes | [Quotes](Sales.md#Sales.Quote) |
| `IsPrimary` | `Boolean` | no |  |
| `RelatedQuotesId` | `Int64?` | yes | [RelatedQuotes](Sales.md#Sales.RelatedQuote) |

**References out:** [Quotes](Sales.md#Sales.Quote), [RelatedQuotes](Sales.md#Sales.RelatedQuote)

<a id="Sales.RelatedQuote"></a>
### RelatedQuotes

Represents a placeholder for related quotes.

- **Endpoint:** `GET /api/v1/Sales/RelatedQuotes`
- **Required permission:** Show quote
- **Introduced in:** 26.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |

**Referenced by:** [Quotes](Sales.md#Sales.Quote), [RelatedQuoteEntries](Sales.md#Sales.RelatedQuoteEntry)

<a id="Sales.SalesAgreementBasis"></a>
### SalesAgreementBases

Represents a sales agreement basis.

- **Endpoint:** `GET /api/v1/Sales/SalesAgreementBases`
- **Required permission:** Show agreement
- **Introduced in:** 26.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `SalesAgreementId` | `Int64` | no | [SalesAgreements](Sales.md#Sales.SalesAgreement) |
| `CustomerOrderId` | `Int64` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `InvoiceId` | `Int64?` | yes | [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice) |
| `AccrualAccountId` | `Int64?` | yes | [Accounts](Accounting.md#Accounting.Account) |
| `IsAccrual` | `Boolean` | no |  |
| `IsOneTimeCost` | `Boolean` | no |  |
| `IsRemoved` | `Boolean` | no |  |
| `IsPaused` | `Boolean` | no |  |
| `InvoicingMethod` | `Int32` | no |  |
| `PeriodStart` | `DateTimeOffset` | no |  |
| `PeriodEnd` | `DateTimeOffset` | no |  |
| `PlannedInvoiceDate` | `DateTimeOffset` | no |  |
| `PeriodStartOnAgreementWhenCreated` | `DateTimeOffset?` | yes |  |
| `ExchangeRate` | `Decimal` | no |  |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `UseForwardRate` | `Boolean` | no |  |
| `Rows` | `SalesAgreementBasisRows[]` | no | [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow) |

- `InvoicingMethod` — InAdvance=1, InArrears=2

**References out:** [Accounts](Accounting.md#Accounting.Account), [Currencies](Common.md#Common.Currency), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreements](Sales.md#Sales.SalesAgreement)
**Referenced by:** [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreements](Sales.md#Sales.SalesAgreement)

<a id="Sales.SalesAgreementBasisRow"></a>
### SalesAgreementBasisRows

Represents a sales agreement basis row.

- **Endpoint:** `GET /api/v1/Sales/SalesAgreementBasisRows`
- **Required permission:** Show agreement
- **Introduced in:** 26.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentRowId` | `Int64?` | yes | [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow) |
| `ParentAgreementBasisId` | `Int64` | no | [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis) |
| `AgreementRowId` | `Int64` | no | [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow) |
| `CustomerOrderRowId` | `Int64` | no | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
| `OrderRowType` | `Int32` | no |  |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `EntityIdentityString` | `String` | no |  |
| `AdditionalRowDescription` | `String` | no |  |
| `FreeTextHtml` | `String` | no |  |
| `FreeText` | `String` | no |  |
| `Quantity` | `Decimal` | no |  |
| `ConversionFactor` | `Decimal` | no |  |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) |
| `MileageHours` | `Decimal` | no |  |
| `Price` | `Decimal?` | yes |  |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `Discount` | `Decimal` | no |  |
| `StandardPrice` | `Decimal?` | yes |  |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `StandardPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `Amount` | `Decimal` | no |  |
| `AmountInCompanyCurrency` | `Decimal` | no |  |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) |
| `IsOneTimeCost` | `Boolean` | no |  |
| `PeriodStart` | `DateTimeOffset?` | yes |  |
| `PeriodEnd` | `DateTimeOffset?` | yes |  |

- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4

**References out:** [Currencies](Common.md#Common.Currency), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [Parts](Inventory.md#Inventory.Part), [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow)

<a id="Sales.SalesAgreementRowInflow"></a>
### SalesAgreementRowInflows

Represents a sales agreement inflow row.

- **Endpoint:** `GET /api/v1/Sales/SalesAgreementRowInflows`
- **Required permission:** Show agreement
- **Introduced in:** 26.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CreationTime` | `DateTimeOffset?` | yes |  |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  |
| `OrderRowType` | `Int32` | no |  |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `AdditionalRowDescription` | `String` | no |  |
| `SalesAgreementId` | `Int64?` | yes | [SalesAgreements](Sales.md#Sales.SalesAgreement) |
| `SalesAgreementRowId` | `Int64?` | yes | [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow) |
| `OrderedQuantityChange` | `Decimal?` | yes |  |
| `PriceChange` | `Decimal?` | yes |  |
| `PriceChangeCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceChangeCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `PriceChangeInCompanyCurrency` | `Decimal?` | yes |  |
| `PriceChangeInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceChangeInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `DiscountChange` | `Decimal?` | yes |  |
| `TotalValueChange` | `Decimal` | no |  |
| `TotalValueChangeCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `TotalValueChangeCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `TotalValueChangeInCompanyCurrency` | `Decimal` | no |  |
| `TotalValueChangeInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `TotalValueChangeInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `RowTotalValue` | `Decimal` | no |  |
| `RowTotalValueCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `RowTotalValueCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `RowTotalValueInCompanyCurrency` | `Decimal` | no |  |
| `RowTotalValueInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `RowTotalValueInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `RowTotalQuantity` | `Decimal` | no |  |
| `IsOneTimeCost` | `Boolean` | no |  |
| `SalesAgreementInvoicingInterval` | `Int32` | no |  |
| `TypeOfChange` | `Int32` | no |  |
| `PriceDefinition` | `Int32` | no |  |
| `PriceChangePerInterval` | `Decimal?` | yes |  |
| `PriceChangePerIntervalCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceChangePerIntervalCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `PriceChangePerIntervalInCompanyCurrency` | `Decimal?` | yes |  |
| `PriceChangePerIntervalInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceChangePerIntervalInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `TotalValueChangePerInterval` | `Decimal` | no |  |
| `TotalValueChangePerIntervalInCompanyCurrency` | `Decimal` | no |  |
| `RowTotalValuePerInterval` | `Decimal` | no |  |
| `RowTotalValuePerIntervalInCompanyCurrency` | `Decimal` | no |  |

- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4
- `SalesAgreementInvoicingInterval` — Monthly=1, EveryOtherMonth=2, Quarterly=3, FourMonthly=4, SemiAnnually=5, Annually=6
- `TypeOfChange` — NewRow=0, Upgrade=1, Downgrade=2, Churn=3, PriceChange=4
- `PriceDefinition` — AccordingToInvoicingInterval=0, Day=1, Week=2, Month=3, TwoMonths=4, Quarter=5, FourMonths=6, SixMonths=7, Annual=8

**References out:** [Currencies](Common.md#Common.Currency), [Parts](Inventory.md#Inventory.Part), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow), [SalesAgreements](Sales.md#Sales.SalesAgreement)

<a id="Sales.SalesAgreementRow"></a>
### SalesAgreementRows

Represents an agreement row.

- **Endpoint:** `GET /api/v1/Sales/SalesAgreementRows`
- **Required permission:** Show agreement
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentRowId` | `Int64?` | yes | [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow) |
| `ParentOrderId` | `Int64` | no | [SalesAgreements](Sales.md#Sales.SalesAgreement) |
| `Position` | `Int64?` | yes |  |
| `OrderRowType` | `Int32` | no |  |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `AdditionalRowDescription` | `String` | no |  |
| `Quantity` | `Decimal` | no |  |
| `FutureQuantity` | `Decimal?` | yes |  |
| `PreviousQuantity` | `Decimal?` | yes |  |
| `ConversionFactor` | `Decimal` | no |  |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) |
| `Price` | `Decimal?` | yes |  |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `FuturePriceAmount` | `Decimal?` | yes |  |
| `PreviousPriceAmount` | `Decimal?` | yes |  |
| `Discount` | `Decimal` | no |  |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) |
| `FutureValidFrom` | `DateTimeOffset?` | yes |  |
| `PreviousValidThrough` | `DateTimeOffset?` | yes |  |
| `CustomerPartNumber` | `String` | no |  |
| `PartRowType` | `Int32` | no |  |
| `SetupPrice` | `Decimal?` | yes |  |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `ShowFreeTextIn` | `Int32` | no |  |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) |
| `FreeTextHtml` | `String` | no |  |
| `FreeText` | `String` | no |  |
| `LifeCycleState` | `Int32` | no |  |
| `QuantityRatio` | `Decimal?` | yes |  |
| `CodingId` | `Int64?` | yes | [Codings](Accounting.md#Accounting.Coding) |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |
| `CompensatedRowId` | `Int64?` | yes | [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow) |
| `OneTimeCostType` | `Int32` | no |  |
| `PeriodStart` | `DateTimeOffset?` | yes |  |
| `PeriodEnd` | `DateTimeOffset?` | yes |  |
| `PlannedInvoiceDate` | `DateTimeOffset?` | yes |  |
| `StandardPrice` | `Decimal?` | yes |  |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `FutureDiscount` | `Decimal?` | yes |  |
| `PreviousDiscount` | `Decimal?` | yes |  |
| `IsAccrual` | `Boolean` | no |  |
| `ValidFrom` | `DateTimeOffset?` | yes |  |
| `ValidTo` | `DateTimeOffset?` | yes |  |
| `FuturePriceInCompanyCurrencyAmount` | `Decimal?` | yes |  |
| `PreviousPriceInCompanyCurrencyAmount` | `Decimal?` | yes |  |
| `EntityIdentityString` | `String` | no |  |
| `ExtraFieldBool` | `Boolean` | no |  |
| `ExtraFieldInteger` | `Int32?` | yes |  |
| `ExtraFieldDecimal` | `Decimal?` | yes |  |
| `ExtraFieldDate` | `DateTimeOffset?` | yes |  |
| `ExtraFieldText` | `String` | no |  |

- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4
- `PartRowType` — NotPartRow=0, RegularRow=1, SubPartRow=2, SetupPriceRow=3, AlloyCostRow=4, PaymentPlanRow=5, PackagingRow=6
- `ShowFreeTextIn` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99
- `OneTimeCostType` — No=0, AddToExistingAgreementBasis=1, CreateNewAgreementBasis=2

**References out:** [Codings](Accounting.md#Accounting.Coding), [Currencies](Common.md#Common.Currency), [Parts](Inventory.md#Inventory.Part), [Revisions](Common.md#Common.Revision), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow), [SalesAgreements](Sales.md#Sales.SalesAgreement), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRowInflows](Sales.md#Sales.SalesAgreementRowInflow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow), [SalesAgreements](Sales.md#Sales.SalesAgreement)

<a id="Sales.SalesAgreement"></a>
### SalesAgreements

Represents an agreement.

- **Endpoint:** `GET /api/v1/Sales/SalesAgreements`
- **Required permission:** Show agreement
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OrderNumber` | `String` | no |  |
| `OrderTypeId` | `Int64` | no | [SalesAgreementTypes](Sales.md#Sales.SalesAgreementType) |
| `PeriodStart` | `DateTimeOffset` | no |  |
| `PeriodEnd` | `DateTimeOffset?` | yes |  |
| `AgreementDate` | `DateTimeOffset?` | yes |  |
| `LastNoticeDate` | `DateTimeOffset?` | yes |  |
| `TerminationDate` | `DateTimeOffset?` | yes |  |
| `ExtensionPeriod` | `Int32?` | yes |  |
| `CustomerAgreementNumber` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `ResponsibleId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `BusinessContactId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) |
| `BusinessContactReferenceName` | `String` | no |  |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `OurReferenceName` | `String` | no |  |
| `Description` | `String` | no |  |
| `UseForwardRate` | `Boolean` | no |  |
| `ExchangeRate` | `Decimal` | no |  |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `TermLocation` | `String` | no |  |
| `InvoicingMethod` | `Int32` | no |  |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) |
| `IsAccrual` | `Boolean` | no |  |
| `DefaultOrderPrintoutVia` | `Int32` | no |  |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `InvoiceBusinessContactId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) |
| `AftermarketProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `Priority` | `Int32` | no |  |
| `AccrualAccountId` | `Int64?` | yes | [Accounts](Accounting.md#Accounting.Account) |
| `InvoiceCurrentMonth` | `Boolean` | no |  |
| `InvoicingInterval` | `Int32` | no |  |
| `ComprehensiveInvoiceChoice` | `Int32` | no |  |
| `ReleaseAgreementBasisAutomatically` | `Boolean` | no |  |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PaymentTermDescription` | `String` | no |  |
| `DestinationForDeliveryTerm` | `String` | no |  |
| `GracePeriodInDays` | `Int32?` | yes |  |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) |
| `DeliveryMethodDescription` | `String` | no |  |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) |
| `DeliveryTermDescription` | `String` | no |  |
| `PriceDefinition` | `Int32` | no |  |
| `UpdateStatusAutomatically` | `Boolean` | no |  |
| `Version` | `Int32` | no |  |
| `NoticePeriod` | `Int32` | no |  |
| `PlannedInvoiceDateOffset` | `Int32` | no |  |
| `NumberOfYearsToCreateBasisFor` | `Int32` | no |  |
| `CreateAgreementBasis` | `Boolean` | no |  |
| `Rows` | `SalesAgreementRows[]` | no | [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow) |
| `LifeCycleState` | `Int32` | no |  |
| `Factoring` | `Boolean` | no |  |
| `Bases` | `SalesAgreementBases[]` | no | [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis) |

- `Status` — Negotiation=1, SignedValid=2, Active=3, Terminated=4, Closed=6, Historic=9
- `InvoicingMethod` — InAdvance=1, InArrears=2
- `DefaultOrderPrintoutVia` — Printer=0, Email=1, Edi=2, None=9
- `InvoicingInterval` — Monthly=1, EveryOtherMonth=2, Quarterly=3, FourMonthly=4, SemiAnnually=5, Annually=6
- `ComprehensiveInvoiceChoice` — No=1, PerCustomer=2
- `PriceDefinition` — AccordingToInvoicingInterval=0, Day=1, Week=2, Month=3, TwoMonths=4, Quarter=5, FourMonths=6, SixMonths=7, Annual=8
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99

**References out:** [Accounts](Accounting.md#Accounting.Account), [Addresses](Common.md#Common.Address), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [Customers](Sales.md#Sales.Customer), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Projects](Common.md#Common.Project), [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow), [SalesAgreementTypes](Sales.md#Sales.SalesAgreementType), [VatGroups](Common.md#Common.VatGroup)
**Referenced by:** [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [SalesAgreementRowInflows](Sales.md#Sales.SalesAgreementRowInflow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow)

<a id="Sales.SalesAgreementType"></a>
### SalesAgreementTypes

Represents an agreement type.

- **Endpoint:** `GET /api/v1/Sales/SalesAgreementTypes`
- **Required permission:** Show agreement
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PriceSetting` | `Int32` | no |  |
| `PriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) |
| `Number` | `Int64` | no |  |
| `Prefix` | `String` | no |  |
| `Description` | `String` | no |  |
| `Priority` | `Int32` | no |  |
| `Visible` | `Boolean` | no |  |
| `IsPreset` | `Boolean` | no |  |
| `CodingGroupId` | `Int64` | no |  |
| `UpdateStatusAutomatically` | `Boolean` | no |  |
| `InvoicingMethod` | `Int32` | no |  |
| `PlannedInvoiceDateOffset` | `Int32` | no |  |
| `ReleaseBasisAutomatically` | `Boolean` | no |  |
| `UpwardAdjustmentTriggerType` | `Int32` | no |  |
| `UpwardAdjustmentTriggerValue` | `Int32` | no |  |
| `AgreementValidFromSetting` | `Int32` | no |  |
| `RateTypeSetting` | `Int32` | no |  |

- `PriceSetting` — Customer=1, PriceList=2, StandardPrice=3
- `InvoicingMethod` — InAdvance=1, InArrears=2
- `UpwardAdjustmentTriggerType` — Always=1, Never=2, MinAmountForRow=3, MinAmountForAllRows=4, MinDaysToNextInvoice=5
- `AgreementValidFromSetting` — Today=1, Empty=2
- `RateTypeSetting` — Customer=1, OrderType=2

**References out:** [PriceLists](Common.md#Common.PriceList)
**Referenced by:** [SalesAgreements](Sales.md#Sales.SalesAgreement)

<a id="Sales.SalesPickingListRowQuantity"></a>
### SalesPickingListRowQuantities

Represents sales picking list row quantity information used by the web-client procedure.

- **Endpoint:** `GET /api/v1/Sales/SalesPickingListRowQuantities`
- **Required permission:** Show customer orders
- **Introduced in:** 22.1.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PickingListRowKey` | `String` | no |  |
| `CustomerOrderDeliveryRowId` | `Int64` | no | [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow) |
| `PartLocationId` | `Int64?` | yes | [PartLocations](Inventory.md#Inventory.PartLocation) |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) |
| `Quantity` | `Decimal` | no |  |
| `Included` | `Boolean?` | yes |  |

**References out:** [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [PartLocations](Inventory.md#Inventory.PartLocation), [Parts](Inventory.md#Inventory.Part), [ProductRecords](Inventory.md#Inventory.ProductRecord)

<a id="Sales.SalesPickingList"></a>
### SalesPickingLists

Represents a sales picking list.

- **Endpoint:** `GET /api/v1/Sales/SalesPickingLists`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `PrintedByApplicationUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `PrintedByPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `PrintedTimestamp` | `DateTimeOffset?` | yes |  |
| `State` | `Int32` | no |  |
| `Status` | `Int32` | no |  |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `CustomerOrderInvoices` | `CustomerOrderInvoices[]` | no | [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice) |
| `LifeCycleState` | `Int32` | no |  |

- `State` — Registered=0, ReadyForInvoicing=1
- `Status` — ReadyForDelivery=1, ReadyForDeliveryCreditLimitExceeded=2, ReadyForDeliveryUnpaidAdvance=3, Pending=4, Shortage=5, UnConfirmed=6, Preliminary=7, PreliminaryCreditLimitExceeded=8, PreliminaryUnpaidAdvance=9
- `LifeCycleState` — Transient=1, Persistent=10, History=20, RemovableCandidate=99

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [Persons](Common.md#Common.Person), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [GetWithdrawalInformation](Sales.md#Sales.GetWithdrawalInformation), [PackageRows](Sales.md#Sales.PackageRow), [RemoveSalesPickingList](Sales.md#Sales.RemoveSalesPickingList), [ShipmentInformationSources](Sales.md#Sales.ShipmentInformationSource), [WithdrawalInformationRow](Sales.md#Sales.WithdrawalInformationRow)

<a id="Sales.SalesPrice"></a>
### SalesPrices

Represents a sales price.

- **Endpoint:** `GET /api/v1/Sales/SalesPrices`
- **Required permission:** Show part
- **Introduced in:** 2.34

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) |
| `PriceListId` | `Int64` | no | [PriceLists](Common.md#Common.PriceList) |
| `Price` | `Decimal?` | yes |  |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `SetupPrice` | `Decimal?` | yes |  |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `SetupPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `ValidThrough` | `DateTimeOffset?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `FuturePrice` | `Decimal?` | yes |  |
| `FuturePriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `FuturePriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `FutureSetupPrice` | `Decimal?` | yes |  |
| `FutureSetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `FutureSetupPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `FuturePriceValidThrough` | `DateTimeOffset?` | yes |  |
| `StaggeredPrices` | `StaggeredPrices[]` | no | [StaggeredPrices](Common.md#Common.StaggeredPrice) |

**References out:** [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [Parts](Inventory.md#Inventory.Part), [PriceLists](Common.md#Common.PriceList), [StaggeredPrices](Common.md#Common.StaggeredPrice)

<a id="Sales.SalesProcessStep"></a>
### SalesProcessSteps

Represents a sales process step.

- **Endpoint:** `GET /api/v1/Sales/SalesProcessSteps`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Step` | `String` | no |  |
| `IsActive` | `Boolean` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow)

<a id="Sales.SalesProcessTemplateRow"></a>
### SalesProcessTemplateRows

Represents a sales process template row.

- **Endpoint:** `GET /api/v1/Sales/SalesProcessTemplateRows`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `SalesProcessStepId` | `Int64` | no | [SalesProcessSteps](Sales.md#Sales.SalesProcessStep) |
| `SalesProcessStep` | `SalesProcessSteps` | no | [SalesProcessSteps](Sales.md#Sales.SalesProcessStep) |
| `Probability` | `Int32` | no |  |
| `LeadTime` | `Int32` | no |  |
| `Responsibility` | `Int32` | no |  |
| `ResponsibleSellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `ResponsibleSeller` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `ResponsibleSellerGroupId` | `Int64?` | yes | [SellerGroups](Sales.md#Sales.SellerGroup) |
| `ResponsibleSellerGroup` | `SellerGroups` | no | [SellerGroups](Sales.md#Sales.SellerGroup) |
| `ParentId` | `Int64` | no | [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate) |

- `Responsibility` — Seller=0, Group=1

**References out:** [Persons](Common.md#Common.Person), [SalesProcessSteps](Sales.md#Sales.SalesProcessStep), [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate), [SellerGroups](Sales.md#Sales.SellerGroup)
**Referenced by:** [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate)

<a id="Sales.SalesProcessTemplate"></a>
### SalesProcessTemplates

Represents a sales process template.

- **Endpoint:** `GET /api/v1/Sales/SalesProcessTemplates`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `IsActive` | `Boolean` | no |  |
| `Description` | `String` | no |  |
| `Rows` | `SalesProcessTemplateRows[]` | no | [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow) |

**References out:** [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow)
**Referenced by:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType), [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow)

<a id="Sales.SellerGroup"></a>
### SellerGroups

Represents a seller group.

- **Endpoint:** `GET /api/v1/Sales/SellerGroups`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `IsActive` | `Boolean` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [BusinessOpportunitySalesProcessSteps](Sales.md#Sales.BusinessOpportunitySalesProcessStep), [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow)

<a id="Sales.ShipmentCustoms"></a>
### ShipmentCustoms

Represents a shipments customs information.

- **Endpoint:** `GET /api/v1/Sales/ShipmentCustoms`
- **Required permission:** Show shipment
- **Introduced in:** 26.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no | [Shipments](Sales.md#Sales.Shipment) |
| `Dutiable` | `Boolean` | no |  |
| `InvoiceNumber` | `String` | no |  |
| `InvoiceDate` | `DateTimeOffset?` | yes |  |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `CurrencyExchangeType` | `CurrencyExchangeTypes` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) |
| `DeliveryMethod` | `DeliveryMethods` | no | [DeliveryMethods](Common.md#Common.DeliveryMethod) |
| `ForeignDeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) |
| `ForeignDeliveryMethod` | `DeliveryMethods` | no | [DeliveryMethods](Common.md#Common.DeliveryMethod) |
| `DeclarantId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `Declarant` | `Persons` | no | [Persons](Common.md#Common.Person) |
| `DeclarantName` | `String` | no |  |
| `NumberOfPackages` | `Int32` | no |  |
| `Comment1` | `String` | no |  |
| `Comment2` | `String` | no |  |
| `Comment3` | `String` | no |  |
| `Comment4` | `String` | no |  |
| `TransactionType` | `String` | no |  |
| `PointOfExport` | `String` | no |  |
| `City` | `String` | no |  |
| `Date` | `DateTimeOffset` | no |  |
| `DeclarantCorporationIdentificationNumber` | `String` | no |  |
| `ReferenceNumber` | `String` | no |  |
| `InvoiceType` | `Int32?` | yes |  |
| `ImportExportType` | `Int32?` | yes |  |
| `ImportExportTypeName` | `String` | no |  |
| `ReasonForExport` | `String` | no |  |
| `StatisticalGoodsCodeType` | `Int32` | no |  |
| `EoriSeller` | `String` | no |  |
| `VatNumberSeller` | `String` | no |  |
| `CorporationIdentificationNumberSeller` | `String` | no |  |
| `EoriPickup` | `String` | no |  |
| `EoriPurchaser` | `String` | no |  |
| `VatNumberPurchaser` | `String` | no |  |
| `CorporationIdentificationNumberPurchaser` | `String` | no |  |
| `EoriDelivery` | `String` | no |  |
| `VatNumberDelivery` | `String` | no |  |
| `CorporationIdentificationNumberDelivery` | `String` | no |  |
| `CustomsPayingParty` | `Int32` | no |  |
| `EoriCustomsPayer` | `String` | no |  |
| `CorporationIdentificationNumberCustomsPayer` | `String` | no |  |
| `VatNumberCustomsPayer` | `String` | no |  |
| `CustomsPayer` | `String` | no |  |
| `Rows` | `ShipmentCustomsRows[]` | no | [ShipmentCustomsRows](Sales.md#Sales.ShipmentCustomsRow) |
| `Documents` | `ShipmentCustomsDocuments[]` | no | [ShipmentCustomsDocuments](Sales.md#Sales.ShipmentCustomsDocument) |

- `InvoiceType` — Proforma=1, Commercial=2
- `ImportExportType` — Permanent=1, Temporary=2, Reexport=3
- `StatisticalGoodsCodeType` — CN=0, HS=1, Taric=2, HTS=3, NCM=4, ECCN=5, SITC=6
- `CustomsPayingParty` — BuyerPays=1, SellerPays=2, OtherPayer=3, Incoterms=4

**References out:** [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [DeliveryMethods](Common.md#Common.DeliveryMethod), [Persons](Common.md#Common.Person), [ShipmentCustomsDocuments](Sales.md#Sales.ShipmentCustomsDocument), [ShipmentCustomsRows](Sales.md#Sales.ShipmentCustomsRow), [Shipments](Sales.md#Sales.Shipment)
**Referenced by:** [ShipmentCustomsDocuments](Sales.md#Sales.ShipmentCustomsDocument), [ShipmentCustomsRows](Sales.md#Sales.ShipmentCustomsRow), [Shipments](Sales.md#Sales.Shipment)

<a id="Sales.ShipmentCustomsDocument"></a>
### ShipmentCustomsDocuments

Represents a shipments customs information document.

- **Endpoint:** `GET /api/v1/Sales/ShipmentCustomsDocuments`
- **Required permission:** Show shipment
- **Introduced in:** 26.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no | [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms) |
| `Code` | `String` | no |  |
| `Name` | `String` | no |  |
| `RowIndex` | `Int32?` | yes |  |

**References out:** [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms)
**Referenced by:** [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms)

<a id="Sales.ShipmentCustomsRow"></a>
### ShipmentCustomsRows

Represents a shipments customs information row.

- **Endpoint:** `GET /api/v1/Sales/ShipmentCustomsRows`
- **Required permission:** Show shipment
- **Introduced in:** 26.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no | [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms) |
| `RowIndex` | `Int32?` | yes |  |
| `CountryOfOriginId` | `Int64?` | yes | [Countries](Common.md#Common.Country) |
| `CountryOfOrigin` | `Countries` | no | [Countries](Common.md#Common.Country) |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) |
| `StatisticalGoodsCode` | `StatisticalGoodsCodes` | no | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) |
| `AdditionalCode` | `String` | no |  |
| `Amount` | `Decimal` | no |  |
| `AmountInCompanyCurrency` | `Decimal` | no |  |
| `Content` | `String` | no |  |
| `GrossWeight` | `Decimal?` | yes |  |
| `NetWeight` | `Decimal?` | yes |  |
| `GoodsLabel` | `String` | no |  |
| `OtherQuantity` | `Decimal?` | yes |  |
| `OtherUnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) |
| `OtherUnit` | `Units` | no | [Units](Common.md#Common.Unit) |
| `OtherUnitCode` | `String` | no |  |
| `Procedure` | `String` | no |  |
| `Quantity` | `Int32` | no |  |

**References out:** [Countries](Common.md#Common.Country), [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [Units](Common.md#Common.Unit)
**Referenced by:** [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms)

<a id="Sales.ShipmentInformationSource"></a>
### ShipmentInformationSources

Represents a shipment information source.

- **Endpoint:** `GET /api/v1/Sales/ShipmentInformationSources`
- **Required permission:** Show shipment
- **Introduced in:** 23.1

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ShipmentId` | `Int64?` | yes | [Shipments](Sales.md#Sales.Shipment) |
| `ShipmentInformationSourceType` | `Int32` | no |  |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) |
| `PickingListId` | `Int64?` | yes | [SalesPickingLists](Sales.md#Sales.SalesPickingList) |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `CustomerOrderInvoiceId` | `Int64?` | yes | [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice) |
| `RowIndex` | `Int32` | no |  |

- `ShipmentInformationSourceType` — CustomerOrder=0, Supplier=1, PickingList=2, Customer=3, PickingListWithPackageStructure=4, Subcontract=5, ReturnOrder=6

**References out:** [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [SalesPickingLists](Sales.md#Sales.SalesPickingList), [Shipments](Sales.md#Sales.Shipment), [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation)

<a id="Sales.ShipmentPackageInformationPackageNumber"></a>
### ShipmentPackageInformationPackageNumbers

Represents a shipping agents real package number for a shipment package information.

- **Endpoint:** `GET /api/v1/Sales/ShipmentPackageInformationPackageNumbers`
- **Required permission:** Show shipment
- **Introduced in:** 24.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no | [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation) |
| `ShippingAgentsPackageNumber` | `String` | no |  |

**References out:** [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation)
**Referenced by:** [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation)

<a id="Sales.ShipmentPackageInformation"></a>
### ShipmentPackageInformations

Represents a shipment package information.

- **Endpoint:** `GET /api/v1/Sales/ShipmentPackageInformations`
- **Required permission:** Show shipment
- **Introduced in:** 23.1

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `InformationSourceId` | `Int64?` | yes | [ShipmentInformationSources](Sales.md#Sales.ShipmentInformationSource) |
| `Count` | `Int32` | no |  |
| `PackageTypeName` | `String` | no |  |
| `PackageType` | `Int64?` | yes | [PackageTypes](Inventory.md#Inventory.PackageType) |
| `GoodsTypeName` | `String` | no |  |
| `GoodsType` | `Int64?` | yes | [GoodsTypes](Inventory.md#Inventory.GoodsType) |
| `PackageIdentification` | `String` | no |  |
| `PackageTypeCode` | `String` | no |  |
| `Volume` | `Decimal` | no |  |
| `GrossWeight` | `Decimal` | no |  |
| `LoadingMeters` | `Decimal` | no |  |
| `Length` | `Decimal` | no |  |
| `Width` | `Decimal` | no |  |
| `Height` | `Decimal` | no |  |
| `GoodsLabel` | `String` | no |  |
| `PackageNumber` | `String` | no |  |
| `ShippingAgentsPackageNumbers` | `ShipmentPackageInformationPackageNumbers[]` | no | [ShipmentPackageInformationPackageNumbers](Sales.md#Sales.ShipmentPackageInformationPackageNumber) |
| `ShipmentId` | `Int64?` | yes | [Shipments](Sales.md#Sales.Shipment) |
| `RowIndex` | `Int32?` | yes |  |

**References out:** [GoodsTypes](Inventory.md#Inventory.GoodsType), [PackageTypes](Inventory.md#Inventory.PackageType), [ShipmentInformationSources](Sales.md#Sales.ShipmentInformationSource), [ShipmentPackageInformationPackageNumbers](Sales.md#Sales.ShipmentPackageInformationPackageNumber), [Shipments](Sales.md#Sales.Shipment)
**Referenced by:** [ShipmentPackageInformationPackageNumbers](Sales.md#Sales.ShipmentPackageInformationPackageNumber)

<a id="Sales.Shipment"></a>
### Shipments

Represents a shipment.

- **Endpoint:** `GET /api/v1/Sales/Shipments`
- **Required permission:** Show shipment
- **Introduced in:** 23.1

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ShipmentNumber` | `String` | no |  |
| `ConsignmentNo` | `String` | no |  |
| `UnifaunOnlineFirstParcelNo` | `String` | no |  |
| `UnifaunOnlineFirstPrintLink` | `String` | no |  |
| `LogTradeTrackingNo` | `String` | no |  |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) |
| `DeliveryTermStandardCode` | `String` | no |  |
| `DeliveryTermLocation` | `String` | no |  |
| `ShippingAgentType` | `Int32` | no |  |
| `ShipmentPayer` | `Int32` | no |  |
| `ShipmentPayerReference` | `String` | no |  |
| `TransportDate` | `DateTimeOffset` | no |  |
| `StoredShipment` | `Boolean` | no |  |
| `PickupDate` | `DateTimeOffset?` | yes |  |
| `PickupTimeFrom` | `DateTimeOffset?` | yes |  |
| `PickupTimeTo` | `DateTimeOffset?` | yes |  |
| `ExportDate` | `DateTimeOffset?` | yes |  |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |
| `DeliveryTime` | `DateTimeOffset?` | yes |  |
| `PickupText1` | `String` | no |  |
| `PickupMisc` | `String` | no |  |
| `SchenkerOpalNumber` | `String` | no |  |
| `IsConsolidated` | `Boolean` | no |  |
| `ConsolidateKey` | `String` | no |  |
| `TotalEurPallets` | `Int32` | no |  |
| `CurrentInformationSourceType` | `Int32` | no |  |
| `Status` | `Int32` | no |  |
| `ShippingAgentId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) |
| `RecipientAdressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `RecipientAdress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `RecipientInvoiceAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `RecipientInvoiceAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `FreightPayerAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `FreightPayerAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `ConsignmentId` | `String` | no |  |
| `ConsignmentIdForReturn` | `String` | no |  |
| `OurReferenceName` | `String` | no |  |
| `OurReferencePhoneNumber` | `String` | no |  |
| `OurReferenceMobilePhoneNumber` | `String` | no |  |
| `OurReferenceMail` | `String` | no |  |
| `OurPickUpAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `OurPickUpAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `OurInvoiceAdressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) |
| `OurInvoiceAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) |
| `PalletRegistrationNo` | `String` | no |  |
| `OurPalletRegistrationNo` | `String` | no |  |
| `BusinessContactReferenceName` | `String` | no |  |
| `BusinessContactReferencePhoneNumber` | `String` | no |  |
| `BusinessContactReferenceMobilePhoneNumber` | `String` | no |  |
| `BusinessContactReferenceMail` | `String` | no |  |
| `ShippingTemplate` | `String` | no |  |
| `ShippingTemplateId` | `Int64?` | yes | [ShippingTemplates](Sales.md#Sales.ShippingTemplate) |
| `ShippingServiceId` | `Int64?` | yes | [ShippingServices](Sales.md#Sales.ShippingService) |
| `ShippingService` | `ShippingServices` | no | [ShippingServices](Sales.md#Sales.ShippingService) |
| `ShippingServiceCode` | `String` | no |  |
| `SenderQuickId` | `String` | no |  |
| `SellerQuickId` | `String` | no |  |
| `ConsignorId` | `String` | no |  |
| `PickupId` | `String` | no |  |
| `LogTradePrintQueue` | `String` | no |  |
| `ShippingAgentCode` | `String` | no |  |
| `SenderReference` | `String` | no |  |
| `RecipientReference` | `String` | no |  |
| `DeliveryInstruction` | `String` | no |  |
| `BookTransport` | `Boolean` | no |  |
| `ReturnLabel` | `Boolean` | no |  |
| `ShipmentPrintSetting` | `Int32` | no |  |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  |
| `ActiveDeliveryAddressDeliveryAddressId` | `Int64?` | yes | [DeliveryAddresses](Common.md#Common.DeliveryAddress) |
| `ActiveDeliveryAddressDeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) |
| `ActiveFallbackDeliveryAddressDeliveryAddressId` | `Int64?` | yes | [DeliveryAddresses](Common.md#Common.DeliveryAddress) |
| `ActiveFallbackDeliveryAddressDeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  |
| `WarehouseShippingAgentCode` | `String` | no |  |
| `CustomerGoodsAddressNumber` | `String` | no |  |
| `CustomerShippingAgentCode` | `String` | no |  |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `ShippingAgentAccountName` | `String` | no |  |
| `CalculatedFreightPrice` | `Decimal?` | yes |  |
| `CalculatedFreightPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `CalculatedFreightPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) |
| `MobilePhoneNotificationNumber` | `String` | no |  |
| `GoodsTrackingUrl` | `String` | no |  |
| `CustomsId` | `Int64?` | yes |  |
| `Customs` | `ShipmentCustoms` | no | [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms) |

- `ShippingAgentType` — Other=0, DHL=1, Schenker=2, PostNord=3, DSV=4
- `ShipmentPayer` — BuyerPays=1, SellerPays=2, OtherPayer=3, Incoterms=4
- `CurrentInformationSourceType` — CustomerOrder=0, Supplier=1, PickingList=2, Customer=3, PickingListWithPackageStructure=4, Subcontract=5, ReturnOrder=6
- `Status` — Registered=1, ShipmentFailed=2, ShipmentInformationNotSufficient=3, Sent=4, Booked=5, Shipped=6, Cancelled=7
- `ShipmentPrintSetting` — WaybillAndParcel=0, Waybill=1, Parcel=2
- `SourceOfAlternativeDeliveryAddresses` — CurrentCustomer=0, Customer=1, Supplier=2, Company=3, CurrentSupplier=4

**References out:** [Addresses](Common.md#Common.Address), [Currencies](Common.md#Common.Currency), [Customers](Sales.md#Sales.Customer), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms), [ShippingServices](Sales.md#Sales.ShippingService), [ShippingTemplates](Sales.md#Sales.ShippingTemplate), [Suppliers](Purchase.md#Purchase.Supplier), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms), [ShipmentInformationSources](Sales.md#Sales.ShipmentInformationSource), [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation)

<a id="Sales.ShippingService"></a>
### ShippingServices

Represents a shipping service.

- **Endpoint:** `GET /api/v1/Sales/ShippingServices`
- **Required permission:** Show shipment
- **Introduced in:** 23.1

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `Code` | `String` | no |  |
| `LogTradePrintQueue` | `String` | no |  |
| `SchenkerOpalNumber` | `String` | no |  |
| `ConsolidatedShipment` | `Boolean` | no |  |
| `StoredShipment` | `Boolean` | no |  |
| `UseSellerAddress` | `Boolean` | no |  |
| `UsePurchaserAddress` | `Boolean` | no |  |
| `UseFrieghtPayerAddress` | `Boolean` | no |  |
| `ShippingTemplateId` | `Int64?` | yes | [ShippingTemplates](Sales.md#Sales.ShippingTemplate) |
| `SenderQuickId` | `String` | no |  |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `SellerQuickId` | `String` | no |  |

**References out:** [ShippingTemplates](Sales.md#Sales.ShippingTemplate), [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [Shipments](Sales.md#Sales.Shipment)

<a id="Sales.ShippingTemplate"></a>
### ShippingTemplates

Represents a shipping service.

- **Endpoint:** `GET /api/v1/Sales/ShippingTemplates`
- **Required permission:** Show shipment
- **Introduced in:** 23.1

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ShippingTemplateName` | `String` | no |  |
| `ShippingTemplateCode` | `String` | no |  |
| `ExportPickupAddress` | `Boolean` | no |  |
| `ExportDeliveryAddress` | `Boolean` | no |  |
| `ConsignorId` | `String` | no |  |
| `PickupId` | `String` | no |  |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |

**References out:** [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [Shipments](Sales.md#Sales.Shipment), [ShippingServices](Sales.md#Sales.ShippingService)

<a id="Sales.ValidityTime"></a>
### ValidityTimes

Represents a validity time.

- **Endpoint:** `GET /api/v1/Sales/ValidityTimes`
- **Required permission:** Show terms
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `Days` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `CompanyIds` | `Int64[]` | no |  |

**Referenced by:** [Customers](Sales.md#Sales.Customer), [Quotes](Sales.md#Sales.Quote)


## Commands

<a id="Sales.CreateCustomerEmployeeSpan"></a>
### CreateCustomerEmployeeSpan

Creates a new customer employee span object.

- **Endpoint:** `POST /api/v1/Sales/CustomerEmployeeSpans/Create`
- **Required permission:** Create new customer
- **Introduced in:** 24.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |


<a id="Sales.CreateSalesPickingList"></a>
### CreateSalesPickingList

Creates picking lists.

- **Endpoint:** `POST /api/v1/Sales/SalesPickingLists/Create`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `DeliveryRows` | `DeliveryRow[]` | no |  |
| `CreatedByPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) |
| `OutgoingDeliveryLocationName` | `String` | no |  |

**References out:** [Persons](Common.md#Common.Person)

<a id="Sales.GetWithdrawalInformation"></a>
### GetWithdrawalInformation

Calculates and returns the suggested withdrawal information for a picking list.

- **Endpoint:** `POST /api/v1/Sales/SalesPickingLists/GetWithdrawalInformation`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `PickingListId` | `Int64` | no | [SalesPickingLists](Sales.md#Sales.SalesPickingList) |

**References out:** [SalesPickingLists](Sales.md#Sales.SalesPickingList)

<a id="Sales.RemoveSalesPickingList"></a>
### RemoveSalesPickingList

Deletes a picking list.

- **Endpoint:** `POST /api/v1/Sales/SalesPickingLists/Remove`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `PickingListId` | `Int64` | no | [SalesPickingLists](Sales.md#Sales.SalesPickingList) |

**References out:** [SalesPickingLists](Sales.md#Sales.SalesPickingList)


## Payload types

<a id="Sales.WithdrawalInformationLocation"></a>
### WithdrawalInformationLocation

Used to provide the suggested withdrawal information of a location.

- **Introduced in:** 2.53

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `PartLocationId` | `Int64` | no | [PartLocations](Inventory.md#Inventory.PartLocation) |
| `ProductRecordId` | `Int64?` | yes | [PartLocations](Inventory.md#Inventory.PartLocation) |
| `ReservedQuantity` | `Decimal` | no |  |
| `AvailableQuantity` | `Decimal` | no |  |
| `SuggestedQuantity` | `Decimal` | no |  |

**References out:** [PartLocations](Inventory.md#Inventory.PartLocation)
**Referenced by:** [WithdrawalInformationRow](Sales.md#Sales.WithdrawalInformationRow)

<a id="Sales.WithdrawalInformationRow"></a>
### WithdrawalInformationRow

Used to provide the suggested withdrawal information of a customer order row.

- **Introduced in:** 2.53

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `CustomerOrderRowId` | `Int64` | no | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |
| `PickingListId` | `Int64` | no | [SalesPickingLists](Sales.md#Sales.SalesPickingList) |
| `Locations` | `WithdrawalInformationLocation[]` | no | [WithdrawalInformationLocation](Sales.md#Sales.WithdrawalInformationLocation) |
| `SuggestedQuantity` | `Decimal` | no |  |
| `ParentCustomerOrderRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) |

**References out:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [SalesPickingLists](Sales.md#Sales.SalesPickingList), [WithdrawalInformationLocation](Sales.md#Sales.WithdrawalInformationLocation)


## Depends on other modules

- [Accounting](Accounting.md): [Accounts](Accounting.md#Accounting.Account), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [Codings](Accounting.md#Accounting.Coding), [CodingEntries](Accounting.md#Accounting.CodingEntry), [FixedAssets](Accounting.md#Accounting.FixedAsset)
- [Common](Common.md): [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Countries](Common.md#Common.Country), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [DeliveryTimes](Common.md#Common.DeliveryTime), [Discounts](Common.md#Common.Discount), [DiscountCategories](Common.md#Common.DiscountCategory), [ExtraFields](Common.md#Common.ExtraField), [FormReportConfigurations](Common.md#Common.FormReportConfiguration), [LanguageCodes](Common.md#Common.LanguageCode), [PartConfigurations](Common.md#Common.PartConfiguration), [PartialQuantities](Common.md#Common.PartialQuantity), [PaymentMethods](Common.md#Common.PaymentMethod), [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [PriceLists](Common.md#Common.PriceList), [Probabilities](Common.md#Common.Probability), [Projects](Common.md#Common.Project), [ReasonCodeDebitNotes](Common.md#Common.ReasonCodeDebitNote), [Resellers](Common.md#Common.Reseller), [Revisions](Common.md#Common.Revision), [StaggeredPrices](Common.md#Common.StaggeredPrice), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode), [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat), [TransferProfiles](Common.md#Common.TransferProfile), [Units](Common.md#Common.Unit), [VatGroups](Common.md#Common.VatGroup), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse)
- [Inventory](Inventory.md): [CaseEntry](Inventory.md#Inventory.CaseEntry), [GoodsTypes](Inventory.md#Inventory.GoodsType), [PackageTypes](Inventory.md#Inventory.PackageType), [Parts](Inventory.md#Inventory.Part), [PartLocations](Inventory.md#Inventory.PartLocation), [ProductRecords](Inventory.md#Inventory.ProductRecord)
- [Manufacturing](Manufacturing.md): [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder)
- [Purchase](Purchase.md): [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [Suppliers](Purchase.md#Purchase.Supplier)
