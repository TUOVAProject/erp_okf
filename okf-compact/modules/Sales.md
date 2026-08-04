# Sales

Monitor API module `Sales`: 70 queryable entities, 4 commands, 2 payload types.

## Queryable entities

<a id="Sales.BlanketOrderSales"></a>
### BlanketOrderSales

Represents a blanket order for sales.

- **Endpoint:** `GET /api/v1/Sales/BlanketOrderSales`
- **Required permission:** Show blanket order
- **Introduced in:** 23.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the blanket order. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the blanket order. |
| `OrderNumber` | `String` | no |  | The human readable identifier of the blanket order. |
| `OrderTypeId` | `Int64?` | yes | [BlanketOrderSalesTypes](Sales.md#Sales.BlanketOrderSalesType) | The business key identifier of the blanket order's type. |
| `OrderType` | `BlanketOrderSalesTypes` | no | [BlanketOrderSalesTypes](Sales.md#Sales.BlanketOrderSalesType) | The type of the blanket order. |
| `BusinessContactId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the blanket order's customer. |
| `BusinessContact` | `Customers` | no | [Customers](Sales.md#Sales.Customer) | The customer of the blanket order. |
| `CustomersOrderNumber` | `String` | no |  | The customer's order number of the blanket order. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the blanket order's business contact reference. |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business contact reference of the blanket order. |
| `IncludeInNetRequirementCalculation` | `Boolean` | no |  | Specifies if the blanket order is included in net requirement calculation. |
| `BusinessContactReferenceName` | `String` | no |  | The business contact reference name of the blanket order. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the blanket order's our reference. |
| `OurReference` | `Persons` | no | [Persons](Common.md#Common.Person) | Our reference of the blanket order. |
| `OurReferenceName` | `String` | no |  | Our reference name of the blanket order. |
| `ValidationPeriod` | `Int32` | no |  | Specifies the validation period of the blanket order. |
| `ValidFrom` | `DateTimeOffset` | no |  | The valid from date of the blanket order. |
| `ValidThrough` | `DateTimeOffset` | no |  | The valid through date of the blanket order. |
| `RequirementDate` | `DateTimeOffset` | no |  | The requirement date of the blanket order. |
| `Priority` | `Int32` | no |  | The priority of the blanket order. |
| `Status` | `Int32` | no |  | The status of the blanket order. |
| `CategoryString` | `String` | no |  | The category string of the blanket order. |
| `UseForwardRate` | `Boolean` | no |  | Specifies if the blanket order use forward rate. |
| `ExchangeRate` | `Decimal` | no |  | The exchange rate of the blanket order. |
| `CurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the blanket order's currency. |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The currency of the blanket order. |
| `OrderDate` | `DateTimeOffset` | no |  | The order date of the blanket order. |
| `DefaultOrderPrintoutVia` | `Int32` | no |  | The default order printout method of the blanket order. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the blanket order's mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The mailing address of the blanket order. |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the blanket order's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the blanket order. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the blanket order's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The external comment of the blanket order. |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the blanket order's seller. |
| `Seller` | `Persons` | no | [Persons](Common.md#Common.Person) | The seller of the blanket order. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the blanket order's currency exchange type. |
| `CurrencyExchangeType` | `CurrencyExchangeTypes` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The currency exchange type of the blanket order. |
| `Rows` | `BlanketOrderSalesRows[]` | no | [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow) | The rows of the blanket order. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the blanket order row. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the row. |
| `ParentOrderId` | `Int64?` | yes | [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales) | The business key identifier of the row's blanket order. |
| `ParentRowId` | `Int64?` | yes | [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow) | The business key identifier of the row's parent row. |
| `CustomerPartNumber` | `String` | no |  | The customer's part number of the row. |
| `Position` | `Int64?` | yes |  | The position of the row. |
| `OrderRowType` | `Int32` | no |  | The order row type of the row. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the row's part. |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The part of the row. |
| `PartRowType` | `Int32` | no |  | The part row type of the row. |
| `Quantity` | `Decimal` | no |  | The quantity of the row. |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The unit of the row. |
| `Price` | `Decimal?` | yes |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's price currency. |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The price currency of the row. |
| `PriceOriginPriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) | The business key identifier of the row's price origin price list. |
| `PriceLockedFromAutomaticChanges` | `Boolean?` | yes |  | Specifies if the row have price locked from automatic changes. |
| `PriceIsFuturePrice` | `Boolean?` | yes |  | Specifies if the row's price is future price. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  | The price in company currency of the row. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's company currency used in price in company currency. |
| `PriceInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The company currency used in price in company currency of the row. |
| `Discount` | `Decimal` | no |  | The discount of the row. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's setup price currency. |
| `SetupPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The setup price currency of the row. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  | The setup price in company currency of the row. |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) | The business key identifier of the row's VAT rate. |
| `VatRate` | `VatRates` | no | [VatRates](Common.md#Common.VatRate) | The VAT rate of the row. |
| `ShowFreeTextIn` | `Int32` | no |  | Specifies where the row's free text should be visible. |
| `ValidThrough` | `DateTimeOffset?` | yes |  | The requirement date of the row. |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the row's revision. |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) | The revision of the row. |
| `FreeTextHtml` | `String` | no |  | The free text in HTML format of the row. |
| `FreeText` | `String` | no |  | The free text of the row. |
| `ConversionFactor` | `Decimal` | no |  | The conversion factor of the row. |
| `QuantityRatio` | `Decimal?` | yes |  | The quantity ratio of the row. |
| `AdditionalRowDescription` | `String` | no |  | The additional row description of the row. |
| `AlternatePreparationCode` | `String` | no |  | The alternate preparation code of the row. |
| `RowsGoodsLabel` | `String` | no |  | The goods label of the row. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the blanket order type. |
| `Number` | `Int64` | no |  | The number of the blanket order type. |
| `Prefix` | `String` | no |  | The prefix of the blanket order type. |
| `Description` | `String` | no |  | The translated description of the blanket order type. |
| `Priority` | `Int32` | no |  | The priority of the blanket order type. |
| `Visible` | `Boolean` | no |  | Specifies if the blanket order type is visible. |
| `IsPreset` | `Boolean` | no |  | Specifies if the blanket order type is preset. |
| `BaseType` | `Int32` | no |  | The base type of the blanket order type. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the blanket order type's warehouse. |
| `PriceSetting` | `Int32` | no |  | The price setting of the blanket order type. |
| `PriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) | The business key identifier of the blanket order type's price list. |
| `RateTypeSetting` | `Int32` | no |  | The rate typ setting of the blanket order type. |
| `BlanketOrderSalesActivityTemplateId` | `Int64?` | yes |  | The business key identifier of the blanket order types activity template. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the blanket order type's currency exchange type. |
| `DefaultValidDays` | `Int32` | no |  | The default valid days of the blanket order type. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business opportunity. |
| `OpportunityNumber` | `String` | no |  | The human readable identifier of the business opportunity. |
| `StartDate` | `DateTimeOffset` | no |  | The start date of the business opportunity. |
| `PlannedEndDate` | `DateTimeOffset?` | yes |  | The planned end date of the business opportunity. |
| `ActualEndDate` | `DateTimeOffset?` | yes |  | The actual end date of the business opportunity. |
| `BusinessOpportunityGroupId` | `Int64?` | yes | [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup) | The business key identifier of the business opportunity's group. |
| `BusinessOpportunityGroup` | `BusinessOpportunityGroups` | no | [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup) | The business opportunity's group. |
| `BusinessOpportunityCategory` | `String` | no |  | The category of the business opportunity. |
| `SalesProcessTemplateId` | `Int64?` | yes | [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate) | The business key identifier of the business opportunity's sales process template. |
| `SalesProcessTemplate` | `SalesProcessTemplates` | no | [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate) | The business opportunity's sales process template. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the business opportunity's our reference. |
| `OurReference` | `Persons` | no | [Persons](Common.md#Common.Person) | The business opportunity's our reference. |
| `Description` | `String` | no |  | The description of the business opportunity. |
| `Status` | `Int32` | no |  | The status of the business opportunity. |
| `Priority` | `Int32` | no |  | The priority of the business opportunity. |
| `BusinessOpportunityTypeId` | `Int64?` | yes | [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType) | The business key identifier of the business opportunity's type. |
| `BusinessOpportunityType` | `BusinessOpportunityTypes` | no | [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType) | The business opportunity's type. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the business opportunity's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The business opportunity's comment. |
| `ReasonLostCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the business opportunity's comment on lost opportunity. |
| `ReasonLostComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The business opportunity's comment on lost opportunity. |
| `TotalValue` | `Decimal?` | yes |  | The total value of the business opportunity. |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the business opportunity's seller. |
| `Seller` | `Persons` | no | [Persons](Common.md#Common.Person) | The business opportunity's seller. |
| `Name` | `String` | no |  | The translated name of the business opportunity. |
| `ReferenceName` | `String` | no |  | The reference name of the business opportunity. |
| `ReasonCodeLostQuoteId` | `Int64?` | yes | [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote) | The business key identifier of the business opportunity's reason code for lost quote. |
| `ReasonCodeLostQuote` | `ReasonCodeLostQuotes` | no | [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote) | The business opportunity's reason code for lost quote. |
| `BusinessContactNoteHistories` | `BusinessContactNoteHistories[]` | no | [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory) | The business contact note history entries for the business opportunity. |
| `Customers` | `Customers[]` | no | [Customers](Sales.md#Sales.Customer) | The customers on the business opportunity. |

- `Status` — Registered=1, InProgress=3, Finished=4, Cancelled=5, Pending=6, Historical=9

**References out:** [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory), [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup), [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType), [Comments](Common.md#Common.Comment), [Customers](Sales.md#Sales.Customer), [Persons](Common.md#Common.Person), [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote), [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate)
**Referenced by:** [BusinessOpportunityActivities](Sales.md#Sales.BusinessOpportunityActivity), [BusinessOpportunityReferences](Sales.md#Sales.BusinessOpportunityReference), [BusinessOpportunitySalesProcessSteps](Sales.md#Sales.BusinessOpportunitySalesProcessStep), [Quotes](Sales.md#Sales.Quote)

<a id="Sales.BusinessOpportunityActivity"></a>
### BusinessOpportunityActivities

Represents a business opportunity activity.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityActivities`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business opportunity activity. |
| `OrderId` | `Int64?` | yes | [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity) | The business key identifier of the activity's business opportunity. |
| `RowIndex` | `Int32?` | yes |  | The row index of the actifity. |
| `ActivityTypeId` | `Int64?` | yes |  | The business key identifier of the activity's type. |
| `IsMandatory` | `Boolean` | no |  | Specifies if the activity is mandatory. |
| `IsDueDatePlannedCompletionDate` | `Boolean` | no |  | Specifies if due date id planned completion date on the activity. |
| `IsAdministratorResponsibleUser` | `Boolean` | no |  | Specifies if the administrator is the responsible user of the activity. |
| `Description` | `String` | no |  | The translated description of the activity. |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  | The planned start date of the activity. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the user who is responsible for this activity. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer on this activity. |
| `ReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the reference on this activity. |
| `DueDateType` | `Int32` | no |  | The due date type of the activity. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the activity's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the activity. |
| `Status` | `Int32` | no |  | The status of the activity. |
| `NumberDaysFromDueDate` | `Int32?` | yes |  | Specifies number of days from due date on this activity. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  | The planned completion date of the activity. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  | The actual start date of the activity. |
| `CompletionDate` | `DateTimeOffset?` | yes |  | The completion date of the activity. |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the user who completed this activity. |
| `ReminderId` | `Int64?` | yes |  | The business key identifier of the activity's reminder. |
| `CalendarAppointmentId` | `String` | no |  | The calendar appointment id of the activity. |

- `DueDateType` — RegistrationDate=0, ValidThrough=1
- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [Comments](Common.md#Common.Comment), [Customers](Sales.md#Sales.Customer), [Persons](Common.md#Common.Person)

<a id="Sales.BusinessOpportunityActivityTemplateRow"></a>
### BusinessOpportunityActivityTemplateRows

Represents a business opportunity activity template row.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityActivityTemplateRows`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business opportunity activity template row. |
| `ActivityTemplateId` | `Int64?` | yes | [BusinessOpportunityActivityTemplates](Sales.md#Sales.BusinessOpportunityActivityTemplate) | The business key identifier of the row's business opportunity activity template. |
| `ActivityTypeId` | `Int64?` | yes | [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType) | The business key identifier of the template row's activity type. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the template row's responsible application user. |
| `Code` | `Int64` | no |  | The code of the template row. |
| `IsAdministratorResponsible` | `Boolean` | no |  | Specifies if administrator is responsible for the template row. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the template row's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The template row's comment. |
| `DueDateType` | `Int32` | no |  | The due date type of the template row. |
| `NumberDaysFromDueDate` | `Int32` | no |  | The number of work days from due date of the template row. |
| `Status` | `Int32` | no |  | The status of the template row. |
| `IsMandatory` | `Boolean` | no |  | Specifies if the template row is mandatory. |
| `IsReminder` | `Boolean` | no |  | Specifies if the template row is a reminder. |
| `IsLoggedUserResponsible` | `Boolean` | no |  | Specifies if the logged user is responsible for the remplate row. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business opportunity activity template. |
| `Code` | `Int64` | no |  | The human readable identifier of the business opportunity activity template. |
| `Description` | `String` | no |  | The translated description of the business opportunity activity template. |
| `Rows` | `BusinessOpportunityActivityTemplateRows[]` | no | [BusinessOpportunityActivityTemplateRows](Sales.md#Sales.BusinessOpportunityActivityTemplateRow) | The rows of the business opportunity activity template. |

**References out:** [BusinessOpportunityActivityTemplateRows](Sales.md#Sales.BusinessOpportunityActivityTemplateRow)
**Referenced by:** [BusinessOpportunityActivityTemplateRows](Sales.md#Sales.BusinessOpportunityActivityTemplateRow), [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType)

<a id="Sales.BusinessOpportunityGroup"></a>
### BusinessOpportunityGroups

Represents a business opportunity group.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityGroups`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business opportunity group. |
| `Code` | `Int64` | no |  | The human readable identifier of the business opportunity group. |
| `IsActive` | `Boolean` | no |  | Specifies if the business opportunity group is active. |
| `Description` | `String` | no |  | The translated description of the business opportunity group. |

**Referenced by:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType)

<a id="Sales.BusinessOpportunityReference"></a>
### BusinessOpportunityReferences

Represents a business opportunity reference.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityReferences`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business opportunity reference. |
| `Name` | `String` | no |  | The name of the reference. |
| `ParentId` | `Int64` | no | [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity) | The business key identifier of the reference's business opportunity. |
| `ShouldFilterLogPosts` | `Boolean` | no |  | Specifies if the reference should filter log posts. |
| `IsDefault` | `Boolean` | no |  | Specifies if this is the default reference for the business opportunity. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer the reference belongs to. |
| `ReferenceCode` | `String` | no |  | The code of the reference. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the reference's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The reference's comment. |
| `Remark` | `String` | no |  | The remark of the reference. |
| `ReferenceCategory` | `String` | no |  | The reference category of the reference. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) | The communication addresses of the reference. |

**References out:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Customers](Sales.md#Sales.Customer)

<a id="Sales.BusinessOpportunitySalesProcessStep"></a>
### BusinessOpportunitySalesProcessSteps

Represents a business opportunity sales process step.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunitySalesProcessSteps`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business opportunity sales process step. |
| `Code` | `Int64` | no |  | The code of the sales process step. |
| `Description` | `String` | no |  | The translated description of the sales process step. |
| `Probability` | `Int32` | no |  | The probability of the sales process step. |
| `LeadTime` | `Int32` | no |  | The lead time of the sales process step. |
| `Responsibility` | `Int32` | no |  | Specifies what is responsibel for the sales process step. |
| `ResponsibleSellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The responsible seller of the sales process step. |
| `ResponsibleSellerGroupId` | `Int64?` | yes | [SellerGroups](Sales.md#Sales.SellerGroup) | The responsible seller group of the sales process step. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The responsible application user of the sales process step. |
| `ParentId` | `Int64?` | yes | [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity) | The business opportunity the sales process step belongs to. |
| `RowIndex` | `Int32?` | yes |  | The row index of the sales process step. |
| `Status` | `Int32` | no |  | The status of the sales process step. |
| `IsActive` | `Boolean` | no |  | Specifies if the sales process step is active. |

- `Responsibility` — Seller=0, Group=1
- `Status` — NotStarted=0, Started=1, Finished=2

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [Persons](Common.md#Common.Person), [SellerGroups](Sales.md#Sales.SellerGroup)

<a id="Sales.BusinessOpportunityType"></a>
### BusinessOpportunityTypes

Represents a business opportunity type.

- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityTypes`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business opportunity type. |
| `Code` | `Int64` | no |  | The human readable identifier of the business opportunity type. |
| `IsActive` | `Boolean` | no |  | Specifies if the business opportunity type is active. |
| `Description` | `String` | no |  | The translated description of the business opportunity type. |
| `Prefix` | `String` | no |  | The prefix of the opportunity number created by the business opportunity type. |
| `IsDefault` | `Boolean` | no |  | Specifies if the business opportunity type is the default type. |
| `Priority` | `Int32` | no |  | The priority of the business opportunity type. |
| `BusinessOpportunityGroupId` | `Int64?` | yes | [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup) | The business key identifier of the business opportunity type's business opportunity group. |
| `BusinessOpportunityGroup` | `BusinessOpportunityGroups` | no | [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup) | The business opportunity type's business opportunity group. |
| `ResponsibleSellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the business opportunity type's .responsible seller. |
| `ResponsibleSeller` | `Persons` | no | [Persons](Common.md#Common.Person) | The business opportunity type's .responsible seller. |
| `SalesProcessTemplateId` | `Int64?` | yes | [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate) | The business key identifier of the business opportunity type's .sales process template. |
| `SalesProcessTemplate` | `SalesProcessTemplates` | no | [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate) | The business opportunity type's .sales process template. |
| `BusinessOpportunityActivityTemplateId` | `Int64?` | yes | [BusinessOpportunityActivityTemplates](Sales.md#Sales.BusinessOpportunityActivityTemplate) | The business key identifier of the business opportunity type's .activity template. |
| `BusinessOpportunityActivityTemplate` | `BusinessOpportunityActivityTemplates` | no | [BusinessOpportunityActivityTemplates](Sales.md#Sales.BusinessOpportunityActivityTemplate) | The business opportunity type's .activity template. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the business opportunity type's .comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The business opportunity type's .comment. |

**References out:** [BusinessOpportunityActivityTemplates](Sales.md#Sales.BusinessOpportunityActivityTemplate), [BusinessOpportunityGroups](Sales.md#Sales.BusinessOpportunityGroup), [Comments](Common.md#Common.Comment), [Persons](Common.md#Common.Person), [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate)
**Referenced by:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity)

<a id="Sales.CountryDocumentSettings"></a>
### CountryDocumentSettings

Represents a country document setting.

- **Endpoint:** `GET /api/v1/Sales/CountryDocumentSettings`
- **Required permission:** Modify settings for file viewer
- **Introduced in:** 26.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the country document setting. |
| `RowIndex` | `Int32?` | yes |  | The row index of the document setting. |
| `CountryId` | `Int64` | no | [Countries](Common.md#Common.Country) | The business key identifier of the document setting's country. |
| `ShowInSalesForm` | `Int32` | no |  | Specifies the document type this setting applies to. |
| `ShowCountryOfOrigin` | `Boolean` | no |  | Specifies if this setting should show country of origin. |
| `ShowNetWeight` | `Boolean` | no |  | Specifies if this setting should show net weight. |
| `ShowTradeClassificationName` | `Boolean` | no |  | Specifies if this setting should show trade classification name. |
| `ShowCN` | `Boolean` | no |  | Specifies if this setting should show CN. |
| `ShowHS` | `Boolean` | no |  | Specifies if this setting should show HS. |
| `ShowTaric` | `Boolean` | no |  | Specifies if this setting should show taric. |
| `ShowHTS` | `Boolean` | no |  | Specifies if this setting should show HTS. |
| `ShowNCM` | `Boolean` | no |  | Specifies if this setting should show NCM. |
| `ShowECCN` | `Boolean` | no |  | Specifies if this setting should show ECCN. |
| `ShowSITC` | `Boolean` | no |  | Specifies if this setting should show SITC. |
| `AmountExcludedDiscount` | `Boolean` | no |  | Specifies if this setting should show amount excluded discount. |
| `TotalByCombCode` | `Int32` | no |  | Specifies which classification code system drives the "Total by Comb. n. code" summary section on Pro forma and Comprehensive proforma invoices. Only meaningful when is . |

- `ShowInSalesForm` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16
- `TotalByCombCode` — CN=0, HS=1, Taric=2, HTS=3, NCM=4, ECCN=5, SITC=6

**References out:** [Countries](Common.md#Common.Country)

<a id="Sales.CustomerAccountGroup"></a>
### CustomerAccountGroups

Represents a customer account group.

- **Endpoint:** `GET /api/v1/Sales/CustomerAccountGroups`
- **Required permission:** Show chart of accounts
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the group. |
| `IsDefault` | `Boolean` | no |  | Specifies if the group is the default group. |
| `Number` | `Int64` | no |  | The human readable identifier of the group. |
| `Description` | `String` | no |  | The translated description of the group. |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |

**Referenced by:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [Countries](Common.md#Common.Country), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [Quotes](Sales.md#Sales.Quote), [SalesAgreements](Sales.md#Sales.SalesAgreement), [SalesForecasts](Inventory.md#Inventory.SalesForecast)

<a id="Sales.CustomerCountryDocumentSettings"></a>
### CustomerCountryDocumentSettings

Represents a customer country document setting.

- **Endpoint:** `GET /api/v1/Sales/CustomerCountryDocumentSettings`
- **Required permission:** Show customer
- **Introduced in:** 26.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer country document setting. |
| `RowIndex` | `Int32?` | yes |  | The row index of the document setting. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the document setting's customer. |
| `CountryId` | `Int64` | no | [Countries](Common.md#Common.Country) | The business key identifier of the document setting's country. |
| `ShowInSalesForm` | `Int32` | no |  | Specifies the document type this setting applies to. |
| `ShowCountryOfOrigin` | `Boolean?` | yes |  | Specifies if this setting should show country of origin. |
| `ShowNetWeight` | `Boolean?` | yes |  | Specifies if this setting should show net weight. |
| `ShowTradeClassificationName` | `Boolean?` | yes |  | Specifies if this setting should show trade classification name. |
| `ShowCN` | `Boolean?` | yes |  | Specifies if this setting should show CN. |
| `ShowHS` | `Boolean?` | yes |  | Specifies if this setting should show HS. |
| `ShowTaric` | `Boolean?` | yes |  | Specifies if this setting should show taric. |
| `ShowHTS` | `Boolean?` | yes |  | Specifies if this setting should show HTS. |
| `ShowNCM` | `Boolean?` | yes |  | Specifies if this setting should show NCM. |
| `ShowECCN` | `Boolean?` | yes |  | Specifies if this setting should show ECCN. |
| `ShowSITC` | `Boolean?` | yes |  | Specifies if this setting should show SITC. |
| `AmountExcludedDiscount` | `Boolean?` | yes |  | Specifies if this setting should show amount excluded discount. |
| `TotalByCombCode` | `Int32?` | yes |  | Overrides the for this customer when set. Null means the country-level setting is used. Only meaningful when is . |

- `ShowInSalesForm` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16
- `TotalByCombCode` — CN=0, HS=1, Taric=2, HTS=3, NCM=4, ECCN=5, SITC=6

**References out:** [Countries](Common.md#Common.Country), [Customers](Sales.md#Sales.Customer)

<a id="Sales.CustomerDistrict"></a>
### CustomerDistricts

Represents a customer district.

- **Endpoint:** `GET /api/v1/Sales/CustomerDistricts`
- **Required permission:** Show customer
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer district. |
| `Code` | `Int64` | no |  | The human readable identifier of the customer district. |
| `Description` | `String` | no |  | The translated description of the customer district. |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |

**Referenced by:** [Customers](Sales.md#Sales.Customer), [Persons](Common.md#Common.Person), [SalesForecasts](Inventory.md#Inventory.SalesForecast)

<a id="Sales.CustomerEmployeeSpan"></a>
### CustomerEmployeeSpans

Represents a customer employee span.

- **Endpoint:** `GET /api/v1/Sales/CustomerEmployeeSpans`
- **Required permission:** Show customer
- **Introduced in:** 24.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer employee span. |
| `Code` | `Int64` | no |  | The human readable key identifier of customer employee span. |
| `Description` | `String` | no |  | The description of customer employee span. |

**Referenced by:** [Customers](Sales.md#Sales.Customer)

<a id="Sales.CustomerOrderActivity"></a>
### CustomerOrderActivities

Represents a customer order activity.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderActivities`
- **Required permission:** Show customer orders
- **Introduced in:** 24.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer order activity. |
| `OrderId` | `Int64` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order to add the activity to. |
| `ActivityTypeId` | `Int64` | no | [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType) | The business key identifier of the customer order activity type that the activity is based on. |
| `Description` | `String` | no |  | The description of the activity. |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that is responsible for the activity. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  | The planned completion date of the activity. |
| `Reminder` | `Boolean?` | yes |  | Sets whether or not a reminder should be created for the activity. |

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType)

<a id="Sales.CustomerOrderDeliveryRow"></a>
### CustomerOrderDeliveryRows

Represents a customer delivery order row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderDeliveryRows`
- **Required permission:** Show customer orders
- **Introduced in:** 2.36

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the row. |
| `AffectStockBalance` | `Boolean` | no |  | Specifies if row affect the stock balance. |
| `BusinessTransactionContextType` | `Int32` | no |  | The type of the business transaction context. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order. |
| `CustomerOrderRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The business key identifier of the customer order row. |
| `DeliveryDate` | `DateTimeOffset` | no |  | The delivery date of the row. |
| `FreeTextHtml` | `String` | no |  | The free text row's rich text HTML row data. |
| `FreeText` | `String` | no |  | The free text row's raw text. |
| `InvoiceId` | `Int64?` | yes | [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice) | The business key identifier of the customer order invoice. CustomerOrderInvoices |
| `ParentId` | `Int64?` | yes |  | The business key identifier of the parent. |
| `ParentInvoiceId` | `Int64?` | yes |  | The business key identifier of the parent invoice. |
| `PickListDeliveryDate` | `DateTimeOffset?` | yes |  | The delivery date of the pick list. |
| `QuantityChangeId` | `Int64?` | yes |  | The business key identifier of the quantity change. |
| `InvoiceRowId` | `Int64?` | yes | [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow) | The business key identifier of the customer order invoice row. CustomerOrderInvoiceRows |
| `InvoiceRow` | `CustomerOrderInvoiceRows` | no | [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow) | The invoice row of the customer order delivery row. CustomerOrderInvoiceRows |

- `BusinessTransactionContextType` — NotInitialized=0, ArrivalReporting=1, ManufacturingOrderReporting=2, DeliveryReporting=3, PhysicalInventory=4, UnplannedStockWithdrawal=5, MoveBetweenWarehouse=6, MoveStockBalance=7, NonconformityPosteriorRejection=8, DirectlyRegisteredInvoice=9, RemovalOfPartLocation=10, ManufacturingOrderMaterialReporting=11, UnplannedStockArrivalReporting=12, StockImport=13, DeliveryReportingStockOrder=14, ArrivalReportingStockOrder=15, UndoManufacturingOrderMaterialReporting=16, UndoManufacturingOrderReporting=17, UndoArrivalReporting=18, UndoDeliveryReporting=19, UndoArrivalReportingStockOrder=20, UndoDeliveryReportingStockOrder=21, OutgoingReusable=22, ArrivalReusable=23, UndoOutgoingReusable=24, UndoArrivalReusable=25, ToolWithdrawal=26, ToolReturn=27, CreditSupplierInvoice=28, CreditCustomerInvoice=29, ReturnPurchaseOrder=30, SplitInvoiceBasis=31, CreationOfPartLocation=32, ArrivalsCorrection=33, ArrivalRejection=34, UndoReturnPurchaseOrder=35

**References out:** [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerOrders](Sales.md#Sales.CustomerOrder)
**Referenced by:** [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [InvoiceLogs](Sales.md#Sales.InvoiceLog), [PackageRows](Sales.md#Sales.PackageRow), [ProductRecords](Inventory.md#Inventory.ProductRecord), [SalesPickingListRowQuantities](Sales.md#Sales.SalesPickingListRowQuantity)

<a id="Sales.CustomerOrderInvoiceOrderRowDiscount"></a>
### CustomerOrderInvoiceOrderRowDiscounts

Represents a discount row for a customer order invoice row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderInvoiceOrderRowDiscounts`
- **Required permission:** Show customer orders
- **Introduced in:** 24.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the discount row. |
| `OrderRowId` | `Int64` | no | [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow) | The business key identifier of the discount row's invoice row. |
| `DiscountId` | `Int64?` | yes | [Discounts](Common.md#Common.Discount) | The business key identifier of the discount row's discount. |
| `AsPercent` | `Decimal?` | yes |  | The discount amount as percent of the discount row. |
| `DiscountLockedFromAutomaticChanges` | `Boolean` | no |  | Specifies if the discount is locked from automatic changes. |
| `AsAmount` | `Decimal?` | yes |  | The discount amount of the discount row. |
| `AsAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the discount row's amount currency. |
| `DiscountType` | `Int32` | no |  | The discount type of the discount row. |
| `GrossPrice` | `Decimal?` | yes |  | The gross price of the discount row. |
| `GrossPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the discount row's gross price currency. |
| `NetPrice` | `Decimal?` | yes |  | The net price of the discount row. |
| `NetPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the discount row's net price currency. |
| `DiscountCalculationType` | `Int32` | no |  | The discount calculation type of the discount row. |
| `Priority` | `Int32` | no |  | The priority of the discount row. |
| `ReplacesDiscountFieldOnOrderRow` | `Boolean` | no |  | Specifies if this discount row represents the discount which could be applied to the discount field on the order row itself before order multiple discounts on order rows were introduced. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the row. |
| `CodingId` | `Int64?` | yes |  |  |
| `Discount` | `Decimal?` | yes |  | The discount specified on the row. |
| `InterestInvoiceBasisId` | `Int64?` | yes |  | The business key identifier of the interest invoice basis. |
| `LedgerId` | `Int64?` | yes |  | The business key identifier to the ledger's accounts receivable of the customer order invoice. |
| `OverrideStandardPrice` | `Decimal?` | yes |  | The value of the overridden standard price. |
| `OverrideStandardPriceCurrencyId` | `Int64?` | yes |  | The business key identifier of the override standard price currency |
| `Price` | `Decimal?` | yes |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's price currency. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  | The row's price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency. |
| `PriceIsFuturePrice` | `Boolean?` | yes |  | Specifies if the price is a future price. |
| `PriceLockedFromAutomaticChanges` | `Boolean?` | yes |  | Specifies if price is locked from automatic changes. |
| `PriceOrigin` | `Int32?` | yes |  | The price origin of the row. |
| `PriceOriginPriceListId` | `Int64?` | yes |  | The business key identifier of the row's original pricelist. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes |  | The business key identifier of the row's setup price currency. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  | The row's setup price in the company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency. |
| `StandardPrice` | `Decimal?` | yes |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's standard price currency. |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) | The business key identifier of the row's VAT rate. |
| `DiscountRows` | `CustomerOrderInvoiceOrderRowDiscounts[]` | no | [CustomerOrderInvoiceOrderRowDiscounts](Sales.md#Sales.CustomerOrderInvoiceOrderRowDiscount) | The discount rows for the row. |

- `PriceOrigin` — Undefined=0, UserDefined=1, PriceList=2, PriceListStaggered=3, BusinessPartLink=4, BusinessPartLinkStaggered=5, StandardPrice=6, PartConfiguration=7, PostCalculatedAverage=8, BusinessPartLinkFuturePrice=9

**References out:** [Currencies](Common.md#Common.Currency), [CustomerOrderInvoiceOrderRowDiscounts](Sales.md#Sales.CustomerOrderInvoiceOrderRowDiscount), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerOrderInvoiceOrderRowDiscounts](Sales.md#Sales.CustomerOrderInvoiceOrderRowDiscount)

<a id="Sales.CustomerOrderInvoice"></a>
### CustomerOrderInvoices

Represents a customer order invoice.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderInvoices`
- **Required permission:** Show customer orders
- **Introduced in:** 2.33

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer order invoice. |
| `Status` | `Int32` | no |  | The status of the customer order invoice. |
| `DeliveryNoteNumber` | `Int64` | no |  | The delivery note number of the customer order invoice. |
| `DeliveryIndex` | `Int32` | no |  | The delivery index of the customer order invoice. |
| `OrderDeliveryNumber` | `String` | no |  | The order delivery number of the customer order invoice. |
| `PickingListId` | `Int64?` | yes |  | The business key identifier of the picking list of the customer order invoice. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the customer order invoice belongs to. |
| `Version` | `Int32` | no |  | The version of the customer order invoice. |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer source of the active delivery address. |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier source of the active delivery address. |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  | The business key identifier of the company source of the active delivery address. |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  | Specifies the source of the customer order invoice delivery address. |
| `ConsigneeReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the consignee reference of the customer order invoice. |
| `ConsigneeReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The consignee reference on the customer order invoice. |
| `ProformaStatus` | `Int32` | no |  | The proforma status of the customer order invoice. |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of project of the customer order invoice. |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the delivery address of the customer order invoice. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The delivery address of the customer order invoice. |
| `InvoiceAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the invoice address of the customer order invoice. |
| `InvoiceAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The invoice address of the customer order invoice. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of our reference for the customer order invoice. Reference Persons |
| `OurReferenceName` | `String` | no |  | The name of our reference for the customer order invoice. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the customer's reference for the customer order invoice. |
| `BusinessContactReferenceName` | `String` | no |  | The name of the customer's reference for the customer order invoice. |
| `GoodsLabel` | `String` | no |  | The goods label of the customer order invoice. |
| `InvoiceStatusPending` | `Boolean` | no |  | Specifies if the invoice status is pending on the customer order invoice. |
| `IsPartOfComprehensiveInvoice` | `Boolean` | no |  | Specifies if the customer order invoice is part of a comprehensive invoice. _(Replaced by ComprehensiveInvoiceGroupingMode)_ |
| `ComprehensiveInvoiceGroupingMode` | `Int32` | no |  | Specifies if the customer order invoice is part of a comprehensive invoice, and how they are grouped. |
| `HasInvoicingCharge` | `Boolean` | no |  | Specifies if the customer order invoice involves an invoicing charge. |
| `IsFreeDeliveryMonth` | `Boolean` | no |  | Specifies if the customer order invoice have a free delivery month. |
| `GoodsAddressNumber` | `String` | no |  | The goods address number of the customer order invoice. |
| `VatNumber` | `String` | no |  | The VAT number of the customer order invoice. |
| `Dock` | `String` | no |  | The dock of the customer order invoice. |
| `DeliveryInstruction` | `String` | no |  | The delivery instruction of the customer order invoice. |
| `InvoicePrintoutMethod` | `Int32?` | yes |  | Specifies the printout method for the customer order invoice. |
| `PrintProformaInvoiceVia` | `Int32?` | yes |  | The preferred Proforma printout method of the customer order invoice. |
| `EInvoiceExportMode` | `Int32?` | yes |  | The preffered electronic invoice export mode to use on this customer order invoice. |
| `Priority` | `Int32` | no |  | The priority of the customer order invoice. |
| `DirectlyRegistered` | `Boolean` | no |  | Specifies if the customer order invoice is directly registered. |
| `PartialInvoiceType` | `Int32?` | yes |  | The partial invoice type of the customer order invoice. |
| `FormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](Common.md#Common.FormReportConfiguration) | The business key identifier of the customer order invoice's form report configuration. |
| `DeliveryNoteCreationDate` | `DateTimeOffset?` | yes |  | The delivery note creation date on the customer order invoice. |
| `ExcludeFromEdi` | `Boolean` | no |  | Specifies if the customer order invoice will be excluded from EDI. |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the seller on the customer order invoice. |
| `ShippingInformationId` | `Int64?` | yes |  | The business key identifier of the shipping information on the customer order invoice. |
| `ProformaNumber` | `Int64?` | yes |  | The proforma number of the customer order invoice. |
| `ProformaDate` | `DateTimeOffset?` | yes |  | The proforma date of the customer order invoice. |
| `DestinationForDeliveryTerm` | `String` | no |  | The destination for delivery term for the customer order invoice. |
| `CandidateDebitInvoiceId` | `Int64?` | yes |  | The business key identifier to the accounts receivable linked to the debit invoice candidate for this customer order invoice. References AccountsReceivable. |
| `ConsigneeReferenceName` | `String` | no |  | The consignee reference name of the customer order invoice. |
| `LedgerId` | `Int64?` | yes |  | The business key identifier to the ledger's accounts receivable of the customer order invoice. References AccountsReceivable. |
| `BusinessContactOrderId` | `Int64` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier to the customre order of the customer order invoice. References CustomerOrders . |
| `InvoiceBusinessContactId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) | The business key identifier to the customer on the customer order invoice. References Customers . |
| `AccountGroupId` | `Int64` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The business key identifier of the account group of the customer order invoice. |
| `AccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The account group on the customer order invoice. |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) | The business key identifier of the VAT group that applies for the customer order invoice. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the payment term of the customer order invoice. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The payment term of the customer order invoice. |
| `PaymentTermDescription` | `String` | no |  | The payment term description of the customer order invoice. |
| `GracePeriodInDays` | `Int32?` | yes |  | The grace period in days of the customer order invoice. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the delivery method of the customer order invoice. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) | The business key identifier of the delivery term of the customer order invoices. |
| `DeliveryTermDescription` | `String` | no |  | The delivery term description of the customer order invoice. |
| `DeliveryMethodDescription` | `String` | no |  | The delivery method description of the customer order invoice. |
| `ShipmentPayer` | `Int32` | no |  | Specifies who is responsible for the shipment payment for the customer order invoce. |
| `DeliveryRows` | `CustomerOrderDeliveryRows[]` | no | [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow) | The customer order delivery rows. CustomerOrderDeliveryRows |
| `InvoiceType` | `Int32` | no |  | Invoice type of customer order invoice |
| `EditedOrderAmountExcludingVat` | `Decimal?` | yes |  | The edited order amount excluding VAT for the customer order invoice. |
| `EditedOrderAmountExcludingVatCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The currency of the edited order amount excluding VAT for the customer order invoice. |
| `EditedOrderAmountDiscount` | `Decimal?` | yes |  | The edited order amount discount in percent for the customer order invoice. |
| `TypeOfOrderAmountEntered` | `Int32?` | yes |  | The type of edited order value entered on the customer order invoice. |
| `Factoring` | `Boolean` | no |  | Specifies if factoring is activated for the customer order invoice. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the discount row. |
| `OrderRowId` | `Int64` | no | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The business key identifier of the discount row's customer order row. |
| `DiscountId` | `Int64?` | yes | [Discounts](Common.md#Common.Discount) | The business key identifier of the discount row's discount. |
| `AsPercent` | `Decimal?` | yes |  | The discount amount as percent of the discount row. |
| `DiscountLockedFromAutomaticChanges` | `Boolean` | no |  | Specifies if the discount is locked from automatic changes. |
| `AsAmount` | `Decimal?` | yes |  | The discount amount of the discount row. |
| `AsAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the discount row's amount currency. |
| `DiscountType` | `Int32` | no |  | The discount type of the discount row. |
| `GrossPrice` | `Decimal?` | yes |  | The gross price of the discount row. |
| `GrossPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the discount row's gross price currency. |
| `NetPrice` | `Decimal?` | yes |  | The net price of the discount row. |
| `NetPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the discount row's net price currency. |
| `DiscountCalculationType` | `Int32` | no |  | The discount calculation type of the discount row. |
| `Priority` | `Int32` | no |  | The priority of the discount row. |
| `ReplacesDiscountFieldOnOrderRow` | `Boolean` | no |  | Specifies if this discount row represents the discount which could be applied to the discount field on the order row itself before order multiple discounts on order rows were introduced. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer order payment plan row. |
| `CustomerOrderId` | `Int64` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order this row belongs to. |
| `InvoicingPeriod` | `DateTimeOffset?` | yes |  | The invoicing period of the row. |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) | The business key identifier of the VAT rate of the row. |
| `Amount` | `Decimal` | no |  | The amount of the row. |
| `AmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the rows amount. |
| `AmountInCompanyCurrency` | `Decimal` | no |  | The amount in company currency of the row. |
| `AmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the rows amount in company currency. |
| `ReducedAmountInCompanyCurrency` | `Decimal?` | yes |  | The reduced amount in company currency of the row. |
| `ReducedAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the rows reduced amount in company currency. |
| `IsReset` | `Boolean` | no |  | Specifies if the row is reset. |
| `CodingEntryId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry for the row. |
| `PartialInvoiceType` | `Int32` | no |  | The partial invoice type of the row. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the rows part. |
| `OverrideDescription` | `String` | no |  | The override description of the row. |
| `FractionOfTotal` | `Decimal` | no |  | The fraction of the total amount for the row. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the payment term for the row. |
| `RowIndex` | `Int32?` | yes |  | The row index of the row. |

- `PartialInvoiceType` — NotInitialized=0, InAdvance=1, Delivery=2, InArrears=3, Text=4

**References out:** [CodingEntries](Accounting.md#Accounting.CodingEntry), [Currencies](Common.md#Common.Currency), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Parts](Inventory.md#Inventory.Part), [PaymentTerms](Common.md#Common.PaymentTerm), [VatRates](Common.md#Common.VatRate)

<a id="Sales.CustomerOrderRowInflow"></a>
### CustomerOrderRowInflows

Represents a customer order inflow row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderRowInflows`
- **Required permission:** Show customer orders
- **Introduced in:** 23.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the inflow row. |
| `OrderRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The business key identifier of the inflow rows customer order row. |
| `OrderRow` | `CustomerOrderRows` | no | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The inflow rows customer order row. |
| `BlanketOrderSalesRowId` | `Int64?` | yes |  | The business key identifier of the inflow rows blanket order sales row. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the inflow rows part. |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The inflow rows part. |
| `EntityIdentityString` | `String` | no |  | The human readable identifier of the entity subject of the inflow row. |
| `AdditionalRowDescription` | `String` | no |  | The additional row description of the inflow row. |
| `Status` | `Int32` | no |  | The status of the inflow row. |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  | The logging timestamp of the inflow row. |
| `OrderedQuantityChange` | `Decimal?` | yes |  | The ordered quantity change of the inflow row. |
| `UnitId` | `Int64?` | yes |  | The business key identifier of the inflow rows unit. |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The inflow rows unit. |
| `PriceChange` | `Decimal?` | yes |  | The price change of the inflow row. |
| `PriceChangeCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the inflow rows price changes currency. |
| `PriceChangeCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The inflow rows price changes currency. |
| `SetupPriceChange` | `Decimal?` | yes |  | The setup price change of the inflow row. |
| `SetupPriceChangeCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the inflow rows setup price changes currency. |
| `SetupPriceChangeCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The inflow rows setup price changes currency. |
| `DiscountChange` | `Decimal?` | yes |  | The discount change of the inflow row. |
| `TotalValueChange` | `Decimal` | no |  | The total value change of the inflow row. |
| `TotalValueChangeCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the inflow rows total value changes currency. |
| `TotalValueChangeCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The inflow rows total value changes currency. |
| `OrderRowType` | `Int32` | no |  | The order row type of the inflow row. |

- `Status` — New=0, Changed=1, Removed=2
- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4

**References out:** [Currencies](Common.md#Common.Currency), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [Parts](Inventory.md#Inventory.Part), [Units](Common.md#Common.Unit)

<a id="Sales.CustomerOrderRow"></a>
### CustomerOrderRows

Represents a customer order row.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderRows`
- **Required permission:** Show customer orders
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the row. |
| `Position` | `Int64?` | yes |  | The relative numeric position of the row. |
| `OrderRowType` | `Int32` | no |  | The type of the row. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part set for the row. |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The part of the row. |
| `EntityIdentityString` | `String` | no |  | The human readable identifier of the entity subject of the row. |
| `AdditionalRowDescription` | `String` | no |  | The additional row description of the row. |
| `FreeTextHtml` | `String` | no |  | The free text row's rich text HTML row data. |
| `FreeText` | `String` | no |  | The free text row's raw text. |
| `ParentRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The business key identifier of the current row's parent. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  | The delivery date set for the row. |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the row's revision. |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) | The revision of the row. |
| `OrderedQuantity` | `Decimal` | no |  | The ordered quantity of the row. |
| `Price` | `Decimal?` | yes |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row price currency. |
| `Discount` | `Decimal` | no |  | The discount in percent set for the row. |
| `ToolId` | `Int64?` | yes |  | The business key identifier of the tool of the row. _(Replaced by Part)_ |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The unit of the row. |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) | The business key identifier of the row's VAT rate. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the row belongs to. |
| `WeightPerUnit` | `Decimal?` | yes |  | The weight per unit of the row. |
| `OrderDate` | `DateTimeOffset` | no |  | The order date of the row. |
| `ConversionFactor` | `Decimal` | no |  | The conversion factor of the row. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  | The row price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  | The setup price of the row in the company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes |  | The business key identifier of the company currency. |
| `StandardPrice` | `Decimal?` | yes |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's standard price currency. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's setup price currency. |
| `ShowPrice` | `Boolean` | no |  | Specifies if price should be shown for the row. |
| `PartRowType` | `Int32` | no |  | The part row type of the row. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the row. |
| `PartStatus` | `Int32?` | yes |  | The part status of the part at the time of row creation. |
| `OrderedQuantityInOrderUnit` | `Decimal` | no |  | The ordered quantity in the order unit. |
| `RestQuantity` | `Decimal` | no |  | The rest quantity of the row. |
| `DeliveredQuantity` | `Decimal` | no |  | The delivered quantity of the row. |
| `InitialDeliveryDate` | `DateTimeOffset?` | yes |  | The initial delivery date of the row. |
| `DesiredDeliveryDate` | `DateTimeOffset?` | yes |  | The desired delivery date of the row. |
| `RestQuantityInOrderUnit` | `Decimal` | no |  | The rest quantity in the order unit. |
| `DeliveredQuantityInOrderUnit` | `Decimal` | no |  | The delivered quantity in the order unit. |
| `CreationContext` | `Int32` | no |  | The creation context of the row. |
| `CustomerCommitmentLevel` | `Int32` | no |  | The customer commitment level of the row. |
| `PickingQuantity` | `Decimal?` | yes |  | The picking quantity of the row. |
| `AlternatePreparationCode` | `String` | no |  | The alternate preparation code of the row. |
| `Storage` | `String` | no |  | The storage specified by the row. |
| `ShowFreeTextIn` | `Int32` | no |  | Specifies which documents the free text row data will appear on. |
| `CreateManufacturingOrder` | `Boolean` | no |  | Specifies if a manufacturing order should be created for the row. |
| `CreatePurchaseOrder` | `Boolean` | no |  | Specifies if a purchase order should be created for the row. |
| `LinkedPurchaseOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The business key identifier of the row's linked purchase order row. |
| `LinkedManufacturingOrderId` | `Int64?` | yes | [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder) | The business key identifier of the row's linked manufacturing order. |
| `LinkedWithdrawalReservationId` | `Int64?` | yes |  | The business key identifier of the row's linked withdrawal reservation. References PartWithdrawalReservation. |
| `PlannedDateOfArrival` | `DateTimeOffset?` | yes |  | The planned date of arrival specified by the row. _(Unavailable)_ |
| `BacklogAmount` | `Decimal` | no |  | The backlog amount on the row. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) | The business key identifier of the row's statistical goods code. |
| `RowStatus` | `Int32` | no |  | The status of the customer order row. |
| `ParentOrderId` | `Int64` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the rows parent order. |
| `Dock` | `String` | no |  | The dock for the row (EDI). |
| `DockName` | `String` | no |  | The dock description for the row (EDI). |
| `KanbanNumber` | `String` | no |  | The kanban number for the row (EDI). |
| `CustomerOrderRowPosition` | `String` | no |  | The customer's order row position for the row. |
| `ReferenceNumberManufacturing` | `String` | no |  | The reference number for manufacturing for the row. |
| `ReferenceNumberDelivery` | `String` | no |  | The reference number for delivery for the row. |
| `ShowDeliveryDate` | `Boolean` | no |  | Specifies if the delivery date is shown on the row |
| `CreatedFrom` | `Int32` | no |  | Specifies what the row was created from. |
| `FixedAssetId` | `Int64?` | yes | [FixedAssets](Accounting.md#Accounting.FixedAsset) | The business key identifier of the rows fixed asset. |
| `LinkedStockOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The business key identifier of the rows linked stock order row. |
| `LinkedStockOrderRow` | `PurchaseOrderRows` | no | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The linked stock order row for the row. |
| `NewFinishDate` | `DateTimeOffset?` | yes |  | The new finish date for the row. |
| `TransferStatus` | `Int32` | no |  | The transfer status for the row. |
| `TransferProfileId` | `Int64?` | yes | [TransferProfiles](Common.md#Common.TransferProfile) | The business key identifier of the rows transfer profile. |
| `OrderNumberInRemoteCompany` | `String` | no |  | The order number in remote company for the row. |
| `PositionInRemoteCompany` | `Int64?` | yes |  | The position in remote company for the row. |
| `CodingId` | `Int64?` | yes |  | The business key identifier of the rows coding. |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) | The coding of the row. |
| `PaymentPlanRowId` | `Int64?` | yes |  | The business key identifier of the rows customer order payment plan row. |
| `IsCreditedPaymentPlanRow` | `Boolean` | no |  | Specifies if the row is a credited payment plan row. |
| `IsIncludedInPaymentPlan` | `Boolean` | no |  | Specifies if the row is included in payment plan. |
| `Status` | `Int32` | no |  | The status of the customer order. |
| `ProformaStatus` | `Int32` | no |  | The status of the row's proforma invoice. |
| `ProformaNumber` | `Int64?` | yes |  | The proforma number of the row. |
| `SubPartParentRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The business key identifier of the sub part row's parent row. |
| `QuantityRatio` | `Decimal?` | yes |  | The quantity ratio of the row. |
| `RowIndex` | `Int32?` | yes |  | The index of the row. |
| `SumRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The business key identifier of the row's sum row. |
| `PriceOrigin` | `Int32?` | yes |  | The price origin of the row. |
| `PriceOriginPriceListId` | `Int64?` | yes |  | The business key identifier of the row's original pricelist. |
| `DiscountIsLockedFromAutomaticChanges` | `Boolean` | no |  | Specifies if the row's discount is locked from automatic changes. |
| `IntrastatTransactionTypeId` | `Int64?` | yes | [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat) | The business key identifier of the row's intrastat transaction type. |
| `IntrastatTransactionType` | `TransactionTypeIntrastats` | no | [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat) | The intrastat transaction type of the row. |
| `TariffAndServiceCodeId` | `Int64?` | yes | [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode) | The business key identifier of the row's tariff and service code. |
| `TariffAndServiceCode` | `TariffAndServiceCodes` | no | [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode) | The tariff and service code of the row. |
| `PartConfigurationId` | `Int64?` | yes |  | The business key identifier of the row's part configuration. |
| `RowsGoodsLabel` | `String` | no |  | The rows goods label specified by the row. |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityCustomerOrders](Sales.md#Sales.OrderQuantityCustomerOrder) | The business key identifier of order quantity. |
| `OrderQuantity` | `OrderQuantityCustomerOrders` | no | [OrderQuantityCustomerOrders](Sales.md#Sales.OrderQuantityCustomerOrder) | Order quantity that holds the partial quantities. |
| `CustomerOrderTransferRowIdentifier` | `Guid?` | yes |  | The customer order transfer row identifier. |
| `PartConfigurationIdInRemoteCompany` | `Int64?` | yes | [PartConfigurations](Common.md#Common.PartConfiguration) | The business key identifier of the row's part configuration in the remote company. |
| `PriceLockedFromAutomaticChanges` | `Boolean?` | yes |  | Specifies if the rows price is locked from automatic changes. |
| `SerialNumberInformation` | `SerialNumberOrderRowInformation[]` | no |  | The serial number information of customer order row |
| `DiscountRows` | `CustomerOrderOrderRowDiscounts[]` | no | [CustomerOrderOrderRowDiscounts](Sales.md#Sales.CustomerOrderOrderRowDiscount) | The discount rows for the row. |
| `ComparativePrice` | `Decimal?` | yes |  | The manually edited comparative price for the row. Note if this price is automatically calculated it is not stored here. |
| `ComparativePriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's manually edited comparative price currency. |
| `BlanketOrderSalesRowId` | `Int64?` | yes | [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow) | The business key identifier of the row's blanket order sales row. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer order. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the payment term of the customer order. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The payment term of the customer order. |
| `PaymentTermDescription` | `String` | no |  | The payment term description of the customer order. |
| `GracePeriodInDays` | `Int32?` | yes |  | The customer order's grace period in days. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the customer order's delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) | The business key identifier of the customer order's delivery term. |
| `DeliveryTermDescription` | `String` | no |  | The delivery term description of the customer order. |
| `DeliveryMethodDescription` | `String` | no |  | The delivery method description of the customer order. |
| `ShipmentPayer` | `Int32` | no |  | Specifies who is responsible for the shipment payment for the customer order. |
| `BusinessContactOrderNumber` | `String` | no |  | The end-customer's order number for the customer order. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of our reference for the customer order. Reference Persons |
| `OurReferenceName` | `String` | no |  | The name of our reference for the customer order. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the customer's reference for the customer order. |
| `BusinessContactReferenceName` | `String` | no |  | The name of the customer's reference for the customer order. |
| `GoodsLabel` | `String` | no |  | The goods label of the customer order. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency of the customer order. |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) | The business key identifier of the VAT group that applies for the customer order. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the customer order belongs to. |
| `Priority` | `Int32` | no |  | The priority of the customer order. |
| `ProjectId` | `Int64?` | yes |  | The business key identifier of the customer order's project. |
| `SendMethod` | `Int32` | no |  | Specifies the printout method for the customer order. |
| `InvoicePrintoutMethod` | `Int32` | no |  | Specifies the printout method that should be used for invoices. |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the customer order's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the customer order. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the customer order's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The external comment of the customer order. |
| `TransportTime` | `Int32?` | yes |  | The transport time of the customer order in workdays. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the customer order. |
| `Version` | `Int32` | no |  | The version of the customer order. |
| `UseForwardRate` | `Boolean` | no |  | Specifies if forward rate should apply for the customer order. |
| `ExchangeRate` | `Decimal` | no |  | Specifies the exchange rate to use for the customer order. |
| `OrderAmount` | `Decimal` | no |  | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `OrderAmountInCompanyCurrency` | `Decimal` | no |  | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `CustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer that the customer order belongs to. |
| `InvoiceCustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) | The business key identifier of the invoice customer that the customer order belongs to. |
| `OrderNumber` | `String` | no |  | The human readable identifier of the customer order. |
| `OrderDate` | `DateTimeOffset` | no |  | The order date of the customer order. |
| `Rows` | `CustomerOrderRows[]` | no | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The rows of the customer order. |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the customer order's seller. |
| `ShowPriceInAcknowledgement` | `Boolean` | no |  | Specifies if price should be shown in the acknowledgement of the customer order. |
| `ShowTotalInAcknowledgement` | `Boolean` | no |  | Specifies if the price total should be shown in the acknowledgement of the customer order. |
| `ThirdPartyTrading` | `Boolean` | no |  | Specifies if the customer order falls under third party trading. |
| `DeliveryInstruction` | `String` | no |  | The delivery instruction of the customer order. |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer source of the active delivery address. |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier source of the active delivery address. |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  | The business key identifier of the company source of the active delivery address. |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  | Specifies the source of the customer order delivery address. |
| `IsCredit` | `Boolean` | no |  | Specifies if the customer order is on credit or not. |
| `InvoiceType` | `Int32` | no |  | The invoice type of the customer order. |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](Common.md#Common.PaymentMethod) | The business key identifier of the customer order's payment method. |
| `PaymentMethod` | `PaymentMethods` | no | [PaymentMethods](Common.md#Common.PaymentMethod) | The payment method on the customer order. |
| `PrintoutTimeStamp` | `DateTimeOffset` | no |  | The date/time when the printout of the customer order was made. _(Printout date is not stored on the order)_ |
| `ConsigneeReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the customer order's consignee reference. |
| `ConsigneeReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The consignee reference on the customer order. |
| `PrintoutBy` | `String` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The user name of the ApplicationUsers that printed the customer order. _(Printout user is not stored on the order)_ |
| `Preliminary` | `Boolean` | no |  | Specifies if the customer order is to be considered preliminary. |
| `ConsigneeReferenceName` | `String` | no |  | The consignee reference name of the customer order. |
| `DestinationForDeliveryTerm` | `String` | no |  | The destination for the delivery term. |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The business key identifier of the customer account group of the customer order. _(Replaced by AccountGroupId)_ |
| `SupplierAccountGroupId` | `Int64?` | yes |  | The business key identifier of the supplier account group of the customer order. References a SupplierAccountGroup _(Refer to DeliveryAddress)_ |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the customer order's delivery address. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The delivery address of the customer order. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the customer order's mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The mailing address of the customer order. |
| `InvoiceAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the customer order's invoice address. |
| `InvoiceAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The invoice address of the customer order. |
| `InvoiceStatusPending` | `Boolean` | no |  | Specifies if the invoice created for the customer order should start out as pending. |
| `IsPartOfComprehensiveInvoice` | `Boolean` | no |  | Specifies if the customer order is part of a comprehensive invoice. _(Replaced by ComprehensiveInvoiceGroupingMode)_ |
| `ComprehensiveInvoiceGroupingMode` | `Int32` | no |  | Specifies if the customer order is part of a comprehensive invoice, and how they are grouped. |
| `HasInvoicingCharge` | `Boolean` | no |  | Specifies if the customer order involves an invoicing charge. |
| `GoodsAddressNumber` | `String` | no |  | The goods address number of the customer order. |
| `VatNumber` | `String` | no |  | The VAT number of the customer order. |
| `Dock` | `String` | no |  | The dock of the customer order. |
| `FromQuoteNumber` | `String` | no |  | The human readable identifier of the quote that resulted in the customer order. |
| `Status` | `Int32` | no |  | The status of the customer order. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) | The communication addresses registered on the customer order. |
| `PrintProformaInvoiceVia` | `Int32?` | yes |  | The preferred Proforma printout method of the customer. |
| `OrderTypeId` | `Int64?` | yes | [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType) | The business key identifier of the customer order's order type. |
| `OrderType` | `CustomerOrderTypes` | no | [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType) | The order type used on the customer order. |
| `IsStockOrder` | `Boolean` | no |  | Specifies if the customer order is stock order. |
| `ExcludeFromEdi` | `Boolean` | no |  | Specifies if the customer order will be excluded from EDI. |
| `IncludeInDeliveryAnalysis` | `Boolean?` | yes |  | Specifies if the customer order will be included in delivery analysis. |
| `PartialDeliveryType` | `Int32` | no |  | The partial delivery type on the customer order. |
| `DeliveryHorizon` | `TimeSpan?` | yes |  | The delivery horizon on the customer order. |
| `DeliveryNoteNumberWhenDeliveryPlanning` | `Boolean` | no |  | Specifies if using delivery note number when delivery planning on the customer order. |
| `AftermarketProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the customer order's aftermarket product record. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of the customer order's purchase order. |
| `PurchaseOrder` | `PurchaseOrders` | no | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The purchase order on the customer order. |
| `PaymentPlanTemplateId` | `Int64?` | yes | [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate) | The business key identifier of the customer order's payment plan template. |
| `PaymentPlanTemplate` | `PaymentPlanTemplates` | no | [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate) | The payment plan template on the customer order. |
| `UnpaidAdvanceWarningType` | `Int32` | no |  | The unpaid advance warning type on the customer order. |
| `CreatedFrom` | `Int32` | no |  | Specifies what the customer order was created from. |
| `ShippingInformationId` | `Int64?` | yes |  | The business key identifier of the customer order's shipping information. |
| `ShippingInformationRows` | `CustomerOrderShippingInformationRows[]` | no | [CustomerOrderShippingInformationRows](Sales.md#Sales.CustomerOrderShippingInformationRow) | The shipping information rows on the customer order. |
| `ExcludeFromPaymentPlanReconciliation` | `Boolean` | no |  | Specifies if the customer order is excluded from payment plan reconciliation. |
| `ResetPaymentPlanDifferenceAmount` | `Decimal?` | yes |  | The reset payment plan difference amount on the customer order. |
| `ResetPaymentPlanDifferenceAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the customer order's reset payment plan difference amount currency. |
| `ResetPaymentPlanDifferenceAmountCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The reset payment plan difference amount currency on the customer order. |
| `TransferStatus` | `Int32` | no |  | The transfer status of the customer order. |
| `CreatedInCompanyWithRole` | `Int32?` | yes |  | The role of the company who created the customer order. |
| `AccountGroupId` | `Int64` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The business key identifier of the account group of the customer order. |
| `AccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The account group on the customer order. |
| `CategoryString` | `String` | no |  | The category string on the customer order. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the customer order's currency exchange type. |
| `EditedOrderAmountExcludingVat` | `Decimal?` | yes |  | The edited order amount excluding VAT for the customer order. |
| `EditedOrderAmountExcludingVatCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The currency of the edited order amount excluding VAT for the customer order. |
| `EditedOrderAmountDiscount` | `Decimal?` | yes |  | The edited order amount discount in percent for the customer order. |
| `TypeOfOrderAmountEntered` | `Int32?` | yes |  | The type of edited order value entered on the customer order. |
| `ReasonCodeDebitNoteId` | `Int64?` | yes | [ReasonCodeDebitNotes](Common.md#Common.ReasonCodeDebitNote) | The business key identifier of the customer order's reason code debit note. |
| `ReasonCodeDebitNote` | `ReasonCodeDebitNotes` | no | [ReasonCodeDebitNotes](Common.md#Common.ReasonCodeDebitNote) | The reason code debit note on the customer order. |
| `Factoring` | `Boolean` | no |  | Specifies if factoring is activated for the customer order. |
| `ReferenceCode` | `String` | no |  | The customer's reference code on the customer order. |
| `PickInstructionId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the customer order's pick instruction. |
| `PickInstruction` | `Comments` | no | [Comments](Common.md#Common.Comment) | The pick instruction of the customer order. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer order shipping information row. |
| `Quantity` | `Decimal` | no |  | The quantity of the customer order shipping information row. |
| `NetWeight` | `Decimal` | no |  | The net weight of the customer order shipping information row. |
| `Weight` | `Decimal` | no |  | The weight of the customer order shipping information row. |
| `Volume` | `Decimal` | no |  | The volume of the customer order shipping information row. |
| `LoadingMeters` | `Decimal` | no |  | The loading meters of the customer order shipping information row. |
| `Length` | `Decimal` | no |  | The length of the customer order shipping information row. |
| `Width` | `Decimal` | no |  | The width of the customer order shipping information row. |
| `Height` | `Decimal` | no |  | The height of the customer order shipping information row. |
| `PackageTypeId` | `Int64` | no | [PackageTypes](Inventory.md#Inventory.PackageType) | The business key identifier of the customer order shipping information row's package type. |
| `PackageType` | `PackageTypes` | no | [PackageTypes](Inventory.md#Inventory.PackageType) | The package type of the customer order shipping information row. |
| `GoodsTypeId` | `Int64` | no | [GoodsTypes](Inventory.md#Inventory.GoodsType) | The business key identifier of the customer order shipping information row's goods type. |
| `GoodsType` | `GoodsTypes` | no | [GoodsTypes](Inventory.md#Inventory.GoodsType) | The goods type of the customer order shipping information row. |
| `PackagingPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the customer order shipping information row's packaging part. |
| `PackagingPart` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The packaging part of the customer order shipping information row. |
| `ParentId` | `Int64?` | yes |  | The business key identifier of the customer order shipping information row's parent. |

**References out:** [GoodsTypes](Inventory.md#Inventory.GoodsType), [PackageTypes](Inventory.md#Inventory.PackageType), [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [CustomerOrders](Sales.md#Sales.CustomerOrder)

<a id="Sales.CustomerOrderType"></a>
### CustomerOrderTypes

Represents a customer order type.

- **Endpoint:** `GET /api/v1/Sales/CustomerOrderTypes`
- **Required permission:** Show order types
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the type. |
| `Number` | `Int64` | no |  | The human readable identifier of the type. |
| `Prefix` | `String` | no |  | The prefix applied to customer order numbers for this type. |
| `Description` | `String` | no |  | The translated description of the type. |
| `Priority` | `Int32` | no |  | The priority of the type. |
| `Visible` | `Boolean` | no |  | Specifies if the type is visible. |
| `IsPreset` | `Boolean` | no |  | Specifies if the type is a preset type. |
| `PriceSetting` | `Int32` | no |  | The price settings of the type. |
| `PriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) | The business key identifier of the type's price list. |
| `IncludeInDeliveryAnalysis` | `Boolean` | no |  | Specifies if customer orders of this type should be included in delivery analysis. |
| `IncludeInStatistics` | `Boolean` | no |  | Specifies if customer orders of this type should be included in statistics. |
| `InvoiceType` | `Int32?` | yes |  | The default invoice type of customer orders created with this type. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the type's default payment term. References a PaymentTerms |
| `PurchaseOrderAddressStrategy` | `Int32` | no |  | The purchase order from customer order address strategy to use for customer orders of this type. |
| `BaseType` | `Int32` | no |  | The base type of customer orders created using this type. |
| `CodingGroupId` | `Int64` | no |  | The business key identifier of the type's coding group. |
| `RateTypeSetting` | `Int32` | no |  | The rate type setting of the customer order type. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the customer order type's currency exchange type. |
| `DefaultTransferProfileId` | `Int64?` | yes | [TransferProfiles](Common.md#Common.TransferProfile) | The business key identifier of the customer order's default transfer profile. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer part link. |
| `CustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer part link customer. References Customers . |
| `CustomerPartNumber` | `String` | no |  | The part number that the customer uses to identify the part. |
| `PackagingPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the customer part link packaging part. References Parts . |
| `Gs1Code` | `String` | no |  | The GS1 code of the customer part link. |
| `SalesCommentShowInForms` | `Int32` | no |  | Specifies which documents the sales comment of the part link will be shown on. |
| `QuantityForLeadTimeToCustomer` | `Decimal?` | yes |  | The quantity for lead time. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the customer part link's part. |
| `Price` | `Decimal?` | yes |  | The price of the customer part link. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price of the customer part link. |
| `LeadTime` | `TimeSpan?` | yes |  | The lead time of the customer part link. |
| `Discount` | `Decimal?` | yes |  | The discount percentage of the customer part link. |
| `PriceValidThrough` | `DateTimeOffset?` | yes |  | The date/time offset that the customer part link price is valid through. |
| `FuturePrice` | `Decimal?` | yes |  | The future price of the customer part link. |
| `FuturePriceValidThrough` | `DateTimeOffset?` | yes |  | The date/time offset that the future customer part link price is valid through. |
| `FutureSetupPrice` | `Decimal?` | yes |  | The future setup price of the customer part link. |
| `QuantityPerPackage` | `Decimal?` | yes |  | The quantity per package of the customer part link. |
| `PickingCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the customer part link picking comment. References Comments . |
| `PickingComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The customer part link picking comment. |
| `OverrideSalesCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the customer part link override sales comment. References Comments . |
| `OverrideSalesComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The customer part link override sales comment. |
| `UnitId` | `Int64` | no | [Units](Common.md#Common.Unit) | The business key identifier of the customer part link unit. References Units . |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The customer part link unit. |
| `PriceCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the customer part link price currency. References Currencies . |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The customer part link price currency. |
| `PriceCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifer of the customer part link price comment. References Comments . |
| `PriceComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The customer part link price comment. |
| `StaggeredPrices` | `StaggeredPrices[]` | no | [StaggeredPrices](Common.md#Common.StaggeredPrice) | The staggered prices on the part link. |

- `SalesCommentShowInForms` (bitmask) — None=0, Quote=1, Acknowledgement=2, DeliveryNote=4, Invoice=8, ProFormaInvoice=16

**References out:** [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [Customers](Sales.md#Sales.Customer), [Parts](Inventory.md#Inventory.Part), [StaggeredPrices](Common.md#Common.StaggeredPrice), [Units](Common.md#Common.Unit)
**Referenced by:** [Customers](Sales.md#Sales.Customer), [Parts](Inventory.md#Inventory.Part)

<a id="Sales.CustomerRelationshipActivityType"></a>
### CustomerRelationshipActivityTypes

Represents a customer relationship activity type.

- **Endpoint:** `GET /api/v1/Sales/CustomerRelationshipActivityTypes`
- **Required permission:** Show customer
- **Introduced in:** 2.55

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer relationship activity type. |
| `Code` | `Int64` | no |  | The human readable identifier of the activity type. |
| `Description` | `String` | no |  | The description of the activity type. |
| `Sources` | `Int32` | no |  | Specifies where this activity type can be used. |

- `Sources` (bitmask) — Part=1, Quote=2, CustomerOrder=4, Customer=8, PurchaseOrder=16, Inquiry=32, BlanketOrderPurchase=64, Supplier=128, BlanketOrderSales=256, SalesAgreement=512, PurchaseAgreement=1024, BusinessOpportunity=2048

**Referenced by:** [BusinessOpportunityActivityTemplateRows](Sales.md#Sales.BusinessOpportunityActivityTemplateRow), [CustomerOrderActivities](Sales.md#Sales.CustomerOrderActivity), [CustomerRelationshipManagementActivities](Sales.md#Sales.CustomerRelationshipManagementActivity), [QuoteActivities](Sales.md#Sales.QuoteActivity)

<a id="Sales.CustomerRelationshipManagementActivity"></a>
### CustomerRelationshipManagementActivities

Represents a customer relationship management activity.

- **Endpoint:** `GET /api/v1/Sales/CustomerRelationshipManagementActivities`
- **Required permission:** Show customer
- **Introduced in:** 2.55

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer relationship management activity. |
| `CustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) | The business key identifier of the activity's customer. |
| `IsMandatory` | `Boolean` | no |  | Specify if the activity is mandatory. |
| `AdministratorType` | `Int32?` | yes |  | The administrator type of the activity. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the activity's business contact reference. |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The activity's business contact reference. |
| `OrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the activity's customer order. |
| `ActivityTypeId` | `Int64?` | yes | [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType) | The business key identifier of the activity's customer relationship activity type. |
| `ActivityType` | `CustomerRelationshipActivityTypes` | no | [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType) | The type of the activity. |
| `CalendarAppointmentId` | `String` | no |  | The unique identifier of the appointment created in the user's calendar program for the activity. |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that has completed the activity. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that is responsible for the activity. |
| `Description` | `String` | no |  | The description of the activity. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the activity's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the activity. |
| `Status` | `Int32` | no |  | The status of the activity. |
| `ReminderId` | `Int64?` | yes |  | The business key identifier of the activity's reminder. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  | The planned completion date of the activity. |
| `CompletionDate` | `DateTimeOffset?` | yes |  | The completion date of the activity. |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  | The planned start date of the activity. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  | The actual start date of the activity. |
| `IsAdministratorResponsibleUser` | `Boolean` | no |  | Specify if the activity's responsible user is synced with the customer's account manager. |
| `IsAdministratorResponsibleUserRestorable` | `Boolean` | no |  | Specify if the activity's responsible user should be changed when changing customer's account manager. |
| `IsDueDatePlannedCompletionDateRestorable` | `Boolean` | no |  | Specify if the activity's planned completion date can be changed from the customer orders delivery date. |

- `AdministratorType` — CustomerResponsible=0, Seller=1
- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType), [Customers](Sales.md#Sales.Customer)

<a id="Sales.Customer"></a>
### Customers

Represents a customer.

- **Endpoint:** `GET /api/v1/Sales/Customers`
- **Required permission:** Show customer
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the customer. |
| `Name` | `String` | no |  | The name of the customer. |
| `Code` | `String` | no |  | The human readable identifier of the customer. |
| `AlternativeName` | `String` | no |  | The alternative name of the customer. |
| `CorporationIdentificationNumber` | `String` | no |  | The corporation identification number of the customer. |
| `PersonalNumber` | `String` | no |  | The personal number of the customer. |
| `IsPrivateCustomer` | `Boolean` | no |  | Specifies if the customer is a private person. |
| `VatNumber` | `String` | no |  | The VAT number of the customer. |
| `DeliveryAddresses` | `DeliveryAddresses[]` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The delivery addresses of the customer. |
| `ActiveDeliveryAddressId` | `Int64` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The business key identifier of the customer's active delivery address. |
| `ActiveDeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The active delivery address of the customer. |
| `References` | `BusinessContactReferences[]` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business contact references belonging to the customer. |
| `DefaultReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the customer's default business contact reference. |
| `DefaultReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The default reference of the customer. |
| `Alias` | `String` | no |  | The alias code of the customer. |
| `AlloyCost` | `Int32` | no |  | The alloy cost associated with the customer. |
| `ApplyBankCharge` | `Boolean` | no |  | Specifies if bank charge should be applied for the customer. |
| `ApplyInvoicingCharge` | `Boolean` | no |  | Specifies if invoicing charge should be applied for the customer. |
| `ApplyReminderCharge` | `Boolean` | no |  | Specifies if reminder charge should be applied for the customer. |
| `AccountManagerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the customer's account manager. |
| `AccountManager` | `Persons` | no | [Persons](Common.md#Common.Person) | The account manager of the customer. |
| `ActiveDeliveryAddressAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The business key identifier of the customer's active delivery address account group. |
| `ActiveDeliveryAddressAccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The active delivery address account group of the customer. |
| `ActualCustomerProbabilityId` | `Int64?` | yes | [Probabilities](Common.md#Common.Probability) | The business key identifier of the customer's actualization probability. |
| `ActualCustomerProbability` | `Probabilities` | no | [Probabilities](Common.md#Common.Probability) | The actualization probability of the customer. |
| `AttachDatafileWithOrder` | `Boolean` | no |  | Specifies if data file should be attached with orders for the customer. |
| `AttachDatafileWithInvoice` | `Boolean` | no |  | Specifies if data file should be attached with invoices for the customer. |
| `AttachDatafileWithCase` | `Boolean` | no |  | Specifies if data file should be attached with cases for the customer. |
| `AttachDatafileWithPart` | `Boolean` | no |  | Specifies if data file should be attached with parts for the customer. |
| `AttachDatafileWithDispatchAdvice` | `Boolean` | no |  | Specifies if data file should be attached with dispatch advice for the customer. |
| `BankChargeAmount` | `Decimal` | no |  | The bank charge amount of the customer. |
| `BankGiroNo` | `String` | no |  | The bank giro number of the customer. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that blocked the entity. |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The application user that blocked the customer. |
| `BlockedStatus` | `Int32` | no |  | The block status of the entity. |
| `BlockedContextType` | `Int32` | no |  | Specifies in which contexts that the customer is blocked. |
| `BlockMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) | The block message that applies for the customer. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  | The date when the entity stops being blocked. |
| `CategoryString` | `String` | no |  | The category string of the customer. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the customer's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the customer. |
| `CompanyId` | `Int64` | no |  | The business key identifier of the company that the customer belongs to. |
| `ConfigurationPriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) | The business key identifier of the configuration price list that the customer belongs to. |
| `CreditLimit` | `Decimal` | no |  | The credit limit of the customer. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the customer's currency. |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The currency of the customer. |
| `DateDisplayFormat` | `Int32` | no |  | The date display format of the customer. |
| `DecimalSymbol` | `String` | no |  | The decimal symbol of the customer. |
| `DeliveryHorizon` | `Int64?` | yes |  | The delivery horizon of the customer. |
| `DeliveryNoteNumberWhenDeliveryPlanning` | `Boolean` | no |  | The delivery note number when delivery planning of the customer. |
| `DistrictId` | `Int64?` | yes | [CustomerDistricts](Sales.md#Sales.CustomerDistrict) | The business key identifier of the district that the customer belongs to. |
| `District` | `CustomerDistricts` | no | [CustomerDistricts](Sales.md#Sales.CustomerDistrict) | The district that the customer belongs to. |
| `DateForTransitionToActualContact` | `DateTimeOffset?` | yes |  | The date/time when transition to actual contact was made for the customer. Changed from DateTimeOffset to DateTimeOffset? in 26.3 |
| `Discount` | `Decimal?` | yes |  | The general discount of the customer. |
| `DiscountCategoryId` | `Int64?` | yes | [DiscountCategories](Common.md#Common.DiscountCategory) | The business key identifier of the discount category that applies for the customer. |
| `DiscountCategory` | `DiscountCategories` | no | [DiscountCategories](Common.md#Common.DiscountCategory) | The discount category that applies for the customer. |
| `DefaultOrderPrintoutVia` | `Int32` | no |  | The preferred order printout method of the customer. |
| `PrintProformaInvoiceVia` | `Int32` | no |  | The preferred Proforma printout method of the customer. |
| `PrintPaymentReminderVia` | `Int32` | no |  | The preferred payment reminder printout method of the customer. |
| `DeliveryInstruction` | `String` | no |  | The delivery instruction of the customer. |
| `DefaultInvoiceStatusPending` | `Boolean` | no |  | Specifies if invoices should be pending by default for the customer. |
| `EdiCode` | `String` | no |  | The EDI code of the customer. _(Replaced by OtherCustomerNumbers)_ |
| `EInvoiceElectronicAddressIdentifier` | `String` | no |  | The e-invoice electronic address identifier of the customer. |
| `EInvoiceId` | `String` | no |  | The e-invoice id of the customer. |
| `EInvoiceOperatorCode` | `String` | no |  | The e-invoice operator code of the customer. |
| `Factoring` | `Boolean` | no |  | Specifies if factoring applies for the customer. |
| `GracePeriod` | `TimeSpan?` | yes |  | The grace period of the customer. |
| `HideDiscountOnProformaInvoice` | `Boolean` | no |  | Specifies if the customer hides discount on proforma invoices. _(Replaced by CustomerCountryDocumentSettings)_ |
| `IncludeInDeliveryAnalysis` | `Boolean?` | yes |  | Specifies if the customer is included in delivery analysis. |
| `InvoiceAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the customer's invoice address. If there is no value here use MailingAddressId. |
| `InvoiceAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The invoice address of the customer. If there is no value here use MailingAddress. |
| `InterestType` | `Int32` | no |  | Specifies the interest type of the customer. |
| `IsCasualCustomer` | `Boolean` | no |  | Specifies if the customer is a stray customer. |
| `InterestInvoiceDays` | `Int32?` | yes |  | Specifies the interest invoice days for the customer. |
| `InsuranceCost` | `Decimal` | no |  | The insurance cost specified for the customer. |
| `InvoiceCustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the invoice customer of the customer. |
| `InvoicePrintoutMethod` | `Int32` | no |  | The customer's preferred printout method for invoices. |
| `InvoicePrintoutOccasion` | `Int32` | no |  | Specifies when invoices should be printed for the customer. |
| `IsInternal` | `Boolean` | no |  | Specifies if the customer is internal. |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The business key identifier of the customer's preferred language. |
| `Language` | `LanguageCodes` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The language of the customer. |
| `LatePaymentFee` | `Decimal?` | yes |  | The late payment fee of the customer. |
| `MailingAddressId` | `Int64` | no | [Addresses](Common.md#Common.Address) | The business key identifier of the customer's mailing address. If InvoiceAddressId does not have a value this is also used as invoice adress. |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The mailing address of the customer. If InvoiceAddressId does not have a value this is also used as invoice adress. |
| `NumberOfInvoiceCopies` | `Int32?` | yes |  | The number of invoice copies that should be produced for the customer. |
| `OurCodeByYou` | `String` | no |  | The supplier code assigned to us by the customer. |
| `PalletRegistrationNo` | `String` | no |  | The customer's pallet registration number. |
| `PartialDeliveryType` | `Int32` | no |  | The partial delivery type of the customer. |
| `PaymentPlanTemplateId` | `Int64?` | yes | [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate) | The business key identifier of the customer's payment plan template. |
| `PaymentPlanTemplate` | `PaymentPlanTemplates` | no | [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate) | The payment plan template of the customer. |
| `PaymentTermId` | `Int64` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the customer's payment term. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The payment term of the customer. |
| `PlusGiroNo` | `String` | no |  | The PlusGiro number of the customer. |
| `PriceListId` | `Int64` | no | [PriceLists](Common.md#Common.PriceList) | The business key identifier of the customer's price list. |
| `Priority` | `Int32` | no |  | The priority of the customer. |
| `PickingListCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the customer's picking list comment. |
| `PickingListComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The picking list comment of the customer. |
| `ProformaInvoicePrintoutOccasion` | `Int32` | no |  | Specifies when proforma invoices should be printed for the customer. |
| `ResellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the customer's reseller. |
| `Reseller` | `Resellers` | no | [Resellers](Common.md#Common.Reseller) | The reseller of the customer. |
| `RoundOff` | `Boolean` | no |  | Specifies if round off applies for the customer. |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the customer's seller. |
| `Seller` | `Persons` | no | [Persons](Common.md#Common.Person) | The seller of the customer. |
| `ServiceAgreementId` | `Int64?` | yes |  | The business key identifier of the customer's service agreement. |
| `ServiceTaxNumber` | `String` | no |  | The service tax number of the customer. |
| `ShowPartStatisticalGoodsCodeAndCountryOfOriginInForms` | `Int32` | no |  | New properties available: ShowPartStatisticalGoodsCodeInForms and ShowCountryOfOriginInForms. Try to use new properties instead. _(Replaced by ShowPartStatisticalGoodsCodeInForms and ShowCountryOfOriginInForms)_ |
| `ShowPartStatisticalGoodsCodeInForms` | `Int32` | no |  | Specifies which documents should display statistical goods codes for the customer. _(Replaced by CustomerCountryDocumentSettings)_ |
| `ShowCountryOfOriginInForms` | `Int32` | no |  | Specifies which documents should show country of origin for the customer. _(Replaced by CustomerCountryDocumentSettings)_ |
| `ShowPartWeightInForms` | `Int32` | no |  | Specifies which documents should show part weight for the customer. _(Replaced by CustomerCountryDocumentSettings)_ |
| `StatusId` | `Int64` | no | [CustomerStatuses](Sales.md#Sales.CustomerStatus) | The business key identifier of the customer's status. |
| `Status` | `CustomerStatuses` | no | [CustomerStatuses](Sales.md#Sales.CustomerStatus) | The status of the customer. |
| `TimeZone` | `String` | no |  | The time zone of the customer. Specified as a time zone identifier (e.g. "W. Europe Standard Time"). |
| `TimeZoneOffset` | `Decimal` | no |  | The time zone offset of the customer. _(Replaced by TimeZone)_ |
| `ToleranceForLateDelivery` | `TimeSpan?` | yes |  | The customer's tolerance for late delivery. |
| `ToleranceForEarlyDelivery` | `TimeSpan?` | yes |  | The customer's tolerance for early delivery. |
| `TypeId` | `Int64?` | yes | [CustomerTypes](Sales.md#Sales.CustomerType) | The business key identifier of the customer's type. |
| `Type` | `CustomerTypes` | no | [CustomerTypes](Sales.md#Sales.CustomerType) | The type of the customer. |
| `Url` | `String` | no |  | The URL of the customer. |
| `UseBundling` | `Boolean?` | yes |  | Specifies if the customer uses bundling. |
| `UseComprehensiveInvoices` | `Boolean` | no |  | Specifies if comprehensive invoices should be used for the customer. _(Replaced by ComprehensiveInvoiceGroupingMode)_ |
| `ComprehensiveInvoiceGroupingMode` | `Int32` | no |  | Specifies if comprehensive invoices should be used for the customer and if so, what they should be grouped on. |
| `UseDeliveryNoteCollectionFormReport` | `Boolean` | no |  | Specifies if comprehensive delivery notes should be used for the customer. |
| `UseEInvoicing` | `Boolean` | no |  | Specifies if the customer uses e-invoicing. |
| `UseForwardRate` | `Boolean` | no |  | Specifies if forward rate should be used for the customer. |
| `UseInvoiceCustomersVatNumber` | `Boolean` | no |  | Specifies if VAT number should be taken via the invoice customer. |
| `UsePackageSpecification` | `Boolean?` | yes |  | Specifies if the customer uses package specification. |
| `UseReminder` | `Boolean` | no |  | Specifies if reminders should be enabled for the customer. |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) | The business key identifier of the customer's VAT rate. _(Replaced by VatGroupId on DeliveryAddress)_ |
| `VatRate` | `VatRates` | no | [VatRates](Common.md#Common.VatRate) | The VAT rate of the customer. _(Replaced by VatGroup from DeliveryAddress)_ |
| `ValidityTimeId` | `Int64` | no | [ValidityTimes](Sales.md#Sales.ValidityTime) | The business key identifier of the customer's validity time. |
| `ValidityTime` | `ValidityTimes` | no | [ValidityTimes](Sales.md#Sales.ValidityTime) | The validity time of the customer. |
| `Version` | `Int32` | no |  | The version of the customer. |
| `VisitingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the customer's visiting address. |
| `VisitingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The visiting address of the customer. |
| `CustomerPartLinks` | `CustomerPartLinks[]` | no | [CustomerPartLinks](Sales.md#Sales.CustomerPartLink) | The part links defined for the customer. |
| `CaseEntries` | `CaseEntry[]` | no | [CaseEntry](Inventory.md#Inventory.CaseEntry) | A collection of case entries that belong to the customer. |
| `OtherCustomerNumbers` | `OtherCustomerNumbers[]` | no | [OtherCustomerNumbers](Sales.md#Sales.OtherCustomerNumber) | Available other customer numbers. Mainly used as EDI identifiers. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) | The communication addresses for the customer. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) | A collection of extra field values for the customer. |
| `PreliminaryPickingList` | `Boolean` | no |  | Specifies if the customer should apply preliminary picking list. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the customer's currency exchange type. |
| `RootId` | `Int64` | no |  | The business key identifier of the customer's root entity. |
| `EmployeeSpanId` | `Int64?` | yes |  | The business key identifier of employee span of customer |
| `EmployeeSpan` | `CustomerEmployeeSpans` | no | [CustomerEmployeeSpans](Sales.md#Sales.CustomerEmployeeSpan) | The employee span of customer |
| `TinNumber` | `String` | no |  | The customer's income tax reference number |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the status. |
| `Code` | `Int64` | no |  | The human readable identifier of the status. |
| `Description` | `String` | no |  | The translated description of the status. |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |

**Referenced by:** [Customers](Sales.md#Sales.Customer)

<a id="Sales.CustomerType"></a>
### CustomerTypes

Represents a customer type.

- **Endpoint:** `GET /api/v1/Sales/CustomerTypes`
- **Required permission:** Show customer
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the type. |
| `Code` | `Int64` | no |  | The human readable identifier of the type. |
| `Description` | `String` | no |  | The translated description of the type. |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |

**Referenced by:** [Customers](Sales.md#Sales.Customer)

<a id="Sales.InvoiceLog"></a>
### InvoiceLogs

Represents an invoice log entry.

- **Endpoint:** `GET /api/v1/Sales/InvoiceLogs`
- **Required permission:** Show customer orders
- **Introduced in:** 2.55

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the invoice log entry. |
| `InvoiceId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) | The business key identifier of accounts receivable of the log entry. |
| `LoggingTimestamp` | `DateTimeOffset` | no |  | The date when the log entry was created. |
| `InvoiceDate` | `DateTimeOffset` | no |  | The invoice date of the log entry. |
| `InvoiceNumber` | `Int64` | no |  | The invoice number of the log entry. |
| `DeliveryRowId` | `Int64?` | yes | [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow) | The business key identifier for the customer order delivery row of the log entry. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier for the part of the log entry. |
| `PartNumber` | `String` | no |  | The part number of the log entry. |
| `PartCategory` | `String` | no |  | The part category of the log entry. |
| `PartCode` | `String` | no |  | The part code of the log entry. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier for the customer of the log entry. |
| `CustomerCode` | `String` | no |  | The customer code of the log entry. |
| `CustomerGroup` | `Int64?` | yes |  | The customer account group number of the log entry. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier for the customer order of the log entry. |
| `CustomerOrderNumber` | `String` | no |  | The customer order number of the log entry. |
| `WarehouseId` | `Int64?` | yes | [Warehouses](Common.md#Common.Warehouse) | The business key identifier for the warehouse of the log entry. |
| `UserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier for the application user of the log entry. |
| `UserName` | `String` | no |  | The user name of the log entry. |
| `Seller` | `String` | no |  | The seller of the log entry. |
| `OrderedQuantity` | `Decimal` | no |  | The ordered quantity of the log entry. |
| `InvoicedQuantity` | `Decimal` | no |  | The invoiced quantity of the log entry. |
| `UnitCode` | `String` | no |  | The unit code of the log entry. |
| `Discount` | `Decimal` | no |  | The discount of the log entry. |
| `Price` | `Decimal?` | yes |  | The price of the log entry. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price of the log entry. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  | The price in company currency of the log entry. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  | The setup price in company currency of the log entry. |
| `StandardPrice` | `Decimal?` | yes |  | The standard price of the log entry. |
| `WeightPerUnit` | `Decimal?` | yes |  | The weight per unit of the log entry. |
| `ProductGroupNumber` | `String` | no |  | The product group number of the log entry. |
| `StatisticalGoodsCode` | `String` | no |  | The statistical goods code of the log entry. |
| `IntrastatTransactionType` | `Int64?` | yes |  | The intrastat transaction type number of the log entry. |
| `TariffAndServiceCode` | `String` | no |  | The tariff and service code of the log entry. |
| `CurrencyCode` | `String` | no |  | The currency code of the log entry. |
| `ExchangeRate` | `Decimal` | no |  | The exchange rate of the log entry. |
| `CustomerOrderCategory` | `String` | no |  | The customer order category of the log entry. |
| `BusinessContactOrderNumber` | `String` | no |  | The business contact order number of the log entry. |
| `OrderRowType` | `Int32` | no |  | The order row type of the log entry. |
| `ConversionFactor` | `Decimal` | no |  | The conversion factor of the log entry. |
| `DeliveryIndex` | `Int32` | no |  | The delivery index of the log entry. |
| `FifoPrice` | `Decimal?` | yes |  | The FIFO price of the log entry. |
| `ServiceType` | `Int32?` | yes |  | The service type of the log entry. |
| `AccountNumber` | `String` | no |  | The account number of the log entry. |
| `DeliveryAddressAddressee` | `String` | no |  | The delivery address addressee of the log entry. |
| `IsExportedToManagementAccounting` | `Boolean` | no |  | If the log entry is exported to management accounting. |

- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4

**References out:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [ApplicationUsers](Common.md#Common.ApplicationUser), [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [Parts](Inventory.md#Inventory.Part), [Warehouses](Common.md#Common.Warehouse)

<a id="Sales.OrderQuantityCustomerOrder"></a>
### OrderQuantityCustomerOrders

Represents a order quantity template on part that holds many partial quantities.

- **Endpoint:** `GET /api/v1/Sales/OrderQuantityCustomerOrders`
- **Required permission:** Show purchase orders
- **Introduced in:** 22.6

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](Common.md#Common.PartialQuantity) | The partial quantities for the order quantity. |

**References out:** [PartialQuantities](Common.md#Common.PartialQuantity)
**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow)

<a id="Sales.OtherCustomerNumber"></a>
### OtherCustomerNumbers

Represents an alternative customer code mainly used for EDI.

- **Endpoint:** `GET /api/v1/Sales/OtherCustomerNumbers`
- **Required permission:** Show customer
- **Introduced in:** 2.32

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the other customer number. |
| `IsDefault` | `Boolean` | no |  | Specifies if this is the default/active other customer number. |
| `Number` | `String` | no |  | The human readable identifier of the other customer number. |
| `CustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) | The business key identifier of the owning customer. |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |

**References out:** [Customers](Sales.md#Sales.Customer)
**Referenced by:** [Customers](Sales.md#Sales.Customer)

<a id="Sales.PackageRowPartLocation"></a>
### PackageRowPartLocations

Represents a package row's location.

- **Endpoint:** `GET /api/v1/Sales/PackageRowPartLocations`
- **Required permission:** Show customer orders
- **Introduced in:** 25.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the package row location. |
| `ParentPackageRowId` | `Int64` | no | [PackageRows](Sales.md#Sales.PackageRow) | The business key identifier of the location's parent package row. |
| `PartLocationId` | `Int64` | no | [PartLocations](Inventory.md#Inventory.PartLocation) | The business key identifier of the package row location's part location. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the package row location's product record. |
| `BalanceChange` | `Decimal` | no |  | The balance change of the package row location. |

**References out:** [PackageRows](Sales.md#Sales.PackageRow), [PartLocations](Inventory.md#Inventory.PartLocation), [ProductRecords](Inventory.md#Inventory.ProductRecord)

<a id="Sales.PackageRow"></a>
### PackageRows

Represents a package row.

- **Endpoint:** `GET /api/v1/Sales/PackageRows`
- **Required permission:** Show customer orders
- **Introduced in:** 25.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the package row. |
| `ParentId` | `Int64?` | yes | [SalesPickingLists](Sales.md#Sales.SalesPickingList) | The business key identifier of the row's picking list. |
| `ParentRowId` | `Int64?` | yes | [PackageRows](Sales.md#Sales.PackageRow) | The business key identifier of the row's parent row. |
| `CustomerOrderDeliveryRowId` | `Int64?` | yes | [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow) | The business key identifier of the row's delivery row. |
| `PackagingPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the packing part. |
| `Cleared` | `Boolean` | no |  | Specifies if the row is cleared. |
| `ContainerNumber` | `String` | no |  | The container number of the row. |
| `SealNumber` | `String` | no |  | The seal number of the row. |
| `PackageNumber` | `String` | no |  | The package number of the row. |
| `OtherPackageNumber` | `String` | no |  | The other package number of the row. |
| `OtherPackageNumberNumberSeriesType` | `Int32?` | yes |  | The other package number series type of the row. |
| `ExternalPackageId` | `String` | no |  | The external package id of the row. |
| `Length` | `Decimal?` | yes |  | The length of the row's content. |
| `Width` | `Decimal?` | yes |  | The width of the row's content. |
| `Height` | `Decimal?` | yes |  | The height of the row's content. |
| `Volume` | `Decimal?` | yes |  | The volume of the row's content. |
| `VolumeCalculated` | `Decimal` | no |  | The calculated volume of the row's content. |
| `GrossWeight` | `Decimal?` | yes |  | The gross weight of the row's content. |
| `GrossWeightCalculated` | `Decimal` | no |  | The calculated gross weight of the row's content. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the row's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The external comment of the row. |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the row's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the row. |
| `PackageComplete` | `Boolean` | no |  | Specifies if the package row is complete. |
| `BalanceChange` | `Decimal` | no |  | The balance change of the row. |
| `TemplateCode` | `String` | no |  | The template code of the row. |

- `OtherPackageNumberNumberSeriesType` — NotInitalized=0, CustomerOrderNumber=2, PurchaseOrderNumber=3, AccountsReceivableNumber=4, SupplierCode=5, CustomerCode=6, AccountsPayableNumber=7, InventoryLogPriceId=13, PickingListNumber=14, AccountsReceivableLedgerNumber=15, RejectionLogId=16, ReportNumberForMaterial=17, ReportNumberForOperation=18, ManufacturingOrderNumber=19, AccountsReceivableNumberCashReceipt=20, AccountsReceivableNumberInterest=21, AccountsReceivableNumberInternal=22, AccountsReceivableNumberCredit=23, ProformaInvoiceNumber=24, DeliveryNoteNumber=25, PhysicalInventoryList=27, VoucherNumber=28, AutoCoding=29, AutoAllocation=30, ManufacturingPickingListNumber=31, AccountsReceivableNumberOnAccount=32, IncomingPaymentsBundleNumber=33, AccrualAccountingNumber=34, ShipmentNumber=35, AccountsPayableNumberOnAccount=36, OutgoingPaymentsBundleNumber=37, CaseNumber=38, TransactionList=39, Quote=40, Inquiry=41, Project=43, ProjectCostReportingEntry=44, FixedAsset=45, EdiFileTransaction=46, ServerPrinterNumber=47, AgentTaskNumber=48, MonitoringTaskNumber=49, DeliverySchedule=50, AccountsReceivableNumberDebitNote=51, AccountsReceivableNumberServiceTax=52, CodingMethod=53, TransferTask=54, BlanketOrderPurchase=55, ArrivalNote=56, GS1Code=57, AccountsReceivableNumberCorrectionInvoice=58, PackageNumber=59, MaintenanceReportingServiceNumber=60, BlanketOrderSales=61, AccountingReport=62, VatReport=63, PaymentBundleNumber=64, PackagingTemplateNumber=65, AllocationKeyNumber=66, PurchaseDeliverySchedule=67, SalesAgreement=68, AccountsReceivableNumberAdvance=69, SsccPackage=70, SalesForecast=71, BankAccountReconciliationReport=72, AccountsReceivableNumberCollectiveCorrectionInvoice=73, OscarPackage=74, DunsPackage=75, JipdecPackage=76, AccountsPayableNumberCorrectionInvoice=77, BusinessOpportunity=78, DeliveryNoteSubcontract=79, SupplierAgreement=80

**References out:** [Comments](Common.md#Common.Comment), [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [PackageRows](Sales.md#Sales.PackageRow), [Parts](Inventory.md#Inventory.Part), [SalesPickingLists](Sales.md#Sales.SalesPickingList)
**Referenced by:** [PackageRowPartLocations](Sales.md#Sales.PackageRowPartLocation), [PackageRows](Sales.md#Sales.PackageRow)

<a id="Sales.QuoteActivity"></a>
### QuoteActivities

Represents a quote activity.

- **Endpoint:** `GET /api/v1/Sales/QuoteActivities`
- **Required permission:** Show quote
- **Introduced in:** 24.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the quote activity. |
| `QuoteId` | `Int64` | no | [Quotes](Sales.md#Sales.Quote) | The business key identifier of the quote this activity belongs to. |
| `IsMandatory` | `Boolean` | no |  | Specifies if this activity is mandatory. |
| `ActivityTypeId` | `Int64` | no | [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType) | The business key identifier of the activity's type. |
| `CalendarAppointmentId` | `String` | no |  | The calendar appointment id of the activity. |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the user who completed this activity. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the user who is responsible for this activity. |
| `Description` | `String` | no |  | The translated description of the activity. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the activity's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the activity. |
| `Status` | `Int32` | no |  | The status of the activity. |
| `ReminderId` | `Int64?` | yes |  | The business key identifier of the activity's reminder. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  | The planned completion date of the activity. |
| `CompletionDate` | `DateTimeOffset?` | yes |  | The completion date of the activity. |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  | The planned start date of the activity. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  | The actual start date of the activity. |
| `IsAdministratorResponsibleUser` | `Boolean` | no |  | Specifies if the administrator is the responsible user of the activity. |
| `NumberDaysFromDueDate` | `Int32?` | yes |  | Specifies number of days from due date on this activity. |
| `IsDueDatePlannedCompletionDate` | `Boolean` | no |  | Specifies if due date id planned completion date on the activity. |
| `DueDateType` | `Int32` | no |  | The due date type of the activity. |

- `Status` — Registered=1, InProgress=2, History=9
- `DueDateType` — RegistrationDate=0, ValidThrough=1

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Comments](Common.md#Common.Comment), [CustomerRelationshipActivityTypes](Sales.md#Sales.CustomerRelationshipActivityType), [Quotes](Sales.md#Sales.Quote)

<a id="Sales.QuoteOrderRowDiscount"></a>
### QuoteOrderRowDiscounts

Represents a discount row for a quote row.

- **Endpoint:** `GET /api/v1/Sales/QuoteOrderRowDiscounts`
- **Required permission:** Show quote
- **Introduced in:** 24.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the discount row. |
| `OrderRowId` | `Int64` | no | [QuoteRows](Sales.md#Sales.QuoteRow) | The business key identifier of the discount row's quote row. |
| `DiscountId` | `Int64?` | yes | [Discounts](Common.md#Common.Discount) | The business key identifier of the discount row's discount. |
| `AsPercent` | `Decimal?` | yes |  | The discount amount as percent of the discount row. |
| `DiscountLockedFromAutomaticChanges` | `Boolean` | no |  | Specifies if the discount is locked from automatic changes. |
| `AsAmount` | `Decimal?` | yes |  | The discount amount of the discount row. |
| `AsAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the discount row's amount currency. |
| `DiscountType` | `Int32` | no |  | The discount type of the discount row. |
| `GrossPrice` | `Decimal?` | yes |  | The gross price of the discount row. |
| `GrossPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the discount row's gross price currency. |
| `NetPrice` | `Decimal?` | yes |  | The net price of the discount row. |
| `NetPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the discount row's net price currency. |
| `DiscountCalculationType` | `Int32` | no |  | The discount calculation type of the discount row. |
| `Priority` | `Int32` | no |  | The priority of the discount row. |
| `ReplacesDiscountFieldOnOrderRow` | `Boolean` | no |  | Specifies if this discount row represents the discount which could be applied to the discount field on the order row itself before order multiple discounts on order rows were introduced. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the row. |
| `Position` | `Int64?` | yes |  | The position of the row. |
| `OrderRowType` | `Int32` | no |  | The row type. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the row's part. |
| `EntityIdentityString` | `String` | no |  | The human readable identifier of the row's entity. |
| `AdditionalRowDescription` | `String` | no |  | The additional row description of the row. |
| `FreeTextHtml` | `String` | no |  | The free text row's rich text HTML data. |
| `FreeText` | `String` | no |  | The free text row's raw text data. |
| `ParentRowId` | `Int64?` | yes | [QuoteRows](Sales.md#Sales.QuoteRow) | The business key identifier of the row's parent. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  | The delivery date of the row. |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the row's revision. |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) | The revision of the row. |
| `OrderedQuantity` | `Decimal` | no |  | The ordered quantity of the row. |
| `Price` | `Decimal?` | yes |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's price currency. |
| `Discount` | `Decimal` | no |  | The discount specified on the row. |
| `ToolId` | `Int64?` | yes |  | The business key identifier of the row's tool. _(Replaced by Part)_ |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The unit of the row. |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) | The business key identifier of the row's VAT rate. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the row's warehouse. |
| `WeightPerUnit` | `Decimal?` | yes |  | The weight per unit of the row. |
| `OrderDate` | `DateTimeOffset` | no |  | The order date of the row. |
| `ConversionFactor` | `Decimal` | no |  | The conversion factor of the row. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  | The row's price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  | The row's setup price in the company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency. |
| `StandardPrice` | `Decimal?` | yes |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's standard price currency. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes |  | The business key identifier of the row's setup price currency. |
| `ShowPrice` | `Boolean` | no |  | Specifies if price should be shown for the row. |
| `PartRowType` | `Int32` | no |  | The part row type of the row. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the row. |
| `PartStatus` | `Int32?` | yes |  | The part status of the row. |
| `OrderedQuantityInOrderUnit` | `Decimal` | no |  | The ordered quantity of the row in the order unit. |
| `AlternatePreparationCode` | `String` | no |  | The alternate preparation code of the row. |
| `ShowFreeTextIn` | `Int32` | no |  | Specifies which documents the free text data of the row should be projected on. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) | The business key identifier of the row's statistical goods code. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order that was created as a result of the row. |
| `ExemptFromStatistics` | `Boolean` | no |  | Specifies if the row should be exempted from statistics. |
| `ParentOrderId` | `Int64` | no | [Quotes](Sales.md#Sales.Quote) | The business key identifier of the rows parent quote. |
| `CodingId` | `Int64?` | yes |  | The business key identifier of the rows coding. |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) | The coding of the row. |
| `RowsGoodsLabel` | `String` | no |  | The goods label of the row |
| `PartConfigurationId` | `Int64?` | yes |  | The business key identifier of the row's part configuration. |
| `RowIndex` | `Int32?` | yes |  | The index of the row. |
| `TransferProfileId` | `Int64?` | yes | [TransferProfiles](Common.md#Common.TransferProfile) | The business key identifier of the row's transfer profile. |
| `PartConfigurationIdInRemoteCompany` | `Int64?` | yes | [PartConfigurations](Common.md#Common.PartConfiguration) | The business key identifier of the row's part configuration in the remote company. |
| `CreateCustomerOrder` | `Boolean` | no |  | The create customer order option for the row |
| `DiscountRows` | `QuoteOrderRowDiscounts[]` | no | [QuoteOrderRowDiscounts](Sales.md#Sales.QuoteOrderRowDiscount) | The discount rows for the row. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the quote. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the quote's payment term. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The payment term of the quote. |
| `PaymentTermDescription` | `String` | no |  | The payment term description of the quote. |
| `GracePeriodInDays` | `Int32?` | yes |  | The quote's grace period in days. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the quote's delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) | The business key identifier of the quote's delivery term. |
| `DeliveryTermDescription` | `String` | no |  | The delivery term description of the quote. |
| `DeliveryMethodDescription` | `String` | no |  | The delivery method description of the quote. |
| `ShipmentPayer` | `Int32` | no |  | Specifies the shipment payer of the quote. |
| `BusinessContactOrderNumber` | `String` | no |  | The customer's quote number. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of our reference on the quote. Reference Persons |
| `OurReferenceName` | `String` | no |  | The name of our reference on the quote. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the customer's reference on the quote. |
| `BusinessContactReferenceName` | `String` | no |  | The name of the customer's reference on the quote. |
| `GoodsLabel` | `String` | no |  | The goods label of the quote. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the quote's currency. |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) | The business key identifier of the quote's VAT group. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the quote's warehouse. |
| `Priority` | `Int32` | no |  | The priority of the quote. |
| `ProjectId` | `Int64?` | yes |  | The business key identifier of the quote's project. |
| `SendMethod` | `Int32` | no |  | Specifies the method of the quote printout. |
| `InvoicePrintoutMethod` | `Int32` | no |  | Specifies the method of future invoice printouts resulted from the quote. |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the quote's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the quote. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the quote's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The external comment of the quote. |
| `TransportTime` | `Int32?` | yes |  | The transport time of the quote. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the quote. |
| `Version` | `Int32` | no |  | The version of the quote. |
| `UseForwardRate` | `Boolean` | no |  | Specifies if forward rate should be used. |
| `ExchangeRate` | `Decimal` | no |  | The exchange rate to use for the quote. |
| `OrderAmount` | `Decimal` | no |  | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `OrderAmountInCompanyCurrency` | `Decimal` | no |  | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `CustomerId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer that the quote belongs to. |
| `OrderNumber` | `String` | no |  | The order number of the customer order created as a result of the quote. |
| `OrderDate` | `DateTimeOffset?` | yes |  | The date/time when the quote was made into an order. |
| `Rows` | `QuoteRows[]` | no | [QuoteRows](Sales.md#Sales.QuoteRow) | The rows of the quote. |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the quote's seller. |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the quote's delivery address. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The delivery address of the quote. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the quote's mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The mailing address of the quote. |
| `VatNumber` | `String` | no |  | The VAT number on the quote. |
| `Status` | `Int32` | no |  | The status of the quote. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) | The communication addresses registered on the quote. |
| `QuoteDate` | `DateTimeOffset` | no |  | The date when the quote was made to the customer. |
| `QuoteDescription` | `String` | no |  | The description of the quote. |
| `LatestContactDate` | `DateTimeOffset?` | yes |  | The last contact date on the quote. |
| `RequestForQuoteDate` | `DateTimeOffset` | no |  | The date when the RFQ was made. |
| `ValidityTimeId` | `Int64?` | yes | [ValidityTimes](Sales.md#Sales.ValidityTime) | The business key identifier of the validity time of the quote. |
| `ValidityTime` | `ValidityTimes` | no | [ValidityTimes](Sales.md#Sales.ValidityTime) | The validity time of the quote. |
| `ValidityTimeDescription` | `String` | no |  | The validity time description of the quote. |
| `ValidityTimeInDays` | `Int32` | no |  | The validity time of the quote in days. |
| `ValidThroughDate` | `DateTimeOffset` | no |  | The valid through date of the quote. |
| `ProbabilityId` | `Int64` | no | [Probabilities](Common.md#Common.Probability) | The business key of the quote's probability. References a Probabilities |
| `Probability` | `Probabilities` | no | [Probabilities](Common.md#Common.Probability) | The probability of the quote. |
| `ReasonCodeLostQuoteId` | `Int64?` | yes | [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote) | The business key identifier of the reason why the quote was lost. |
| `ReasonCodeLostQuote` | `ReasonCodeLostQuotes` | no | [ReasonCodeLostQuotes](Sales.md#Sales.ReasonCodeLostQuote) | The reason why the quote was lost. |
| `ReasonLostCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the quote's reason of loss comment. Reference Comments |
| `ReasonLostComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The reason of loss comment for the quote. |
| `OrderTypeId` | `Int64?` | yes | [QuoteTypes](Sales.md#Sales.QuoteType) | The business key identifier of the quote's quote type. |
| `OrderType` | `QuoteTypes` | no | [QuoteTypes](Sales.md#Sales.QuoteType) | The quote type used on the quote. |
| `Preliminary` | `Boolean` | no |  | Specifies if the quote is to be considered preliminary. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the quote's currency exchange type. |
| `DeliveryTimeId` | `Int64?` | yes | [DeliveryTimes](Common.md#Common.DeliveryTime) | The business key identifier of the quote's delivery time. |
| `DeliveryTime` | `DeliveryTimes` | no | [DeliveryTimes](Common.md#Common.DeliveryTime) | The delivery time of the quote. |
| `DeliveryTimeInDays` | `Int32?` | yes |  | The delivery time in days of the quote. |
| `AccountGroupId` | `Int64` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The business key identifier of the account group of the quote. |
| `AccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The account group on the quote. |
| `CategoryString` | `String` | no |  | The category string on the quote. |
| `DestinationForDeliveryTerm` | `String` | no |  | The destination for the delivery term. |
| `EditedOrderAmountExcludingVat` | `Decimal?` | yes |  | The edited order amount excluding VAT for the quote. |
| `EditedOrderAmountExcludingVatCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The currency of the edited order amount excluding VAT for the quote. |
| `EditedOrderAmountDiscount` | `Decimal?` | yes |  | The edited order amount discount in percent for the quote. |
| `TypeOfOrderAmountEntered` | `Int32?` | yes |  | The type of edited order value entered on the quote. |
| `Factoring` | `Boolean` | no |  | Specifies if factoring is activated for the quote. |
| `BusinessOpportunityId` | `Int64?` | yes | [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity) | The business key identifier of the business opportunity of the quote. |
| `BusinessOpportunity` | `BusinessOpportunities` | no | [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity) | The business opportunity of the quote. |
| `RelatedQuotesId` | `Int64?` | yes | [RelatedQuotes](Sales.md#Sales.RelatedQuote) | The business key identifier of the related quotes placeholder. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the type. |
| `Number` | `Int64` | no |  | The human readable identifier of the type. |
| `Prefix` | `String` | no |  | The prefix to apply on quote numbers spawned from this type. |
| `Description` | `String` | no |  | The translated description of the type. |
| `Priority` | `Int32` | no |  | The priority of the type. |
| `Visible` | `Boolean` | no |  | Specifies if the type is visible. |
| `IsPreset` | `Boolean` | no |  | Specifies if the type is a preset type. |
| `PriceSetting` | `Int32` | no |  | The price setting to apply for quotes of this type. |
| `PriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) | The business key identifier of the type's price list. |
| `BaseType` | `Int32` | no |  | The base type of quotes created from this type. |
| `CodingGroupId` | `Int64` | no |  | The business key identifier of the type's coding group. |
| `FormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](Common.md#Common.FormReportConfiguration) | The business key identifier of the type's form report configuration. |
| `RateTypeSetting` | `Int32` | no |  | The rate type setting of the quote type. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the quote type's currency exchange type. |
| `CustomerOrderTypeId` | `Int64?` | yes | [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType) | The business key identifier of the quote type's cutomer order type. |
| `CustomerOrderType` | `CustomerOrderTypes` | no | [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType) | The quote type's cutomer order type. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the reason code. |
| `Code` | `String` | no |  | The human readable identifier of the reason code. |
| `Description` | `String` | no |  | The translated description of the reason code. |
| `CommentMandatory` | `Boolean` | no |  | Specifies if a comment is mandatory for this reason code. |
| `Active` | `Boolean` | no |  | Specifies if the reason code is active. |

**Referenced by:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [Quotes](Sales.md#Sales.Quote)

<a id="Sales.RelatedQuoteEntry"></a>
### RelatedQuoteEntries

Represents a related quote entry.

- **Endpoint:** `GET /api/v1/Sales/RelatedQuoteEntries`
- **Required permission:** Show quote
- **Introduced in:** 26.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the related quote entry. |
| `QuoteId` | `Int64?` | yes | [Quotes](Sales.md#Sales.Quote) | The business key identifier of the entry's related quote. |
| `IsPrimary` | `Boolean` | no |  | Specifies if this is the primary related quote. |
| `RelatedQuotesId` | `Int64?` | yes | [RelatedQuotes](Sales.md#Sales.RelatedQuote) | The business key identifier of the entry's related quotes placeholder. |

**References out:** [Quotes](Sales.md#Sales.Quote), [RelatedQuotes](Sales.md#Sales.RelatedQuote)

<a id="Sales.RelatedQuote"></a>
### RelatedQuotes

Represents a placeholder for related quotes.

- **Endpoint:** `GET /api/v1/Sales/RelatedQuotes`
- **Required permission:** Show quote
- **Introduced in:** 26.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the related quote placeholder. |

**Referenced by:** [Quotes](Sales.md#Sales.Quote), [RelatedQuoteEntries](Sales.md#Sales.RelatedQuoteEntry)

<a id="Sales.SalesAgreementBasis"></a>
### SalesAgreementBases

Represents a sales agreement basis.

- **Endpoint:** `GET /api/v1/Sales/SalesAgreementBases`
- **Required permission:** Show agreement
- **Introduced in:** 26.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the agreement basis. |
| `SalesAgreementId` | `Int64` | no | [SalesAgreements](Sales.md#Sales.SalesAgreement) | The business key identifier of the parent agreement. |
| `CustomerOrderId` | `Int64` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order generated from this agreement basis. |
| `InvoiceId` | `Int64?` | yes | [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice) | The business key identifier of the invoice for this agreement basis. |
| `AccrualAccountId` | `Int64?` | yes | [Accounts](Accounting.md#Accounting.Account) | The business key identifier of the accrual account for this agreement basis. |
| `IsAccrual` | `Boolean` | no |  | Indicates if this agreement basis uses accrual accounting. |
| `IsOneTimeCost` | `Boolean` | no |  | Indicates if this agreement basis is a one-time cost. |
| `IsRemoved` | `Boolean` | no |  | Indicates if the agreement basis and the linked customer order has been set as removed. |
| `IsPaused` | `Boolean` | no |  | Indicates if the agreement basis is paused. |
| `InvoicingMethod` | `Int32` | no |  | The invoicing method of the agreement basis. |
| `PeriodStart` | `DateTimeOffset` | no |  | The period start date of the agreement basis. |
| `PeriodEnd` | `DateTimeOffset` | no |  | The period end date of the agreement basis. |
| `PlannedInvoiceDate` | `DateTimeOffset` | no |  | The planned invoice date of the agreement basis. |
| `PeriodStartOnAgreementWhenCreated` | `DateTimeOffset?` | yes |  | The period start on the agreement when this basis was created. |
| `ExchangeRate` | `Decimal` | no |  | The exchange rate of the agreement basis. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency of the agreement basis. |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The currency of the agreement basis. |
| `UseForwardRate` | `Boolean` | no |  | Indicates if the agreement basis uses forward rate. |
| `Rows` | `SalesAgreementBasisRows[]` | no | [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow) | The rows of the agreement basis. |

- `InvoicingMethod` — InAdvance=1, InArrears=2

**References out:** [Accounts](Accounting.md#Accounting.Account), [Currencies](Common.md#Common.Currency), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreements](Sales.md#Sales.SalesAgreement)
**Referenced by:** [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreements](Sales.md#Sales.SalesAgreement)

<a id="Sales.SalesAgreementBasisRow"></a>
### SalesAgreementBasisRows

Represents a sales agreement basis row.

- **Endpoint:** `GET /api/v1/Sales/SalesAgreementBasisRows`
- **Required permission:** Show agreement
- **Introduced in:** 26.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the agreement basis row. |
| `ParentRowId` | `Int64?` | yes | [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow) | The business key identifier of the parent row. |
| `ParentAgreementBasisId` | `Int64` | no | [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis) | The business key identifier of the parent agreement basis. |
| `AgreementRowId` | `Int64` | no | [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow) | The business key identifier of the source agreement row. |
| `CustomerOrderRowId` | `Int64` | no | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The business key identifier of the generated customer order row. |
| `OrderRowType` | `Int32` | no |  | The order row type of the row. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the row's part. |
| `EntityIdentityString` | `String` | no |  | The entity identity string of the row. |
| `AdditionalRowDescription` | `String` | no |  | The additional row description of the row. |
| `FreeTextHtml` | `String` | no |  | The free text formatted as rich text HTML of the row. |
| `FreeText` | `String` | no |  | The free text as raw text of the row. |
| `Quantity` | `Decimal` | no |  | The quantity of the row. |
| `ConversionFactor` | `Decimal` | no |  | The conversion factor of the row. |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The unit of the row. |
| `MileageHours` | `Decimal` | no |  | The mileage hours of the row. |
| `Price` | `Decimal?` | yes |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's price currency. |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The price currency of the row. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  | The price in company currency of the row. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency. |
| `PriceInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The company currency of the row's price. |
| `Discount` | `Decimal` | no |  | The discount of the row. |
| `StandardPrice` | `Decimal?` | yes |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's standard price currency. |
| `StandardPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The standard price currency of the row. |
| `Amount` | `Decimal` | no |  | The total amount of the row. |
| `AmountInCompanyCurrency` | `Decimal` | no |  | The total amount in company currency of the row. |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) | The business key identifier of the row's VAT rate. |
| `IsOneTimeCost` | `Boolean` | no |  | Indicates if the row is a one-time cost. |
| `PeriodStart` | `DateTimeOffset?` | yes |  | The period start date of the row. |
| `PeriodEnd` | `DateTimeOffset?` | yes |  | The period end date of the row. |

- `OrderRowType` — Part=1, Additional=2, Sum=3, FreeText=4

**References out:** [Currencies](Common.md#Common.Currency), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [Parts](Inventory.md#Inventory.Part), [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow), [Units](Common.md#Common.Unit), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow)

<a id="Sales.SalesAgreementRowInflow"></a>
### SalesAgreementRowInflows

Represents a sales agreement inflow row.

- **Endpoint:** `GET /api/v1/Sales/SalesAgreementRowInflows`
- **Required permission:** Show agreement
- **Introduced in:** 26.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the inflow row. |
| `CreationTime` | `DateTimeOffset?` | yes |  | The creation time of the inflow row. |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  | The logging timestamp of the inflow row. |
| `OrderRowType` | `Int32` | no |  | The order row type of the inflow row. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the inflow rows part. |
| `AdditionalRowDescription` | `String` | no |  | The additional row description of the inflow row. |
| `SalesAgreementId` | `Int64?` | yes | [SalesAgreements](Sales.md#Sales.SalesAgreement) | The business key identifier of the inflow rows sales agreement. |
| `SalesAgreementRowId` | `Int64?` | yes | [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow) | The business key identifier of the inflow rows sales agreement row. |
| `OrderedQuantityChange` | `Decimal?` | yes |  | The ordered quantity change of the inflow row. |
| `PriceChange` | `Decimal?` | yes |  | The price change of the inflow row. |
| `PriceChangeCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the price change currency. |
| `PriceChangeCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The price change currency. |
| `PriceChangeInCompanyCurrency` | `Decimal?` | yes |  | The price change in company currency of the inflow row. |
| `PriceChangeInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the price change in company currency. |
| `PriceChangeInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The price change in company currency. |
| `DiscountChange` | `Decimal?` | yes |  | The discount change of the inflow row. |
| `TotalValueChange` | `Decimal` | no |  | The total value change of the inflow row. |
| `TotalValueChangeCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the total value change currency. |
| `TotalValueChangeCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The total value change currency. |
| `TotalValueChangeInCompanyCurrency` | `Decimal` | no |  | The total value change in company currency of the inflow row. |
| `TotalValueChangeInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the total value change in company currency. |
| `TotalValueChangeInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The total value change in company currency. |
| `RowTotalValue` | `Decimal` | no |  | The row total value of the inflow row. |
| `RowTotalValueCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row total value currency. |
| `RowTotalValueCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The row total value currency. |
| `RowTotalValueInCompanyCurrency` | `Decimal` | no |  | The row total value in company currency of the inflow row. |
| `RowTotalValueInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row total value in company currency. |
| `RowTotalValueInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The row total value in company currency. |
| `RowTotalQuantity` | `Decimal` | no |  | The row total quantity of the inflow row. |
| `IsOneTimeCost` | `Boolean` | no |  | Whether the inflow row is a one-time cost. |
| `SalesAgreementInvoicingInterval` | `Int32` | no |  | The invoicing interval of the inflow row. |
| `TypeOfChange` | `Int32` | no |  | The type of change of the inflow row. |
| `PriceDefinition` | `Int32` | no |  | The price definition of the inflow row. |
| `PriceChangePerInterval` | `Decimal?` | yes |  | The price change per interval of the inflow row. |
| `PriceChangePerIntervalCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the price change per interval currency. |
| `PriceChangePerIntervalCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The price change per interval currency. |
| `PriceChangePerIntervalInCompanyCurrency` | `Decimal?` | yes |  | The price change per interval in company currency of the inflow row. |
| `PriceChangePerIntervalInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the price change per interval in company currency. |
| `PriceChangePerIntervalInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The price change per interval in company currency. |
| `TotalValueChangePerInterval` | `Decimal` | no |  | The total value change per interval of the inflow row. |
| `TotalValueChangePerIntervalInCompanyCurrency` | `Decimal` | no |  | The total value change per interval in company currency of the inflow row. |
| `RowTotalValuePerInterval` | `Decimal` | no |  | The row total value per interval of the inflow row. |
| `RowTotalValuePerIntervalInCompanyCurrency` | `Decimal` | no |  | The row total value per interval in company currency of the inflow row. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the row. |
| `ParentRowId` | `Int64?` | yes | [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow) | The business key identifier of the rows parent row. |
| `ParentOrderId` | `Int64` | no | [SalesAgreements](Sales.md#Sales.SalesAgreement) | The business key identifier of the rows parent agreement. |
| `Position` | `Int64?` | yes |  | The position of the row. |
| `OrderRowType` | `Int32` | no |  | The order row type of the row. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the rows part. |
| `AdditionalRowDescription` | `String` | no |  | The additional row description of the row. |
| `Quantity` | `Decimal` | no |  | The quantity of the row. |
| `FutureQuantity` | `Decimal?` | yes |  | The future quantity of the row. |
| `PreviousQuantity` | `Decimal?` | yes |  | The previous quantity of the row. |
| `ConversionFactor` | `Decimal` | no |  | The conversion factor of the row. |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the rows unit. |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The unit of the row. |
| `Price` | `Decimal?` | yes |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the rows price currency. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  | The rows price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency. |
| `FuturePriceAmount` | `Decimal?` | yes |  | The future price amount of the row. |
| `PreviousPriceAmount` | `Decimal?` | yes |  | The previous price amount of the row. |
| `Discount` | `Decimal` | no |  | The discount of the row. |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) | The business key identifier of the rows VAT rate. |
| `FutureValidFrom` | `DateTimeOffset?` | yes |  | The future valid from of the row. |
| `PreviousValidThrough` | `DateTimeOffset?` | yes |  | The previous valid through of the row. |
| `CustomerPartNumber` | `String` | no |  | The customer part number of the row. |
| `PartRowType` | `Int32` | no |  | The part row type of the row. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price of the row. _(Setup price has never been used in sales agreements. One time cost rows are used instead.)_ |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the rows setup price currency. _(Setup price has never been used in sales agreements. One time cost rows are used instead.)_ |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  | The setup price in company currency of the row. _(Setup price has never been used in sales agreements. One time cost rows are used instead.)_ |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency. _(Setup price has never been used in sales agreements. One time cost rows are used instead.)_ |
| `ShowFreeTextIn` | `Int32` | no |  | Specifies which documents the free text data of the row should be projected on. |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the revision of the rows part. |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) | The revision of the row's part. |
| `FreeTextHtml` | `String` | no |  | The free text formatted as rich text HTML of the row. |
| `FreeText` | `String` | no |  | The free text as raw text of the row. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the row. |
| `QuantityRatio` | `Decimal?` | yes |  | The quantity ratio of the row. |
| `CodingId` | `Int64?` | yes | [Codings](Accounting.md#Accounting.Coding) | The business key identifier of the rows coding. |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) | The coding of the row. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  | The delivery date of the row. |
| `CompensatedRowId` | `Int64?` | yes | [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow) | The business key identifier of the row compensated for this row. |
| `OneTimeCostType` | `Int32` | no |  | The one time cost type of the row. |
| `PeriodStart` | `DateTimeOffset?` | yes |  | The period start of the row. |
| `PeriodEnd` | `DateTimeOffset?` | yes |  | The period end of the row. |
| `PlannedInvoiceDate` | `DateTimeOffset?` | yes |  | The planned invoice date of the row. |
| `StandardPrice` | `Decimal?` | yes |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the rows standard price currency. |
| `FutureDiscount` | `Decimal?` | yes |  | The future discount of the row. |
| `PreviousDiscount` | `Decimal?` | yes |  | The previous discount of the row. |
| `IsAccrual` | `Boolean` | no |  | Indicates if the row is accrual. |
| `ValidFrom` | `DateTimeOffset?` | yes |  | The valid from date of the row. |
| `ValidTo` | `DateTimeOffset?` | yes |  | The valid to date of the row. |
| `FuturePriceInCompanyCurrencyAmount` | `Decimal?` | yes |  | The future price in company currency amount of the row. |
| `PreviousPriceInCompanyCurrencyAmount` | `Decimal?` | yes |  | The previous price in company currency amount of the row. |
| `EntityIdentityString` | `String` | no |  | The entity identity string of the row. |
| `ExtraFieldBool` | `Boolean` | no |  | An extra field of type bool. |
| `ExtraFieldInteger` | `Int32?` | yes |  | An extra field of type integer. |
| `ExtraFieldDecimal` | `Decimal?` | yes |  | An extra field of type decimal. |
| `ExtraFieldDate` | `DateTimeOffset?` | yes |  | An extra field of type date. |
| `ExtraFieldText` | `String` | no |  | An extra field of type text. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the agreement. |
| `OrderNumber` | `String` | no |  | The human readable identifier of the agreement. |
| `OrderTypeId` | `Int64` | no | [SalesAgreementTypes](Sales.md#Sales.SalesAgreementType) | The business key identifier of the agreements type. |
| `PeriodStart` | `DateTimeOffset` | no |  | The start period of the agreement. |
| `PeriodEnd` | `DateTimeOffset?` | yes |  | The end period of the agreement. |
| `AgreementDate` | `DateTimeOffset?` | yes |  | The date of the agreement. |
| `LastNoticeDate` | `DateTimeOffset?` | yes |  | The last notice date of the agreement. |
| `TerminationDate` | `DateTimeOffset?` | yes |  | The termination date of the agreement. |
| `ExtensionPeriod` | `Int32?` | yes |  | The extension period in months of the agreement. |
| `CustomerAgreementNumber` | `String` | no |  | The customers number of the agreement. |
| `Status` | `Int32` | no |  | The status of the agreement. |
| `ResponsibleId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the person responsible of the agreement. |
| `BusinessContactId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) | The business key identifier of the agreements customer. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the agreements customer reference. |
| `BusinessContactReferenceName` | `String` | no |  | The customers reference name of the agreement. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of our reference on the agreement. |
| `OurReferenceName` | `String` | no |  | Our reference name of the agreement. |
| `Description` | `String` | no |  | The translated description of the agreement. |
| `UseForwardRate` | `Boolean` | no |  | Indicates if the agreement use forward rate. |
| `ExchangeRate` | `Decimal` | no |  | The exchange rate of the agreement. |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the agreements internal comment. |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the agreement. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the agreements external comment. |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The external comment of the agreement. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the agreements currency. |
| `TermLocation` | `String` | no |  | The term location of the agreement. |
| `InvoicingMethod` | `Int32` | no |  | The invoicing method of the agreement. |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) | The business key identifier of the agreements VAT group. |
| `IsAccrual` | `Boolean` | no |  | Indicates if the agreement is accrual. |
| `DefaultOrderPrintoutVia` | `Int32` | no |  | The default printout method of the agreement. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the agreements mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The mailing address of the agreement. |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the agreements delivery address. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The delivery address of the agreement. |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The business key identifier of the agreements customers account group. |
| `InvoiceBusinessContactId` | `Int64` | no | [Customers](Sales.md#Sales.Customer) | The business key identifier of the agreements invoice customer. |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of the agreements project. |
| `AftermarketProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the agreements aftermarket product record. |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the agreements seller. |
| `Priority` | `Int32` | no |  | The priority of the agreement. |
| `AccrualAccountId` | `Int64?` | yes | [Accounts](Accounting.md#Accounting.Account) | The business key identifier of the agreements accrual account. |
| `InvoiceCurrentMonth` | `Boolean` | no |  | Indicates if the agreement should be invoiced the current month. |
| `InvoicingInterval` | `Int32` | no |  | The invoicing interval of the agreement. |
| `ComprehensiveInvoiceChoice` | `Int32` | no |  | The comprehensive invoice choice of the agreement. |
| `ReleaseAgreementBasisAutomatically` | `Boolean` | no |  | Indicates if agreement basis should be released automatically. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the agreements payment term. |
| `PaymentTermDescription` | `String` | no |  | The payment term description of the agreement. |
| `DestinationForDeliveryTerm` | `String` | no |  | The destination for delivery term of the agreement. |
| `GracePeriodInDays` | `Int32?` | yes |  | The grace period in days of the agreement. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the agreements delivery method. |
| `DeliveryMethodDescription` | `String` | no |  | The delivery method description of the agreement. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) | The business key identifier of the delivery term of the agreement. |
| `DeliveryTermDescription` | `String` | no |  | The delivery term description of the agreement. |
| `PriceDefinition` | `Int32` | no |  | The price definition of the agreement. |
| `UpdateStatusAutomatically` | `Boolean` | no |  | Indicates if agreement status should be updated automatically. |
| `Version` | `Int32` | no |  | The version of the agreement. |
| `NoticePeriod` | `Int32` | no |  | The notice period of the agreement. |
| `PlannedInvoiceDateOffset` | `Int32` | no |  | The planned invoice date offset in days of the agreement. |
| `NumberOfYearsToCreateBasisFor` | `Int32` | no |  | The number of years to create agreement basis for in advance. |
| `CreateAgreementBasis` | `Boolean` | no |  | Indicates if agreement basis should be created. |
| `Rows` | `SalesAgreementRows[]` | no | [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow) | The rows of the agreement. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the agreement. |
| `Factoring` | `Boolean` | no |  | Specifies if factoring is activated for the agreement. |
| `Bases` | `SalesAgreementBases[]` | no | [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis) | The agreement bases of the agreement. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the agreement type. |
| `PriceSetting` | `Int32` | no |  | The price setting of the agreement type. |
| `PriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) | The business key identifier of the agreement types price list. |
| `Number` | `Int64` | no |  | The number of the agreement type. |
| `Prefix` | `String` | no |  | The prefix of the agreement type. |
| `Description` | `String` | no |  | The translated description of the agreement type. |
| `Priority` | `Int32` | no |  | The priority of the agreement type. |
| `Visible` | `Boolean` | no |  | Indicates if the agreement type should be visible. |
| `IsPreset` | `Boolean` | no |  | Indicates if the agreement type is preset. |
| `CodingGroupId` | `Int64` | no |  | The business key identifier of the agreement types coding group. |
| `UpdateStatusAutomatically` | `Boolean` | no |  | Indicates if the status of the agreement should be updated automatically. |
| `InvoicingMethod` | `Int32` | no |  | The invoicing method of the agreement type. |
| `PlannedInvoiceDateOffset` | `Int32` | no |  | The planned invoice date offset in days of the agreement type. |
| `ReleaseBasisAutomatically` | `Boolean` | no |  | Indicates if the agreement basis should be released automatically. |
| `UpwardAdjustmentTriggerType` | `Int32` | no |  | The trigger type for upward adjustments. |
| `UpwardAdjustmentTriggerValue` | `Int32` | no |  | The trigger value for upward adjustments. |
| `AgreementValidFromSetting` | `Int32` | no |  | The valid from setting of the agreement type. |
| `RateTypeSetting` | `Int32` | no |  | The rate type setting of the agreement type. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the sales picking list row quantity. |
| `PickingListRowKey` | `String` | no |  | The composite string key of the sales picking list row quantity. |
| `CustomerOrderDeliveryRowId` | `Int64` | no | [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow) | The business key identifier of the customer order delivery row that the row quantity relates to. |
| `PartLocationId` | `Int64?` | yes | [PartLocations](Inventory.md#Inventory.PartLocation) | The business key identifier of the part location that the row quantity relates to. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](Inventory.md#Inventory.ProductRecord) | The business key identifier of the product record that the row quantity relates to. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the row quantity relates to. |
| `Quantity` | `Decimal` | no |  | The quantity set for the row. |
| `Included` | `Boolean?` | yes |  | Null if the user has not specifically set the included state of the row, otherwise true or false depending on if the row is included or not. |

**References out:** [CustomerOrderDeliveryRows](Sales.md#Sales.CustomerOrderDeliveryRow), [PartLocations](Inventory.md#Inventory.PartLocation), [Parts](Inventory.md#Inventory.Part), [ProductRecords](Inventory.md#Inventory.ProductRecord)

<a id="Sales.SalesPickingList"></a>
### SalesPickingLists

Represents a sales picking list.

- **Endpoint:** `GET /api/v1/Sales/SalesPickingLists`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the picking list. |
| `Number` | `Int64` | no |  | The human readable identifier of the picking list. |
| `PrintedByApplicationUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that printed the picking list. |
| `PrintedByPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the person that printed the picking list. |
| `PrintedTimestamp` | `DateTimeOffset?` | yes |  | The date the picking list was printed. |
| `State` | `Int32` | no |  | The state for the picking list. |
| `Status` | `Int32` | no |  | The state for the picking list. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse for the picking list. |
| `CustomerOrderInvoices` | `CustomerOrderInvoices[]` | no | [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice) | The customer order invoices of the picking list. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the picking list. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the sales price. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part the sales price belongs to. |
| `PriceListId` | `Int64` | no | [PriceLists](Common.md#Common.PriceList) | The business key identifier of the price list the sales price belongs to. |
| `Price` | `Decimal?` | yes |  | The price on the sales price. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the price on the sales price. |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The currency for the price on the sales price. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price on the sales price. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the setup price on the sales price. |
| `SetupPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The currency for the setup price on the sales price. |
| `ValidThrough` | `DateTimeOffset?` | yes |  | The valid through date on the sales price. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the sales price's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the sales price. |
| `FuturePrice` | `Decimal?` | yes |  | The future price on the sales price. |
| `FuturePriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the future price on the sales price. |
| `FuturePriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The currency for the future price on the sales price. |
| `FutureSetupPrice` | `Decimal?` | yes |  | The future setup price on the sales price. |
| `FutureSetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the future setup price on the sales price. |
| `FutureSetupPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The currency for the future setup price on the sales price. |
| `FuturePriceValidThrough` | `DateTimeOffset?` | yes |  | The future valid through date on the sales price. |
| `StaggeredPrices` | `StaggeredPrices[]` | no | [StaggeredPrices](Common.md#Common.StaggeredPrice) | The staggered prices on the sales price. |

**References out:** [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [Parts](Inventory.md#Inventory.Part), [PriceLists](Common.md#Common.PriceList), [StaggeredPrices](Common.md#Common.StaggeredPrice)

<a id="Sales.SalesProcessStep"></a>
### SalesProcessSteps

Represents a sales process step.

- **Endpoint:** `GET /api/v1/Sales/SalesProcessSteps`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the sales process step. |
| `Code` | `Int64` | no |  | The human readable identifier of the sales process step. |
| `Step` | `String` | no |  | The name of the sales process step. |
| `IsActive` | `Boolean` | no |  | Specifies if the sales process step is active. |
| `Description` | `String` | no |  | The translated description of the sales process step. |

**Referenced by:** [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow)

<a id="Sales.SalesProcessTemplateRow"></a>
### SalesProcessTemplateRows

Represents a sales process template row.

- **Endpoint:** `GET /api/v1/Sales/SalesProcessTemplateRows`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the sales process template row. |
| `Code` | `Int64` | no |  | The human readable identifier of the sales process template row. |
| `SalesProcessStepId` | `Int64` | no | [SalesProcessSteps](Sales.md#Sales.SalesProcessStep) | The business key identifier of the sales process template row's sales process step. |
| `SalesProcessStep` | `SalesProcessSteps` | no | [SalesProcessSteps](Sales.md#Sales.SalesProcessStep) | The sales process step of the sales process template row. |
| `Probability` | `Int32` | no |  | The probability of the sales process template row. |
| `LeadTime` | `Int32` | no |  | The lead time of the sales process template row. |
| `Responsibility` | `Int32` | no |  | The responsibility of the sales process template row. |
| `ResponsibleSellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the sales process template row's responsible seller. |
| `ResponsibleSeller` | `Persons` | no | [Persons](Common.md#Common.Person) | The sales process template row's responsible seller. |
| `ResponsibleSellerGroupId` | `Int64?` | yes | [SellerGroups](Sales.md#Sales.SellerGroup) | The business key identifier of the sales process template row's seller group. |
| `ResponsibleSellerGroup` | `SellerGroups` | no | [SellerGroups](Sales.md#Sales.SellerGroup) | The sales process template row's seller group. |
| `ParentId` | `Int64` | no | [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate) | The business key identifier of the sales process template row's parent. |

- `Responsibility` — Seller=0, Group=1

**References out:** [Persons](Common.md#Common.Person), [SalesProcessSteps](Sales.md#Sales.SalesProcessStep), [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate), [SellerGroups](Sales.md#Sales.SellerGroup)
**Referenced by:** [SalesProcessTemplates](Sales.md#Sales.SalesProcessTemplate)

<a id="Sales.SalesProcessTemplate"></a>
### SalesProcessTemplates

Represents a sales process template.

- **Endpoint:** `GET /api/v1/Sales/SalesProcessTemplates`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the sales process template. |
| `Code` | `String` | no |  | The human readable identifier of the sales process template. |
| `IsActive` | `Boolean` | no |  | Specifies if the sales process template is active. |
| `Description` | `String` | no |  | The translated description of the sales process template. |
| `Rows` | `SalesProcessTemplateRows[]` | no | [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow) | The rows of the sales process template. |

**References out:** [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow)
**Referenced by:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType), [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow)

<a id="Sales.SellerGroup"></a>
### SellerGroups

Represents a seller group.

- **Endpoint:** `GET /api/v1/Sales/SellerGroups`
- **Required permission:** Show business opportunity
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the seller group. |
| `Code` | `Int64` | no |  | The human readable identifier of the seller group. |
| `IsActive` | `Boolean` | no |  | Specifies if the seller group is active. |
| `Description` | `String` | no |  | The translated description of the seller group. |

**Referenced by:** [BusinessOpportunitySalesProcessSteps](Sales.md#Sales.BusinessOpportunitySalesProcessStep), [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow)

<a id="Sales.ShipmentCustoms"></a>
### ShipmentCustoms

Represents a shipments customs information.

- **Endpoint:** `GET /api/v1/Sales/ShipmentCustoms`
- **Required permission:** Show shipment
- **Introduced in:** 26.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the shipments customs information. |
| `ParentId` | `Int64` | no | [Shipments](Sales.md#Sales.Shipment) | The business key identifier of the customs informations shipment. |
| `Dutiable` | `Boolean` | no |  | Indicates if the shipment is dutiable. |
| `InvoiceNumber` | `String` | no |  | The invoice number on the customs information. |
| `InvoiceDate` | `DateTimeOffset?` | yes |  | The invoice date on the customs information. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the customs informations currency. |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The customs informations currency. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the customs informations currency exchange type. |
| `CurrencyExchangeType` | `CurrencyExchangeTypes` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The customs informations currency exchange type. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the customs informations delivery method. |
| `DeliveryMethod` | `DeliveryMethods` | no | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The customs informations delivery method. |
| `ForeignDeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the customs informations foreign delivery method. |
| `ForeignDeliveryMethod` | `DeliveryMethods` | no | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The customs informations foreign delivery method. |
| `DeclarantId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the customs informations declarant person. |
| `Declarant` | `Persons` | no | [Persons](Common.md#Common.Person) | The customs informations declarant person. |
| `DeclarantName` | `String` | no |  | The customs informations declarant name. |
| `NumberOfPackages` | `Int32` | no |  | The number of packages on the customs information. |
| `Comment1` | `String` | no |  | The comment row 1 on the customs information. |
| `Comment2` | `String` | no |  | The comment row 2 on the customs information. |
| `Comment3` | `String` | no |  | The comment row 3 on the customs information. |
| `Comment4` | `String` | no |  | The comment row 4 on the customs information. |
| `TransactionType` | `String` | no |  | The customs informations transaction type. |
| `PointOfExport` | `String` | no |  | The customs informations point of export. |
| `City` | `String` | no |  | The customs informations city. |
| `Date` | `DateTimeOffset` | no |  | The customs informations date. |
| `DeclarantCorporationIdentificationNumber` | `String` | no |  | The customs informations declarant corporation identification number. |
| `ReferenceNumber` | `String` | no |  | The customs informations reference number. |
| `InvoiceType` | `Int32?` | yes |  | The customs informations invoice type. |
| `ImportExportType` | `Int32?` | yes |  | The customs informations import export type. |
| `ImportExportTypeName` | `String` | no |  | Free-text override of the import/export type. When set, it takes precedence over when the shipment is exported to forwarders (for example for forwarder-specific codes like "GIFT" or "sample"). |
| `ReasonForExport` | `String` | no |  | The customs informations reason for export. |
| `StatisticalGoodsCodeType` | `Int32` | no |  | The customs informations statistical goods code type. |
| `EoriSeller` | `String` | no |  | The Economic Operator Registration and Identification number of the customs informations seller. |
| `VatNumberSeller` | `String` | no |  | The VAT number of the customs informations seller. |
| `CorporationIdentificationNumberSeller` | `String` | no |  | The corporation identification number of the customs informations seller. |
| `EoriPickup` | `String` | no |  | The customs informations Economic Operator Registration and Identification pickup number. |
| `EoriPurchaser` | `String` | no |  | The Economic Operator Registration and Identification number of the customs informations purchaser. |
| `VatNumberPurchaser` | `String` | no |  | The VAT number of the customs informations purchaser. |
| `CorporationIdentificationNumberPurchaser` | `String` | no |  | The corporation identification number of the customs informations purchaser. |
| `EoriDelivery` | `String` | no |  | The Economic Operator Registration and Identification number of the customs informations delivery. |
| `VatNumberDelivery` | `String` | no |  | The VAT number of the customs informations delivery. |
| `CorporationIdentificationNumberDelivery` | `String` | no |  | The corporation identification number of the customs informations delivery. |
| `CustomsPayingParty` | `Int32` | no |  | Specifies who pay the cusoms fee. |
| `EoriCustomsPayer` | `String` | no |  | The Economic Operator Registration and Identification number of the customs payer. |
| `CorporationIdentificationNumberCustomsPayer` | `String` | no |  | The corporation identification number of the customs payer. |
| `VatNumberCustomsPayer` | `String` | no |  | The VAT number of the customs payer. |
| `CustomsPayer` | `String` | no |  | The customs informations customs payer. |
| `Rows` | `ShipmentCustomsRows[]` | no | [ShipmentCustomsRows](Sales.md#Sales.ShipmentCustomsRow) | The rows of the customs information. |
| `Documents` | `ShipmentCustomsDocuments[]` | no | [ShipmentCustomsDocuments](Sales.md#Sales.ShipmentCustomsDocument) | The documents of the customs information. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the shipments customs information document. |
| `ParentId` | `Int64` | no | [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms) | The business key identifier of the documents customs information. |
| `Code` | `String` | no |  | The documents code. |
| `Name` | `String` | no |  | The documents name. |
| `RowIndex` | `Int32?` | yes |  | The documents row index. |

**References out:** [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms)
**Referenced by:** [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms)

<a id="Sales.ShipmentCustomsRow"></a>
### ShipmentCustomsRows

Represents a shipments customs information row.

- **Endpoint:** `GET /api/v1/Sales/ShipmentCustomsRows`
- **Required permission:** Show shipment
- **Introduced in:** 26.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the shipments customs information row. |
| `ParentId` | `Int64` | no | [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms) | The business key identifier of the rows customs information. |
| `RowIndex` | `Int32?` | yes |  | The rows index number. |
| `CountryOfOriginId` | `Int64?` | yes | [Countries](Common.md#Common.Country) | The business key identifier of the rows country of origin. |
| `CountryOfOrigin` | `Countries` | no | [Countries](Common.md#Common.Country) | The rows country of origin. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) | The business key identifier of the rows statistical goods code. |
| `StatisticalGoodsCode` | `StatisticalGoodsCodes` | no | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) | The rows statistical goods code. |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the rows unit. |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The rows unit. |
| `AdditionalCode` | `String` | no |  | The rows additional code. |
| `Amount` | `Decimal` | no |  | The rows amount. |
| `AmountInCompanyCurrency` | `Decimal` | no |  | The rows amount in company currency. |
| `Content` | `String` | no |  | The rows content. |
| `GrossWeight` | `Decimal?` | yes |  | The rows gross weight. |
| `NetWeight` | `Decimal?` | yes |  | The rows net weight. |
| `GoodsLabel` | `String` | no |  | The rows goods label. |
| `OtherQuantity` | `Decimal?` | yes |  | The rows other quantity. |
| `OtherUnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the rows other unit. |
| `OtherUnit` | `Units` | no | [Units](Common.md#Common.Unit) | The rows other unit. |
| `OtherUnitCode` | `String` | no |  | The rows other unit code. |
| `Procedure` | `String` | no |  | The rows procedure. |
| `Quantity` | `Int32` | no |  | The rows quantity. |

**References out:** [Countries](Common.md#Common.Country), [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [Units](Common.md#Common.Unit)
**Referenced by:** [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms)

<a id="Sales.ShipmentInformationSource"></a>
### ShipmentInformationSources

Represents a shipment information source.

- **Endpoint:** `GET /api/v1/Sales/ShipmentInformationSources`
- **Required permission:** Show shipment
- **Introduced in:** 23.1

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the shipment information source. |
| `ShipmentId` | `Int64?` | yes | [Shipments](Sales.md#Sales.Shipment) | The business key identifier of the shipment of the shipment information source. |
| `ShipmentInformationSourceType` | `Int32` | no |  | The shipment information source type of the shipment information source. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order of the shipment information source. |
| `PickingListId` | `Int64?` | yes | [SalesPickingLists](Sales.md#Sales.SalesPickingList) | The business key identifier of the picking list of the shipment information source. |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier of the shipment information source. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer of the shipment information source. |
| `CustomerOrderInvoiceId` | `Int64?` | yes | [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice) | The business key identifier of the customer order shipment of the shipping information source. |
| `RowIndex` | `Int32` | no |  | The row index of the shipment information source. |

- `ShipmentInformationSourceType` — CustomerOrder=0, Supplier=1, PickingList=2, Customer=3, PickingListWithPackageStructure=4, Subcontract=5, ReturnOrder=6

**References out:** [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [SalesPickingLists](Sales.md#Sales.SalesPickingList), [Shipments](Sales.md#Sales.Shipment), [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation)

<a id="Sales.ShipmentPackageInformationPackageNumber"></a>
### ShipmentPackageInformationPackageNumbers

Represents a shipping agents real package number for a shipment package information.

- **Endpoint:** `GET /api/v1/Sales/ShipmentPackageInformationPackageNumbers`
- **Required permission:** Show shipment
- **Introduced in:** 24.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the shipment package information package number. |
| `ParentId` | `Int64` | no | [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation) | The business key identifier of the ShipmentPackageInformation it belongs to. |
| `ShippingAgentsPackageNumber` | `String` | no |  | The Real PackageNumber from shipper or edited manually of the package information. |

**References out:** [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation)
**Referenced by:** [ShipmentPackageInformations](Sales.md#Sales.ShipmentPackageInformation)

<a id="Sales.ShipmentPackageInformation"></a>
### ShipmentPackageInformations

Represents a shipment package information.

- **Endpoint:** `GET /api/v1/Sales/ShipmentPackageInformations`
- **Required permission:** Show shipment
- **Introduced in:** 23.1

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the shipment package information. |
| `InformationSourceId` | `Int64?` | yes | [ShipmentInformationSources](Sales.md#Sales.ShipmentInformationSource) | The business key identifier of the information source of the package information. |
| `Count` | `Int32` | no |  | The number of packages of the package information. |
| `PackageTypeName` | `String` | no |  | The package type name of the package information. |
| `PackageType` | `Int64?` | yes | [PackageTypes](Inventory.md#Inventory.PackageType) | The business key identifier of the package type of the package information. |
| `GoodsTypeName` | `String` | no |  | The goods type name of the package information. |
| `GoodsType` | `Int64?` | yes | [GoodsTypes](Inventory.md#Inventory.GoodsType) | The business key identifier of the goods type of the package information. |
| `PackageIdentification` | `String` | no |  | The package identification of the package information. |
| `PackageTypeCode` | `String` | no |  | The package type code of the package information. |
| `Volume` | `Decimal` | no |  | The volume of the package information. |
| `GrossWeight` | `Decimal` | no |  | The gross weight of the package information. |
| `LoadingMeters` | `Decimal` | no |  | The loading meters of the package information. |
| `Length` | `Decimal` | no |  | The length of the package information. |
| `Width` | `Decimal` | no |  | The width of the package information. |
| `Height` | `Decimal` | no |  | The height of the package information. |
| `GoodsLabel` | `String` | no |  | The GoodsLabel of the package information. |
| `PackageNumber` | `String` | no |  | The PackageNumber to identify a package with a Shipping Partner of the package information. |
| `ShippingAgentsPackageNumbers` | `ShipmentPackageInformationPackageNumbers[]` | no | [ShipmentPackageInformationPackageNumbers](Sales.md#Sales.ShipmentPackageInformationPackageNumber) | The Real PackageNumbers from shipping agent or edited manually of the package information. |
| `ShipmentId` | `Int64?` | yes | [Shipments](Sales.md#Sales.Shipment) | The business key identifier of the shipment of the package information. |
| `RowIndex` | `Int32?` | yes |  | The row index of the package information. |

**References out:** [GoodsTypes](Inventory.md#Inventory.GoodsType), [PackageTypes](Inventory.md#Inventory.PackageType), [ShipmentInformationSources](Sales.md#Sales.ShipmentInformationSource), [ShipmentPackageInformationPackageNumbers](Sales.md#Sales.ShipmentPackageInformationPackageNumber), [Shipments](Sales.md#Sales.Shipment)
**Referenced by:** [ShipmentPackageInformationPackageNumbers](Sales.md#Sales.ShipmentPackageInformationPackageNumber)

<a id="Sales.Shipment"></a>
### Shipments

Represents a shipment.

- **Endpoint:** `GET /api/v1/Sales/Shipments`
- **Required permission:** Show shipment
- **Introduced in:** 23.1

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the shipment. |
| `ShipmentNumber` | `String` | no |  | The human readable identifier of the shipment. |
| `ConsignmentNo` | `String` | no |  | The real consignment/shipment number from the shipper. |
| `UnifaunOnlineFirstParcelNo` | `String` | no |  | The unifaun online first parcel number of the shipment. |
| `UnifaunOnlineFirstPrintLink` | `String` | no |  | The unifaun online first print link of the shipment. |
| `LogTradeTrackingNo` | `String` | no |  | The log trade tracking number of the shipment. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the shipments delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) | The business key identifier of the shipments delivery term. |
| `DeliveryTermStandardCode` | `String` | no |  | The delivery term standard code of the shipment. |
| `DeliveryTermLocation` | `String` | no |  | The delivery term location of the shipment. |
| `ShippingAgentType` | `Int32` | no |  | The shipping agent type of the shipment. |
| `ShipmentPayer` | `Int32` | no |  | The shipment payer of the shipment. |
| `ShipmentPayerReference` | `String` | no |  | The shipment payer reference of the shipment. |
| `TransportDate` | `DateTimeOffset` | no |  | The transport date of the shipment. |
| `StoredShipment` | `Boolean` | no |  | Indicates if the shipment is stored. |
| `PickupDate` | `DateTimeOffset?` | yes |  | The pickup date of the shipment. |
| `PickupTimeFrom` | `DateTimeOffset?` | yes |  | The pickup time from of the shipment. |
| `PickupTimeTo` | `DateTimeOffset?` | yes |  | The pickup time to of the shipment. |
| `ExportDate` | `DateTimeOffset?` | yes |  | The export date of the shipment. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  | The delivery date of the shipment. |
| `DeliveryTime` | `DateTimeOffset?` | yes |  | The delivery time of the shipment. |
| `PickupText1` | `String` | no |  | The first pickup text of the shipment. |
| `PickupMisc` | `String` | no |  | The pickup misc. text of the shipment. |
| `SchenkerOpalNumber` | `String` | no |  | The Schenker opal number of the shipment. |
| `IsConsolidated` | `Boolean` | no |  | Indicates if the shipment is consolidated. |
| `ConsolidateKey` | `String` | no |  | The consolidate key of the shipment. |
| `TotalEurPallets` | `Int32` | no |  | The total number of euro pallets on the shipment. |
| `CurrentInformationSourceType` | `Int32` | no |  | The current shipment information source type of the shipment. |
| `Status` | `Int32` | no |  | The status of the shipment. |
| `ShippingAgentId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the shipping agent of the shipment. |
| `RecipientAdressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the recipient adress of the shipment. |
| `RecipientAdress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The recipient adress of the shipment. |
| `RecipientInvoiceAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the recipient invoice adress of the shipment. |
| `RecipientInvoiceAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The recipient invoice adress of the shipment. |
| `FreightPayerAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the freight payer adress of the shipment. |
| `FreightPayerAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The freight payer adress of the shipment. |
| `ConsignmentId` | `String` | no |  | The consignment id of the shipment. |
| `ConsignmentIdForReturn` | `String` | no |  | The consignment id for return of the shipment. |
| `OurReferenceName` | `String` | no |  | Our reference name of the shipment. |
| `OurReferencePhoneNumber` | `String` | no |  | Our reference phone number of the shipment. |
| `OurReferenceMobilePhoneNumber` | `String` | no |  | Our reference mobile phone number of the shipment. |
| `OurReferenceMail` | `String` | no |  | Our reference mail of the shipment. |
| `OurPickUpAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of our pick up address of the shipment. |
| `OurPickUpAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | Our pick up adress of the shipment. |
| `OurInvoiceAdressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of our invoce address of the shipment. |
| `OurInvoiceAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | Our invoice adress of the shipment. |
| `PalletRegistrationNo` | `String` | no |  | The pallet registration number of the shipment. |
| `OurPalletRegistrationNo` | `String` | no |  | Our pallet registration number of the shipment. |
| `BusinessContactReferenceName` | `String` | no |  | The business contact reference name of the shipment. |
| `BusinessContactReferencePhoneNumber` | `String` | no |  | The business contact reference phone number of the shipment. |
| `BusinessContactReferenceMobilePhoneNumber` | `String` | no |  | The business contact reference mobile phone number of the shipment. |
| `BusinessContactReferenceMail` | `String` | no |  | The business contact reference mail of the shipment. |
| `ShippingTemplate` | `String` | no |  | The shipping template code of the shipment. |
| `ShippingTemplateId` | `Int64?` | yes | [ShippingTemplates](Sales.md#Sales.ShippingTemplate) | The business key identifier of the shipping template of the shipment. |
| `ShippingServiceId` | `Int64?` | yes | [ShippingServices](Sales.md#Sales.ShippingService) | The business key identifier of shipping service of the shipment. |
| `ShippingService` | `ShippingServices` | no | [ShippingServices](Sales.md#Sales.ShippingService) | The shipping service of the shipment. |
| `ShippingServiceCode` | `String` | no |  | The shipping service code of the shipment. |
| `SenderQuickId` | `String` | no |  | The sender quick id of the shipment. |
| `SellerQuickId` | `String` | no |  | The seller quick id of the shipment. |
| `ConsignorId` | `String` | no |  | The consignor id of the shipment. |
| `PickupId` | `String` | no |  | The pickup id of the shipment. |
| `LogTradePrintQueue` | `String` | no |  | The log trade print queue of the shipment. |
| `ShippingAgentCode` | `String` | no |  | The shipping agent code of the shipment. |
| `SenderReference` | `String` | no |  | The sender reference of the shipment. |
| `RecipientReference` | `String` | no |  | The recipient reference of the shipment. |
| `DeliveryInstruction` | `String` | no |  | The delivery instruction of the shipment. |
| `BookTransport` | `Boolean` | no |  | Indicates if the shipment has booked transport. |
| `ReturnLabel` | `Boolean` | no |  | Indicates if the shipment has return label. |
| `ShipmentPrintSetting` | `Int32` | no |  | The print setting of the shipment. |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the active delivery address customer of the shipment. |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the active delivery address supplier of the shipment. |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  | The business key identifier of the active delivery address company of the shipment. |
| `ActiveDeliveryAddressDeliveryAddressId` | `Int64?` | yes | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The business key identifier of the active delivery address delivery address of the shipment. |
| `ActiveDeliveryAddressDeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The active delivery address delivery address of the shipment. |
| `ActiveFallbackDeliveryAddressDeliveryAddressId` | `Int64?` | yes | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The business key identifier of the active fallback delivery address delivery address of the shipment. |
| `ActiveFallbackDeliveryAddressDeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The active fallback delivery address delivery address of the shipment. |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  | The source of alternative delivery addresses of the shipment. |
| `WarehouseShippingAgentCode` | `String` | no |  | The warehouse shipping agent code of the shipment. |
| `CustomerGoodsAddressNumber` | `String` | no |  | The customer goods address number of the shipment. |
| `CustomerShippingAgentCode` | `String` | no |  | The customer shipping agent code of the shipment. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the shipments warehouse. |
| `ShippingAgentAccountName` | `String` | no |  | The shipping agent account name of the shipment. |
| `CalculatedFreightPrice` | `Decimal?` | yes |  | The calculated freight price of the shipment. |
| `CalculatedFreightPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the calculated freight price currency of the shipment. |
| `CalculatedFreightPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The calculated freight price currency of the shipment. |
| `MobilePhoneNotificationNumber` | `String` | no |  | The mobile phone notification number for phone advice of the shipment. |
| `GoodsTrackingUrl` | `String` | no |  | The goods tracking URL of the shipment. |
| `CustomsId` | `Int64?` | yes |  | The business key identifier of the customs information of the shipment. |
| `Customs` | `ShipmentCustoms` | no | [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms) | The customs information of the shipment. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the shipping service. |
| `Name` | `String` | no |  | The name of the shipping service. |
| `Code` | `String` | no |  | The human readable identifier of the shipping service. |
| `LogTradePrintQueue` | `String` | no |  | The Logtrade print queue of the shipping service. |
| `SchenkerOpalNumber` | `String` | no |  | The Schenker opal number of the shipping service. |
| `ConsolidatedShipment` | `Boolean` | no |  | Indicates if the shipping service is a consolidated shipment. |
| `StoredShipment` | `Boolean` | no |  | Indicates if the shipping service is a stored shipment. |
| `UseSellerAddress` | `Boolean` | no |  | Indicates if the shipping service use seller address. |
| `UsePurchaserAddress` | `Boolean` | no |  | Indicates if the shipping service use purchaser address. |
| `UseFrieghtPayerAddress` | `Boolean` | no |  | Indicates if the shipping service use frieght payer address. |
| `ShippingTemplateId` | `Int64?` | yes | [ShippingTemplates](Sales.md#Sales.ShippingTemplate) | The business key identifier of the shipping template of the shipping service. |
| `SenderQuickId` | `String` | no |  | The sender quick id of the shipping service. |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier of the shipping service. |
| `SellerQuickId` | `String` | no |  | The seller quick id of the shipping service. |

**References out:** [ShippingTemplates](Sales.md#Sales.ShippingTemplate), [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [Shipments](Sales.md#Sales.Shipment)

<a id="Sales.ShippingTemplate"></a>
### ShippingTemplates

Represents a shipping service.

- **Endpoint:** `GET /api/v1/Sales/ShippingTemplates`
- **Required permission:** Show shipment
- **Introduced in:** 23.1

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the shipping template. |
| `ShippingTemplateName` | `String` | no |  | The name of the shipping template. |
| `ShippingTemplateCode` | `String` | no |  | The human readable identifier of the shipping template. |
| `ExportPickupAddress` | `Boolean` | no |  | Indicates if the shipping template export pickup address. |
| `ExportDeliveryAddress` | `Boolean` | no |  | Indicates if the shipping template export delivery address. |
| `ConsignorId` | `String` | no |  | The consignor id of the shipping template. |
| `PickupId` | `String` | no |  | The pickup id of the shipping template. |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the shipping templates supplier. |

**References out:** [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [Shipments](Sales.md#Sales.Shipment), [ShippingServices](Sales.md#Sales.ShippingService)

<a id="Sales.ValidityTime"></a>
### ValidityTimes

Represents a validity time.

- **Endpoint:** `GET /api/v1/Sales/ValidityTimes`
- **Required permission:** Show terms
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the validity time. |
| `Number` | `Int64` | no |  | The human readable identifier of the validity time. |
| `IsDefault` | `Boolean` | no |  | Specifies if the validity time is default. |
| `Days` | `Int32` | no |  | Specifies the validity time in days. |
| `Description` | `String` | no |  | The translated description of the validity time. |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |

**Referenced by:** [Customers](Sales.md#Sales.Customer), [Quotes](Sales.md#Sales.Quote)


## Commands

<a id="Sales.CreateCustomerEmployeeSpan"></a>
### CreateCustomerEmployeeSpan

Creates a new customer employee span object.

- **Endpoint:** `POST /api/v1/Sales/CustomerEmployeeSpans/Create`
- **Required permission:** Create new customer
- **Introduced in:** 24.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Code` | `Int64` | no |  | The human readable identifier of the customer employee span object. |
| `Description` | `String` | no |  | The translated description of the customer employee span object. |


<a id="Sales.CreateSalesPickingList"></a>
### CreateSalesPickingList

Creates picking lists.

- **Endpoint:** `POST /api/v1/Sales/SalesPickingLists/Create`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `DeliveryRows` | `DeliveryRow[]` | no |  | Collection of the customer order rows that should be added to the picking list. |
| `CreatedByPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the person that created the picking list. |
| `OutgoingDeliveryLocationName` | `String` | no |  | The name of the outgoing delivery location for the picking list. |

**References out:** [Persons](Common.md#Common.Person)

<a id="Sales.GetWithdrawalInformation"></a>
### GetWithdrawalInformation

Calculates and returns the suggested withdrawal information for a picking list.

- **Endpoint:** `POST /api/v1/Sales/SalesPickingLists/GetWithdrawalInformation`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `PickingListId` | `Int64` | no | [SalesPickingLists](Sales.md#Sales.SalesPickingList) | The business key identifier of the picking list. |

**References out:** [SalesPickingLists](Sales.md#Sales.SalesPickingList)

<a id="Sales.RemoveSalesPickingList"></a>
### RemoveSalesPickingList

Deletes a picking list.

- **Endpoint:** `POST /api/v1/Sales/SalesPickingLists/Remove`
- **Required permission:** Show customer orders
- **Introduced in:** 2.53

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `PickingListId` | `Int64` | no | [SalesPickingLists](Sales.md#Sales.SalesPickingList) | The business key identifier of the picking list that will get removed. |

**References out:** [SalesPickingLists](Sales.md#Sales.SalesPickingList)


## Payload types

<a id="Sales.WithdrawalInformationLocation"></a>
### WithdrawalInformationLocation

Used to provide the suggested withdrawal information of a location.

- **Introduced in:** 2.53

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `PartLocationId` | `Int64` | no | [PartLocations](Inventory.md#Inventory.PartLocation) | The business key identifier of the part location. |
| `ProductRecordId` | `Int64?` | yes | [PartLocations](Inventory.md#Inventory.PartLocation) | The business key identifier of the product record. |
| `ReservedQuantity` | `Decimal` | no |  | The reserved quantity for the location. |
| `AvailableQuantity` | `Decimal` | no |  | The available quantity for the location. |
| `SuggestedQuantity` | `Decimal` | no |  | The suggested quantity to withdraw from the location. |

**References out:** [PartLocations](Inventory.md#Inventory.PartLocation)
**Referenced by:** [WithdrawalInformationRow](Sales.md#Sales.WithdrawalInformationRow)

<a id="Sales.WithdrawalInformationRow"></a>
### WithdrawalInformationRow

Used to provide the suggested withdrawal information of a customer order row.

- **Introduced in:** 2.53

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `CustomerOrderRowId` | `Int64` | no | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The business key identifier of the customer order row that the withdrawal information is for. |
| `PickingListId` | `Int64` | no | [SalesPickingLists](Sales.md#Sales.SalesPickingList) | The business key identifier of the picking list that the withdrawal information is for. |
| `Locations` | `WithdrawalInformationLocation[]` | no | [WithdrawalInformationLocation](Sales.md#Sales.WithdrawalInformationLocation) | The location withdrawal information. |
| `SuggestedQuantity` | `Decimal` | no |  | The suggested quantity to withdraw. |
| `ParentCustomerOrderRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The business key identifier of the customer order row's parent row that the withdrawal information is for. |

**References out:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [SalesPickingLists](Sales.md#Sales.SalesPickingList), [WithdrawalInformationLocation](Sales.md#Sales.WithdrawalInformationLocation)


## Depends on other modules

- [Accounting](Accounting.md): [Accounts](Accounting.md#Accounting.Account), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [Codings](Accounting.md#Accounting.Coding), [CodingEntries](Accounting.md#Accounting.CodingEntry), [FixedAssets](Accounting.md#Accounting.FixedAsset)
- [Common](Common.md): [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Countries](Common.md#Common.Country), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [DeliveryTimes](Common.md#Common.DeliveryTime), [Discounts](Common.md#Common.Discount), [DiscountCategories](Common.md#Common.DiscountCategory), [ExtraFields](Common.md#Common.ExtraField), [FormReportConfigurations](Common.md#Common.FormReportConfiguration), [LanguageCodes](Common.md#Common.LanguageCode), [PartConfigurations](Common.md#Common.PartConfiguration), [PartialQuantities](Common.md#Common.PartialQuantity), [PaymentMethods](Common.md#Common.PaymentMethod), [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [PriceLists](Common.md#Common.PriceList), [Probabilities](Common.md#Common.Probability), [Projects](Common.md#Common.Project), [ReasonCodeDebitNotes](Common.md#Common.ReasonCodeDebitNote), [Resellers](Common.md#Common.Reseller), [Revisions](Common.md#Common.Revision), [StaggeredPrices](Common.md#Common.StaggeredPrice), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode), [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat), [TransferProfiles](Common.md#Common.TransferProfile), [Units](Common.md#Common.Unit), [VatGroups](Common.md#Common.VatGroup), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse)
- [Inventory](Inventory.md): [CaseEntry](Inventory.md#Inventory.CaseEntry), [GoodsTypes](Inventory.md#Inventory.GoodsType), [PackageTypes](Inventory.md#Inventory.PackageType), [Parts](Inventory.md#Inventory.Part), [PartLocations](Inventory.md#Inventory.PartLocation), [ProductRecords](Inventory.md#Inventory.ProductRecord)
- [Manufacturing](Manufacturing.md): [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder)
- [Purchase](Purchase.md): [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [Suppliers](Purchase.md#Purchase.Supplier)
