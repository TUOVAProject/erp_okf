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
| `BudgetId` | `Int64` | no | [AccountingBudgets](Accounting.md#Accounting.AccountingBudget) |
| `PeriodId` | `Int64` | no | [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod) |
| `Amount` | `Decimal` | no |  |
| `Quantity` | `Decimal` | no |  |

**References out:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget), [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod)
**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget)

<a id="Accounting.AccountingBudget"></a>
### AccountingBudgets

Represents an accounting budget.

- **Endpoint:** `GET /api/v1/Accounting/AccountingBudgets`
- **Required permission:** Show budget
- **Introduced in:** 23.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountYearSettingId` | `Int64` | no | [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting) |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) |
| `BalanceId` | `Int64` | no | [Balances](Accounting.md#Accounting.Balance) |
| `BudgetChartId` | `Int64` | no | [BudgetCharts](Accounting.md#Accounting.BudgetChart) |
| `BudgetTypeId` | `Int64` | no | [AccountingBudgetTypes](Accounting.md#Accounting.AccountingBudgetType) |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `Periods` | `AccountingBudgetPeriods[]` | no | [AccountingBudgetPeriods](Accounting.md#Accounting.AccountingBudgetPeriod) |

**References out:** [AccountingBudgetPeriods](Accounting.md#Accounting.AccountingBudgetPeriod), [AccountingBudgetTypes](Accounting.md#Accounting.AccountingBudgetType), [AccountingYears](Accounting.md#Accounting.AccountingYear), [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting), [Balances](Accounting.md#Accounting.Balance), [BudgetCharts](Accounting.md#Accounting.BudgetChart), [CodingEntries](Accounting.md#Accounting.CodingEntry)
**Referenced by:** [AccountingBudgetPeriods](Accounting.md#Accounting.AccountingBudgetPeriod)

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

**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget)

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
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) |
| `AccountingYear` | `AccountingYears` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) |

- `Status` — Undefined=0, Open=1, Closed=2, Locked=3

**References out:** [AccountingYears](Accounting.md#Accounting.AccountingYear)
**Referenced by:** [AccountingBudgetPeriods](Accounting.md#Accounting.AccountingBudgetPeriod), [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow)

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

**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget), [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod), [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting), [Balances](Accounting.md#Accounting.Balance), [OpeningBalances](Accounting.md#Accounting.OpeningBalance), [Vouchers](Accounting.md#Accounting.Voucher)

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

**Referenced by:** [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting), [BankAccounts](Accounting.md#Accounting.BankAccount), [CodingEntries](Accounting.md#Accounting.CodingEntry), [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [SalesAgreements](Sales.md#Sales.SalesAgreement), [VatRates](Common.md#Common.VatRate)

<a id="Accounting.AccountsPayableCashDiscountLevel"></a>
### AccountsPayableCashDiscountLevels

Represents a cash discount level for an accounts payable.

- **Endpoint:** `GET /api/v1/Accounting/AccountsPayableCashDiscountLevels`
- **Required permission:** Show accounts payable
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `Discount` | `Decimal?` | yes |  |
| `DiscountDate` | `DateTimeOffset?` | yes |  |
| `RowIndex` | `Int32?` | yes |  |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable)

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
| `CancelCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `CancelComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](Common.md#Common.PaymentMethod) |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) |
| `Language` | `LanguageCodes` | no | [LanguageCodes](Common.md#Common.LanguageCode) |
| `SuppliersInvoiceNumber` | `String` | no |  |
| `InvoiceType` | `Int32` | no |  |
| `IsCredit` | `Boolean` | no |  |
| `IsFinalBooked` | `Boolean` | no |  |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) |
| `PreliminaryBookingDate` | `DateTimeOffset?` | yes |  |
| `VoucherDate` | `DateTimeOffset?` | yes |  |
| `CancelVoucherDate` | `DateTimeOffset?` | yes |  |
| `SupplierAccountGroupId` | `Int64?` | yes | [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup) |
| `CountryId` | `Int64` | no | [Countries](Common.md#Common.Country) |
| `Status` | `Int32` | no |  |
| `BlockMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `BlockMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `OCRNumber` | `String` | no |  |
| `UseOCRNumber` | `Boolean` | no |  |
| `CreditedAccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) |
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
| `InvoiceAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `InvoiceAmountInCompanyCurrency` | `Decimal` | no |  |
| `InvoiceAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `VatAmount` | `Decimal` | no |  |
| `VatAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `VatAmountInCompanyCurrency` | `Decimal` | no |  |
| `VatAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `RestAmount` | `Decimal` | no |  |
| `RestAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `RestAmountInCompanyCurrency` | `Decimal` | no |  |
| `RestAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `OrderedRestAmount` | `Decimal` | no |  |
| `OrderedRestAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `CurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `ExchangeRate` | `Decimal` | no |  |
| `PaidInFullDate` | `DateTimeOffset?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ReferenceNumber` | `String` | no |  |
| `UseFixedDueDate` | `Boolean` | no |  |
| `VatGroupId` | `Int64?` | yes | [VatGroups](Common.md#Common.VatGroup) |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `FinalBookingId` | `Int64?` | yes |  |
| `BusinessContactId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
| `Payments` | `OutgoingPayments[]` | no | [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment) |
| `WithholdTaxAmount` | `Decimal?` | yes |  |
| `WithholdTaxAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `WithholdTaxAmountInCompanyCurrency` | `Decimal?` | yes |  |
| `WithholdTaxAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `InputVatDate` | `DateTimeOffset?` | yes |  |
| `OutputVatDate` | `DateTimeOffset?` | yes |  |

- `InvoiceType` — Standard=1, Interest=4, OnAccount=5, ForOrderingOnAccount=8, CorrectionInvoice=9
- `Status` — Registered=0, Preliminary=1, Final=2, Cancelled=6
- `BlockedStatus` — None=0, Message=1, Blocked=2
- `BlockedContextType` (bitmask) — None=0, Payment=1
- `EimInvoiceStatus` — None=0, Hold=1, ForAuthorization=2, Approved=3, Rejected=4, FinalBooked=5

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [ApplicationUsers](Common.md#Common.ApplicationUser), [Comments](Common.md#Common.Comment), [Countries](Common.md#Common.Country), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [LanguageCodes](Common.md#Common.LanguageCode), [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment), [PaymentMethods](Common.md#Common.PaymentMethod), [PaymentTerms](Common.md#Common.PaymentTerm), [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup), [Suppliers](Purchase.md#Purchase.Supplier), [VatGroups](Common.md#Common.VatGroup), [Warehouses](Common.md#Common.Warehouse)
**Referenced by:** [AccountsPayableCashDiscountLevels](Accounting.md#Accounting.AccountsPayableCashDiscountLevel), [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting), [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink), [EimDocuments](Purchase.md#Purchase.EimDocument), [FixedAssets](Accounting.md#Accounting.FixedAsset), [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [SetOffDestination](Accounting.md#Accounting.SetOffDestination), [VoucherRows](Accounting.md#Accounting.VoucherRow), [Vouchers](Accounting.md#Accounting.Voucher)

<a id="Accounting.AccountsReceivableCashDiscountLevel"></a>
### AccountsReceivableCashDiscountLevels

Represents a cash discount level for an accounts receivable.

- **Endpoint:** `GET /api/v1/Accounting/AccountsReceivableCashDiscountLevels`
- **Required permission:** Show accounts receivable
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ParentId` | `Int64` | no | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) |
| `Discount` | `Decimal?` | yes |  |
| `DiscountDate` | `DateTimeOffset?` | yes |  |
| `RowIndex` | `Int32?` | yes |  |

