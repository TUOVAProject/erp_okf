# Purchase

Monitor API module `Purchase`: 30 queryable entities, 0 commands, 0 payload types.

## Queryable entities

<a id="Purchase.BlanketOrderPurchaseRow"></a>
### BlanketOrderPurchaseRows

Represents a blanket order row for purchase.

- **Endpoint:** `GET /api/v1/Purchase/BlanketOrderPurchaseRows`
- **Required permission:** Show blanket order
- **Introduced in:** 23.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the blanket order row. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the row. |
| `ParentOrderId` | `Int64?` | yes | [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase) | The business key identifier of the row's blanket order. |
| `ParentRowId` | `Int64?` | yes | [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow) | The business key identifier of the row's parent row. |
| `SupplierPartNumber` | `String` | no |  | The supplier's part number of the row. |
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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the blanket order. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the blanket order. |
| `OrderNumber` | `String` | no |  | The human readable identifier of the blanket order. |
| `OrderTypeId` | `Int64?` | yes | [BlanketOrderPurchaseTypes](Purchase.md#Purchase.BlanketOrderPurchaseType) | The business key identifier of the blanket order's type. |
| `BusinessContactId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the blanket order's supplier. |
| `SuppliersOrderNumber` | `String` | no |  | The supplier's order number of the blanket order. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the blanket order's business contact reference. |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business contact reference of the blanket order. |
| `BusinessContactReferenceName` | `String` | no |  | The business contact reference name of the blanket order. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the blanket order's our reference. |
| `OurReference` | `Persons` | no | [Persons](Common.md#Common.Person) | Our reference of the blanket order. |
| `OurReferenceName` | `String` | no |  | Our reference name of the blanket order. |
| `ValidationPeriod` | `Int32` | no |  | Specifies the validation period of the blanket order. |
| `ValidFrom` | `DateTimeOffset` | no |  | The valid from date of the blanket order. |
| `ValidThrough` | `DateTimeOffset` | no |  | The valid through date of the blanket order. |
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
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the blanket order's currency exchange type. |
| `CurrencyExchangeType` | `CurrencyExchangeTypes` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The currency exchange type of the blanket order. |
| `Rows` | `BlanketOrderPurchaseRows[]` | no | [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow) | The rows of the blanket order. |

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
| `BlanketOrderPurchaseActivityTemplateId` | `Int64?` | yes |  | The business key identifier of the blanket order types activity template. |
| `RateTypeSetting` | `Int32` | no |  | The rate typ setting of the blanket order type. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the blanket order type's currency exchange type. |
| `DefaultValidDays` | `Int32` | no |  | The default valid days of the blanket order type. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the document. |
| `BlobDataId` | `Int64` | no | [BlobData](Common.md#Common.BlobData) | The business key identifier of the blob data contained in the document. |
| `RotationAngle` | `Int32` | no |  | The amount of rotation in degrees to be applied to the document. |
| `AccountsPayableId` | `Int64` | no | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of the accounts payable to which document belongs. |
| `DocumentTypeId` | `Int64` | no | [EimDocumentTypes](Purchase.md#Purchase.EimDocumentType) | The business key identifier of the document type of the document. |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [BlobData](Common.md#Common.BlobData), [EimDocumentTypes](Purchase.md#Purchase.EimDocumentType)

<a id="Purchase.EimDocumentType"></a>
### EimDocumentTypes

Represents an EIM document type.

- **Endpoint:** `GET /api/v1/Purchase/EimDocumentTypes`
- **Required permission:** Show attachment types
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the document type. |
| `Number` | `Int64` | no |  | The human readable identifier of the document type. |
| `Description` | `String` | no |  | The name of the document type. |
| `IsDefaultImportType` | `Boolean` | no |  | Specifies if the type is the default type for E-invoice imports. |
| `IsDefaultMonitorExpenseType` | `Boolean` | no |  | Specifies if the type is the default type for imports from Monitor Expense. |
| `IsDefaultBankIntegrationType` | `Boolean` | no |  | Specifies if the type is the default type for imports via bank integration. |

**Referenced by:** [EimDocuments](Purchase.md#Purchase.EimDocument)

<a id="Purchase.Inquiry"></a>
### Inquiries

Represents an inquiry.

- **Endpoint:** `GET /api/v1/Purchase/Inquiries`
- **Required permission:** Show inquiry
- **Introduced in:** 2.30

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the inquiry. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the inquiry's payment term. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The payment term of the inquiry. |
| `PaymentTermDescription` | `String` | no |  | The payment term description of the inquiry. |
| `GracePeriodInDays` | `Int32?` | yes |  | The inquiry's grace period in days. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the inquiry's delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) | The business key identifier of the inquiry's delivery term. |
| `DeliveryTermDescription` | `String` | no |  | The delivery term description of the inquiry. |
| `DeliveryMethodDescription` | `String` | no |  | The delivery method description of the inquiry. |
| `BusinessContactOrderNumber` | `String` | no |  | The supplier's inquiry number. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of our reference on the inquiry. Reference Persons |
| `OurReferenceName` | `String` | no |  | The name of our reference on the inquiry. |
| `BusinessContactReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the supplier's reference on the inquiry. Reference Persons |
| `BusinessContactReferenceName` | `String` | no |  | The name of the supplier's reference on the inquiry. |
| `GoodsLabel` | `String` | no |  | The goods label of the inquiry. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the inquiry's currency. |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) | The business key identifier of the inquiry's VAT group. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the inquiry's warehouse. |
| `Priority` | `Int32` | no |  | The priority of the inquiry. |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of the inquiry's project. |
| `SendMethod` | `Int32` | no |  | Specifies the method of the inquiry printout. |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the inquiry's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the inquiry. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the inquiry's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The external comment of the inquiry. |
| `TransportTime` | `Int32?` | yes |  | The transport time of the inquiry. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the inquiry. |
| `Version` | `Int32` | no |  | The version of the inquiry. |
| `UseForwardRate` | `Boolean` | no |  | Specifies if forward rate should be used. |
| `ExchangeRate` | `Decimal` | no |  | The exchange rate to use for the inquiry. |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier that the inquiry belongs to. |
| `OrderNumber` | `String` | no |  | The order number of the purchase order created as a result of the inquiry. |
| `OrderDate` | `DateTimeOffset?` | yes |  | The date/time when the inquiry was made. |
| `Rows` | `InquiryRows[]` | no | [InquiryRows](Purchase.md#Purchase.InquiryRow) | The rows of the inquiry. |
| `CreatedById` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the inquiry's creator. _(Unavailable)_ |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the inquiry's delivery address. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The delivery address of the inquiry. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the inquiry's mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The mailing address of the inquiry. |
| `VatNumber` | `String` | no |  | The VAT number on the inquiry. _(Unavailable)_ |
| `Status` | `Int32` | no |  | The status of the inquiry. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) | The communication addresses registered on the inquiry. |
| `InquiryDate` | `DateTimeOffset` | no |  | The date when the inquiry was made to the supplier. |
| `InquiryDescription` | `String` | no |  | The description of the inquiry. |
| `LatestContactDate` | `DateTimeOffset?` | yes |  | The last contact date on the inquiry. |
| `ValidThroughDate` | `DateTimeOffset?` | yes |  | The valid through date of the inquiry. |
| `OrderTypeId` | `Int64?` | yes | [InquiryTypes](Purchase.md#Purchase.InquiryType) | The business key identifier of the inquiry's inquiry type. |
| `OrderType` | `InquiryTypes` | no | [InquiryTypes](Purchase.md#Purchase.InquiryType) | The inquiry type used on the inquiry. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the inquiry's currency exchange type. |

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
| `ParentRowId` | `Int64?` | yes | [InquiryRows](Purchase.md#Purchase.InquiryRow) | The business key identifier of the row's parent. |
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
| `ShowFreeTextIn` | `Int32` | no |  | Specifies which documents the free text data of the row should be projected on. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) | The business key identifier of the row's statistical goods code. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of the purchase order that was created as a result of the row. |
| `ExemptFromStatistics` | `Boolean` | no |  | Specifies if the row should be exempted from statistics. |
| `ParentOrderId` | `Int64` | no | [Inquiries](Purchase.md#Purchase.Inquiry) | The business key identifier of the rows parent inquiry. |
| `CodingId` | `Int64?` | yes | [Codings](Accounting.md#Accounting.Coding) | The business key identifier of the rows coding. |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) | The coding of the row. |
| `RowIndex` | `Int32?` | yes |  | The index of the row. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the type. |
| `Number` | `Int64` | no |  | The human readable identifier of the type. |
| `Prefix` | `String` | no |  | The prefix to apply on inquiry numbers spawned from this type. |
| `Description` | `String` | no |  | The translated description of the type. |
| `Priority` | `Int32` | no |  | The priority of the type. |
| `Visible` | `Boolean` | no |  | Specifies if the type is visible. |
| `IsPreset` | `Boolean` | no |  | Specifies if the type is a preset type. |
| `BaseType` | `Int32` | no |  | The base type of inquiries created from this type. |
| `CodingGroupId` | `Int64` | no |  | The business key identifier of the type's coding group. |
| `RateTypeSetting` | `Int32` | no |  | The rate type setting of the inquiry type. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the inquiry type's currency exchange type. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `PartialQuantities` | `PartialQuantities[]` | no | [PartialQuantities](Common.md#Common.PartialQuantity) | The partial quantities for the order quantity. |

**References out:** [PartialQuantities](Common.md#Common.PartialQuantity)
**Referenced by:** [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)

<a id="Purchase.OtherSupplierNumber"></a>
### OtherSupplierNumbers

Represents an alternative supplier code mainly used for EDI.

- **Endpoint:** `GET /api/v1/Purchase/OtherSupplierNumbers`
- **Required permission:** Show supplier
- **Introduced in:** 2.32

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the other supplier number. |
| `IsDefault` | `Boolean` | no |  | Specifies if this is the default/active other supplier number. |
| `Number` | `String` | no |  | The human readable identifier of the other supplier number. |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the owning supplier. |

**References out:** [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.PackingTerm"></a>
### PackingTerms

Represents a packing term.

- **Endpoint:** `GET /api/v1/Purchase/PackingTerms`
- **Required permission:** Show terms
- **Introduced in:** 2.28

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the packing term. |
| `Description` | `String` | no |  | The description of the packing term. |
| `Number` | `Int64` | no |  | The human readable identifier of the packing term. |
| `IsDefault` | `Boolean` | no |  | The is default of the packing term. |

**Referenced by:** [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.PurchaseOrderAdviceRowProductRecord"></a>
### PurchaseOrderAdviceRowProductRecords

Represents a purchase order advice row product record.

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderAdviceRowProductRecords`
- **Required permission:** Show arrival
- **Introduced in:** 22.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the purchase order advice row product record. |
| `ParentId` | `Int64?` | yes | [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow) | The business key identifier of the purchase order advice row that this product record belongs to. |
| `TraceabilityMode` | `Int32` | no |  | The traceability mode for the product record. |
| `BatchNumber` | `String` | no |  | The batch number for the product record. |
| `BatchQuantity` | `Decimal` | no |  | The batch quantity for the product record. |
| `BatchBestBeforeDate` | `DateTimeOffset?` | yes |  | The batch best before date for the product record. |
| `SerialNumberPrefix` | `String` | no |  | The serial number prefix for the product records. |
| `SerialNumberStart` | `String` | no |  | The serial number start for the product records. |
| `SerialNumberCount` | `Int32` | no |  | Number of product records with serial number to create. |
| `ChargeNumber` | `String` | no |  | The charge number of the product record(s). |

- `TraceabilityMode` — None=0, Batch=1, Individual=2, IndividualOnlyWithdrawal=4

**References out:** [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow)

<a id="Purchase.PurchaseOrderAdviceRow"></a>
### PurchaseOrderAdviceRows

Represents a purchase order advice row.

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderAdviceRows`
- **Required permission:** Show arrival
- **Introduced in:** 22.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the purchase order advice row. |
| `PurchaseOrderRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The business key identifier of the purchase order row for this row. |
| `ParentId` | `Int64?` | yes | [PurchaseOrderAdvices](Purchase.md#Purchase.PurchaseOrderAdvice) | The business key identifier of the purchase order advice for this row. |
| `Status` | `Int32` | no |  | The status for the row. |
| `Quantity` | `Decimal` | no |  | The quantity for the row. |
| `DeliveredQuantity` | `Decimal` | no |  | The delivered quantity for the row. |
| `RestQuantity` | `Decimal` | no |  | The rest quantity for the row. |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the unit for the row. |
| `ConversionFactor` | `Decimal?` | yes |  | The conversion factor for the row. |
| `ParentRowId` | `Int64?` | yes | [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow) | The business key identifier of the purchase order advice row for the row. |
| `SupplierPackageNumber` | `String` | no |  | The supplier package number for the row. |
| `SupplierAgreementReference` | `String` | no |  | The supplier agreement reference tor the row. |

- `Status` — Registered=1, PartiallyDelivered=5, History=9

**References out:** [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow), [PurchaseOrderAdvices](Purchase.md#Purchase.PurchaseOrderAdvice), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [Units](Common.md#Common.Unit)
**Referenced by:** [PurchaseOrderAdviceRowProductRecords](Purchase.md#Purchase.PurchaseOrderAdviceRowProductRecord), [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow)

<a id="Purchase.PurchaseOrderAdvice"></a>
### PurchaseOrderAdvices

Represents a purchase order advice.

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderAdvices`
- **Required permission:** Show arrival
- **Introduced in:** 22.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the purchase order advice. |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier for the advice. |
| `Status` | `Int32` | no |  | The status of the advice. |
| `DispatchDate` | `DateTimeOffset` | no |  | The dispatch date of the advice. |
| `DeliveryNoteNumber` | `String` | no |  | The delivery note number of the advice. |
| `ShipmentNumber` | `String` | no |  | The shipment number of the advice. |
| `GoodsTrackingUrl` | `String` | no |  | The gods tracking url of the advice. |

- `Status` — Registered=1, PartiallyDelivered=5, History=9

**References out:** [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow)

<a id="Purchase.PurchaseOrderDelivery"></a>
### PurchaseOrderDeliveries

Represents a purchase order delivery entry

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderDeliveries`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the purchase order delivery. |
| `PurchaseOrderId` | `Int64` | no | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of the purchase order. |
| `ConfirmationDate` | `DateTimeOffset?` | yes |  | The confirmation date of the of purchase order delivery. _(This field has been removed as it was never used.)_ |
| `AdviceDate` | `DateTimeOffset?` | yes |  | The advice date of the of purchase order delivery. _(This field has been removed as it was never used.)_ |
| `DeliveryNoteNumber` | `String` | no |  | The human readable delivery note number of the purchase order delivery. |
| `WayBillNumber` | `String` | no |  | The human readable way bill number of the purchase order delivery. |
| `Rows` | `PurchaseOrderDeliveryRows[]` | no | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) | The rows of the purchase order delivery. |
| `ArrivalNoteNumber` | `Int64` | no |  | The arrival note number of the purchase order delivery. |

**References out:** [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder)
**Referenced by:** [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice)

<a id="Purchase.PurchaseOrderDeliveryRowQuantity"></a>
### PurchaseOrderDeliveryRowQuantities

Represents a purchase order delivery row quantity entry

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderDeliveryRowQuantities`
- **Required permission:** Show purchase orders
- **Introduced in:** 26.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the purchase order delivery row quantity. |
| `QuantityChangeId` | `Int64` | no | [QuantityChanges](Inventory.md#Inventory.QuantityChange) | The business key identifier of the quantity change. |
| `QuantityChange` | `QuantityChanges` | no | [QuantityChanges](Inventory.md#Inventory.QuantityChange) | The quantity change. |
| `BusinessTransactionContextType` | `Int32` | no |  | The type of business transaction context. |
| `ParentId` | `Int64` | no | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) | The business key identifier of the purchase order delivery row. |

- `BusinessTransactionContextType` — NotInitialized=0, ArrivalReporting=1, ManufacturingOrderReporting=2, DeliveryReporting=3, PhysicalInventory=4, UnplannedStockWithdrawal=5, MoveBetweenWarehouse=6, MoveStockBalance=7, NonconformityPosteriorRejection=8, DirectlyRegisteredInvoice=9, RemovalOfPartLocation=10, ManufacturingOrderMaterialReporting=11, UnplannedStockArrivalReporting=12, StockImport=13, DeliveryReportingStockOrder=14, ArrivalReportingStockOrder=15, UndoManufacturingOrderMaterialReporting=16, UndoManufacturingOrderReporting=17, UndoArrivalReporting=18, UndoDeliveryReporting=19, UndoArrivalReportingStockOrder=20, UndoDeliveryReportingStockOrder=21, OutgoingReusable=22, ArrivalReusable=23, UndoOutgoingReusable=24, UndoArrivalReusable=25, ToolWithdrawal=26, ToolReturn=27, CreditSupplierInvoice=28, CreditCustomerInvoice=29, ReturnPurchaseOrder=30, SplitInvoiceBasis=31, CreationOfPartLocation=32, ArrivalsCorrection=33, ArrivalRejection=34, UndoReturnPurchaseOrder=35

**References out:** [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [QuantityChanges](Inventory.md#Inventory.QuantityChange)
**Referenced by:** [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow)

<a id="Purchase.PurchaseOrderDeliveryRow"></a>
### PurchaseOrderDeliveryRows

Represents a purchase order delivery row entry

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderDeliveryRows`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the purchase order delivery row. |
| `Version` | `Int32` | no |  | The version of the purchase order delivery row. |
| `PurchaseOrderId` | `Int64` | no | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of the purchase order. |
| `PurchaseOrderRowId` | `Int64` | no | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The business key identifier of the purchase order row. |
| `PurchaseOrderRow` | `PurchaseOrderRows` | no | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The purchase order row. |
| `DeliveryDate` | `DateTimeOffset` | no |  | The delivery date of the of order delivery row. |
| `GoodsLocation` | `String` | no |  | The human readable goods location of the order delivery row. |
| `GoodsMessage` | `String` | no |  | The human readable good message on the order delivery row. |
| `ArrivedQuantity` | `Decimal` | no |  | The arrived qty on the order delivery row. |
| `ApprovedQuantity` | `Decimal` | no |  | The approved qty on the order delivery row. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of the accounts payable the delivery row is linked to. |
| `PurchaseOrderDeliveryRowQuantities` | `PurchaseOrderDeliveryRowQuantities[]` | no | [PurchaseOrderDeliveryRowQuantities](Purchase.md#Purchase.PurchaseOrderDeliveryRowQuantity) | The quantities of the order delivery row. |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [PurchaseOrderDeliveryRowQuantities](Purchase.md#Purchase.PurchaseOrderDeliveryRowQuantity), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder)
**Referenced by:** [BookingRows](Accounting.md#Accounting.BookingRow), [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [PurchaseOrderDeliveries](Purchase.md#Purchase.PurchaseOrderDelivery), [PurchaseOrderDeliveryRowQuantities](Purchase.md#Purchase.PurchaseOrderDeliveryRowQuantity), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)

<a id="Purchase.PurchaseOrderInvoiceRow"></a>
### PurchaseOrderInvoiceRows

Represents a purchase order invoice row entry

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderInvoiceRows`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the purchase order invoice row. |
| `PurchaseOrderDeliveryRowId` | `Int64` | no | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) | The business key identifier of the purchase order delivery row. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the purchase order's invoice row comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the purchase order invoice row. |
| `Price` | `Decimal?` | yes |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row price currency. |
| `PriceLockedFromAutomaticChanges` | `Boolean` | no |  | Specifies if price is locked from automatic changes. |
| `PriceIsFuturePrice` | `Boolean` | no |  | Specifies if price is a future price. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  | The price of the row in company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the row price in the company currency. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the row setup price. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  | The setup price of the row in company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for row setup price in company currency. |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) | The business key identifier of the row's VAT rate. |
| `Discount` | `Decimal` | no |  | The discount in percent set for the row. |
| `StandardPrice` | `Decimal?` | yes |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the row standard price. |
| `CodingId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the row's coding. |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) | The coding of the row. |
| `LedgerId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of the invoice row's ledger. |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [CodingEntries](Accounting.md#Accounting.CodingEntry), [Codings](Accounting.md#Accounting.Coding), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice)

<a id="Purchase.PurchaseOrderInvoice"></a>
### PurchaseOrderInvoices

Represents a purchase order invoice entry

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderInvoices`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the purchase order invoice. |
| `PurchaseOrderDeliveryId` | `Int64?` | yes | [PurchaseOrderDeliveries](Purchase.md#Purchase.PurchaseOrderDelivery) | The business key identifier of the purchase order delivery. |
| `AccountGroupId` | `Int64?` | yes | [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup) | The business key identifier of the supplier account group. References SupplierAccountGroups . |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the purchase order invoice belongs to. |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) | The business key identifier of the VAT group that applies for the purchase order invoice. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the payment term of the purchase order invoice. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The payment term of the purchase order invoice. |
| `PaymentTermDescription` | `String` | no |  | The payment term description of the purchase order invoice. |
| `GracePeriodInDays` | `Int32?` | yes |  | The purchase order invoice grace period in days. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the purchase order invoice delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) | The business key identifier of the purchase order invoice delivery term. |
| `DeliveryTermDescription` | `String` | no |  | The delivery term description of the purchase order invoice. |
| `DeliveryMethodDescription` | `String` | no |  | The delivery method description of the purchase order invoice. |
| `ShipmentPayer` | `Int32` | no |  | Specifies who is responsible for the shipment payment for the purchase order invoice. |
| `Rows` | `PurchaseOrderInvoiceRows[]` | no | [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow) | The rows of the purchase order invoice. |

- `ShipmentPayer` — BuyerPays=1, SellerPays=2, OtherPayer=3, Incoterms=4

**References out:** [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [PaymentTerms](Common.md#Common.PaymentTerm), [PurchaseOrderDeliveries](Purchase.md#Purchase.PurchaseOrderDelivery), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup), [VatGroups](Common.md#Common.VatGroup), [Warehouses](Common.md#Common.Warehouse)

<a id="Purchase.PurchaseOrderRow"></a>
### PurchaseOrderRows

Represents a purchase order row.

- **Endpoint:** `GET /api/v1/Purchase/PurchaseOrderRows`
- **Required permission:** Show purchase orders
- **Introduced in:** 2.26

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
| `ParentRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The business key identifier of the current row's parent. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  | The delivery date set for the row. |
| `RevisionId` | `Int64?` | yes | [Revisions](Common.md#Common.Revision) | The business key identifier of the row's revision. |
| `Revision` | `Revisions` | no | [Revisions](Common.md#Common.Revision) | The revision of the row. |
| `OrderedQuantity` | `Decimal` | no |  | The ordered quantity of the row. |
| `Price` | `Decimal?` | yes |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row price currency. |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The price currency for the row. |
| `Discount` | `Decimal` | no |  | The discount in percent set for the row. |
| `ToolId` | `Int64?` | yes |  | The business key identifier of the tool of the row. _(Replaced by Part)_ |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The unit of the row. |
| `VatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) | The business key identifier of the row's VAT rate. |
| `VatRate` | `VatRates` | no | [VatRates](Common.md#Common.VatRate) | The VAT rate of the row. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the row belongs to. |
| `Warehouse` | `Warehouses` | no | [Warehouses](Common.md#Common.Warehouse) | The warehouse that the row belongs to. |
| `WeightPerUnit` | `Decimal?` | yes |  | The weight per unit of the row. |
| `OrderDate` | `DateTimeOffset` | no |  | The order date of the row. |
| `ConversionFactor` | `Decimal` | no |  | The conversion factor of the row. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  | The row price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency. |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  | The setup price of the row in the company currency. |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes |  | The business key identifier of the company currency. |
| `StandardPrice` | `Decimal?` | yes |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's standard price currency. |
| `StandardPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The standard price currency of the row. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price of the row. |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the row's setup price currency. |
| `SetupPriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The setup price currency of the row. |
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
| `ShowFreeTextIn` | `Int32` | no |  | Specifies which documents the free text row data will appear on. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) | The business key identifier of the row's statistical goods code. |
| `StatisticalGoodsCode` | `StatisticalGoodsCodes` | no | [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode) | The statistical goods code of the row. |
| `RowStatus` | `Int32` | no |  | The status of the purchase order row. |
| `Version` | `Int32` | no |  | The version of the row. |
| `ArrivalReporting` | `Boolean` | no |  | Specifies if the row uses arrival reporting. |
| `ConfirmedDelayed` | `Boolean` | no |  | Specifies if the row is confirmed delayed. |
| `DelayCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the row's delay comment. |
| `DelayComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The delay comment of the row. |
| `DelayReasonId` | `Int64?` | yes | [ReasonCodes](Common.md#Common.ReasonCode) | The business key identifier of the row's delay reason. |
| `DelayReason` | `ReasonCodes` | no | [ReasonCodes](Common.md#Common.ReasonCode) | The delay reason of the row. |
| `CodingId` | `Int64?` | yes |  | The business key identifier of the row's coding. |
| `Coding` | `Codings` | no | [Codings](Accounting.md#Accounting.Coding) | The coding of the row. |
| `IsConfirmed` | `Boolean` | no |  | Specifies if the row is confirmed. |
| `ReceivingInspectionInstructionId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the row's receiving inspection instruction. |
| `ReceivingInspectionInstruction` | `Comments` | no | [Comments](Common.md#Common.Comment) | The receiving inspection instruction of the row. |
| `ReceivingInspectionType` | `Int32` | no |  | The receiving inspection type of the row. |
| `ReceivingMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the row's receiving message. |
| `ReceivingMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) | The receiving message of the row. |
| `RequiredForManufacturingOrderNode` | `Int64?` | yes |  | The business key identifier of the manufacturing order node that requires this row. |
| `Weight` | `Decimal` | no |  | The weight of the row. |
| `LinkedStockOrderRowId` | `Int64?` | yes | [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow) | The business key identifier of the row's linked stock order row. |
| `LinkedSubcontractingManufacturingOrderOperation` | `Int64?` | yes | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) | The business key identifier of the row's linked subcontracting manufacturing order operation. |
| `OriginatingPurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) | The business key identifier of the row's originating purchase order delivery row. |
| `CausingTransType` | `Int32` | no |  | The causing transaction type of the row. |
| `CausingOrderRowId` | `Int64?` | yes |  | The business key identifier of the order row that was the cause of this row. References depends on CausingTransType |
| `RequirementDate` | `DateTimeOffset?` | yes |  | The requirement date of the row. |
| `PreviousOrderedQuantity` | `Decimal?` | yes |  | The previous ordered quantity of the row. |
| `PreviousDeliveryDate` | `DateTimeOffset?` | yes |  | The previous delivery date of the row. |
| `SubPartParentRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The business key identifier of the row's sub part parent row. |
| `QuantityRatio` | `Decimal?` | yes |  | The quantity ratio of the row. |
| `ParentOrderId` | `Int64` | no | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of the row's purchase order. |
| `RowIndex` | `Int32` | no |  | The row index of the row. |
| `SumRowId` | `Int64?` | yes | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The business key identifier of the row's sum row. |
| `PriceOrigin` | `Int32` | no |  | The row index of the row. |
| `DiscountIsLockedFromAutomaticChanges` | `Boolean` | no |  | Specifies if the row's discount is locked from automatic changes. |
| `IntrastatTransactionTypeId` | `Int64?` | yes | [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat) | The business key identifier of the row's intrastat transaction type. |
| `IntrastatTransactionType` | `TransactionTypeIntrastats` | no | [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat) | The intrastat transaction type of the row. |
| `TariffAndServiceCodeId` | `Int64?` | yes | [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode) | The business key identifier of the row's tariff and service code. |
| `TariffAndServiceCode` | `TariffAndServiceCodes` | no | [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode) | The tariff and service code of the row. |
| `PartConfigurationId` | `Int64?` | yes |  | The business key identifier of the row's part configuration. |
| `RowsGoodsLabel` | `String` | no |  | The goods label of the purchase order row. |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityPurchaseOrders](Purchase.md#Purchase.OrderQuantityPurchaseOrder) | The business key identifier of order quantity. |
| `OrderQuantity` | `OrderQuantityPurchaseOrders` | no | [OrderQuantityPurchaseOrders](Purchase.md#Purchase.OrderQuantityPurchaseOrder) | Order quantity that holds the partial quantities. |
| `SupplierDrawingNumber` | `String` | no |  | The supplier drawing number of the purchase order row. |
| `SupplierRevisionNumber` | `String` | no |  | The supplier revision number of the purchase order row. |
| `RowNotes` | `String` | no |  | The note of the purchase order row. |
| `BlanketOrderPurchaseRowId` | `Int64?` | yes | [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow) | The business key identifier of the row's blanket order purchase row. |
| `SupplierOrderNumber` | `String` | no |  | The supplier order number of the purchase order row. |
| `SupplierOrderRowPosition` | `String` | no |  | The supplier order row position of the purchase order row. |
| `SupplierPartNumber` | `String` | no |  | The supplier's part number of the purchase order row. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the purchase order. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the payment term of the purchase order. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The payment term of the purchase order. |
| `PaymentTermDescription` | `String` | no |  | The payment term description of the purchase order. |
| `GracePeriodInDays` | `Int32?` | yes |  | The purchase order's grace period in days. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the purchase order's delivery method. |
| `DeliveryMethod` | `DeliveryMethods` | no | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The purchase order's delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) | The business key identifier of the purchase order's delivery term. |
| `DeliveryTerm` | `DeliveryTerms` | no | [DeliveryTerms](Common.md#Common.DeliveryTerm) | The purchase order's delivery term. |
| `DeliveryTermDescription` | `String` | no |  | The delivery term description of the purchase order. |
| `DeliveryMethodDescription` | `String` | no |  | The delivery method description of the purchase order. |
| `ShipmentPayer` | `Int32` | no |  | Specifies who is responsible for the shipment payment for the purchase order. |
| `BusinessContactOrderNumber` | `String` | no |  | The supplier's order number for the purchase order. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of our reference for the purchase order. Reference Persons |
| `OurReference` | `Persons` | no | [Persons](Common.md#Common.Person) | Our reference for the purchase order. |
| `OurReferenceName` | `String` | no |  | The name of our reference for the purchase order. |
| `BusinessContactReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the supplier's reference for the purchase order. |
| `BusinessContactReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The supplier's reference for the purchase order. |
| `BusinessContactReferenceName` | `String` | no |  | The name of the supplier's reference for the purchase order. |
| `GoodsLabel` | `String` | no |  | The goods label of the purchase order. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency of the purchase order. |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The currency for the purchase order. |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) | The business key identifier of the VAT group that applies for the purchase order. |
| `VatGroup` | `VatGroups` | no | [VatGroups](Common.md#Common.VatGroup) | The VAT group that applies for the purchase order. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the purchase order belongs to. |
| `Warehouse` | `Warehouses` | no | [Warehouses](Common.md#Common.Warehouse) | The warehouse that the purchase order belongs to. |
| `Priority` | `Int32` | no |  | The priority of the purchase order. |
| `ProjectId` | `Int64?` | yes |  | The business key identifier of the purchase order's project. |
| `SendMethod` | `Int32` | no |  | Specifies the printout method for the purchase order. |
| `InvoicePrintoutMethod` | `Int32` | no |  | Specifies the printout method that should be used for invoices. |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the purchase order's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the purchase order. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the purchase order's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The external comment of the purchase order. |
| `TransportTime` | `Int32?` | yes |  | The transport time of the purchase order in workdays. |
| `LifeCycleState` | `Int32` | no |  | The life cycle state of the purchase order. |
| `Version` | `Int32` | no |  | The version of the purchase order. |
| `UseForwardRate` | `Boolean` | no |  | Specifies if forward rate should apply for the purchase order. |
| `ExchangeRate` | `Decimal` | no |  | Specifies the exchange rate to use for the purchase order. |
| `OrderAmount` | `Decimal` | no |  | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `OrderAmountInCompanyCurrency` | `Decimal` | no |  | This property is obsolete and no longer carries a value. _(Unavailable)_ |
| `AgentSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the agent that the purchase order belongs to. |
| `SuppliersQuoteNumber` | `String` | no |  | The readable supplier's quote number. |
| `IsStockOrder` | `Boolean` | no |  | Specifies if the purchase order is a Stock order. |
| `IsConfirmed` | `Boolean` | no |  | Specifies if the order is Confirmed. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the customer order. |
| `OrderNumber` | `String` | no |  | The human readable identifier of the purchase order. |
| `OrderDate` | `DateTimeOffset` | no |  | The order date of the purchase order. |
| `Rows` | `PurchaseOrderRows[]` | no | [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow) | The rows of the purchase order. |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer source of the active delivery address. |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier source of the active delivery address. |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  | The business key identifier of the company source of the active delivery address. |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  | Specifies the source of the purchase order delivery address. |
| `DeliveryAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the purchase order's delivery address. |
| `DeliveryAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The delivery address of the purchase order. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the purchase order's mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The mailing address of the purchase order. |
| `GoodsAddressNumber` | `String` | no |  | The goods address number of the purchase order. |
| `FromInquiryNumber` | `String` | no |  | The human readable identifier of the inquiry that resulted in the purchase order. |
| `Status` | `Int32` | no |  | The status of the purchase order. |
| `InquiryId` | `Int64?` | yes |  | The business key identifier of the purchase order's inquiry. |
| `PackingTermId` | `Int64?` | yes | [PackingTerms](Purchase.md#Purchase.PackingTerm) | The business key identifier of the purchase order's packing term. |
| `PackingTerm` | `PackingTerms` | no | [PackingTerms](Purchase.md#Purchase.PackingTerm) | The packing term of the purchase order. |
| `PackingTermDescription` | `String` | no |  | The packing term description of the purchase order. |
| `ShowPriceInFormReport` | `Boolean` | no |  | Specifies if the purchase order shows price in form report. |
| `ShowTotalInFormReport` | `Boolean` | no |  | Specifies if the purchase order shows total in form report. |
| `IsCredit` | `Boolean` | no |  | Specifies if the purchase order is a credit order. |
| `CausingCreditPurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of the purchase order which caused this credit purchase order to be created. |
| `BusinessContactId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the purchase order's supplier. |
| `InvoiceBusinessContactId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the purchase order's supplier sending the invoice. |
| `OrderTypeId` | `Int64` | no | [PurchaseOrderTypes](Purchase.md#Purchase.PurchaseOrderType) | The business key identifier of the purchase order's type. |
| `OrderType` | `PurchaseOrderTypes` | no | [PurchaseOrderTypes](Purchase.md#Purchase.PurchaseOrderType) | The order type of the purchase order. |
| `AccountGroupId` | `Int64` | no | [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup) | The business key identifier of the purchase order's account group. |
| `AccountGroup` | `SupplierAccountGroups` | no | [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup) | The account group of the purchase order. |
| `CategoryString` | `String` | no |  | The category string of the purchase order. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the purchase order's currency exchange type. |
| `DestinationForDeliveryTerm` | `String` | no |  | The destination for the delivery term. |
| `TransportDistance` | `Int32?` | yes |  | The transport distance of the purchase order in kilometres. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) | The communication addresses of the purchase order. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the type. |
| `Number` | `Int64` | no |  | The human readable identifier of the type. |
| `Prefix` | `String` | no |  | The prefix applied to purchase order numbers for this type. |
| `Description` | `String` | no |  | The translated description of the type. |
| `Priority` | `Int32` | no |  | The priority of the type. |
| `Visible` | `Boolean` | no |  | Specifies if the type is visible. |
| `IsPreset` | `Boolean` | no |  | Specifies if the type is a preset type. |
| `IncludeInPurchaseStatistics` | `Boolean` | no |  | Specifies if purchase orders of this type should be included in statistics. |
| `BaseType` | `Int32` | no |  | The base type of purchase orders created using this type. |
| `CodingGroupId` | `Int64` | no |  | The business key identifier of the type's coding group. |
| `RateTypeSetting` | `Int32` | no |  | The rate type setting of the purchase order type. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the purchase order type's currency exchange type. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the response time. |
| `Days` | `Int32?` | yes |  | The days of the response time. |
| `Description` | `String` | no |  | The description of the response time. |
| `Number` | `Int64` | no |  | The human readable identifier of the response time. |
| `IsDefault` | `Boolean` | no |  | Specifies if the response time is default. |

**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.SupplierAccountGroup"></a>
### SupplierAccountGroups

Represents a supplier account group.

- **Endpoint:** `GET /api/v1/Purchase/SupplierAccountGroups`
- **Required permission:** Show chart of accounts
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the group. |
| `IsDefault` | `Boolean` | no |  | Specifies if the group is the default group. |
| `Number` | `Int64` | no |  | The human readable identifier of the group. |
| `Description` | `String` | no |  | The translated description of the group. |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |

**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.SupplierAccount"></a>
### SupplierAccounts

Represents a supplier account.

- **Endpoint:** `GET /api/v1/Purchase/SupplierAccounts`
- **Required permission:** Show supplier
- **Introduced in:** 22.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the supplier account. |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the accounts supplier. |
| `StandardAccountId` | `Int64?` | yes | [StandardAccounts](Accounting.md#Accounting.StandardAccount) | The business key identifier of the standard account for the account. |
| `StandardAccount` | `StandardAccounts` | no | [StandardAccounts](Accounting.md#Accounting.StandardAccount) | The standard account for the account. |
| `CodingEntryId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry for the account. |

**References out:** [CodingEntries](Accounting.md#Accounting.CodingEntry), [StandardAccounts](Accounting.md#Accounting.StandardAccount), [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.SupplierDistrict"></a>
### SupplierDistricts

Represents a supplier district.

- **Endpoint:** `GET /api/v1/Purchase/SupplierDistricts`
- **Required permission:** Show supplier
- **Introduced in:** 2.28

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the supplier district. |
| `Code` | `Int64` | no |  | The human readable identifier of the supplier district. |
| `Description` | `String` | no |  | The description of the supplier district. |

**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.SupplierPartLink"></a>
### SupplierPartLinks

Represents a supplier part link.

- **Endpoint:** `GET /api/v1/Purchase/SupplierPartLinks`
- **Required permission:** Show supplier
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the supplier part link. |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier part link supplier. |
| `SupplierPartNumber` | `String` | no |  | The supplier part link part number. |
| `PurchaseCommentShowInForms` | `Int32` | no |  | Specifies on which forms the purchase comment should be shown. |
| `IncludeAlloyCostOnPurchaseOrder` | `Boolean` | no |  | Include alloy cost on purchase orders for this supplier part link. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the supplier part link part. |
| `Price` | `Decimal?` | yes |  | The price of the supplier link part. |
| `SetupPrice` | `Decimal?` | yes |  | The setup price of the supplier link part. |
| `LeadTime` | `TimeSpan?` | yes |  | The lead time of the supplier part link in work days. |
| `Discount` | `Decimal?` | yes |  | The discount of the supplier part link. |
| `PriceValidThrough` | `DateTimeOffset?` | yes |  | The valid through date of the supplier part link price. |
| `FuturePrice` | `Decimal?` | yes |  | The future price of the supplier part link. |
| `FuturePriceValidThrough` | `DateTimeOffset?` | yes |  | The valid through date of the supplier part link future price. |
| `FutureSetupPrice` | `Decimal?` | yes |  | The future setup price of the supplier part link. |
| `QuantityPerPackage` | `Decimal?` | yes |  | The quantity per package of the supplier part link. |
| `OverridePurchaseCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the supplier part link override purchase comment. |
| `OverridePurchaseComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The supplier part link override purchase comment. |
| `UnitId` | `Int64` | no | [Units](Common.md#Common.Unit) | The business key identifier of the supplier part link unit. |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The supplier part link unit. |
| `PriceCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the supplier part link price currency. |
| `PriceCurrency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The supplier part link price currency. |
| `PriceCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the supplier part link price comment. |
| `PriceComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The supplier part link price comment. |
| `Brand` | `String` | no |  | The brand of the supplier part link. |
| `Storage` | `String` | no |  | The storage of the supplier part link. |
| `Dock` | `String` | no |  | The dock of the supplier part link. |
| `IsRemoteConfigured` | `Boolean` | no |  | Specifies if the part is remote configured via the transfer profile connected to the supplier. |
| `PartPurchaseExpenseValuesId` | `Int64?` | yes | [PartPurchaseExpenseValues](Inventory.md#Inventory.PartPurchaseExpenseValues) | The business key identitier of the supplier part link purchase expense values. |
| `PartPurchaseExpenseValues` | `PartPurchaseExpenseValues` | no | [PartPurchaseExpenseValues](Inventory.md#Inventory.PartPurchaseExpenseValues) | The supplier part link purchase expense values. |

- `PurchaseCommentShowInForms` (bitmask) — Internal=0, Inquiry=1, Order=2, DeliverySchedule=4

**References out:** [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [PartPurchaseExpenseValues](Inventory.md#Inventory.PartPurchaseExpenseValues), [Parts](Inventory.md#Inventory.Part), [Suppliers](Purchase.md#Purchase.Supplier), [Units](Common.md#Common.Unit)
**Referenced by:** [PartPlanningInformation](Inventory.md#Inventory.PartPlanningInformation), [Parts](Inventory.md#Inventory.Part), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.Supplier"></a>
### Suppliers

Represents a supplier.

- **Endpoint:** `GET /api/v1/Purchase/Suppliers`
- **Required permission:** Show supplier
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the supplier. |
| `SupplierCode` | `String` | no |  | The human readable code of the supplier. |
| `Name` | `String` | no |  | The name of the supplier. |
| `AlternativeName` | `String` | no |  | The alternative name of the supplier. |
| `MailingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the supplier mailing address. |
| `MailingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The mailing address of then supplier. |
| `CorporationIdentificationNumber` | `String` | no |  | The corporation identification number of the supplier. |
| `VatNumber` | `String` | no |  | The VAT number of the supplier. |
| `ServiceTaxNumber` | `String` | no |  | The service tax number of the supplier. |
| `PersonalNumber` | `String` | no |  | The name of private person if is private supplier enabled. |
| `PackingTermId` | `Int64?` | yes | [PackingTerms](Purchase.md#Purchase.PackingTerm) | The business key identifier of the supplier packing term. |
| `PackingTerm` | `PackingTerms` | no | [PackingTerms](Purchase.md#Purchase.PackingTerm) | The packing term of the supplier. |
| `GracePeriodOrderConfirmation` | `Int32?` | yes |  | The grace period order confirmation of the supplier. |
| `GracePeriodDelivery` | `Int32?` | yes |  | The grace period delivery of the supplier. |
| `InvoiceSupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier invoice supplier. |
| `AuthorizedSignerPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the supplier authorized signer person. |
| `AuthorizedSignerPerson` | `Persons` | no | [Persons](Common.md#Common.Person) | The authorized signer person of the supplier. |
| `BankIdNumber` | `String` | no |  | The bank id number of the supplier. |
| `CentralBankCode` | `String` | no |  | The central bank code of the supplier. |
| `ResponseTimeId` | `Int64?` | yes | [ResponseTimes](Purchase.md#Purchase.ResponseTime) | The business key identifier of the supplier response time. |
| `ResponseTime` | `ResponseTimes` | no | [ResponseTimes](Purchase.md#Purchase.ResponseTime) | The response time of the supplier. |
| `InvoiceBasisException` | `Boolean` | no |  | The invoice basis exception of the supplier. |
| `Role` | `Int32` | no |  | The role of the supplier. |
| `AttachDatafileWithOrder` | `Boolean` | no |  | Specifies if the supplier have attached datafile with order. |
| `AttachDatafileWithDeliverySchedule` | `Boolean` | no |  | Specifies if the supplier have attached datafile with delivery schedule. |
| `AttachDatafileWithCase` | `Boolean` | no |  | Specifies if the supplier have attached datafile with case. |
| `ReceivingInspectionType` | `Int32` | no |  | The receiving inspection type of the supplier. |
| `ArrivalReportingInstructionId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the supplier arrival reporting instruction. |
| `ArrivalReportingInstruction` | `Comments` | no | [Comments](Common.md#Common.Comment) | The arrival reporting instruction of the supplier. |
| `UseOCRNumber` | `Boolean` | no |  | Specifies if the supplier use OCR number. |
| `UseReferenceNumber` | `Boolean` | no |  | Specifies if the supplier use reference number. |
| `FixedReferenceNumber` | `String` | no |  | The fixed reference number of the supplier. |
| `EInvoiceId` | `String` | no |  | The e-invoice id of the supplier. |
| `PurchaseManagerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the supplier purchase manager. |
| `PurchaseManager` | `Persons` | no | [Persons](Common.md#Common.Person) | The purchase manager of the supplier. |
| `ShippingAgentCode` | `String` | no |  | The shipping agent code of the supplier. |
| `DefaultBusinessContactBankAccountId` | `Int64?` | yes | [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount) | The business key identifier of the supplier default business contact bank account. |
| `DefaultBusinessContactBankAccount` | `BusinessContactBankAccounts` | no | [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount) | The default business contact bank account of the supplier. |
| `IsCasualSupplier` | `Boolean` | no |  | Specifies if the supplier is a casual supplier. |
| `ShippingAgentType` | `Int32?` | yes |  | The shipping agent type of the supplier. |
| `BookTransport` | `Boolean` | no |  | The book transport of the supplier. |
| `ReturnLabel` | `Boolean` | no |  | The return label of the supplier. |
| `ShipmentPrintSetting` | `Int32` | no |  | The shipment print setting of the supplier. |
| `Url` | `String` | no |  | The URL of the supplier. |
| `Discount` | `Decimal?` | yes |  | The discount of the supplier. |
| `StatusId` | `Int64` | no | [SupplierStatuses](Purchase.md#Purchase.SupplierStatus) | The business key identifier of the supplier status. |
| `Status` | `SupplierStatuses` | no | [SupplierStatuses](Purchase.md#Purchase.SupplierStatus) | The status of the supplier. |
| `TypeId` | `Int64?` | yes | [SupplierTypes](Purchase.md#Purchase.SupplierType) | The business key identifier of the supplier type. |
| `Type` | `SupplierTypes` | no | [SupplierTypes](Purchase.md#Purchase.SupplierType) | The type of the supplier. |
| `DistrictId` | `Int64?` | yes | [SupplierDistricts](Purchase.md#Purchase.SupplierDistrict) | The business key identifier of the supplier district. |
| `District` | `SupplierDistricts` | no | [SupplierDistricts](Purchase.md#Purchase.SupplierDistrict) | The district of the supplier. |
| `PayViaId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier that the current supplier payments should go through. |
| `DateForTransitionToActualContact` | `DateTimeOffset?` | yes |  | The date for transition to actual contact of the supplier. Changed from DateTimeOffset to DateTimeOffset? in 26.3 |
| `PaymentTermId` | `Int64` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the supplier payment term |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The payment term of the supplier. |
| `BankGiroNo` | `String` | no |  | The bank giro no of the supplier. |
| `EdiCode` | `String` | no |  | The EDI code of the supplier. _(Replaced by OtherSupplierNumbers)_ |
| `DefaultOrderPrintoutVia` | `Int32` | no |  | The default order printout via of the supplier. |
| `PlusGiroNo` | `String` | no |  | The plus giro number of the supplier. |
| `OurCodeByYou` | `String` | no |  | The human readable identifier that the the supplier uses to identify the current company. |
| `DiscountCategoryId` | `Int64?` | yes | [DiscountCategories](Common.md#Common.DiscountCategory) | The business key identifier of the supplier discount category. |
| `DiscountCategory` | `DiscountCategories` | no | [DiscountCategories](Common.md#Common.DiscountCategory) | The discount category of the supplier. |
| `ToleranceForEarlyDelivery` | `Int64?` | yes |  | The tolerance value for early delivery by the supplier. |
| `ToleranceForLateDelivery` | `Int64?` | yes |  | The tolerance value for late delivery by the supplier. |
| `Alias` | `String` | no |  | The alias of the supplier. |
| `BlockedContextType` | `Int32` | no |  | The blocked context type of the supplier. |
| `IsInternal` | `Boolean` | no |  | Specifies if the supplier is internal. |
| `CompanyId` | `Int64` | no |  | The business key identifier of the company that the supplier data is active for. |
| `BlockedStatus` | `Int32` | no |  | The block status of the entity. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  | The date when the entity stops being blocked. |
| `Priority` | `Int32` | no |  | The priority of the supplier. |
| `CategoryString` | `String` | no |  | The category string of the supplier. |
| `DeliveryInstruction` | `String` | no |  | The delivery instruction of the supplier. |
| `PaymentMethodId` | `Int64` | no | [PaymentMethods](Common.md#Common.PaymentMethod) | The business key identifier of the supplier payment method. |
| `LastChange` | `DateTimeOffset?` | yes |  | Last change on Supplier från EntityChangeLog |
| `PaymentMethod` | `PaymentMethods` | no | [PaymentMethods](Common.md#Common.PaymentMethod) | The payment method of the supplier. |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The business key identifier of the supplier language. |
| `Language` | `LanguageCodes` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The language of the supplier. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the supplier comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The supplier comment. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the supplier currency. References Currencies . |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The currency of the supplier. |
| `VisitingAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the supplier visiting address. |
| `VisitingAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The visiting address of the supplier. |
| `BlockMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) | The block message of the supplier. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that blocked the entity. |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The application user that blocked the supplier. |
| `DefaultReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the default reference of the supplier. |
| `DefaultReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The default reference of the supplier. |
| `DeliveryAddressId` | `Int64` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The business key identifier of the supplier delivery address. |
| `DeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The delivery address of the supplier. |
| `SupplierPartLinks` | `SupplierPartLinks[]` | no | [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink) | A collection of supplier part links that belong to the supplier. |
| `CaseEntries` | `CaseEntry[]` | no | [CaseEntry](Inventory.md#Inventory.CaseEntry) | A collection of case entries that belong to the supplier. |
| `OtherSupplierNumbers` | `OtherSupplierNumbers[]` | no | [OtherSupplierNumbers](Purchase.md#Purchase.OtherSupplierNumber) | Available other supplier numbers. Mainly used as EDI identifiers. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](Common.md#Common.CommunicationAddress) | The communication addresses for the supplier. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) | A collection of extra field values for the supplier. |
| `PurchaseAccountId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry with supplier purchase account. |
| `PurchaseAccount` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The coding entry with supplier purchase account. |
| `AccrualAccountingReverseAccountId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry with supplier offset account for accruals. |
| `AccrualAccountingReverseAccount` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The coding entry with supplier offset account for accruals. |
| `OutgoingPaymentsAccountId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry with supplier account for outgoing payments. |
| `OutgoingPaymentsAccount` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The coding entry with supplier account for outgoing payments. |
| `SupplierAccounts` | `SupplierAccounts[]` | no | [SupplierAccounts](Purchase.md#Purchase.SupplierAccount) | The supplier account exceptions. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the supplier's currency exchange type. |
| `RootId` | `Int64` | no |  | The business key identifier of the supplier root id. |
| `References` | `BusinessContactReferences[]` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business contact references belonging to the supplier. |
| `ReceivingInspecionFromDate` | `DateTimeOffset?` | yes |  | The receiving inspection from date for supplier. |
| `ReceivingInspecionEndDate` | `DateTimeOffset?` | yes |  | The receiving inspection end date for supplier. |
| `SupplierAccountGroupId` | `Int64` | no | [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup) | The business key identifier of the supplier account group for supplier. _(Refer to DeliveryAddress)_ |
| `IsPrivateSupplier` | `Boolean` | no |  | The private person setting of supplier. |
| `EORINumber` | `String` | no |  | The eori of supplier. mainly used for validation to retrieve business address. |
| `DeliveryAddresses` | `DeliveryAddresses[]` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | All available delivery addresses of the supplier. |
| `AllBusinessContactBankAccountOfSupplier` | `BusinessContactBankAccounts[]` | no | [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount) | All available supplier's business contact bank accounts. |
| `TinNumber` | `String` | no |  | The supplier’s income tax reference number |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the supplier status. |
| `Code` | `Int64` | no |  | The human readable identifier of the supplier status. |
| `Description` | `String` | no |  | The description of the supplier status. |

**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Purchase.SupplierType"></a>
### SupplierTypes

Represents a supplier type.

- **Endpoint:** `GET /api/v1/Purchase/SupplierTypes`
- **Required permission:** Show supplier
- **Introduced in:** 2.28

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the supplier type. |
| `Code` | `Int64` | no |  | The human readable identifier of the supplier type. |
| `Description` | `String` | no |  | The description of the supplier type. |

**Referenced by:** [Suppliers](Purchase.md#Purchase.Supplier)


## Depends on other modules

- [Accounting](Accounting.md): [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [Codings](Accounting.md#Accounting.Coding), [CodingEntries](Accounting.md#Accounting.CodingEntry), [StandardAccounts](Accounting.md#Accounting.StandardAccount)
- [Common](Common.md): [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BlobData](Common.md#Common.BlobData), [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [CommunicationAddresses](Common.md#Common.CommunicationAddress), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [DiscountCategories](Common.md#Common.DiscountCategory), [ExtraFields](Common.md#Common.ExtraField), [LanguageCodes](Common.md#Common.LanguageCode), [PartialQuantities](Common.md#Common.PartialQuantity), [PaymentMethods](Common.md#Common.PaymentMethod), [PaymentTerms](Common.md#Common.PaymentTerm), [Persons](Common.md#Common.Person), [PriceLists](Common.md#Common.PriceList), [Projects](Common.md#Common.Project), [ReasonCodes](Common.md#Common.ReasonCode), [Revisions](Common.md#Common.Revision), [StatisticalGoodsCodes](Common.md#Common.StatisticalGoodsCode), [TariffAndServiceCodes](Common.md#Common.TariffAndServiceCode), [TransactionTypeIntrastats](Common.md#Common.TransactionTypeIntrastat), [Units](Common.md#Common.Unit), [VatGroups](Common.md#Common.VatGroup), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse)
- [Inventory](Inventory.md): [CaseEntry](Inventory.md#Inventory.CaseEntry), [Parts](Inventory.md#Inventory.Part), [PartPurchaseExpenseValues](Inventory.md#Inventory.PartPurchaseExpenseValues), [QuantityChanges](Inventory.md#Inventory.QuantityChange)
- [Manufacturing](Manufacturing.md): [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation)
- [Sales](Sales.md): [Customers](Sales.md#Sales.Customer), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow)
