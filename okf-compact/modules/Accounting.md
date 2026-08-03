# Accounting

Monitor API module `Accounting`: 41 queryable entities, 0 commands, 2 payload types.

## Queryable entities

<a id="Accounting.AccountingBudgetPeriod"></a>
### AccountingBudgetPeriods

Represents an accounting budget period.

- **Endpoint:** `GET /api/v1/Accounting/AccountingBudgetPeriods`
- **Required permission:** Show budget
- **Introduced in:** 23.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `BudgetId` | `Int64` | no | [AccountingBudgets](/modules/Accounting.md#Accounting.AccountingBudget) |
| `PeriodId` | `Int64` | no | [AccountingYearPeriods](/modules/Accounting.md#Accounting.AccountingYearPeriod) |
| `Amount` | `Decimal` | no |  |
| `Quantity` | `Decimal` | no |  |

**References out:** [AccountingBudgets](/modules/Accounting.md#Accounting.AccountingBudget), [AccountingYearPeriods](/modules/Accounting.md#Accounting.AccountingYearPeriod)
**Referenced by:** [AccountingBudgets](/modules/Accounting.md#Accounting.AccountingBudget)

<a id="Accounting.AccountingBudget"></a>
### AccountingBudgets

Represents an accounting budget.

- **Endpoint:** `GET /api/v1/Accounting/AccountingBudgets`
- **Required permission:** Show budget
- **Introduced in:** 23.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountYearSettingId` | `Int64` | no | [AccountYearSettings](/modules/Accounting.md#Accounting.AccountYearSetting) |
| `AccountingYearId` | `Int64` | no | [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear) |
| `BalanceId` | `Int64` | no | [Balances](/modules/Accounting.md#Accounting.Balance) |
| `BudgetChartId` | `Int64` | no | [BudgetCharts](/modules/Accounting.md#Accounting.BudgetChart) |
| `BudgetTypeId` | `Int64` | no | [AccountingBudgetTypes](/modules/Accounting.md#Accounting.AccountingBudgetType) |
| `CodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `Periods` | `AccountingBudgetPeriods[]` | no | [AccountingBudgetPeriods](/modules/Accounting.md#Accounting.AccountingBudgetPeriod) |

**References out:** [AccountingBudgetPeriods](/modules/Accounting.md#Accounting.AccountingBudgetPeriod), [AccountingBudgetTypes](/modules/Accounting.md#Accounting.AccountingBudgetType), [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear), [AccountYearSettings](/modules/Accounting.md#Accounting.AccountYearSetting), [Balances](/modules/Accounting.md#Accounting.Balance), [BudgetCharts](/modules/Accounting.md#Accounting.BudgetChart), [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry)
**Referenced by:** [AccountingBudgetPeriods](/modules/Accounting.md#Accounting.AccountingBudgetPeriod)

<a id="Accounting.AccountingBudgetType"></a>
### AccountingBudgetTypes

Represents an accounting budget type.

- **Endpoint:** `GET /api/v1/Accounting/AccountingBudgetTypes`
- **Required permission:** Show basic data for budget
- **Introduced in:** 23.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Description` | `String` | no |  |
| `IsActive` | `Boolean` | no |  |

**Referenced by:** [AccountingBudgets](/modules/Accounting.md#Accounting.AccountingBudget)

<a id="Accounting.AccountingYearPeriod"></a>
### AccountingYearPeriods

Represents a accounting year period.

- **Endpoint:** `GET /api/v1/Accounting/AccountingYearPeriods`
- **Required permission:** Show accounting year
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `FromDate` | `DateTimeOffset?` | yes |  |
| `ToDate` | `DateTimeOffset?` | yes |  |
| `Number` | `Int32?` | yes |  |
| `Status` | `Int32` | no |  |
| `AccountingYearId` | `Int64` | no | [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear) |
| `AccountingYear` | `AccountingYears` | no | [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear) |

- `Status` — Undefined=0, Open=1, Closed=2, Locked=3

**References out:** [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear)
**Referenced by:** [AccountingBudgetPeriods](/modules/Accounting.md#Accounting.AccountingBudgetPeriod), [AccrualAccountingRows](/modules/Accounting.md#Accounting.AccrualAccountingRow)

<a id="Accounting.AccountingYear"></a>
### AccountingYears

Represents a accounting year.

- **Endpoint:** `GET /api/v1/Accounting/AccountingYears`
- **Required permission:** Show accounting year
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ActivePeriodId` | `Int64?` | yes |  |
| `Description` | `String` | no |  |
| `Status` | `Int32` | no |  |
| `OpeningBalanceLocked` | `Boolean` | no |  |

- `Status` — Active=0, Previous=1, PeriodFinancialStatement=2, Historical=9, Future=-1

**Referenced by:** [AccountingBudgets](/modules/Accounting.md#Accounting.AccountingBudget), [AccountingYearPeriods](/modules/Accounting.md#Accounting.AccountingYearPeriod), [AccountYearSettings](/modules/Accounting.md#Accounting.AccountYearSetting), [Balances](/modules/Accounting.md#Accounting.Balance), [OpeningBalances](/modules/Accounting.md#Accounting.OpeningBalance), [Vouchers](/modules/Accounting.md#Accounting.Voucher)

<a id="Accounting.Account"></a>
### Accounts

Represents a account.

- **Endpoint:** `GET /api/v1/Accounting/Accounts`
- **Required permission:** Show chart of accounts
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `Type` | `Int32` | no |  |

- `Type` — Assets=1, DebtAndOwnCapital=2, Incomes=3, Costs=4, Internal=5, BalanceSheet=6, OutsideBalanceSheet=7, Settlement=8, Wynikowe=9, FixedAssets=10, CurrentAssets=11, Equity=12, Liabilities=13, Other=14

**Referenced by:** [AccountYearSettings](/modules/Accounting.md#Accounting.AccountYearSetting), [BankAccounts](/modules/Accounting.md#Accounting.BankAccount), [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry), [SalesAgreementBases](/modules/Sales.md#Sales.SalesAgreementBasis), [SalesAgreements](/modules/Sales.md#Sales.SalesAgreement), [VatRates](/modules/Common.md#Common.VatRate)

<a id="Accounting.AccountsPayableCashDiscountLevel"></a>
### AccountsPayableCashDiscountLevels

Represents a cash discount level for an accounts payable.

- **Endpoint:** `GET /api/v1/Accounting/AccountsPayableCashDiscountLevels`
- **Required permission:** Show accounts payable
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no | [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable) |
| `Discount` | `Decimal?` | yes |  |
| `DiscountDate` | `DateTimeOffset?` | yes |  |
| `RowIndex` | `Int32?` | yes |  |

**References out:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable)

<a id="Accounting.AccountsPayable"></a>
### AccountsPayables

Represents a account's payable.

- **Endpoint:** `GET /api/v1/Accounting/AccountsPayables`
- **Required permission:** Show accounts payable
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Version` | `Int32` | no |  |
| `CancelCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `CancelComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](/modules/Common.md#Common.PaymentMethod) |
| `LanguageId` | `Int64` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `Language` | `LanguageCodes` | no | [LanguageCodes](/modules/Common.md#Common.LanguageCode) |
| `SuppliersInvoiceNumber` | `String` | no |  |
| `InvoiceType` | `Int32` | no |  |
| `IsCredit` | `Boolean` | no |  |
| `IsFinalBooked` | `Boolean` | no |  |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder) |
| `WarehouseId` | `Int64` | no | [Warehouses](/modules/Common.md#Common.Warehouse) |
| `PreliminaryBookingDate` | `DateTimeOffset?` | yes |  |
| `VoucherDate` | `DateTimeOffset?` | yes |  |
| `CancelVoucherDate` | `DateTimeOffset?` | yes |  |
| `SupplierAccountGroupId` | `Int64?` | yes | [SupplierAccountGroups](/modules/Purchase.md#Purchase.SupplierAccountGroup) |
| `CountryId` | `Int64` | no | [Countries](/modules/Common.md#Common.Country) |
| `Status` | `Int32` | no |  |
| `BlockMessageId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `BlockMessage` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `OCRNumber` | `String` | no |  |
| `UseOCRNumber` | `Boolean` | no |  |
| `CreditedAccountsPayableId` | `Int64?` | yes | [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable) |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |
| `BlockedStatus` | `Int32` | no |  |
| `BlockedContextType` | `Int32` | no |  |
| `HasEimInvoice` | `Boolean` | no |  |
| `HoldEimInvoice` | `Boolean` | no |  |
| `EimInvoiceStatus` | `Int32` | no |  |
| `InvoiceNumber` | `Int64` | no |  |
| `InvoiceDate` | `DateTimeOffset` | no |  |
| `DueDate` | `DateTimeOffset` | no |  |
| `InvoiceAmount` | `Decimal` | no |  |
| `InvoiceAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `InvoiceAmountInCompanyCurrency` | `Decimal` | no |  |
| `InvoiceAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `VatAmount` | `Decimal` | no |  |
| `VatAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `VatAmountInCompanyCurrency` | `Decimal` | no |  |
| `VatAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `RestAmount` | `Decimal` | no |  |
| `RestAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `RestAmountInCompanyCurrency` | `Decimal` | no |  |
| `RestAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `OrderedRestAmount` | `Decimal` | no |  |
| `OrderedRestAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `CurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `ExchangeRate` | `Decimal` | no |  |
| `PaidInFullDate` | `DateTimeOffset?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `ReferenceNumber` | `String` | no |  |
| `UseFixedDueDate` | `Boolean` | no |  |
| `VatGroupId` | `Int64?` | yes | [VatGroups](/modules/Common.md#Common.VatGroup) |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](/modules/Common.md#Common.PaymentTerm) |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](/modules/Common.md#Common.PaymentTerm) |
| `FinalBookingId` | `Int64?` | yes |  |
| `BusinessContactId` | `Int64` | no | [Suppliers](/modules/Purchase.md#Purchase.Supplier) |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](/modules/Common.md#Common.CurrencyExchangeType) |
| `Payments` | `OutgoingPayments[]` | no | [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment) |
| `WithholdTaxAmount` | `Decimal?` | yes |  |
| `WithholdTaxAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `WithholdTaxAmountInCompanyCurrency` | `Decimal?` | yes |  |
| `WithholdTaxAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `InputVatDate` | `DateTimeOffset?` | yes |  |
| `OutputVatDate` | `DateTimeOffset?` | yes |  |

- `InvoiceType` — Standard=1, Interest=4, OnAccount=5, ForOrderingOnAccount=8, CorrectionInvoice=9
- `Status` — Registered=0, Preliminary=1, Final=2, Cancelled=6
- `BlockedStatus` — None=0, Message=1, Blocked=2
- `BlockedContextType` (bitmask) — None=0, Payment=1
- `EimInvoiceStatus` — None=0, Hold=1, ForAuthorization=2, Approved=3, Rejected=4, FinalBooked=5

**References out:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Comments](/modules/Common.md#Common.Comment), [Countries](/modules/Common.md#Common.Country), [Currencies](/modules/Common.md#Common.Currency), [CurrencyExchangeTypes](/modules/Common.md#Common.CurrencyExchangeType), [LanguageCodes](/modules/Common.md#Common.LanguageCode), [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment), [PaymentMethods](/modules/Common.md#Common.PaymentMethod), [PaymentTerms](/modules/Common.md#Common.PaymentTerm), [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [SupplierAccountGroups](/modules/Purchase.md#Purchase.SupplierAccountGroup), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [VatGroups](/modules/Common.md#Common.VatGroup), [Warehouses](/modules/Common.md#Common.Warehouse)
**Referenced by:** [AccountsPayableCashDiscountLevels](/modules/Accounting.md#Accounting.AccountsPayableCashDiscountLevel), [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccrualAccountings](/modules/Accounting.md#Accounting.AccrualAccounting), [CaseEntryPartLinks](/modules/Inventory.md#Inventory.CasePartLink), [EimDocuments](/modules/Purchase.md#Purchase.EimDocument), [FixedAssets](/modules/Accounting.md#Accounting.FixedAsset), [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment), [PurchaseOrderDeliveryRows](/modules/Purchase.md#Purchase.PurchaseOrderDeliveryRow), [PurchaseOrderInvoiceRows](/modules/Purchase.md#Purchase.PurchaseOrderInvoiceRow), [SetOffDestination](/modules/Accounting.md#Accounting.SetOffDestination), [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow), [Vouchers](/modules/Accounting.md#Accounting.Voucher)

<a id="Accounting.AccountsReceivableCashDiscountLevel"></a>
### AccountsReceivableCashDiscountLevels

Represents a cash discount level for an accounts receivable.

- **Endpoint:** `GET /api/v1/Accounting/AccountsReceivableCashDiscountLevels`
- **Required permission:** Show accounts receivable
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no | [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable) |
| `Discount` | `Decimal?` | yes |  |
| `DiscountDate` | `DateTimeOffset?` | yes |  |
| `RowIndex` | `Int32?` | yes |  |

**References out:** [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable)

<a id="Accounting.AccountsReceivable"></a>
### AccountsReceivables

Represents an accounts receivable.

- **Endpoint:** `GET /api/v1/Accounting/AccountsReceivables`
- **Required permission:** Show accounts receivable
- **Introduced in:** 2.44

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Version` | `Int32` | no |  |
| `BookingId` | `Int64?` | yes | [Bookings](/modules/Accounting.md#Accounting.Booking) |
| `Booking` | `Bookings` | no | [Bookings](/modules/Accounting.md#Accounting.Booking) |
| `InvoiceType` | `Int32` | no |  |
| `LatestReminderDate` | `DateTimeOffset?` | yes |  |
| `PaymentReminder` | `Boolean` | no |  |
| `NumberOfPaymentReminders` | `Int32` | no |  |
| `CollectionDate` | `DateTimeOffset?` | yes |  |
| `Collection` | `Boolean` | no |  |
| `InterestType` | `Int32` | no |  |
| `IsComprehensive` | `Boolean` | no |  |
| `PartialInvoiceType` | `Int32` | no |  |
| `CustomerAccountGroupId` | `Int64` | no | [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup) |
| `CustomerAccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup) |
| `DebitInvoiceId` | `Int64?` | yes | [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable) |
| `OnAccountIncomingPaymentLedgerId` | `Int64?` | yes |  |
| `OnAccountCancelledIncomingPaymentLedgerId` | `Int64?` | yes |  |
| `IsEInvoiceExported` | `Boolean` | no |  |
| `AccountsReceivableLedgerId` | `Int64?` | yes |  |
| `CancelledAccountsReceivableLedgerId` | `Int64?` | yes |  |
| `Status` | `Int32` | no |  |
| `LatePaymentFee` | `Decimal?` | yes |  |
| `CancelCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `CancelComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CancelDate` | `DateTimeOffset` | no |  |
| `CancelBookingId` | `Int64?` | yes | [Bookings](/modules/Accounting.md#Accounting.Booking) |
| `CancelBooking` | `Bookings` | no | [Bookings](/modules/Accounting.md#Accounting.Booking) |
| `BusinessContactId` | `Int64?` | yes | [Customers](/modules/Sales.md#Sales.Customer) |
| `InvoiceNumber` | `Int64` | no |  |
| `InvoiceDate` | `DateTimeOffset` | no |  |
| `DueDate` | `DateTimeOffset` | no |  |
| `IsCredit` | `Boolean` | no |  |
| `InvoiceAmount` | `Decimal` | no |  |
| `InvoiceAmountCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `InvoiceAmountInCompanyCurrency` | `Decimal` | no |  |
| `InvoiceAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `VatAmount` | `Decimal` | no |  |
| `VatAmountCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `VatAmountInCompanyCurrency` | `Decimal` | no |  |
| `VatAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `RestAmount` | `Decimal` | no |  |
| `RestAmountCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `RestAmountInCompanyCurrency` | `Decimal` | no |  |
| `RestAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `OrderedRestAmount` | `Decimal` | no |  |
| `OrderedRestAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `CurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `ExchangeRate` | `Decimal` | no |  |
| `PaidInFullDate` | `DateTimeOffset?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `ReferenceNumber` | `String` | no |  |
| `UseFixedDueDate` | `Boolean` | no |  |
| `VatGroupId` | `Int64` | no | [VatGroups](/modules/Common.md#Common.VatGroup) |
| `PaymentTermId` | `Int64` | no | [PaymentTerms](/modules/Common.md#Common.PaymentTerm) |
| `ChineseVatInvoiceNumber` | `String` | no |  |
| `ChineseVatInvoiceDate` | `DateTimeOffset?` | yes |  |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](/modules/Common.md#Common.CurrencyExchangeType) |
| `CTCReportingInvoiceNumber` | `String` | no |  |
| `CTCReportingReasonForRejection` | `String` | no |  |
| `CTCReportingStatus` | `Int32?` | yes |  |
| `CTCReportingInvoiceDate` | `DateTimeOffset?` | yes |  |
| `CTCReportingIdentifier` | `String` | no |  |
| `CTCReportingElectronicConfirmationURL` | `String` | no |  |
| `CTCReportingElectronicConfirmationNumber` | `String` | no |  |

- `InvoiceType` — Standard=1, Internal=2, CashReceipt=3, Interest=4, OnAccount=5, DebitNote=6, ServiceTax=7, CorrectionInvoice=8, CollectiveCorrectionInvoice=9
- `InterestType` — InterestInvoice=0, NextRegularInvoice=1, None=2
- `PartialInvoiceType` — NotInitialized=0, InAdvance=1, Delivery=2, InArrears=3, Text=4
- `Status` — Approved=0, Printed=1, Cancelled=2
- `CTCReportingStatus` — NotSent=0, SentForApproval=1, Approved=2, NotApproved=3, Cancelled=4

**References out:** [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [Bookings](/modules/Accounting.md#Accounting.Booking), [Comments](/modules/Common.md#Common.Comment), [Currencies](/modules/Common.md#Common.Currency), [CurrencyExchangeTypes](/modules/Common.md#Common.CurrencyExchangeType), [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup), [Customers](/modules/Sales.md#Sales.Customer), [PaymentTerms](/modules/Common.md#Common.PaymentTerm), [VatGroups](/modules/Common.md#Common.VatGroup)
**Referenced by:** [AccountsReceivableCashDiscountLevels](/modules/Accounting.md#Accounting.AccountsReceivableCashDiscountLevel), [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [CaseEntry](/modules/Inventory.md#Inventory.CaseEntry), [CaseEntryPartLinks](/modules/Inventory.md#Inventory.CasePartLink), [FixedAssetSales](/modules/Accounting.md#Accounting.FixedAssetSale), [IncomingPayments](/modules/Accounting.md#Accounting.IncomingPayment), [InvoiceLogs](/modules/Sales.md#Sales.InvoiceLog), [SetOffDestination](/modules/Accounting.md#Accounting.SetOffDestination), [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow)

<a id="Accounting.AccountYearSettingCodingDimensionAvailability"></a>
### AccountYearSettingCodingDimensionAvailabilities

Represents a coding dimension available on a account for a specific year setting.

- **Endpoint:** `GET /api/v1/Accounting/AccountYearSettingCodingDimensionAvailabilities`
- **Required permission:** Show accounting year
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](/modules/Accounting.md#Accounting.CodingDimension) |
| `CodingDimension` | `CodingDimensions` | no | [CodingDimensions](/modules/Accounting.md#Accounting.CodingDimension) |
| `CodingDimensionAvailability` | `Int32` | no |  |
| `AccountYearSettingId` | `Int64` | no | [AccountYearSettings](/modules/Accounting.md#Accounting.AccountYearSetting) |

- `CodingDimensionAvailability` — NotAllowed=0, Allowed=1, Mandatory=2

**References out:** [AccountYearSettings](/modules/Accounting.md#Accounting.AccountYearSetting), [CodingDimensions](/modules/Accounting.md#Accounting.CodingDimension)
**Referenced by:** [AccountYearSettings](/modules/Accounting.md#Accounting.AccountYearSetting)

<a id="Accounting.AccountYearSetting"></a>
### AccountYearSettings

Represents a account setting on a specific year.

- **Endpoint:** `GET /api/v1/Accounting/AccountYearSettings`
- **Required permission:** Show accounting year
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountingYearId` | `Int64` | no | [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear) |
| `Description` | `String` | no |  |
| `AllowSpecification` | `Boolean` | no |  |
| `AllowQuantity` | `Boolean` | no |  |
| `IsCurrencyAccount` | `Boolean` | no |  |
| `CurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `IsAccrual` | `Boolean` | no |  |
| `DebitOrCreditType` | `Int32` | no |  |
| `VatType` | `Int32` | no |  |
| `VatRateId` | `Int64?` | yes | [VatRates](/modules/Common.md#Common.VatRate) |
| `BlockedForManualCoding` | `Boolean` | no |  |
| `IsFixedAssetAccount` | `Boolean` | no |  |
| `IncludeOrderNumberInCoding` | `Boolean` | no |  |
| `AccountId` | `Int64` | no | [Accounts](/modules/Accounting.md#Accounting.Account) |
| `Account` | `Accounts` | no | [Accounts](/modules/Accounting.md#Accounting.Account) |
| `AccountCodingDimensions` | `AccountYearSettingCodingDimensionAvailabilities[]` | no | [AccountYearSettingCodingDimensionAvailabilities](/modules/Accounting.md#Accounting.AccountYearSettingCodingDimensionAvailability) |

- `DebitOrCreditType` — Debit=0, Credit=1
- `VatType` — None=0, Sales=1, Purchase=2, InputVat=3, OutputVat=4

**References out:** [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear), [Accounts](/modules/Accounting.md#Accounting.Account), [AccountYearSettingCodingDimensionAvailabilities](/modules/Accounting.md#Accounting.AccountYearSettingCodingDimensionAvailability), [Currencies](/modules/Common.md#Common.Currency), [VatRates](/modules/Common.md#Common.VatRate)
**Referenced by:** [AccountingBudgets](/modules/Accounting.md#Accounting.AccountingBudget), [AccountYearSettingCodingDimensionAvailabilities](/modules/Accounting.md#Accounting.AccountYearSettingCodingDimensionAvailability)

<a id="Accounting.AccrualAccountingLedger"></a>
### AccrualAccountingLedgers

Represents a accrual accounting ledger.

- **Endpoint:** `GET /api/v1/Accounting/AccrualAccountingLedgers`
- **Required permission:** Show accrual
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `ApprovedDate` | `DateTimeOffset?` | yes |  |

**Referenced by:** [AccrualAccountingRows](/modules/Accounting.md#Accounting.AccrualAccountingRow)

<a id="Accounting.AccrualAccountingRow"></a>
### AccrualAccountingRows

Represents a accrual accounting row.

- **Endpoint:** `GET /api/v1/Accounting/AccrualAccountingRows`
- **Required permission:** Show accrual
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PeriodId` | `Int64` | no | [AccountingYearPeriods](/modules/Accounting.md#Accounting.AccountingYearPeriod) |
| `Period` | `AccountingYearPeriods` | no | [AccountingYearPeriods](/modules/Accounting.md#Accounting.AccountingYearPeriod) |
| `PeriodAmountInCompanyCurrency` | `Decimal` | no |  |
| `AccrualAccountingId` | `Int64` | no |  |
| `IsReleased` | `Boolean` | no |  |
| `LedgerId` | `Int64?` | yes | [AccrualAccountingLedgers](/modules/Accounting.md#Accounting.AccrualAccountingLedger) |
| `Ledger` | `AccrualAccountingLedgers` | no | [AccrualAccountingLedgers](/modules/Accounting.md#Accounting.AccrualAccountingLedger) |
| `BookingId` | `Int64?` | yes |  |
| `RowIndex` | `Int32` | no |  |
| `BookingRows` | `BookingRows[]` | no | [BookingRows](/modules/Accounting.md#Accounting.BookingRow) |

**References out:** [AccountingYearPeriods](/modules/Accounting.md#Accounting.AccountingYearPeriod), [AccrualAccountingLedgers](/modules/Accounting.md#Accounting.AccrualAccountingLedger), [BookingRows](/modules/Accounting.md#Accounting.BookingRow)
**Referenced by:** [AccrualAccountings](/modules/Accounting.md#Accounting.AccrualAccounting), [Vouchers](/modules/Accounting.md#Accounting.Voucher)

<a id="Accounting.AccrualAccounting"></a>
### AccrualAccountings

Represents a accrual accounting.

- **Endpoint:** `GET /api/v1/Accounting/AccrualAccountings`
- **Required permission:** Show accrual
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `Text` | `String` | no |  |
| `Type` | `Int32` | no |  |
| `StartDate` | `DateTimeOffset?` | yes |  |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable) |
| `AccountsPayableBookingRowId` | `Int64?` | yes |  |
| `VoucherId` | `Int64?` | yes |  |
| `VoucherRowId` | `Int64?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `CancelCommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `CancelComment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `IsCancelled` | `Boolean` | no |  |
| `BookingId` | `Int64` | no |  |
| `Rows` | `AccrualAccountingRows[]` | no | [AccrualAccountingRows](/modules/Accounting.md#Accounting.AccrualAccountingRow) |
| `BookingRows` | `BookingRows[]` | no | [BookingRows](/modules/Accounting.md#Accounting.BookingRow) |
| `AccountsPayableBookingRow` | `BookingRows` | no | [BookingRows](/modules/Accounting.md#Accounting.BookingRow) |

- `Type` — AccountsPayableBookingRow=1, VoucherRow=2, ReverseVoucher=3, FreeBooking=4, SalesAgreement=5, SupplierAgreement=6

**References out:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccrualAccountingRows](/modules/Accounting.md#Accounting.AccrualAccountingRow), [BookingRows](/modules/Accounting.md#Accounting.BookingRow), [Comments](/modules/Common.md#Common.Comment)
**Referenced by:** [BookingRows](/modules/Accounting.md#Accounting.BookingRow), [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow)

<a id="Accounting.AllocationKeyResultRow"></a>
### AllocationKeyResultRows

Represent an allocation key result row.

- **Endpoint:** `GET /api/v1/Accounting/AllocationKeyResultRows`
- **Required permission:** Show allocation keys
- **Introduced in:** 24.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AllocationKeyId` | `Int64` | no | [AllocationKeys](/modules/Accounting.md#Accounting.AllocationKey) |
| `CodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `Percentage` | `Decimal` | no |  |
| `RowIndex` | `Int32` | no |  |

**References out:** [AllocationKeys](/modules/Accounting.md#Accounting.AllocationKey), [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry)
**Referenced by:** [AllocationKeys](/modules/Accounting.md#Accounting.AllocationKey)

<a id="Accounting.AllocationKey"></a>
### AllocationKeys

Represent an allocation key.

- **Endpoint:** `GET /api/v1/Accounting/AllocationKeys`
- **Required permission:** Show allocation keys
- **Introduced in:** 24.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int64` | no |  |
| `Name` | `String` | no |  |
| `AllocationKeyResultRow` | `AllocationKeyResultRows[]` | no | [AllocationKeyResultRows](/modules/Accounting.md#Accounting.AllocationKeyResultRow) |

**References out:** [AllocationKeyResultRows](/modules/Accounting.md#Accounting.AllocationKeyResultRow)
**Referenced by:** [AllocationKeyResultRows](/modules/Accounting.md#Accounting.AllocationKeyResultRow), [AutoAllocations](/modules/Accounting.md#Accounting.AutoAllocation)

<a id="Accounting.AutoAllocation"></a>
### AutoAllocations

Represent an auto allocation.

- **Endpoint:** `GET /api/v1/Accounting/AutoAllocations`
- **Required permission:** Show automatic allocations
- **Introduced in:** 24.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `String` | no |  |
| `Description` | `String` | no |  |
| `Type` | `Int32` | no |  |
| `Active` | `Boolean` | no |  |
| `AllocationKeyId` | `Int64?` | yes | [AllocationKeys](/modules/Accounting.md#Accounting.AllocationKey) |
| `AllocationKey` | `AllocationKeys` | no | [AllocationKeys](/modules/Accounting.md#Accounting.AllocationKey) |
| `AccountFrom` | `String` | no |  |
| `AccountTo` | `String` | no |  |

- `Type` — Direct=0, PeriodBalance=1, AccumulatedBalance=2

**References out:** [AllocationKeys](/modules/Accounting.md#Accounting.AllocationKey)

<a id="Accounting.BalanceRowDay"></a>
### BalanceRowDays

Represents a balance row day.

- **Endpoint:** `GET /api/v1/Accounting/BalanceRowDays`
- **Required permission:** Show balance information
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `BalanceId` | `Int64` | no | [Balances](/modules/Accounting.md#Accounting.Balance) |
| `Credit` | `Decimal` | no |  |
| `CreditInCompanyCurrency` | `Decimal` | no |  |
| `Date` | `DateTimeOffset` | no |  |
| `Debit` | `Decimal` | no |  |
| `DebitInCompanyCurrency` | `Decimal` | no |  |
| `PeriodNumber` | `Int32` | no |  |
| `Quantity` | `Decimal` | no |  |

**References out:** [Balances](/modules/Accounting.md#Accounting.Balance)

<a id="Accounting.Balance"></a>
### Balances

Represents a balance.

- **Endpoint:** `GET /api/v1/Accounting/Balances`
- **Required permission:** Show balance information
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountingYearId` | `Int64` | no | [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear) |
| `Amount` | `Decimal` | no |  |
| `AmountInCompanyCurrency` | `Decimal` | no |  |
| `CodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `OpeningBalanceId` | `Int64?` | yes | [OpeningBalances](/modules/Accounting.md#Accounting.OpeningBalance) |
| `Quantity` | `Decimal` | no |  |

**References out:** [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear), [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry), [OpeningBalances](/modules/Accounting.md#Accounting.OpeningBalance)
**Referenced by:** [AccountingBudgets](/modules/Accounting.md#Accounting.AccountingBudget), [BalanceRowDays](/modules/Accounting.md#Accounting.BalanceRowDay), [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow)

<a id="Accounting.BankAccount"></a>
### BankAccounts

Represents a bank account.

- **Endpoint:** `GET /api/v1/Accounting/BankAccounts`
- **Required permission:** Show bank settings
- **Introduced in:** 24.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `Type` | `Int32` | no |  |
| `Number` | `String` | no |  |
| `BgNumber` | `String` | no |  |
| `PgNumber` | `String` | no |  |
| `BankIdentifierCode` | `String` | no |  |
| `CurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `AccountingAccountId` | `Int64` | no | [Accounts](/modules/Accounting.md#Accounting.Account) |
| `BankAddressId` | `Int64` | no | [Addresses](/modules/Common.md#Common.Address) |

- `Type` — Iban=1, Bban=2, Upic=3, Miscellaneous=4

**References out:** [Accounts](/modules/Accounting.md#Accounting.Account), [Addresses](/modules/Common.md#Common.Address), [Currencies](/modules/Common.md#Common.Currency)
**Referenced by:** [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment)

<a id="Accounting.BookingRow"></a>
### BookingRows

Represents a booking row.

- **Endpoint:** `GET /api/v1/Accounting/BookingRows`
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Type` | `Int32` | no |  |
| `AuthorizedWhen` | `DateTimeOffset?` | yes |  |
| `PurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](/modules/Purchase.md#Purchase.PurchaseOrderDeliveryRow) |
| `BookingId` | `Int64` | no | [Bookings](/modules/Accounting.md#Accounting.Booking) |
| `VatRateId` | `Int64?` | yes | [VatRates](/modules/Common.md#Common.VatRate) |
| `AccrualAccountingId` | `Int64?` | yes | [AccrualAccountings](/modules/Accounting.md#Accounting.AccrualAccounting) |
| `OrderNumber` | `String` | no |  |
| `DebitInCompanyCurrency` | `Decimal` | no |  |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `CreditInCompanyCurrency` | `Decimal` | no |  |
| `CreditInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `Debit` | `Decimal` | no |  |
| `DebitCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `Credit` | `Decimal` | no |  |
| `CreditCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `Quantity` | `Decimal` | no |  |
| `RowIndex` | `Int32` | no |  |
| `CodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `NetAmountBookingRowId` | `Int64?` | yes | [BookingRows](/modules/Accounting.md#Accounting.BookingRow) |

- `Type` — NotInitialized=0, AccountsReceivable=1, OutputVat=2, AccountsPayable=3, PreliminaryAccountsPayable=4, PaymentIn=5, PaymentOut=6, Purchase=7, Sales=8, Miscellaneous=9, PurchaseWithoutOrder=10, InvoicingCharges=11, InsuranceCost=12, RoundOff=13, SetupPrice=14, Material=15, Inventory=16, PreliminaryAccount=17, InputVat=18, ExchangeRateAdjustment=19, InvoiceReminderFee=20, PriceDifference=21, PaymentInVat=22, PaymentOutVat=23, OtherPayment=24, InputVatNonDeductible=25, CurrencyDifference=26, WithholdingTax=27, ManualAccountsPayableFinalBookingFromG4=999

**References out:** [AccrualAccountings](/modules/Accounting.md#Accounting.AccrualAccounting), [BookingRows](/modules/Accounting.md#Accounting.BookingRow), [Bookings](/modules/Accounting.md#Accounting.Booking), [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry), [Currencies](/modules/Common.md#Common.Currency), [PurchaseOrderDeliveryRows](/modules/Purchase.md#Purchase.PurchaseOrderDeliveryRow), [VatRates](/modules/Common.md#Common.VatRate)
**Referenced by:** [AccrualAccountingRows](/modules/Accounting.md#Accounting.AccrualAccountingRow), [AccrualAccountings](/modules/Accounting.md#Accounting.AccrualAccounting), [BookingRows](/modules/Accounting.md#Accounting.BookingRow), [Bookings](/modules/Accounting.md#Accounting.Booking)

<a id="Accounting.Booking"></a>
### Bookings

Represents a booking.

- **Endpoint:** `GET /api/v1/Accounting/Bookings`
- **Introduced in:** 2.44

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentClass` | `Guid` | no |  |
| `ParentId` | `Int64` | no |  |
| `Rows` | `BookingRows[]` | no | [BookingRows](/modules/Accounting.md#Accounting.BookingRow) |

**References out:** [BookingRows](/modules/Accounting.md#Accounting.BookingRow)
**Referenced by:** [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [BookingRows](/modules/Accounting.md#Accounting.BookingRow), [FixedAssetSales](/modules/Accounting.md#Accounting.FixedAssetSale), [IncomingPayments](/modules/Accounting.md#Accounting.IncomingPayment), [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment)

<a id="Accounting.BudgetChart"></a>
### BudgetCharts

Represents a budget chart.

- **Endpoint:** `GET /api/v1/Accounting/BudgetCharts`
- **Required permission:** Show basic data for budget
- **Introduced in:** 23.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [AccountingBudgets](/modules/Accounting.md#Accounting.AccountingBudget)

<a id="Accounting.CodingDimension"></a>
### CodingDimensions

Represents a Coding dimension.

- **Endpoint:** `GET /api/v1/Accounting/CodingDimensions`
- **Required permission:** Show dimensions/dimension codes
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Number` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `CodeDescription` | `String` | no |  |
| `ReferenceEntityType` | `Int32` | no |  |
| `CodingElements` | `CodingElements[]` | no | [CodingElements](/modules/Accounting.md#Accounting.CodingElement) |

- `ReferenceEntityType` — None=0, Project=1, ProductGroup=2, PartCode=3, Part=4, Department=5, WorkCenter=6, CustomerRootFromOrder=7, CustomerRootFromInvoice=8, SupplierRoot=9, Person=10, CustomerAccountGroupOnCustomer=11, CustomerDistrict=12, CustomerType=13, SupplierAccountGroupOnSupplier=14, SupplierDistrict=15, SupplierType=16

**References out:** [CodingElements](/modules/Accounting.md#Accounting.CodingElement)
**Referenced by:** [AccountYearSettingCodingDimensionAvailabilities](/modules/Accounting.md#Accounting.AccountYearSettingCodingDimensionAvailability), [CodingElements](/modules/Accounting.md#Accounting.CodingElement), [CodingEntryElements](/modules/Accounting.md#Accounting.CodingEntryElement)

<a id="Accounting.CodingElement"></a>
### CodingElements

Represents a Coding element.

- **Endpoint:** `GET /api/v1/Accounting/CodingElements`
- **Required permission:** Show dimensions/dimension codes
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](/modules/Accounting.md#Accounting.CodingDimension) |
| `IsActive` | `Boolean` | no |  |

**References out:** [CodingDimensions](/modules/Accounting.md#Accounting.CodingDimension)
**Referenced by:** [CodingDimensions](/modules/Accounting.md#Accounting.CodingDimension), [CodingEntryElements](/modules/Accounting.md#Accounting.CodingEntryElement)

<a id="Accounting.CodingEntry"></a>
### CodingEntries

Represents a coding entry.

- **Endpoint:** `GET /api/v1/Accounting/CodingEntries`
- **Required permission:** Show dimensions/dimension codes
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CodingEntryDescription` | `String` | no |  |
| `AccountId` | `Int64?` | yes | [Accounts](/modules/Accounting.md#Accounting.Account) |
| `Account` | `Accounts` | no | [Accounts](/modules/Accounting.md#Accounting.Account) |
| `CodingEntryElements` | `CodingEntryElements[]` | no | [CodingEntryElements](/modules/Accounting.md#Accounting.CodingEntryElement) |

**References out:** [Accounts](/modules/Accounting.md#Accounting.Account), [CodingEntryElements](/modules/Accounting.md#Accounting.CodingEntryElement)
**Referenced by:** [AccountingBudgets](/modules/Accounting.md#Accounting.AccountingBudget), [AllocationKeyResultRows](/modules/Accounting.md#Accounting.AllocationKeyResultRow), [Balances](/modules/Accounting.md#Accounting.Balance), [BookingRows](/modules/Accounting.md#Accounting.BookingRow), [CodingEntryElements](/modules/Accounting.md#Accounting.CodingEntryElement), [CodingRows](/modules/Accounting.md#Accounting.CodingRow), [CustomerOrderPaymentPlanRows](/modules/Sales.md#Sales.CustomerOrderPaymentPlanRow), [OpeningBalances](/modules/Accounting.md#Accounting.OpeningBalance), [PaymentMethods](/modules/Common.md#Common.PaymentMethod), [PurchaseOrderInvoiceRows](/modules/Purchase.md#Purchase.PurchaseOrderInvoiceRow), [StandardAccounts](/modules/Accounting.md#Accounting.StandardAccount), [SupplierAccounts](/modules/Purchase.md#Purchase.SupplierAccount), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow), [WriteOffCodes](/modules/Common.md#Common.WriteOffCode)

<a id="Accounting.CodingEntryElement"></a>
### CodingEntryElements

Represents a coding entry element.

- **Endpoint:** `GET /api/v1/Accounting/CodingEntryElements`
- **Required permission:** Show dimensions/dimension codes
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](/modules/Accounting.md#Accounting.CodingDimension) |
| `CodingDimension` | `CodingDimensions` | no | [CodingDimensions](/modules/Accounting.md#Accounting.CodingDimension) |
| `ReferencingEntityId` | `Int64?` | yes | [CodingElements](/modules/Accounting.md#Accounting.CodingElement) |

**References out:** [CodingDimensions](/modules/Accounting.md#Accounting.CodingDimension), [CodingElements](/modules/Accounting.md#Accounting.CodingElement), [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry)
**Referenced by:** [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry)

<a id="Accounting.CodingRow"></a>
### CodingRows

Represents a coding row.

- **Endpoint:** `GET /api/v1/Accounting/CodingRows`
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `Type` | `Int32` | no |  |

- `Type` — Standard=1, Setup=2, Material=3, Inventory=4, PriceDifference=5, Cost=6

**References out:** [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry)
**Referenced by:** [Codings](/modules/Accounting.md#Accounting.Coding)

<a id="Accounting.Coding"></a>
### Codings

Represents a coding.

- **Endpoint:** `GET /api/v1/Accounting/Codings`
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CodingRows` | `CodingRows[]` | no | [CodingRows](/modules/Accounting.md#Accounting.CodingRow) |

**References out:** [CodingRows](/modules/Accounting.md#Accounting.CodingRow)
**Referenced by:** [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [InquiryRows](/modules/Purchase.md#Purchase.InquiryRow), [PurchaseOrderInvoiceRows](/modules/Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](/modules/Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](/modules/Sales.md#Sales.QuoteRow), [SalesAgreementRows](/modules/Sales.md#Sales.SalesAgreementRow)

<a id="Accounting.FixedAssetDepreciation"></a>
### FixedAssetDepreciations

Represents a depreciation for a fixed assets object.

- **Endpoint:** `GET /api/v1/Accounting/FixedAssetDepreciations`
- **Required permission:** Show depreciation
- **Introduced in:** 23.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Amount` | `Decimal` | no |  |
| `DepreciationDate` | `DateTimeOffset` | no |  |
| `VoucherDate` | `DateTimeOffset` | no |  |
| `VoucherText` | `String` | no |  |
| `ParentId` | `Int64` | no | [FixedAssets](/modules/Accounting.md#Accounting.FixedAsset) |

**References out:** [FixedAssets](/modules/Accounting.md#Accounting.FixedAsset)

<a id="Accounting.FixedAssetGroup"></a>
### FixedAssetGroups

Represents a fixed assets group.

- **Endpoint:** `GET /api/v1/Accounting/FixedAssetGroups`
- **Required permission:** Show basic data for fixed assets register
- **Introduced in:** 23.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |

**Referenced by:** [FixedAssets](/modules/Accounting.md#Accounting.FixedAsset)

<a id="Accounting.FixedAsset"></a>
### FixedAssets

Represents a fixed assets object.

- **Endpoint:** `GET /api/v1/Accounting/FixedAssets`
- **Required permission:** Show fixed assets objects
- **Introduced in:** 23.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `GroupId` | `Int64` | no | [FixedAssetGroups](/modules/Accounting.md#Accounting.FixedAssetGroup) |
| `Group` | `FixedAssetGroups` | no | [FixedAssetGroups](/modules/Accounting.md#Accounting.FixedAssetGroup) |
| `AcquisitionDate` | `DateTimeOffset` | no |  |
| `AcquisitionValue` | `Decimal` | no |  |
| `Quantity` | `Decimal` | no |  |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable) |
| `VoucherId` | `Int64?` | yes | [Vouchers](/modules/Accounting.md#Accounting.Voucher) |
| `SupplierId` | `Int64?` | yes | [Suppliers](/modules/Purchase.md#Purchase.Supplier) |
| `CategoryString` | `String` | no |  |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |
| `DepartmentId` | `Int64?` | yes | [Departments](/modules/Common.md#Common.Department) |
| `SerialNumber` | `String` | no |  |
| `Location` | `String` | no |  |
| `PlannedDepreciationStartDate` | `DateTimeOffset` | no |  |
| `PlannedDepreciationTimeInYears` | `Decimal` | no |  |
| `PlannedDepreciationPercentage` | `Decimal` | no |  |
| `CalculatedDepreciationStartDate` | `DateTimeOffset` | no |  |
| `CalculatedDepreciationPercentage` | `Decimal` | no |  |
| `MinimumValue` | `Decimal` | no |  |
| `Sales` | `FixedAssetSales[]` | no | [FixedAssetSales](/modules/Accounting.md#Accounting.FixedAssetSale) |

**References out:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [Departments](/modules/Common.md#Common.Department), [FixedAssetGroups](/modules/Accounting.md#Accounting.FixedAssetGroup), [FixedAssetSales](/modules/Accounting.md#Accounting.FixedAssetSale), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [Vouchers](/modules/Accounting.md#Accounting.Voucher), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [CustomerOrderRows](/modules/Sales.md#Sales.CustomerOrderRow), [FixedAssetDepreciations](/modules/Accounting.md#Accounting.FixedAssetDepreciation)

<a id="Accounting.FixedAssetSale"></a>
### FixedAssetSales

Represents a sale/retirement of a fixed assets object.

- **Endpoint:** `GET /api/v1/Accounting/FixedAssetSales`
- **Required permission:** Show fixed assets objects
- **Introduced in:** 23.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `SalesDate` | `DateTimeOffset` | no |  |
| `Type` | `Int32` | no |  |
| `Quantity` | `Decimal` | no |  |
| `PartOfAcquisitionValue` | `Decimal` | no |  |
| `SalesValue` | `Decimal` | no |  |
| `SalesProfit` | `Decimal?` | yes |  |
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable) |
| `CustomerId` | `Int64?` | yes | [Customers](/modules/Sales.md#Sales.Customer) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `VoucherText` | `String` | no |  |
| `SalesTimestamp` | `DateTimeOffset` | no |  |
| `BookingId` | `Int64?` | yes | [Bookings](/modules/Accounting.md#Accounting.Booking) |

- `Type` — Sale=0, Retirement=1

**References out:** [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [Bookings](/modules/Accounting.md#Accounting.Booking), [Comments](/modules/Common.md#Common.Comment), [Customers](/modules/Sales.md#Sales.Customer)
**Referenced by:** [FixedAssets](/modules/Accounting.md#Accounting.FixedAsset)

<a id="Accounting.IncomingPayment"></a>
### IncomingPayments

Represents an incoming payment.

- **Endpoint:** `GET /api/v1/Accounting/IncomingPayments`
- **Required permission:** Show accounts receivable
- **Introduced in:** 22.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `BankChargeAmount` | `Decimal?` | yes |  |
| `BankChargeAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `BookingId` | `Int64?` | yes | [Bookings](/modules/Accounting.md#Accounting.Booking) |
| `CancelDate` | `DateTimeOffset?` | yes |  |
| `CancelTimeStamp` | `DateTimeOffset?` | yes |  |
| `CancelledByUserId` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `CancelPaymentDate` | `DateTimeOffset` | no |  |
| `CreationDate` | `DateTimeOffset` | no |  |
| `CurrencyExchangeRate` | `Decimal` | no |  |
| `InterestType` | `Int32` | no |  |
| `IsCancelled` | `Boolean` | no |  |
| `PaidAmount` | `Decimal` | no |  |
| `PaidAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `PaidAmountInCompanyCurrency` | `Decimal` | no |  |
| `PaidAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `PaidVatAmount` | `Decimal?` | yes |  |
| `PaidVatAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `ParentId` | `Int64` | no | [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable) |
| `PaymentDate` | `DateTimeOffset` | no |  |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](/modules/Common.md#Common.PaymentMethod) |
| `VoucherText` | `String` | no |  |
| `WriteOffAmount` | `Decimal?` | yes |  |
| `WriteOffAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `WriteOffAmountInCompanyCurrency` | `Decimal?` | yes |  |
| `WriteOffAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](/modules/Common.md#Common.WriteOffCode) |
| `InterestInvoicingStatus` | `Int32` | no |  |
| `IsSetOffPayment` | `Boolean` | no |  |
| `LedgerId` | `Int64?` | yes |  |
| `ChequeNumber` | `String` | no |  |

- `InterestType` — InterestInvoice=0, NextRegularInvoice=1, None=2
- `InterestInvoicingStatus` — NoInterest=0, Interest=1, InterestInvoiced=9

**References out:** [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Bookings](/modules/Accounting.md#Accounting.Booking), [Currencies](/modules/Common.md#Common.Currency), [PaymentMethods](/modules/Common.md#Common.PaymentMethod), [WriteOffCodes](/modules/Common.md#Common.WriteOffCode)
**Referenced by:** [OutgoingPayments](/modules/Accounting.md#Accounting.OutgoingPayment)

<a id="Accounting.OpeningBalance"></a>
### OpeningBalances

Represents an opening balance.

- **Endpoint:** `GET /api/v1/Accounting/OpeningBalances`
- **Required permission:** Show opening balance
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountingYearId` | `Int64` | no | [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear) |
| `CodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `Credit` | `Decimal` | no |  |
| `CreditCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `CreditInCompanyCurrency` | `Decimal` | no |  |
| `CreditInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `Debit` | `Decimal` | no |  |
| `DebitCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `DebitInCompanyCurrency` | `Decimal` | no |  |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `ExchangeRate` | `Decimal` | no |  |
| `Quantity` | `Decimal` | no |  |

**References out:** [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear), [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry), [Currencies](/modules/Common.md#Common.Currency)
**Referenced by:** [Balances](/modules/Accounting.md#Accounting.Balance)

<a id="Accounting.OutgoingPayment"></a>
### OutgoingPayments

Represents an outgoing payment.

- **Endpoint:** `GET /api/v1/Accounting/OutgoingPayments`
- **Required permission:** Show accounts payable
- **Introduced in:** 24.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountsPayableId` | `Int64` | no | [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable) |
| `SupplierId` | `Int64` | no | [Suppliers](/modules/Purchase.md#Purchase.Supplier) |
| `CreationDate` | `DateTimeOffset` | no |  |
| `PaymentDate` | `DateTimeOffset` | no |  |
| `PaymentMethodId` | `Int64` | no | [PaymentMethods](/modules/Common.md#Common.PaymentMethod) |
| `PaidAmount` | `Decimal` | no |  |
| `PaidAmountCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `PaidAmountInCompanyCurrency` | `Decimal` | no |  |
| `PaidAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `PaidVatAmount` | `Decimal?` | yes |  |
| `PaidVatAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `BankChargeAmount` | `Decimal?` | yes |  |
| `BankChargeAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `IsOrdered` | `Boolean` | no |  |
| `IsCancelled` | `Boolean` | no |  |
| `CancelledByUserId` | `Int64?` | yes | [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) |
| `CancelDate` | `DateTimeOffset?` | yes |  |
| `CancelTimeStamp` | `DateTimeOffset?` | yes |  |
| `ReceivingBankAccountId` | `Int64?` | yes | [BusinessContactBankAccounts](/modules/Common.md#Common.BusinessContactBankAccount) |
| `SendingBankAccountId` | `Int64?` | yes | [BankAccounts](/modules/Accounting.md#Accounting.BankAccount) |
| `SetOffIncomingPaymentId` | `Int64?` | yes | [IncomingPayments](/modules/Accounting.md#Accounting.IncomingPayment) |
| `BookingId` | `Int64?` | yes | [Bookings](/modules/Accounting.md#Accounting.Booking) |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](/modules/Common.md#Common.WriteOffCode) |
| `WriteOffAmount` | `Decimal?` | yes |  |
| `WriteOffAmountCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `WriteOffAmountInCompanyCurrency` | `Decimal?` | yes |  |
| `WriteOffAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `BundleNumber` | `Int64` | no |  |
| `ChequeNumber` | `String` | no |  |
| `CurrencyExchangeRate` | `Decimal` | no |  |
| `VoucherText` | `String` | no |  |

**References out:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [BankAccounts](/modules/Accounting.md#Accounting.BankAccount), [Bookings](/modules/Accounting.md#Accounting.Booking), [BusinessContactBankAccounts](/modules/Common.md#Common.BusinessContactBankAccount), [Currencies](/modules/Common.md#Common.Currency), [IncomingPayments](/modules/Accounting.md#Accounting.IncomingPayment), [PaymentMethods](/modules/Common.md#Common.PaymentMethod), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [WriteOffCodes](/modules/Common.md#Common.WriteOffCode)
**Referenced by:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable)

<a id="Accounting.StandardAccount"></a>
### StandardAccounts

Represents a standard account.

- **Endpoint:** `GET /api/v1/Accounting/StandardAccounts`
- **Required permission:** Show chart of accounts
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountType` | `Int32` | no |  |
| `Version` | `Int32` | no |  |
| `CodingEntryId` | `Int64?` | yes | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `StandardAccountCategory` | `Int32` | no |  |

- `AccountType` — NotInitialized=0, AccountsReceivable=1, AccountsPayable=2, InvoicingCharges=3, RoundOff=6, CustomerDiscounts=10, BadDebtLoss=11, ExchangeProfitAccountsReceivable=16, BankCharge=17, SupplierDiscounts=18, AccountsPayableWriteOffs=19, PreliminaryAccount=20, InsuranceCost=21, PreliminaryAccountsPayable=22, ReminderFee=23, RoundOffVat=27, VatClearingAccountToPay=28, ExchangeLossAccountsReceivable=32, ExchangeProfitAccountsPayable=33, ExchangeLossAccountsPayable=34, TransitionAccountFixedAssetSales=35, SuspenseAccountDuringPosteriorCoding=40, DebitAccountForInternalInvoices=43, AdditionalPartRowPurchase=50, AdditionalPartRowSales=51, PenaltyInterestExpenseForAccountsPayable=55, PaidAdvanceCustomer=63, UnrealizedExchangeProfitSales=96, UnrealizedExchangeLossSales=97, UnrealizedExchangeProfitPurchase=98, UnrealizedExchangeLossPurchase=99, OnAccountPurchase=101, ExchangeProfitOnPriceDifference=102, ExchangeLossOnPriceDifference=103, RoundOffPurchase=104, VatClearingAccountToReceive=105, OverDepreciations=106, AccountForRevaluationSales=124, AccountForRevaluationPurchase=125, PreliminaryAccrualAccountSuspendedVatForSalesAgreement=126, RecognizedIncomeNotInvoiced=135, RecognizedIncomeConsecutivePrice=136, RecognizedIncomeFixedPrice=137, AnticipatedLossIncomeFixedPrice=140, ReduceOfIncomeAnticipatedLoss=141, OffsetAccountForAdvancesBookedOnBalanceAccount=150, OnAccountSales=151, AccrualAccountForAgreements=152, ProjectMaterialCostCalculationWriteUp=153, ProjectMaterialCostCalculationOffset=154, FactoringFees=155, FactoringRecource=156, FactoringLoss=157, PaidInvoicesFromCustomer=158, AccrualAccountForSupplierAgreements=159
- `StandardAccountCategory` — Sales=1, Purchase=2, Accounting=3

**References out:** [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry)
**Referenced by:** [SupplierAccounts](/modules/Purchase.md#Purchase.SupplierAccount)

<a id="Accounting.VoucherRow"></a>
### VoucherRows

Represents a voucher row.

- **Endpoint:** `GET /api/v1/Accounting/VoucherRows`
- **Required permission:** Show voucher
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `EntryIdentifier` | `String` | no |  |
| `VoucherId` | `Int64` | no | [Vouchers](/modules/Accounting.md#Accounting.Voucher) |
| `ParentVoucherDate` | `DateTimeOffset` | no |  |
| `ParentIsPreliminary` | `Boolean` | no |  |
| `ExchangeRate` | `Decimal` | no |  |
| `VatRateId` | `Int64?` | yes | [VatRates](/modules/Common.md#Common.VatRate) |
| `BalanceId` | `Int64?` | yes | [Balances](/modules/Accounting.md#Accounting.Balance) |
| `CodingMethodId` | `Int64?` | yes |  |
| `AccrualAccountingId` | `Int64?` | yes | [AccrualAccountings](/modules/Accounting.md#Accounting.AccrualAccounting) |
| `OrderNumber` | `String` | no |  |
| `DebitInCompanyCurrency` | `Decimal` | no |  |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `CreditInCompanyCurrency` | `Decimal` | no |  |
| `CreditInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `Debit` | `Decimal` | no |  |
| `DebitCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `Credit` | `Decimal` | no |  |
| `CreditCurrencyId` | `Int64` | no | [Currencies](/modules/Common.md#Common.Currency) |
| `Quantity` | `Decimal` | no |  |
| `CodingEntryId` | `Int64` | no | [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable) |
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable) |
| `NetAmountVoucherRowId` | `Int64?` | yes | [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow) |

**References out:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [AccrualAccountings](/modules/Accounting.md#Accounting.AccrualAccounting), [Balances](/modules/Accounting.md#Accounting.Balance), [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry), [Currencies](/modules/Common.md#Common.Currency), [VatRates](/modules/Common.md#Common.VatRate), [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow), [Vouchers](/modules/Accounting.md#Accounting.Voucher)
**Referenced by:** [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow), [Vouchers](/modules/Accounting.md#Accounting.Voucher)

<a id="Accounting.Voucher"></a>
### Vouchers

Represents a voucher.

- **Endpoint:** `GET /api/v1/Accounting/Vouchers`
- **Required permission:** Show voucher
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Version` | `Int32` | no |  |
| `SeriesId` | `Int64` | no | [VoucherSeries](/modules/Accounting.md#Accounting.VoucherSeries) |
| `AccountingYearId` | `Int64` | no | [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear) |
| `Number` | `Int64` | no |  |
| `Text` | `String` | no |  |
| `VoucherDate` | `DateTimeOffset` | no |  |
| `ConnectedVoucherId` | `Int64?` | yes | [Vouchers](/modules/Accounting.md#Accounting.Voucher) |
| `ConnectionType` | `Int32` | no |  |
| `ReverseConnectionVoucherId` | `Int64?` | yes | [Vouchers](/modules/Accounting.md#Accounting.Voucher) |
| `ReverseConnectionType` | `Int32` | no |  |
| `IsPreliminary` | `Boolean` | no |  |
| `BundleNumber` | `Int64?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `Rows` | `VoucherRows[]` | no | [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow) |
| `AccountsReceivableLedgerId` | `Int64?` | yes |  |
| `CancelledAccountsReceivableLedgerId` | `Int64?` | yes |  |
| `AccountsPayableLedgerId` | `Int64?` | yes |  |
| `CancelledAccountsPayableLedgerId` | `Int64?` | yes |  |
| `PreliminaryAccountsPayableLedgerId` | `Int64?` | yes |  |
| `CancelledPreliminaryAccountsPayableLedgerId` | `Int64?` | yes |  |
| `IncomingPaymentLedgerId` | `Int64?` | yes |  |
| `AccrualAccountingLedgerId` | `Int64?` | yes |  |
| `OutgoingPaymentLedgerId` | `Int64?` | yes |  |
| `FixedAssetLedgerId` | `Int64?` | yes |  |
| `UnplannedStockBalanceChangeLedgerId` | `Int64?` | yes |  |
| `StockTransactionLogLedgerId` | `Int64?` | yes |  |
| `ManufacturingOrderLogLedgerId` | `Int64?` | yes |  |
| `InvoiceLogLedgerId` | `Int64?` | yes |  |
| `PriceChangeLogLedgerId` | `Int64?` | yes |  |
| `CalculationDifferenceLedgerId` | `Int64?` | yes |  |
| `UnplannedStockBalanceChangeTransactionId` | `Int64?` | yes |  |
| `AccountsReceivableId` | `Int64?` | yes |  |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable) |
| `AccountsPayable` | `AccountsPayables` | no | [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable) |
| `AccrualAccountingRowId` | `Int64?` | yes | [AccrualAccountingRows](/modules/Accounting.md#Accounting.AccrualAccountingRow) |
| `VatBookingId` | `Int64?` | yes |  |
| `CorrectionBookingId` | `Int64?` | yes |  |
| `CNSeries` | `String` | no |  |
| `CNNumber` | `String` | no |  |

- `ConnectionType` — None=0, Correction=1, Copy=2
- `ReverseConnectionType` — None=0, Correction=1, Copy=2

**References out:** [AccountingYears](/modules/Accounting.md#Accounting.AccountingYear), [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccrualAccountingRows](/modules/Accounting.md#Accounting.AccrualAccountingRow), [Comments](/modules/Common.md#Common.Comment), [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow), [Vouchers](/modules/Accounting.md#Accounting.Voucher), [VoucherSeries](/modules/Accounting.md#Accounting.VoucherSeries)
**Referenced by:** [FixedAssets](/modules/Accounting.md#Accounting.FixedAsset), [VoucherRows](/modules/Accounting.md#Accounting.VoucherRow), [Vouchers](/modules/Accounting.md#Accounting.Voucher)

<a id="Accounting.VoucherSeries"></a>
### VoucherSeries

Represents a voucher series.

- **Endpoint:** `GET /api/v1/Accounting/VoucherSeries`
- **Required permission:** Show voucher
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Series` | `String` | no |  |
| `IsActive` | `Boolean` | no |  |

**Referenced by:** [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [Vouchers](/modules/Accounting.md#Accounting.Voucher)


## Payload types

<a id="Accounting.AccountingExportResponse"></a>
### AccountingExportResponse

The response object used by accounting exports.

- **Introduced in:** 23.9

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `CommandName` | `String` | no |  |
| `Name` | `String` | no |  |
| `Data` | `String` | no |  |


<a id="Accounting.SetOffDestination"></a>
### SetOffDestination

The set-off invoice.

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable) |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable) |
| `SetOffAmount` | `Decimal` | no |  |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](/modules/Common.md#Common.WriteOffCode) |
| `InterestType` | `Int32?` | yes |  |

- `InterestType` — InterestInvoice=0, NextRegularInvoice=1, None=2

**References out:** [AccountsPayables](/modules/Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](/modules/Accounting.md#Accounting.AccountsReceivable), [WriteOffCodes](/modules/Common.md#Common.WriteOffCode)


## Depends on other modules

- [Common](/modules/Common.md): [Addresses](/modules/Common.md#Common.Address), [ApplicationUsers](/modules/Common.md#Common.ApplicationUser), [BusinessContactBankAccounts](/modules/Common.md#Common.BusinessContactBankAccount), [Comments](/modules/Common.md#Common.Comment), [Countries](/modules/Common.md#Common.Country), [Currencies](/modules/Common.md#Common.Currency), [CurrencyExchangeTypes](/modules/Common.md#Common.CurrencyExchangeType), [Departments](/modules/Common.md#Common.Department), [LanguageCodes](/modules/Common.md#Common.LanguageCode), [PaymentMethods](/modules/Common.md#Common.PaymentMethod), [PaymentTerms](/modules/Common.md#Common.PaymentTerm), [VatGroups](/modules/Common.md#Common.VatGroup), [VatRates](/modules/Common.md#Common.VatRate), [Warehouses](/modules/Common.md#Common.Warehouse), [WriteOffCodes](/modules/Common.md#Common.WriteOffCode)
- [Manufacturing](/modules/Manufacturing.md): [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
- [Purchase](/modules/Purchase.md): [PurchaseOrders](/modules/Purchase.md#Purchase.PurchaseOrder), [PurchaseOrderDeliveryRows](/modules/Purchase.md#Purchase.PurchaseOrderDeliveryRow), [Suppliers](/modules/Purchase.md#Purchase.Supplier), [SupplierAccountGroups](/modules/Purchase.md#Purchase.SupplierAccountGroup)
- [Sales](/modules/Sales.md): [Customers](/modules/Sales.md#Sales.Customer), [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup)