**References out:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable)

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
| `BookingId` | `Int64?` | yes | [Bookings](Accounting.md#Accounting.Booking) |
| `Booking` | `Bookings` | no | [Bookings](Accounting.md#Accounting.Booking) |
| `InvoiceType` | `Int32` | no |  |
| `LatestReminderDate` | `DateTimeOffset?` | yes |  |
| `PaymentReminder` | `Boolean` | no |  |
| `NumberOfPaymentReminders` | `Int32` | no |  |
| `CollectionDate` | `DateTimeOffset?` | yes |  |
| `Collection` | `Boolean` | no |  |
| `InterestType` | `Int32` | no |  |
| `IsComprehensive` | `Boolean` | no |  |
| `PartialInvoiceType` | `Int32` | no |  |
| `CustomerAccountGroupId` | `Int64` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `CustomerAccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) |
| `DebitInvoiceId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) |
| `OnAccountIncomingPaymentLedgerId` | `Int64?` | yes |  |
| `OnAccountCancelledIncomingPaymentLedgerId` | `Int64?` | yes |  |
| `IsEInvoiceExported` | `Boolean` | no |  |
| `AccountsReceivableLedgerId` | `Int64?` | yes |  |
| `CancelledAccountsReceivableLedgerId` | `Int64?` | yes |  |
| `Status` | `Int32` | no |  |
| `LatePaymentFee` | `Decimal?` | yes |  |
| `CancelCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `CancelComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `CancelDate` | `DateTimeOffset` | no |  |
| `CancelBookingId` | `Int64?` | yes | [Bookings](Accounting.md#Accounting.Booking) |
| `CancelBooking` | `Bookings` | no | [Bookings](Accounting.md#Accounting.Booking) |
| `BusinessContactId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `InvoiceNumber` | `Int64` | no |  |
| `InvoiceDate` | `DateTimeOffset` | no |  |
| `DueDate` | `DateTimeOffset` | no |  |
| `IsCredit` | `Boolean` | no |  |
| `InvoiceAmount` | `Decimal` | no |  |
| `InvoiceAmountCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `InvoiceAmountInCompanyCurrency` | `Decimal` | no |  |
| `InvoiceAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `VatAmount` | `Decimal` | no |  |
| `VatAmountCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `VatAmountInCompanyCurrency` | `Decimal` | no |  |
| `VatAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `RestAmount` | `Decimal` | no |  |
| `RestAmountCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `RestAmountInCompanyCurrency` | `Decimal` | no |  |
| `RestAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `OrderedRestAmount` | `Decimal` | no |  |
| `OrderedRestAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `ExchangeRate` | `Decimal` | no |  |
| `PaidInFullDate` | `DateTimeOffset?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `ReferenceNumber` | `String` | no |  |
| `UseFixedDueDate` | `Boolean` | no |  |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) |
| `PaymentTermId` | `Int64` | no | [PaymentTerms](Common.md#Common.PaymentTerm) |
| `ChineseVatInvoiceNumber` | `String` | no |  |
| `ChineseVatInvoiceDate` | `DateTimeOffset?` | yes |  |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) |
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

**References out:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [Bookings](Accounting.md#Accounting.Booking), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup), [Customers](Sales.md#Sales.Customer), [PaymentTerms](Common.md#Common.PaymentTerm), [VatGroups](Common.md#Common.VatGroup)
**Referenced by:** [AccountsReceivableCashDiscountLevels](Accounting.md#Accounting.AccountsReceivableCashDiscountLevel), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [CaseEntry](Inventory.md#Inventory.CaseEntry), [CaseEntryPartLinks](Inventory.md#Inventory.CasePartLink), [FixedAssetSales](Accounting.md#Accounting.FixedAssetSale), [IncomingPayments](Accounting.md#Accounting.IncomingPayment), [InvoiceLogs](Sales.md#Sales.InvoiceLog), [SetOffDestination](Accounting.md#Accounting.SetOffDestination), [VoucherRows](Accounting.md#Accounting.VoucherRow)

<a id="Accounting.AccountYearSettingCodingDimensionAvailability"></a>
### AccountYearSettingCodingDimensionAvailabilities

Represents a coding dimension available on a account for a specific year setting.

- **Endpoint:** `GET /api/v1/Accounting/AccountYearSettingCodingDimensionAvailabilities`
- **Required permission:** Show accounting year
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](Accounting.md#Accounting.CodingDimension) |
| `CodingDimension` | `CodingDimensions` | no | [CodingDimensions](Accounting.md#Accounting.CodingDimension) |
| `CodingDimensionAvailability` | `Int32` | no |  |
| `AccountYearSettingId` | `Int64` | no | [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting) |

- `CodingDimensionAvailability` — NotAllowed=0, Allowed=1, Mandatory=2

**References out:** [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting), [CodingDimensions](Accounting.md#Accounting.CodingDimension)
**Referenced by:** [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting)

<a id="Accounting.AccountYearSetting"></a>
### AccountYearSettings

Represents a account setting on a specific year.

- **Endpoint:** `GET /api/v1/Accounting/AccountYearSettings`
- **Required permission:** Show accounting year
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) |
| `Description` | `String` | no |  |
| `AllowSpecification` | `Boolean` | no |  |
| `AllowQuantity` | `Boolean` | no |  |
| `IsCurrencyAccount` | `Boolean` | no |  |
| `CurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `IsAccrual` | `Boolean` | no |  |
| `DebitOrCreditType` | `Int32` | no |  |
| `VatType` | `Int32` | no |  |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) |
| `BlockedForManualCoding` | `Boolean` | no |  |
| `IsFixedAssetAccount` | `Boolean` | no |  |
| `IncludeOrderNumberInCoding` | `Boolean` | no |  |
| `AccountId` | `Int64` | no | [Accounts](Accounting.md#Accounting.Account) |
| `Account` | `Accounts` | no | [Accounts](Accounting.md#Accounting.Account) |
| `AccountCodingDimensions` | `AccountYearSettingCodingDimensionAvailabilities[]` | no | [AccountYearSettingCodingDimensionAvailabilities](Accounting.md#Accounting.AccountYearSettingCodingDimensionAvailability) |

- `DebitOrCreditType` — Debit=0, Credit=1
- `VatType` — None=0, Sales=1, Purchase=2, InputVat=3, OutputVat=4

**References out:** [AccountingYears](Accounting.md#Accounting.AccountingYear), [Accounts](Accounting.md#Accounting.Account), [AccountYearSettingCodingDimensionAvailabilities](Accounting.md#Accounting.AccountYearSettingCodingDimensionAvailability), [Currencies](Common.md#Common.Currency), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget), [AccountYearSettingCodingDimensionAvailabilities](Accounting.md#Accounting.AccountYearSettingCodingDimensionAvailability)

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

**Referenced by:** [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow)

<a id="Accounting.AccrualAccountingRow"></a>
### AccrualAccountingRows

Represents a accrual accounting row.

- **Endpoint:** `GET /api/v1/Accounting/AccrualAccountingRows`
- **Required permission:** Show accrual
- **Introduced in:** 2.27

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PeriodId` | `Int64` | no | [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod) |
| `Period` | `AccountingYearPeriods` | no | [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod) |
| `PeriodAmountInCompanyCurrency` | `Decimal` | no |  |
| `AccrualAccountingId` | `Int64` | no |  |
| `IsReleased` | `Boolean` | no |  |
| `LedgerId` | `Int64?` | yes | [AccrualAccountingLedgers](Accounting.md#Accounting.AccrualAccountingLedger) |
| `Ledger` | `AccrualAccountingLedgers` | no | [AccrualAccountingLedgers](Accounting.md#Accounting.AccrualAccountingLedger) |
| `BookingId` | `Int64?` | yes |  |
| `RowIndex` | `Int32` | no |  |
| `BookingRows` | `BookingRows[]` | no | [BookingRows](Accounting.md#Accounting.BookingRow) |

**References out:** [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod), [AccrualAccountingLedgers](Accounting.md#Accounting.AccrualAccountingLedger), [BookingRows](Accounting.md#Accounting.BookingRow)
**Referenced by:** [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting), [Vouchers](Accounting.md#Accounting.Voucher)

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
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `AccountsPayableBookingRowId` | `Int64?` | yes |  |
| `VoucherId` | `Int64?` | yes |  |
| `VoucherRowId` | `Int64?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `CancelCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `CancelComment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `IsCancelled` | `Boolean` | no |  |
| `BookingId` | `Int64` | no |  |
| `Rows` | `AccrualAccountingRows[]` | no | [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow) |
| `BookingRows` | `BookingRows[]` | no | [BookingRows](Accounting.md#Accounting.BookingRow) |
| `AccountsPayableBookingRow` | `BookingRows` | no | [BookingRows](Accounting.md#Accounting.BookingRow) |

- `Type` — AccountsPayableBookingRow=1, VoucherRow=2, ReverseVoucher=3, FreeBooking=4, SalesAgreement=5, SupplierAgreement=6

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow), [BookingRows](Accounting.md#Accounting.BookingRow), [Comments](Common.md#Common.Comment)
**Referenced by:** [BookingRows](Accounting.md#Accounting.BookingRow), [VoucherRows](Accounting.md#Accounting.VoucherRow)

<a id="Accounting.AllocationKeyResultRow"></a>
### AllocationKeyResultRows

Represent an allocation key result row.

- **Endpoint:** `GET /api/v1/Accounting/AllocationKeyResultRows`
- **Required permission:** Show allocation keys
- **Introduced in:** 24.8

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AllocationKeyId` | `Int64` | no | [AllocationKeys](Accounting.md#Accounting.AllocationKey) |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `Percentage` | `Decimal` | no |  |
| `RowIndex` | `Int32` | no |  |

**References out:** [AllocationKeys](Accounting.md#Accounting.AllocationKey), [CodingEntries](Accounting.md#Accounting.CodingEntry)
**Referenced by:** [AllocationKeys](Accounting.md#Accounting.AllocationKey)

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
| `AllocationKeyResultRow` | `AllocationKeyResultRows[]` | no | [AllocationKeyResultRows](Accounting.md#Accounting.AllocationKeyResultRow) |

**References out:** [AllocationKeyResultRows](Accounting.md#Accounting.AllocationKeyResultRow)
**Referenced by:** [AllocationKeyResultRows](Accounting.md#Accounting.AllocationKeyResultRow), [AutoAllocations](Accounting.md#Accounting.AutoAllocation)

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
| `AllocationKeyId` | `Int64?` | yes | [AllocationKeys](Accounting.md#Accounting.AllocationKey) |
| `AllocationKey` | `AllocationKeys` | no | [AllocationKeys](Accounting.md#Accounting.AllocationKey) |
| `AccountFrom` | `String` | no |  |
| `AccountTo` | `String` | no |  |

- `Type` — Direct=0, PeriodBalance=1, AccumulatedBalance=2

**References out:** [AllocationKeys](Accounting.md#Accounting.AllocationKey)

<a id="Accounting.BalanceRowDay"></a>
### BalanceRowDays

Represents a balance row day.

- **Endpoint:** `GET /api/v1/Accounting/BalanceRowDays`
- **Required permission:** Show balance information
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `BalanceId` | `Int64` | no | [Balances](Accounting.md#Accounting.Balance) |
| `Credit` | `Decimal` | no |  |
| `CreditInCompanyCurrency` | `Decimal` | no |  |
| `Date` | `DateTimeOffset` | no |  |
| `Debit` | `Decimal` | no |  |
| `DebitInCompanyCurrency` | `Decimal` | no |  |
| `PeriodNumber` | `Int32` | no |  |
| `Quantity` | `Decimal` | no |  |

**References out:** [Balances](Accounting.md#Accounting.Balance)

<a id="Accounting.Balance"></a>
### Balances

Represents a balance.

- **Endpoint:** `GET /api/v1/Accounting/Balances`
- **Required permission:** Show balance information
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) |
| `Amount` | `Decimal` | no |  |
| `AmountInCompanyCurrency` | `Decimal` | no |  |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `OpeningBalanceId` | `Int64?` | yes | [OpeningBalances](Accounting.md#Accounting.OpeningBalance) |
| `Quantity` | `Decimal` | no |  |

**References out:** [AccountingYears](Accounting.md#Accounting.AccountingYear), [CodingEntries](Accounting.md#Accounting.CodingEntry), [OpeningBalances](Accounting.md#Accounting.OpeningBalance)
**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget), [BalanceRowDays](Accounting.md#Accounting.BalanceRowDay), [VoucherRows](Accounting.md#Accounting.VoucherRow)

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
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `AccountingAccountId` | `Int64` | no | [Accounts](Accounting.md#Accounting.Account) |
| `BankAddressId` | `Int64` | no | [Addresses](Common.md#Common.Address) |

- `Type` — Iban=1, Bban=2, Upic=3, Miscellaneous=4

**References out:** [Accounts](Accounting.md#Accounting.Account), [Addresses](Common.md#Common.Address), [Currencies](Common.md#Common.Currency)
**Referenced by:** [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment)

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
| `PurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) |
| `BookingId` | `Int64` | no | [Bookings](Accounting.md#Accounting.Booking) |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) |
| `AccrualAccountingId` | `Int64?` | yes | [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting) |
| `OrderNumber` | `String` | no |  |
| `DebitInCompanyCurrency` | `Decimal` | no |  |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `CreditInCompanyCurrency` | `Decimal` | no |  |
| `CreditInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Debit` | `Decimal` | no |  |
| `DebitCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Credit` | `Decimal` | no |  |
| `CreditCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Quantity` | `Decimal` | no |  |
| `RowIndex` | `Int32` | no |  |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `NetAmountBookingRowId` | `Int64?` | yes | [BookingRows](Accounting.md#Accounting.BookingRow) |

- `Type` — NotInitialized=0, AccountsReceivable=1, OutputVat=2, AccountsPayable=3, PreliminaryAccountsPayable=4, PaymentIn=5, PaymentOut=6, Purchase=7, Sales=8, Miscellaneous=9, PurchaseWithoutOrder=10, InvoicingCharges=11, InsuranceCost=12, RoundOff=13, SetupPrice=14, Material=15, Inventory=16, PreliminaryAccount=17, InputVat=18, ExchangeRateAdjustment=19, InvoiceReminderFee=20, PriceDifference=21, PaymentInVat=22, PaymentOutVat=23, OtherPayment=24, InputVatNonDeductible=25, CurrencyDifference=26, WithholdingTax=27, ManualAccountsPayableFinalBookingFromG4=999

**References out:** [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting), [BookingRows](Accounting.md#Accounting.BookingRow), [Bookings](Accounting.md#Accounting.Booking), [CodingEntries](Accounting.md#Accounting.CodingEntry), [Currencies](Common.md#Common.Currency), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow), [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting), [BookingRows](Accounting.md#Accounting.BookingRow), [Bookings](Accounting.md#Accounting.Booking)

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
| `Rows` | `BookingRows[]` | no | [BookingRows](Accounting.md#Accounting.BookingRow) |

**References out:** [BookingRows](Accounting.md#Accounting.BookingRow)
**Referenced by:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [BookingRows](Accounting.md#Accounting.BookingRow), [FixedAssetSales](Accounting.md#Accounting.FixedAssetSale), [IncomingPayments](Accounting.md#Accounting.IncomingPayment), [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment)

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

**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget)

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
| `CodingElements` | `CodingElements[]` | no | [CodingElements](Accounting.md#Accounting.CodingElement) |

- `ReferenceEntityType` — None=0, Project=1, ProductGroup=2, PartCode=3, Part=4, Department=5, WorkCenter=6, CustomerRootFromOrder=7, CustomerRootFromInvoice=8, SupplierRoot=9, Person=10, CustomerAccountGroupOnCustomer=11, CustomerDistrict=12, CustomerType=13, SupplierAccountGroupOnSupplier=14, SupplierDistrict=15, SupplierType=16

**References out:** [CodingElements](Accounting.md#Accounting.CodingElement)
**Referenced by:** [AccountYearSettingCodingDimensionAvailabilities](Accounting.md#Accounting.AccountYearSettingCodingDimensionAvailability), [CodingElements](Accounting.md#Accounting.CodingElement), [CodingEntryElements](Accounting.md#Accounting.CodingEntryElement)

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
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](Accounting.md#Accounting.CodingDimension) |
| `IsActive` | `Boolean` | no |  |

**References out:** [CodingDimensions](Accounting.md#Accounting.CodingDimension)
**Referenced by:** [CodingDimensions](Accounting.md#Accounting.CodingDimension), [CodingEntryElements](Accounting.md#Accounting.CodingEntryElement)

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
| `AccountId` | `Int64?` | yes | [Accounts](Accounting.md#Accounting.Account) |
| `Account` | `Accounts` | no | [Accounts](Accounting.md#Accounting.Account) |
| `CodingEntryElements` | `CodingEntryElements[]` | no | [CodingEntryElements](Accounting.md#Accounting.CodingEntryElement) |

**References out:** [Accounts](Accounting.md#Accounting.Account), [CodingEntryElements](Accounting.md#Accounting.CodingEntryElement)
**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget), [AllocationKeyResultRows](Accounting.md#Accounting.AllocationKeyResultRow), [Balances](Accounting.md#Accounting.Balance), [BookingRows](Accounting.md#Accounting.BookingRow), [CodingEntryElements](Accounting.md#Accounting.CodingEntryElement), [CodingRows](Accounting.md#Accounting.CodingRow), [CustomerOrderPaymentPlanRows](Sales.md#Sales.CustomerOrderPaymentPlanRow), [OpeningBalances](Accounting.md#Accounting.OpeningBalance), [PaymentMethods](Common.md#Common.PaymentMethod), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [StandardAccounts](Accounting.md#Accounting.StandardAccount), [SupplierAccounts](Purchase.md#Purchase.SupplierAccount), [Suppliers](Purchase.md#Purchase.Supplier), [VoucherRows](Accounting.md#Accounting.VoucherRow), [WriteOffCodes](Common.md#Common.WriteOffCode)

<a id="Accounting.CodingEntryElement"></a>
### CodingEntryElements

Represents a coding entry element.

- **Endpoint:** `GET /api/v1/Accounting/CodingEntryElements`
- **Required permission:** Show dimensions/dimension codes
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](Accounting.md#Accounting.CodingDimension) |
| `CodingDimension` | `CodingDimensions` | no | [CodingDimensions](Accounting.md#Accounting.CodingDimension) |
| `ReferencingEntityId` | `Int64?` | yes | [CodingElements](Accounting.md#Accounting.CodingElement) |

**References out:** [CodingDimensions](Accounting.md#Accounting.CodingDimension), [CodingElements](Accounting.md#Accounting.CodingElement), [CodingEntries](Accounting.md#Accounting.CodingEntry)
**Referenced by:** [CodingEntries](Accounting.md#Accounting.CodingEntry)

<a id="Accounting.CodingRow"></a>
### CodingRows

Represents a coding row.

- **Endpoint:** `GET /api/v1/Accounting/CodingRows`
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `Type` | `Int32` | no |  |

- `Type` — Standard=1, Setup=2, Material=3, Inventory=4, PriceDifference=5, Cost=6

**References out:** [CodingEntries](Accounting.md#Accounting.CodingEntry)
**Referenced by:** [Codings](Accounting.md#Accounting.Coding)

<a id="Accounting.Coding"></a>
### Codings

Represents a coding.

- **Endpoint:** `GET /api/v1/Accounting/Codings`
- **Introduced in:** 2.30

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `CodingRows` | `CodingRows[]` | no | [CodingRows](Accounting.md#Accounting.CodingRow) |

**References out:** [CodingRows](Accounting.md#Accounting.CodingRow)
**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [InquiryRows](Purchase.md#Purchase.InquiryRow), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](Sales.md#Sales.QuoteRow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow)

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
| `ParentId` | `Int64` | no | [FixedAssets](Accounting.md#Accounting.FixedAsset) |

**References out:** [FixedAssets](Accounting.md#Accounting.FixedAsset)

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

**Referenced by:** [FixedAssets](Accounting.md#Accounting.FixedAsset)

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
| `GroupId` | `Int64` | no | [FixedAssetGroups](Accounting.md#Accounting.FixedAssetGroup) |
| `Group` | `FixedAssetGroups` | no | [FixedAssetGroups](Accounting.md#Accounting.FixedAssetGroup) |
| `AcquisitionDate` | `DateTimeOffset` | no |  |
| `AcquisitionValue` | `Decimal` | no |  |
| `Quantity` | `Decimal` | no |  |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `VoucherId` | `Int64?` | yes | [Vouchers](Accounting.md#Accounting.Voucher) |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) |
| `CategoryString` | `String` | no |  |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) |
| `DepartmentId` | `Int64?` | yes | [Departments](Common.md#Common.Department) |
| `SerialNumber` | `String` | no |  |
| `Location` | `String` | no |  |
| `PlannedDepreciationStartDate` | `DateTimeOffset` | no |  |
| `PlannedDepreciationTimeInYears` | `Decimal` | no |  |
| `PlannedDepreciationPercentage` | `Decimal` | no |  |
| `CalculatedDepreciationStartDate` | `DateTimeOffset` | no |  |
| `CalculatedDepreciationPercentage` | `Decimal` | no |  |
| `MinimumValue` | `Decimal` | no |  |
| `Sales` | `FixedAssetSales[]` | no | [FixedAssetSales](Accounting.md#Accounting.FixedAssetSale) |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [Departments](Common.md#Common.Department), [FixedAssetGroups](Accounting.md#Accounting.FixedAssetGroup), [FixedAssetSales](Accounting.md#Accounting.FixedAssetSale), [Suppliers](Purchase.md#Purchase.Supplier), [Vouchers](Accounting.md#Accounting.Voucher), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [FixedAssetDepreciations](Accounting.md#Accounting.FixedAssetDepreciation)

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
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `VoucherText` | `String` | no |  |
| `SalesTimestamp` | `DateTimeOffset` | no |  |
| `BookingId` | `Int64?` | yes | [Bookings](Accounting.md#Accounting.Booking) |

- `Type` — Sale=0, Retirement=1

**References out:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [Bookings](Accounting.md#Accounting.Booking), [Comments](Common.md#Common.Comment), [Customers](Sales.md#Sales.Customer)
**Referenced by:** [FixedAssets](Accounting.md#Accounting.FixedAsset)

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
| `BankChargeAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `BookingId` | `Int64?` | yes | [Bookings](Accounting.md#Accounting.Booking) |
| `CancelDate` | `DateTimeOffset?` | yes |  |
| `CancelTimeStamp` | `DateTimeOffset?` | yes |  |
| `CancelledByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `CancelPaymentDate` | `DateTimeOffset` | no |  |
| `CreationDate` | `DateTimeOffset` | no |  |
| `CurrencyExchangeRate` | `Decimal` | no |  |
| `InterestType` | `Int32` | no |  |
| `IsCancelled` | `Boolean` | no |  |
| `PaidAmount` | `Decimal` | no |  |
| `PaidAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PaidAmountInCompanyCurrency` | `Decimal` | no |  |
| `PaidAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `PaidVatAmount` | `Decimal?` | yes |  |
| `PaidVatAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `ParentId` | `Int64` | no | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) |
| `PaymentDate` | `DateTimeOffset` | no |  |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](Common.md#Common.PaymentMethod) |
| `VoucherText` | `String` | no |  |
| `WriteOffAmount` | `Decimal?` | yes |  |
| `WriteOffAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `WriteOffAmountInCompanyCurrency` | `Decimal?` | yes |  |
| `WriteOffAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](Common.md#Common.WriteOffCode) |
| `InterestInvoicingStatus` | `Int32` | no |  |
| `IsSetOffPayment` | `Boolean` | no |  |
| `LedgerId` | `Int64?` | yes |  |
| `ChequeNumber` | `String` | no |  |

- `InterestType` — InterestInvoice=0, NextRegularInvoice=1, None=2
- `InterestInvoicingStatus` — NoInterest=0, Interest=1, InterestInvoiced=9

**References out:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [ApplicationUsers](Common.md#Common.ApplicationUser), [Bookings](Accounting.md#Accounting.Booking), [Currencies](Common.md#Common.Currency), [PaymentMethods](Common.md#Common.PaymentMethod), [WriteOffCodes](Common.md#Common.WriteOffCode)
**Referenced by:** [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment)

<a id="Accounting.OpeningBalance"></a>
### OpeningBalances

Represents an opening balance.

- **Endpoint:** `GET /api/v1/Accounting/OpeningBalances`
- **Required permission:** Show opening balance
- **Introduced in:** 22.5

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `Credit` | `Decimal` | no |  |
| `CreditCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `CreditInCompanyCurrency` | `Decimal` | no |  |
| `CreditInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `Debit` | `Decimal` | no |  |
| `DebitCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `DebitInCompanyCurrency` | `Decimal` | no |  |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `ExchangeRate` | `Decimal` | no |  |
| `Quantity` | `Decimal` | no |  |

**References out:** [AccountingYears](Accounting.md#Accounting.AccountingYear), [CodingEntries](Accounting.md#Accounting.CodingEntry), [Currencies](Common.md#Common.Currency)
**Referenced by:** [Balances](Accounting.md#Accounting.Balance)

<a id="Accounting.OutgoingPayment"></a>
### OutgoingPayments

Represents an outgoing payment.

- **Endpoint:** `GET /api/v1/Accounting/OutgoingPayments`
- **Required permission:** Show accounts payable
- **Introduced in:** 24.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AccountsPayableId` | `Int64` | no | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) |
| `CreationDate` | `DateTimeOffset` | no |  |
| `PaymentDate` | `DateTimeOffset` | no |  |
| `PaymentMethodId` | `Int64` | no | [PaymentMethods](Common.md#Common.PaymentMethod) |
| `PaidAmount` | `Decimal` | no |  |
| `PaidAmountCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `PaidAmountInCompanyCurrency` | `Decimal` | no |  |
| `PaidAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `PaidVatAmount` | `Decimal?` | yes |  |
| `PaidVatAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `BankChargeAmount` | `Decimal?` | yes |  |
| `BankChargeAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `IsOrdered` | `Boolean` | no |  |
| `IsCancelled` | `Boolean` | no |  |
| `CancelledByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) |
| `CancelDate` | `DateTimeOffset?` | yes |  |
| `CancelTimeStamp` | `DateTimeOffset?` | yes |  |
| `ReceivingBankAccountId` | `Int64?` | yes | [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount) |
| `SendingBankAccountId` | `Int64?` | yes | [BankAccounts](Accounting.md#Accounting.BankAccount) |
| `SetOffIncomingPaymentId` | `Int64?` | yes | [IncomingPayments](Accounting.md#Accounting.IncomingPayment) |
| `BookingId` | `Int64?` | yes | [Bookings](Accounting.md#Accounting.Booking) |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](Common.md#Common.WriteOffCode) |
| `WriteOffAmount` | `Decimal?` | yes |  |
| `WriteOffAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `WriteOffAmountInCompanyCurrency` | `Decimal?` | yes |  |
| `WriteOffAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) |
| `BundleNumber` | `Int64` | no |  |
| `ChequeNumber` | `String` | no |  |
| `CurrencyExchangeRate` | `Decimal` | no |  |
| `VoucherText` | `String` | no |  |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [ApplicationUsers](Common.md#Common.ApplicationUser), [BankAccounts](Accounting.md#Accounting.BankAccount), [Bookings](Accounting.md#Accounting.Booking), [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount), [Currencies](Common.md#Common.Currency), [IncomingPayments](Accounting.md#Accounting.IncomingPayment), [PaymentMethods](Common.md#Common.PaymentMethod), [Suppliers](Purchase.md#Purchase.Supplier), [WriteOffCodes](Common.md#Common.WriteOffCode)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable)

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
| `CodingEntryId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `StandardAccountCategory` | `Int32` | no |  |

- `AccountType` — NotInitialized=0, AccountsReceivable=1, AccountsPayable=2, InvoicingCharges=3, RoundOff=6, CustomerDiscounts=10, BadDebtLoss=11, ExchangeProfitAccountsReceivable=16, BankCharge=17, SupplierDiscounts=18, AccountsPayableWriteOffs=19, PreliminaryAccount=20, InsuranceCost=21, PreliminaryAccountsPayable=22, ReminderFee=23, RoundOffVat=27, VatClearingAccountToPay=28, ExchangeLossAccountsReceivable=32, ExchangeProfitAccountsPayable=33, ExchangeLossAccountsPayable=34, TransitionAccountFixedAssetSales=35, SuspenseAccountDuringPosteriorCoding=40, DebitAccountForInternalInvoices=43, AdditionalPartRowPurchase=50, AdditionalPartRowSales=51, PenaltyInterestExpenseForAccountsPayable=55, PaidAdvanceCustomer=63, UnrealizedExchangeProfitSales=96, UnrealizedExchangeLossSales=97, UnrealizedExchangeProfitPurchase=98, UnrealizedExchangeLossPurchase=99, OnAccountPurchase=101, ExchangeProfitOnPriceDifference=102, ExchangeLossOnPriceDifference=103, RoundOffPurchase=104, VatClearingAccountToReceive=105, OverDepreciations=106, AccountForRevaluationSales=124, AccountForRevaluationPurchase=125, PreliminaryAccrualAccountSuspendedVatForSalesAgreement=126, RecognizedIncomeNotInvoiced=135, RecognizedIncomeConsecutivePrice=136, RecognizedIncomeFixedPrice=137, AnticipatedLossIncomeFixedPrice=140, ReduceOfIncomeAnticipatedLoss=141, OffsetAccountForAdvancesBookedOnBalanceAccount=150, OnAccountSales=151, AccrualAccountForAgreements=152, ProjectMaterialCostCalculationWriteUp=153, ProjectMaterialCostCalculationOffset=154, FactoringFees=155, FactoringRecource=156, FactoringLoss=157, PaidInvoicesFromCustomer=158, AccrualAccountForSupplierAgreements=159
- `StandardAccountCategory` — Sales=1, Purchase=2, Accounting=3

**References out:** [CodingEntries](Accounting.md#Accounting.CodingEntry)
**Referenced by:** [SupplierAccounts](Purchase.md#Purchase.SupplierAccount)

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
| `VoucherId` | `Int64` | no | [Vouchers](Accounting.md#Accounting.Voucher) |
| `ParentVoucherDate` | `DateTimeOffset` | no |  |
| `ParentIsPreliminary` | `Boolean` | no |  |
| `ExchangeRate` | `Decimal` | no |  |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) |
| `BalanceId` | `Int64?` | yes | [Balances](Accounting.md#Accounting.Balance) |
| `CodingMethodId` | `Int64?` | yes |  |
| `AccrualAccountingId` | `Int64?` | yes | [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting) |
| `OrderNumber` | `String` | no |  |
| `DebitInCompanyCurrency` | `Decimal` | no |  |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `CreditInCompanyCurrency` | `Decimal` | no |  |
| `CreditInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Debit` | `Decimal` | no |  |
| `DebitCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Credit` | `Decimal` | no |  |
| `CreditCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) |
| `Quantity` | `Decimal` | no |  |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) |
| `NetAmountVoucherRowId` | `Int64?` | yes | [VoucherRows](Accounting.md#Accounting.VoucherRow) |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting), [Balances](Accounting.md#Accounting.Balance), [CodingEntries](Accounting.md#Accounting.CodingEntry), [Currencies](Common.md#Common.Currency), [VatRates](Common.md#Common.VatRate), [VoucherRows](Accounting.md#Accounting.VoucherRow), [Vouchers](Accounting.md#Accounting.Voucher)
**Referenced by:** [VoucherRows](Accounting.md#Accounting.VoucherRow), [Vouchers](Accounting.md#Accounting.Voucher)

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
| `SeriesId` | `Int64` | no | [VoucherSeries](Accounting.md#Accounting.VoucherSeries) |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) |
| `Number` | `Int64` | no |  |
| `Text` | `String` | no |  |
| `VoucherDate` | `DateTimeOffset` | no |  |
| `ConnectedVoucherId` | `Int64?` | yes | [Vouchers](Accounting.md#Accounting.Voucher) |
| `ConnectionType` | `Int32` | no |  |
| `ReverseConnectionVoucherId` | `Int64?` | yes | [Vouchers](Accounting.md#Accounting.Voucher) |
| `ReverseConnectionType` | `Int32` | no |  |
| `IsPreliminary` | `Boolean` | no |  |
| `BundleNumber` | `Int64?` | yes |  |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) |
| `Rows` | `VoucherRows[]` | no | [VoucherRows](Accounting.md#Accounting.VoucherRow) |
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
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `AccountsPayable` | `AccountsPayables` | no | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `AccrualAccountingRowId` | `Int64?` | yes | [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow) |
| `VatBookingId` | `Int64?` | yes |  |
| `CorrectionBookingId` | `Int64?` | yes |  |
| `CNSeries` | `String` | no |  |
| `CNNumber` | `String` | no |  |

- `ConnectionType` — None=0, Correction=1, Copy=2
- `ReverseConnectionType` — None=0, Correction=1, Copy=2

**References out:** [AccountingYears](Accounting.md#Accounting.AccountingYear), [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow), [Comments](Common.md#Common.Comment), [VoucherRows](Accounting.md#Accounting.VoucherRow), [Vouchers](Accounting.md#Accounting.Voucher), [VoucherSeries](Accounting.md#Accounting.VoucherSeries)
**Referenced by:** [FixedAssets](Accounting.md#Accounting.FixedAsset), [VoucherRows](Accounting.md#Accounting.VoucherRow), [Vouchers](Accounting.md#Accounting.Voucher)

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

**Referenced by:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Vouchers](Accounting.md#Accounting.Voucher)


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
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) |
| `SetOffAmount` | `Decimal` | no |  |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](Common.md#Common.WriteOffCode) |
| `InterestType` | `Int32?` | yes |  |

- `InterestType` — InterestInvoice=0, NextRegularInvoice=1, None=2

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [WriteOffCodes](Common.md#Common.WriteOffCode)


## Depends on other modules

- [Common](Common.md): [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount), [Comments](Common.md#Common.Comment), [Countries](Common.md#Common.Country), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [Departments](Common.md#Common.Department), [LanguageCodes](Common.md#Common.LanguageCode), [PaymentMethods](Common.md#Common.PaymentMethod), [PaymentTerms](Common.md#Common.PaymentTerm), [VatGroups](Common.md#Common.VatGroup), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse), [WriteOffCodes](Common.md#Common.WriteOffCode)
- [Manufacturing](Manufacturing.md): [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
- [Purchase](Purchase.md): [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [Suppliers](Purchase.md#Purchase.Supplier), [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup)
- [Sales](Sales.md): [Customers](Sales.md#Sales.Customer), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup)
