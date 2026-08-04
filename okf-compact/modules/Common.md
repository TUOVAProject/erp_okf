# Common

Monitor API module `Common`: 110 queryable entities, 0 commands, 3 payload types.

## Queryable entities

<a id="Common.Address"></a>
### Addresses

Represents a queryable address.

- **Endpoint:** `GET /api/v1/Common/Addresses`
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the address. |
| `Addressee` | `String` | no |  | The addressee of the address. |
| `Field1` | `String` | no |  | The first field of the address. |
| `Field2` | `String` | no |  | The second field of the address. |
| `Field3` | `String` | no |  | The third field of the address. |
| `Field4` | `String` | no |  | The fourth field of the address. |
| `Field5` | `String` | no |  | The fifth field of the address. |
| `Locality` | `String` | no |  | The locality of the address. |
| `Region` | `String` | no |  | The region of the address. |
| `PostalCode` | `String` | no |  | The postal code of the address. |
| `AddressFormatType` | `Int32` | no |  | The format type of the address. |
| `CountryId` | `Int64` | no | [Countries](Common.md#Common.Country) | References Countries . |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The business key identifier of the language code. References LanguageCodes . |
| `FormReportTranslationGroupId` | `Int64` | no |  | The business key identifier of the form report translation group. References FormReportTranslationGroup. |
| `PostalCodeId` | `Int64?` | yes |  | The business key identifier of the postal code. References PostalCode. _(Unavailable)_ |

- `AddressFormatType` — Generic=0, PostalCodeCity=1, CityStatePostalCode=2, CityPostalCodeTwoRows=3, CityProvinsPostalCode=4

**References out:** [Countries](Common.md#Common.Country), [LanguageCodes](Common.md#Common.LanguageCode)
**Referenced by:** [BankAccounts](Accounting.md#Accounting.BankAccount), [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales), [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [Inquiries](Purchase.md#Purchase.Inquiry), [Persons](Common.md#Common.Person), [ProductRecords](Inventory.md#Inventory.ProductRecord), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Quotes](Sales.md#Sales.Quote), [SalesAgreements](Sales.md#Sales.SalesAgreement), [Shipments](Sales.md#Sales.Shipment), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Common.ApplicationUserPrinter"></a>
### ApplicationUserPrinters

Represents a printer that has been assigned to an application user.

- **Endpoint:** `GET /api/v1/Common/ApplicationUserPrinters`
- **Required permission:** Show user
- **Introduced in:** 2.52

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the application user printer. |
| `ApplicationUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that the application user printer belongs to. |
| `PrinterName` | `String` | no |  | The name of the local printer that is assigned. |
| `NormalizedFormReportType` | `Int32?` | yes |  | The type of form report that the printer assignment will be used for. |
| `FormReportType` | `Guid?` | yes |  | The type of form report that the printer assignment will be used for. |
| `ServerPrinterId` | `Int64?` | yes | [ServerPrinters](Common.md#Common.ServerPrinter) | The server printer that is linked to the application user printer. |
| `FormDocumentType` | `Int32` | no |  | The type of document that the printer assignment will be used for. |

- `NormalizedFormReportType` — NotInitialized=0, Quote=1, Acknowledgement=3, CustomerDeliveryNote=5, CustomerDeliveryNoteDelivered=6, Invoice=7, CustomerDeliveryNoteCollectionDelivered=8, SalesTransportLabelA4=16, ComprehensiveInvoice=17, PurchaseOrder=22, PurchaseOrderConfirmationReminder=23, PurchaseOrderConfirmationReminderCasualSupplier=24, PurchaseOrderDeliveryConfirmationReminder=25, PurchaseOrderDeliveryConfirmationReminderCasualSupplier=26, PurchaseTransportLabel=31, PickingList=100, InspectionReport=101, PurchaseTransportLabelForRejection=102, ProformaInvoice=103, ComprehensiveProformaInvoice=104, ManufacturingTransportLabelA4=105, ManufacturingTransportLabelA4ForRejection=106, ManufacturingTransportLabelA4InProgress=107, ManufacturingTransportLabelA4BeforeReporting=108, ManufacturingOrderOperation=109, ManufacturingOrderMaterial=110, ManufacturingOrderTraveler=111, PreCalculationSummary=112, SubcontractPurchaseOrder=113, SubcontractDeliveryNote=114, SubcontractTransportLabelA4=117, SubcontractTransportLabelA5=118, SubcontractTransportLabelSmall=119, LevelListWhereUsedList=120, LevelListConsistsOfList=122, PostCalculationSummary=123, PhysicalInventoryList=124, MaterialClearanceShortageList=125, AccountingOrder=126, GeneralLedgerDrilldown=127, JournalDrilldown=128, ManufacturingPickingList=129, ManufacturingPickingListGroupByOrder=130, ManufacturingPickingListGroupByMaterial=131, AccountingReportHeader=132, InternalInvoice=133, CashReceipt=134, AccountsReceivableLedger=135, AccountsReceivableLedgerReprint=136, IncomingPaymentLedger=137, IncomingPaymentLedgerReprint=138, AccountsPayableLedger=139, AccountsPayableLedgerReprint=140, PreliminaryAccountsPayableLedger=141, PreliminaryAccountsPayableLedgerReprint=142, CancelledAccountsPayableLedger=143, CancelledAccountsPayableLedgerReprint=144, CancelledPreliminaryAccountsPayableLedger=145, CancelledPreliminaryAccountsPayableLedgerReprint=146, PaymentReminder=147, PaymentReminderReprint=148, AccrualAccountingLedger=149, AccrualAccountingLedgerReprint=150, VatReport=151, VatReportAccounts=152, VatReportGeneralLedger=153, VatReportTransactions=154, VatReportCheck=155, VatReportDifferenceSearch=156, TransactionList=157, OutgoingPaymentLedger=158, OutgoingPaymentLedgerReprint=159, SalesTransportLabelA5=160, CustomerCaseConfirmation=161, AccountStatement=162, CustomerCaseAnswer=163, CustomerNonconformityReport=164, SupplierNonconformityReport=165, InternalNonconformityReport=166, SupplierClaimReport=167, CancelledAccountsReceivableLedger=168, CancelledAccountsReceivableLedgerReprint=169, ShipmentWayBill=170, ShipmentParcel=171, Inquiry=172, CustomerOrderPickingList=173, EimInvoiceInformation=174, InterestInvoice=175, FileLink=176, RecordingsAndSalaryTypeSummary=177, ProductRecordConsistsOf=178, ProductRecordIncludedIn=179, InternalProjectReport=180, ExternalProjectReport=181, TraceabilityProtocol=182, FixedAssetLedger=183, FixedAssetLedgerReprint=184, CustomReport=185, StockAcknowledgement=186, StockDeliveryNote=187, StockPurchaseOrder=188, StockDeliveryNoteDelivered=189, PurchaseOrderModified=190, TaxDepreciation=191, TaxDepreciationDrilldown=192, PartTransportLabelSmall=193, PartTransportLabelA5=194, PartTransportLabelA4=195, UnplannedStockBalanceChangeLedger=196, UnplannedStockBalanceChangeLedgerReprint=197, PIADetailed=198, StockTransactionLogLedger=199, ManufacturingOrderLogLedger=200, InvoiceLogLedger=201, PriceChangeLogLedger=202, CalculationDifferenceLedger=203, AccountStatementBalancePerCustomer=204, StockTransactionLogLedgerReprint=205, ManufacturingOrderLogLedgerReprint=206, PriceChangeLogLedgerReprint=207, CalculationDifferenceLedgerReprint=208, InvoiceLogLedgerReprint=209, PrintoutDemoCertificate=210, BlanketOrderPurchase=211, ArrivalNote=212, CorrectionInvoice=213, ModifiedOrderConfirmation=214, PurchaseDeliverySchedule=215, PackageList=216, PackageTransportLabel=217, AnnualVolumeList=218, BlanketOrderSales=219, TransportLabelDirectWithdrawalA4=220, TransportLabelDirectWithdrawalA5=221, TransportLabelDirectWithdrawalSmall=222, TransportLabelDirectArrivalA4=223, TransportLabelDirectArrivalA5=224, TransportLabelDirectArrivalSmall=225, TransportLabelMoveBetweenLocationsA4=226, TransportLabelMoveBetweenLocationsA5=227, TransportLabelMoveBetweenLocationsSmall=228, TransportLabelMoveBetweenWarehousesA4=229, TransportLabelMoveBetweenWarehousesA5=230, TransportLabelMoveBetweenWarehousesSmall=231, Standard8DNonconformityReport=232, PaymentLedger=233, PaymentLedgerReprint=234, PaymentVoucher=235, DebtorStatement=236, CreditorStatement=237, PrintVoucher=238, OfficialReceipt=239, PolishCashReceipt=240, PolishCashReport=241, Standard8DCustomerNonconformityReport=242, AutoCodingLedger=243, AutoCodingLedgerReprint=244, MeasuringProtocolManufacturing=245, MeasuringProtocolPurchase=246, VoucherList=247, RevenueCalculationLedger=248, RevenueCalculationLedgerReprint=249, GeneralActivityList=250, ReturnPurchaseOrderDeliveryNote=251, ReturnPurchaseOrderProforma=252, ReturnPurchaseOrderTransportLabelA4=253, ReturnPurchaseOrderTransportLabelA5=254, ReturnPurchaseOrderTransportLabelSmall=255, Waybill=256, ShipmentAdvice=257, PartTransportMultiLabel=258, StockTransportMultiLabel=259, SustainabilityCalculationDetailed=260, ShipmentReceipt=261, OrderRowDiscounts=262, BankAccountReconciliation=263, CollectiveCorrectionInvoice=264, ExternalCustomerNonconformityReport=265, ExternalSupplierNonconformityReport=266, ExternalInternalNonconformityReport=267, PartContentDeliveryReport=268, ProjectMaterialCalculationLedger=269, ProjectMaterialCalculationLedgerReprint=270, CausesForShortage=271, CustomerLevelListConsistsOfList=272, CustomerLevelListIncludedInList=273, SupplierLevelListConsistsOfList=274, SupplierLevelListIncludedInList=275, GPBForm=276, CurrencyWarehouse=277, ReturnPurchaseOrderPickingList=278, SubcontractProformaInvoice=279, LocationLabel=280, LocationMultiLabel=281, FilesExternal1=282, FilesExternal2=283, FilesExternal3=284, RemittanceAdvice=285, SupplierAgreement=286, ModifiedSupplierAgreement=287, SelfBilledInvoice=288, PurchaseTransportLabelA5=310, RefillPickingLocationStandard=500, PurchaseTransportLabelA5ForRejection=1020, ManufacturingTransportLabelA5=1050, ManufacturingTransportLabelA5ForRejection=1060, ManufacturingTransportLabelA5InProgress=1070, ManufacturingTransportLabelA5BeforeReporting=1080, SalesTransportLabelSmall=1600, Form=2401, ServiceReporting=2402, SalesAgreement=2501, ModifiedSalesAgreement=2502, AccountStatementPurchase=2503, ReturnPurchaseOrder=2504, PurchaseTransportLabelSmall=3100, PurchaseTransportLabelSmallForRejection=10200, ManufacturingTransportLabelSmall=10500, ManufacturingTransportLabelSmallForRejection=10600, ManufacturingTransportLabelSmallInProgress=10700, ManufacturingTransportLabelSmallBeforeReporting=10800, DebitNote=10801, ServiceTax=10802, EdiCustomerOrderConfirmation=20001, EdiCustomerOrderInvoice=20002, EdiCustomerOrderSimpleDispatchAdvice=20003, EdiCustomerOrderResponse=20004, EdiPurchaseOrder=20005, EdiCustomerOrderComplexDispatchAdvice=20006, EdiPurchaseDeliverySchedule=20007
- `FormDocumentType` — Document=0, AdaptedReport=1

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [ServerPrinters](Common.md#Common.ServerPrinter)
**Referenced by:** [ApplicationUsers](Common.md#Common.ApplicationUser)

<a id="Common.ApplicationUser"></a>
### ApplicationUsers

Represents a queryable MONITOR application user.

- **Endpoint:** `GET /api/v1/Common/ApplicationUsers`
- **Required permission:** Show user
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the application user. |
| `Username` | `String` | no |  | The username of the application user. |
| `Description` | `String` | no |  | The description of the application user. |
| `WindowsUserAccountName` | `String` | no |  | The windows account username of the application user. |
| `IsInvisible` | `Boolean` | no |  | Specifies if the application user is hidden from general use in the MONITOR system. |
| `DefaultRole` | `Int64` | no |  | The default role of the application user. |
| `DefaultGroup` | `Int64?` | yes |  | The business key identifier of the application user's default permission group. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the application user's default warehouse. References Warehouses . |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The business key identifier of the application user's default language code. References LanguageCodes . |
| `MailAddress` | `String` | no |  | The email address of the user. |
| `MailMethod` | `Int32?` | yes |  | The email method of the user. |
| `Printers` | `ApplicationUserPrinters[]` | no | [ApplicationUserPrinters](Common.md#Common.ApplicationUserPrinter) | The printers that have been assigned to the user. |
| `DefaultPrinter` | `String` | no |  | The name of the default printer that have been assigned to the user. |
| `External1Printer` | `String` | no |  | The name of the external 1 printer that has been assigned to the user. _(Use the Printers collection with FormReportType = FilesExternal1 instead)_ |
| `External2Printer` | `String` | no |  | The name of the external 2 printer that has been assigned to the user. _(Use the Printers collection with FormReportType = FilesExternal2 instead)_ |
| `External3Printer` | `String` | no |  | The name of the external 3 printer that has been assigned to the user. _(Use the Printers collection with FormReportType = FilesExternal3 instead)_ |
| `PrintoutFormatForParcel` | `Int32` | no |  | The printout document format type that have been assigned to the user. |
| `WarehousePermissions` | `WarehousePermissions[]` | no | [WarehousePermissions](Common.md#Common.WarehousePermission) | The warehouse permissions that apply to the application user. |
| `DefaultVoucherSeriesId` | `Int64?` | yes | [VoucherSeries](Accounting.md#Accounting.VoucherSeries) | The business key identifier of the application user's default voucher series. |
| `UserAuthenticationMethod` | `Int32` | no |  | The selected authentication method of the application user. |
| `Culture` | `String` | no |  | The culture setting of the user in .NET format. |

- `MailMethod` — ClientBasedOutlook=0, ServerBasedExchange=2, ServerBasedSmtp=3, ServerBasedExchangeOnline=4
- `PrintoutFormatForParcel` — PDF=0, ZPL=1, LaserSte=2, ThermoSe=3, LaserA5=4, Laser2A5=5, Thermo190=6, ThermoBrev3=7, Thermo165=8
- `UserAuthenticationMethod` — Password=0, WindowsIntegrated=1, Oidc=4

**References out:** [ApplicationUserPrinters](Common.md#Common.ApplicationUserPrinter), [LanguageCodes](Common.md#Common.LanguageCode), [VoucherSeries](Accounting.md#Accounting.VoucherSeries), [WarehousePermissions](Common.md#Common.WarehousePermission), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [ApplicationUserPrinters](Common.md#Common.ApplicationUserPrinter), [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory), [BusinessOpportunityActivities](Sales.md#Sales.BusinessOpportunityActivity), [BusinessOpportunityActivityTemplateRows](Sales.md#Sales.BusinessOpportunityActivityTemplateRow), [BusinessOpportunitySalesProcessSteps](Sales.md#Sales.BusinessOpportunitySalesProcessStep), [CaseEntryActivities](Inventory.md#Inventory.CaseEntryActivity), [CaseEntryPhases](Inventory.md#Inventory.CaseEntryPhase), [CaseManagementTemplateNodes](Inventory.md#Inventory.CaseManagementTemplateNode), [CustomerOrderActivities](Sales.md#Sales.CustomerOrderActivity), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerRelationshipManagementActivities](Sales.md#Sales.CustomerRelationshipManagementActivity), [Customers](Sales.md#Sales.Customer), [DelegatedWork](Common.md#Common.DelegatedWork), [IncomingPayments](Accounting.md#Accounting.IncomingPayment), [InvoiceLogs](Sales.md#Sales.InvoiceLog), [Locations](Inventory.md#Inventory.Location), [ManufacturingPickingLists](Manufacturing.md#Manufacturing.ManufacturingPickingList), [MonitoringTaskRecipients](Common.md#Common.MonitoringTaskRecipient), [MonitoringTasks](Common.md#Common.MonitoringTask), [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment), [PartActivities](Inventory.md#Inventory.PartActivity), [PartConfigurationPresets](Common.md#Common.PartConfigurationPreset), [Parts](Inventory.md#Inventory.Part), [Persons](Common.md#Common.Person), [ProductRecords](Inventory.md#Inventory.ProductRecord), [ProjectActivities](Common.md#Common.ProjectActivity), [ProjectActivityTypes](Common.md#Common.ProjectActivityType), [ProjectPhases](Common.md#Common.ProjectPhase), [ProjectPhaseTypes](Common.md#Common.ProjectPhaseType), [QuantityChanges](Inventory.md#Inventory.QuantityChange), [QuoteActivities](Sales.md#Sales.QuoteActivity), [SalesPickingLists](Sales.md#Sales.SalesPickingList), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Common.AutoCompleteConfiguration"></a>
### AutoCompleteConfigurations

Represents an auto-complete configuration.

- **Endpoint:** `GET /api/v1/Common/AutoCompleteConfigurations`
- **Introduced in:** 2.46

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the auto-complete configuration. |
| `Description` | `String` | no |  | The description of the auto-complete configuration. |
| `IsPreset` | `Boolean` | no |  | Specifies whether or not the auto-complete configuration is a preset configuration. |
| `PopupTypeId` | `Guid` | no |  | The GUID identifier of the popup-type that the auto-complete configuration applies to. |


<a id="Common.BlobData"></a>
### BlobData

A container for blob data.

- **Endpoint:** `GET /api/v1/Common/BlobData`
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the blob data. |
| `MediaType` | `Int32` | no |  | The media type of the blob data. |
| `MediaSubType` | `String` | no |  | The media subtype of the blob data. |
| `Value` | `String` | no |  | The value of the blob data, represented as a Base64 string. |

- `MediaType` — Text=0, Image=1, Audio=2, Video=3, Application=4, Multipart=5, Message=6

**Referenced by:** [Companies](Common.md#Common.Company), [EimDocuments](Purchase.md#Purchase.EimDocument), [PartImages](Inventory.md#Inventory.PartImage), [Persons](Common.md#Common.Person)

<a id="Common.BusinessContactBankAccount"></a>
### BusinessContactBankAccounts

Represents a business contact bank account.

- **Endpoint:** `GET /api/v1/Common/BusinessContactBankAccounts`
- **Introduced in:** 2.28

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business contact bank account. |
| `ClearingNumber` | `String` | no |  | The clearing number of the business contact bank account. |
| `ClearingSystem` | `String` | no |  | The clearing system of the business contact bank account. |
| `CountryId` | `Int64` | no | [Countries](Common.md#Common.Country) | The business key identifier of the business contact bank account country. |
| `Country` | `Countries` | no | [Countries](Common.md#Common.Country) | The country of the business contact bank account. |
| `CentralBankCodeId` | `Int64?` | yes | [CentralBankCodes](Common.md#Common.CentralBankCode) | The business key identifier of the business contact bank account central bank code. |
| `CentralBankCode` | `CentralBankCodes` | no | [CentralBankCodes](Common.md#Common.CentralBankCode) | The central bank code of the business contact bank account. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the business contact bank account currency. |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The currency of the business contact bank account. |
| `Type` | `Int32` | no |  | The type of the business contact bank account. |
| `Number` | `String` | no |  | The human readable identifier number of the business contact bank account. |
| `BankIdentifierCode` | `String` | no |  | The human readable identifier bank identifier code of the business contact bank account. |
| `BankAddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the business contact bank account bank address. |
| `BankAddress` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The bank address of the business contact bank account. |

- `Type` — Iban=1, Bban=2, Upic=3, Miscellaneous=4

**References out:** [Addresses](Common.md#Common.Address), [CentralBankCodes](Common.md#Common.CentralBankCode), [Countries](Common.md#Common.Country), [Currencies](Common.md#Common.Currency)
**Referenced by:** [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Common.BusinessContactNoteHistory"></a>
### BusinessContactNoteHistories

Represents a business contact note history entry.

- **Endpoint:** `GET /api/v1/Common/BusinessContactNoteHistories`
- **Introduced in:** 2.55

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business contact note. |
| `Subject` | `String` | no |  | The subject of the business contact note. |
| `BodyId` | `Int64?` | yes |  | The business key identifier for the body of the business contact note. |
| `Body` | `Comments` | no | [Comments](Common.md#Common.Comment) | The body of the business contact note. |
| `CreatedByUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that created the business contact note. |
| `CreatedTimestamp` | `DateTimeOffset` | no |  | The date the business contact note was created. |
| `ParentId` | `Int64` | no |  | The business key identifier of the parent. |
| `ParentClass` | `Guid` | no |  | The GUID of the parent type. |

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Comments](Common.md#Common.Comment)
**Referenced by:** [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [CaseEntry](Inventory.md#Inventory.CaseEntry), [Parts](Inventory.md#Inventory.Part)

<a id="Common.BusinessContactReference"></a>
### BusinessContactReferences

Represents a queryable business contact reference.

- **Endpoint:** `GET /api/v1/Common/BusinessContactReferences`
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the business contact reference. |
| `Name` | `String` | no |  | The name of the business contact reference. |
| `ExtraInformation1` | `String` | no |  | The first extra information field of the business contact reference. |
| `ExtraInformation2` | `String` | no |  | The second extra information field of the business contact reference. |
| `ExtraInformation3` | `String` | no |  | The third extra information field of the business contact reference. |
| `Category` | `String` | no |  | The category of the business contact reference. |
| `Note` | `String` | no |  | Any extra notes regarding the business contact reference. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the comment that is linked to the business contact reference. References Comments . |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment that is linked to the the business contact reference. |
| `CellPhoneNumber` | `String` | no |  | The value of the communication address. |
| `PhoneNumber` | `String` | no |  | The value of the communication address. |
| `EmailAddress` | `String` | no |  | The value of the communication address. |
| `FaxNumber` | `String` | no |  | The value of the communication address. |
| `Code` | `String` | no |  | The code / number of the business contact reference. |

**References out:** [Comments](Common.md#Common.Comment)
**Referenced by:** [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerRelationshipManagementActivities](Sales.md#Sales.CustomerRelationshipManagementActivity), [Customers](Sales.md#Sales.Customer), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Projects](Common.md#Common.Project), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Quotes](Sales.md#Sales.Quote), [SalesAgreements](Sales.md#Sales.SalesAgreement), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Common.Calendar"></a>
### Calendars

Represents a queryable calendar.

- **Endpoint:** `GET /api/v1/Common/Calendars`
- **Required permission:** Show calendar
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the calendar. |
| `CalendarType` | `Int32` | no |  | The type of the calendar. |
| `HolidayType` | `Int32` | no |  | The holiday type of the calendar. |
| `Description` | `String` | no |  | The translated description of the calendar. |
| `Code` | `String` | no |  | The human readable code of the calendar. |

- `CalendarType` — NoHoliday=0, Weekend=1, OnlySundayWeekend=2, Swedish=10, Norwegian=11, Estonian=12, Finnish=13, German=14, Hungarian=15, Latvian=16, Polish=17, Russian=18, Lithuanian=19, Usa=20, Danish=21, Andorra=22, UnitedArabEmirates=23, Afghanistan=24, AntiguaBarbuda=25, Albania=26, Armenia=27, Angola=28, Argentina=29, AmericanSamoa=30, Austria=31, Australia=32, Aruba=33, Azerbaijan=34, BosniaHerzegovina=35, Barbados=36, Bangladesh=37, Belgium=38, BurkinaFaso=39, Bulgaria=40, Bahrain=41, Burundi=42, Brunei=43, Bolivia=44, Brazil=45, Bahamas=46, Botswana=47, Belarus=48, Belize=49, Canada=50, CongoBrazzaville=51, Switzerland=52, CotedIvoire=53, Chile=54, Cameroon=55, China=56, Colombia=57, CostaRica=58, Cuba=59, Curacao=60, Cyprus=61, CzechRepublic=62, Djibouti=63, Dominica=64, DominicanRepublic=65, Algeria=66, Ecuador=67, Egypt=68, Spain=69, Ethiopia=70, Fiji=71, France=72, Gabon=73, UnitedKingdom=74, Georgia=75, Guernsey=76, Ghana=77, Greenland=78, Guinea=79, Greece=80, Guatemala=81, Guam=82, HongKong=83, Honduras=84, Croatia=85, Haiti=86, Indonesia=87, Ireland=88, Israel=89, IsleofMan=90, India=91, Iran=92, Iceland=93, Italy=94, Jersey=95, Jamaica=96, Jordan=97, Japan=98, Kenya=99, Kyrgyzstan=100, Cambodia=101, SaintKittsNevis=102, SouthKorea=103, Kuwait=104, Kazakhstan=105, Laos=106, SaintLucia=107, Liechtenstein=108, SriLanka=109, Lesotho=110, Luxembourg=111, Morocco=112, Monaco=113, Moldova=114, Montenegro=115, Madagascar=116, MarshallIslands=117, NorthMacedonia=118, Macau=119, NorthernMarianaIslands=120, Mauritania=121, Malta=122, Maldives=123, Malawi=124, Mexico=125, Malaysia=126, Mozambique=127, Namibia=128, Nigeria=129, Nicaragua=130, Netherlands=131, NewZealand=132, Oman=133, Panama=134, Peru=135, PapuaNewGuinea=136, Philippines=137, Pakistan=138, PuertoRico=139, Portugal=140, Palau=141, Paraguay=142, Qatar=143, Romania=144, Serbia=145, SaudiArabia=146, Seychelles=147, Singapore=148, Slovenia=149, Slovakia=150, SierraLeone=151, SanMarino=152, Surinam=153, SaoTomePrincipe=154, ElSalvador=155, Eswatini=156, Chad=157, FrenchSouthernTerritories=158, Thailand=159, EastTimor=160, Tunisia=161, Tonga=162, Turkiye=163, TrinidadTobago=164, Tuvalu=165, Taiwan=166, Tanzania=167, Ukraine=168, UnitedStatesMinorOutlyingIslands=169, Uruguay=170, Uzbekistan=171, VaticanCity=172, Venezuela=173, UnitedStatesVirginIslands=174, Vietnam=175, Vanuatu=176, Samoa=177, SouthAfrica=178, Zambia=179, Zimbabwe=180
- `HolidayType` (bitmask) — None=0, Weekend=1, Holiday=2, All=3

**Referenced by:** [Warehouses](Common.md#Common.Warehouse)

<a id="Common.CentralBankCode"></a>
### CentralBankCodes

Represents a central bank code.

- **Endpoint:** `GET /api/v1/Common/CentralBankCodes`
- **Required permission:** Show bank settings
- **Introduced in:** 2.28

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the central bank code. |
| `Code` | `String` | no |  | The code of the central bank code. |
| `Description` | `String` | no |  | The description of the central bank code. |
| `IsDefault` | `Boolean` | no |  | Specifies if the bank code is default. |

**Referenced by:** [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount)

<a id="Common.Comment"></a>
### Comments

Represents a comment, containing both raw and HTML formatted text.

- **Endpoint:** `GET /api/v1/Common/Comments`
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the comment. |
| `Text` | `String` | no |  | The comment text with HTML formatting. |
| `RawText` | `String` | no |  | The comment text without HTML formatting. In MONITOR this is used exclusively for indexing purposes and is not shown anywhere in the system. |
| `HasFileLinks` | `Boolean` | no |  | Specifies if the comment has files linked to it. |
| `FileLinks` | `FileLink[]` | no | [FileLink](Common.md#Common.FileLink) | A collection of all file links that belong to the comment. |

**References out:** [FileLink](Common.md#Common.FileLink)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting), [AdditionRecordings](TimeRecording.md#TimeRecording.AdditionRecording), [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales), [BusinessContactNoteHistories](Common.md#Common.BusinessContactNoteHistory), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [BusinessOpportunityActivities](Sales.md#Sales.BusinessOpportunityActivity), [BusinessOpportunityActivityTemplateRows](Sales.md#Sales.BusinessOpportunityActivityTemplateRow), [BusinessOpportunityReferences](Sales.md#Sales.BusinessOpportunityReference), [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseEntryActivities](Inventory.md#Inventory.CaseEntryActivity), [CaseManagementTemplateNodes](Inventory.md#Inventory.CaseManagementTemplateNode), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerPartLinks](Sales.md#Sales.CustomerPartLink), [CustomerRelationshipManagementActivities](Sales.md#Sales.CustomerRelationshipManagementActivity), [Customers](Sales.md#Sales.Customer), [DrawingRevisions](Manufacturing.md#Manufacturing.DrawingRevision), [EmploymentPeriods](Common.md#Common.EmploymentPeriod), [ExtraFields](Common.md#Common.ExtraField), [FixedAssetSales](Accounting.md#Accounting.FixedAssetSale), [FormTemplateRows](Common.md#Common.FormTemplateRow), [FormTemplates](Common.md#Common.FormTemplate), [FormTemplateSelectionRows](Common.md#Common.FormTemplateSelectionRow), [Inquiries](Purchase.md#Purchase.Inquiry), [Locations](Inventory.md#Inventory.Location), [MaintenanceReportingRows](Manufacturing.md#Manufacturing.MaintenanceReportingRow), [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting), [MaintenanceReportingSelectionRows](Manufacturing.md#Manufacturing.MaintenanceReportingSelectionRow), [ManufacturingOrderMaterials](Manufacturing.md#Manufacturing.ManufacturingOrderMaterial), [ManufacturingOrderNodeDrawingRevisions](Manufacturing.md#Manufacturing.ManufacturingOrderNodeDrawingRevision), [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [MaterialRows](Manufacturing.md#Manufacturing.MaterialRow), [MonitoringTasks](Common.md#Common.MonitoringTask), [OperationRows](Manufacturing.md#Manufacturing.OperationRow), [PackageRows](Sales.md#Sales.PackageRow), [PartActivities](Inventory.md#Inventory.PartActivity), [PartConfigurations](Common.md#Common.PartConfiguration), [PartConfigurationTemplates](Common.md#Common.PartConfigurationTemplate), [Parts](Inventory.md#Inventory.Part), [Persons](Common.md#Common.Person), [ProductRecords](Inventory.md#Inventory.ProductRecord), [ProjectActivities](Common.md#Common.ProjectActivity), [ProjectActivityTypes](Common.md#Common.ProjectActivityType), [ProjectCostBudgets](Common.md#Common.ProjectCostBudget), [ProjectCostForecasts](Common.md#Common.ProjectCostForecast), [ProjectCostReportingEntries](Common.md#Common.ProjectCostReportingEntry), [Projects](Common.md#Common.Project), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [QuoteActivities](Sales.md#Sales.QuoteActivity), [Quotes](Sales.md#Sales.Quote), [Revisions](Common.md#Common.Revision), [SalesAgreements](Sales.md#Sales.SalesAgreement), [SalesPrices](Sales.md#Sales.SalesPrice), [Schedules](TimeRecording.md#TimeRecording.Schedule), [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink), [Suppliers](Purchase.md#Purchase.Supplier), [VatRates](Common.md#Common.VatRate), [Vouchers](Accounting.md#Accounting.Voucher), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter), [WorkIntervals](TimeRecording.md#TimeRecording.WorkInterval)

<a id="Common.CommunicationAddress"></a>
### CommunicationAddresses

Represents a queryable communication address. A communication address is used to store either phone, cellphone, email or fax information in MONITOR.

- **Endpoint:** `GET /api/v1/Common/CommunicationAddresses`
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the communication address. |
| `Type` | `Int32` | no |  | The type of information stored within this particular communication address instance. |
| `CommunicationAddressValue` | `String` | no |  | The value of the communication address. |
| `Remarks` | `String` | no |  | Any remarks regarding the communication address. |
| `RecipientOf` | `Int32` | no |  | Specifies what types of communication the address should be recipient of. |
| `ContactName` | `String` | no |  | The contact name of the communication address. |

- `Type` — Phone=0, Fax=1, Email=2, CellPhone=3
- `RecipientOf` (bitmask) — None=0, Invoice=1, Reminder=2, OrderConfirmation=4, DispatchAdvice=8, ShippingAgentAdvice=16, OrderConfirmationReminder=32, DeliveryReminder=64, DeliverySchedule=128, PurchaseOrder=256, Quote=512, ShippingAgentSmsAdvice=1024, SubcontractDeliveryNote=2048, Inquiry=4096, CaseClaimReport=8192, CaseConfirmation=16384, CaseResponse=32768, NonconformityReport=65536, Proforma=131072, ProjectReportExternal=262144, ProjectReportInternal=524288, CustomerDeliveryNote=1048576, TraceabilityProtocol=2097152, BlanketOrderPurchase=4194304, BlanketOrderSales=8388608, PurchaseDeliverySchedule=16777216, SalesAgreement=33554432, AccountStatement=67108864, EInvoiceInvitation=134217728, ReturnOrder=268435456, SubcontractProformaInvoice=536870912, SupplierAgreement=1073741824

**Referenced by:** [BusinessOpportunityReferences](Sales.md#Sales.BusinessOpportunityReference), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [Inquiries](Purchase.md#Purchase.Inquiry), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Quotes](Sales.md#Sales.Quote), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Common.Company"></a>
### Companies

Represents a company in the MONITOR system.

- **Endpoint:** `GET /api/v1/Common/Companies`
- **Required permission:** Show company information
- **Introduced in:** 24.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the company. |
| `Name` | `String` | no |  | The name of the company. |
| `ImageId` | `Int64?` | yes |  | The business key identifier for the image of the company. |
| `Image` | `BlobData` | no | [BlobData](Common.md#Common.BlobData) | The image blob of the company. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier for the currency of the company. |
| `Currency` | `Currencies` | no | [Currencies](Common.md#Common.Currency) | The company currency. |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The business key identifier of the language. |
| `Language` | `LanguageCodes` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The language of the company. |
| `Warehouses` | `Warehouses[]` | no | [Warehouses](Common.md#Common.Warehouse) | The warehouses that belong to the company. |
| `TimeZone` | `String` | no |  | The time zone of the company. Specified as a time zone identifier. Identifier depends on underlying database engine, and could be in either IANA or Windows style. |
| `CorporationIdentificationNumber` | `String` | no |  | The corporation identification number of the company. |

**References out:** [BlobData](Common.md#Common.BlobData), [Currencies](Common.md#Common.Currency), [LanguageCodes](Common.md#Common.LanguageCode), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [Warehouses](Common.md#Common.Warehouse)

<a id="Common.CompanyEmissionDetail"></a>
### CompanyEmissionDetails

Represents a company emission type linked to sustainability reporting according to the GHG protocol.

- **Endpoint:** `GET /api/v1/Common/CompanyEmissionDetails`
- **Required permission:** Show pre-calculation
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the company emission type. |
| `Code` | `String` | no |  | The code of the company emission type. |
| `Description` | `String` | no |  | The description of the company emission type. |
| `EmissionType` | `Int32` | no |  | The emission type of the company emission type. |
| `Value` | `Decimal` | no |  | The value of the company emission type. |
| `Origin` | `String` | no |  | The origin of the company emission type. |
| `OriginDate` | `DateTimeOffset?` | yes |  | The origin date of the company emission type. |
| `ReliabilityIndex` | `Decimal` | no |  | The reliability index of the company emission type. |
| `ReportingMethod` | `Int32` | no |  | The reporting method of the company emission type. |
| `UnitId` | `Int64?` | yes |  | The business key identifier of the company emission type's unit. |
| `Unit` | `Units` | no | [Units](Common.md#Common.Unit) | The company emission type's unit. |

**References out:** [Units](Common.md#Common.Unit)

<a id="Common.CompanyOverheadType"></a>
### CompanyOverheadTypes

Represents an overhead type used in company emission and sustainability calculations.

- **Endpoint:** `GET /api/v1/Common/CompanyOverheadTypes`
- **Required permission:** Show pre-calculation
- **Introduced in:** 25.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the overhead type. |
| `Description` | `String` | no |  | The description of the overhead type. |
| `Code` | `String` | no |  | The code of the overhead type. |
| `IsDefault` | `Boolean` | no |  | Specifies if the overhead type is default. |


<a id="Common.ConnectionProfile"></a>
### ConnectionProfiles

Represents a connection profile.

- **Endpoint:** `GET /api/v1/Common/ConnectionProfiles`
- **Required permission:** Show connection
- **Introduced in:** 23.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the profile. |
| `Number` | `Int64` | no |  | The number of the profile. |
| `Description` | `String` | no |  | The description of the profile. |
| `TargetRole` | `Int32` | no |  | The transfer role of the profile. |
| `RemoteCompanyId` | `Guid` | no |  | The remote company identifier of the profile. |
| `RemoteCompanyNumber` | `String` | no |  | The remote company number of the profile. |
| `RemoteCompanyName` | `String` | no |  | The remote company name of the profile. |
| `RemoteDnsName` | `String` | no |  | The remote dns name of the profile. |
| `RemotePort` | `Int32` | no |  | The remote TCP/IP port of the profile. |
| `LocalDnsName` | `String` | no |  | The local dns name of the profile. |
| `LocalPort` | `Int32` | no |  | The local TCP/IP port of the profile. |

- `TargetRole` — ManufacturingCompany=0, SalesCompany=1

**Referenced by:** [TransferProfiles](Common.md#Common.TransferProfile)

<a id="Common.Country"></a>
### Countries

Represents a queryable country.

- **Endpoint:** `GET /api/v1/Common/Countries`
- **Required permission:** Show countries
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the country. |
| `Code` | `String` | no |  | The human readable code of the country. |
| `Description` | `String` | no |  | The translated description of the country. |
| `IsEuMember` | `Boolean` | no |  | Specifies if the country is a member of the European Union. |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | References LanguageCodes . |
| `CurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | References Currencies . |
| `AddressFormatType` | `Int32` | no |  | The format type of the address. |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | References CustomerAccountGroups . |
| `IsActive` | `Boolean` | no |  | Specifies if the country is active and available in MONITOR or not. |
| `SupplierAccountGroupId` | `Int64?` | yes |  | References SupplierAccountGroup. |
| `VatGroupId` | `Int64?` | yes | [VatGroups](Common.md#Common.VatGroup) | References VatGroups . _(Replaced by CustomerVatGroupId/SupplierVatGroupId)_ |
| `SupplierVatGroupId` | `Int64?` | yes | [VatGroups](Common.md#Common.VatGroup) | References VatGroups . |
| `CustomerVatGroupId` | `Int64?` | yes | [VatGroups](Common.md#Common.VatGroup) | References VatGroups . |
| `VatRegistrationNumberPrefixException` | `String` | no |  | The VAT registration number prefix exception of the country. |
| `CountryRegion` | `Int32` | no |  | Region code in integer format according to ISO-3166 |
| `CountrySubRegion` | `Int32` | no |  | Sub region code in integer format according to ISO-3166 |
| `CountryIntermediateRegion` | `Int32` | no |  | Intermediate region code in integer format according to ISO-3166 |

**References out:** [Currencies](Common.md#Common.Currency), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [LanguageCodes](Common.md#Common.LanguageCode), [VatGroups](Common.md#Common.VatGroup)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [Addresses](Common.md#Common.Address), [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount), [CountryDocumentSettings](Sales.md#Sales.CountryDocumentSettings), [CustomerCountryDocumentSettings](Sales.md#Sales.CustomerCountryDocumentSettings), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [Parts](Inventory.md#Inventory.Part), [PartTemplates](Inventory.md#Inventory.PartTemplate), [ShipmentCustomsRows](Sales.md#Sales.ShipmentCustomsRow), [Warehouses](Common.md#Common.Warehouse)

<a id="Common.Currency"></a>
### Currencies

Represents a queryable currency.

- **Endpoint:** `GET /api/v1/Common/Currencies`
- **Required permission:** Show currencies
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the currency. |
| `Code` | `String` | no |  | The human readable identifier of the currency. |
| `Description` | `String` | no |  | The translated description of the currency. |
| `RateFactor` | `Int32` | no |  | The rate factor of the currency. |
| `DefaultSalesExchangeRate` | `Decimal` | no |  | The default sales exchange rate. |
| `DefaultPurchaseExchangeRate` | `Decimal` | no |  | The default purchase exchange rate. |
| `ExchangeRates` | `CurrencyExchangeRates[]` | no | [CurrencyExchangeRates](Common.md#Common.CurrencyExchangeRate) | All available exchange rates for the currency. |
| `ExchangeRatesChangeLog` | `CurrencyExchangeRateChangeLogs[]` | no | [CurrencyExchangeRateChangeLogs](Common.md#Common.CurrencyExchangeRateChangeLog) | All previous exchange rates for the currency |

**References out:** [CurrencyExchangeRateChangeLogs](Common.md#Common.CurrencyExchangeRateChangeLog), [CurrencyExchangeRates](Common.md#Common.CurrencyExchangeRate)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting), [AdditionRecordings](TimeRecording.md#TimeRecording.AdditionRecording), [Alloys](Inventory.md#Inventory.Alloy), [AttendanceAdditions](TimeRecording.md#TimeRecording.AttendanceAddition), [BankAccounts](Accounting.md#Accounting.BankAccount), [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales), [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow), [BookingRows](Accounting.md#Accounting.BookingRow), [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount), [CaseEntryActivities](Inventory.md#Inventory.CaseEntryActivity), [CaseEntryAdditionalCost](Inventory.md#Inventory.CaseEntryAdditionalCost), [CaseManagementActivities](Inventory.md#Inventory.CaseManagementActivity), [CaseManagementCost](Inventory.md#Inventory.CaseManagementCost), [CaseManagementTemplateCosts](Inventory.md#Inventory.CaseManagementTemplateCost), [Companies](Common.md#Common.Company), [Countries](Common.md#Common.Country), [CurrencyExchangeRateChangeLogs](Common.md#Common.CurrencyExchangeRateChangeLog), [CustomerOrderInvoiceOrderRowDiscounts](Sales.md#Sales.CustomerOrderInvoiceOrderRowDiscount), [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrderOrderRowDiscounts](Sales.md#Sales.CustomerOrderOrderRowDiscount), [CustomerOrderPaymentPlanRows](Sales.md#Sales.CustomerOrderPaymentPlanRow), [CustomerOrderRowInflows](Sales.md#Sales.CustomerOrderRowInflow), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerPartLinks](Sales.md#Sales.CustomerPartLink), [Customers](Sales.md#Sales.Customer), [IncomingPayments](Accounting.md#Accounting.IncomingPayment), [Inquiries](Purchase.md#Purchase.Inquiry), [InquiryRows](Purchase.md#Purchase.InquiryRow), [Money](Common.md#Common.Money), [OpeningBalances](Accounting.md#Accounting.OpeningBalance), [OperationRows](Manufacturing.md#Manufacturing.OperationRow), [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment), [PartConfigurationResults](Common.md#Common.PartConfigurationResult), [PartConfigurationSelectionGroupResults](Common.md#Common.PartConfigurationSelectionGroupResult), [Parts](Inventory.md#Inventory.Part), [PriceChangeLogs](Inventory.md#Inventory.PriceChangeLog), [PriceLists](Common.md#Common.PriceList), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [QuoteOrderRowDiscounts](Sales.md#Sales.QuoteOrderRowDiscount), [QuoteRows](Sales.md#Sales.QuoteRow), [Quotes](Sales.md#Sales.Quote), [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRowInflows](Sales.md#Sales.SalesAgreementRowInflow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow), [SalesAgreements](Sales.md#Sales.SalesAgreement), [SalesPrices](Sales.md#Sales.SalesPrice), [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms), [Shipments](Sales.md#Sales.Shipment), [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink), [Suppliers](Purchase.md#Purchase.Supplier), [VoucherRows](Accounting.md#Accounting.VoucherRow)

<a id="Common.CurrencyExchangeRateChangeLog"></a>
### CurrencyExchangeRateChangeLogs

Represents a currency exchange rate entry.

- **Endpoint:** `GET /api/v1/Common/CurrencyExchangeRateChangeLogs`
- **Required permission:** Show currencies
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the currency exchange rate change log entry. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The currency exchange type of the entry. |
| `Rate` | `Decimal` | no |  | The exchange rate of the entry. |
| `ValidUntilDate` | `DateTimeOffset` | no |  | The date when entry was changed. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency the exchange rate log entry belongs to. |

**References out:** [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType)
**Referenced by:** [Currencies](Common.md#Common.Currency)

<a id="Common.CurrencyExchangeRate"></a>
### CurrencyExchangeRates

Represents a currency exchange rate entry.

- **Endpoint:** `GET /api/v1/Common/CurrencyExchangeRates`
- **Required permission:** Show currencies
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the currency exchange rate entry. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The currency exchange type of the entry. |
| `Rate` | `Decimal` | no |  | The exchange rate of the entry. |

**References out:** [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType)
**Referenced by:** [Currencies](Common.md#Common.Currency)

<a id="Common.CurrencyExchangeType"></a>
### CurrencyExchangeTypes

Represents a currency exchange type.

- **Endpoint:** `GET /api/v1/Common/CurrencyExchangeTypes`
- **Required permission:** Show currencies
- **Introduced in:** 22.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the currency exchange type. |
| `Description` | `String` | no |  | The translated description of the currency exchange type. |
| `IsDefaultAFSRate` | `Boolean` | no |  | Specifies if default AFS rate. |

**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderPurchaseTypes](Purchase.md#Purchase.BlanketOrderPurchaseType), [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales), [BlanketOrderSalesTypes](Sales.md#Sales.BlanketOrderSalesType), [CurrencyExchangeRateChangeLogs](Common.md#Common.CurrencyExchangeRateChangeLog), [CurrencyExchangeRates](Common.md#Common.CurrencyExchangeRate), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType), [Customers](Sales.md#Sales.Customer), [Inquiries](Purchase.md#Purchase.Inquiry), [InquiryTypes](Purchase.md#Purchase.InquiryType), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [PurchaseOrderTypes](Purchase.md#Purchase.PurchaseOrderType), [Quotes](Sales.md#Sales.Quote), [QuoteTypes](Sales.md#Sales.QuoteType), [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Common.CustomReportDefinition"></a>
### CustomReportDefinitions

Represents a queryable custom report definition.

- **Endpoint:** `GET /api/v1/Common/CustomReportDefinitions`
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the custom report. |
| `ReportNumber` | `String` | no |  | The report number of the custom report. |
| `Description` | `String` | no |  | The translated description of the custom report. |
| `DisplayDefinitions` | `CustomReportDisplayDefinitions[]` | no | [CustomReportDisplayDefinitions](Common.md#Common.CustomReportDisplayDefinition) | A collection of display definitions belonging to the custom report definition. |

**References out:** [CustomReportDisplayDefinitions](Common.md#Common.CustomReportDisplayDefinition)
**Referenced by:** [CustomReportDisplayDefinitions](Common.md#Common.CustomReportDisplayDefinition)

<a id="Common.CustomReportDisplayDefinition"></a>
### CustomReportDisplayDefinitions

Represents a queryable custom report display definition.

- **Endpoint:** `GET /api/v1/Common/CustomReportDisplayDefinitions`
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the custom report display definition. |
| `DisplayId` | `Guid` | no |  | The identifier of the custom report display definition. |
| `Description` | `String` | no |  | The translated description of the custom report display definition. |
| `ReportType` | `Int32` | no |  | The report type of the custom report display definition. |
| `Sql` | `String` | no |  | The SQL query of the custom report display definition. |
| `ParentId` | `Int64` | no | [CustomReportDefinitions](Common.md#Common.CustomReportDefinition) | The business key identifier of the parent custom report definition. References CustomReportDefinitions . |

- `ReportType` — Grid=0, Report=1, SubReport=2

**References out:** [CustomReportDefinitions](Common.md#Common.CustomReportDefinition)
**Referenced by:** [CustomReportDefinitions](Common.md#Common.CustomReportDefinition)

<a id="Common.DelegatedWork"></a>
### DelegatedWork

Represents a delegated work.

- **Endpoint:** `GET /api/v1/Common/DelegatedWork`
- **Required permission:** Show Activity list – Project
- **Introduced in:** 2.50

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the delegated work. |
| `WorkRecordingType` | `Int32` | no |  | The work recording type of the delegated work. |
| `DelegatedBy` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the user who delegated the work. |
| `EmployeeId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the employee the work is delegated to. |
| `ActivityId` | `Int64?` | yes | [ProjectActivities](Common.md#Common.ProjectActivity) | The business key identifier of the delegated work's activity. |
| `OperationId` | `Int64?` | yes | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) | The business key identifier of the delegated work's operation. |

- `WorkRecordingType` — Indirect=0, OperationSetup=1, OperationUnit=2, ProjectActivity=3

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [Persons](Common.md#Common.Person), [ProjectActivities](Common.md#Common.ProjectActivity)

<a id="Common.DeliveryAddress"></a>
### DeliveryAddresses

Represents a delivery address.

- **Endpoint:** `GET /api/v1/Common/DeliveryAddresses`
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the address. |
| `Addressee` | `String` | no |  | The addressee of the address. |
| `Field1` | `String` | no |  | The first field of the address. |
| `Field2` | `String` | no |  | The second field of the address. |
| `Field3` | `String` | no |  | The third field of the address. |
| `Field4` | `String` | no |  | The fourth field of the address. |
| `Field5` | `String` | no |  | The fifth field of the address. |
| `Locality` | `String` | no |  | The locality of the address. |
| `Region` | `String` | no |  | The region of the address. |
| `PostalCode` | `String` | no |  | The postal code of the address. |
| `AddressFormatType` | `Int32` | no |  | The format type of the address. |
| `CountryId` | `Int64` | no | [Countries](Common.md#Common.Country) | References Countries . |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The business key identifier of the language code. References LanguageCodes . |
| `FormReportTranslationGroupId` | `Int64` | no |  | The business key identifier of the form report translation group. References FormReportTranslationGroup. |
| `PostalCodeId` | `Int64?` | yes |  | The business key identifier of the postal code. References PostalCode. _(Unavailable)_ |
| `IsDefault` | `Boolean` | no |  | Specifies if this is the default delivery address. |
| `AddressId` | `Int64` | no | [Addresses](Common.md#Common.Address) | References Addresses . |
| `ConsigneeReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | References BusinessContactReferences . |
| `ConsigneeReferenceName` | `String` | no |  | The consignee reference name of the delivery address. |
| `Destination` | `String` | no |  | The destination of the delivery address. |
| `DeliveryWeekdays` | `Int32` | no |  | Specifies which days delivery can be made to the delivery address. _(Can be found under Warehouses)_ |
| `DeliveryInstruction` | `String` | no |  | The instruction of delivery for the delivery address. |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) | The business key identifier of the VatRate of the delivery address. References VatRates . |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The business key identifier of the customer account group of the delivery address. References CustomerAccountGroups . |
| `SupplierAccountGroupId` | `Int64?` | yes |  | The business key identifier of the supplier account group of the delivery address. References SupplierAccountGroup. |
| `VatGroupId` | `Int64?` | yes | [VatGroups](Common.md#Common.VatGroup) | The business key identifier of the VAT group that the delivery address belongs to. References VatGroups . |
| `VatNumber` | `String` | no |  | Vat registration number to be set on delivery address |
| `Warehouses` | `DeliveryAddressWarehouseInformations[]` | no | [DeliveryAddressWarehouseInformations](Common.md#Common.DeliveryAddressWarehouseInformation) | The warehouse information that belongs to the delivery address. |

- `DeliveryWeekdays` (bitmask) — None=0, Monday=1, Tuesday=2, Wednesday=4, Thursday=8, Friday=16, Saturday=32, Sunday=64

**References out:** [Addresses](Common.md#Common.Address), [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Countries](Common.md#Common.Country), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [DeliveryAddressWarehouseInformations](Common.md#Common.DeliveryAddressWarehouseInformation), [LanguageCodes](Common.md#Common.LanguageCode), [VatGroups](Common.md#Common.VatGroup), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [Customers](Sales.md#Sales.Customer), [DeliveryAddressWarehouseInformations](Common.md#Common.DeliveryAddressWarehouseInformation), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Shipments](Sales.md#Sales.Shipment), [Suppliers](Purchase.md#Purchase.Supplier), [Warehouses](Common.md#Common.Warehouse)

<a id="Common.DeliveryAddressWarehouseInformation"></a>
### DeliveryAddressWarehouseInformations

Represents a queryable delivery address warehouse information entry.

- **Endpoint:** `GET /api/v1/Common/DeliveryAddressWarehouseInformations`
- **Introduced in:** 2.43

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the warehouse information entry. |
| `WarehouseId` | `Int64?` | yes | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the information pertains to. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](Common.md#Common.DeliveryMethod) | The business key identifier of the delivery method that applies to the warehouse and delivery address. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](Common.md#Common.DeliveryTerm) | The business key identifier of the delivery term that applies to the warehouse and delivery address. |
| `TransportTime` | `TimeSpan?` | yes |  | The transport time that applies to the warehouse and delivery address. |
| `DeliveryWeekdays` | `Int32` | no |  | Specifies what days delivery can be made for the warehouse and delivery address. |
| `DestinationForDeliveryTerm` | `String` | no |  | Specifies the destination for the delivery term. |
| `ParentId` | `Int64` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | The business key identifier of the delivery address that the warehouse information pertains to. |

- `DeliveryWeekdays` (bitmask) — None=0, Monday=1, Tuesday=2, Wednesday=4, Thursday=8, Friday=16, Saturday=32, Sunday=64

**References out:** [DeliveryAddresses](Common.md#Common.DeliveryAddress), [DeliveryMethods](Common.md#Common.DeliveryMethod), [DeliveryTerms](Common.md#Common.DeliveryTerm), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [DeliveryAddresses](Common.md#Common.DeliveryAddress)

<a id="Common.DeliveryMethod"></a>
### DeliveryMethods

Represents a queryable delivery method.

- **Endpoint:** `GET /api/v1/Common/DeliveryMethods`
- **Required permission:** Show terms
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the delivery method. |
| `IsDefault` | `Boolean` | no |  | Specifies if the delivery method is the default method. |
| `Number` | `Int64` | no |  | The delivery method number. |
| `Description` | `String` | no |  | The translated description of the delivery method. |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the delivery method supplier. References Suppliers . |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |
| `ShippingServiceId` | `Int64?` | yes |  | The business key identifier of the delivery method shipping service. References ShippingService. |
| `ShippingTemplateId` | `Int64?` | yes |  | The business key identifier of the delivery method shipping template. References ShippingTemplate. |
| `Code` | `String` | no |  | The code of the delivery method. |

**References out:** [Suppliers](Purchase.md#Purchase.Supplier)
**Referenced by:** [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [DeliveryAddressWarehouseInformations](Common.md#Common.DeliveryAddressWarehouseInformation), [Inquiries](Purchase.md#Purchase.Inquiry), [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Quotes](Sales.md#Sales.Quote), [SalesAgreements](Sales.md#Sales.SalesAgreement), [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms), [Shipments](Sales.md#Sales.Shipment)

<a id="Common.DeliveryTerm"></a>
### DeliveryTerms

Represents a queryable delivery term.

- **Endpoint:** `GET /api/v1/Common/DeliveryTerms`
- **Required permission:** Show terms
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the delivery term. |
| `IsDefault` | `Boolean` | no |  | Specifies if the delivery term is the default term. |
| `Description` | `String` | no |  | The translated description of the delivery term. |
| `Number` | `Int64` | no |  | The delivery term number. |
| `Destination` | `String` | no |  | The destination specified by the delivery term. |
| `TermLocation` | `String` | no |  | The location specified by the delivery term. |
| `TermCode` | `String` | no |  | The code specified by the delivery term. |
| `Payer` | `Int32` | no |  | Specifies how payment is handled for the delivery term. |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |
| `ShipmentDefaultCode` | `String` | no |  | The shipment default code specified by the delivery term. |

- `Payer` — BuyerPays=1, SellerPays=2, OtherPayer=3, Incoterms=4

**Referenced by:** [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [DeliveryAddressWarehouseInformations](Common.md#Common.DeliveryAddressWarehouseInformation), [Inquiries](Purchase.md#Purchase.Inquiry), [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Quotes](Sales.md#Sales.Quote), [SalesAgreements](Sales.md#Sales.SalesAgreement), [Shipments](Sales.md#Sales.Shipment)

<a id="Common.DeliveryTime"></a>
### DeliveryTimes

Represents a queryable delivery time.

- **Endpoint:** `GET /api/v1/Common/DeliveryTimes`
- **Required permission:** Show terms
- **Introduced in:** 23.6

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the delivery time. |
| `Days` | `Int32` | no |  | The number of days until delivery of the delivery time. |
| `Description` | `String` | no |  | The translated description of the delivery time. |
| `Number` | `Int64` | no |  | The delivery time number. |
| `IsDefault` | `Boolean` | no |  | Specifies if the delivery time is the default time. |

**Referenced by:** [Quotes](Sales.md#Sales.Quote)

<a id="Common.Department"></a>
### Departments

Represents a queryable department.

- **Endpoint:** `GET /api/v1/Common/Departments`
- **Required permission:** Show departments
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the department. |
| `Code` | `String` | no |  | The human readable code of the department. |
| `Description` | `String` | no |  | The translated description of the department. |

**Referenced by:** [CaseEntry](Inventory.md#Inventory.CaseEntry), [FixedAssets](Accounting.md#Accounting.FixedAsset), [Persons](Common.md#Common.Person)

<a id="Common.DiscountCategory"></a>
### DiscountCategories

Represents a queryable discount category.

- **Endpoint:** `GET /api/v1/Common/DiscountCategories`
- **Required permission:** Show discount categories
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the discount category. |
| `Number` | `String` | no |  | The discount category number. |
| `Description` | `String` | no |  | The translated description of the discount category. |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |
| `Rows` | `DiscountCategoryRows[]` | no | [DiscountCategoryRows](Common.md#Common.DiscountCategoryRow) | The rows for the discount category. |

**References out:** [DiscountCategoryRows](Common.md#Common.DiscountCategoryRow)
**Referenced by:** [Customers](Sales.md#Sales.Customer), [DiscountCategoryRows](Common.md#Common.DiscountCategoryRow), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Common.DiscountCategoryRow"></a>
### DiscountCategoryRows

Represents a discount category row.

- **Endpoint:** `GET /api/v1/Common/DiscountCategoryRows`
- **Required permission:** Show discount categories
- **Introduced in:** 22.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the row. |
| `DiscountCategoryId` | `Int64` | no | [DiscountCategories](Common.md#Common.DiscountCategory) | The business key identifier of the discount category this row belongs to. |
| `BoundaryType` | `Int32` | no |  | The boundary type of the row. |
| `ProductGroupId` | `Int64?` | yes | [ProductGroups](Common.md#Common.ProductGroup) | The business key identifier of the product group for this row. |
| `PartCodeId` | `Int64?` | yes | [PartCodes](Inventory.md#Inventory.PartCode) | The business key identifier of the part code for this row. |
| `PartCategory` | `String` | no |  | The part category for this row. |
| `Boundary1` | `Decimal` | no |  | The first boundary of this row. |
| `Discount1` | `Decimal` | no |  | The discount for the first boundary of this row. |
| `Boundary2` | `Decimal` | no |  | The second boundary of this row. |
| `Discount2` | `Decimal` | no |  | The discount for the second boundary of this row. |
| `Boundary3` | `Decimal` | no |  | The third boundary of this row. |
| `Discount3` | `Decimal` | no |  | The discount for the third boundary of this row. |
| `Boundary4` | `Decimal` | no |  | The fourth boundary of this row. |
| `Discount4` | `Decimal` | no |  | The discount for the fourth boundary of this row. |
| `Boundary5` | `Decimal` | no |  | The fifth boundary of this row. |
| `Discount5` | `Decimal` | no |  | The discount for the fifth boundary of this row. |
| `Boundary6` | `Decimal` | no |  | The sixth boundary of this row. |
| `Discount6` | `Decimal` | no |  | The discount for the sixth boundary of this row. |
| `Boundary7` | `Decimal` | no |  | The seventh boundary of this row. |
| `Discount7` | `Decimal` | no |  | The discount for the seventh boundary of this row. |
| `Boundary8` | `Decimal` | no |  | The eighth boundary of this row. |
| `Discount8` | `Decimal` | no |  | The discount for the eighth boundary of this row. |
| `Boundary9` | `Decimal` | no |  | The ninth boundary of this row. |
| `Discount9` | `Decimal` | no |  | The discount for the ninth boundary of this row. |
| `Boundary10` | `Decimal` | no |  | The tenth boundary of this row. |
| `Discount10` | `Decimal` | no |  | The discount for the tenth boundary of this row. |

- `BoundaryType` — Quantity=0, Value=1

**References out:** [DiscountCategories](Common.md#Common.DiscountCategory), [PartCodes](Inventory.md#Inventory.PartCode), [ProductGroups](Common.md#Common.ProductGroup)
**Referenced by:** [DiscountCategories](Common.md#Common.DiscountCategory)

<a id="Common.Discount"></a>
### Discounts

Represents a queryable discount.

- **Endpoint:** `GET /api/v1/Common/Discounts`
- **Required permission:** Show discounts
- **Introduced in:** 24.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the discount. |
| `Code` | `String` | no |  | The human readable identifier of the discount. |
| `Name` | `String` | no |  | The translated name of the discount. |
| `IsActive` | `Boolean` | no |  | Specifies if the discount is active. |
| `IsDefault` | `Boolean` | no |  | Specifies if this is the default discount for the discount type. |
| `DiscountForModule` | `Int32` | no |  | The sales or purchase module of the discount. |
| `DiscountType` | `Int32` | no |  | The type of the discount. |
| `Priority` | `Int32` | no |  | The priority of the discount. |
| `DiscountCalculationType` | `Int32` | no |  | The calculation type of the discount. |

- `DiscountForModule` — Sales=0
- `DiscountType` — Discount=0, OrderDiscount=1, TotalRowDiscount=2, ProjectDiscount=3, CustomerDiscountOnDiscount=4, OrderTypeDiscount=5, ManualDiscount=99
- `DiscountCalculationType` — Percent=1, Amount=2

**Referenced by:** [CustomerOrderInvoiceOrderRowDiscounts](Sales.md#Sales.CustomerOrderInvoiceOrderRowDiscount), [CustomerOrderOrderRowDiscounts](Sales.md#Sales.CustomerOrderOrderRowDiscount), [QuoteOrderRowDiscounts](Sales.md#Sales.QuoteOrderRowDiscount)

<a id="Common.EdiBehavior"></a>
### EdiBehaviors

Represents an Edi Behavior

- **Endpoint:** `GET /api/v1/Common/EdiBehaviors`
- **Required permission:** Show EDI settings
- **Introduced in:** 25.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the edi behaviour. |
| `Name` | `String` | no |  | The name of the edi behaviour. |
| `Module` | `Int32` | no |  | The module of the edi behaviour. |
| `EdiChannelConfigurations` | `EdiChannelConfigurations[]` | no | [EdiChannelConfigurations](Common.md#Common.EdiChannelConfiguration) | The edi channel configurations of edi behavior. |
| `Customers` | `Customers[]` | no | [Customers](Sales.md#Sales.Customer) | The customer of edi behavior. |
| `InvoiceCustomers` | `Customers[]` | no | [Customers](Sales.md#Sales.Customer) | The invoice customers of edi behavior. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse. |
| `Warehouse` | `Warehouses` | no | [Warehouses](Common.md#Common.Warehouse) | The warehouse of the edi behavior. |

- `Module` — None=0, Sales=1, Purchase=2

**References out:** [Customers](Sales.md#Sales.Customer), [EdiChannelConfigurations](Common.md#Common.EdiChannelConfiguration), [Warehouses](Common.md#Common.Warehouse)

<a id="Common.EdiChannelConfiguration"></a>
### EdiChannelConfigurations

Represents an Edi Channel Configuration.

- **Endpoint:** `GET /api/v1/Common/EdiChannelConfigurations`
- **Introduced in:** 25.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the edi channel configuration. |
| `ParentId` | `Int64` | no |  | The parent id of the edi channel configuration. |
| `ChannelId` | `Int64` | no |  | The channel id of the edi channel configuration. |
| `NotificationsActive` | `Boolean` | no |  | The notification active identifier of the edi channel configuration. |
| `Active` | `Boolean` | no |  | The active of the edi channel configuration. |

**Referenced by:** [EdiBehaviors](Common.md#Common.EdiBehavior)

<a id="Common.EmploymentPeriod"></a>
### EmploymentPeriods

Represents the employment period of a personnel record.

- **Endpoint:** `GET /api/v1/Common/EmploymentPeriods`
- **Required permission:** Show person
- **Introduced in:** 22.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the employment period. |
| `StartDate` | `DateTimeOffset` | no |  | The start date of the employment period. |
| `FinishDate` | `DateTimeOffset?` | yes |  | The finish date of the employment period. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the comment that belongs to the employment period. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment that belongs to the employment period. |
| `PersonId` | `Int64` | no | [Persons](Common.md#Common.Person) | The business key identifier of the personnel record that the employment period belongs to. |
| `RowIndex` | `Int32` | no |  | The ordered row index of the employment period. |

**References out:** [Comments](Common.md#Common.Comment), [Persons](Common.md#Common.Person)
**Referenced by:** [Persons](Common.md#Common.Person)

<a id="Common.EntityChangeLog"></a>
### EntityChangeLogs

Represents a queryable entity changelog entry.

- **Endpoint:** `GET /api/v1/Common/EntityChangeLogs`
- **Required permission:** Show changelog
- **Introduced in:** 2.33

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the changelog entry. |
| `ChangeType` | `Int32` | no |  | The type of change that was made to the entity. |
| `EntityTypeId` | `Guid` | no |  | The GUID of the changed entity's type. |
| `EntityId` | `Int64` | no |  | The business key identifier of the changed entity. |
| `ModifiedBy` | `String` | no |  | The human readable identifier of the application user that performed the change. |
| `ModifiedTimestamp` | `DateTimeOffset` | no |  | The date when the change was made. |
| `AssociatedTypeId` | `Guid?` | yes |  | The GUID of the changed entity's parent type. |
| `AssociatedEntityId` | `Int64?` | yes |  | The business key identifier of the changed entity's parent. |
| `EntityCode` | `String` | no |  | The human readable identifier of the changed entity. |
| `Changes` | `EntityPropertyChanges[]` | no | [EntityPropertyChanges](Common.md#Common.EntityPropertyChange) | The property changes for this entity. |
| `Remark` | `String` | no |  | Holds extra information about the change. |

- `ChangeType` — Update=0, Create=1, Delete=2

**References out:** [EntityPropertyChanges](Common.md#Common.EntityPropertyChange)

<a id="Common.EntityPropertyChange"></a>
### EntityPropertyChanges

Represents a queryable entity property change entry.

- **Endpoint:** `GET /api/v1/Common/EntityPropertyChanges`
- **Required permission:** Show changelog
- **Introduced in:** 2.33

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the property change entry. |
| `MemberName` | `String` | no |  | The path to the property where the change occured. |
| `OldValue` | `String` | no |  | The value of the property before the change. |
| `NewValue` | `String` | no |  | The value of the property after the change. |
| `ChangeType` | `Int32` | no |  | The type of change that was made to the property. |
| `EntityChangeLogId` | `Int64` | no |  | The business key identifier of the property's change log |

- `ChangeType` — Update=0, Create=1, Delete=2

**Referenced by:** [EntityChangeLogs](Common.md#Common.EntityChangeLog)

<a id="Common.ExtraFieldGroup"></a>
### ExtraFieldGroups

Represents an extra field group.

- **Endpoint:** `GET /api/v1/Common/ExtraFieldGroups`
- **Required permission:** Show extra fields
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the extra field group. |
| `Name` | `String` | no |  | The translated name of the extra field group. |
| `EntityId` | `Guid` | no |  | The business-domain identifier of the entity that the extra field group is defined for. |
| `RowNumber` | `Int32` | no |  | The row number of the extra field group. |
| `Templates` | `ExtraFieldTemplates[]` | no | [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate) | A collection of extra field templates that belong to the extra field group. |

**References out:** [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate)
**Referenced by:** [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate)

<a id="Common.ExtraFieldOptionTemplate"></a>
### ExtraFieldOptionTemplates

Represents an extra field option template.

- **Endpoint:** `GET /api/v1/Common/ExtraFieldOptionTemplates`
- **Required permission:** Show extra fields
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the extra field option template. |
| `Code` | `String` | no |  | The human readable code of the extra field option template. |
| `IsActive` | `Boolean` | no |  | Specifies whether or not the extra field option template is active in the system. |
| `Description` | `String` | no |  | The translated description of the extra field option template. |
| `ExtraFieldTemplateId` | `Int64` | no | [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate) | The business key identifier of the extra field template that the extra field option template belongs to. |

**References out:** [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate)
**Referenced by:** [ExtraFields](Common.md#Common.ExtraField), [ExtraFieldTemplates](Common.md#Common.ExtraFieldTemplate)

<a id="Common.ExtraField"></a>
### ExtraFields

Represents an extra field.

- **Endpoint:** `GET /api/v1/Common/ExtraFields`
- **Required permission:** Show extra fields
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the extra field. |
| `ParentClass` | `Guid` | no |  | The GUID of the parent type. |
| `ParentId` | `Int64` | no |  | The business key identifier of the parent. |
| `Identifier` | `String` | no |  | The alphanumeric identifier of the extra field template. |
| `Type` | `Int32` | no |  | The extra field template type. |
| `StringValue` | `String` | no |  | The string value of the extra field. |
| `IntegerValue` | `Int32?` | yes |  | The integer value of the extra field. |
| `DecimalValue` | `Decimal?` | yes |  | The decimal value of the extra field. |
| `DateOnlyValue` | `DateTimeOffset?` | yes |  | The date-only value of the extra field. |
| `DateTimeValue` | `DateTimeOffset?` | yes |  | The date-time value of the extra field. |
| `SelectedOptionId` | `Int64?` | yes | [ExtraFieldOptionTemplates](Common.md#Common.ExtraFieldOptionTemplate) | The business key identifier of the selected option. References ExtraFieldOptionTemplates . |
| `SelectedOption` | `ExtraFieldOptionTemplates` | no | [ExtraFieldOptionTemplates](Common.md#Common.ExtraFieldOptionTemplate) | The selected option of the extra field. Only applicable to extra fields of type 6 (Options). |
| `SelectedOptionIds` | `String` | no | [ExtraFieldOptionTemplates](Common.md#Common.ExtraFieldOptionTemplate) | A comma separated value list of the selected options. References multiple ExtraFieldOptionTemplates . |
| `SelectedOptions` | `ExtraFieldOptionTemplates[]` | no | [ExtraFieldOptionTemplates](Common.md#Common.ExtraFieldOptionTemplate) | The selected options of the extra field. Only applicable to extra fields of type 7 (Multiple options). |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the comment value of the extra field. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment value of the extra field. |

**References out:** [Comments](Common.md#Common.Comment), [ExtraFieldOptionTemplates](Common.md#Common.ExtraFieldOptionTemplate)
**Referenced by:** [CaseEntry](Inventory.md#Inventory.CaseEntry), [Customers](Sales.md#Sales.Customer), [OperationRows](Manufacturing.md#Manufacturing.OperationRow), [Parts](Inventory.md#Inventory.Part), [Persons](Common.md#Common.Person), [ProductRecords](Inventory.md#Inventory.ProductRecord), [Projects](Common.md#Common.Project), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Common.ExtraFieldTemplate"></a>
### ExtraFieldTemplates

Represents an extra field template.

- **Endpoint:** `GET /api/v1/Common/ExtraFieldTemplates`
- **Required permission:** Show extra fields
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the extra field template. |
| `Name` | `String` | no |  | The translated name of the extra field template. |
| `Description` | `String` | no |  | The translated description of the extra field template. |
| `Type` | `Int32` | no |  | The extra field template type. |
| `ParentId` | `Int64` | no | [ExtraFieldGroups](Common.md#Common.ExtraFieldGroup) | The business key identifier of the extra field group that the template belongs to. |
| `RowNumber` | `Int32` | no |  | The row number of the extra field template. |
| `Identifier` | `String` | no |  | The alphanumeric identifier of the extra field template. |
| `OptionTemplates` | `ExtraFieldOptionTemplates[]` | no | [ExtraFieldOptionTemplates](Common.md#Common.ExtraFieldOptionTemplate) | The extra field option templates that belong to the extra field template. |

- `Type` — String=0, Integer=1, Decimal=2, Date=3, DateTime=4, Comment=5, Options=6, MultiOptions=7

**References out:** [ExtraFieldGroups](Common.md#Common.ExtraFieldGroup), [ExtraFieldOptionTemplates](Common.md#Common.ExtraFieldOptionTemplate)
**Referenced by:** [ExtraFieldGroups](Common.md#Common.ExtraFieldGroup), [ExtraFieldOptionTemplates](Common.md#Common.ExtraFieldOptionTemplate), [Preparations](Manufacturing.md#Manufacturing.Preparation)

<a id="Common.FilePath"></a>
### FilePaths

Represents a queryable file path.

- **Endpoint:** `GET /api/v1/Common/FilePaths`
- **Required permission:** Show paths
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the file path. |
| `Path` | `String` | no |  | The server-local path of the file path. |
| `Description` | `String` | no |  | The description of the file path. |
| `Active` | `Boolean` | no |  | Specifies whether the file path is active or not. |
| `Category` | `Int32` | no |  | The category of the file path. |
| `FileType` | `Int32` | no |  | The file type of the file path. |
| `PathType` | `Int32` | no |  | The path type of the file path. |

- `Category` — FileViewer=1, ExportAccounting=2, ExportAgent=3, ExportFactoring=4, ExportServerPrinter=5, ImportAccounting=6, ImportSerialNumbers=7, ImportAdditionalIds=8
- `FileType` — FileSystem=0, SharePoint=1
- `PathType` (bitmask) — LocalServerDrives=1, UncServerShare=2, SharePoint=4, AvailablePaths=8, RegisteredPaths=16, LocalClient=32

**Referenced by:** [ServerPrinters](Common.md#Common.ServerPrinter)

<a id="Common.FormReportConfiguration"></a>
### FormReportConfigurations

Represents a form report configuration.

- **Endpoint:** `GET /api/v1/Common/FormReportConfigurations`
- **Introduced in:** 2.36

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the form report configuration. |
| `Type` | `Int32` | no |  | Type of form report. When querying the value retrieved this is converted from the new Guid Type property to the old Enum type. _(Replaced by TypeId. $filter and $orderby cannot be used with this property. Use TypeId instead)_ |
| `TypeId` | `Guid` | no |  | Id of form report Type. Translation for each guid is shown if existing. Each TypeId also has a corresponding FormReportType listed in parenthesis. None: 00000000-0000-0000-0000-000000000000 (NotInitialized:0) Quote: eafce8bd-64c1-4bee-bf64-1d4389adce5f (Quote:1) Order confirmation: e013402a-73cb-4d6f-8b53-cac95c7f709a (Acknowledgement:3) Delivery note: dc7d6709-e4b9-41e1-8ca4-96d24a69d6ba (CustomerDeliveryNote:5) Delivery note, delivered: 8dda82c8-c394-451f-821c-75bbf2955f4e (CustomerDeliveryNoteDelivered:6) Invoice: 932cfa90-7499-43da-bc16-d049c688cc07 (Invoice:7) Comprehensive delivery note: 4bac9892-9e62-4d8f-8234-ae4da535e506 (CustomerDeliveryNoteCollectionDelivered:8) Transport label, sales: 0ce06331-f6ab-4383-97e7-9e9cc32930a8 (SalesTransportLabelA4:16) Comprehensive invoice: 97578728-4aab-4a6f-9a41-91d4202e9d41 (ComprehensiveInvoice:17) Purchase order: bcfe8d1d-860c-413b-bd33-1917a0ea34af (PurchaseOrder:22) Order confirmation reminder: f673f852-cd1c-419a-981a-d61d6a979e8e (PurchaseOrderConfirmationReminder:23) Order confirmation reminder (stray supplier): 3a508aa4-91be-4d56-8631-8f5218acec16 (PurchaseOrderConfirmationReminderCasualSupplier:24) Delivery reminder: 836d0088-7819-48b1-8cb9-6c41c4a034c6 (PurchaseOrderDeliveryConfirmationReminder:25) Delivery reminder (stray supplier): 9a5035b7-625e-4fa6-9309-0ce3643753a7 (PurchaseOrderDeliveryConfirmationReminderCasualSupplier:26) Transport label, purchase: 61319239-2b20-4514-8101-611178f1c116 (PurchaseTransportLabel:31) Pick list – Ready for delivery: f1e25675-553d-4f1e-9443-dba517f7949e (PickingList:100) Inspection report: 97db03da-93f5-42ca-97d7-a39370645a45 (InspectionReport:101) Transport label, purchase, rejected: bd606210-1bc7-43c3-a6f3-30a8d8010202 (PurchaseTransportLabelForRejection:102) Pro forma invoice: 91033be4-c02d-44cc-8a24-d3eacaf23fd7 (ProformaInvoice:103) Pro forma – Comprehensive invoice: ec6f7da0-072c-47f6-8c77-b0aef3c260d8 (ComprehensiveProformaInvoice:104) Transport label, manufacturing, transfer to stock: 0f880b25-2013-4d80-bfe2-fa20b53df9e0 (ManufacturingTransportLabelA4:105) Transport label, manufacturing, rejected: 6b7bb6f1-593f-412c-8c93-547674ef43fe (ManufacturingTransportLabelA4ForRejection:106) Transport label, manufacturing, in progress: 6a8529fa-5fba-4836-8a69-6d2928f82599 (ManufacturingTransportLabelA4InProgress:107) Transport label, manufacturing, prior to reporting: 79656978-0310-45c4-abeb-1faed6be1a8b (ManufacturingTransportLabelA4BeforeReporting:108) Operation document: 1bff7361-d75e-4698-a0ba-e088abc9f0c5 (ManufacturingOrderOperation:109) Material document: e974a3ec-198a-421c-8a79-40930451b2ed (ManufacturingOrderMaterial:110) Traveler: bc91d33e-8b31-451a-bfd2-d941f101ddc8 (ManufacturingOrderTraveler:111) Pre-calculation – Summary: dae6b764-698c-4e48-80cc-f556d903401d (PreCalculationSummary:112) Purchase order (subc.): 2ab68cf7-0885-41d6-8098-162a8f97a4ca (SubcontractPurchaseOrder:113) Delivery note (subc.): dc037f40-02fd-431f-aefd-b03e47efdc10 (SubcontractDeliveryNote:114) Transport label, subcontract: 6927245e-67e2-41b7-af95-2598178dbe66 (SubcontractTransportLabelA4:117) Transport label, subcontract – A5: 28ba8c2d-f45c-46ca-9515-44285e1ab452 (SubcontractTransportLabelA5:118) Transport label, subcontract – Label: ee677374-a11d-453e-a494-045f767ceac2 (SubcontractTransportLabelSmall:119) Included in: 7ca067e4-a6d7-4233-8d22-458430582df7 (LevelListWhereUsedList:120) Consists of: 3f49ed90-e3ac-4af2-bfa0-aac95a90f047 (LevelListConsistsOfList:122) Post-calculation – Summary: 4d9a3c77-0acf-4529-ab64-07c983fb4f73 (PostCalculationSummary:123) Stock count basis: ff8fb009-29fc-440c-93cb-4d1cd6512255 (PhysicalInventoryList:124) Shortage list: e7937a7f-2cd8-4ab5-a831-1e5a2163804d (MaterialClearanceShortageList:125) Accounting order: ef3bf6be-1dd2-45e6-a816-c5d9f7349c67 (AccountingOrder:126) General ledger (drilldown): 65d4227a-f5d4-49e7-b111-2a8fd7bdd25c (GeneralLedgerDrilldown:127) Voucher (drilldown): e977d354-e5c7-4619-bf6a-e313bcf64347 (JournalDrilldown:128) Pick list – Manufacturing, no grouping: ec67174b-f59a-42d7-bfce-1132da7f635c (ManufacturingPickingList:129) Pick list – Manufacturing, grouped by order: 220aa289-ee0f-4748-b13e-0acb0c1e425b (ManufacturingPickingListGroupByOrder:130) Pick list – Manufacturing, grouped by material: 19b12c7e-6657-4f47-9f56-1f92640a15a4 (ManufacturingPickingListGroupByMaterial:131) Accounting report – Header: f1245731-0e98-4362-8e72-a6ed30cd3e71 (AccountingReportHeader:132) Internal invoice: 75f654f5-e2fc-4e05-b560-a1bc464e277b (InternalInvoice:133) Cash receipt: 0ec3ea22-823c-4870-b880-b4d3f33729b0 (CashReceipt:134) Customer invoice journal: cd72d166-edbb-4e2a-8870-803c38fa9480 (AccountsReceivableLedger:135) Reprint – Customer invoice journal: 8d289d30-a1e3-40cb-a741-856d94bc327e (AccountsReceivableLedgerReprint:136) Incoming payment journal: 306a323a-13f6-49df-9634-b626781219df (IncomingPaymentLedger:137) Reprint – Incoming payment journal: 6085f126-9941-4e0f-8b78-dc833af25018 (IncomingPaymentLedgerReprint:138) Supplier invoice journal: f2ac9337-f5f2-4fb6-9767-4ba088fcae78 (AccountsPayableLedger:139) Reprint – Supplier invoice journal: 82688ad3-2233-4d53-a51b-2c210899f545 (AccountsPayableLedgerReprint:140) Preliminary entry journal: d48e6f5a-5fbd-4ceb-ae2d-819c40ed797d (PreliminaryAccountsPayableLedger:141) Reprint – Preliminary entry journal: 31fb0f84-5bfb-4c8e-ba07-8730f7e0500f (PreliminaryAccountsPayableLedgerReprint:142) Cancellation journal of suppl. invoices: fde103f4-abbc-46ee-a1a3-9a23759565a3 (CancelledAccountsPayableLedger:143) Reprint – Cancellation journal of suppl. invoices: 1985401c-ba0b-4dfa-96f4-853ecb3a4a1e (CancelledAccountsPayableLedgerReprint:144) Cancellation journal of prel. entries: a2561f92-14da-4103-9168-019667d46565 (CancelledPreliminaryAccountsPayableLedger:145) Reprint – Cancellation journal of prel. entries: aef26f21-1653-4fff-aab8-12b201153927 (CancelledPreliminaryAccountsPayableLedgerReprint:146) Payment reminder: 218f35dd-3c57-4d70-933e-e8a3e1059274 (PaymentReminder:147) Reprint – Payment reminder: c091e3a4-5119-4288-b175-658dbbdd217b (PaymentReminderReprint:148) Accrual accounting journal: b79e1255-f198-496b-bd02-e695dbaa17aa (AccrualAccountingLedger:149) Reprint – Accrual accounting journal : 2961c4d5-f8c3-41a7-a70f-09e6b4558a63 (AccrualAccountingLedgerReprint:150) VAT report: 923e18d6-e3a4-46d4-86a8-698724116a61 (VatReport:151) VAT report – Accounts: a0634f20-249f-4d7e-93eb-6a3436c26181 (VatReportAccounts:152) VAT report – General ledger: e1615e01-edf9-40e4-a381-e352196b994e (VatReportGeneralLedger:153) VAT report – Transactions: 874e1f9f-9686-4717-ae52-b376af407df8 (VatReportTransactions:154) VAT report – VAT control: 8ac35a6c-3466-421a-bb7d-475822900239 (VatReportCheck:155) VAT report – Find difference: 147eef4b-9cde-4fb0-acaf-526515b5a95b (VatReportDifferenceSearch:156) Transaction list: 0c02e0d3-742a-4564-8ddb-968d297eebc2 (TransactionList:157) Outgoing payment journal: 2f2d5f42-495f-4dda-80d1-e0d7eeae8c6d (OutgoingPaymentLedger:158) Reprint – Outgoing payment journal : d6690ff3-05ab-4557-97da-9c42c874bdf2 (OutgoingPaymentLedgerReprint:159) Transport label, sales – A5: 54da85af-8ec2-4780-b50a-dc13bcf95fd7 (SalesTransportLabelA5:160) Confirmation of customer nonconformity: 920b1dff-ab65-4f19-8b78-4dfbad94ed8d (CustomerCaseConfirmation:161) Statement – Sales: 1194287c-0812-4cf2-8ab9-10ad023cc258 (AccountStatement:162) Response to customer nonconformity: 115c2889-9c55-462b-aa29-5c0cbd398756 (CustomerCaseAnswer:163) Nonconformity report (internal) (customer noncon.): 75461eec-b83d-433c-9dbb-b8ce42c220d2 (CustomerNonconformityReport:164) Nonconformity report (internal) (suppl. noncon.): 760b392d-e4bb-4038-9cfb-de5f23425b14 (SupplierNonconformityReport:165) Nonconformity report (internal) (internal noncon.): 9b6e0da2-0a56-4cba-8c5a-bcb3cf86ff50 (InternalNonconformityReport:166) Claim report: 1ad587c9-da25-420a-beb2-9f7f88f0c676 (SupplierClaimReport:167) Cancellation journal of customer invoices: 2597c873-42f9-4c17-91c5-e6fe4ee55f92 (CancelledAccountsReceivableLedger:168) Reprint – Cancellation journal of customer invoices : 61cfa874-db5a-4209-962a-438e973e1dd4 (CancelledAccountsReceivableLedgerReprint:169) Shipping – Waybill: 54f71041-2f72-460d-88ba-96ad6e8246af (ShipmentWayBill:170) Shipping – Label: b40a4ea5-590e-470a-af77-8e6ba1903cec (ShipmentParcel:171) Inquiry: 1c34fe91-fc5e-4620-8be9-674c307a007a (Inquiry:172) Pick list – By order: c97d45c4-8f05-48c7-9692-e386abcd12f7 (CustomerOrderPickingList:173) EIM – Invoice information: 8011d3f0-beb2-45d0-8e42-1568faf50e37 (EimInvoiceInformation:174) Interest invoice: d88af683-b2a6-4843-aa32-f9bce581e724 (InterestInvoice:175) Files: 6d401da3-1e18-492f-b932-bf8dbe44cd1b (FileLink:176) Recording and total per salary type: af518555-d4f9-4669-821d-028247e072dd (RecordingsAndSalaryTypeSummary:177) Traceability – Consists of: 33d5ca31-5a3a-486a-993e-8e98b1288d2b (ProductRecordConsistsOf:178) Traceability – Included in: 5978216a-ffd6-4922-9cd6-341713652b93 (ProductRecordIncludedIn:179) Internal project report: e518a66d-ba3b-4ff2-acc5-9a9a3c34e95c (InternalProjectReport:180) External project report: 025343d2-1ad7-451c-97c2-4fba3e356106 (ExternalProjectReport:181) Product description incl. certificate: 9693a1e5-b13d-4367-ba56-ef10a14f176a (TraceabilityProtocol:182) Fixed assets journal: 9a7d5961-2a64-45ef-b49f-457d27718752 (FixedAssetLedger:183) Reprint – Fixed assets journal: 4c5061ec-1805-4d34-850e-b60acce40afc (FixedAssetLedgerReprint:184) CustomReport: 743e498a-539b-416d-a42b-cb09cf60d519 (obsolete) (CustomReport:185) Order confirmation – Stock order: 29e7a2f7-0694-4b2d-b8b9-e0a647c7ea36 (StockAcknowledgement:186) Delivery note – Stock order: 63611f39-e8c7-4479-bf29-1d39fca68b75 (StockDeliveryNote:187) Purchase – Stock order: e4531daa-5836-4844-b991-5b819ae40aec (StockPurchaseOrder:188) Delivery note, delivered – Stock order: 1407c853-d6de-4c57-af6c-16633ad6baf0 (StockDeliveryNoteDelivered:189) Modified purchase order: e8e74d3b-ef31-4b2f-aac3-b6573a946621 (PurchaseOrderModified:190) Tax depreciation: 50dbc0fd-3d81-48e2-a1ae-6181c490aea1 (TaxDepreciation:191) Drilldown, tax depreciation: e6586902-bee7-4485-a0c1-e69910d631d7 (TaxDepreciationDrilldown:192) Transport label – Label: 6abd31bf-1a02-4b31-a3a9-17ef2bd5f243 (PartTransportLabelSmall:193) Transport label – A5: 40acea6f-7ded-42e7-a7bd-cdd4a9a2a324 (PartTransportLabelA5:194) Transport label – A4: 7a67a731-dfff-4fc7-ad84-b5b7e5633204 (PartTransportLabelA4:195) Stock reporting journal: 2a6a84b3-7413-457f-bc06-04f36ee7e1fd (UnplannedStockBalanceChangeLedger:196) Reprint – Stock reporting journal: bffda7cc-e95d-46dc-b0af-1db29bdb87c7 (UnplannedStockBalanceChangeLedgerReprint:197) WIP value, detailed: 862cd2bb-2606-48d9-a83c-be50c59b09cf (PIADetailed:198) Stock transaction journal: 373c1669-0c22-4be3-b9f7-0a3de1a78f35 (StockTransactionLogLedger:199) Manufacturing order journal: cf1ff7d9-5619-411d-aabd-baf06fc0b006 (ManufacturingOrderLogLedger:200) Invoicing journal: 2706d19b-59e9-4271-bdf5-a12b54abf5f8 (InvoiceLogLedger:201) Price change journal: 7b746bf0-4088-40c8-8dbb-6f37b2696475 (PriceChangeLogLedger:202) Calculation difference journal: ac22350f-53ef-4eaf-a376-a69229741bcc (CalculationDifferenceLedger:203) Balance per customer: 6f2f383a-04d3-4d4b-84b1-f34ebb627ebf (AccountStatementBalancePerCustomer:204) Reprint – Stock transaction journal: 92c5814f-d1a0-4428-8e21-afdc8b2b9f3a (StockTransactionLogLedgerReprint:205) Reprint – Manufacturing order journal: 4d434ad0-6f1e-4f76-bcc2-9c41fc7979f1 (ManufacturingOrderLogLedgerReprint:206) Reprint – Price change journal: f2b7fe09-73e3-4108-98fd-1cd8a80c716e (PriceChangeLogLedgerReprint:207) Reprint – Calculation difference log journal: 71f539d0-3fbf-4a2f-b789-94997b20e32f (CalculationDifferenceLedgerReprint:208) Reprint – Invoicing journal: 32eb0f25-4a03-479e-8263-332946af2230 (InvoiceLogLedgerReprint:209) Printout demo certificate: 17ec79b8-3df2-48da-bdd8-7ee30277f5ac (PrintoutDemoCertificate:210) Blanket order – Purchase: f0899bd9-7584-4490-a4e2-c28971f1c353 (BlanketOrderPurchase:211) Arrival note: ee277e80-7cbb-4727-8dbb-b1ec55b851a8 (ArrivalNote:212) Correction invoice: acc03146-758b-4eb4-be77-dbe05cd9283c (CorrectionInvoice:213) Modified order confirmation: 4339c24d-bf19-4fbc-9157-9205ce7fd670 (ModifiedOrderConfirmation:214) Delivery schedule – Purchase: b3a15846-9c6b-4d0c-8065-33d8a9e81d39 (PurchaseDeliverySchedule:215) Packing list: f07d7023-3513-46e3-a48d-271d85eb4751 (PackageList:216) Transport label – Package structure: 7a90e262-e1fe-44cd-a393-fba077f59752 (PackageTransportLabel:217) Annual volume: a0a902f4-2da7-414f-861d-5b3d4f5250a7 (AnnualVolumeList:218) Blanket order – Sales: 5fa18c37-34be-4387-a75a-4d7e5f7d17fc (BlanketOrderSales:219) Transport label, direct withdrawal – A4: 41e94543-4ecc-4866-b347-b8f920934331 (TransportLabelDirectWithdrawalA4:220) Transport label, direct withdrawal – A5: 1ea50061-a032-4ab8-bcb6-7b4ca026f199 (TransportLabelDirectWithdrawalA5:221) Transport label, direct withdrawal – Label: f2e64493-702f-475b-b8e4-66214da6cca2 (TransportLabelDirectWithdrawalSmall:222) Transport label, direct arrival – A4: 248e7815-3878-4dd0-8a00-6224efc68a9c (TransportLabelDirectArrivalA4:223) Transport label, direct arrival – A5: 2c5270f8-8c1d-41d7-a271-600e4a6e26d5 (TransportLabelDirectArrivalA5:224) Transport label, direct arrival – Label: 92712a79-8485-44a0-b833-6a5b26e4206d (TransportLabelDirectArrivalSmall:225) Transport label, move between locations – A4: efff335f-034f-4dad-88e0-edfa8eb2fc93 (TransportLabelMoveBetweenLocationsA4:226) Transport label, move between locations – A5: b06919f9-5266-4122-b14e-5decd92ea4ec (TransportLabelMoveBetweenLocationsA5:227) Transport label, move between locations – Label: 9bf0deda-289d-49df-92e3-11a3902ba567 (TransportLabelMoveBetweenLocationsSmall:228) Transport label, move between warehouses – A4: f76084dc-94c7-4065-a415-f1b7faee204f (TransportLabelMoveBetweenWarehousesA4:229) Transport label, move between warehouses – A5: 9ad5ae01-782b-4530-a3a8-448ce71d3b74 (TransportLabelMoveBetweenWarehousesA5:230) Transport label, move between warehouses – Label: 2f31de4e-7239-47f5-8a04-e8da5abb9696 (TransportLabelMoveBetweenWarehousesSmall:231) 8D Internal report: 8fb1cef8-f38d-45ef-ad54-c01ecbeea562 (Standard8DNonconformityReport:232) Payment journal: cccd7875-6214-4053-989f-36365331d0b9 (PaymentLedger:233) Reprint – Payment journal: fc148c16-4be6-42e2-aa28-b5db15b78859 (PaymentLedgerReprint:234) Payment voucher: 8ab6f5cf-d677-4706-9788-2ced86e0c8a4 (PaymentVoucher:235) Debtor statement: 2405953a-ceb8-4469-8b71-3c96b504eef7 (DebtorStatement:236) Creditor statement: 17930d0a-a563-48e5-a807-a8b89cda95f3 (CreditorStatement:237) Print voucher: 7dac1305-b16b-4c9a-ab68-543e0be26ff0 (PrintVoucher:238) Official receipt: 7362b68e-9b41-48c9-b65a-a500562a32f0 (OfficialReceipt:239) Cash receipt: 44f7644c-395b-4863-b8aa-48a5b9c1ec14 (PolishCashReceipt:240) Cash report: 3acc9f86-b8b8-441c-89fc-80dd51e0dd51 (PolishCashReport:241) 8D Report to customer: 11800def-9275-43b4-9c16-3013a2c752fa (Standard8DCustomerNonconformityReport:242) Automatic postings/allocations journal: 372029ab-5a8b-4321-b1aa-7e62180224dd (AutoCodingLedger:243) Reprint – Automatic postings/allocations journal: 26f0c8fc-4258-4262-84c9-4cc5d046e932 (AutoCodingLedgerReprint:244) Measurement record – Manufacturing: 4b5fc35b-d7dd-4726-97fb-d1d58cb32fea (MeasuringProtocolManufacturing:245) Measurement record – Purchase: fef45cea-e553-4411-a7a2-652a4abad913 (MeasuringProtocolPurchase:246) Voucher list: 6ca862a5-a18e-4d64-a89a-4520e60ed16a (VoucherList:247) Revenue calculation journal: b9abc267-483d-4b09-bb92-7db9d3d4cfb1 (RevenueCalculationLedger:248) Reprint – Revenue calculation journal: 8923cf69-de06-43d4-91d9-ba4aae8d1917 (RevenueCalculationLedgerReprint:249) Activity list, standard: 965248e0-976f-44ec-a568-210ea65e063a (GeneralActivityList:250) Delivery note (return order): 0f392981-928c-4d12-96ff-154b32a7aad5 (ReturnPurchaseOrderDeliveryNote:251) Pro forma – Return order: 243d4277-ffcf-4289-add4-21fa98de6c8d (ReturnPurchaseOrderProforma:252) Transport label, return order: 620f2d83-27d2-4852-8ee7-a18ef055ac9f (ReturnPurchaseOrderTransportLabelA4:253) Transport label, return order – A5: f711b21f-0bec-449b-9672-e00d3f63bf2c (ReturnPurchaseOrderTransportLabelA5:254) Transport label, return order – Label: ff60dbc2-a97d-4cd0-8308-0340e6c372b9 (ReturnPurchaseOrderTransportLabelSmall:255) Waybill: 706a2a3d-9d72-4aef-98b1-61f0a32db3ad (Waybill:256) Shipment advice: 9b44b771-c1e1-4729-9af5-16efb1d8ce61 (ShipmentAdvice:257) Transport label (part) – Grouped: 7a7d94cd-91e6-4312-8222-b1f6b9fb0bf1 (PartTransportMultiLabel:258) Transport label (stock) – Grouped: 633e17cd-e794-4180-add2-cef1ee212db1 (StockTransportMultiLabel:259) Emission calculation – Detailed: 13fb1fac-667f-47ff-baca-547fc1c051e4 (SustainabilityCalculationDetailed:260) Shipment receipt: 5dc2afb1-0845-403c-ad05-d655bbb55b0c (ShipmentReceipt:261) Order row discounts: 4ec248fd-a3e5-41e5-94bb-69da8d51a996 (OrderRowDiscounts:262) Bank reconciliation report: 7bb84be0-0133-4c15-9d50-bcd44c6482a3 (BankAccountReconciliation:263) Collective correction invoice: b7acc870-8952-4a6f-8942-aae35a0d2ee6 (CollectiveCorrectionInvoice:264) Nonconformity report (customer noncon.): 11b8598a-65d3-4f76-a4e3-3888583dcdbd (ExternalCustomerNonconformityReport:265) Nonconformity report (suppl. noncon.): 2d49c11a-4402-4bb8-9a85-f908cbaa03cb (ExternalSupplierNonconformityReport:266) Nonconformity report (internal noncon.): c8dbc4c3-8dee-4b91-940a-e7a78874d047 (ExternalInternalNonconformityReport:267) Part contents – Delivery: 7ae8fdb9-411d-4a62-ad2d-419a7d393eaf (PartContentDeliveryReport:268) Material cost calculation journal: dec4476e-6c19-479c-8c82-660db0eeb556 (ProjectMaterialCalculationLedger:269) Reprint – Material cost calculation journal: ef45f2d6-e80d-46d3-ae16-0eae08ff48a5 (ProjectMaterialCalculationLedgerReprint:270) Causes for shortage: d7a641d7-08ca-4798-a767-ba1783453374 (CausesForShortage:271) Customer consists of: e0e1a152-118f-45cf-baf6-59d99e3f60f6 (CustomerLevelListConsistsOfList:272) Customer included in: 331903cc-0e37-4ac0-a810-ac4b0031a28c (CustomerLevelListIncludedInList:273) Supplier consists of: db1d96d7-5e4d-4009-8119-788b40943c84 (SupplierLevelListConsistsOfList:274) Supplier included in: 232412ed-0ea6-4a07-b5e9-3cc791ab273c (SupplierLevelListIncludedInList:275) GPB form: 8a96da92-8718-489c-bf27-2b53b117231c (GPBForm:276) Currency warehouse: d227b757-c6d8-4b5c-af5e-849a4cc45554 (CurrencyWarehouse:277) Pick list – Return order: 3008625c-3817-438b-894c-20bd6365bc9b (ReturnPurchaseOrderPickingList:278) Pro forma – Subcontract: 799b8e9b-b084-4983-ab13-3b328b9adfb4 (SubcontractProformaInvoice:279) Location label: f846467e-587e-453c-893d-0e6c1abd5c13 (LocationLabel:280) Location label (grouped): bd9d08e7-c979-4e51-87e8-12dd5c5363a6 (LocationMultiLabel:281) Files – External 1: fa315dd4-d7be-4cd8-aae0-4764e4c645a2 (FilesExternal1:282) Files – External 2: d3d834d7-fa0a-4ed4-9990-17c0ee955562 (FilesExternal2:283) Files – External 3: 6350e944-e659-4d27-a6fb-918dde12cc1d (FilesExternal3:284) Remittance advice: 631d1e42-725e-451f-aa88-d3736d0b6524 (RemittanceAdvice:285) Supplier agreement: c84c5776-76df-4eea-9eec-2938825d56c6 (SupplierAgreement:286) Modified supplier agreement: ec227dfa-ace8-4669-aedb-83e0fcdd056c (ModifiedSupplierAgreement:287) Self-billed invoice: a1c7e3f5-6b2d-4a8e-9f01-3d5e7c9b2a4f (SelfBilledInvoice:288) Transport label, purchase – A5: 9f000a32-f873-4766-96fe-ce96d93febe0 (PurchaseTransportLabelA5:310) Refill pick location: 5a65ead5-3268-4843-85ab-0bde904364ff (RefillPickingLocationStandard:500) Transport label, purchase, rejected – A5: b413093d-5e78-4af4-927c-2d28cbb628c3 (PurchaseTransportLabelA5ForRejection:1020) Transport label, manufacturing, transfer to stock – A5: aa95647b-d822-4ff4-ad00-8256ee66d957 (ManufacturingTransportLabelA5:1050) Transport label, manufacturing, rejected – A5: e29de335-254d-43bd-bdf5-316da09780bb (ManufacturingTransportLabelA5ForRejection:1060) Transport label, manufacturing, in progress – A5: 90eef0ea-fdb1-447a-b0af-e471b9b57498 (ManufacturingTransportLabelA5InProgress:1070) Transport label, manufacturing, prior to reporting – A5: 35042984-e462-42b6-9008-5060b05ef2ac (ManufacturingTransportLabelA5BeforeReporting:1080) Transport label, sales – Label: 39342c6e-3a50-4522-81d5-b3cdefff9898 (SalesTransportLabelSmall:1600) Form: 5673c63a-9738-4f7f-ad81-22daf5644bd0 (Form:2401) Service reporting: 63a761be-63df-469d-b1a1-b6902834ae7e (ServiceReporting:2402) Customer agreement: bcf47983-4284-4ddc-848c-de587e63971d (SalesAgreement:2501) Modified customer agreement: 031443e5-f432-4780-9cd7-da9f1c50534e (ModifiedSalesAgreement:2502) Balance per supplier: ee88f434-fbb0-4bc8-8583-2f948c5b4e7b (AccountStatementPurchase:2503) Return order: 1ebc4fb7-52c4-4e18-83c6-986b1cb75906 (ReturnPurchaseOrder:2504) Transport label, purchase – Label: 843c501e-c6c7-4e14-98f9-b0376846cce8 (PurchaseTransportLabelSmall:3100) Transport label, purchase, rejected – Label: 7451185c-cc36-4708-bb11-ddedd8431bf0 (PurchaseTransportLabelSmallForRejection:10200) Transport label, manufacturing, transfer to stock – Label: 2d65c164-620c-44a3-9c4f-501a7dbfad9b (ManufacturingTransportLabelSmall:10500) Transport label, manufacturing, rejected – Label: 0a76662a-741d-415c-9f85-f970257201fa (ManufacturingTransportLabelSmallForRejection:10600) Transport label, manufacturing, in progress – Label: b31f7c82-8aa7-4df7-95d5-f34f9a72036e (ManufacturingTransportLabelSmallInProgress:10700) Transport label, manufacturing, prior to reporting – Label: 3454d90d-46e7-426d-bdc4-a35f5e7e17b7 (ManufacturingTransportLabelSmallBeforeReporting:10800) Debit note: 1db44533-7218-4884-aac4-b95c91efb8f9 (DebitNote:10801) Service invoice: d883c1dc-e5c3-40e7-bdb1-36417d56fa0b (ServiceTax:10802) Sales – Order confirmation: cbc56d0a-ab13-4d8b-9508-5bfc88d099b8 (EdiCustomerOrderConfirmation:20001) Sales – Customer invoice: d416b442-0e51-44f6-b083-4335df21c28b (EdiCustomerOrderInvoice:20002) Sales – Simplified dispatch advice: fdeea94d-fe02-419a-aa0b-d3864b019273 (EdiCustomerOrderSimpleDispatchAdvice:20003) Sales – Customer order response: f3d0ca97-bca5-4a2d-bde3-bafb2a9e901f (EdiCustomerOrderResponse:20004) Purchase – Purchase order: 8530c00d-ae4d-4bc4-bb45-0f720ddac9f2 (EdiPurchaseOrder:20005) Sales – Complex dispatch advice: cae7be59-23f1-46e3-b085-27382bfa1cc7 (EdiCustomerOrderComplexDispatchAdvice:20006) Purchase – Delivery schedule: 051aad1f-7c06-412e-bfa7-7551e06c6706 (EdiPurchaseDeliverySchedule:20007) |
| `IsDefault` | `Boolean` | no |  | Specifies if the form report is default. |
| `Hint` | `String` | no |  | The human readable form of the report type. |
| `Name` | `String` | no |  | Name of the form report. |
| `IsStandard` | `Boolean` | no |  | Specifies if the form report is a standard report. |
| `DocumentId` | `Guid` | no |  | Globally unique identifier (GUID) of the form report. |
| `IsAdaptation` | `Boolean` | no |  | Specifies if the form report is an adaptation. |

**Referenced by:** [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [PartDefaultTransportLabels](Inventory.md#Inventory.PartDefaultTransportLabel), [PaymentMethods](Common.md#Common.PaymentMethod), [QuoteTypes](Sales.md#Sales.QuoteType)

<a id="Common.FormReportTranslationGroup"></a>
### FormReportTranslationGroups

Represents a form report translation group.

- **Endpoint:** `GET /api/v1/Common/FormReportTranslationGroups`
- **Introduced in:** 2.48

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the translation group. |
| `DocumentFont` | `Int32` | no |  | The type of document font that is applied for the translation group. |
| `IsPreset` | `Boolean` | no |  | Whether or not the translation group is a preset delivered with MONITOR or not. |
| `Description` | `String` | no |  | The translated description of the translation group. |
| `Code` | `String` | no |  | The human readable identifier of the translation group. |
| `Translations` | `FormReportTranslations[]` | no | [FormReportTranslations](Common.md#Common.FormReportTranslation) | The translations that belong to the translation group. |

- `DocumentFont` — Default=0, SimplifiedChinese=1, Thai=2

**References out:** [FormReportTranslations](Common.md#Common.FormReportTranslation)
**Referenced by:** [FormReportTranslations](Common.md#Common.FormReportTranslation)

<a id="Common.FormReportTranslation"></a>
### FormReportTranslations

Represents a form report translation.

- **Endpoint:** `GET /api/v1/Common/FormReportTranslations`
- **Introduced in:** 2.48

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the translation. |
| `Phrase` | `String` | no |  | The overriding phrase text for the translation. |
| `PhraseId` | `Int64` | no |  | The identifier of the phrase that the translation overrides. |
| `FormReportTranslationGroupId` | `Int64` | no | [FormReportTranslationGroups](Common.md#Common.FormReportTranslationGroup) | The business key identifier of the translation group that the translation belongs to. |

**References out:** [FormReportTranslationGroups](Common.md#Common.FormReportTranslationGroup)
**Referenced by:** [FormReportTranslationGroups](Common.md#Common.FormReportTranslationGroup)

<a id="Common.FormTemplateRow"></a>
### FormTemplateRows

Represents a form template row.

- **Endpoint:** `GET /api/v1/Common/FormTemplateRows`
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `Code` | `String` | no |  | The human readable identifier of the form template row. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the form template row. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the form template row's comment. |
| `Description` | `String` | no |  | The translated description of the form template row. |
| `FormTemplateSelectionRowId` | `Int64` | no | [FormTemplateSelectionRows](Common.md#Common.FormTemplateSelectionRow) | The business key identifier of the form template selection row that the form template row relates to. |
| `RowIndex` | `Int32?` | yes |  | The row index of the form template row. |
| `Checkbox` | `Boolean` | no |  | The boolean value of the form template row. |
| `DateTimeValue` | `DateTimeOffset?` | yes |  | The timestamp of the form template row. |
| `Number` | `Decimal?` | yes |  | The numeric value of the form template row. |
| `TextValue` | `String` | no |  | The text value of the form template row. |
| `Type` | `Int32` | no |  | The type of the value stored in the form template row. |
| `LowerBoundary` | `Decimal?` | yes |  | The minimum setpoint value of the form template row. |
| `UpperBoundary` | `Decimal?` | yes |  | The maximum setpoint value of the form template row. |
| `MinValue` | `Decimal?` | yes |  | The minimum tolerance value of the form template row. |
| `MaxValue` | `Decimal?` | yes |  | The maximum tolerance value of the form template row. |
| `Value` | `Decimal?` | yes |  | The setpoint value of the form template row. |
| `Mandatory` | `Boolean` | no |  | Indicates if the value of the form template row needs to be reported. |
| `PrintOut` | `Boolean` | no |  | Indicates if the form template row's properties should be printed on the document. |
| `MasterToolId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the tool that the form template row relates to. |
| `UnitId` | `Int64?` | yes | [Units](Common.md#Common.Unit) | The business key identifier of the unit of the form template row's value. |

- `Type` — Decimal=0, Text=1, CheckBox=2, Date=3

**References out:** [Comments](Common.md#Common.Comment), [FormTemplateSelectionRows](Common.md#Common.FormTemplateSelectionRow), [Parts](Inventory.md#Inventory.Part), [Units](Common.md#Common.Unit)

<a id="Common.FormTemplate"></a>
### FormTemplates

Represents a measuring or maintenance form template.

- **Endpoint:** `GET /api/v1/Common/FormTemplates`
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `Code` | `String` | no |  | The human readable identifier of the form template. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the form template. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the form template's comment. |
| `Description` | `String` | no |  | The translated description of the form template. |
| `ControlDataType` | `Int32` | no |  | The type of the template form which specifices in which apps the form can be used. |
| `Type` | `Int32` | no |  | The usage type of the measuring template form that restricts in which module the measuring form template can be used. |

- `ControlDataType` — Maintenance=0, MeasuringData=1
- `Type` (bitmask) — None=0, Manufacturing=1, Purchase=2

**References out:** [Comments](Common.md#Common.Comment)
**Referenced by:** [FormTemplateSelectionRows](Common.md#Common.FormTemplateSelectionRow), [ManufacturingOrderOperationControlDataRows](Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow), [MeasuringTemplates](Common.md#Common.MeasuringTemplate), [OperationRowControlDataRows](Manufacturing.md#Manufacturing.OperationRowControlDataRow), [PartPurchaseControlDataRows](Inventory.md#Inventory.PartPurchaseControlDataRow)

<a id="Common.FormTemplateSelectionRow"></a>
### FormTemplateSelectionRows

Represents a form template selection row.

- **Endpoint:** `GET /api/v1/Common/FormTemplateSelectionRows`
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `Code` | `String` | no |  | The human readable identifier of the form template selection row. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the form template selection row. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the form template selection row's comment. |
| `Description` | `String` | no |  | The translated description of the form template selection row. |
| `FormTemplateId` | `Int64` | no | [FormTemplates](Common.md#Common.FormTemplate) | The business key identifier of the form template that the form template selection row relates to. |
| `RowIndex` | `Int32?` | yes |  | The row index of the form template selection row. |

**References out:** [Comments](Common.md#Common.Comment), [FormTemplates](Common.md#Common.FormTemplate)
**Referenced by:** [FormTemplateRows](Common.md#Common.FormTemplateRow)

<a id="Common.LanguageCode"></a>
### LanguageCodes

Represents a language code. Language codes are the language definitions in MONITOR.

- **Endpoint:** `GET /api/v1/Common/LanguageCodes`
- **Required permission:** Show languages
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the language code. |
| `Code` | `String` | no |  | The human readable code of the language. |
| `Phrase` | `String` | no |  | The translated description of the language code. |

**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [Companies](Common.md#Common.Company), [Countries](Common.md#Common.Country), [Customers](Sales.md#Sales.Customer), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [MonitoringTaskRecipients](Common.md#Common.MonitoringTaskRecipient), [Persons](Common.md#Common.Person), [Suppliers](Purchase.md#Purchase.Supplier), [Warehouses](Common.md#Common.Warehouse)

<a id="Common.MeasuringTemplate"></a>
### MeasuringTemplates

Represents a measuring template.

- **Endpoint:** `GET /api/v1/Common/MeasuringTemplates`
- **Required permission:** Show measuring templates
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the entity. |
| `FormTemplateId` | `Int64` | no | [FormTemplates](Common.md#Common.FormTemplate) | The business key identifier of the form template that the measuring template relates to. |
| `Code` | `String` | no |  | The human readable identifier of the measuring template. |
| `Description` | `String` | no |  | The translated description of the measuring template. |
| `FrequencyText` | `String` | no |  | The frequency text defined for the measuring template. |
| `IntervalAmount` | `Int32?` | yes |  | The quantity value defined for the measuring template. |
| `Interval` | `Int32?` | yes |  | The interval value defined for the measuring template. |
| `MeasuringFrequency` | `Int32` | no |  | The frequency value defined for the measuring template. |
| `Type` | `Int32` | no |  | Type of the measuring template which restricts in which module the measuring template can be used. |

- `MeasuringFrequency` — First=0, Last=1, All=2, Sample=3, Other=4, PerOrder=5
- `Type` (bitmask) — None=0, Manufacturing=1, Purchase=2

**References out:** [FormTemplates](Common.md#Common.FormTemplate)
**Referenced by:** [ManufacturingOrderOperationControlDataRows](Manufacturing.md#Manufacturing.ManufacturingOrderOperationControlDataRow), [OperationRowControlDataRows](Manufacturing.md#Manufacturing.OperationRowControlDataRow), [PartPurchaseControlDataRows](Inventory.md#Inventory.PartPurchaseControlDataRow)

<a id="Common.MonitoringTaskRecipient"></a>
### MonitoringTaskRecipients

Represents a recipient for monitoring task.

- **Endpoint:** `GET /api/v1/Common/MonitoringTaskRecipients`
- **Required permission:** Create and handle all monitoring tasks
- **Introduced in:** 24.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier key of the monitoring task recipient. |
| `TaskId` | `Int64` | no | [MonitoringTasks](Common.md#Common.MonitoringTask) | The business key identifier of the monitoring task that the recipient belongs to. |
| `LanguageCodeId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The business key identifier of the language code used in the recipient. |
| `RecipientType` | `Int32` | no |  | Specifies the type of the monitoring task's recipient. |
| `Email` | `String` | no |  | Specifies the mail of recipient if recipient type is email. |
| `ApplicationUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user of the monitoring task's recipient. |

- `RecipientType` — EmailRecipient=0, NotificationRecipient=1, UserEmailRecipient=2

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [LanguageCodes](Common.md#Common.LanguageCode), [MonitoringTasks](Common.md#Common.MonitoringTask)

<a id="Common.MonitoringTaskRow"></a>
### MonitoringTaskRows

Represents a monitoring task row.

- **Endpoint:** `GET /api/v1/Common/MonitoringTaskRows`
- **Required permission:** Create and handle all monitoring tasks
- **Introduced in:** 24.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the monitoring task row. |
| `TaskId` | `Int64` | no | [MonitoringTasks](Common.md#Common.MonitoringTask) | The business key identifier of the monitoring task that the row belongs to. |
| `EntityId` | `Int64` | no |  | The business key identifier of the entity type that the row belongs to. |
| `EntityType` | `Guid` | no |  | The type of entity that the row belongs to. |
| `ConditionType` | `Int32` | no |  | The condition type of the monitoring task row. |
| `Value` | `String` | no |  | The threshold balance of stock. Applicable to monitoring task type of StockBalance |
| `Message` | `String` | no |  | The message of row to be sent to recipient. |
| `Warehouses` | `Warehouses[]` | no | [Warehouses](Common.md#Common.Warehouse) | Specifies the warehouse of the monitoring task row. |

**References out:** [MonitoringTasks](Common.md#Common.MonitoringTask), [Warehouses](Common.md#Common.Warehouse)

<a id="Common.MonitoringTask"></a>
### MonitoringTasks

Represents a monitoring task.

- **Endpoint:** `GET /api/v1/Common/MonitoringTasks`
- **Required permission:** Create and handle all monitoring tasks
- **Introduced in:** 24.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the monitoring task. |
| `Number` | `String` | no |  | The monitoring task number. |
| `Name` | `String` | no |  | The name of monitoring task. |
| `TaskType` | `Int32` | no |  | The type of monitoring task. |
| `Status` | `Int32` | no |  | The status of monitoring task. |
| `UseSchedule` | `Boolean` | no |  | Specifies if the monitoring task should be used in schedule. |
| `RunOnce` | `Boolean` | no |  | Specifies if the monitoring task should be deactivated when any of the terms are fulfilled. |
| `StartTime` | `DateTimeOffset?` | yes |  | The start time of the monitoring task. |
| `StopTime` | `DateTimeOffset?` | yes |  | The end time of the monitoring task. |
| `ApplicationUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that create the monitoring task. |
| `ApplicationUser` | `ApplicationUsers` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The application user that create the monitoring task. |
| `CommentId` | `Int64` | no | [Comments](Common.md#Common.Comment) | The business key identifier of the monitoring task's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The monitoring task's comment. |

- `TaskType` — StockBalance=0, PersonActivity=1, CustomerActivity=2, QuoteActivity=3, CustomerOrderActivity=4, SupplierActivity=5, PartActivity=6, PurchaseOrderActivity=7, InquiryActivity=8, ManufacturingOrderOperation=9, ArrivalReporting=10, OrderRowArrivalReporting=11, BlanketOrderPurchaseActivity=12, BlanketOrderSalesActivity=13, SalesAgreementActivity=14, CaseEntryActivity=15, ExposureTime=16, BusinessOpportunityActivity=17, ProductRecordActivity=18, SupplierAgreementActivity=19
- `Status` — Active=0, Disabled=1

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Comments](Common.md#Common.Comment)
**Referenced by:** [MonitoringTaskRecipients](Common.md#Common.MonitoringTaskRecipient), [MonitoringTaskRows](Common.md#Common.MonitoringTaskRow)

<a id="Common.OrderTransferSetting"></a>
### OrderTransferSettings

Represents an order transfer setting.

- **Endpoint:** `GET /api/v1/Common/OrderTransferSettings`
- **Required permission:** Show setting
- **Introduced in:** 23.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the setting. |
| `ManufacturingCompanyPartIdentityTypeCode` | `String` | no |  | The manufacturing company part identity type code of the setting. |
| `ManufacturingCompanyUsePartOtherIdentities` | `Boolean` | no |  | Specifies if the manufacturing company use part other identities. |
| `ManufacturingCompanyOrderOrderTypeCode` | `String` | no |  | The manufacturing company orders order type code. |

**Referenced by:** [TransferProfiles](Common.md#Common.TransferProfile)

<a id="Common.PartConfigurationComponentSnapshot"></a>
### PartConfigurationComponentSnapshots

Represents a part configuration component snapshot.

- **Endpoint:** `GET /api/v1/Common/PartConfigurationComponentSnapshots`
- **Required permission:** Show part
- **Introduced in:** 26.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the component snapshot. |
| `ComponentType` | `Int32` | no |  | The component type discriminator. |
| `ParentId` | `Int64` | no |  | The business key identifier of the template snapshot this component belongs to. |
| `OriginComponentId` | `Int64?` | yes |  | The business key identifier of the origin configuration component. |
| `ParentRowId` | `Int64?` | yes | [PartConfigurationComponentSnapshots](Common.md#Common.PartConfigurationComponentSnapshot) | The business key identifier of the parent component within the same template (self-referencing hierarchy). For example, a variable nested under a section. |
| `RowIndex` | `Int32?` | yes |  | The row index for ordering. |
| `ShowOnDocument` | `Int32?` | yes |  | Document types to show the section on. Only applicable for Section components. |
| `ShowOnFooter` | `Int32?` | yes |  | Document types to show the section footer on. Only applicable for Section components. |
| `Visible` | `Boolean?` | yes |  | Whether the section is visible. Only applicable for Section components. |
| `ExternalVisible` | `Boolean?` | yes |  | Whether the section is externally visible. Only applicable for Section components. |
| `Name` | `String` | no |  | The variable name. Only applicable for Variable components. |
| `VariableType` | `Int32?` | yes |  | The variable type. Only applicable for Variable components. |
| `Formula` | `String` | no |  | The variable formula. Only applicable for Variable components. |
| `Mandatory` | `Boolean?` | yes |  | Whether the variable is mandatory. Only applicable for Variable components. |
| `Min` | `Decimal?` | yes |  | The minimum value. Only applicable for Variable components. |
| `Max` | `Decimal?` | yes |  | The maximum value. Only applicable for Variable components. |
| `NumberOfDecimals` | `Int32?` | yes |  | The number of decimals. Only applicable for Variable components. |
| `RoundingBase` | `Decimal?` | yes |  | The rounding base. Only applicable for Variable components. |
| `UnitId` | `Int64?` | yes |  | The business key identifier of the unit. Only applicable for Variable components. |
| `ExtraFieldTemplateId` | `Int64?` | yes |  | The business key identifier of the extra field template. Only applicable for Variable components. |
| `VariableId` | `Int64?` | yes |  | The business key identifier of the variable. Only applicable for Variable components. |
| `DocumentDisplaySettings` | `Int32?` | yes |  | The document display settings. Only applicable for Variable components. |
| `BindPropertyType` | `Int32?` | yes |  | The bind property type. Only applicable for Variable components. |
| `Code` | `String` | no |  | The selection group code. Only applicable for SelectionGroup components. |
| `AutomaticSelectionAlternative` | `Int32?` | yes |  | The automatic selection alternative. Only applicable for SelectionGroup components. |
| `MaximumSelectedRows` | `Int32?` | yes |  | The maximum number of selected rows. Only applicable for SelectionGroup components. |
| `MinimumSelectedRows` | `Int32?` | yes |  | The minimum number of selected rows. Only applicable for SelectionGroup components. |
| `MinimumSelectedQuantity` | `Decimal?` | yes |  | The minimum selected quantity. Only applicable for SelectionGroup components. |
| `MaximumSelectedQuantity` | `Decimal?` | yes |  | The maximum selected quantity. Only applicable for SelectionGroup components. |
| `ManagedOptionsType` | `Int32?` | yes |  | The managed options type. Only applicable for SelectionGroup components. |
| `ManagedOptionsIdentifier` | `String` | no |  | The managed options identifier. Only applicable for SelectionGroup components. |
| `SourceVersion` | `Int32?` | yes |  | The source version. Only applicable for SelectionGroup components. |

- `ComponentType` — Section=0, Variable=1, SelectionGroup=2
- `AutomaticSelectionAlternative` — None=0, YesFirst=1, YesAll=2
- `ManagedOptionsType` — None=0, Selection=1, SelectionAndQuantity=2

**References out:** [PartConfigurationComponentSnapshots](Common.md#Common.PartConfigurationComponentSnapshot)
**Referenced by:** [PartConfigurationComponentSnapshots](Common.md#Common.PartConfigurationComponentSnapshot), [PartConfigurationSelectionGroupResults](Common.md#Common.PartConfigurationSelectionGroupResult)

<a id="Common.PartConfigurationPreset"></a>
### PartConfigurationPresets

Represents a part configuration preset.

- **Endpoint:** `GET /api/v1/Common/PartConfigurationPresets`
- **Required permission:** Show part
- **Introduced in:** 2.55

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part configuration preset. |
| `Name` | `String` | no |  | The name of the preset. |
| `ChangedDate` | `DateTimeOffset?` | yes |  | The date and time the preset was last changed. |
| `ChangedBy` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user who last changed the preset. |
| `CreatedDate` | `DateTimeOffset` | no |  | The date and time the preset was created. |
| `CreatedBy` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user who created the preset. |
| `PartConfigurationId` | `Int64?` | yes | [PartConfigurations](Common.md#Common.PartConfiguration) | The business key identifier of the preset's configuration. |
| `Type` | `Int32` | no |  | The type of part configuration preset. |

- `Type` — Normal=0, Temporary=1

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [PartConfigurations](Common.md#Common.PartConfiguration)

<a id="Common.PartConfigurationResult"></a>
### PartConfigurationResults

Represents a part configuration result.

- **Endpoint:** `GET /api/v1/Common/PartConfigurationResults`
- **Required permission:** Show part
- **Introduced in:** 2.55

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part configuration result. |
| `TemplateId` | `Int64` | no | [PartConfigurationTemplates](Common.md#Common.PartConfigurationTemplate) | The business key identifier of the result's template. |
| `MainPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part to configure. |
| `Quantity` | `Decimal` | no |  | The quantity to produce from this configuration. |
| `UnitPrice` | `Decimal?` | yes |  | The unit price of the configured part. |
| `UnitPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the configured part's unit price. |
| `StandardPrice` | `Decimal?` | yes |  | The standard price of the configured part. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the configured part's standard price. |
| `UnitPriceInCompanyCurrency` | `Decimal?` | yes |  | The unit price of the configured part int the company's currency. |
| `UnitPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the configured part's price in company currency. |
| `DiscountPercentage` | `Decimal` | no |  | The discount percentage for the configured part. |
| `LockedUnitPrice` | `Boolean` | no |  | If the unit price is locked on the configured part. |
| `LockedDiscount` | `Boolean` | no |  | If the discount percentage is locked on the configured part. |
| `AlternativePreparationCode` | `String` | no |  | The alternative preparation code on the configured part. |
| `WeightPerUnit` | `Decimal?` | yes |  | The weight per unit on the configured part. |
| `IsValid` | `Boolean` | no |  | If the configuration is valid. |
| `PriceFormulaFactor` | `Decimal` | no |  | The price formula factor for the configured part. |
| `SnapshotId` | `Int64?` | yes |  | The business key identifier of the result's snapshot. |
| `PartConfigurationId` | `Int64?` | yes | [PartConfigurations](Common.md#Common.PartConfiguration) | The business key identifier of the result's configuration. |
| `PartCalculationId` | `Int64?` | yes |  | The business key identifier of the result's calculation. |
| `PartConfigurationSelectionGroupResults` | `PartConfigurationSelectionGroupResults[]` | no | [PartConfigurationSelectionGroupResults](Common.md#Common.PartConfigurationSelectionGroupResult) | The list of Part configuration selection group result. |

**References out:** [Currencies](Common.md#Common.Currency), [PartConfigurations](Common.md#Common.PartConfiguration), [PartConfigurationSelectionGroupResults](Common.md#Common.PartConfigurationSelectionGroupResult), [PartConfigurationTemplates](Common.md#Common.PartConfigurationTemplate), [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [PartConfigurations](Common.md#Common.PartConfiguration), [PartConfigurationSelectionGroupResults](Common.md#Common.PartConfigurationSelectionGroupResult)

<a id="Common.PartConfiguration"></a>
### PartConfigurations

Represents a part configuration.

- **Endpoint:** `GET /api/v1/Common/PartConfigurations`
- **Required permission:** Show part
- **Introduced in:** 2.55

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part configuration. |
| `ResultId` | `Int64?` | yes | [PartConfigurationResults](Common.md#Common.PartConfigurationResult) | The business key identifier of the configuration's result. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the comment that belongs to the configuration. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment that belongs to the configuration. |

**References out:** [Comments](Common.md#Common.Comment), [PartConfigurationResults](Common.md#Common.PartConfigurationResult)
**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [PartConfigurationPresets](Common.md#Common.PartConfigurationPreset), [PartConfigurationResults](Common.md#Common.PartConfigurationResult), [QuoteRows](Sales.md#Sales.QuoteRow), [RemotePartConfigurations](Common.md#Common.RemotePartConfiguration)

<a id="Common.PartConfigurationSelectionGroupResult"></a>
### PartConfigurationSelectionGroupResults

Represents a part configuration selection group result

- **Endpoint:** `GET /api/v1/Common/PartConfigurationSelectionGroupResults`
- **Required permission:** Show part
- **Introduced in:** 25.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part configuration selection group result. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part. |
| `SelectionGroupTemplateRowId` | `Int64` | no |  | The business key identifier of the selection group row snapshot. |
| `RowIndex` | `Int32` | no |  | The row of the result. |
| `SelectionGroupTemplateId` | `Int64` | no | [PartConfigurationComponentSnapshots](Common.md#Common.PartConfigurationComponentSnapshot) | The business key identifier of the selection group snapshot. |
| `PartConfigurationResultId` | `Int64` | no | [PartConfigurationResults](Common.md#Common.PartConfigurationResult) | The business key identifier of the part configuration result. |
| `Quantity` | `Decimal` | no |  | The quantity of the result row. |
| `SetupQuantity` | `Decimal` | no |  | The setup quantity of the result row. |
| `UnitPrice` | `Decimal?` | yes |  | The unit price amount. |
| `UnitPriceCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the unit price. |
| `UnitPriceInCompanyCurrency` | `Decimal?` | yes |  | The unit price amount in company currency. |
| `UnitPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency for the unit price in company currency. |
| `DiscountPercentage` | `Decimal` | no |  | The discount percentage. |
| `PriceFormulaFactor` | `Decimal` | no |  | The price formula factor. |
| `LockedUnitPrice` | `Boolean` | no |  | Whether the unit price is locked. |
| `LockedDiscount` | `Boolean` | no |  | Whether the discount is locked. |
| `SelectedByType` | `Int32` | no |  | The type indicating how the row was selected. |
| `SelectedByName` | `String` | no |  | The name indicating who or what selected the row. |
| `SelectionType` | `Int32` | no |  | The selection type. |
| `ToOperation` | `Int32?` | yes |  | The target operation number. |
| `MainPartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the main part. |
| `Position` | `String` | no |  | The position string. |

- `SelectedByType` — User=0, Preset=1
- `SelectionType` — None=0, Initialization=5, RuleUnselect=10, Manual=20, GroupRule=30, SelectionRuleSelect=40, Locked=50, TemporaryLockedByManualSelection=60

**References out:** [Currencies](Common.md#Common.Currency), [PartConfigurationComponentSnapshots](Common.md#Common.PartConfigurationComponentSnapshot), [PartConfigurationResults](Common.md#Common.PartConfigurationResult), [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [PartConfigurationResults](Common.md#Common.PartConfigurationResult)

<a id="Common.PartConfigurationTemplate"></a>
### PartConfigurationTemplates

Represents a part configuration template.

- **Endpoint:** `GET /api/v1/Common/PartConfigurationTemplates`
- **Required permission:** Show part
- **Introduced in:** 2.55

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part configuration template. |
| `Version` | `Int32` | no |  | The version of the template. |
| `Code` | `String` | no |  | The human readable identifier of the template. |
| `Description` | `String` | no |  | The decription of the template. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the comment that belongs to the template. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment that belongs to the template. |

**References out:** [Comments](Common.md#Common.Comment)
**Referenced by:** [PartConfigurationResults](Common.md#Common.PartConfigurationResult), [Parts](Inventory.md#Inventory.Part)

<a id="Common.PartialQuantity"></a>
### PartialQuantities

Represents a partial quantity.

- **Endpoint:** `GET /api/v1/Common/PartialQuantities`
- **Introduced in:** 22.6

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the partial quantity. |
| `Quantity` | `Decimal` | no |  | Quantity, can be a length or weight. |
| `NumberOf` | `Decimal` | no |  | Number of Quantity. Total amount of quantities is NumberOf * Quantity |
| `PackagePartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the package part id for this partial quantity. |
| `RowIndex` | `Int32` | no |  | The ordered row index of the partial quantity. |

**References out:** [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [OrderQuantityCustomerOrders](Sales.md#Sales.OrderQuantityCustomerOrder), [OrderQuantityManufacturingOrderOperations](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrderOperation), [OrderQuantityManufacturingOrders](Manufacturing.md#Manufacturing.OrderQuantityManufacturingOrder), [OrderQuantityPurchaseOrders](Purchase.md#Purchase.OrderQuantityPurchaseOrder), [OrderQuantityTemplates](Inventory.md#Inventory.OrderQuantityTemplate)

<a id="Common.PartUnitUsage"></a>
### PartUnitUsages

Represents a part unit usage.

- **Endpoint:** `GET /api/v1/Common/PartUnitUsages`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the part unit usage. |
| `UnitId` | `Int64` | no | [Units](Common.md#Common.Unit) | The unit of the part unit usage. References Units . |
| `IsRemoved` | `Boolean` | no |  | Specifies if the part unit usage has been removed. |
| `ConversionFactor` | `Decimal` | no |  | The conversion factor between the default part unit usage and this part unit usage. |
| `UsageType` | `Int32` | no |  | The usage type of the part unit usage. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the part unit usage belongs to. References . |

- `UsageType` (bitmask) — None=0, ManufacturingMaterialWithdrawal=1, PurchaseOrder=2, ArrivalReporting=4, CustomerOrder=8, DeliveryReporting=16, PhysicalInventoryAndStockReporting=32, StatisticalUnit=64, PackForDelivery=128

**References out:** [Parts](Inventory.md#Inventory.Part), [Units](Common.md#Common.Unit)
**Referenced by:** [Parts](Inventory.md#Inventory.Part)

<a id="Common.PaymentMethod"></a>
### PaymentMethods

Represents a queryable payment method.

- **Endpoint:** `GET /api/v1/Common/PaymentMethods`
- **Required permission:** Show terms
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the payment method. |
| `Code` | `String` | no |  | Max length 7 |
| `Description` | `String` | no |  | The translated description of the payment method. |
| `PaymentType` | `Int32` | no |  | The payment type of the payment method. |
| `BankWebpage` | `String` | no |  | The bank webpage URL of the payment method. |
| `CustomerIdAtBank` | `String` | no |  | The bank customer identifier of the payment method. |
| `SendPaymentFilePath` | `String` | no |  | The send payment file path of the payment method. |
| `SendPaymentDirectoryPath` | `String` | no |  | The send payment directory path of the payment method. |
| `CodingAccountId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the payment method's coding account. This account is also found in the payment method's . References Account. |
| `IsActive` | `Boolean` | no |  | Specifies if the payment method is active and available in the MONITOR system. |
| `BankingFeeAccountId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the payment method's banking fee account. This account is also found in the payment method's . References Account. |
| `TransactionListFormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](Common.md#Common.FormReportConfiguration) | The business key identifier of the payment method's translation list form report configuration. |
| `ReceivingBankAccountValidation` | `Int32` | no |  | Specifies which type of validation will be performed for the payment method's receiving bank account. |
| `ReceivingGiroAccountValidation` | `Int32` | no |  | Specifies which type of validation will be performed for the payment method's receiving giro account. |
| `CodingAccountCodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the payment method's coding account coding entry. References CodingEntries . |
| `CodingAccountCodingEntry` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The payment method's coding account coding entry. |
| `BankingFeeCodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the payment method's banking fee coding entry. References CodingEntries . |
| `BankingFeeCodingEntry` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The payment method's banking fee coding entry. |

- `PaymentType` — ManualPayment=0, ElectronicPayment=1, ElectronicIncomingPayment=2, CashPayment=3, BankIntegration=4, Factoring=5
- `ReceivingBankAccountValidation` — None=0, WarnIfMissing=1, BlockIfMissing=2
- `ReceivingGiroAccountValidation` — None=0, WarnIfMissing=1, BlockIfMissing=2

**References out:** [CodingEntries](Accounting.md#Accounting.CodingEntry), [FormReportConfigurations](Common.md#Common.FormReportConfiguration)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [CustomerOrders](Sales.md#Sales.CustomerOrder), [IncomingPayments](Accounting.md#Accounting.IncomingPayment), [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment), [PaymentTerms](Common.md#Common.PaymentTerm), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Common.PaymentPlanTemplateRow"></a>
### PaymentPlanTemplateRows

Represents a payment plan template row.

- **Endpoint:** `GET /api/v1/Common/PaymentPlanTemplateRows`
- **Required permission:** Show invoicing plan
- **Introduced in:** 2.28

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the payment plan template row. |
| `UnpaidAdvanceWarningType` | `Int32?` | yes |  | The unpaid advance warning type of the payment plan template row. |
| `PaymentPlanTemplateId` | `Int64` | no | [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate) | The business key identifier of the payment plan template of the payment plan template row. |
| `PartialInvoiceType` | `Int32` | no |  | The partial invoice type of the payment plan template row. |
| `PartId` | `Int64?` | yes | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part of the payment plan template row. |
| `Part` | `Parts` | no | [Parts](Inventory.md#Inventory.Part) | The part of the payment plan template row. |
| `OverrideDescription` | `String` | no |  | The override description of the payment plan template row. |
| `FractionOfTotal` | `Decimal` | no |  | The fraction of total of the payment plan template row. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the payment term of the payment plan template row. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The payment term of the payment plan template row. |
| `RowIndex` | `Int32?` | yes |  | The row index of the payment plan template row. |

- `UnpaidAdvanceWarningType` — NoAlert=0, Warning=1, PreventDelivery=2
- `PartialInvoiceType` — NotInitialized=0, InAdvance=1, Delivery=2, InArrears=3, Text=4

**References out:** [Parts](Inventory.md#Inventory.Part), [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate), [PaymentTerms](Common.md#Common.PaymentTerm)
**Referenced by:** [PaymentPlanTemplates](Common.md#Common.PaymentPlanTemplate)

<a id="Common.PaymentPlanTemplate"></a>
### PaymentPlanTemplates

Represents a payment plan template.

- **Endpoint:** `GET /api/v1/Common/PaymentPlanTemplates`
- **Required permission:** Show invoicing plan
- **Introduced in:** 2.28

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the payment plan template. |
| `PaymentPlanTemplateType` | `Int32` | no |  | The type of the payment plan template. |
| `Number` | `String` | no |  | The human readable identifier of the payment plan template. |
| `Description` | `String` | no |  | The description of the payment plan template. |
| `IsActive` | `Boolean` | no |  | The is active of the payment plan template. |
| `InvoiceTextTypes` | `Int32` | no |  | The invoice text types of the payment plan template. |
| `PaymentPlanTemplateRows` | `PaymentPlanTemplateRows[]` | no | [PaymentPlanTemplateRows](Common.md#Common.PaymentPlanTemplateRow) | A collection of payment plan template rows that belong to the payment plan template. |

- `PaymentPlanTemplateType` — ForSales=1, ForPurchase=2, ForSalesAndPurchase=3
- `InvoiceTextTypes` (bitmask) — OrderRowText=1, OrderRows=2, ProjectNumberAndName=4, GoodsLabel=8, OrderAdditionalText=16, ConfigurationInfo=32, OrderRowTextInPolishOrderInfo=64, ConfigurationInfoInPolishOrderInfo=128

**References out:** [PaymentPlanTemplateRows](Common.md#Common.PaymentPlanTemplateRow)
**Referenced by:** [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [PaymentPlanTemplateRows](Common.md#Common.PaymentPlanTemplateRow)

<a id="Common.PaymentTerm"></a>
### PaymentTerms

Represents a queryable payment term.

- **Endpoint:** `GET /api/v1/Common/PaymentTerms`
- **Required permission:** Show terms
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the payment term. |
| `Number` | `Int64` | no |  | The payment term number. |
| `Description` | `String` | no |  | The translated description of the payment term. |
| `GracePeriodInDays` | `Int32` | no |  | The grace period of the payment term specified in days. |
| `IsFreeDeliveryMonth` | `Boolean` | no |  | Specifies if the payment term implies a free delivery month. _(Replaced by Method)_ |
| `Method` | `Int32` | no |  | The method of the payment term. |
| `AddDaysToEOM` | `Int32` | no |  | The number of days to add to the due date when using the end of month method. |
| `IsDefault` | `Boolean` | no |  | Specifies if the payment term is the default. |
| `InvoiceType` | `Int32` | no |  | The invoice type of the payment term. |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](Common.md#Common.PaymentMethod) | The business key identifier of the payment method of the payment term. References PaymentMethods . |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |
| `Code` | `String` | no |  | The code of the payment term. |

- `Method` — Days=0, FreeDeliveryMonth=1, EOM=2
- `InvoiceType` — Standard=1, Internal=2, CashReceipt=3, Interest=4, OnAccount=5, DebitNote=6, ServiceTax=7, CorrectionInvoice=8, CollectiveCorrectionInvoice=9

**References out:** [PaymentMethods](Common.md#Common.PaymentMethod)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrderPaymentPlanRows](Sales.md#Sales.CustomerOrderPaymentPlanRow), [CustomerOrders](Sales.md#Sales.CustomerOrder), [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType), [Customers](Sales.md#Sales.Customer), [Inquiries](Purchase.md#Purchase.Inquiry), [PaymentPlanTemplateRows](Common.md#Common.PaymentPlanTemplateRow), [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Quotes](Sales.md#Sales.Quote), [SalesAgreements](Sales.md#Sales.SalesAgreement), [Suppliers](Purchase.md#Purchase.Supplier)

<a id="Common.PermissionGroup"></a>
### PermissionGroups

Represents a permission group.

- **Endpoint:** `GET /api/v1/Common/PermissionGroups`
- **Required permission:** Show user rights groups
- **Introduced in:** 22.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the permission group. |
| `Description` | `String` | no |  | The translated description of the permission group. |
| `Permissions` | `Permissions[]` | no | [Permissions](Common.md#Common.Permission) | The permissions that apply to the permission group. |

**References out:** [Permissions](Common.md#Common.Permission)
**Referenced by:** [WarehousePermissions](Common.md#Common.WarehousePermission)

<a id="Common.Permission"></a>
### Permissions

Represents a permission node.

- **Endpoint:** `GET /api/v1/Common/Permissions`
- **Required permission:** Show user
- **Introduced in:** 22.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the permission. |
| `PermissionId` | `Guid` | no |  | The programmatic identifier of the permission node. |
| `IsDenied` | `Boolean` | no |  | Whether or not the permission is denied. |
| `ParentClass` | `Guid` | no |  | The GUID identifier of the type of entity that the permission belongs to. |
| `ParentId` | `Int64` | no |  | The business key identifier of the parent that the permission belongs to. |

**Referenced by:** [PermissionGroups](Common.md#Common.PermissionGroup), [WarehousePermissions](Common.md#Common.WarehousePermission)

<a id="Common.PersonManufacturingPrintSettings"></a>
### PersonManufacturingPrintSettings

Represents manufacturing print settings for a person.

- **Endpoint:** `GET /api/v1/Common/PersonManufacturingPrintSettings`
- **Required permission:** Show person
- **Introduced in:** 2.28

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the person manufacturing print settings. |
| `Copies` | `Int32` | no |  | Number of copies of the document. |
| `PrintExternalDocuments` | `Boolean` | no |  | Specifies if external documents should be included in the printout. |
| `FormReportId` | `Int64` | no |  | The business key identifier of the form report the settings applies to. |

**Referenced by:** [Persons](Common.md#Common.Person)

<a id="Common.PersonRelative"></a>
### PersonRelatives

Represents the relative of a person.

- **Endpoint:** `GET /api/v1/Common/PersonRelatives`
- **Required permission:** Show person
- **Introduced in:** 22.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the relative. |
| `PersonId` | `Int64` | no |  | The business key identifier of the person that the relative is related to. |
| `Name` | `String` | no |  | The name of the relative. |

**Referenced by:** [Persons](Common.md#Common.Person)

<a id="Common.Person"></a>
### Persons

Represents a person.

- **Endpoint:** `GET /api/v1/Common/Persons`
- **Required permission:** Show person
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the person. |
| `BlockedContextType` | `Int32` | no |  | Specifies where the person block applies. |
| `IsRecordingEmployee` | `Boolean` | no |  | Specifies if the person has any type of employee recording enabled. |
| `EmployeeNumber` | `String` | no |  | The human readable employee number of the person. |
| `FirstName` | `String` | no |  | The first name of the person. |
| `LastName` | `String` | no |  | The last name of the person. |
| `PhoneNumber` | `String` | no |  | The phone number of the person. |
| `PrivatePhoneNumber` | `String` | no |  | The private phone number of the person. |
| `CellPhoneNumber` | `String` | no |  | The cell phone number of the person. |
| `PrivateCellPhoneNumber` | `String` | no |  | The private cell phone number of the person. |
| `InternalPhoneNumber` | `String` | no |  | The internal phone number of the person. |
| `EmailAddress` | `String` | no |  | The email address of the person. |
| `PrivateEmailAddress` | `String` | no |  | The private email address of the person. |
| `SkypeId` | `String` | no |  | The Skype identifier of the person. |
| `FaxNumber` | `String` | no |  | The fax number of the person. |
| `Position` | `String` | no |  | The position of the person. |
| `IsReference` | `Boolean` | no |  | Specifies if the person is a reference. |
| `IsPurchaseManager` | `Boolean` | no |  | Specifies if the person is a purchase manager. |
| `IsPlanner` | `Boolean` | no |  | Specififes if the person is a planner. |
| `IsAccountManager` | `Boolean` | no |  | Specifies if the person is an account manager. |
| `Contact` | `String` | no |  | The name of the person's contact. |
| `ContactPhoneNumber` | `String` | no |  | The phone number of the person's contact. |
| `ContactCellPhoneNumber` | `String` | no |  | The cell phone number of the person's contact. |
| `ContactEmailAddress` | `String` | no |  | The email address of the person's contact. |
| `AddressId` | `Int64?` | yes | [Addresses](Common.md#Common.Address) | The business key identifier of the person's address. References Addresses . |
| `Address` | `Addresses` | no | [Addresses](Common.md#Common.Address) | The address of the person. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the person's comment. Reference Comments . |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the person. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  | The date that the person starts being blocked from. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  | The date that the person stops being blocked. |
| `IsPersonBlocked` | `Boolean` | no |  | Specifies if the person is blocked. |
| `PersonBlockedById` | `Int64?` | yes |  | Specifies the application user that blocked the person. |
| `PersonBlockedDate` | `DateTimeOffset?` | yes |  | The date when the person was blocked. |
| `CanAuthorize` | `Boolean` | no |  | Specifies if the person can authorize invoices provided that EIM is not enabled for this MONITOR system. |
| `ApplicationUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that is coupled to the person. References ApplicationUsers . |
| `IsSeller` | `Boolean` | no |  | Specifies if the person is a seller. |
| `Initials` | `String` | no |  | Max length 5 |
| `DepartmentId` | `Int64` | no | [Departments](Common.md#Common.Department) | The business key identifier of the department that the person belongs to. References Departments . |
| `DistrictId` | `Int64?` | yes | [CustomerDistricts](Sales.md#Sales.CustomerDistrict) | The business key identifier of the district that the person belongs to. References CustomerDistricts . |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The business key identifier of the person's preferred language. References LanguageCodes . |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the person's default warehouse. References Warehouses . |
| `Category` | `String` | no |  | The category of the person. |
| `IdentityNumber` | `String` | no |  | The identity number of the person. |
| `GroupSettingsId` | `Int64?` | yes |  | The business key identifier of the person's attendance group settings. References AttendanceGroupSettings. |
| `UseWorkCenterManufacturingPrintSettings` | `Boolean` | no |  | Specifies if manufacturing order document settings should come from the work center's settings or the person's settings. |
| `ManufacturingPrintSettings` | `PersonManufacturingPrintSettings[]` | no | [PersonManufacturingPrintSettings](Common.md#Common.PersonManufacturingPrintSettings) | The person's print settings for manufacturing order documents. |
| `PlannedAbsences` | `PlannedAbsences[]` | no | [PlannedAbsences](TimeRecording.md#TimeRecording.PlannedAbsence) | The planned absences for the person. |
| `TimeBanks` | `PersonTimeBanks[]` | no | [PersonTimeBanks](TimeRecording.md#TimeRecording.PersonTimeBank) | The time banks for the person. |
| `Relatives` | `PersonRelatives[]` | no | [PersonRelatives](Common.md#Common.PersonRelative) | The relatives of the person. |
| `EmploymentPeriods` | `EmploymentPeriods[]` | no | [EmploymentPeriods](Common.md#Common.EmploymentPeriod) | The employment periods that belong to the personnel record. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) | The extra fields of the personnel record. |
| `IsProjectManager` | `Boolean` | no |  | Specifies if the person is a project manager. |
| `AvailableWorkshopSchedules` | `Schedules[]` | no | [Schedules](TimeRecording.md#TimeRecording.Schedule) | The workshop schedules of the personnel record. |
| `AvailableWorkCenters` | `PersonWorkCenters[]` | no | [PersonWorkCenters](TimeRecording.md#TimeRecording.PersonWorkCenter) | Specifies which work centers (and thereby which report numbers) the person should be allowed to select among in the priority plan and when starting work via report numbers. |
| `Signature` | `BlobData` | no | [BlobData](Common.md#Common.BlobData) | The entity signature blob data |
| `EmployeeRecordingType` | `Int32` | no |  | The employee recording type of the person. |
| `ScheduleManagementType` | `Int32` | no |  | The schedule management type of the person. |
| `PersonScheduleCycles` | `PersonScheduleCycles[]` | no |  | The schedule cycles of the personnel record. |
| `AttendanceRecordingAuthorizers` | `AttendanceRecordingAuthorizers[]` | no |  | The attendance recording authorizers of the personnel record. |
| `WorkMethod` | `Int32` | no |  | The work method of the person. |

- `BlockedContextType` (bitmask) — None=0, RegisterCustomerOrder=1
- `EmployeeRecordingType` (bitmask) — None=0, AttendanceAndWork=1, OnlyWork=2
- `ScheduleManagementType` (bitmask) — None=0, ScheduleCycle=1
- `WorkMethod` — OnlyChange=0, StartFinishAtWill=1

**References out:** [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BlobData](Common.md#Common.BlobData), [Comments](Common.md#Common.Comment), [CustomerDistricts](Sales.md#Sales.CustomerDistrict), [Departments](Common.md#Common.Department), [EmploymentPeriods](Common.md#Common.EmploymentPeriod), [ExtraFields](Common.md#Common.ExtraField), [LanguageCodes](Common.md#Common.LanguageCode), [PersonManufacturingPrintSettings](Common.md#Common.PersonManufacturingPrintSettings), [PersonRelatives](Common.md#Common.PersonRelative), [PersonTimeBanks](TimeRecording.md#TimeRecording.PersonTimeBank), [PersonWorkCenters](TimeRecording.md#TimeRecording.PersonWorkCenter), [PlannedAbsences](TimeRecording.md#TimeRecording.PlannedAbsence), [Schedules](TimeRecording.md#TimeRecording.Schedule), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [AttendanceChart](TimeRecording.md#TimeRecording.AttendanceChart), [BlanketOrderPurchases](Purchase.md#Purchase.BlanketOrderPurchase), [BlanketOrderSales](Sales.md#Sales.BlanketOrderSales), [BusinessOpportunities](Sales.md#Sales.BusinessOpportunity), [BusinessOpportunityActivities](Sales.md#Sales.BusinessOpportunityActivity), [BusinessOpportunitySalesProcessSteps](Sales.md#Sales.BusinessOpportunitySalesProcessStep), [BusinessOpportunityTypes](Sales.md#Sales.BusinessOpportunityType), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CreateSalesPickingList](Sales.md#Sales.CreateSalesPickingList), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [DelegatedWork](Common.md#Common.DelegatedWork), [EmploymentPeriods](Common.md#Common.EmploymentPeriod), [Inquiries](Purchase.md#Purchase.Inquiry), [MaintenanceReportings](Manufacturing.md#Manufacturing.MaintenanceReporting), [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingPickingLists](Manufacturing.md#Manufacturing.ManufacturingPickingList), [PartPlanningInformation](Inventory.md#Inventory.PartPlanningInformation), [Parts](Inventory.md#Inventory.Part), [PartTemplates](Inventory.md#Inventory.PartTemplate), [PersonTimeBanks](TimeRecording.md#TimeRecording.PersonTimeBank), [PersonWorkCenters](TimeRecording.md#TimeRecording.PersonWorkCenter), [ProductRecords](Inventory.md#Inventory.ProductRecord), [ProjectActivityCalendarAppointments](Common.md#Common.ProjectActivityCalendarAppointment), [Projects](Common.md#Common.Project), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [QuantityChanges](Inventory.md#Inventory.QuantityChange), [Quotes](Sales.md#Sales.Quote), [RecordingDays](TimeRecording.md#TimeRecording.RecordingDay), [SalesAgreements](Sales.md#Sales.SalesAgreement), [SalesPickingLists](Sales.md#Sales.SalesPickingList), [SalesProcessTemplateRows](Sales.md#Sales.SalesProcessTemplateRow), [ShipmentCustoms](Sales.md#Sales.ShipmentCustoms), [StandbyWorks](TimeRecording.md#TimeRecording.StandbyWork), [Suppliers](Purchase.md#Purchase.Supplier), [WorkIntervals](TimeRecording.md#TimeRecording.WorkInterval)

<a id="Common.PriceList"></a>
### PriceLists

Represents a price list.

- **Endpoint:** `GET /api/v1/Common/PriceLists`
- **Required permission:** Show price lists
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the price list. |
| `Number` | `Int64` | no |  | The price list number. |
| `Description` | `String` | no |  | The translated description of the price list. |
| `ConversionFactor` | `Decimal` | no |  | The conversion factor of the price list. |
| `ParentPriceListId` | `Int64?` | yes | [PriceLists](Common.md#Common.PriceList) | The business key identifier of the price list's parent. References PriceLists . |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the price list's currency. References Currencies . |
| `PriceListBasis` | `Int32` | no |  | Specifies the basis of the price list. |
| `CompanyIds` | `Int64[]` | no |  | The business key identifiers of the companies that this entity is available for. |

- `PriceListBasis` — None=0, ParentPriceList=1, StandardPrice=2

**References out:** [Currencies](Common.md#Common.Currency), [PriceLists](Common.md#Common.PriceList)
**Referenced by:** [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow), [BlanketOrderSalesTypes](Sales.md#Sales.BlanketOrderSalesType), [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType), [Customers](Sales.md#Sales.Customer), [PriceChangeLogs](Inventory.md#Inventory.PriceChangeLog), [PriceLists](Common.md#Common.PriceList), [QuoteTypes](Sales.md#Sales.QuoteType), [SalesAgreementTypes](Sales.md#Sales.SalesAgreementType), [SalesPrices](Sales.md#Sales.SalesPrice)

<a id="Common.Probability"></a>
### Probabilities

Represents a probability.

- **Endpoint:** `GET /api/v1/Common/Probabilities`
- **Required permission:** Show probability codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the probability. |
| `Number` | `Int64` | no |  | The probability number. |
| `Description` | `String` | no |  | The translated description of the probability. |
| `Percentage` | `Decimal?` | yes |  | The probability percentage. |
| `IsPreset` | `Boolean` | no |  | Specifies if the probability is the default. |

**Referenced by:** [Customers](Sales.md#Sales.Customer), [Quotes](Sales.md#Sales.Quote)

<a id="Common.ProductGroup"></a>
### ProductGroups

Represents a product group.

- **Endpoint:** `GET /api/v1/Common/ProductGroups`
- **Required permission:** Show posting matrix
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the product group. |
| `Number` | `String` | no |  | The product group number. |
| `Description` | `String` | no |  | The translated description of the product group. |
| `Alias` | `String` | no |  | The product group alias. |
| `IsDefault` | `Boolean` | no |  | Specifies if the product group is the default. |

**Referenced by:** [DiscountCategoryRows](Common.md#Common.DiscountCategoryRow), [Parts](Inventory.md#Inventory.Part), [PartTemplates](Inventory.md#Inventory.PartTemplate)

<a id="Common.ProjectActivity"></a>
### ProjectActivities

Represents a project activity.

- **Endpoint:** `GET /api/v1/Common/ProjectActivities`
- **Required permission:** Show Activity list – Project
- **Introduced in:** 2.36

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project activity. |
| `Number` | `Int64` | no |  | The number of the project activity. |
| `ReportedTimeInHours` | `Decimal` | no |  | The reported time in hours of the project activity. |
| `RestTimeInHours` | `Decimal` | no |  | The rest time in hours of the project activity. |
| `PlannedTimeInHours` | `Decimal` | no |  | The planned time in hours of the project activity. |
| `ShowInProjectReport` | `Boolean` | no |  | Specifies if the project activity should be shown in the project report. |
| `ParentId` | `Int64` | no | [ProjectPhases](Common.md#Common.ProjectPhase) | The business key identifier of the activity's parent. References ProjectPhases . |
| `LockedDelegateWork` | `Boolean` | no |  | Specifies if the activity's delegate work is locked. |
| `ActivityTypeId` | `Int64` | no | [ProjectActivityTypes](Common.md#Common.ProjectActivityType) | The business key identifier of the activity's type. References ProjectActivityTypes . |
| `ActivityType` | `ProjectActivityTypes` | no | [ProjectActivityTypes](Common.md#Common.ProjectActivityType) | The type of the project activity. |
| `CompletedByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that has completed the activity. References ApplicationUsers . |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that is responsible for the activity. References ApplicationUsers . |
| `Description` | `String` | no |  | The description of the activity. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the activity's comment. References Comments . |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the activity. |
| `Status` | `Int32` | no |  | The status of the activity. |
| `ReminderId` | `Int64?` | yes |  | The business key identifier of the activity's reminder. References Reminder. |
| `PlannedCompletionDate` | `DateTimeOffset` | no |  | The planned completion date of the activity. |
| `CompletionDate` | `DateTimeOffset?` | yes |  | The completion date of the activity. |
| `PlannedStartDate` | `DateTimeOffset?` | yes |  | The planned start date of the activity. |
| `ActualStartDate` | `DateTimeOffset?` | yes |  | The actual start date of the activity. |
| `Mandatory` | `Boolean` | no |  | Whether or not the activity is mandatory. |
| `CalendarAppointmentId` | `String` | no |  | The unique calendar appointment identifier of the activity. |

- `Status` — Registered=1, InProgress=2, History=9

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Comments](Common.md#Common.Comment), [ProjectActivityTypes](Common.md#Common.ProjectActivityType), [ProjectPhases](Common.md#Common.ProjectPhase)
**Referenced by:** [DelegatedWork](Common.md#Common.DelegatedWork), [ProjectActivityCalendarAppointments](Common.md#Common.ProjectActivityCalendarAppointment), [ProjectActivityRelations](Common.md#Common.ProjectActivityRelation), [ProjectPhases](Common.md#Common.ProjectPhase), [WorkIntervals](TimeRecording.md#TimeRecording.WorkInterval)

<a id="Common.ProjectActivityCalendarAppointment"></a>
### ProjectActivityCalendarAppointments

Represents a Project Activity Calendar Appointment.

- **Endpoint:** `GET /api/v1/Common/ProjectActivityCalendarAppointments`
- **Required permission:** Show projects
- **Introduced in:** 25.6

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project appointment. |
| `ProjectActivityId` | `Int64?` | yes | [ProjectActivities](Common.md#Common.ProjectActivity) | The business key identifier of the project activity. |
| `SenderPersonId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the sender person. |
| `CalendarAppointmentId` | `String` | no |  | The unique identifier of the appointment created in the user's calendar program. |

**References out:** [Persons](Common.md#Common.Person), [ProjectActivities](Common.md#Common.ProjectActivity)

<a id="Common.ProjectActivityRelation"></a>
### ProjectActivityRelations

Represents a relation between two project activities.

- **Endpoint:** `GET /api/v1/Common/ProjectActivityRelations`
- **Required permission:** Show Activity list – Project
- **Introduced in:** 2.50

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project activity relation. |
| `ParentId` | `Int64` | no | [ProjectActivities](Common.md#Common.ProjectActivity) | The business key identifier of the activity that the relation belongs to. |
| `DependentOnEntityId` | `Int64` | no | [ProjectActivities](Common.md#Common.ProjectActivity) | The business key identifier of the activity that the relation depends on. |
| `Type` | `Int32` | no |  | The type of activitity relation. |
| `RowIndex` | `Int32` | no |  | The row index of the activity relation. |

- `Type` — FinishedBeforeStart=0, StartedBeforeStart=1

**References out:** [ProjectActivities](Common.md#Common.ProjectActivity)

<a id="Common.ProjectActivityType"></a>
### ProjectActivityTypes

Represents a project activity type.

- **Endpoint:** `GET /api/v1/Common/ProjectActivityTypes`
- **Required permission:** Show basic data for project
- **Introduced in:** 2.36

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the type. |
| `ResponsibleUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the type's responsible user. References ApplicationUsers . |
| `PlannedTimeInHours` | `Decimal` | no |  | The planned time in hours of the type. |
| `LeadTimeInDays` | `Int32` | no |  | The lead time in days of the type. |
| `QueueTimeInDays` | `Int32` | no |  | The queue time in days of the type. |
| `CostTypeId` | `Int64` | no |  | The business key identifier of type's project cost type. References ProjectCostType. |
| `IsActive` | `Boolean` | no |  | Specifies if the project activity type is active. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of type's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the type. |
| `UseReminder` | `Boolean` | no |  | Specifies if the project activity type should use reminder. |
| `ShowInProjectReport` | `Boolean` | no |  | Specifies if the project activity type be shown in the project report. |
| `Code` | `Int64` | no |  | The code of the activity type. |
| `Description` | `String` | no |  | The description of the activity type. |
| `IsReportedAsDirectTime` | `Boolean` | no |  | Whether or not activities of this type should be reported as direct time. |

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Comments](Common.md#Common.Comment)
**Referenced by:** [ProjectActivities](Common.md#Common.ProjectActivity)

<a id="Common.ProjectAggregate"></a>
### ProjectAggregates

Represents a project aggregate.

- **Endpoint:** `GET /api/v1/Common/ProjectAggregates`
- **Required permission:** Show projects
- **Introduced in:** 2.46

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project aggregate. |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of the project the project aggregate belongs to. |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](Common.md#Common.ProjectCostType) | The business key identifier of the project cost type the project aggregate belongs to. |
| `ExpectedResultCost` | `Decimal` | no |  | The expected result cost. |
| `ExpectedResultIncome` | `Decimal` | no |  | The expected result income. |
| `ExpectedResultTime` | `Decimal` | no |  | The expected result time in hours. |
| `ResultCost` | `Decimal` | no |  | The results cost. |
| `ResultIncome` | `Decimal` | no |  | The results income. |
| `ResultTime` | `Decimal` | no |  | The results time in hours. |

**References out:** [ProjectCostTypes](Common.md#Common.ProjectCostType), [Projects](Common.md#Common.Project)
**Referenced by:** [Projects](Common.md#Common.Project)

<a id="Common.ProjectCostBudget"></a>
### ProjectCostBudgets

Represents a project cost budget.

- **Endpoint:** `GET /api/v1/Common/ProjectCostBudgets`
- **Required permission:** Show projects
- **Introduced in:** 2.46

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project cost budget. |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of the project this project cost budget belongs to. |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](Common.md#Common.ProjectCostType) | The business key identifier of the project cost type this project cost budget belongs to. |
| `Hours` | `Decimal` | no |  | The time in hours of the project cost budget. |
| `Cost` | `Decimal` | no |  | The cost of the project cost budget. |
| `Income` | `Decimal` | no |  | The income of the project cost budget. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the project cost budget's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the project cost budget. |

**References out:** [Comments](Common.md#Common.Comment), [ProjectCostTypes](Common.md#Common.ProjectCostType), [Projects](Common.md#Common.Project)
**Referenced by:** [Projects](Common.md#Common.Project)

<a id="Common.ProjectCostForecast"></a>
### ProjectCostForecasts

Represents a project cost forecast.

- **Endpoint:** `GET /api/v1/Common/ProjectCostForecasts`
- **Required permission:** Show projects
- **Introduced in:** 2.46

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project cost forecast. |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of the project this project cost forecast belongs to. |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](Common.md#Common.ProjectCostType) | The business key identifier of the project cost type this project cost forecast belongs to. |
| `Hours` | `Decimal` | no |  | The time in hours of the project cost forecast. |
| `Cost` | `Decimal` | no |  | The cost of the project cost forecast. |
| `Income` | `Decimal` | no |  | The income of the project cost forecast. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the project cost forecast's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the project cost forecast. |

**References out:** [Comments](Common.md#Common.Comment), [ProjectCostTypes](Common.md#Common.ProjectCostType), [Projects](Common.md#Common.Project)
**Referenced by:** [Projects](Common.md#Common.Project)

<a id="Common.ProjectCostReportingEntry"></a>
### ProjectCostReportingEntries

Represents a project cost reporting entry.

- **Endpoint:** `GET /api/v1/Common/ProjectCostReportingEntries`
- **Required permission:** Report activity for any user
- **Introduced in:** 2.50

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project cost reporting entry. |
| `Number` | `Int64` | no |  | The human readable identifier of the project cost reporting entry. |
| `ProjectId` | `Int64?` | yes |  | The business key identifier of the project linked to the project cost reporting entry. |
| `IsIncome` | `Boolean` | no |  | Specifies if the project cost reporting entry concerns income. |
| `ActivityId` | `Int64?` | yes |  | The business key identifier of the project activity linked to the project cost reporting entry. |
| `ReportedTimeInHours` | `Decimal` | no |  | The time in hours reported by the project cost reporting entry. |
| `CostTypeId` | `Int64?` | yes |  | The business key identifier of the cost type linked to the project cost reporting entry. |
| `Amount` | `Decimal` | no |  | The amount reported by the project cost reporting entry. |
| `ReportingDate` | `DateTimeOffset` | no |  | The date of the project cost reporting entry. |
| `OurReferenceId` | `Int64?` | yes |  | The business key identifier of the reference for the project cost reporting entry. |
| `OurReferenceName` | `String` | no |  | The name of our reference for the project cost reporting entry. |
| `EmployeeId` | `Int64?` | yes |  | The business key identifier of the employee that performed the reporting. |
| `WorkCenterId` | `Int64?` | yes |  | The business key identifier of the work center the reporting concerns. |
| `DepartmentId` | `Int64?` | yes |  | The business key identifier of the department the reporting concerns. |
| `IsCancelled` | `Boolean` | no |  | Specifies if the project cost reporting entry is cancelled. |
| `CommentId` | `Int64?` | yes |  | The business key identifier of the comment for the project cost reporting entry. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the project cost reporting entry. |
| `CustomerReference` | `String` | no |  | Customer reference for the project cost reporting entry. Entered per log in Authorize/adjust and copied from the work recording. |
| `CustomerOrderNumber` | `String` | no |  | Customer order number for the project cost reporting entry. Entered per log in Authorize/adjust and copied from the work recording. |
| `GoodsMark` | `String` | no |  | Goods mark for the project cost reporting entry. Entered per log in Authorize/adjust and copied from the work recording. |
| `InternalCommentId` | `Int64?` | yes |  | The business key identifier of the internal comment for the project cost reporting entry. |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the project cost reporting entry. |

**References out:** [Comments](Common.md#Common.Comment)

<a id="Common.ProjectCostType"></a>
### ProjectCostTypes

Represents a project cost type.

- **Endpoint:** `GET /api/v1/Common/ProjectCostTypes`
- **Required permission:** Show projects
- **Introduced in:** 2.46

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project cost type. |
| `Number` | `Int64` | no |  | The human readable identifier of the project cost type. |
| `Description` | `String` | no |  | The translated description of the project cost type. |
| `Type` | `Int32` | no |  | The type of the project cost type. |

- `Type` — Cost=1, Income=2

**Referenced by:** [AttendanceAdditions](TimeRecording.md#TimeRecording.AttendanceAddition), [ProjectAggregates](Common.md#Common.ProjectAggregate), [ProjectCostBudgets](Common.md#Common.ProjectCostBudget), [ProjectCostForecasts](Common.md#Common.ProjectCostForecast)

<a id="Common.ProjectGroup"></a>
### ProjectGroups

Represents a project group.

- **Endpoint:** `GET /api/v1/Common/ProjectGroups`
- **Required permission:** Show basic data for project
- **Introduced in:** 24.6

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project group. |
| `Number` | `Int64` | no |  | The human readable identifier of the project group. |
| `Description` | `String` | no |  | The translated description of the project group. |

**Referenced by:** [Projects](Common.md#Common.Project)

<a id="Common.ProjectPhase"></a>
### ProjectPhases

Represents a project phase.

- **Endpoint:** `GET /api/v1/Common/ProjectPhases`
- **Required permission:** Show Activity list – Project
- **Introduced in:** 2.36

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project phase. |
| `Description` | `String` | no |  | The translated description of the project phase. |
| `Number` | `Int64` | no |  | The number of the project phase. |
| `PhaseTypeId` | `Int64` | no | [ProjectPhaseTypes](Common.md#Common.ProjectPhaseType) | The business key identifier of the type of the project phase. References ProjectPhaseTypes . |
| `PhaseType` | `ProjectPhaseTypes` | no | [ProjectPhaseTypes](Common.md#Common.ProjectPhaseType) | The type of the project phase. |
| `ResponsibleUserId` | `Int64` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the project phase's reponsible user. References ApplicationUsers . |
| `ParentId` | `Int64` | no | [Projects](Common.md#Common.Project) | The business key identifier of the phase's parent. References Projects . |
| `IsDummy` | `Boolean` | no |  | Specifies if the project phase is a dummy phase. |
| `RowIndex` | `Int32` | no |  | The row index of the project phase. |
| `Activities` | `ProjectActivities[]` | no | [ProjectActivities](Common.md#Common.ProjectActivity) | The activities of the project phase. |

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser), [ProjectActivities](Common.md#Common.ProjectActivity), [ProjectPhaseTypes](Common.md#Common.ProjectPhaseType), [Projects](Common.md#Common.Project)
**Referenced by:** [ProjectActivities](Common.md#Common.ProjectActivity), [Projects](Common.md#Common.Project)

<a id="Common.ProjectPhaseType"></a>
### ProjectPhaseTypes

Represents a project phase type.

- **Endpoint:** `GET /api/v1/Common/ProjectPhaseTypes`
- **Required permission:** Show basic data for project
- **Introduced in:** 2.36

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the type. |
| `Number` | `Int32` | no |  | The number of the type. |
| `Description` | `String` | no |  | The translated description of the type. |
| `ManagerId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the manager of the type. References ApplicationUsers . |

**References out:** [ApplicationUsers](Common.md#Common.ApplicationUser)
**Referenced by:** [ProjectPhases](Common.md#Common.ProjectPhase)

<a id="Common.Project"></a>
### Projects

Represents a project.

- **Endpoint:** `GET /api/v1/Common/Projects`
- **Required permission:** Show projects
- **Introduced in:** 2.31

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project. |
| `Code` | `String` | no |  | The human readable code of the project. |
| `Description` | `String` | no |  | The translated description of the project. |
| `Status` | `Int32` | no |  | The status of the project. |
| `Priority` | `Int32` | no |  | The priority of the project. |
| `StartDate` | `DateTimeOffset` | no |  | The start date of the project. |
| `EndDate` | `DateTimeOffset` | no |  | The end date of the project. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer that the project belongs to. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The business key identifier of the project's customer order. |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](Sales.md#Sales.CustomerOrder) | The customer order of the project. |
| `CustomerOrderNumber` | `String` | no |  | The customer's order number of the project. |
| `SellerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the project's seller. |
| `Seller` | `Persons` | no | [Persons](Common.md#Common.Person) | The seller of the project. |
| `OurReferenceId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the project's our reference. |
| `OurReference` | `Persons` | no | [Persons](Common.md#Common.Person) | Our reference of the project. |
| `CustomerReferenceId` | `Int64?` | yes | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The business key identifier of the project's customer reference. |
| `CustomerReference` | `BusinessContactReferences` | no | [BusinessContactReferences](Common.md#Common.BusinessContactReference) | The customer's reference of the project. |
| `InternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the project's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the project |
| `ExternalCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the project's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The external comment of the project. |
| `LongDescription` | `String` | no |  | The long description of the project. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](Common.md#Common.ExtraField) | A collection of extra field values for the project. |
| `Phases` | `ProjectPhases[]` | no | [ProjectPhases](Common.md#Common.ProjectPhase) | The phases of the project. |
| `ProjectTypeId` | `Int64` | no | [ProjectTypes](Common.md#Common.ProjectType) | The business key identifier of the project's type. |
| `ProjectType` | `ProjectTypes` | no | [ProjectTypes](Common.md#Common.ProjectType) | The project type. |
| `ProjectGroupId` | `Int64?` | yes | [ProjectGroups](Common.md#Common.ProjectGroup) | The business key identifier of the project's group. |
| `ProjectGroup` | `ProjectGroups` | no | [ProjectGroups](Common.md#Common.ProjectGroup) | The project group of the project. |
| `ProjectCostBudgets` | `ProjectCostBudgets[]` | no | [ProjectCostBudgets](Common.md#Common.ProjectCostBudget) | The project cost budgets of the project. |
| `ProjectCostForecasts` | `ProjectCostForecasts[]` | no | [ProjectCostForecasts](Common.md#Common.ProjectCostForecast) | The project cost forecasts of the project. |
| `ProjectAggregates` | `ProjectAggregates[]` | no | [ProjectAggregates](Common.md#Common.ProjectAggregate) | The project aggregates of the project. |
| `ParentProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of the parent project to the project. |
| `ProjectManagerId` | `Int64?` | yes | [Persons](Common.md#Common.Person) | The business key identifier of the manager for the project. |

- `Status` — Registered=1, InProgress=3, Finished=4, Standby=6, History=9

**References out:** [BusinessContactReferences](Common.md#Common.BusinessContactReference), [Comments](Common.md#Common.Comment), [CustomerOrders](Sales.md#Sales.CustomerOrder), [Customers](Sales.md#Sales.Customer), [ExtraFields](Common.md#Common.ExtraField), [Persons](Common.md#Common.Person), [ProjectAggregates](Common.md#Common.ProjectAggregate), [ProjectCostBudgets](Common.md#Common.ProjectCostBudget), [ProjectCostForecasts](Common.md#Common.ProjectCostForecast), [ProjectGroups](Common.md#Common.ProjectGroup), [ProjectPhases](Common.md#Common.ProjectPhase), [Projects](Common.md#Common.Project), [ProjectTypes](Common.md#Common.ProjectType)
**Referenced by:** [AdditionRecordings](TimeRecording.md#TimeRecording.AdditionRecording), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [Inquiries](Purchase.md#Purchase.Inquiry), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [Parts](Inventory.md#Inventory.Part), [ProjectAggregates](Common.md#Common.ProjectAggregate), [ProjectCostBudgets](Common.md#Common.ProjectCostBudget), [ProjectCostForecasts](Common.md#Common.ProjectCostForecast), [ProjectPhases](Common.md#Common.ProjectPhase), [Projects](Common.md#Common.Project), [SalesAgreements](Sales.md#Sales.SalesAgreement)

<a id="Common.ProjectType"></a>
### ProjectTypes

Represents a project type.

- **Endpoint:** `GET /api/v1/Common/ProjectTypes`
- **Required permission:** Show basic data for project
- **Introduced in:** 2.43

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the project type. |
| `Number` | `Int64` | no |  | The human readable identifier of the project type. |
| `Description` | `String` | no |  | The translated description of the project type. |

**Referenced by:** [Projects](Common.md#Common.Project)

<a id="Common.ReasonCodeDebitNote"></a>
### ReasonCodeDebitNotes

Represents a reason code for debit note.

- **Endpoint:** `GET /api/v1/Common/ReasonCodeDebitNotes`
- **Required permission:** Show cause codes
- **Introduced in:** 25.6

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the reason code debit note. |
| `Code` | `String` | no |  | The human readable identifier of the reason code debit note. |
| `Description` | `String` | no |  | The translated description of the reason code debit note. |
| `Active` | `Boolean` | no |  | Specifies if the reason code debit note is active. |

**Referenced by:** [CustomerOrders](Sales.md#Sales.CustomerOrder)

<a id="Common.ReasonCode"></a>
### ReasonCodes

Represents a reason code.

- **Endpoint:** `GET /api/v1/Common/ReasonCodes`
- **Required permission:** Show cause codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the reason code. |
| `Type` | `Int32` | no |  | The usage type of the reason code. |
| `Code` | `String` | no |  | The alphanumeric code of the reason code. |
| `Description` | `String` | no |  | The translated description of the reason code. |
| `CommentMandatory` | `Boolean` | no |  | Specifies if a comment is mandatory for the reason code. |
| `Active` | `Boolean` | no |  | Specifies if the reason code is active in the system. |

- `Type` (bitmask) — All=0, PurchaseOrder=1, ManufacturingOrder=2

**Referenced by:** [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)

<a id="Common.RejectionCodeItem"></a>
### RejectionCodeItems

Represents a rejection code.

- **Endpoint:** `GET /api/v1/Common/RejectionCodeItems`
- **Required permission:** Show rejection codes/cause codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the rejection code. |
| `Code` | `String` | no |  | The string identifier of the rejection code. |
| `Description` | `String` | no |  | The translated description of the rejection code. |
| `Active` | `Boolean` | no |  | Specifies if the rejection code item is active. |
| `ForcedComment` | `Boolean` | no |  | Specifies if the rejection code item requires a comment. |
| `Type` | `Int32` | no |  | The rejection code item type. |

- `Type` (bitmask) — None=0, ManufacturingReporting=1, ReceivingInspectionPurchase=2, CustomerNonConformity=4, SupplierNonConformity=8, InternalNonConformity=16, Standard8DNonConformity=32

**Referenced by:** [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink)

<a id="Common.RemotePartConfigurationRow"></a>
### RemotePartConfigurationRows

Represents a remote part configuration row.

- **Endpoint:** `GET /api/v1/Common/RemotePartConfigurationRows`
- **Required permission:** Show part
- **Introduced in:** 24.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the remote part configuration row. |
| `ParentId` | `Int64` | no |  | The business key identifier of the remote part configuration. |
| `ManualPriceOrDiscount` | `Boolean` | no |  | Indicates manual change of price or discount. |
| `PriceEach` | `Decimal` | no |  | The price set. |
| `Discount` | `Decimal` | no |  | The discount set. |
| `CurrencyCode` | `String` | no |  | The currency set. |

**Referenced by:** [RemotePartConfigurations](Common.md#Common.RemotePartConfiguration)

<a id="Common.RemotePartConfiguration"></a>
### RemotePartConfigurations

Represents a remote part configuration.

- **Endpoint:** `GET /api/v1/Common/RemotePartConfigurations`
- **Required permission:** Show part
- **Introduced in:** 24.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | /// The business key identifier of the remote part configuration. |
| `PartConfigurationIdInRemoteCompany` | `Int64` | no | [PartConfigurations](Common.md#Common.PartConfiguration) | The business key identifier of the row's part configuration in the remote company. |
| `Rows` | `RemotePartConfigurationRows[]` | no | [RemotePartConfigurationRows](Common.md#Common.RemotePartConfigurationRow) | A collection of remote comfiguration rows that belong to the remote configuration. |

**References out:** [PartConfigurations](Common.md#Common.PartConfiguration), [RemotePartConfigurationRows](Common.md#Common.RemotePartConfigurationRow)

<a id="Common.Reseller"></a>
### Resellers

Represents a reseller.

- **Endpoint:** `GET /api/v1/Common/Resellers`
- **Required permission:** Show customer
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the reseller. |
| `Code` | `Int64` | no |  | The reseller code. |
| `Name` | `String` | no |  | The name of the reseller. |
| `Provision` | `Decimal` | no |  | The reseller provision in percent. |

**Referenced by:** [Customers](Sales.md#Sales.Customer)

<a id="Common.Revision"></a>
### Revisions

Represents a revision.

- **Endpoint:** `GET /api/v1/Common/Revisions`
- **Required permission:** Show part
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the revision. |
| `Number` | `String` | no |  | The revision number. Max length 25 Nullable No Unique Yes (per Part) |
| `ValidFrom` | `DateTimeOffset?` | yes |  | The valid from date of the revision. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the revision comment. References Comments . |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The revision comment. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part that the revision belongs to. References . |

**References out:** [Comments](Common.md#Common.Comment), [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [InquiryRows](Purchase.md#Purchase.InquiryRow), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [PartLocations](Inventory.md#Inventory.PartLocation), [Parts](Inventory.md#Inventory.Part), [ProductRecords](Inventory.md#Inventory.ProductRecord), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](Sales.md#Sales.QuoteRow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow)

<a id="Common.Role"></a>
### Roles

Represents a user role.

- **Endpoint:** `GET /api/v1/Common/Roles`
- **Required permission:** Show user
- **Introduced in:** 22.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the role. |
| `Description` | `String` | no |  | The translated description of the role. |
| `IsSuperUser` | `Boolean` | no |  | Whether or not application user's that belong to the role are considered super users. |

**Referenced by:** [WarehousePermissions](Common.md#Common.WarehousePermission)

<a id="Common.ServerPrinter"></a>
### ServerPrinters

Represents a server printer that can be used to print documents via the MONITOR server.

- **Endpoint:** `GET /api/v1/Common/ServerPrinters`
- **Introduced in:** 2.52

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the server printer. |
| `Number` | `String` | no |  | The human readable identifier of the server printer. |
| `Description` | `String` | no |  | The translated description of the server printer. |
| `Name` | `String` | no |  | The name of the printer that the server printer connects to. |
| `Orientation` | `Int32` | no |  | The printout orientation to apply to the server printer. |
| `DuplexMode` | `Int32` | no |  | The duplex mode to apply to the server printer. |
| `PaperSize` | `Int32` | no |  | The paper size to apply to the server printer. |
| `Width` | `Int32` | no |  | The paper width in millimeters to use if the paper size is "custom". |
| `Height` | `Int32` | no |  | The paper height in millimeters to use if the paper size is "custom". |
| `ColorMode` | `Int32` | no |  | The color mode to apply to the server printer. |
| `FilePathId` | `Int64?` | yes | [FilePaths](Common.md#Common.FilePath) | The business key identifier of the file path used as output path of a Microsoft Print To PDF Printer References FilePaths . |
| `FilePath` | `FilePaths` | no | [FilePaths](Common.md#Common.FilePath) | The file path used as output path of a Microsoft Print To PDF Printer References FilePaths . |
| `SubPath` | `String` | no | [FilePaths](Common.md#Common.FilePath) | The sub path applied to used as output path of a Microsoft Print To PDF Printer |

- `Orientation` — Portrait=0, Landscape=1, Auto=2
- `DuplexMode` — None=0, LongEdge=1, ShortEdge=2
- `PaperSize` — A4=0, A3=1, A5=2, Custom=3, PrinterDefault=4, Letter=5
- `ColorMode` — BlackAndWhite=0, FullColor=1

**References out:** [FilePaths](Common.md#Common.FilePath)
**Referenced by:** [ApplicationUserPrinters](Common.md#Common.ApplicationUserPrinter)

<a id="Common.StaggeredPrice"></a>
### StaggeredPrices

Represents a staggered price.

- **Endpoint:** `GET /api/v1/Common/StaggeredPrices`
- **Required permission:** Show part
- **Introduced in:** 2.34

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the staggered price. |
| `PartId` | `Int64` | no | [Parts](Inventory.md#Inventory.Part) | The business key identifier of the part the staggered price belongs to. |
| `Price` | `Decimal` | no |  | The price on the staggered price in the parent's currency. |
| `LowerBoundaryQuantity` | `Decimal` | no |  | The lower boundary quantity on the staggered price. |
| `FuturePrice` | `Decimal?` | yes |  | The future price on the staggered price in the parent's currency. |
| `ShippingPrice` | `Decimal` | no |  | The shipping price on the staggered price in the parent's currency. |
| `ParentClass` | `Guid` | no |  | The GUID of the staggered price's parent type. |
| `ParentId` | `Int64` | no |  | The business key identifier of the staggered price's parent. |

**References out:** [Parts](Inventory.md#Inventory.Part)
**Referenced by:** [CustomerPartLinks](Sales.md#Sales.CustomerPartLink), [SalesPrices](Sales.md#Sales.SalesPrice)

<a id="Common.StatisticalGoodsCode"></a>
### StatisticalGoodsCodes

Represents a queryable statistical goods code.

- **Endpoint:** `GET /api/v1/Common/StatisticalGoodsCodes`
- **Required permission:** Show CN codes
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the statistical goods code. |
| `Code` | `String` | no |  | The human readable identifier of the statistical goods code. |
| `Description` | `String` | no |  | The translated description of the statistical goods code. |
| `DeclarationType` | `Int32` | no |  | The declaration type of the statistical goods code. |

- `DeclarationType` — Weight=1, OtherQuantity=2, WeightAndOtherQuantity=3, ExcludeFromDeclaration=4

**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [InquiryRows](Purchase.md#Purchase.InquiryRow), [Parts](Inventory.md#Inventory.Part), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](Sales.md#Sales.QuoteRow), [ShipmentCustomsRows](Sales.md#Sales.ShipmentCustomsRow)

<a id="Common.Tag"></a>
### Tags

Represents a tag.

- **Endpoint:** `GET /api/v1/Common/Tags`
- **Required permission:** Show part
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the tag. |
| `OwnerTypeId` | `Guid` | no |  | The GUID identifier for the type of entity that owns the tag. |
| `OwnerId` | `Int64` | no |  | The business key identifier for the owner of the tag. |
| `Name` | `String` | no |  | The name of the tag. |


<a id="Common.TariffAndServiceCode"></a>
### TariffAndServiceCodes

Represents a tariff and service code.

- **Endpoint:** `GET /api/v1/Common/TariffAndServiceCodes`
- **Required permission:** Show basic data for part
- **Introduced in:** 2.30

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the code. |
| `Code` | `String` | no |  | The human readable identifier of the code. |
| `Name` | `String` | no |  | The translated name of the code. |
| `Type` | `Int32?` | yes |  | The type of the code. |
| `IsActive` | `Boolean` | no |  | Specifies if the code is active. |

- `Type` — Sales=1, Service=2, Purchase=3

**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)

<a id="Common.TransactionTypeIntrastat"></a>
### TransactionTypeIntrastats

Represents a transaction type intrastat.

- **Endpoint:** `GET /api/v1/Common/TransactionTypeIntrastats`
- **Required permission:** Show transaction types
- **Introduced in:** 2.30

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the transaction type. |
| `Number` | `Int64` | no |  | The human readable identifier of the transaction type. |
| `IsDefault` | `Boolean` | no |  | Specifies if the transaction type is default. |
| `Description` | `String` | no |  | The translated description of the currency transaction type. |

**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow)

<a id="Common.TransferProfile"></a>
### TransferProfiles

Represents a transfer profile.

- **Endpoint:** `GET /api/v1/Common/TransferProfiles`
- **Required permission:** Show transfer profile
- **Introduced in:** 22.1

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the transfer profile. |
| `Number` | `Int64` | no |  | The number of the transfer profile. |
| `Description` | `String` | no |  | The description of the transfer profile. |
| `Usages` | `Int32` | no |  | The usages type of the transfer profile. |
| `TargetRole` | `Int32` | no |  | The role of the transfer profile. |
| `IsVerified` | `Boolean` | no |  | Specifies if this transfer profile is verified. |
| `IsActive` | `Boolean` | no |  | Specifies if this transfer profile is active. |
| `ConnectionProfileId` | `Int64` | no | [ConnectionProfiles](Common.md#Common.ConnectionProfile) | The business key identifier of the transfer profile's connection profile. |
| `RemoteWarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the transfer profile's remote warehouse. |
| `OrderTransferSettingsId` | `Int64` | no | [OrderTransferSettings](Common.md#Common.OrderTransferSetting) | The business key identifier of the transfer profile's order transfer setting. |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the transfer profile's supplier. |
| `CustomerCode` | `String` | no |  | The customer code of the transfer profile. |

- `Usages` (bitmask) — None=0, CustomerOrderTransfer=1, PartSynchronization=2, PartInformation=4
- `TargetRole` — ManufacturingCompany=0, SalesCompany=1

**References out:** [ConnectionProfiles](Common.md#Common.ConnectionProfile), [OrderTransferSettings](Common.md#Common.OrderTransferSetting), [Suppliers](Purchase.md#Purchase.Supplier), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerOrderTypes](Sales.md#Sales.CustomerOrderType), [PartPlanningInformation](Inventory.md#Inventory.PartPlanningInformation), [QuoteRows](Sales.md#Sales.QuoteRow)

<a id="Common.Unit"></a>
### Units

Represents a quantity unit.

- **Endpoint:** `GET /api/v1/Common/Units`
- **Required permission:** Show units
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the unit. |
| `Code` | `String` | no |  | The translatable code of the unit. |
| `Description` | `String` | no |  | The translated description of the unit. |
| `Number` | `Int64` | no |  | The unit number. |

**Referenced by:** [Alloys](Inventory.md#Inventory.Alloy), [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow), [CompanyEmissionDetails](Common.md#Common.CompanyEmissionDetail), [CustomerOrderRowInflows](Sales.md#Sales.CustomerOrderRowInflow), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerPartLinks](Sales.md#Sales.CustomerPartLink), [FormTemplateRows](Common.md#Common.FormTemplateRow), [InquiryRows](Purchase.md#Purchase.InquiryRow), [MaintenanceReportingRows](Manufacturing.md#Manufacturing.MaintenanceReportingRow), [Parts](Inventory.md#Inventory.Part), [PartUnitUsages](Common.md#Common.PartUnitUsage), [PurchaseOrderAdviceRows](Purchase.md#Purchase.PurchaseOrderAdviceRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](Sales.md#Sales.QuoteRow), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow), [SalesForecastRows](Inventory.md#Inventory.SalesForecastRow), [ShipmentCustomsRows](Sales.md#Sales.ShipmentCustomsRow), [SupplierPartLinks](Purchase.md#Purchase.SupplierPartLink)

<a id="Common.VatGroup"></a>
### VatGroups

Represents a VAT group.

- **Endpoint:** `GET /api/v1/Common/VatGroups`
- **Required permission:** Show VAT settings
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the VAT group. |
| `Number` | `Int64` | no |  | The VAT group number. |
| `Description` | `String` | no |  | The translated description of the VAT group. |
| `DefaultVatRateForPurchaseId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) | The business key identifier of the VAT group's default VAT rate for Purchase. References VatRates . |
| `DefaultVatRateForSalesId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) | The business key identifier of the VAT group's default VAT rate for Sales. References VatRates . |
| `DefaultVatRateId` | `Int64` | no | [VatRates](Common.md#Common.VatRate) | This property is obsolete and split into DefaultVatRateForPurchaseId and DefaultVatRateForSalesId The business key identifier of the VAT group's default VAT rate. References VatRates . |

**References out:** [VatRates](Common.md#Common.VatRate)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [Countries](Common.md#Common.Country), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrders](Sales.md#Sales.CustomerOrder), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [Inquiries](Purchase.md#Purchase.Inquiry), [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [Quotes](Sales.md#Sales.Quote), [SalesAgreements](Sales.md#Sales.SalesAgreement)

<a id="Common.VatRate"></a>
### VatRates

Represents a VAT rate.

- **Endpoint:** `GET /api/v1/Common/VatRates`
- **Required permission:** Show VAT settings
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the VAT rate. |
| `Number` | `Int64` | no |  | The VAT rate number. |
| `Percentage` | `Decimal` | no |  | The VAT percentage of the rate. |
| `Description` | `String` | no |  | The translated description of the rate. |
| `ReversedTax` | `Boolean` | no |  | Specifies if reverse tax responsibility is applicable for the rate. |
| `OutputVatAccountId` | `Int64?` | yes | [Accounts](Accounting.md#Accounting.Account) | The business key identifier of the output account for the rate. |
| `InputVatAccountId` | `Int64?` | yes | [Accounts](Accounting.md#Accounting.Account) | The business key identifier of the input account for the rate. |
| `Active` | `Boolean` | no |  | Specifies if the rate is active. |
| `ReversedTaxPercentage` | `Decimal` | no |  | Specifies the reverse VAT percentage of the rate. |
| `ReferenceTextId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the rate reference text. References Comments . _(Replaced by Reference.)_ |
| `ReferenceText` | `Comments` | no | [Comments](Common.md#Common.Comment) | The rate reference text. _(Replaced by Reference.)_ |
| `Reference` | `String` | no |  | The translated reference text of the rate. |
| `EcSalesType` | `Int32?` | yes |  | Specifies the European Commission sales type of the VAT rate. |
| `CodeType` | `Int32` | no |  | Specifies the VAT code type of the VAT rate. |
| `DatevVatCode` | `Int64?` | yes |  | The VAT code used in DATEV exports. |

- `EcSalesType` — Goods trade=1, Services=2, Third party trade=3, GoodsTrade=1, Services=2, ThirdPartyTrade=3
- `CodeType` (bitmask) — None=0, Sales=1, Purchase=2

**References out:** [Accounts](Accounting.md#Accounting.Account), [Comments](Common.md#Common.Comment)
**Referenced by:** [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting), [BlanketOrderPurchaseRows](Purchase.md#Purchase.BlanketOrderPurchaseRow), [BlanketOrderSalesRows](Sales.md#Sales.BlanketOrderSalesRow), [BookingRows](Accounting.md#Accounting.BookingRow), [CustomerOrderInvoiceRows](Sales.md#Sales.CustomerOrderInvoiceRow), [CustomerOrderPaymentPlanRows](Sales.md#Sales.CustomerOrderPaymentPlanRow), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [Customers](Sales.md#Sales.Customer), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [InquiryRows](Purchase.md#Purchase.InquiryRow), [Parts](Inventory.md#Inventory.Part), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](Sales.md#Sales.QuoteRow), [SalesAgreementBasisRows](Sales.md#Sales.SalesAgreementBasisRow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow), [VatGroups](Common.md#Common.VatGroup), [VoucherRows](Accounting.md#Accounting.VoucherRow)

<a id="Common.WarehousePermission"></a>
### WarehousePermissions

Represents an application user warehouse permission.

- **Endpoint:** `GET /api/v1/Common/WarehousePermissions`
- **Required permission:** Show user rights groups
- **Introduced in:** 22.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the warehouse permission. |
| `ApplicationUserId` | `Int64` | no |  | The business key identifier of the application user that the warehouse permission belongs to. |
| `WarehouseId` | `Int64` | no |  | The business key identifier of the warehouse that the warehouse permission applies to. |
| `PermissionGroups` | `PermissionGroups[]` | no | [PermissionGroups](Common.md#Common.PermissionGroup) | The permission groups that apply to the warehouse permission. |
| `Roles` | `Roles[]` | no | [Roles](Common.md#Common.Role) | The roles that apply to the warehouse permission. |
| `Permissions` | `Permissions[]` | no | [Permissions](Common.md#Common.Permission) | The individual permissions that apply to the warehouse permission. |

**References out:** [PermissionGroups](Common.md#Common.PermissionGroup), [Permissions](Common.md#Common.Permission), [Roles](Common.md#Common.Role)
**Referenced by:** [ApplicationUsers](Common.md#Common.ApplicationUser)

<a id="Common.Warehouse"></a>
### Warehouses

Represents a warehouse.

- **Endpoint:** `GET /api/v1/Common/Warehouses`
- **Required permission:** Show company information
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the warehouse. |
| `Name` | `String` | no |  | The warehouse name. |
| `Code` | `String` | no |  | The warehouse code. |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The business key identifier of the warehouse language code. References LanguageCodes . |
| `CountryId` | `Int64` | no | [Countries](Common.md#Common.Country) | The business key identifier of the warehouse country. References Countries . |
| `PlaceOfDispatch` | `String` | no |  | The place of dispatch for the warehouse. |
| `PalletRegistrationNumber` | `String` | no |  | The pallet registration number of the warehouse. _(Never used in G5.)_ |
| `Url` | `String` | no |  | The website URL of the warehouse. |
| `TimeZoneId` | `String` | no | [Companies](Common.md#Common.Company) | The time zone of the warehouse. Specified as a time zone identifier (e.g. "W. Europe Standard Time"). From 25.2 moved to Companies . _(Time zone is now on company level. All warhouses will return the same value as the company time zone.)_ |
| `TimeZone` | `Decimal?` | yes |  | The timezone offset of the warehouse. _(Replaced by TimeZoneId)_ |
| `CalendarId` | `Int64` | no | [Calendars](Common.md#Common.Calendar) | The business key identifier of the warehouse calendar. References Calendars . |
| `Calendar` | `Calendars` | no | [Calendars](Common.md#Common.Calendar) | The warehouse calendar. |
| `VatNumber` | `String` | no |  | The VAT number of the warehouse. |
| `DeliveryAddresses` | `DeliveryAddresses[]` | no | [DeliveryAddresses](Common.md#Common.DeliveryAddress) | All available delivery addresses of the warehouse. |

**References out:** [Calendars](Common.md#Common.Calendar), [Companies](Common.md#Common.Company), [Countries](Common.md#Common.Country), [DeliveryAddresses](Common.md#Common.DeliveryAddress), [LanguageCodes](Common.md#Common.LanguageCode)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [ApplicationUsers](Common.md#Common.ApplicationUser), [BlanketOrderSalesTypes](Sales.md#Sales.BlanketOrderSalesType), [CaseEntry](Inventory.md#Inventory.CaseEntry), [Companies](Common.md#Common.Company), [CustomerOrderInvoices](Sales.md#Sales.CustomerOrderInvoice), [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [CustomerOrders](Sales.md#Sales.CustomerOrder), [DeliveryAddressWarehouseInformations](Common.md#Common.DeliveryAddressWarehouseInformation), [EdiBehaviors](Common.md#Common.EdiBehavior), [Inquiries](Purchase.md#Purchase.Inquiry), [InquiryRows](Purchase.md#Purchase.InquiryRow), [InvoiceLogs](Sales.md#Sales.InvoiceLog), [Locations](Inventory.md#Inventory.Location), [ManufacturingOrderNodes](Manufacturing.md#Manufacturing.ManufacturingOrderNode), [ManufacturingOrderOperationReportings](Manufacturing.md#Manufacturing.ManufacturingOrderOperationReporting), [ManufacturingOrders](Manufacturing.md#Manufacturing.ManufacturingOrder), [ManufacturingPickingLists](Manufacturing.md#Manufacturing.ManufacturingPickingList), [MonitoringTaskRows](Common.md#Common.MonitoringTaskRow), [PartLocations](Inventory.md#Inventory.PartLocation), [PartPlanningInformation](Inventory.md#Inventory.PartPlanningInformation), [Parts](Inventory.md#Inventory.Part), [Persons](Common.md#Common.Person), [PhysicalInventoryLists](Inventory.md#Inventory.PhysicalInventoryList), [PurchaseOrderInvoices](Purchase.md#Purchase.PurchaseOrderInvoice), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [QuantityChanges](Inventory.md#Inventory.QuantityChange), [QuoteRows](Sales.md#Sales.QuoteRow), [Quotes](Sales.md#Sales.Quote), [SalesForecasts](Inventory.md#Inventory.SalesForecast), [SalesPickingLists](Sales.md#Sales.SalesPickingList), [Shipments](Sales.md#Sales.Shipment), [StockTransactions](Inventory.md#Inventory.StockTransaction), [TransferProfiles](Common.md#Common.TransferProfile), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)

<a id="Common.WriteOffCode"></a>
### WriteOffCodes

Represents a write off code.

- **Endpoint:** `GET /api/v1/Common/WriteOffCodes`
- **Required permission:** Show bank settings
- **Introduced in:** 22.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the write off code. |
| `Code` | `String` | no |  | The human readable identifier of the write off code. |
| `Description` | `String` | no |  | The translated description of the write off code. |
| `IncomingPaymentCodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the write off code's coding entry for incoming payments. |
| `IncomingPaymentCodingEntry` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The write off code's coding entry for incoming payments. |
| `OutgoingPaymentCodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the write off code's coding entry for outgoing payments. |
| `OutgoingPaymentCodingEntry` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The write off code's coding entry for outgoing payments. |

**References out:** [CodingEntries](Accounting.md#Accounting.CodingEntry)
**Referenced by:** [IncomingPayments](Accounting.md#Accounting.IncomingPayment), [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment), [SetOffDestination](Accounting.md#Accounting.SetOffDestination)


## Payload types

<a id="Common.FileLink"></a>
### FileLink

Represents a file that has been linked to a comment.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the file link. |
| `FilePathId` | `Int64` | no |  | The business key identifier of the file path. |
| `FileLinkContainerId` | `Int64` | no |  | The business key identifier of the file link container. |
| `IsDefault` | `Boolean` | no |  | Specifies if the linked file should be selected by default. |
| `IsGenerated` | `Boolean` | no |  | Specifies if the linked file has been automatically generated by MONITOR or not. |
| `Filename` | `String` | no |  | Specifies the filename of the linked file. |
| `Directory` | `String` | no |  | Specifies the directory path of the linked file. |
| `Orientation` | `Int32` | no |  | Specifies the preferred printing orientation of the file. |
| `AutomaticPrintOut` | `Boolean` | no |  | Specifies if the linked file should use automatic printouts. |
| `GenerateCopies` | `Boolean` | no |  | Specifies if the linked file should generate copies. |
| `AllowExternalEditing` | `Boolean` | no |  | Specifies if the linked file allows external editing. _(Will always return true.)_ |
| `PrinterType` | `Int32` | no |  | Specifies the preferred printer type of the file. |
| `SharePointFileVersion` | `String` | no |  | Specifies the SharePoint file version if file type is SharePoint. |
| `UseLatestPublishedVersion` | `Boolean` | no |  | Specifies if need to use latest published SharePoint file when file type is SharePoint. |

- `Orientation` — Portrait=0, Landscape=1, Auto=2
- `PrinterType` — Automatic=0, External1=1, External2=2, External3=3

**Referenced by:** [Comments](Common.md#Common.Comment), [FormReportData](Common.md#Common.FormReportData)

<a id="Common.FormReportData"></a>
### FormReportData

Represents form report data from MONITOR.

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Name` | `String` | no |  | The name of the form report. |
| `Data` | `String` | no |  | The form report PDF data represented as a Base64 string. |
| `FileLinkIds` | `Int64[]` | no | [FileLink](Common.md#Common.FileLink) | The business key identifiers of the file links associated with this report. References FileLink . |

**References out:** [FileLink](Common.md#Common.FileLink)

<a id="Common.Money"></a>
### Money

An object composite representing a money value.

- **Introduced in:** 2.33

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Amount` | `Decimal` | no |  | The money amount. |
| `CurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency that the amount is specified in. |

**References out:** [Currencies](Common.md#Common.Currency)


## Depends on other modules

- [Accounting](Accounting.md): [Accounts](Accounting.md#Accounting.Account), [CodingEntries](Accounting.md#Accounting.CodingEntry), [VoucherSeries](Accounting.md#Accounting.VoucherSeries)
- [Inventory](Inventory.md): [Parts](Inventory.md#Inventory.Part), [PartCodes](Inventory.md#Inventory.PartCode)
- [Manufacturing](Manufacturing.md): [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation)
- [Purchase](Purchase.md): [Suppliers](Purchase.md#Purchase.Supplier)
- [Sales](Sales.md): [Customers](Sales.md#Sales.Customer), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [CustomerDistricts](Sales.md#Sales.CustomerDistrict), [CustomerOrders](Sales.md#Sales.CustomerOrder)
- [TimeRecording](TimeRecording.md): [PersonTimeBanks](TimeRecording.md#TimeRecording.PersonTimeBank), [PersonWorkCenters](TimeRecording.md#TimeRecording.PersonWorkCenter), [PlannedAbsences](TimeRecording.md#TimeRecording.PlannedAbsence), [Schedules](TimeRecording.md#TimeRecording.Schedule)
