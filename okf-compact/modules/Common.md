# Common

Monitor API module `Common`: 110 queryable entities, 0 commands, 3 payload types.

## Queryable entities

<a id="Common.Address"></a>
### Addresses

Represents a queryable address.

- **Endpoint:** `GET /api/v1/Common/Addresses`
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Addressee` | `String` | no |  |
| `Field1` | `String` | no |  |
| `Field2` | `String` | no |  |
| `Field3` | `String` | no |  |
| `Field4` | `String` | no |  |
| `Field5` | `String` | no |  |
| `Locality` | `String` | no |  |
| `Region` | `String` | no |  |
| `PostalCode` | `String` | no |  |
| `AddressFormatType` | `Int32` | no |  |
| `CountryId` | `Int64` | no | [Countries](/modules/Common.md#Common.Country) |
| `LanguageId` | `Int64` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `FormReportTranslationGroupId` | `Int64` | no |  |
| `PostalCodeId` | `Int64?` | yes |  |

- `AddressFormatType` — Generic=0, PostalCodeCity=1, CityStatePostalCode=2, CityPostalCodeTwoRows=3, CityProvinsPostalCode=4

**References out:** [Countries](/modules/Common.md#Common.Country), [LanguageCodes](/modules/Common.md#Common.LanguageCode)
**Referenced by:** [BankAccounts](/modules/Accounting.md#Accounting.BankAccount), [BlanketOrderPurchases](/modules/Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderSales](/modules/Sales.md#Sales.BlanketOrderSales), [BusinessContactBankAccounts](/modules/Common.md#Common.BusinessContactBankAccount), [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [Customers](/modules/Sales.md#Sales.Customer), [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [Persons](/modules/Common.md#Common.Person), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [Quotes](/modules/Sales.md#Sales.Quote), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement), [Shipments](/modules/Sales.md#Sales.Shipment), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Common.ApplicationUserPrinter"></a>
### ApplicationUserPrinters

Represents a printer that has been assigned to an application user.

- **Endpoint:** `GET /api/v1/Common/ApplicationUserPrinters`
- **Required permission:** Show user
- **Introduced in:** 2.52

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ApplicationUserId` | `Int64` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `PrinterName` | `String` | no |  |
| `NormalizedFormReportType` | `Int32?` | yes |  |
| `FormReportType` | `Guid?` | yes |  |
| `ServerPrinterId` | `Int64?` | yes | [ServerPrinters](/modules/Common.md#Common.ServerPrinter) |
| `FormDocumentType` | `Int32` | no |  |

- `NormalizedFormReportType` — NotInitialized=0, Quote=1, Acknowledgement=3, CustomerDeliveryNote=5, CustomerDeliveryNoteDelivered=6, Invoice=7, CustomerDeliveryNoteCollectionDelivered=8, SalesTransportLabelA4=16, ComprehensiveInvoice=17, PurchaseOrder=22, PurchaseOrderConfirmationReminder=23, PurchaseOrderConfirmationReminderCasualSupplier=24, PurchaseOrderDeliveryConfirmationReminder=25, PurchaseOrderDeliveryConfirmationReminderCasualSupplier=26, PurchaseTransportLabel=31, PickingList=100, InspectionReport=101, PurchaseTransportLabelForRejection=102, ProformaInvoice=103, ComprehensiveProformaInvoice=104, ManufacturingTransportLabelA4=105, ManufacturingTransportLabelA4ForRejection=106, ManufacturingTransportLabelA4InProgress=107, ManufacturingTransportLabelA4BeforeReporting=108, ManufacturingOrderOperation=109, ManufacturingOrderMaterial=110, ManufacturingOrderTraveler=111, PreCalculationSummary=112, SubcontractPurchaseOrder=113, SubcontractDeliveryNote=114, SubcontractTransportLabelA4=117, SubcontractTransportLabelA5=118, SubcontractTransportLabelSmall=119, LevelListWhereUsedList=120, LevelListConsistsOfList=122, PostCalculationSummary=123, PhysicalInventoryList=124, MaterialClearanceShortageList=125, AccountingOrder=126, GeneralLedgerDrilldown=127, JournalDrilldown=128, ManufacturingPickingList=129, ManufacturingPickingListGroupByOrder=130, ManufacturingPickingListGroupByMaterial=131, AccountingReportHeader=132, InternalInvoice=133, CashReceipt=134, AccountsReceivableLedger=135, AccountsReceivableLedgerReprint=136, IncomingPaymentLedger=137, IncomingPaymentLedgerReprint=138, AccountsPayableLedger=139, AccountsPayableLedgerReprint=140, PreliminaryAccountsPayableLedger=141, PreliminaryAccountsPayableLedgerReprint=142, CancelledAccountsPayableLedger=143, CancelledAccountsPayableLedgerReprint=144, CancelledPreliminaryAccountsPayableLedger=145, CancelledPreliminaryAccountsPayableLedgerReprint=146, PaymentReminder=147, PaymentReminderReprint=148, AccrualAccountingLedger=149, AccrualAccountingLedgerReprint=150, VatReport=151, VatReportAccounts=152, VatReportGeneralLedger=153, VatReportTransactions=154, VatReportCheck=155, VatReportDifferenceSearch=156, TransactionList=157, OutgoingPaymentLedger=158, OutgoingPaymentLedgerReprint=159, SalesTransportLabelA5=160, CustomerCaseConfirmation=161, AccountStatement=162, CustomerCaseAnswer=163, CustomerNonconformityReport=164, SupplierNonconformityReport=165, InternalNonconformityReport=166, SupplierClaimReport=167, CancelledAccountsReceivableLedger=168, CancelledAccountsReceivableLedgerReprint=169, ShipmentWayBill=170, ShipmentParcel=171, Inquiry=172, CustomerOrderPickingList=173, EimInvoiceInformation=174, InterestInvoice=175, FileLink=176, RecordingsAndSalaryTypeSummary=177, ProductRecordConsistsOf=178, ProductRecordIncludedIn=179, InternalProjectReport=180, ExternalProjectReport=181, TraceabilityProtocol=182, FixedAssetLedger=183, FixedAssetLedgerReprint=184, CustomReport=185, StockAcknowledgement=186, StockDeliveryNote=187, StockPurchaseOrder=188, StockDeliveryNoteDelivered=189, PurchaseOrderModified=190, TaxDepreciation=191, TaxDepreciationDrilldown=192, PartTransportLabelSmall=193, PartTransportLabelA5=194, PartTransportLabelA4=195, UnplannedStockBalanceChangeLedger=196, UnplannedStockBalanceChangeLedgerReprint=197, PIADetailed=198, StockTransactionLogLedger=199, ManufacturingOrderLogLedger=200, InvoiceLogLedger=201, PriceChangeLogLedger=202, CalculationDifferenceLedger=203, AccountStatementBalancePerCustomer=204, StockTransactionLogLedgerReprint=205, ManufacturingOrderLogLedgerReprint=206, PriceChangeLogLedgerReprint=207, CalculationDifferenceLedgerReprint=208, InvoiceLogLedgerReprint=209, PrintoutDemoCertificate=210, BlanketOrderPurchase=211, ArrivalNote=212, CorrectionInvoice=213, ModifiedOrderConfirmation=214, PurchaseDeliverySchedule=215, PackageList=216, PackageTransportLabel=217, AnnualVolumeList=218, BlanketOrderSales=219, TransportLabelDirectWithdrawalA4=220, TransportLabelDirectWithdrawalA5=221, TransportLabelDirectWithdrawalSmall=222, TransportLabelDirectArrivalA4=223, TransportLabelDirectArrivalA5=224, TransportLabelDirectArrivalSmall=225, TransportLabelMoveBetweenLocationsA4=226, TransportLabelMoveBetweenLocationsA5=227, TransportLabelMoveBetweenLocationsSmall=228, TransportLabelMoveBetweenWarehousesA4=229, TransportLabelMoveBetweenWarehousesA5=230, TransportLabelMoveBetweenWarehousesSmall=231, Standard8DNonconformityReport=232, PaymentLedger=233, PaymentLedgerReprint=234, PaymentVoucher=235, DebtorStatement=236, CreditorStatement=237, PrintVoucher=238, OfficialReceipt=239, PolishCashReceipt=240, PolishCashReport=241, Standard8DCustomerNonconformityReport=242, AutoCodingLedger=243, AutoCodingLedgerReprint=244, MeasuringProtocolManufacturing=245, MeasuringProtocolPurchase=246, VoucherList=247, RevenueCalculationLedger=248, RevenueCalculationLedgerReprint=249, GeneralActivityList=250, ReturnPurchaseOrderDeliveryNote=251, ReturnPurchaseOrderProforma=252, ReturnPurchaseOrderTransportLabelA4=253, ReturnPurchaseOrderTransportLabelA5=254, ReturnPurchaseOrderTransportLabelSmall=255, Waybill=256, ShipmentAdvice=257, PartTransportMultiLabel=258, StockTransportMultiLabel=259, SustainabilityCalculationDetailed=260, ShipmentReceipt=261, OrderRowDiscounts=262, BankAccountReconciliation=263, CollectiveCorrectionInvoice=264, ExternalCustomerNonconformityReport=265, ExternalSupplierNonconformityReport=266, ExternalInternalNonconformityReport=267, PartContentDeliveryReport=268, ProjectMaterialCalculationLedger=269, ProjectMaterialCalculationLedgerReprint=270, CausesForShortage=271, CustomerLevelListConsistsOfList=272, CustomerLevelListIncludedInList=273, SupplierLevelListConsistsOfList=274, SupplierLevelListIncludedInList=275, GPBForm=276, CurrencyWarehouse=277, ReturnPurchaseOrderPickingList=278, SubcontractProformaInvoice=279, LocationLabel=280, LocationMultiLabel=281, FilesExternal1=282, FilesExternal2=283, FilesExternal3=284, RemittanceAdvice=285, SupplierAgreement=286, ModifiedSupplierAgreement=287, SelfBilledInvoice=288, PurchaseTransportLabelA5=310, RefillPickingLocationStandard=500, PurchaseTransportLabelA5ForRejection=1020, ManufacturingTransportLabelA5=1050, ManufacturingTransportLabelA5ForRejection=1060, ManufacturingTransportLabelA5InProgress=1070, ManufacturingTransportLabelA5BeforeReporting=1080, SalesTransportLabelSmall=1600, Form=2401, ServiceReporting=2402, SalesAgreement=2501, ModifiedSalesAgreement=2502, AccountStatementPurchase=2503, ReturnPurchaseOrder=2504, PurchaseTransportLabelSmall=3100, PurchaseTransportLabelSmallForRejection=10200, ManufacturingTransportLabelSmall=10500, ManufacturingTransportLabelSmallForRejection=10600, ManufacturingTransportLabelSmallInProgress=10700, ManufacturingTransportLabelSmallBeforeReporting=10800, DebitNote=10801, ServiceTax=10802, EdiCustomerOrderConfirmation=20001, EdiCustomerOrderInvoice=20002, EdiCustomerOrderSimpleDispatchAdvice=20003, EdiCustomerOrderResponse=20004, EdiPurchaseOrder=20005, EdiCustomerOrderComplexDispatchAdvice=20006, EdiPurchaseDeliverySchedule=20007
- `FormDocumentType` — Document=0, AdaptedReport=1

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [ServerPrinters](/modules/Common.md#Common.ServerPrinter)
**Referenced by:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser)

<a id="Common.ApplicationUser"></a>
### ApplicationUsers

Represents a queryable MONITOR application user.

- **Endpoint:** `GET /api/v1/Common/ApplicationUsers`
- **Required permission:** Show user
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Username` | `String` | no |  |
| `Description` | `String` | no |  |
| `WindowsUserAccountName` | `String` | no |  |
| `IsInvisible` | `Boolean` | no |  |
| `DefaultRole` | `Int64` | no |  |
| `DefaultGroup` | `Int64?` | yes |  |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `LanguageId` | `Int64` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `MailAddress` | `String` | no |  |
| `MailMethod` | `Int32?` | yes |  |
| `Printers` | `ApplicationUserPrinters[]` | no | [ApplicationUserPrinters](/modules/Common.md#Common.ApplicationUserPrinter) |
| `DefaultPrinter` | `String` | no |  |
| `External1Printer` | `String` | no |  |
| `External2Printer` | `String` | no |  |
| `External3Printer` | `String` | no |  |
| `PrintoutFormatForParcel` | `Int32` | no |  |
| `WarehousePermissions` | `WarehousePermissions[]` | no | [WarehousePermissions](/modules/Common.md#Common.WarehousePermission) |
| `DefaultVoucherSeriesId` | `Int64?` | yes | [VoucherSeries](/modules/Accounting.md#Accounting.VoucherSeries) |
| `UserAuthenticationMethod` | `Int32` | no |  |
| `Culture` | `String` | no |  |

- `MailMethod` — ClientBasedOutlook=0, ServerBasedExchange=2, ServerBasedSmtp=3, ServerBasedExchangeOnline=4
- `PrintoutFormatForParcel` — PDF=0, ZPL=1, LaserSte=2, ThermoSe=3, LaserA5=4, Laser2A5=5, Thermo190=6, ThermoBrev3=7, Thermo165=8
- `UserAuthenticationMethod` — Password=0, WindowsIntegrated=1, Oidc=4

**References out:** [ApplicationUserPrinters](/modules/Common.md#Common.ApplicationUserPrinter), [LanguageCodes](/modules/Common.md#Common.LanguageCode), [VoucherSeries](/modules/Accounting.md#Accounting.VoucherSeries), [WarehousePermissions](/modules/Common.md#Common.WarehousePermission), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [ApplicationUserPrinters](/modules/Common.md#Common.ApplicationUserPrinter), [BusinessContactNoteHistories](/modules/Common.md#Common.BusinessContactNoteHistory), [BusinessOpportunityActivities](/modules/Sales.md#Sales.BusinessOpportunityActivity), [BusinessOpportunityActivityTemplateRows](/modules/Sales.md#Sales.BusinessOpportunityActivityTemplateRow), [BusinessOpportunitySalesProcessSteps](/modules/Sales.md#Sales.BusinessOpportunitySalesProcessStep), [CaseEntryActivities](/modules/Inventory.md#Inventory.CaseEntryActivity), [CaseEntryPhases](/modules/Inventory.md#Inventory.CaseEntryPhase), [CaseManagementTemplateNodes](/modules/Inventory.md#Inventory.CaseManagementTemplateNode), [CustomerOrderActivities](/modules/Sales.md#Sales.CustomerOrderActivity), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [CustomerRelationshipManagementActivities](/modules/Sales.md#Sales.CustomerRelationshipManagementActivity), [Customers](/modules/Sales.md#Sales.Customer), [DelegatedWork](/modules/Common.md#Common.DelegatedWork), [IncomingPayments](/modules/Accounting.md#Accounting.IncomingPayment), [InvoiceLogs](/modules/Sales.md#Sales.InvoiceLog), [Locations](/modules/Inventory.md#Inventory.Location), [ManufacturingPickingLists](/modules/Manufacturing.md#Manufacturing.ManufacturingPickingList), [MonitoringTaskRecipients](/modules/Common.md#Common.MonitoringTaskRecipient), [MonitoringTasks](/modules/Common.md#Common.MonitoringTask), [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment), [PartActivities](/modules/Inventory.md#Inventory.PartActivity), [PartConfigurationPresets](/modules/Common.md#Common.PartConfigurationPreset), [Parts](/modules/Inventory.md#Inventory.Part), [Persons](/modules/Common.md#Common.Person), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [ProjectActivities](/modules/Common.md#Common.ProjectActivity), [ProjectActivityTypes](/modules/Common.md#Common.ProjectActivityType), [ProjectPhases](/modules/Common.md#Common.ProjectPhase), [ProjectPhaseTypes](/modules/Common.md#Common.ProjectPhaseType), [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange), [QuoteActivities](/modules/Sales.md#Sales.QuoteActivity), [SalesPickingLists](/modules/Sales.md#Sales.SalesPickingList), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Common.AutoCompleteConfiguration"></a>
### AutoCompleteConfigurations

Represents an auto-complete configuration.

- **Endpoint:** `GET /api/v1/Common/AutoCompleteConfigurations`
- **Introduced in:** 2.46

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `IsPreset` | `Boolean` | no |  |
| `PopupTypeId` | `Guid` | no |  |


<a id="Common.BlobData"></a>
### BlobData

A container for blob data.

- **Endpoint:** `GET /api/v1/Common/BlobData`
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `MediaType` | `Int32` | no |  |
| `MediaSubType` | `String` | no |  |
| `Value` | `String` | no |  |

- `MediaType` — Text=0, Image=1, Audio=2, Video=3, Application=4, Multipart=5, Message=6

**Referenced by:** [Companies](/modules/Common.md#Common.Company), [EimDocuments](/modules/Purchase.md#Purchase.EimDocument), [PartImages](/modules/Inventory.md#Inventory.PartImage), [Persons](/modules/Common.md#Common.Person)

<a id="Common.BusinessContactBankAccount"></a>
### BusinessContactBankAccounts

Represents a business contact bank account.

- **Endpoint:** `GET /api/v1/Common/BusinessContactBankAccounts`
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ClearingNumber` | `String` | no |  |
| `ClearingSystem` | `String` | no |  |
| `CountryId` | `Int64` | no | [Countries](/modules/Common.md#Common.Country) |
| `Country` | `Countries` | no | [Countries](/modules/Common.md#Common.Country) |
| `CentralBankCodeId` | `Int64?` | yes | [CentralBankCodes](/modules/Common.md#Common.CentralBankCode) |
| `CentralBankCode` | `CentralBankCodes` | no | [CentralBankCodes](/modules/Common.md#Common.CentralBankCode) |
| `CurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `Currency` | `Currencies` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `Type` | `Int32` | no |  |
| `Number` | `String` | no |  |
| `BankIdentifierCode` | `String` | no |  |
| `BankAddressId` | `Int64?` | yes | [Addresses](/modules/Common.md#Common.Address) |
| `BankAddress` | `Addresses` | no | [Addresses](/modules/Common.md#Common.Address) |

- `Type` — Iban=1, Bban=2, Upic=3, Miscellaneous=4

**References out:** [Addresses](/modules/Common.md#Common.Address), [CentralBankCodes](/modules/Common.md#Common.CentralBankCode), [Countries](/modules/Common.md#Common.Country), [Currencies](/modules/Common.md#Common.Currency)
**Referenced by:** [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Common.BusinessContactNoteHistory"></a>
### BusinessContactNoteHistories

Represents a business contact note history entry.

- **Endpoint:** `GET /api/v1/Common/BusinessContactNoteHistories`
- **Introduced in:** 2.55

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Subject` | `String` | no |  |
| `BodyId` | `Int64?` | yes |  |
| `Body` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CreatedByUserId` | `Int64` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `CreatedTimestamp` | `DateTimeOffset` | no |  |
| `ParentId` | `Int64` | no |  |
| `ParentClass` | `Guid` | no |  |

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Comments](/modules/Common.md#Common.Comment)
**Referenced by:** [BusinessOpportunities](/modules/Sales.md#Sales.BusinessOpportunity), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Common.BusinessContactReference"></a>
### BusinessContactReferences

Represents a queryable business contact reference.

- **Endpoint:** `GET /api/v1/Common/BusinessContactReferences`
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `ExtraInformation1` | `String` | no |  |
| `ExtraInformation2` | `String` | no |  |
| `ExtraInformation3` | `String` | no |  |
| `Category` | `String` | no |  |
| `Note` | `String` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CellPhoneNumber` | `String` | no |  |
| `PhoneNumber` | `String` | no |  |
| `EmailAddress` | `String` | no |  |
| `FaxNumber` | `String` | no |  |
| `Code` | `String` | no |  |

**References out:** [Comments](/modules/Common.md#Common.Comment)
**Referenced by:** [BlanketOrderPurchases](/modules/Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderSales](/modules/Sales.md#Sales.BlanketOrderSales), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [CustomerRelationshipManagementActivities](/modules/Sales.md#Sales.CustomerRelationshipManagementActivity), [Customers](/modules/Sales.md#Sales.Customer), [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [Projects](/modules/Common.md#Common.Project), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [Quotes](/modules/Sales.md#Sales.Quote), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Common.Calendar"></a>
### Calendars

Represents a queryable calendar.

- **Endpoint:** `GET /api/v1/Common/Calendars`
- **Required permission:** Show calendar
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CalendarType` | `Int32` | no |  |
| `HolidayType` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `Code` | `String` | no |  |

- `CalendarType` — NoHoliday=0, Weekend=1, OnlySundayWeekend=2, Swedish=10, Norwegian=11, Estonian=12, Finnish=13, German=14, Hungarian=15, Latvian=16, Polish=17, Russian=18, Lithuanian=19, Usa=20, Danish=21, Andorra=22, UnitedArabEmirates=23, Afghanistan=24, AntiguaBarbuda=25, Albania=26, Armenia=27, Angola=28, Argentina=29, AmericanSamoa=30, Austria=31, Australia=32, Aruba=33, Azerbaijan=34, BosniaHerzegovina=35, Barbados=36, Bangladesh=37, Belgium=38, BurkinaFaso=39, Bulgaria=40, Bahrain=41, Burundi=42, Brunei=43, Bolivia=44, Brazil=45, Bahamas=46, Botswana=47, Belarus=48, Belize=49, Canada=50, CongoBrazzaville=51, Switzerland=52, CotedIvoire=53, Chile=54, Cameroon=55, China=56, Colombia=57, CostaRica=58, Cuba=59, Curacao=60, Cyprus=61, CzechRepublic=62, Djibouti=63, Dominica=64, DominicanRepublic=65, Algeria=66, Ecuador=67, Egypt=68, Spain=69, Ethiopia=70, Fiji=71, France=72, Gabon=73, UnitedKingdom=74, Georgia=75, Guernsey=76, Ghana=77, Greenland=78, Guinea=79, Greece=80, Guatemala=81, Guam=82, HongKong=83, Honduras=84, Croatia=85, Haiti=86, Indonesia=87, Ireland=88, Israel=89, IsleofMan=90, India=91, Iran=92, Iceland=93, Italy=94, Jersey=95, Jamaica=96, Jordan=97, Japan=98, Kenya=99, Kyrgyzstan=100, Cambodia=101, SaintKittsNevis=102, SouthKorea=103, Kuwait=104, Kazakhstan=105, Laos=106, SaintLucia=107, Liechtenstein=108, SriLanka=109, Lesotho=110, Luxembourg=111, Morocco=112, Monaco=113, Moldova=114, Montenegro=115, Madagascar=116, MarshallIslands=117, NorthMacedonia=118, Macau=119, NorthernMarianaIslands=120, Mauritania=121, Malta=122, Maldives=123, Malawi=124, Mexico=125, Malaysia=126, Mozambique=127, Namibia=128, Nigeria=129, Nicaragua=130, Netherlands=131, NewZealand=132, Oman=133, Panama=134, Peru=135, PapuaNewGuinea=136, Philippines=137, Pakistan=138, PuertoRico=139, Portugal=140, Palau=141, Paraguay=142, Qatar=143, Romania=144, Serbia=145, SaudiArabia=146, Seychelles=147, Singapore=148, Slovenia=149, Slovakia=150, SierraLeone=151, SanMarino=152, Surinam=153, SaoTomePrincipe=154, ElSalvador=155, Eswatini=156, Chad=157, FrenchSouthernTerritories=158, Thailand=159, EastTimor=160, Tunisia=161, Tonga=162, Turkiye=163, TrinidadTobago=164, Tuvalu=165, Taiwan=166, Tanzania=167, Ukraine=168, UnitedStatesMinorOutlyingIslands=169, Uruguay=170, Uzbekistan=171, VaticanCity=172, Venezuela=173, UnitedStatesVirginIslands=174, Vietnam=175, Vanuatu=176, Samoa=177, SouthAfrica=178, Zambia=179, Zimbabwe=180
- `HolidayType` (bitmask) — None=0, Weekend=1, Holiday=2, All=3

**Referenced by:** [Warehouses](/modules/Common.md#Common.Warehouse)

<a id="Common.CentralBankCode"></a>
### CentralBankCodes

Represents a central bank code.

- **Endpoint:** `GET /api/v1/Common/CentralBankCodes`
- **Required permission:** Show bank settings
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `IsDefault` | `Boolean` | no |  |

**Referenced by:** [BusinessContactBankAccounts](/modules/Common.md#Common.BusinessContactBankAccount)

<a id="Common.Comment"></a>
### Comments

Represents a comment, containing both raw and HTML formatted text.

- **Endpoint:** `GET /api/v1/Common/Comments`
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Text` | `String` | no |  |
| `RawText` | `String` | no |  |
| `HasFileLinks` | `Boolean` | no |  |
| `FileLinks` | `FileLink[]` | no | [FileLink](/modules/Common.md#Common.FileLink) |

**References out:** [FileLink](/modules/Common.md#Common.FileLink)
**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [AccrualAccountings](/modules/Accounting.md#Accounting.AccrualAccounting), [AdditionRecordings](/modules/TimeRecording.md#TimeRecording.AdditionRecording), [BlanketOrderPurchases](/modules/Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderSales](/modules/Sales.md#Sales.BlanketOrderSales), [BusinessContactNoteHistories](/modules/Common.md#Common.BusinessContactNoteHistory), [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference), [BusinessOpportunities](/modules/Sales.md#Sales.BusinessOpportunity), [BusinessOpportunityActivities](/modules/Sales.md#Sales.BusinessOpportunityActivity), [BusinessOpportunityActivityTemplateRows](/modules/Sales.md#Sales.BusinessOpportunityActivityTemplateRow), [BusinessOpportunityReferences](/modules/Sales.md#Sales.BusinessOpportunityReference), [BusinessOpportunityTypes](/modules/Sales.md#Sales.BusinessOpportunityType), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CaseEntryActivities](/modules/Inventory.md#Inventory.CaseEntryActivity), [CaseManagementTemplateNodes](/modules/Inventory.md#Inventory.CaseManagementTemplateNode), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [CustomerPartLinks](/modules/Sales.md#Sales.CustomerPartLink), [CustomerRelationshipManagementActivities](/modules/Sales.md#Sales.CustomerRelationshipManagementActivity), [Customers](/modules/Sales.md#Sales.Customer), [DrawingRevisions](/modules/Manufacturing.md#Manufacturing.DrawingRevision), [EmploymentPeriods](/modules/Common.md#Common.EmploymentPeriod), [ExtraFields](/modules/Common.md#Common.ExtraField), [FixedAssetSales](/modules/Accounting.md#Accounting.FixedAssetSale), [FormTemplateRows](/modules/Common.md#Common.FormTemplateRow), [FormTemplates](/modules/Common.md#Common.FormTemplate), [FormTemplateSelectionRows](/modules/Common.md#Common.FormTemplateSelectionRow), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [Locations](/modules/Inventory.md#Inventory.Location), [MaintenanceReportingRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingRow), [MaintenanceReportings](/modules/Manufacturing.md#Manufacturing.MaintenanceReporting), [MaintenanceReportingSelectionRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow), [ManufacturingOrderMaterials](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodeDrawingRevisions](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision), [ManufacturingOrderOperationReportings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [MaterialRows](/modules/Manufacturing.md#Manufacturing.MaterialRow), [MonitoringTasks](/modules/Common.md#Common.MonitoringTask), [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow), [PackageRows](/modules/Sales.md#Sales.PackageRow), [PartActivities](/modules/Inventory.md#Inventory.PartActivity), [PartConfigurations](/modules/Common.md#Common.PartConfiguration), [PartConfigurationTemplates](/modules/Common.md#Common.PartConfigurationTemplate), [Parts](/modules/Inventory.md#Inventory.Part), [Persons](/modules/Common.md#Common.Person), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [ProjectActivities](/modules/Common.md#Common.ProjectActivity), [ProjectActivityTypes](/modules/Common.md#Common.ProjectActivityType), [ProjectCostBudgets](/modules/Common.md#Common.ProjectCostBudget), [ProjectCostForecasts](/modules/Common.md#Common.ProjectCostForecast), [ProjectCostReportingEntries](/modules/Common.md#Common.ProjectCostReportingEntry), [Projects](/modules/Common.md#Common.Project), [PurchaseOrderInvoiceRows](/modules/Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [QuoteActivities](/modules/Sales.md#Sales.QuoteActivity), [Quotes](/modules/Sales.md#Sales.Quote), [Revisions](/modules/Common.md#Common.Revision), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement), [SalesPrices](/modules/Sales.md#Sales.SalesPrice), [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule), [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [VatRates](/modules/Common.md#Common.VatRate), [Vouchers](/modules/Accounting.md#Accounting.Voucher), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter), [WorkIntervals](/modules/TimeRecording.md#TimeRecording.WorkInterval)

<a id="Common.CommunicationAddress"></a>
### CommunicationAddresses

Represents a queryable communication address. A communication address is used to store either phone, cellphone, email or fax information in MONITOR.

- **Endpoint:** `GET /api/v1/Common/CommunicationAddresses`
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Type` | `Int32` | no |  |
| `CommunicationAddressValue` | `String` | no |  |
| `Remarks` | `String` | no |  |
| `RecipientOf` | `Int32` | no |  |
| `ContactName` | `String` | no |  |

- `Type` — Phone=0, Fax=1, Email=2, CellPhone=3
- `RecipientOf` (bitmask) — None=0, Invoice=1, Reminder=2, OrderConfirmation=4, DispatchAdvice=8, ShippingAgentAdvice=16, OrderConfirmationReminder=32, DeliveryReminder=64, DeliverySchedule=128, PurchaseOrder=256, Quote=512, ShippingAgentSmsAdvice=1024, SubcontractDeliveryNote=2048, Inquiry=4096, CaseClaimReport=8192, CaseConfirmation=16384, CaseResponse=32768, NonconformityReport=65536, Proforma=131072, ProjectReportExternal=262144, ProjectReportInternal=524288, CustomerDeliveryNote=1048576, TraceabilityProtocol=2097152, BlanketOrderPurchase=4194304, BlanketOrderSales=8388608, PurchaseDeliverySchedule=16777216, SalesAgreement=33554432, AccountStatement=67108864, EInvoiceInvitation=134217728, ReturnOrder=268435456, SubcontractProformaInvoice=536870912, SupplierAgreement=1073741824

**Referenced by:** [BusinessOpportunityReferences](/modules/Sales.md#Sales.BusinessOpportunityReference), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [Customers](/modules/Sales.md#Sales.Customer), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [Quotes](/modules/Sales.md#Sales.Quote), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Common.Company"></a>
### Companies

Represents a company in the MONITOR system.

- **Endpoint:** `GET /api/v1/Common/Companies`
- **Required permission:** Show company information
- **Introduced in:** 24.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `ImageId` | `Int64?` | yes |  |
| `Image` | `BlobData` | no | [BlobData](/modules/Common.md#Common.BlobData) |
| `CurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `Currency` | `Currencies` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `LanguageId` | `Int64` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `Language` | `LanguageCodes` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `Warehouses` | `Warehouses[]` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `TimeZone` | `String` | no |  |
| `CorporationIdentificationNumber` | `String` | no |  |

**References out:** [BlobData](/modules/Common.md#Common.BlobData), [Currencies](/modules/Common.md#Common.Currency), [LanguageCodes](/modules/Common.md#Common.LanguageCode), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [Warehouses](/modules/Common.md#Common.Warehouse)

<a id="Common.CompanyEmissionDetail"></a>
### CompanyEmissionDetails

Represents a company emission type linked to sustainability reporting according to the GHG protocol.

- **Endpoint:** `GET /api/v1/Common/CompanyEmissionDetails`
- **Required permission:** Show pre-calculation
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `EmissionType` | `Int32` | no |  |
| `Value` | `Decimal` | no |  |
| `Origin` | `String` | no |  |
| `OriginDate` | `DateTimeOffset?` | yes |  |
| `ReliabilityIndex` | `Decimal` | no |  |
| `ReportingMethod` | `Int32` | no |  |
| `UnitId` | `Int64?` | yes |  |
| `Unit` | `Units` | no | [Units](/modules/Common.md#Common.Unit) |

**References out:** [Units](/modules/Common.md#Common.Unit)

<a id="Common.CompanyOverheadType"></a>
### CompanyOverheadTypes

Represents an overhead type used in company emission and sustainability calculations.

- **Endpoint:** `GET /api/v1/Common/CompanyOverheadTypes`
- **Required permission:** Show pre-calculation
- **Introduced in:** 25.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Code` | `String` | no |  |
| `IsDefault` | `Boolean` | no |  |


<a id="Common.ConnectionProfile"></a>
### ConnectionProfiles

Represents a connection profile.

- **Endpoint:** `GET /api/v1/Common/ConnectionProfiles`
- **Required permission:** Show connection
- **Introduced in:** 23.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `TargetRole` | `Int32` | no |  |
| `RemoteCompanyId` | `Guid` | no |  |
| `RemoteCompanyNumber` | `String` | no |  |
| `RemoteCompanyName` | `String` | no |  |
| `RemoteDnsName` | `String` | no |  |
| `RemotePort` | `Int32` | no |  |
| `LocalDnsName` | `String` | no |  |
| `LocalPort` | `Int32` | no |  |

- `TargetRole` — ManufacturingCompany=0, SalesCompany=1

**Referenced by:** [TransferProfiles](/modules/Common.md#Common.TransferProfile)

<a id="Common.Country"></a>
### Countries

Represents a queryable country.

- **Endpoint:** `GET /api/v1/Common/Countries`
- **Required permission:** Show countries
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `IsEuMember` | `Boolean` | no |  |
| `LanguageId` | `Int64` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `CurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `AddressFormatType` | `Int32` | no |  |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup) |
| `IsActive` | `Boolean` | no |  |
| `SupplierAccountGroupId` | `Int64?` | yes |  |
| `VatGroupId` | `Int64?` | yes | [VatGroups](/modules/Common.md#Common.VatGroup) |
| `SupplierVatGroupId` | `Int64?` | yes | [VatGroups](/modules/Common.md#Common.VatGroup) |
| `CustomerVatGroupId` | `Int64?` | yes | [VatGroups](/modules/Common.md#Common.VatGroup) |
| `VatRegistrationNumberPrefixException` | `String` | no |  |
| `CountryRegion` | `Int32` | no |  |
| `CountrySubRegion` | `Int32` | no |  |
| `CountryIntermediateRegion` | `Int32` | no |  |

**References out:** [Currencies](/modules/Common.md#Common.Currency), [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup), [LanguageCodes](/modules/Common.md#Common.LanguageCode), [VatGroups](/modules/Common.md#Common.VatGroup)
**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [Addresses](/modules/Common.md#Common.Address), [BusinessContactBankAccounts](/modules/Common.md#Common.BusinessContactBankAccount), [CountryDocumentSettings](/modules/Sales.md#Sales.CountryDocumentSettings), [CustomerCountryDocumentSettings](/modules/Sales.md#Sales.CustomerCountryDocumentSettings), [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress), [Parts](/modules/Inventory.md#Inventory.Part), [PartTemplates](/modules/Inventory.md#Inventory.PartTemplate), [ShipmentCustomsRows](/modules/Sales.md#Sales.ShipmentCustomsRow), [Warehouses](/modules/Common.md#Common.Warehouse)

<a id="Common.Currency"></a>
### Currencies

Represents a queryable currency.

- **Endpoint:** `GET /api/v1/Common/Currencies`
- **Required permission:** Show currencies
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `RateFactor` | `Int32` | no |  |
| `DefaultSalesExchangeRate` | `Decimal` | no |  |
| `DefaultPurchaseExchangeRate` | `Decimal` | no |  |
| `ExchangeRates` | `CurrencyExchangeRates[]` | no | [CurrencyExchangeRates](/modules/Common.md#Common.CurrencyExchangeRate) |
| `ExchangeRatesChangeLog` | `CurrencyExchangeRateChangeLogs[]` | no | [CurrencyExchangeRateChangeLogs](/modules/Common.md#Common.CurrencyExchangeRateChangeLog) |

**References out:** [CurrencyExchangeRateChangeLogs](/modules/Common.md#Common.CurrencyExchangeRateChangeLog), [CurrencyExchangeRates](/modules/Common.md#Common.CurrencyExchangeRate)
**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [AccountYearSettings](/modules/Accounting.md#Accounting.AccountYearSetting), [AdditionRecordings](/modules/TimeRecording.md#TimeRecording.AdditionRecording), [Alloys](/modules/Inventory.md#Inventory.Alloy), [AttendanceAdditions](/modules/TimeRecording.md#TimeRecording.AttendanceAddition), [BankAccounts](/modules/Accounting.md#Accounting.BankAccount), [BlanketOrderPurchaseRows](/modules/Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderPurchases](/modules/Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderSales](/modules/Sales.md#Sales.BlanketOrderSales), [BlanketOrderSalesRows](/modules/Sales.md#Sales.BlanketOrderSalesRow), [BookingRows](/modules/Accounting.md#Accounting.BookingRow), [BusinessContactBankAccounts](/modules/Common.md#Common.BusinessContactBankAccount), [CaseEntryActivities](/modules/Inventory.md#Inventory.CaseEntryActivity), [CaseEntryAdditionalCost](/modules/Inventory.md#Inventory.CaseEntryAdditionalCost), [CaseManagementActivities](/modules/Inventory.md#Inventory.CaseManagementActivity), [CaseManagementCost](/modules/Inventory.md#Inventory.CaseManagementCost), [CaseManagementTemplateCosts](/modules/Inventory.md#Inventory.CaseManagementTemplateCost), [Companies](/modules/Common.md#Common.Company), [Countries](/modules/Common.md#Common.Country), [CurrencyExchangeRateChangeLogs](/modules/Common.md#Common.CurrencyExchangeRateChangeLog), [CustomerOrderInvoiceOrderRowDiscounts](/modules/Sales.md#Sales.CustomerOrderInvoiceOrderRowDiscount), [CustomerOrderInvoiceRows](/modules/Sales.md#Sales.CustomerOrderInvoiceRow), [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [CustomerOrderOrderRowDiscounts](/modules/Sales.md#Sales.CustomerOrderOrderRowDiscount), [CustomerOrderPaymentPlanRows](/modules/Sales.md#Sales.CustomerOrderPaymentPlanRow), [CustomerOrderRowInflows](/modules/Sales.md#Sales.CustomerOrderRowInflow), [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [CustomerPartLinks](/modules/Sales.md#Sales.CustomerPartLink), [Customers](/modules/Sales.md#Sales.Customer), [IncomingPayments](/modules/Accounting.md#Accounting.IncomingPayment), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [InquiryRows](/modules/Purchase.md#Purchase.InquiryRow), [Money](/modules/Common.md#Common.Money), [OpeningBalances](/modules/Accounting.md#Accounting.OpeningBalance), [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow), [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment), [PartConfigurationResults](/modules/Common.md#Common.PartConfigurationResult), [PartConfigurationSelectionGroupResults](/modules/Common.md#Common.PartConfigurationSelectionGroupResult), [Parts](/modules/Inventory.md#Inventory.Part), [PriceChangeLogs](/modules/Inventory.md#Inventory.PriceChangeLog), [PriceLists](/modules/Common.md#Common.PriceList), [PurchaseOrderInvoiceRows](/modules/Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [QuoteOrderRowDiscounts](/modules/Sales.md#Sales.QuoteOrderRowDiscount), [QuoteRows](/modules/Sales.md#Sales.QuoteRow), [Quotes](/modules/Sales.md#Sales.Quote), [SalesAgreementBases](/modules/Sales.md#Sales.SalesAgreementBasis), [SalesAgreementBasisRows](/modules/Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRowInflows](/modules/Sales.md#Sales.SalesAgreementRowInflow), [SalesAgreementRows](/modules/Sales.md#Sales.SalesAgreementRow), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement), [SalesPrices](/modules/Sales.md#Sales.SalesPrice), [ShipmentCustoms](/modules/Sales.md#Sales.ShipmentCustoms), [Shipments](/modules/Sales.md#Sales.Shipment), [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow)

<a id="Common.CurrencyExchangeRateChangeLog"></a>
### CurrencyExchangeRateChangeLogs

Represents a currency exchange rate entry.

- **Endpoint:** `GET /api/v1/Common/CurrencyExchangeRateChangeLogs`
- **Required permission:** Show currencies
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](/modules/Common.md#Common.CurrencyExchangeType) |
| `Rate` | `Decimal` | no |  |
| `ValidUntilDate` | `DateTimeOffset` | no |  |
| `CurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |

**References out:** [Currencies](/modules/Common.md#Common.Currency), [CurrencyExchangeTypes](/modules/Common.md#Common.CurrencyExchangeType)
**Referenced by:** [Currencies](/modules/Common.md#Common.Currency)

<a id="Common.CurrencyExchangeRate"></a>
### CurrencyExchangeRates

Represents a currency exchange rate entry.

- **Endpoint:** `GET /api/v1/Common/CurrencyExchangeRates`
- **Required permission:** Show currencies
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](/modules/Common.md#Common.CurrencyExchangeType) |
| `Rate` | `Decimal` | no |  |

**References out:** [CurrencyExchangeTypes](/modules/Common.md#Common.CurrencyExchangeType)
**Referenced by:** [Currencies](/modules/Common.md#Common.Currency)

<a id="Common.CurrencyExchangeType"></a>
### CurrencyExchangeTypes

Represents a currency exchange type.

- **Endpoint:** `GET /api/v1/Common/CurrencyExchangeTypes`
- **Required permission:** Show currencies
- **Introduced in:** 22.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `IsDefaultAFSRate` | `Boolean` | no |  |

**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [BlanketOrderPurchases](/modules/Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderPurchaseTypes](/modules/Purchase.md#Purchase.BlanketOrderPurchaseType), [BlanketOrderSales](/modules/Sales.md#Sales.BlanketOrderSales), [BlanketOrderSalesTypes](/modules/Sales.md#Sales.BlanketOrderSalesType), [CurrencyExchangeRateChangeLogs](/modules/Common.md#Common.CurrencyExchangeRateChangeLog), [CurrencyExchangeRates](/modules/Common.md#Common.CurrencyExchangeRate), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [CustomerOrderTypes](/modules/Sales.md#Sales.CustomerOrderType), [Customers](/modules/Sales.md#Sales.Customer), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [InquiryTypes](/modules/Purchase.md#Purchase.InquiryType), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [PurchaseOrderTypes](/modules/Purchase.md#Purchase.PurchaseOrderType), [Quotes](/modules/Sales.md#Sales.Quote), [QuoteTypes](/modules/Sales.md#Sales.QuoteType), [ShipmentCustoms](/modules/Sales.md#Sales.ShipmentCustoms), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Common.CustomReportDefinition"></a>
### CustomReportDefinitions

Represents a queryable custom report definition.

- **Endpoint:** `GET /api/v1/Common/CustomReportDefinitions`
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ReportNumber` | `String` | no |  |
| `Description` | `String` | no |  |
| `DisplayDefinitions` | `CustomReportDisplayDefinitions[]` | no | [CustomReportDisplayDefinitions](/modules/Common.md#Common.CustomReportDisplayDefinition) |

**References out:** [CustomReportDisplayDefinitions](/modules/Common.md#Common.CustomReportDisplayDefinition)
**Referenced by:** [CustomReportDisplayDefinitions](/modules/Common.md#Common.CustomReportDisplayDefinition)

<a id="Common.CustomReportDisplayDefinition"></a>
### CustomReportDisplayDefinitions

Represents a queryable custom report display definition.

- **Endpoint:** `GET /api/v1/Common/CustomReportDisplayDefinitions`
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `DisplayId` | `Guid` | no |  |
| `Description` | `String` | no |  |
| `ReportType` | `Int32` | no |  |
| `Sql` | `String` | no |  |
| `ParentId` | `Int64` | no | [CustomReportDefinitions](/modules/Common.md#Common.CustomReportDefinition) |

- `ReportType` — Grid=0, Report=1, SubReport=2

**References out:** [CustomReportDefinitions](/modules/Common.md#Common.CustomReportDefinition)
**Referenced by:** [CustomReportDefinitions](/modules/Common.md#Common.CustomReportDefinition)

<a id="Common.DelegatedWork"></a>
### DelegatedWork

Represents a delegated work.

- **Endpoint:** `GET /api/v1/Common/DelegatedWork`
- **Required permission:** Show Activity list – Project
- **Introduced in:** 2.50

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `WorkRecordingType` | `Int32` | no |  |
| `DelegatedBy` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `EmployeeId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `ActivityId` | `Int64?` | yes | [ProjectActivities](/modules/Common.md#Common.ProjectActivity) |
| `OperationId` | `Int64?` | yes | [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |

- `WorkRecordingType` — Indirect=0, OperationSetup=1, OperationUnit=2, ProjectActivity=3

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [Persons](/modules/Common.md#Common.Person), [ProjectActivities](/modules/Common.md#Common.ProjectActivity)

<a id="Common.DeliveryAddress"></a>
### DeliveryAddresses

Represents a delivery address.

- **Endpoint:** `GET /api/v1/Common/DeliveryAddresses`
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Addressee` | `String` | no |  |
| `Field1` | `String` | no |  |
| `Field2` | `String` | no |  |
| `Field3` | `String` | no |  |
| `Field4` | `String` | no |  |
| `Field5` | `String` | no |  |
| `Locality` | `String` | no |  |
| `Region` | `String` | no |  |
| `PostalCode` | `String` | no |  |
| `AddressFormatType` | `Int32` | no |  |
| `CountryId` | `Int64` | no | [Countries](/modules/Common.md#Common.Country) |
| `LanguageId` | `Int64` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `FormReportTranslationGroupId` | `Int64` | no |  |
| `PostalCodeId` | `Int64?` | yes |  |
| `IsDefault` | `Boolean` | no |  |
| `AddressId` | `Int64` | no | [Addresses](/modules/Common.md#Common.Address) |
| `ConsigneeReferenceId` | `Int64?` | yes | [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference) |
| `ConsigneeReferenceName` | `String` | no |  |
| `Destination` | `String` | no |  |
| `DeliveryWeekdays` | `Int32` | no |  |
| `DeliveryInstruction` | `String` | no |  |
| `VatRateId` | `Int64?` | yes | [VatRates](/modules/Common.md#Common.VatRate) |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup) |
| `SupplierAccountGroupId` | `Int64?` | yes |  |
| `VatGroupId` | `Int64?` | yes | [VatGroups](/modules/Common.md#Common.VatGroup) |
| `VatNumber` | `String` | no |  |
| `Warehouses` | `DeliveryAddressWarehouseInformations[]` | no | [DeliveryAddressWarehouseInformations](/modules/Common.md#Common.DeliveryAddressWarehouseInformation) |

- `DeliveryWeekdays` (bitmask) — None=0, Monday=1, Tuesday=2, Wednesday=4, Thursday=8, Friday=16, Saturday=32, Sunday=64

**References out:** [Addresses](/modules/Common.md#Common.Address), [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference), [Countries](/modules/Common.md#Common.Country), [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup), [DeliveryAddressWarehouseInformations](/modules/Common.md#Common.DeliveryAddressWarehouseInformation), [LanguageCodes](/modules/Common.md#Common.LanguageCode), [VatGroups](/modules/Common.md#Common.VatGroup), [VatRates](/modules/Common.md#Common.VatRate)
**Referenced by:** [Customers](/modules/Sales.md#Sales.Customer), [DeliveryAddressWarehouseInformations](/modules/Common.md#Common.DeliveryAddressWarehouseInformation), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [Shipments](/modules/Sales.md#Sales.Shipment), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [Warehouses](/modules/Common.md#Common.Warehouse)

<a id="Common.DeliveryAddressWarehouseInformation"></a>
### DeliveryAddressWarehouseInformations

Represents a queryable delivery address warehouse information entry.

- **Endpoint:** `GET /api/v1/Common/DeliveryAddressWarehouseInformations`
- **Introduced in:** 2.43

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `WarehouseId` | `Int64?` | yes | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](/modules/Common.md#Common.DeliveryMethod) |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](/modules/Common.md#Common.DeliveryTerm) |
| `TransportTime` | `TimeSpan?` | yes |  |
| `DeliveryWeekdays` | `Int32` | no |  |
| `DestinationForDeliveryTerm` | `String` | no |  |
| `ParentId` | `Int64` | no | [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress) |

- `DeliveryWeekdays` (bitmask) — None=0, Monday=1, Tuesday=2, Wednesday=4, Thursday=8, Friday=16, Saturday=32, Sunday=64

**References out:** [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress), [DeliveryMethods](/modules/Common.md#Common.DeliveryMethod), [DeliveryTerms](/modules/Common.md#Common.DeliveryTerm), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress)

<a id="Common.DeliveryMethod"></a>
### DeliveryMethods

Represents a queryable delivery method.

- **Endpoint:** `GET /api/v1/Common/DeliveryMethods`
- **Required permission:** Show terms
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `SupplierId` | `Int64?` | yes | [Suppliers](/modules/Purchase.md#Purchase.Supplier) |
| `CompanyIds` | `Int64[]` | no |  |
| `ShippingServiceId` | `Int64?` | yes |  |
| `ShippingTemplateId` | `Int64?` | yes |  |
| `Code` | `String` | no |  |

**References out:** [Suppliers](/modules/Purchase.md#Purchase.Supplier)
**Referenced by:** [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [DeliveryAddressWarehouseInformations](/modules/Common.md#Common.DeliveryAddressWarehouseInformation), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [PurchaseOrderInvoices](/modules/Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [Quotes](/modules/Sales.md#Sales.Quote), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement), [ShipmentCustoms](/modules/Sales.md#Sales.ShipmentCustoms), [Shipments](/modules/Sales.md#Sales.Shipment)

<a id="Common.DeliveryTerm"></a>
### DeliveryTerms

Represents a queryable delivery term.

- **Endpoint:** `GET /api/v1/Common/DeliveryTerms`
- **Required permission:** Show terms
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `Description` | `String` | no |  |
| `Number` | `Int64` | no |  |
| `Destination` | `String` | no |  |
| `TermLocation` | `String` | no |  |
| `TermCode` | `String` | no |  |
| `Payer` | `Int32` | no |  |
| `CompanyIds` | `Int64[]` | no |  |
| `ShipmentDefaultCode` | `String` | no |  |

- `Payer` — BuyerPays=1, SellerPays=2, OtherPayer=3, Incoterms=4

**Referenced by:** [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [DeliveryAddressWarehouseInformations](/modules/Common.md#Common.DeliveryAddressWarehouseInformation), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [PurchaseOrderInvoices](/modules/Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [Quotes](/modules/Sales.md#Sales.Quote), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement), [Shipments](/modules/Sales.md#Sales.Shipment)

<a id="Common.DeliveryTime"></a>
### DeliveryTimes

Represents a queryable delivery time.

- **Endpoint:** `GET /api/v1/Common/DeliveryTimes`
- **Required permission:** Show terms
- **Introduced in:** 23.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Days` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `Number` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |

**Referenced by:** [Quotes](/modules/Sales.md#Sales.Quote)

<a id="Common.Department"></a>
### Departments

Represents a queryable department.

- **Endpoint:** `GET /api/v1/Common/Departments`
- **Required permission:** Show departments
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [FixedAssets](/modules/Accounting.md#Accounting.FixedAsset), [Persons](/modules/Common.md#Common.Person)

<a id="Common.DiscountCategory"></a>
### DiscountCategories

Represents a queryable discount category.

- **Endpoint:** `GET /api/v1/Common/DiscountCategories`
- **Required permission:** Show discount categories
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `Description` | `String` | no |  |
| `CompanyIds` | `Int64[]` | no |  |
| `Rows` | `DiscountCategoryRows[]` | no | [DiscountCategoryRows](/modules/Common.md#Common.DiscountCategoryRow) |

**References out:** [DiscountCategoryRows](/modules/Common.md#Common.DiscountCategoryRow)
**Referenced by:** [Customers](/modules/Sales.md#Sales.Customer), [DiscountCategoryRows](/modules/Common.md#Common.DiscountCategoryRow), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Common.DiscountCategoryRow"></a>
### DiscountCategoryRows

Represents a discount category row.

- **Endpoint:** `GET /api/v1/Common/DiscountCategoryRows`
- **Required permission:** Show discount categories
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `DiscountCategoryId` | `Int64` | no | [DiscountCategories](/modules/Common.md#Common.DiscountCategory) |
| `BoundaryType` | `Int32` | no |  |
| `ProductGroupId` | `Int64?` | yes | [ProductGroups](/modules/Common.md#Common.ProductGroup) |
| `PartCodeId` | `Int64?` | yes | [PartCodes](/modules/Inventory.md#Inventory.PartCode) |
| `PartCategory` | `String` | no |  |
| `Boundary1` | `Decimal` | no |  |
| `Discount1` | `Decimal` | no |  |
| `Boundary2` | `Decimal` | no |  |
| `Discount2` | `Decimal` | no |  |
| `Boundary3` | `Decimal` | no |  |
| `Discount3` | `Decimal` | no |  |
| `Boundary4` | `Decimal` | no |  |
| `Discount4` | `Decimal` | no |  |
| `Boundary5` | `Decimal` | no |  |
| `Discount5` | `Decimal` | no |  |
| `Boundary6` | `Decimal` | no |  |
| `Discount6` | `Decimal` | no |  |
| `Boundary7` | `Decimal` | no |  |
| `Discount7` | `Decimal` | no |  |
| `Boundary8` | `Decimal` | no |  |
| `Discount8` | `Decimal` | no |  |
| `Boundary9` | `Decimal` | no |  |
| `Discount9` | `Decimal` | no |  |
| `Boundary10` | `Decimal` | no |  |
| `Discount10` | `Decimal` | no |  |

- `BoundaryType` — Quantity=0, Value=1

**References out:** [DiscountCategories](/modules/Common.md#Common.DiscountCategory), [PartCodes](/modules/Inventory.md#Inventory.PartCode), [ProductGroups](/modules/Common.md#Common.ProductGroup)
**Referenced by:** [DiscountCategories](/modules/Common.md#Common.DiscountCategory)

<a id="Common.Discount"></a>
### Discounts

Represents a queryable discount.

- **Endpoint:** `GET /api/v1/Common/Discounts`
- **Required permission:** Show discounts
- **Introduced in:** 24.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Name` | `String` | no |  |
| `IsActive` | `Boolean` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `DiscountForModule` | `Int32` | no |  |
| `DiscountType` | `Int32` | no |  |
| `Priority` | `Int32` | no |  |
| `DiscountCalculationType` | `Int32` | no |  |

- `DiscountForModule` — Sales=0
- `DiscountType` — Discount=0, OrderDiscount=1, TotalRowDiscount=2, ProjectDiscount=3, CustomerDiscountOnDiscount=4, OrderTypeDiscount=5, ManualDiscount=99
- `DiscountCalculationType` — Percent=1, Amount=2

**Referenced by:** [CustomerOrderInvoiceOrderRowDiscounts](/modules/Sales.md#Sales.CustomerOrderInvoiceOrderRowDiscount), [CustomerOrderOrderRowDiscounts](/modules/Sales.md#Sales.CustomerOrderOrderRowDiscount), [QuoteOrderRowDiscounts](/modules/Sales.md#Sales.QuoteOrderRowDiscount)

<a id="Common.EdiBehavior"></a>
### EdiBehaviors

Represents an Edi Behavior

- **Endpoint:** `GET /api/v1/Common/EdiBehaviors`
- **Required permission:** Show EDI settings
- **Introduced in:** 25.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `Module` | `Int32` | no |  |
| `EdiChannelConfigurations` | `EdiChannelConfigurations[]` | no | [EdiChannelConfigurations](/modules/Common.md#Common.EdiChannelConfiguration) |
| `Customers` | `Customers[]` | no | [Customers](/modules/Sales.md#Sales.Customer) |
| `InvoiceCustomers` | `Customers[]` | no | [Customers](/modules/Sales.md#Sales.Customer) |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Warehouse` | `Warehouses` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |

- `Module` — None=0, Sales=1, Purchase=2

**References out:** [Customers](/modules/Sales.md#Sales.Customer), [EdiChannelConfigurations](/modules/Common.md#Common.EdiChannelConfiguration), [Warehouses](/modules/Common.md#Common.Warehouse)

<a id="Common.EdiChannelConfiguration"></a>
### EdiChannelConfigurations

Represents an Edi Channel Configuration.

- **Endpoint:** `GET /api/v1/Common/EdiChannelConfigurations`
- **Introduced in:** 25.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no |  |
| `ChannelId` | `Int64` | no |  |
| `NotificationsActive` | `Boolean` | no |  |
| `Active` | `Boolean` | no |  |

**Referenced by:** [EdiBehaviors](/modules/Common.md#Common.EdiBehavior)

<a id="Common.EmploymentPeriod"></a>
### EmploymentPeriods

Represents the employment period of a personnel record.

- **Endpoint:** `GET /api/v1/Common/EmploymentPeriods`
- **Required permission:** Show person
- **Introduced in:** 22.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `StartDate` | `DateTimeOffset` | no |  |
| `FinishDate` | `DateTimeOffset?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `PersonId` | `Int64` | no | [Persons](/modules/Common.md#Common.Person) |
| `RowIndex` | `Int32` | no |  |

**References out:** [Comments](/modules/Common.md#Common.Comment), [Persons](/modules/Common.md#Common.Person)
**Referenced by:** [Persons](/modules/Common.md#Common.Person)

<a id="Common.EntityChangeLog"></a>
### EntityChangeLogs

Represents a queryable entity changelog entry.

- **Endpoint:** `GET /api/v1/Common/EntityChangeLogs`
- **Required permission:** Show changelog
- **Introduced in:** 2.33

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ChangeType` | `Int32` | no |  |
| `EntityTypeId` | `Guid` | no |  |
| `EntityId` | `Int64` | no |  |
| `ModifiedBy` | `String` | no |  |
| `ModifiedTimestamp` | `DateTimeOffset` | no |  |
| `AssociatedTypeId` | `Guid?` | yes |  |
| `AssociatedEntityId` | `Int64?` | yes |  |
| `EntityCode` | `String` | no |  |
| `Changes` | `EntityPropertyChanges[]` | no | [EntityPropertyChanges](/modules/Common.md#Common.EntityPropertyChange) |
| `Remark` | `String` | no |  |

- `ChangeType` — Update=0, Create=1, Delete=2

**References out:** [EntityPropertyChanges](/modules/Common.md#Common.EntityPropertyChange)

<a id="Common.EntityPropertyChange"></a>
### EntityPropertyChanges

Represents a queryable entity property change entry.

- **Endpoint:** `GET /api/v1/Common/EntityPropertyChanges`
- **Required permission:** Show changelog
- **Introduced in:** 2.33

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `MemberName` | `String` | no |  |
| `OldValue` | `String` | no |  |
| `NewValue` | `String` | no |  |
| `ChangeType` | `Int32` | no |  |
| `EntityChangeLogId` | `Int64` | no |  |

- `ChangeType` — Update=0, Create=1, Delete=2

**Referenced by:** [EntityChangeLogs](/modules/Common.md#Common.EntityChangeLog)

<a id="Common.ExtraFieldGroup"></a>
### ExtraFieldGroups

Represents an extra field group.

- **Endpoint:** `GET /api/v1/Common/ExtraFieldGroups`
- **Required permission:** Show extra fields
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `EntityId` | `Guid` | no |  |
| `RowNumber` | `Int32` | no |  |
| `Templates` | `ExtraFieldTemplates[]` | no | [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate) |

**References out:** [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate)
**Referenced by:** [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate)

<a id="Common.ExtraFieldOptionTemplate"></a>
### ExtraFieldOptionTemplates

Represents an extra field option template.

- **Endpoint:** `GET /api/v1/Common/ExtraFieldOptionTemplates`
- **Required permission:** Show extra fields
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `IsActive` | `Boolean` | no |  |
| `Description` | `String` | no |  |
| `ExtraFieldTemplateId` | `Int64` | no | [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate) |

**References out:** [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate)
**Referenced by:** [ExtraFields](/modules/Common.md#Common.ExtraField), [ExtraFieldTemplates](/modules/Common.md#Common.ExtraFieldTemplate)

<a id="Common.ExtraField"></a>
### ExtraFields

Represents an extra field.

- **Endpoint:** `GET /api/v1/Common/ExtraFields`
- **Required permission:** Show extra fields
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentClass` | `Guid` | no |  |
| `ParentId` | `Int64` | no |  |
| `Identifier` | `String` | no |  |
| `Type` | `Int32` | no |  |
| `StringValue` | `String` | no |  |
| `IntegerValue` | `Int32?` | yes |  |
| `DecimalValue` | `Decimal?` | yes |  |
| `DateOnlyValue` | `DateTimeOffset?` | yes |  |
| `DateTimeValue` | `DateTimeOffset?` | yes |  |
| `SelectedOptionId` | `Int64?` | yes | [ExtraFieldOptionTemplates](/modules/Common.md#Common.ExtraFieldOptionTemplate) |
| `SelectedOption` | `ExtraFieldOptionTemplates` | no | [ExtraFieldOptionTemplates](/modules/Common.md#Common.ExtraFieldOptionTemplate) |
| `SelectedOptionIds` | `String` | no | [ExtraFieldOptionTemplates](/modules/Common.md#Common.ExtraFieldOptionTemplate) |
| `SelectedOptions` | `ExtraFieldOptionTemplates[]` | no | [ExtraFieldOptionTemplates](/modules/Common.md#Common.ExtraFieldOptionTemplate) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

**References out:** [Comments](/modules/Common.md#Common.Comment), [ExtraFieldOptionTemplates](/modules/Common.md#Common.ExtraFieldOptionTemplate)
**Referenced by:** [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [Customers](/modules/Sales.md#Sales.Customer), [OperationRows](/modules/Manufacturing.md#Manufacturing.OperationRow), [Parts](/modules/Inventory.md#Inventory.Part), [Persons](/modules/Common.md#Common.Person), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [Projects](/modules/Common.md#Common.Project), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Common.ExtraFieldTemplate"></a>
### ExtraFieldTemplates

Represents an extra field template.

- **Endpoint:** `GET /api/v1/Common/ExtraFieldTemplates`
- **Required permission:** Show extra fields
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `Description` | `String` | no |  |
| `Type` | `Int32` | no |  |
| `ParentId` | `Int64` | no | [ExtraFieldGroups](/modules/Common.md#Common.ExtraFieldGroup) |
| `RowNumber` | `Int32` | no |  |
| `Identifier` | `String` | no |  |
| `OptionTemplates` | `ExtraFieldOptionTemplates[]` | no | [ExtraFieldOptionTemplates](/modules/Common.md#Common.ExtraFieldOptionTemplate) |

- `Type` — String=0, Integer=1, Decimal=2, Date=3, DateTime=4, Comment=5, Options=6, MultiOptions=7

**References out:** [ExtraFieldGroups](/modules/Common.md#Common.ExtraFieldGroup), [ExtraFieldOptionTemplates](/modules/Common.md#Common.ExtraFieldOptionTemplate)
**Referenced by:** [ExtraFieldGroups](/modules/Common.md#Common.ExtraFieldGroup), [ExtraFieldOptionTemplates](/modules/Common.md#Common.ExtraFieldOptionTemplate), [Preparations](/modules/Manufacturing.md#Manufacturing.Preparation)

<a id="Common.FilePath"></a>
### FilePaths

Represents a queryable file path.

- **Endpoint:** `GET /api/v1/Common/FilePaths`
- **Required permission:** Show paths
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Path` | `String` | no |  |
| `Description` | `String` | no |  |
| `Active` | `Boolean` | no |  |
| `Category` | `Int32` | no |  |
| `FileType` | `Int32` | no |  |
| `PathType` | `Int32` | no |  |

- `Category` — FileViewer=1, ExportAccounting=2, ExportAgent=3, ExportFactoring=4, ExportServerPrinter=5, ImportAccounting=6, ImportSerialNumbers=7, ImportAdditionalIds=8
- `FileType` — FileSystem=0, SharePoint=1
- `PathType` (bitmask) — LocalServerDrives=1, UncServerShare=2, SharePoint=4, AvailablePaths=8, RegisteredPaths=16, LocalClient=32

**Referenced by:** [ServerPrinters](/modules/Common.md#Common.ServerPrinter)

<a id="Common.FormReportConfiguration"></a>
### FormReportConfigurations

Represents a form report configuration.

- **Endpoint:** `GET /api/v1/Common/FormReportConfigurations`
- **Introduced in:** 2.36

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Type` | `Int32` | no |  |
| `TypeId` | `Guid` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `Hint` | `String` | no |  |
| `Name` | `String` | no |  |
| `IsStandard` | `Boolean` | no |  |
| `DocumentId` | `Guid` | no |  |
| `IsAdaptation` | `Boolean` | no |  |

**Referenced by:** [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [PartDefaultTransportLabels](/modules/Inventory.md#Inventory.PartDefaultTransportLabel), [PaymentMethods](/modules/Common.md#Common.PaymentMethod), [QuoteTypes](/modules/Sales.md#Sales.QuoteType)

<a id="Common.FormReportTranslationGroup"></a>
### FormReportTranslationGroups

Represents a form report translation group.

- **Endpoint:** `GET /api/v1/Common/FormReportTranslationGroups`
- **Introduced in:** 2.48

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `DocumentFont` | `Int32` | no |  |
| `IsPreset` | `Boolean` | no |  |
| `Description` | `String` | no |  |
| `Code` | `String` | no |  |
| `Translations` | `FormReportTranslations[]` | no | [FormReportTranslations](/modules/Common.md#Common.FormReportTranslation) |

- `DocumentFont` — Default=0, SimplifiedChinese=1, Thai=2

**References out:** [FormReportTranslations](/modules/Common.md#Common.FormReportTranslation)
**Referenced by:** [FormReportTranslations](/modules/Common.md#Common.FormReportTranslation)

<a id="Common.FormReportTranslation"></a>
### FormReportTranslations

Represents a form report translation.

- **Endpoint:** `GET /api/v1/Common/FormReportTranslations`
- **Introduced in:** 2.48

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Phrase` | `String` | no |  |
| `PhraseId` | `Int64` | no |  |
| `FormReportTranslationGroupId` | `Int64` | no | [FormReportTranslationGroups](/modules/Common.md#Common.FormReportTranslationGroup) |

**References out:** [FormReportTranslationGroups](/modules/Common.md#Common.FormReportTranslationGroup)
**Referenced by:** [FormReportTranslationGroups](/modules/Common.md#Common.FormReportTranslationGroup)

<a id="Common.FormTemplateRow"></a>
### FormTemplateRows

Represents a form template row.

- **Endpoint:** `GET /api/v1/Common/FormTemplateRows`
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Description` | `String` | no |  |
| `FormTemplateSelectionRowId` | `Int64` | no | [FormTemplateSelectionRows](/modules/Common.md#Common.FormTemplateSelectionRow) |
| `RowIndex` | `Int32?` | yes |  |
| `Checkbox` | `Boolean` | no |  |
| `DateTimeValue` | `DateTimeOffset?` | yes |  |
| `Number` | `Decimal?` | yes |  |
| `TextValue` | `String` | no |  |
| `Type` | `Int32` | no |  |
| `LowerBoundary` | `Decimal?` | yes |  |
| `UpperBoundary` | `Decimal?` | yes |  |
| `MinValue` | `Decimal?` | yes |  |
| `MaxValue` | `Decimal?` | yes |  |
| `Value` | `Decimal?` | yes |  |
| `Mandatory` | `Boolean` | no |  |
| `PrintOut` | `Boolean` | no |  |
| `MasterToolId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `UnitId` | `Int64?` | yes | [Units](/modules/Common.md#Common.Unit) |

- `Type` — Decimal=0, Text=1, CheckBox=2, Date=3

**References out:** [Comments](/modules/Common.md#Common.Comment), [FormTemplateSelectionRows](/modules/Common.md#Common.FormTemplateSelectionRow), [Parts](/modules/Inventory.md#Inventory.Part), [Units](/modules/Common.md#Common.Unit)

<a id="Common.FormTemplate"></a>
### FormTemplates

Represents a measuring or maintenance form template.

- **Endpoint:** `GET /api/v1/Common/FormTemplates`
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Description` | `String` | no |  |
| `ControlDataType` | `Int32` | no |  |
| `Type` | `Int32` | no |  |

- `ControlDataType` — Maintenance=0, MeasuringData=1
- `Type` (bitmask) — None=0, Manufacturing=1, Purchase=2

**References out:** [Comments](/modules/Common.md#Common.Comment)
**Referenced by:** [FormTemplateSelectionRows](/modules/Common.md#Common.FormTemplateSelectionRow), [ManufacturingOrderOperationControlDataRows](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow), [MeasuringTemplates](/modules/Common.md#Common.MeasuringTemplate), [OperationRowControlDataRows](/modules/Manufacturing.md#Manufacturing.OperationRowControlDataRow), [PartPurchaseControlDataRows](/modules/Inventory.md#Inventory.PartPurchaseControlDataRow)

<a id="Common.FormTemplateSelectionRow"></a>
### FormTemplateSelectionRows

Represents a form template selection row.

- **Endpoint:** `GET /api/v1/Common/FormTemplateSelectionRows`
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Description` | `String` | no |  |
| `FormTemplateId` | `Int64` | no | [FormTemplates](/modules/Common.md#Common.FormTemplate) |
| `RowIndex` | `Int32?` | yes |  |

**References out:** [Comments](/modules/Common.md#Common.Comment), [FormTemplates](/modules/Common.md#Common.FormTemplate)
**Referenced by:** [FormTemplateRows](/modules/Common.md#Common.FormTemplateRow)

<a id="Common.LanguageCode"></a>
### LanguageCodes

Represents a language code. Language codes are the language definitions in MONITOR.

- **Endpoint:** `GET /api/v1/Common/LanguageCodes`
- **Required permission:** Show languages
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Phrase` | `String` | no |  |

**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [Addresses](/modules/Common.md#Common.Address), [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Companies](/modules/Common.md#Common.Company), [Countries](/modules/Common.md#Common.Country), [Customers](/modules/Sales.md#Sales.Customer), [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress), [MonitoringTaskRecipients](/modules/Common.md#Common.MonitoringTaskRecipient), [Persons](/modules/Common.md#Common.Person), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [Warehouses](/modules/Common.md#Common.Warehouse)

<a id="Common.MeasuringTemplate"></a>
### MeasuringTemplates

Represents a measuring template.

- **Endpoint:** `GET /api/v1/Common/MeasuringTemplates`
- **Required permission:** Show measuring templates
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `FormTemplateId` | `Int64` | no | [FormTemplates](/modules/Common.md#Common.FormTemplate) |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `FrequencyText` | `String` | no |  |
| `IntervalAmount` | `Int32?` | yes |  |
| `Interval` | `Int32?` | yes |  |
| `MeasuringFrequency` | `Int32` | no |  |
| `Type` | `Int32` | no |  |

- `MeasuringFrequency` — First=0, Last=1, All=2, Sample=3, Other=4, PerOrder=5
- `Type` (bitmask) — None=0, Manufacturing=1, Purchase=2

**References out:** [FormTemplates](/modules/Common.md#Common.FormTemplate)
**Referenced by:** [ManufacturingOrderOperationControlDataRows](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow), [OperationRowControlDataRows](/modules/Manufacturing.md#Manufacturing.OperationRowControlDataRow), [PartPurchaseControlDataRows](/modules/Inventory.md#Inventory.PartPurchaseControlDataRow)

<a id="Common.MonitoringTaskRecipient"></a>
### MonitoringTaskRecipients

Represents a recipient for monitoring task.

- **Endpoint:** `GET /api/v1/Common/MonitoringTaskRecipients`
- **Required permission:** Create and handle all monitoring tasks
- **Introduced in:** 24.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `TaskId` | `Int64` | no | [MonitoringTasks](/modules/Common.md#Common.MonitoringTask) |
| `LanguageCodeId` | `Int64` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `RecipientType` | `Int32` | no |  |
| `Email` | `String` | no |  |
| `ApplicationUserId` | `Int64` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |

- `RecipientType` — EmailRecipient=0, NotificationRecipient=1, UserEmailRecipient=2

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [LanguageCodes](/modules/Common.md#Common.LanguageCode), [MonitoringTasks](/modules/Common.md#Common.MonitoringTask)

<a id="Common.MonitoringTaskRow"></a>
### MonitoringTaskRows

Represents a monitoring task row.

- **Endpoint:** `GET /api/v1/Common/MonitoringTaskRows`
- **Required permission:** Create and handle all monitoring tasks
- **Introduced in:** 24.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `TaskId` | `Int64` | no | [MonitoringTasks](/modules/Common.md#Common.MonitoringTask) |
| `EntityId` | `Int64` | no |  |
| `EntityType` | `Guid` | no |  |
| `ConditionType` | `Int32` | no |  |
| `Value` | `String` | no |  |
| `Message` | `String` | no |  |
| `Warehouses` | `Warehouses[]` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |

**References out:** [MonitoringTasks](/modules/Common.md#Common.MonitoringTask), [Warehouses](/modules/Common.md#Common.Warehouse)

<a id="Common.MonitoringTask"></a>
### MonitoringTasks

Represents a monitoring task.

- **Endpoint:** `GET /api/v1/Common/MonitoringTasks`
- **Required permission:** Create and handle all monitoring tasks
- **Introduced in:** 24.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `Name` | `String` | no |  |
| `TaskType` | `Int32` | no |  |
| `Status` | `Int32` | no |  |
| `UseSchedule` | `Boolean` | no |  |
| `RunOnce` | `Boolean` | no |  |
| `StartTime` | `DateTimeOffset?` | yes |  |
| `StopTime` | `DateTimeOffset?` | yes |  |
| `ApplicationUserId` | `Int64` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `ApplicationUser` | `ApplicationUsers` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `CommentId` | `Int64` | no | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

- `TaskType` — StockBalance=0, PersonActivity=1, CustomerActivity=2, QuoteActivity=3, CustomerOrderActivity=4, SupplierActivity=5, PartActivity=6, PurchaseOrderActivity=7, InquiryActivity=8, ManufacturingOrderOperation=9, ArrivalReporting=10, OrderRowArrivalReporting=11, BlanketOrderPurchaseActivity=12, BlanketOrderSalesActivity=13, SalesAgreementActivity=14, CaseEntryActivity=15, ExposureTime=16, BusinessOpportunityActivity=17, ProductRecordActivity=18, SupplierAgreementActivity=19
- `Status` — Active=0, Disabled=1

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Comments](/modules/Common.md#Common.Comment)
**Referenced by:** [MonitoringTaskRecipients](/modules/Common.md#Common.MonitoringTaskRecipient), [MonitoringTaskRows](/modules/Common.md#Common.MonitoringTaskRow)

<a id="Common.OrderTransferSetting"></a>
### OrderTransferSettings

Represents an order transfer setting.

- **Endpoint:** `GET /api/v1/Common/OrderTransferSettings`
- **Required permission:** Show setting
- **Introduced in:** 23.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ManufacturingCompanyPartIdentityTypeCode` | `String` | no |  |
| `ManufacturingCompanyUsePartOtherIdentities` | `Boolean` | no |  |
| `ManufacturingCompanyOrderOrderTypeCode` | `String` | no |  |

**Referenced by:** [TransferProfiles](/modules/Common.md#Common.TransferProfile)

<a id="Common.PartConfigurationComponentSnapshot"></a>
### PartConfigurationComponentSnapshots

Represents a part configuration component snapshot.

- **Endpoint:** `GET /api/v1/Common/PartConfigurationComponentSnapshots`
- **Required permission:** Show part
- **Introduced in:** 26.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ComponentType` | `Int32` | no |  |
| `ParentId` | `Int64` | no |  |
| `OriginComponentId` | `Int64?` | yes |  |
| `ParentRowId` | `Int64?` | yes | [PartConfigurationComponentSnapshots](/modules/Common.md#Common.PartConfigurationComponentSnapshot) |
| `RowIndex` | `Int32?` | yes |  |
| `ShowOnDocument` | `Int32?` | yes |  |
| `ShowOnFooter` | `Int32?` | yes |  |
| `Visible` | `Boolean?` | yes |  |
| `ExternalVisible` | `Boolean?` | yes |  |
| `Name` | `String` | no |  |
| `VariableType` | `Int32?` | yes |  |
| `Formula` | `String` | no |  |
| `Mandatory` | `Boolean?` | yes |  |
| `Min` | `Decimal?` | yes |  |
| `Max` | `Decimal?` | yes |  |
| `NumberOfDecimals` | `Int32?` | yes |  |
| `RoundingBase` | `Decimal?` | yes |  |
| `UnitId` | `Int64?` | yes |  |
| `ExtraFieldTemplateId` | `Int64?` | yes |  |
| `VariableId` | `Int64?` | yes |  |
| `DocumentDisplaySettings` | `Int32?` | yes |  |
| `BindPropertyType` | `Int32?` | yes |  |
| `Code` | `String` | no |  |
| `AutomaticSelectionAlternative` | `Int32?` | yes |  |
| `MaximumSelectedRows` | `Int32?` | yes |  |
| `MinimumSelectedRows` | `Int32?` | yes |  |
| `MinimumSelectedQuantity` | `Decimal?` | yes |  |
| `MaximumSelectedQuantity` | `Decimal?` | yes |  |
| `ManagedOptionsType` | `Int32?` | yes |  |
| `ManagedOptionsIdentifier` | `String` | no |  |
| `SourceVersion` | `Int32?` | yes |  |

- `ComponentType` — Section=0, Variable=1, SelectionGroup=2
- `AutomaticSelectionAlternative` — None=0, YesFirst=1, YesAll=2
- `ManagedOptionsType` — None=0, Selection=1, SelectionAndQuantity=2

**References out:** [PartConfigurationComponentSnapshots](/modules/Common.md#Common.PartConfigurationComponentSnapshot)
**Referenced by:** [PartConfigurationComponentSnapshots](/modules/Common.md#Common.PartConfigurationComponentSnapshot), [PartConfigurationSelectionGroupResults](/modules/Common.md#Common.PartConfigurationSelectionGroupResult)

<a id="Common.PartConfigurationPreset"></a>
### PartConfigurationPresets

Represents a part configuration preset.

- **Endpoint:** `GET /api/v1/Common/PartConfigurationPresets`
- **Required permission:** Show part
- **Introduced in:** 2.55

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `ChangedDate` | `DateTimeOffset?` | yes |  |
| `ChangedBy` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `CreatedDate` | `DateTimeOffset` | no |  |
| `CreatedBy` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `PartConfigurationId` | `Int64?` | yes | [PartConfigurations](/modules/Common.md#Common.PartConfiguration) |
| `Type` | `Int32` | no |  |

- `Type` — Normal=0, Temporary=1

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [PartConfigurations](/modules/Common.md#Common.PartConfiguration)

<a id="Common.PartConfigurationResult"></a>
### PartConfigurationResults

Represents a part configuration result.

- **Endpoint:** `GET /api/v1/Common/PartConfigurationResults`
- **Required permission:** Show part
- **Introduced in:** 2.55

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `TemplateId` | `Int64` | no | [PartConfigurationTemplates](/modules/Common.md#Common.PartConfigurationTemplate) |
| `MainPartId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Quantity` | `Decimal` | no |  |
| `UnitPrice` | `Decimal?` | yes |  |
| `UnitPriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `StandardPrice` | `Decimal?` | yes |  |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `UnitPriceInCompanyCurrency` | `Decimal?` | yes |  |
| `UnitPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `DiscountPercentage` | `Decimal` | no |  |
| `LockedUnitPrice` | `Boolean` | no |  |
| `LockedDiscount` | `Boolean` | no |  |
| `AlternativePreparationCode` | `String` | no |  |
| `WeightPerUnit` | `Decimal?` | yes |  |
| `IsValid` | `Boolean` | no |  |
| `PriceFormulaFactor` | `Decimal` | no |  |
| `SnapshotId` | `Int64?` | yes |  |
| `PartConfigurationId` | `Int64?` | yes | [PartConfigurations](/modules/Common.md#Common.PartConfiguration) |
| `PartCalculationId` | `Int64?` | yes |  |
| `PartConfigurationSelectionGroupResults` | `PartConfigurationSelectionGroupResults[]` | no | [PartConfigurationSelectionGroupResults](/modules/Common.md#Common.PartConfigurationSelectionGroupResult) |

**References out:** [Currencies](/modules/Common.md#Common.Currency), [PartConfigurations](/modules/Common.md#Common.PartConfiguration), [PartConfigurationSelectionGroupResults](/modules/Common.md#Common.PartConfigurationSelectionGroupResult), [PartConfigurationTemplates](/modules/Common.md#Common.PartConfigurationTemplate), [Parts](/modules/Inventory.md#Inventory.Part)
**Referenced by:** [PartConfigurations](/modules/Common.md#Common.PartConfiguration), [PartConfigurationSelectionGroupResults](/modules/Common.md#Common.PartConfigurationSelectionGroupResult)

<a id="Common.PartConfiguration"></a>
### PartConfigurations

Represents a part configuration.

- **Endpoint:** `GET /api/v1/Common/PartConfigurations`
- **Required permission:** Show part
- **Introduced in:** 2.55

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ResultId` | `Int64?` | yes | [PartConfigurationResults](/modules/Common.md#Common.PartConfigurationResult) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

**References out:** [Comments](/modules/Common.md#Common.Comment), [PartConfigurationResults](/modules/Common.md#Common.PartConfigurationResult)
**Referenced by:** [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [PartConfigurationPresets](/modules/Common.md#Common.PartConfigurationPreset), [PartConfigurationResults](/modules/Common.md#Common.PartConfigurationResult), [QuoteRows](/modules/Sales.md#Sales.QuoteRow), [RemotePartConfigurations](/modules/Common.md#Common.RemotePartConfiguration)

<a id="Common.PartConfigurationSelectionGroupResult"></a>
### PartConfigurationSelectionGroupResults

Represents a part configuration selection group result

- **Endpoint:** `GET /api/v1/Common/PartConfigurationSelectionGroupResults`
- **Required permission:** Show part
- **Introduced in:** 25.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `SelectionGroupTemplateRowId` | `Int64` | no |  |
| `RowIndex` | `Int32` | no |  |
| `SelectionGroupTemplateId` | `Int64` | no | [PartConfigurationComponentSnapshots](/modules/Common.md#Common.PartConfigurationComponentSnapshot) |
| `PartConfigurationResultId` | `Int64` | no | [PartConfigurationResults](/modules/Common.md#Common.PartConfigurationResult) |
| `Quantity` | `Decimal` | no |  |
| `SetupQuantity` | `Decimal` | no |  |
| `UnitPrice` | `Decimal?` | yes |  |
| `UnitPriceCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `UnitPriceInCompanyCurrency` | `Decimal?` | yes |  |
| `UnitPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `DiscountPercentage` | `Decimal` | no |  |
| `PriceFormulaFactor` | `Decimal` | no |  |
| `LockedUnitPrice` | `Boolean` | no |  |
| `LockedDiscount` | `Boolean` | no |  |
| `SelectedByType` | `Int32` | no |  |
| `SelectedByName` | `String` | no |  |
| `SelectionType` | `Int32` | no |  |
| `ToOperation` | `Int32?` | yes |  |
| `MainPartId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Position` | `String` | no |  |

- `SelectedByType` — User=0, Preset=1
- `SelectionType` — None=0, Initialization=5, RuleUnselect=10, Manual=20, GroupRule=30, SelectionRuleSelect=40, Locked=50, TemporaryLockedByManualSelection=60

**References out:** [Currencies](/modules/Common.md#Common.Currency), [PartConfigurationComponentSnapshots](/modules/Common.md#Common.PartConfigurationComponentSnapshot), [PartConfigurationResults](/modules/Common.md#Common.PartConfigurationResult), [Parts](/modules/Inventory.md#Inventory.Part)
**Referenced by:** [PartConfigurationResults](/modules/Common.md#Common.PartConfigurationResult)

<a id="Common.PartConfigurationTemplate"></a>
### PartConfigurationTemplates

Represents a part configuration template.

- **Endpoint:** `GET /api/v1/Common/PartConfigurationTemplates`
- **Required permission:** Show part
- **Introduced in:** 2.55

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Version` | `Int32` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

**References out:** [Comments](/modules/Common.md#Common.Comment)
**Referenced by:** [PartConfigurationResults](/modules/Common.md#Common.PartConfigurationResult), [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Common.PartialQuantity"></a>
### PartialQuantities

Represents a partial quantity.

- **Endpoint:** `GET /api/v1/Common/PartialQuantities`
- **Introduced in:** 22.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Quantity` | `Decimal` | no |  |
| `NumberOf` | `Decimal` | no |  |
| `PackagePartId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `RowIndex` | `Int32` | no |  |

**References out:** [Parts](/modules/Inventory.md#Inventory.Part)
**Referenced by:** [OrderQuantityCustomerOrders](/modules/Sales.md#Sales.OrderQuantityCustomerOrder), [OrderQuantityManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrderOperation), [OrderQuantityManufacturingOrders](/modules/Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder), [OrderQuantityPurchaseOrders](/modules/Purchase.md#Purchase.OrderQuantityPurchaseOrder), [OrderQuantityTemplates](/modules/Inventory.md#Inventory.OrderQuantityTemplate)

<a id="Common.PartUnitUsage"></a>
### PartUnitUsages

Represents a part unit usage.

- **Endpoint:** `GET /api/v1/Common/PartUnitUsages`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `UnitId` | `Int64` | no | [Units](/modules/Common.md#Common.Unit) |
| `IsRemoved` | `Boolean` | no |  |
| `ConversionFactor` | `Decimal` | no |  |
| `UsageType` | `Int32` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |

- `UsageType` (bitmask) — None=0, ManufacturingMaterialWithdrawal=1, PurchaseOrder=2, ArrivalReporting=4, CustomerOrder=8, DeliveryReporting=16, PhysicalInventoryAndStockReporting=32, StatisticalUnit=64, PackForDelivery=128

**References out:** [Parts](/modules/Inventory.md#Inventory.Part), [Units](/modules/Common.md#Common.Unit)
**Referenced by:** [Parts](/modules/Inventory.md#Inventory.Part)

<a id="Common.PaymentMethod"></a>
### PaymentMethods

Represents a queryable payment method.

- **Endpoint:** `GET /api/v1/Common/PaymentMethods`
- **Required permission:** Show terms
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `PaymentType` | `Int32` | no |  |
| `BankWebpage` | `String` | no |  |
| `CustomerIdAtBank` | `String` | no |  |
| `SendPaymentFilePath` | `String` | no |  |
| `SendPaymentDirectoryPath` | `String` | no |  |
| `CodingAccountId` | `Int64?` | yes | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `IsActive` | `Boolean` | no |  |
| `BankingFeeAccountId` | `Int64?` | yes | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `TransactionListFormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](/modules/Common.md#Common.FormReportConfiguration) |
| `ReceivingBankAccountValidation` | `Int32` | no |  |
| `ReceivingGiroAccountValidation` | `Int32` | no |  |
| `CodingAccountCodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `CodingAccountCodingEntry` | `CodingEntries` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `BankingFeeCodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `BankingFeeCodingEntry` | `CodingEntries` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |

- `PaymentType` — ManualPayment=0, ElectronicPayment=1, ElectronicIncomingPayment=2, CashPayment=3, BankIntegration=4, Factoring=5
- `ReceivingBankAccountValidation` — None=0, WarnIfMissing=1, BlockIfMissing=2
- `ReceivingGiroAccountValidation` — None=0, WarnIfMissing=1, BlockIfMissing=2

**References out:** [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry), [FormReportConfigurations](/modules/Common.md#Common.FormReportConfiguration)
**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [IncomingPayments](/modules/Accounting.md#Accounting.IncomingPayment), [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment), [PaymentTerms](/modules/Common.md#Common.PaymentTerm), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Common.PaymentPlanTemplateRow"></a>
### PaymentPlanTemplateRows

Represents a payment plan template row.

- **Endpoint:** `GET /api/v1/Common/PaymentPlanTemplateRows`
- **Required permission:** Show invoicing plan
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `UnpaidAdvanceWarningType` | `Int32?` | yes |  |
| `PaymentPlanTemplateId` | `Int64` | no | [PaymentPlanTemplates](/modules/Common.md#Common.PaymentPlanTemplate) |
| `PartialInvoiceType` | `Int32` | no |  |
| `PartId` | `Int64?` | yes | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Part` | `Parts` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `OverrideDescription` | `String` | no |  |
| `FractionOfTotal` | `Decimal` | no |  |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](/modules/Common.md#Common.PaymentTerm) |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](/modules/Common.md#Common.PaymentTerm) |
| `RowIndex` | `Int32?` | yes |  |

- `UnpaidAdvanceWarningType` — NoAlert=0, Warning=1, PreventDelivery=2
- `PartialInvoiceType` — NotInitialized=0, InAdvance=1, Delivery=2, InArrears=3, Text=4

**References out:** [Parts](/modules/Inventory.md#Inventory.Part), [PaymentPlanTemplates](/modules/Common.md#Common.PaymentPlanTemplate), [PaymentTerms](/modules/Common.md#Common.PaymentTerm)
**Referenced by:** [PaymentPlanTemplates](/modules/Common.md#Common.PaymentPlanTemplate)

<a id="Common.PaymentPlanTemplate"></a>
### PaymentPlanTemplates

Represents a payment plan template.

- **Endpoint:** `GET /api/v1/Common/PaymentPlanTemplates`
- **Required permission:** Show invoicing plan
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PaymentPlanTemplateType` | `Int32` | no |  |
| `Number` | `String` | no |  |
| `Description` | `String` | no |  |
| `IsActive` | `Boolean` | no |  |
| `InvoiceTextTypes` | `Int32` | no |  |
| `PaymentPlanTemplateRows` | `PaymentPlanTemplateRows[]` | no | [PaymentPlanTemplateRows](/modules/Common.md#Common.PaymentPlanTemplateRow) |

- `PaymentPlanTemplateType` — ForSales=1, ForPurchase=2, ForSalesAndPurchase=3
- `InvoiceTextTypes` (bitmask) — OrderRowText=1, OrderRows=2, ProjectNumberAndName=4, GoodsLabel=8, OrderAdditionalText=16, ConfigurationInfo=32, OrderRowTextInPolishOrderInfo=64, ConfigurationInfoInPolishOrderInfo=128

**References out:** [PaymentPlanTemplateRows](/modules/Common.md#Common.PaymentPlanTemplateRow)
**Referenced by:** [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [Customers](/modules/Sales.md#Sales.Customer), [PaymentPlanTemplateRows](/modules/Common.md#Common.PaymentPlanTemplateRow)

<a id="Common.PaymentTerm"></a>
### PaymentTerms

Represents a queryable payment term.

- **Endpoint:** `GET /api/v1/Common/PaymentTerms`
- **Required permission:** Show terms
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `GracePeriodInDays` | `Int32` | no |  |
| `IsFreeDeliveryMonth` | `Boolean` | no |  |
| `Method` | `Int32` | no |  |
| `AddDaysToEOM` | `Int32` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `InvoiceType` | `Int32` | no |  |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](/modules/Common.md#Common.PaymentMethod) |
| `CompanyIds` | `Int64[]` | no |  |
| `Code` | `String` | no |  |

- `Method` — Days=0, FreeDeliveryMonth=1, EOM=2
- `InvoiceType` — Standard=1, Internal=2, CashReceipt=3, Interest=4, OnAccount=5, DebitNote=6, ServiceTax=7, CorrectionInvoice=8, CollectiveCorrectionInvoice=9

**References out:** [PaymentMethods](/modules/Common.md#Common.PaymentMethod)
**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [CustomerOrderPaymentPlanRows](/modules/Sales.md#Sales.CustomerOrderPaymentPlanRow), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [CustomerOrderTypes](/modules/Sales.md#Sales.CustomerOrderType), [Customers](/modules/Sales.md#Sales.Customer), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [PaymentPlanTemplateRows](/modules/Common.md#Common.PaymentPlanTemplateRow), [PurchaseOrderInvoices](/modules/Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [Quotes](/modules/Sales.md#Sales.Quote), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement), [Suppliers](/modules/Purchase.md#Purchase.Supplier)

<a id="Common.PermissionGroup"></a>
### PermissionGroups

Represents a permission group.

- **Endpoint:** `GET /api/v1/Common/PermissionGroups`
- **Required permission:** Show user rights groups
- **Introduced in:** 22.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Permissions` | `Permissions[]` | no | [Permissions](/modules/Common.md#Common.Permission) |

**References out:** [Permissions](/modules/Common.md#Common.Permission)
**Referenced by:** [WarehousePermissions](/modules/Common.md#Common.WarehousePermission)

<a id="Common.Permission"></a>
### Permissions

Represents a permission node.

- **Endpoint:** `GET /api/v1/Common/Permissions`
- **Required permission:** Show user
- **Introduced in:** 22.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PermissionId` | `Guid` | no |  |
| `IsDenied` | `Boolean` | no |  |
| `ParentClass` | `Guid` | no |  |
| `ParentId` | `Int64` | no |  |

**Referenced by:** [PermissionGroups](/modules/Common.md#Common.PermissionGroup), [WarehousePermissions](/modules/Common.md#Common.WarehousePermission)

<a id="Common.PersonManufacturingPrintSettings"></a>
### PersonManufacturingPrintSettings

Represents manufacturing print settings for a person.

- **Endpoint:** `GET /api/v1/Common/PersonManufacturingPrintSettings`
- **Required permission:** Show person
- **Introduced in:** 2.28

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Copies` | `Int32` | no |  |
| `PrintExternalDocuments` | `Boolean` | no |  |
| `FormReportId` | `Int64` | no |  |

**Referenced by:** [Persons](/modules/Common.md#Common.Person)

<a id="Common.PersonRelative"></a>
### PersonRelatives

Represents the relative of a person.

- **Endpoint:** `GET /api/v1/Common/PersonRelatives`
- **Required permission:** Show person
- **Introduced in:** 22.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PersonId` | `Int64` | no |  |
| `Name` | `String` | no |  |

**Referenced by:** [Persons](/modules/Common.md#Common.Person)

<a id="Common.Person"></a>
### Persons

Represents a person.

- **Endpoint:** `GET /api/v1/Common/Persons`
- **Required permission:** Show person
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `BlockedContextType` | `Int32` | no |  |
| `IsRecordingEmployee` | `Boolean` | no |  |
| `EmployeeNumber` | `String` | no |  |
| `FirstName` | `String` | no |  |
| `LastName` | `String` | no |  |
| `PhoneNumber` | `String` | no |  |
| `PrivatePhoneNumber` | `String` | no |  |
| `CellPhoneNumber` | `String` | no |  |
| `PrivateCellPhoneNumber` | `String` | no |  |
| `InternalPhoneNumber` | `String` | no |  |
| `EmailAddress` | `String` | no |  |
| `PrivateEmailAddress` | `String` | no |  |
| `SkypeId` | `String` | no |  |
| `FaxNumber` | `String` | no |  |
| `Position` | `String` | no |  |
| `IsReference` | `Boolean` | no |  |
| `IsPurchaseManager` | `Boolean` | no |  |
| `IsPlanner` | `Boolean` | no |  |
| `IsAccountManager` | `Boolean` | no |  |
| `Contact` | `String` | no |  |
| `ContactPhoneNumber` | `String` | no |  |
| `ContactCellPhoneNumber` | `String` | no |  |
| `ContactEmailAddress` | `String` | no |  |
| `AddressId` | `Int64?` | yes | [Addresses](/modules/Common.md#Common.Address) |
| `Address` | `Addresses` | no | [Addresses](/modules/Common.md#Common.Address) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |
| `IsPersonBlocked` | `Boolean` | no |  |
| `PersonBlockedById` | `Int64?` | yes |  |
| `PersonBlockedDate` | `DateTimeOffset?` | yes |  |
| `CanAuthorize` | `Boolean` | no |  |
| `ApplicationUserId` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `IsSeller` | `Boolean` | no |  |
| `Initials` | `String` | no |  |
| `DepartmentId` | `Int64` | no | [Departments](/modules/Common.md#Common.Department) |
| `DistrictId` | `Int64?` | yes | [CustomerDistricts](/modules/Sales.md#Sales.CustomerDistrict) |
| `LanguageId` | `Int64` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `Category` | `String` | no |  |
| `IdentityNumber` | `String` | no |  |
| `GroupSettingsId` | `Int64?` | yes |  |
| `UseWorkCenterManufacturingPrintSettings` | `Boolean` | no |  |
| `ManufacturingPrintSettings` | `PersonManufacturingPrintSettings[]` | no | [PersonManufacturingPrintSettings](/modules/Common.md#Common.PersonManufacturingPrintSettings) |
| `PlannedAbsences` | `PlannedAbsences[]` | no | [PlannedAbsences](/modules/TimeRecording.md#TimeRecording.PlannedAbsence) |
| `TimeBanks` | `PersonTimeBanks[]` | no | [PersonTimeBanks](/modules/TimeRecording.md#TimeRecording.PersonTimeBank) |
| `Relatives` | `PersonRelatives[]` | no | [PersonRelatives](/modules/Common.md#Common.PersonRelative) |
| `EmploymentPeriods` | `EmploymentPeriods[]` | no | [EmploymentPeriods](/modules/Common.md#Common.EmploymentPeriod) |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](/modules/Common.md#Common.ExtraField) |
| `IsProjectManager` | `Boolean` | no |  |
| `AvailableWorkshopSchedules` | `Schedules[]` | no | [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule) |
| `AvailableWorkCenters` | `PersonWorkCenters[]` | no | [PersonWorkCenters](/modules/TimeRecording.md#TimeRecording.PersonWorkCenter) |
| `Signature` | `BlobData` | no | [BlobData](/modules/Common.md#Common.BlobData) |
| `EmployeeRecordingType` | `Int32` | no |  |
| `ScheduleManagementType` | `Int32` | no |  |
| `PersonScheduleCycles` | `PersonScheduleCycles[]` | no |  |
| `AttendanceRecordingAuthorizers` | `AttendanceRecordingAuthorizers[]` | no |  |
| `WorkMethod` | `Int32` | no |  |

- `BlockedContextType` (bitmask) — None=0, RegisterCustomerOrder=1
- `EmployeeRecordingType` (bitmask) — None=0, AttendanceAndWork=1, OnlyWork=2
- `ScheduleManagementType` (bitmask) — None=0, ScheduleCycle=1
- `WorkMethod` — OnlyChange=0, StartFinishAtWill=1

**References out:** [Addresses](/modules/Common.md#Common.Address), [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [BlobData](/modules/Common.md#Common.BlobData), [Comments](/modules/Common.md#Common.Comment), [CustomerDistricts](/modules/Sales.md#Sales.CustomerDistrict), [Departments](/modules/Common.md#Common.Department), [EmploymentPeriods](/modules/Common.md#Common.EmploymentPeriod), [ExtraFields](/modules/Common.md#Common.ExtraField), [LanguageCodes](/modules/Common.md#Common.LanguageCode), [PersonManufacturingPrintSettings](/modules/Common.md#Common.PersonManufacturingPrintSettings), [PersonRelatives](/modules/Common.md#Common.PersonRelative), [PersonTimeBanks](/modules/TimeRecording.md#TimeRecording.PersonTimeBank), [PersonWorkCenters](/modules/TimeRecording.md#TimeRecording.PersonWorkCenter), [PlannedAbsences](/modules/TimeRecording.md#TimeRecording.PlannedAbsence), [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [AttendanceChart](/modules/TimeRecording.md#TimeRecording.AttendanceChart), [BlanketOrderPurchases](/modules/Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderSales](/modules/Sales.md#Sales.BlanketOrderSales), [BusinessOpportunities](/modules/Sales.md#Sales.BusinessOpportunity), [BusinessOpportunityActivities](/modules/Sales.md#Sales.BusinessOpportunityActivity), [BusinessOpportunitySalesProcessSteps](/modules/Sales.md#Sales.BusinessOpportunitySalesProcessStep), [BusinessOpportunityTypes](/modules/Sales.md#Sales.BusinessOpportunityType), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CreateSalesPickingList](/modules/Sales.md#Sales.CreateSalesPickingList), [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [Customers](/modules/Sales.md#Sales.Customer), [DelegatedWork](/modules/Common.md#Common.DelegatedWork), [EmploymentPeriods](/modules/Common.md#Common.EmploymentPeriod), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [MaintenanceReportings](/modules/Manufacturing.md#Manufacturing.MaintenanceReporting), [ManufacturingOrderOperationReportings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingPickingLists](/modules/Manufacturing.md#Manufacturing.ManufacturingPickingList), [PartPlanningInformation](/modules/Inventory.md#Inventory.PartPlanningInformation), [Parts](/modules/Inventory.md#Inventory.Part), [PartTemplates](/modules/Inventory.md#Inventory.PartTemplate), [PersonTimeBanks](/modules/TimeRecording.md#TimeRecording.PersonTimeBank), [PersonWorkCenters](/modules/TimeRecording.md#TimeRecording.PersonWorkCenter), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [ProjectActivityCalendarAppointments](/modules/Common.md#Common.ProjectActivityCalendarAppointment), [Projects](/modules/Common.md#Common.Project), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange), [Quotes](/modules/Sales.md#Sales.Quote), [RecordingDays](/modules/TimeRecording.md#TimeRecording.RecordingDay), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement), [SalesPickingLists](/modules/Sales.md#Sales.SalesPickingList), [SalesProcessTemplateRows](/modules/Sales.md#Sales.SalesProcessTemplateRow), [ShipmentCustoms](/modules/Sales.md#Sales.ShipmentCustoms), [StandbyWorks](/modules/TimeRecording.md#TimeRecording.StandbyWork), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [WorkIntervals](/modules/TimeRecording.md#TimeRecording.WorkInterval)

<a id="Common.PriceList"></a>
### PriceLists

Represents a price list.

- **Endpoint:** `GET /api/v1/Common/PriceLists`
- **Required permission:** Show price lists
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `ConversionFactor` | `Decimal` | no |  |
| `ParentPriceListId` | `Int64?` | yes | [PriceLists](/modules/Common.md#Common.PriceList) |
| `CurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `PriceListBasis` | `Int32` | no |  |
| `CompanyIds` | `Int64[]` | no |  |

- `PriceListBasis` — None=0, ParentPriceList=1, StandardPrice=2

**References out:** [Currencies](/modules/Common.md#Common.Currency), [PriceLists](/modules/Common.md#Common.PriceList)
**Referenced by:** [BlanketOrderPurchaseRows](/modules/Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderSalesRows](/modules/Sales.md#Sales.BlanketOrderSalesRow), [BlanketOrderSalesTypes](/modules/Sales.md#Sales.BlanketOrderSalesType), [CustomerOrderTypes](/modules/Sales.md#Sales.CustomerOrderType), [Customers](/modules/Sales.md#Sales.Customer), [PriceChangeLogs](/modules/Inventory.md#Inventory.PriceChangeLog), [PriceLists](/modules/Common.md#Common.PriceList), [QuoteTypes](/modules/Sales.md#Sales.QuoteType), [SalesAgreementTypes](/modules/Sales.md#Sales.SalesAgreementType), [SalesPrices](/modules/Sales.md#Sales.SalesPrice)

<a id="Common.Probability"></a>
### Probabilities

Represents a probability.

- **Endpoint:** `GET /api/v1/Common/Probabilities`
- **Required permission:** Show probability codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Percentage` | `Decimal?` | yes |  |
| `IsPreset` | `Boolean` | no |  |

**Referenced by:** [Customers](/modules/Sales.md#Sales.Customer), [Quotes](/modules/Sales.md#Sales.Quote)

<a id="Common.ProductGroup"></a>
### ProductGroups

Represents a product group.

- **Endpoint:** `GET /api/v1/Common/ProductGroups`
- **Required permission:** Show posting matrix
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `Description` | `String` | no |  |
| `Alias` | `String` | no |  |
| `IsDefault` | `Boolean` | no |  |

**Referenced by:** [DiscountCategoryRows](/modules/Common.md#Common.DiscountCategoryRow), [Parts](/modules/Inventory.md#Inventory.Part), [PartTemplates](/modules/Inventory.md#Inventory.PartTemplate)

<a id="Common.ProjectActivity"></a>
### ProjectActivities

Represents a project activity.

- **Endpoint:** `GET /api/v1/Common/ProjectActivities`
- **Required permission:** Show Activity list – Project
- **Introduced in:** 2.36

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `ReportedTimeInHours` | `Decimal` | no |  |
| `RestTimeInHours` | `Decimal` | no |  |
| `PlannedTimeInHours` | `Decimal` | no |  |
| `ShowInProjectReport` | `Boolean` | no |  |
| `ParentId` | `Int64` | no | [ProjectPhases](/modules/Common.md#Common.ProjectPhase) |
| `LockedDelegateWork` | `Boolean` | no |  |
| `ActivityTypeId` | `Int64` | no | [ProjectActivityTypes](/modules/Common.md#Common.ProjectActivityType) |
| `ActivityType` | `ProjectActivityTypes` | no | [ProjectActivityTypes](/modules/Common.md#Common.ProjectActivityType) |
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
| `Mandatory` | `Boolean` | no |  |
| `CalendarAppointmentId` | `String` | no |  |

- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Comments](/modules/Common.md#Common.Comment), [ProjectActivityTypes](/modules/Common.md#Common.ProjectActivityType), [ProjectPhases](/modules/Common.md#Common.ProjectPhase)
**Referenced by:** [DelegatedWork](/modules/Common.md#Common.DelegatedWork), [ProjectActivityCalendarAppointments](/modules/Common.md#Common.ProjectActivityCalendarAppointment), [ProjectActivityRelations](/modules/Common.md#Common.ProjectActivityRelation), [ProjectPhases](/modules/Common.md#Common.ProjectPhase), [WorkIntervals](/modules/TimeRecording.md#TimeRecording.WorkInterval)

<a id="Common.ProjectActivityCalendarAppointment"></a>
### ProjectActivityCalendarAppointments

Represents a Project Activity Calendar Appointment.

- **Endpoint:** `GET /api/v1/Common/ProjectActivityCalendarAppointments`
- **Required permission:** Show projects
- **Introduced in:** 25.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ProjectActivityId` | `Int64?` | yes | [ProjectActivities](/modules/Common.md#Common.ProjectActivity) |
| `SenderPersonId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `CalendarAppointmentId` | `String` | no |  |

**References out:** [Persons](/modules/Common.md#Common.Person), [ProjectActivities](/modules/Common.md#Common.ProjectActivity)

<a id="Common.ProjectActivityRelation"></a>
### ProjectActivityRelations

Represents a relation between two project activities.

- **Endpoint:** `GET /api/v1/Common/ProjectActivityRelations`
- **Required permission:** Show Activity list – Project
- **Introduced in:** 2.50

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no | [ProjectActivities](/modules/Common.md#Common.ProjectActivity) |
| `DependentOnEntityId` | `Int64` | no | [ProjectActivities](/modules/Common.md#Common.ProjectActivity) |
| `Type` | `Int32` | no |  |
| `RowIndex` | `Int32` | no |  |

- `Type` — FinishedBeforeStart=0, StartedBeforeStart=1

**References out:** [ProjectActivities](/modules/Common.md#Common.ProjectActivity)

<a id="Common.ProjectActivityType"></a>
### ProjectActivityTypes

Represents a project activity type.

- **Endpoint:** `GET /api/v1/Common/ProjectActivityTypes`
- **Required permission:** Show basic data for project
- **Introduced in:** 2.36

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `PlannedTimeInHours` | `Decimal` | no |  |
| `LeadTimeInDays` | `Int32` | no |  |
| `QueueTimeInDays` | `Int32` | no |  |
| `CostTypeId` | `Int64` | no |  |
| `IsActive` | `Boolean` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `UseReminder` | `Boolean` | no |  |
| `ShowInProjectReport` | `Boolean` | no |  |
| `Code` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `IsReportedAsDirectTime` | `Boolean` | no |  |

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Comments](/modules/Common.md#Common.Comment)
**Referenced by:** [ProjectActivities](/modules/Common.md#Common.ProjectActivity)

<a id="Common.ProjectAggregate"></a>
### ProjectAggregates

Represents a project aggregate.

- **Endpoint:** `GET /api/v1/Common/ProjectAggregates`
- **Required permission:** Show projects
- **Introduced in:** 2.46

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ProjectId` | `Int64?` | yes | [Projects](/modules/Common.md#Common.Project) |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](/modules/Common.md#Common.ProjectCostType) |
| `ExpectedResultCost` | `Decimal` | no |  |
| `ExpectedResultIncome` | `Decimal` | no |  |
| `ExpectedResultTime` | `Decimal` | no |  |
| `ResultCost` | `Decimal` | no |  |
| `ResultIncome` | `Decimal` | no |  |
| `ResultTime` | `Decimal` | no |  |

**References out:** [ProjectCostTypes](/modules/Common.md#Common.ProjectCostType), [Projects](/modules/Common.md#Common.Project)
**Referenced by:** [Projects](/modules/Common.md#Common.Project)

<a id="Common.ProjectCostBudget"></a>
### ProjectCostBudgets

Represents a project cost budget.

- **Endpoint:** `GET /api/v1/Common/ProjectCostBudgets`
- **Required permission:** Show projects
- **Introduced in:** 2.46

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ProjectId` | `Int64?` | yes | [Projects](/modules/Common.md#Common.Project) |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](/modules/Common.md#Common.ProjectCostType) |
| `Hours` | `Decimal` | no |  |
| `Cost` | `Decimal` | no |  |
| `Income` | `Decimal` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

**References out:** [Comments](/modules/Common.md#Common.Comment), [ProjectCostTypes](/modules/Common.md#Common.ProjectCostType), [Projects](/modules/Common.md#Common.Project)
**Referenced by:** [Projects](/modules/Common.md#Common.Project)

<a id="Common.ProjectCostForecast"></a>
### ProjectCostForecasts

Represents a project cost forecast.

- **Endpoint:** `GET /api/v1/Common/ProjectCostForecasts`
- **Required permission:** Show projects
- **Introduced in:** 2.46

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ProjectId` | `Int64?` | yes | [Projects](/modules/Common.md#Common.Project) |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](/modules/Common.md#Common.ProjectCostType) |
| `Hours` | `Decimal` | no |  |
| `Cost` | `Decimal` | no |  |
| `Income` | `Decimal` | no |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

**References out:** [Comments](/modules/Common.md#Common.Comment), [ProjectCostTypes](/modules/Common.md#Common.ProjectCostType), [Projects](/modules/Common.md#Common.Project)
**Referenced by:** [Projects](/modules/Common.md#Common.Project)

<a id="Common.ProjectCostReportingEntry"></a>
### ProjectCostReportingEntries

Represents a project cost reporting entry.

- **Endpoint:** `GET /api/v1/Common/ProjectCostReportingEntries`
- **Required permission:** Report activity for any user
- **Introduced in:** 2.50

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `ProjectId` | `Int64?` | yes |  |
| `IsIncome` | `Boolean` | no |  |
| `ActivityId` | `Int64?` | yes |  |
| `ReportedTimeInHours` | `Decimal` | no |  |
| `CostTypeId` | `Int64?` | yes |  |
| `Amount` | `Decimal` | no |  |
| `ReportingDate` | `DateTimeOffset` | no |  |
| `OurReferenceId` | `Int64?` | yes |  |
| `OurReferenceName` | `String` | no |  |
| `EmployeeId` | `Int64?` | yes |  |
| `WorkCenterId` | `Int64?` | yes |  |
| `DepartmentId` | `Int64?` | yes |  |
| `IsCancelled` | `Boolean` | no |  |
| `CommentId` | `Int64?` | yes |  |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CustomerReference` | `String` | no |  |
| `CustomerOrderNumber` | `String` | no |  |
| `GoodsMark` | `String` | no |  |
| `InternalCommentId` | `Int64?` | yes |  |
| `InternalComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

**References out:** [Comments](/modules/Common.md#Common.Comment)

<a id="Common.ProjectCostType"></a>
### ProjectCostTypes

Represents a project cost type.

- **Endpoint:** `GET /api/v1/Common/ProjectCostTypes`
- **Required permission:** Show projects
- **Introduced in:** 2.46

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Type` | `Int32` | no |  |

- `Type` — Cost=1, Income=2

**Referenced by:** [AttendanceAdditions](/modules/TimeRecording.md#TimeRecording.AttendanceAddition), [ProjectAggregates](/modules/Common.md#Common.ProjectAggregate), [ProjectCostBudgets](/modules/Common.md#Common.ProjectCostBudget), [ProjectCostForecasts](/modules/Common.md#Common.ProjectCostForecast)

<a id="Common.ProjectGroup"></a>
### ProjectGroups

Represents a project group.

- **Endpoint:** `GET /api/v1/Common/ProjectGroups`
- **Required permission:** Show basic data for project
- **Introduced in:** 24.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [Projects](/modules/Common.md#Common.Project)

<a id="Common.ProjectPhase"></a>
### ProjectPhases

Represents a project phase.

- **Endpoint:** `GET /api/v1/Common/ProjectPhases`
- **Required permission:** Show Activity list – Project
- **Introduced in:** 2.36

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Number` | `Int64` | no |  |
| `PhaseTypeId` | `Int64` | no | [ProjectPhaseTypes](/modules/Common.md#Common.ProjectPhaseType) |
| `PhaseType` | `ProjectPhaseTypes` | no | [ProjectPhaseTypes](/modules/Common.md#Common.ProjectPhaseType) |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `ParentId` | `Int64` | no | [Projects](/modules/Common.md#Common.Project) |
| `IsDummy` | `Boolean` | no |  |
| `RowIndex` | `Int32` | no |  |
| `Activities` | `ProjectActivities[]` | no | [ProjectActivities](/modules/Common.md#Common.ProjectActivity) |

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [ProjectActivities](/modules/Common.md#Common.ProjectActivity), [ProjectPhaseTypes](/modules/Common.md#Common.ProjectPhaseType), [Projects](/modules/Common.md#Common.Project)
**Referenced by:** [ProjectActivities](/modules/Common.md#Common.ProjectActivity), [Projects](/modules/Common.md#Common.Project)

<a id="Common.ProjectPhaseType"></a>
### ProjectPhaseTypes

Represents a project phase type.

- **Endpoint:** `GET /api/v1/Common/ProjectPhaseTypes`
- **Required permission:** Show basic data for project
- **Introduced in:** 2.36

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `ManagerId` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |

**References out:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser)
**Referenced by:** [ProjectPhases](/modules/Common.md#Common.ProjectPhase)

<a id="Common.Project"></a>
### Projects

Represents a project.

- **Endpoint:** `GET /api/v1/Common/Projects`
- **Required permission:** Show projects
- **Introduced in:** 2.31

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `Priority` | `Int32` | no |  |
| `StartDate` | `DateTimeOffset` | no |  |
| `EndDate` | `DateTimeOffset` | no |  |
| `CustomerId` | `Int64?` | yes | [Customers](/modules/Sales.md#Sales.Customer) |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) |
| `CustomerOrderNumber` | `String` | no |  |
| `SellerId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `Seller` | `Persons` | no | [Persons](/modules/Common.md#Common.Person) |
| `OurReferenceId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |
| `OurReference` | `Persons` | no | [Persons](/modules/Common.md#Common.Person) |
| `CustomerReferenceId` | `Int64?` | yes | [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference) |
| `CustomerReference` | `BusinessContactReferences` | no | [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference) |
| `InternalCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `InternalComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `ExternalCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `ExternalComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `LongDescription` | `String` | no |  |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](/modules/Common.md#Common.ExtraField) |
| `Phases` | `ProjectPhases[]` | no | [ProjectPhases](/modules/Common.md#Common.ProjectPhase) |
| `ProjectTypeId` | `Int64` | no | [ProjectTypes](/modules/Common.md#Common.ProjectType) |
| `ProjectType` | `ProjectTypes` | no | [ProjectTypes](/modules/Common.md#Common.ProjectType) |
| `ProjectGroupId` | `Int64?` | yes | [ProjectGroups](/modules/Common.md#Common.ProjectGroup) |
| `ProjectGroup` | `ProjectGroups` | no | [ProjectGroups](/modules/Common.md#Common.ProjectGroup) |
| `ProjectCostBudgets` | `ProjectCostBudgets[]` | no | [ProjectCostBudgets](/modules/Common.md#Common.ProjectCostBudget) |
| `ProjectCostForecasts` | `ProjectCostForecasts[]` | no | [ProjectCostForecasts](/modules/Common.md#Common.ProjectCostForecast) |
| `ProjectAggregates` | `ProjectAggregates[]` | no | [ProjectAggregates](/modules/Common.md#Common.ProjectAggregate) |
| `ParentProjectId` | `Int64?` | yes | [Projects](/modules/Common.md#Common.Project) |
| `ProjectManagerId` | `Int64?` | yes | [Persons](/modules/Common.md#Common.Person) |

- `Status` — Registered=1, InProgress=3, Finished=4, Standby=6, History=9

**References out:** [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference), [Comments](/modules/Common.md#Common.Comment), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [Customers](/modules/Sales.md#Sales.Customer), [ExtraFields](/modules/Common.md#Common.ExtraField), [Persons](/modules/Common.md#Common.Person), [ProjectAggregates](/modules/Common.md#Common.ProjectAggregate), [ProjectCostBudgets](/modules/Common.md#Common.ProjectCostBudget), [ProjectCostForecasts](/modules/Common.md#Common.ProjectCostForecast), [ProjectGroups](/modules/Common.md#Common.ProjectGroup), [ProjectPhases](/modules/Common.md#Common.ProjectPhase), [Projects](/modules/Common.md#Common.Project), [ProjectTypes](/modules/Common.md#Common.ProjectType)
**Referenced by:** [AdditionRecordings](/modules/TimeRecording.md#TimeRecording.AdditionRecording), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](/modules/Inventory.md#Inventory.Part), [ProjectAggregates](/modules/Common.md#Common.ProjectAggregate), [ProjectCostBudgets](/modules/Common.md#Common.ProjectCostBudget), [ProjectCostForecasts](/modules/Common.md#Common.ProjectCostForecast), [ProjectPhases](/modules/Common.md#Common.ProjectPhase), [Projects](/modules/Common.md#Common.Project), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement)

<a id="Common.ProjectType"></a>
### ProjectTypes

Represents a project type.

- **Endpoint:** `GET /api/v1/Common/ProjectTypes`
- **Required permission:** Show basic data for project
- **Introduced in:** 2.43

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [Projects](/modules/Common.md#Common.Project)

<a id="Common.ReasonCodeDebitNote"></a>
### ReasonCodeDebitNotes

Represents a reason code for debit note.

- **Endpoint:** `GET /api/v1/Common/ReasonCodeDebitNotes`
- **Required permission:** Show cause codes
- **Introduced in:** 25.6

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `Active` | `Boolean` | no |  |

**Referenced by:** [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder)

<a id="Common.ReasonCode"></a>
### ReasonCodes

Represents a reason code.

- **Endpoint:** `GET /api/v1/Common/ReasonCodes`
- **Required permission:** Show cause codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Type` | `Int32` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `CommentMandatory` | `Boolean` | no |  |
| `Active` | `Boolean` | no |  |

- `Type` (bitmask) — All=0, PurchaseOrder=1, ManufacturingOrder=2

**Referenced by:** [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow)

<a id="Common.RejectionCodeItem"></a>
### RejectionCodeItems

Represents a rejection code.

- **Endpoint:** `GET /api/v1/Common/RejectionCodeItems`
- **Required permission:** Show rejection codes/cause codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `Active` | `Boolean` | no |  |
| `ForcedComment` | `Boolean` | no |  |
| `Type` | `Int32` | no |  |

- `Type` (bitmask) — None=0, ManufacturingReporting=1, ReceivingInspectionPurchase=2, CustomerNonConformity=4, SupplierNonConformity=8, InternalNonConformity=16, Standard8DNonConformity=32

**Referenced by:** [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CaseEntryPartLinks](/modules/Inventory.md#Inventory.CasePartLink)

<a id="Common.RemotePartConfigurationRow"></a>
### RemotePartConfigurationRows

Represents a remote part configuration row.

- **Endpoint:** `GET /api/v1/Common/RemotePartConfigurationRows`
- **Required permission:** Show part
- **Introduced in:** 24.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no |  |
| `ManualPriceOrDiscount` | `Boolean` | no |  |
| `PriceEach` | `Decimal` | no |  |
| `Discount` | `Decimal` | no |  |
| `CurrencyCode` | `String` | no |  |

**Referenced by:** [RemotePartConfigurations](/modules/Common.md#Common.RemotePartConfiguration)

<a id="Common.RemotePartConfiguration"></a>
### RemotePartConfigurations

Represents a remote part configuration.

- **Endpoint:** `GET /api/v1/Common/RemotePartConfigurations`
- **Required permission:** Show part
- **Introduced in:** 24.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartConfigurationIdInRemoteCompany` | `Int64` | no | [PartConfigurations](/modules/Common.md#Common.PartConfiguration) |
| `Rows` | `RemotePartConfigurationRows[]` | no | [RemotePartConfigurationRows](/modules/Common.md#Common.RemotePartConfigurationRow) |

**References out:** [PartConfigurations](/modules/Common.md#Common.PartConfiguration), [RemotePartConfigurationRows](/modules/Common.md#Common.RemotePartConfigurationRow)

<a id="Common.Reseller"></a>
### Resellers

Represents a reseller.

- **Endpoint:** `GET /api/v1/Common/Resellers`
- **Required permission:** Show customer
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `Provision` | `Decimal` | no |  |

**Referenced by:** [Customers](/modules/Sales.md#Sales.Customer)

<a id="Common.Revision"></a>
### Revisions

Represents a revision.

- **Endpoint:** `GET /api/v1/Common/Revisions`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `ValidFrom` | `DateTimeOffset?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |

**References out:** [Comments](/modules/Common.md#Common.Comment), [Parts](/modules/Inventory.md#Inventory.Part)
**Referenced by:** [BlanketOrderPurchaseRows](/modules/Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderSalesRows](/modules/Sales.md#Sales.BlanketOrderSalesRow), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CaseEntryPartLinks](/modules/Inventory.md#Inventory.CasePartLink), [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [InquiryRows](/modules/Purchase.md#Purchase.InquiryRow), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode), [PartLocations](/modules/Inventory.md#Inventory.PartLocation), [Parts](/modules/Inventory.md#Inventory.Part), [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](/modules/Sales.md#Sales.QuoteRow), [SalesAgreementRows](/modules/Sales.md#Sales.SalesAgreementRow)

<a id="Common.Role"></a>
### Roles

Represents a user role.

- **Endpoint:** `GET /api/v1/Common/Roles`
- **Required permission:** Show user
- **Introduced in:** 22.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `IsSuperUser` | `Boolean` | no |  |

**Referenced by:** [WarehousePermissions](/modules/Common.md#Common.WarehousePermission)

<a id="Common.ServerPrinter"></a>
### ServerPrinters

Represents a server printer that can be used to print documents via the MONITOR server.

- **Endpoint:** `GET /api/v1/Common/ServerPrinters`
- **Introduced in:** 2.52

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `Description` | `String` | no |  |
| `Name` | `String` | no |  |
| `Orientation` | `Int32` | no |  |
| `DuplexMode` | `Int32` | no |  |
| `PaperSize` | `Int32` | no |  |
| `Width` | `Int32` | no |  |
| `Height` | `Int32` | no |  |
| `ColorMode` | `Int32` | no |  |
| `FilePathId` | `Int64?` | yes | [FilePaths](/modules/Common.md#Common.FilePath) |
| `FilePath` | `FilePaths` | no | [FilePaths](/modules/Common.md#Common.FilePath) |
| `SubPath` | `String` | no | [FilePaths](/modules/Common.md#Common.FilePath) |

- `Orientation` — Portrait=0, Landscape=1, Auto=2
- `DuplexMode` — None=0, LongEdge=1, ShortEdge=2
- `PaperSize` — A4=0, A3=1, A5=2, Custom=3, PrinterDefault=4, Letter=5
- `ColorMode` — BlackAndWhite=0, FullColor=1

**References out:** [FilePaths](/modules/Common.md#Common.FilePath)
**Referenced by:** [ApplicationUserPrinters](/modules/Common.md#Common.ApplicationUserPrinter)

<a id="Common.StaggeredPrice"></a>
### StaggeredPrices

Represents a staggered price.

- **Endpoint:** `GET /api/v1/Common/StaggeredPrices`
- **Required permission:** Show part
- **Introduced in:** 2.34

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PartId` | `Int64` | no | [Parts](/modules/Inventory.md#Inventory.Part) |
| `Price` | `Decimal` | no |  |
| `LowerBoundaryQuantity` | `Decimal` | no |  |
| `FuturePrice` | `Decimal?` | yes |  |
| `ShippingPrice` | `Decimal` | no |  |
| `ParentClass` | `Guid` | no |  |
| `ParentId` | `Int64` | no |  |

**References out:** [Parts](/modules/Inventory.md#Inventory.Part)
**Referenced by:** [CustomerPartLinks](/modules/Sales.md#Sales.CustomerPartLink), [SalesPrices](/modules/Sales.md#Sales.SalesPrice)

<a id="Common.StatisticalGoodsCode"></a>
### StatisticalGoodsCodes

Represents a queryable statistical goods code.

- **Endpoint:** `GET /api/v1/Common/StatisticalGoodsCodes`
- **Required permission:** Show CN codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `DeclarationType` | `Int32` | no |  |

- `DeclarationType` — Weight=1, OtherQuantity=2, WeightAndOtherQuantity=3, ExcludeFromDeclaration=4

**Referenced by:** [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [InquiryRows](/modules/Purchase.md#Purchase.InquiryRow), [Parts](/modules/Inventory.md#Inventory.Part), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](/modules/Sales.md#Sales.QuoteRow), [ShipmentCustomsRows](/modules/Sales.md#Sales.ShipmentCustomsRow)

<a id="Common.Tag"></a>
### Tags

Represents a tag.

- **Endpoint:** `GET /api/v1/Common/Tags`
- **Required permission:** Show part
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `OwnerTypeId` | `Guid` | no |  |
| `OwnerId` | `Int64` | no |  |
| `Name` | `String` | no |  |


<a id="Common.TariffAndServiceCode"></a>
### TariffAndServiceCodes

Represents a tariff and service code.

- **Endpoint:** `GET /api/v1/Common/TariffAndServiceCodes`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Name` | `String` | no |  |
| `Type` | `Int32?` | yes |  |
| `IsActive` | `Boolean` | no |  |

- `Type` — Sales=1, Service=2, Purchase=3

**Referenced by:** [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow)

<a id="Common.TransactionTypeIntrastat"></a>
### TransactionTypeIntrastats

Represents a transaction type intrastat.

- **Endpoint:** `GET /api/v1/Common/TransactionTypeIntrastats`
- **Required permission:** Show transaction types
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow)

<a id="Common.TransferProfile"></a>
### TransferProfiles

Represents a transfer profile.

- **Endpoint:** `GET /api/v1/Common/TransferProfiles`
- **Required permission:** Show transfer profile
- **Introduced in:** 22.1

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `Usages` | `Int32` | no |  |
| `TargetRole` | `Int32` | no |  |
| `IsVerified` | `Boolean` | no |  |
| `IsActive` | `Boolean` | no |  |
| `ConnectionProfileId` | `Int64` | no | [ConnectionProfiles](/modules/Common.md#Common.ConnectionProfile) |
| `RemoteWarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `OrderTransferSettingsId` | `Int64` | no | [OrderTransferSettings](/modules/Common.md#Common.OrderTransferSetting) |
| `SupplierId` | `Int64?` | yes | [Suppliers](/modules/Purchase.md#Purchase.Supplier) |
| `CustomerCode` | `String` | no |  |

- `Usages` (bitmask) — None=0, CustomerOrderTransfer=1, PartSynchronization=2, PartInformation=4
- `TargetRole` — ManufacturingCompany=0, SalesCompany=1

**References out:** [ConnectionProfiles](/modules/Common.md#Common.ConnectionProfile), [OrderTransferSettings](/modules/Common.md#Common.OrderTransferSetting), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [CustomerOrderTypes](/modules/Sales.md#Sales.CustomerOrderType), [PartPlanningInformation](/modules/Inventory.md#Inventory.PartPlanningInformation), [QuoteRows](/modules/Sales.md#Sales.QuoteRow)

<a id="Common.Unit"></a>
### Units

Represents a quantity unit.

- **Endpoint:** `GET /api/v1/Common/Units`
- **Required permission:** Show units
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `Number` | `Int64` | no |  |

**Referenced by:** [Alloys](/modules/Inventory.md#Inventory.Alloy), [BlanketOrderPurchaseRows](/modules/Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderSalesRows](/modules/Sales.md#Sales.BlanketOrderSalesRow), [CompanyEmissionDetails](/modules/Common.md#Common.CompanyEmissionDetail), [CustomerOrderRowInflows](/modules/Sales.md#Sales.CustomerOrderRowInflow), [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [CustomerPartLinks](/modules/Sales.md#Sales.CustomerPartLink), [FormTemplateRows](/modules/Common.md#Common.FormTemplateRow), [InquiryRows](/modules/Purchase.md#Purchase.InquiryRow), [MaintenanceReportingRows](/modules/Manufacturing.md#Manufacturing.MaintenanceReportingRow), [Parts](/modules/Inventory.md#Inventory.Part), [PartUnitUsages](/modules/Common.md#Common.PartUnitUsage), [PurchaseOrderAdviceRows](/modules/Purchase.md#Purchase.PurchaseOrderAdviceRow), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](/modules/Sales.md#Sales.QuoteRow), [SalesAgreementBasisRows](/modules/Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRows](/modules/Sales.md#Sales.SalesAgreementRow), [SalesForecastRows](/modules/Inventory.md#Inventory.SalesForecastRow), [ShipmentCustomsRows](/modules/Sales.md#Sales.ShipmentCustomsRow), [SupplierPartLinks](/modules/Purchase.md#Purchase.SupplierPartLink)

<a id="Common.VatGroup"></a>
### VatGroups

Represents a VAT group.

- **Endpoint:** `GET /api/v1/Common/VatGroups`
- **Required permission:** Show VAT settings
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `DefaultVatRateForPurchaseId` | `Int64` | no | [VatRates](/modules/Common.md#Common.VatRate) |
| `DefaultVatRateForSalesId` | `Int64` | no | [VatRates](/modules/Common.md#Common.VatRate) |
| `DefaultVatRateId` | `Int64` | no | [VatRates](/modules/Common.md#Common.VatRate) |

**References out:** [VatRates](/modules/Common.md#Common.VatRate)
**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [Countries](/modules/Common.md#Common.Country), [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [PurchaseOrderInvoices](/modules/Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [Quotes](/modules/Sales.md#Sales.Quote), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement)

<a id="Common.VatRate"></a>
### VatRates

Represents a VAT rate.

- **Endpoint:** `GET /api/v1/Common/VatRates`
- **Required permission:** Show VAT settings
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Percentage` | `Decimal` | no |  |
| `Description` | `String` | no |  |
| `ReversedTax` | `Boolean` | no |  |
| `OutputVatAccountId` | `Int64?` | yes | [Accounts](/modules/Accounting.md#Accounting.Account) |
| `InputVatAccountId` | `Int64?` | yes | [Accounts](/modules/Accounting.md#Accounting.Account) |
| `Active` | `Boolean` | no |  |
| `ReversedTaxPercentage` | `Decimal` | no |  |
| `ReferenceTextId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `ReferenceText` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `Reference` | `String` | no |  |
| `EcSalesType` | `Int32?` | yes |  |
| `CodeType` | `Int32` | no |  |
| `DatevVatCode` | `Int64?` | yes |  |

- `EcSalesType` — Goods trade=1, Services=2, Third party trade=3, GoodsTrade=1, Services=2, ThirdPartyTrade=3
- `CodeType` (bitmask) — None=0, Sales=1, Purchase=2

**References out:** [Accounts](/modules/Accounting.md#Accounting.Account), [Comments](/modules/Common.md#Common.Comment)
**Referenced by:** [AccountYearSettings](/modules/Accounting.md#Accounting.AccountYearSetting), [BlanketOrderPurchaseRows](/modules/Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderSalesRows](/modules/Sales.md#Sales.BlanketOrderSalesRow), [BookingRows](/modules/Accounting.md#Accounting.BookingRow), [CustomerOrderInvoiceRows](/modules/Sales.md#Sales.CustomerOrderInvoiceRow), [CustomerOrderPaymentPlanRows](/modules/Sales.md#Sales.CustomerOrderPaymentPlanRow), [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [Customers](/modules/Sales.md#Sales.Customer), [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress), [InquiryRows](/modules/Purchase.md#Purchase.InquiryRow), [Parts](/modules/Inventory.md#Inventory.Part), [PurchaseOrderInvoiceRows](/modules/Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](/modules/Sales.md#Sales.QuoteRow), [SalesAgreementBasisRows](/modules/Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRows](/modules/Sales.md#Sales.SalesAgreementRow), [VatGroups](/modules/Common.md#Common.VatGroup), [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow)

<a id="Common.WarehousePermission"></a>
### WarehousePermissions

Represents an application user warehouse permission.

- **Endpoint:** `GET /api/v1/Common/WarehousePermissions`
- **Required permission:** Show user rights groups
- **Introduced in:** 22.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ApplicationUserId` | `Int64` | no |  |
| `WarehouseId` | `Int64` | no |  |
| `PermissionGroups` | `PermissionGroups[]` | no | [PermissionGroups](/modules/Common.md#Common.PermissionGroup) |
| `Roles` | `Roles[]` | no | [Roles](/modules/Common.md#Common.Role) |
| `Permissions` | `Permissions[]` | no | [Permissions](/modules/Common.md#Common.Permission) |

**References out:** [PermissionGroups](/modules/Common.md#Common.PermissionGroup), [Permissions](/modules/Common.md#Common.Permission), [Roles](/modules/Common.md#Common.Role)
**Referenced by:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser)

<a id="Common.Warehouse"></a>
### Warehouses

Represents a warehouse.

- **Endpoint:** `GET /api/v1/Common/Warehouses`
- **Required permission:** Show company information
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `Code` | `String` | no |  |
| `LanguageId` | `Int64` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `CountryId` | `Int64` | no | [Countries](/modules/Common.md#Common.Country) |
| `PlaceOfDispatch` | `String` | no |  |
| `PalletRegistrationNumber` | `String` | no |  |
| `Url` | `String` | no |  |
| `TimeZoneId` | `String` | no | [Companies](/modules/Common.md#Common.Company) |
| `TimeZone` | `Decimal?` | yes |  |
| `CalendarId` | `Int64` | no | [Calendars](/modules/Common.md#Common.Calendar) |
| `Calendar` | `Calendars` | no | [Calendars](/modules/Common.md#Common.Calendar) |
| `VatNumber` | `String` | no |  |
| `DeliveryAddresses` | `DeliveryAddresses[]` | no | [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress) |

**References out:** [Calendars](/modules/Common.md#Common.Calendar), [Companies](/modules/Common.md#Common.Company), [Countries](/modules/Common.md#Common.Country), [DeliveryAddresses](/modules/Common.md#Common.DeliveryAddress), [LanguageCodes](/modules/Common.md#Common.LanguageCode)
**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [BlanketOrderSalesTypes](/modules/Sales.md#Sales.BlanketOrderSalesType), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [Companies](/modules/Common.md#Common.Company), [CustomerOrderInvoices](/modules/Sales.md#Sales.CustomerOrderInvoice), [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder), [DeliveryAddressWarehouseInformations](/modules/Common.md#Common.DeliveryAddressWarehouseInformation), [EdiBehaviors](/modules/Common.md#Common.EdiBehavior), [Inquiries](/modules/Purchase.md#Purchase.Inquiry), [InquiryRows](/modules/Purchase.md#Purchase.InquiryRow), [InvoiceLogs](/modules/Sales.md#Sales.InvoiceLog), [Locations](/modules/Inventory.md#Inventory.Location), [ManufacturingOrderNodes](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperationReportings](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingOrders](/modules/Manufacturing.md#Manufacturing.ManufacturingOrder), [ManufacturingPickingLists](/modules/Manufacturing.md#Manufacturing.ManufacturingPickingList), [MonitoringTaskRows](/modules/Common.md#Common.MonitoringTaskRow), [PartLocations](/modules/Inventory.md#Inventory.PartLocation), [PartPlanningInformation](/modules/Inventory.md#Inventory.PartPlanningInformation), [Parts](/modules/Inventory.md#Inventory.Part), [Persons](/modules/Common.md#Common.Person), [PhysicalInventoryLists](/modules/Inventory.md#Inventory.PhysicalInventoryList), [PurchaseOrderInvoices](/modules/Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [QuantityChanges](/modules/Inventory.md#Inventory.QuantityChange), [QuoteRows](/modules/Sales.md#Sales.QuoteRow), [Quotes](/modules/Sales.md#Sales.Quote), [SalesForecasts](/modules/Inventory.md#Inventory.SalesForecast), [SalesPickingLists](/modules/Sales.md#Sales.SalesPickingList), [Shipments](/modules/Sales.md#Sales.Shipment), [StockTransactions](/modules/Inventory.md#Inventory.StockTransaction), [TransferProfiles](/modules/Common.md#Common.TransferProfile), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)

<a id="Common.WriteOffCode"></a>
### WriteOffCodes

Represents a write off code.

- **Endpoint:** `GET /api/v1/Common/WriteOffCodes`
- **Required permission:** Show bank settings
- **Introduced in:** 22.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `IncomingPaymentCodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `IncomingPaymentCodingEntry` | `CodingEntries` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `OutgoingPaymentCodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `OutgoingPaymentCodingEntry` | `CodingEntries` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |

**References out:** [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry)
**Referenced by:** [IncomingPayments](/modules/Accounting.md#Accounting.IncomingPayment), [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment), [SetOffDestination](/modules/Accounting.md#Accounting.SetOffDestination)


## Payload types

<a id="Common.FileLink"></a>
### FileLink

Represents a file that has been linked to a comment.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `FilePathId` | `Int64` | no |  |
| `FileLinkContainerId` | `Int64` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `IsGenerated` | `Boolean` | no |  |
| `Filename` | `String` | no |  |
| `Directory` | `String` | no |  |
| `Orientation` | `Int32` | no |  |
| `AutomaticPrintOut` | `Boolean` | no |  |
| `GenerateCopies` | `Boolean` | no |  |
| `AllowExternalEditing` | `Boolean` | no |  |
| `PrinterType` | `Int32` | no |  |
| `SharePointFileVersion` | `String` | no |  |
| `UseLatestPublishedVersion` | `Boolean` | no |  |

- `Orientation` — Portrait=0, Landscape=1, Auto=2
- `PrinterType` — Automatic=0, External1=1, External2=2, External3=3

**Referenced by:** [Comments](/modules/Common.md#Common.Comment), [FormReportData](/modules/Common.md#Common.FormReportData)

<a id="Common.FormReportData"></a>
### FormReportData

Represents form report data from MONITOR.

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Name` | `String` | no |  |
| `Data` | `String` | no |  |
| `FileLinkIds` | `Int64[]` | no | [FileLink](/modules/Common.md#Common.FileLink) |

**References out:** [FileLink](/modules/Common.md#Common.FileLink)

<a id="Common.Money"></a>
### Money

An object composite representing a money value.

- **Introduced in:** 2.33

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Amount` | `Decimal` | no |  |
| `CurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |

**References out:** [Currencies](/modules/Common.md#Common.Currency)


## Depends on other modules

- [Accounting](/modules/Accounting.md): [Accounts](/modules/Accounting.md#Accounting.Account), [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry), [VoucherSeries](/modules/Accounting.md#Accounting.VoucherSeries)
- [Inventory](/modules/Inventory.md): [Parts](/modules/Inventory.md#Inventory.Part), [PartCodes](/modules/Inventory.md#Inventory.PartCode)
- [Manufacturing](/modules/Manufacturing.md): [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation)
- [Purchase](/modules/Purchase.md): [Suppliers](/modules/Purchase.md#Purchase.Supplier)
- [Sales](/modules/Sales.md): [Customers](/modules/Sales.md#Sales.Customer), [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup), [CustomerDistricts](/modules/Sales.md#Sales.CustomerDistrict), [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder)
- [TimeRecording](/modules/TimeRecording.md): [PersonTimeBanks](/modules/TimeRecording.md#TimeRecording.PersonTimeBank), [PersonWorkCenters](/modules/TimeRecording.md#TimeRecording.PersonWorkCenter), [PlannedAbsences](/modules/TimeRecording.md#TimeRecording.PlannedAbsence), [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule)
