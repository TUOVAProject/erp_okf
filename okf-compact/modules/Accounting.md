# Accounting

Monitor API module `Accounting`: 41 queryable entities, 0 commands, 2 payload types.

## Queryable entities

<a id="Accounting.AccountingBudgetPeriod"></a>
### AccountingBudgetPeriods

Represents an accounting budget period.

- **Endpoint:** `GET /api/v1/Accounting/AccountingBudgetPeriods`
- **Required permission:** Show budget
- **Introduced in:** 23.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the accounting budget period. |
| `BudgetId` | `Int64` | no | [AccountingBudgets](Accounting.md#Accounting.AccountingBudget) | The business key identifier of the budget the accounting budget period belongs to. |
| `PeriodId` | `Int64` | no | [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod) | The business key identifier of the period the accounting budget period belongs to. |
| `Amount` | `Decimal` | no |  | The amount of the accounting budget period. |
| `Quantity` | `Decimal` | no |  | The quantity of the accounting budget period. |

**References out:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget), [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod)
**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget)

<a id="Accounting.AccountingBudget"></a>
### AccountingBudgets

Represents an accounting budget.

- **Endpoint:** `GET /api/v1/Accounting/AccountingBudgets`
- **Required permission:** Show budget
- **Introduced in:** 23.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the accounting budget. |
| `AccountYearSettingId` | `Int64` | no | [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting) | The business key identifier of the account year setting the budget belongs to. |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) | The business key identifier of the accounting year the budget belongs to. |
| `BalanceId` | `Int64` | no | [Balances](Accounting.md#Accounting.Balance) | The business key identifier of the budget's balance. |
| `BudgetChartId` | `Int64` | no | [BudgetCharts](Accounting.md#Accounting.BudgetChart) | The business key identifier of the budget's budget chart. |
| `BudgetTypeId` | `Int64` | no | [AccountingBudgetTypes](Accounting.md#Accounting.AccountingBudgetType) | The business key identifier of the budget type. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the budget's coding entry. |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The coding entry of the budget. |
| `Periods` | `AccountingBudgetPeriods[]` | no | [AccountingBudgetPeriods](Accounting.md#Accounting.AccountingBudgetPeriod) | The periods of the accounting budget. |

**References out:** [AccountingBudgetPeriods](Accounting.md#Accounting.AccountingBudgetPeriod), [AccountingBudgetTypes](Accounting.md#Accounting.AccountingBudgetType), [AccountingYears](Accounting.md#Accounting.AccountingYear), [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting), [Balances](Accounting.md#Accounting.Balance), [BudgetCharts](Accounting.md#Accounting.BudgetChart), [CodingEntries](Accounting.md#Accounting.CodingEntry)
**Referenced by:** [AccountingBudgetPeriods](Accounting.md#Accounting.AccountingBudgetPeriod)

<a id="Accounting.AccountingBudgetType"></a>
### AccountingBudgetTypes

Represents an accounting budget type.

- **Endpoint:** `GET /api/v1/Accounting/AccountingBudgetTypes`
- **Required permission:** Show basic data for budget
- **Introduced in:** 23.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the accounting budget type. |
| `Number` | `Int64` | no |  | The human readable identifier of the accounting budget type. |
| `Description` | `String` | no |  | The translated description of the accounting budget type. |
| `IsActive` | `Boolean` | no |  | Whether or not the accounting budget type is active. |

**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget)

<a id="Accounting.AccountingYearPeriod"></a>
### AccountingYearPeriods

Represents a accounting year period.

- **Endpoint:** `GET /api/v1/Accounting/AccountingYearPeriods`
- **Required permission:** Show accounting year
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the accounting year period. |
| `FromDate` | `DateTimeOffset?` | yes |  | Period date, from |
| `ToDate` | `DateTimeOffset?` | yes |  | Period date, to |
| `Number` | `Int32?` | yes |  | Period number |
| `Status` | `Int32` | no |  | Status of the period |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) | The business key identifier of the accounting year |
| `AccountingYear` | `AccountingYears` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) | The accounting year of the period. |

- `Status` — Undefined=0, Open=1, Closed=2, Locked=3

**References out:** [AccountingYears](Accounting.md#Accounting.AccountingYear)
**Referenced by:** [AccountingBudgetPeriods](Accounting.md#Accounting.AccountingBudgetPeriod), [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow)

<a id="Accounting.AccountingYear"></a>
### AccountingYears

Represents a accounting year.

- **Endpoint:** `GET /api/v1/Accounting/AccountingYears`
- **Required permission:** Show accounting year
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the accounting year. |
| `ActivePeriodId` | `Int64?` | yes |  | The business key identifier of the active period |
| `Description` | `String` | no |  | The description of the accounting year |
| `Status` | `Int32` | no |  | Status of the accounting year |
| `OpeningBalanceLocked` | `Boolean` | no |  | True if the opening balance is locked |

- `Status` — Active=0, Previous=1, PeriodFinancialStatement=2, Historical=9, Future=-1

**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget), [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod), [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting), [Balances](Accounting.md#Accounting.Balance), [OpeningBalances](Accounting.md#Accounting.OpeningBalance), [Vouchers](Accounting.md#Accounting.Voucher)

<a id="Accounting.Account"></a>
### Accounts

Represents a account.

- **Endpoint:** `GET /api/v1/Accounting/Accounts`
- **Required permission:** Show chart of accounts
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the Account. |
| `Number` | `String` | no |  | The human readable identifier of the account number. |
| `Type` | `Int32` | no |  | The type of account. |

- `Type` — Assets=1, DebtAndOwnCapital=2, Incomes=3, Costs=4, Internal=5, BalanceSheet=6, OutsideBalanceSheet=7, Settlement=8, Wynikowe=9, FixedAssets=10, CurrentAssets=11, Equity=12, Liabilities=13, Other=14

**Referenced by:** [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting), [BankAccounts](Accounting.md#Accounting.BankAccount), [CodingEntries](Accounting.md#Accounting.CodingEntry), [SalesAgreementBases](Sales.md#Sales.SalesAgreementBasis), [SalesAgreements](Sales.md#Sales.SalesAgreement), [VatRates](Common.md#Common.VatRate)

<a id="Accounting.AccountsPayableCashDiscountLevel"></a>
### AccountsPayableCashDiscountLevels

Represents a cash discount level for an accounts payable.

- **Endpoint:** `GET /api/v1/Accounting/AccountsPayableCashDiscountLevels`
- **Required permission:** Show accounts payable
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the cash discount level. |
| `ParentId` | `Int64` | no | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of the accounts payable the cash discount level belongs to. |
| `Discount` | `Decimal?` | yes |  | The discount in percent for the cash discount level. |
| `DiscountDate` | `DateTimeOffset?` | yes |  | The date to which the discount applies. |
| `RowIndex` | `Int32?` | yes |  | The row index of the cash discount level. |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable)

<a id="Accounting.AccountsPayable"></a>
### AccountsPayables

Represents a account's payable.

- **Endpoint:** `GET /api/v1/Accounting/AccountsPayables`
- **Required permission:** Show accounts payable
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the account's payable. |
| `Version` | `Int32` | no |  | The version of the account's payable. |
| `CancelCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the account payable's cancellation comment. |
| `CancelComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The cancellation comment of the account payable. |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](Common.md#Common.PaymentMethod) | The business key identifier of the account payable's payment method. |
| `LanguageId` | `Int64` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The business key identifier of the account payable's language. |
| `Language` | `LanguageCodes` | no | [LanguageCodes](Common.md#Common.LanguageCode) | The language of the account payable. |
| `SuppliersInvoiceNumber` | `String` | no |  | The human readable identifier of the supplier's invoice number. |
| `InvoiceType` | `Int32` | no |  | The invoice type of the accounts payable. |
| `IsCredit` | `Boolean` | no |  | Specifies if the accounts payable is a credit or not. |
| `IsFinalBooked` | `Boolean` | no |  | Specifies if the accounts payable is final booked or not. |
| `PurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder) | The business key identifier of the account payable's purchase order. |
| `WarehouseId` | `Int64` | no | [Warehouses](Common.md#Common.Warehouse) | The business key identifier of the warehouse that the accounts payable belongs to. |
| `PreliminaryBookingDate` | `DateTimeOffset?` | yes |  | The date of the preliminary booking. |
| `VoucherDate` | `DateTimeOffset?` | yes |  | The voucher date of the account payable. |
| `CancelVoucherDate` | `DateTimeOffset?` | yes |  | The voucher cancellation date of the account payable. |
| `SupplierAccountGroupId` | `Int64?` | yes | [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup) | The business key identifier of the supplier account group of the acounts payable. |
| `CountryId` | `Int64` | no | [Countries](Common.md#Common.Country) | The business key identifier of the account payable's country. |
| `Status` | `Int32` | no |  | The status of the accounts payable invoice. |
| `BlockMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) | The block message of the account payable. |
| `OCRNumber` | `String` | no |  | The OCR number of the account payable. |
| `UseOCRNumber` | `Boolean` | no |  | Specifies if OCR number is used. |
| `CreditedAccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of the account payable's credit account payable. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the application user that blocked the entity. |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](Common.md#Common.ApplicationUser) | The application user that blocked the account payable. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  | The date when the entity stops being blocked. |
| `BlockedStatus` | `Int32` | no |  | The block status of the entity. |
| `BlockedContextType` | `Int32` | no |  | Specifies which contexts the block applies for. |
| `HasEimInvoice` | `Boolean` | no |  | Specifies if the account payable has EIM invoice. |
| `HoldEimInvoice` | `Boolean` | no |  | Specifies if the EIM invoice is on hold. |
| `EimInvoiceStatus` | `Int32` | no |  | Specifies the status of the EIM invoice. |
| `InvoiceNumber` | `Int64` | no |  | The invoice number of the accounts payable. |
| `InvoiceDate` | `DateTimeOffset` | no |  | The invoice date on the account payable. |
| `DueDate` | `DateTimeOffset` | no |  | The due date on the account payable. |
| `InvoiceAmount` | `Decimal` | no |  | The invoice amount on the account payable. |
| `InvoiceAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the invoice amount currency. |
| `InvoiceAmountInCompanyCurrency` | `Decimal` | no |  | The invoice amount in the company currency. |
| `InvoiceAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency for the invoice amount. |
| `VatAmount` | `Decimal` | no |  | The VAT amount on the account payable. |
| `VatAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the invoice vat amount currency. |
| `VatAmountInCompanyCurrency` | `Decimal` | no |  | The VAT amount in company currency. |
| `VatAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency for the invoice vat amount. |
| `RestAmount` | `Decimal` | no |  | The rest amount on the account payable. |
| `RestAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the invoice rest amount currency. |
| `RestAmountInCompanyCurrency` | `Decimal` | no |  | The rest amount in company currency. |
| `RestAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the company currency for the invoice rest amount. |
| `OrderedRestAmount` | `Decimal` | no |  | The ordered rest amount on the account payable. |
| `OrderedRestAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the invoice ordered rest amount currency. |
| `CurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency on the account payable. |
| `ExchangeRate` | `Decimal` | no |  | The exchange rate on the account payable. |
| `PaidInFullDate` | `DateTimeOffset?` | yes |  | Specifies the date when the account payable was paid in full. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the account payable's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The internal comment of the account payable. |
| `ReferenceNumber` | `String` | no |  | The human readable reference number on the account payable. |
| `UseFixedDueDate` | `Boolean` | no |  | Specifies if a fixed due date is used. |
| `VatGroupId` | `Int64?` | yes | [VatGroups](Common.md#Common.VatGroup) | The business key identifier of the VAT group that the account payable belongs to. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the payment term of the account payable. |
| `PaymentTerm` | `PaymentTerms` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The payment term of the account payable. |
| `FinalBookingId` | `Int64?` | yes |  | The business key identifier of the account payable's final booking. References Booking. |
| `BusinessContactId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier that the accounts payable belongs to. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the accounts payable's currency exchange type. |
| `Payments` | `OutgoingPayments[]` | no | [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment) | The payments of the accounts payable. |
| `WithholdTaxAmount` | `Decimal?` | yes |  | The withholding tax amount on the account payable. |
| `WithholdTaxAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the withholding tax amount currency. |
| `WithholdTaxAmountInCompanyCurrency` | `Decimal?` | yes |  | The withholding tax in company currency amount on the account payable. |
| `WithholdTaxAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the withholding tax in company currency amount currency. |
| `InputVatDate` | `DateTimeOffset?` | yes |  | The date used to assign the invoice's input VAT to the correct VAT period. Only used in the Polish and Hungarian country packages. |
| `OutputVatDate` | `DateTimeOffset?` | yes |  | The date used to assign the invoice's output VAT to the correct VAT period. Only used in the Polish and Hungarian country packages. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the cash discount level. |
| `ParentId` | `Int64` | no | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) | The business key identifier of the accounts receivable the cash discount level belongs to. |
| `Discount` | `Decimal?` | yes |  | The discount in percent for the cash discount level. |
| `DiscountDate` | `DateTimeOffset?` | yes |  | The date to which the discount applies. |
| `RowIndex` | `Int32?` | yes |  | The row index of the cash discount level. |

**References out:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable)

<a id="Accounting.AccountsReceivable"></a>
### AccountsReceivables

Represents an accounts receivable.

- **Endpoint:** `GET /api/v1/Accounting/AccountsReceivables`
- **Required permission:** Show accounts receivable
- **Introduced in:** 2.44

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the accounts receivable. |
| `Version` | `Int32` | no |  | The version of the accounts receivable. |
| `BookingId` | `Int64?` | yes | [Bookings](Accounting.md#Accounting.Booking) | The business key identifier of the booking that the accounts receivable belongs to. |
| `Booking` | `Bookings` | no | [Bookings](Accounting.md#Accounting.Booking) | The booking that the accounts receivable belongs to. |
| `InvoiceType` | `Int32` | no |  | The invoice type of the accounts receivable. |
| `LatestReminderDate` | `DateTimeOffset?` | yes |  | The latest reminder date of the accounts receivable. |
| `PaymentReminder` | `Boolean` | no |  | Specifies if the accounts receivable has payment reminders. |
| `NumberOfPaymentReminders` | `Int32` | no |  | The number of payment reminders that are left for the accounts receivable. |
| `CollectionDate` | `DateTimeOffset?` | yes |  | The collection date of the accounts receivable. |
| `Collection` | `Boolean` | no |  | Specifies if the accounts receivable has been collected or not. |
| `InterestType` | `Int32` | no |  | The interest type of the accounts receivable. |
| `IsComprehensive` | `Boolean` | no |  | Specifies if the accounts receivable is comprehensive or not. |
| `PartialInvoiceType` | `Int32` | no |  | Specifies how partial invoicing works for the accounts receivable. |
| `CustomerAccountGroupId` | `Int64` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The business key identifier of the customer account group for the accounts receivable. |
| `CustomerAccountGroup` | `CustomerAccountGroups` | no | [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup) | The customer account group of the accounts receivable. |
| `DebitInvoiceId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) | The business key identifier of the debit invoice that the accounts receivable belongs to. |
| `OnAccountIncomingPaymentLedgerId` | `Int64?` | yes |  | The business key identifier of the incoming payment ledger for the accounts receivable. |
| `OnAccountCancelledIncomingPaymentLedgerId` | `Int64?` | yes |  | The business key identifier of the cancelled incoming payment ledger for the accounts receivable. |
| `IsEInvoiceExported` | `Boolean` | no |  | Specifies if an e-invoice has been exported for the accounts receivable. |
| `AccountsReceivableLedgerId` | `Int64?` | yes |  | The business key identifier of the accounts receivable ledger. |
| `CancelledAccountsReceivableLedgerId` | `Int64?` | yes |  | The business key identifier of the cancelled accounts receivable ledger. |
| `Status` | `Int32` | no |  | The status of the accounts receivable. |
| `LatePaymentFee` | `Decimal?` | yes |  | The late payment fee of the accounts receivable in percent. |
| `CancelCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the cancel comment of the accounts receivable. |
| `CancelComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The cancel comment of the accounts receivable. |
| `CancelDate` | `DateTimeOffset` | no |  | The cancel date of the accounts receivable. |
| `CancelBookingId` | `Int64?` | yes | [Bookings](Accounting.md#Accounting.Booking) | The business key identifier of the cancel booking that the accounts receivable belongs to. |
| `CancelBooking` | `Bookings` | no | [Bookings](Accounting.md#Accounting.Booking) | The cancel booking that the accounts receivable belongs to. |
| `BusinessContactId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer that the accounts receivable belongs to. |
| `InvoiceNumber` | `Int64` | no |  | The human readable identifier of the accounts receivable. |
| `InvoiceDate` | `DateTimeOffset` | no |  | The invoice date of the accounts receivable. |
| `DueDate` | `DateTimeOffset` | no |  | The due date of the accounts receivable. |
| `IsCredit` | `Boolean` | no |  | Specifies if the accounts receivable is on credit or not. |
| `InvoiceAmount` | `Decimal` | no |  | The invoice amount of the accounts receivable. |
| `InvoiceAmountCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the accounts receivable’s invoice amount currency. |
| `InvoiceAmountInCompanyCurrency` | `Decimal` | no |  | The invoice amount of the accounts receivable in the company currency. |
| `InvoiceAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the accounts receivable’s invoice amount company currency. |
| `VatAmount` | `Decimal` | no |  | The VAT amount of the accounts receivable. |
| `VatAmountCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the accounts receivable’s VAT amount currency. |
| `VatAmountInCompanyCurrency` | `Decimal` | no |  | The VAT amount of the accounts receivable in the company currency. |
| `VatAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the accounts receivable’s VAT amount company currency. |
| `RestAmount` | `Decimal` | no |  | The rest amount of the accounts receivable. |
| `RestAmountCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the accounts receivable’s rest amount currency. |
| `RestAmountInCompanyCurrency` | `Decimal` | no |  | The rest amount of the accounts receivable in the company currency. |
| `RestAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the accounts receivable’s rest amount company currency. |
| `OrderedRestAmount` | `Decimal` | no |  | The ordered rest amount of the accounts receivable. |
| `OrderedRestAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the accounts receivable’s ordered rest amount currency. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the accounts receivable currency. |
| `ExchangeRate` | `Decimal` | no |  | The exchange rate applicable to the accounts receivable. |
| `PaidInFullDate` | `DateTimeOffset?` | yes |  | Specifies when the accounts receivable was paid in full. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the accounts receivable comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the accounts receivable. |
| `ReferenceNumber` | `String` | no |  | The reference number of the accounts receivable. |
| `UseFixedDueDate` | `Boolean` | no |  | Specifies if the accounts receivable uses a fixed due date. |
| `VatGroupId` | `Int64` | no | [VatGroups](Common.md#Common.VatGroup) | The business key identifier of the VAT group that the accounts receivable belongs to. |
| `PaymentTermId` | `Int64` | no | [PaymentTerms](Common.md#Common.PaymentTerm) | The business key identifier of the payment term that the accounts receivable belongs to. |
| `ChineseVatInvoiceNumber` | `String` | no |  | The Chinese VAT invoice number of the accounts receivable. |
| `ChineseVatInvoiceDate` | `DateTimeOffset?` | yes |  | The Chinese VAT invoice date of the accounts receivable. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType) | The business key identifier of the accounts receivable's currency exchange type. |
| `CTCReportingInvoiceNumber` | `String` | no |  | The invoice number for accounts receivable from CTC reporting system. |
| `CTCReportingReasonForRejection` | `String` | no |  | The reason for rejection accounts receivable in CTC reporting system. |
| `CTCReportingStatus` | `Int32?` | yes |  | The accounts receivable's status from CTC reporting system. |
| `CTCReportingInvoiceDate` | `DateTimeOffset?` | yes |  | The accounts receivable's invoice date from CTC reporting system. |
| `CTCReportingIdentifier` | `String` | no |  | The accounts receivable's identifier from CTC reporting system. |
| `CTCReportingElectronicConfirmationURL` | `String` | no |  | The official electronic confirmation URL of receipt from CTC reporting system. |
| `CTCReportingElectronicConfirmationNumber` | `String` | no |  | The official electronic confirmation number of receipt from CTC reporting system. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the Account year setting coding dimension availability. |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](Accounting.md#Accounting.CodingDimension) | The business key identifier of the coding dimension. |
| `CodingDimension` | `CodingDimensions` | no | [CodingDimensions](Accounting.md#Accounting.CodingDimension) | The coding dimension. |
| `CodingDimensionAvailability` | `Int32` | no |  | The coding dimension availability state. |
| `AccountYearSettingId` | `Int64` | no | [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting) | The business key identifier of the account year setting. |

- `CodingDimensionAvailability` — NotAllowed=0, Allowed=1, Mandatory=2

**References out:** [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting), [CodingDimensions](Accounting.md#Accounting.CodingDimension)
**Referenced by:** [AccountYearSettings](Accounting.md#Accounting.AccountYearSetting)

<a id="Accounting.AccountYearSetting"></a>
### AccountYearSettings

Represents a account setting on a specific year.

- **Endpoint:** `GET /api/v1/Accounting/AccountYearSettings`
- **Required permission:** Show accounting year
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the account year setting. |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) | The business key identifier of accounting year. |
| `Description` | `String` | no |  | The description of the account year setting. |
| `AllowSpecification` | `Boolean` | no |  | Specifies if the account year setting allows specification to be used. |
| `AllowQuantity` | `Boolean` | no |  | Specifies if the account year setting allows quantity to be used. |
| `IsCurrencyAccount` | `Boolean` | no |  | Specifies if the account year setting is a currency account. |
| `CurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency if used. |
| `IsAccrual` | `Boolean` | no |  | Specifies if the account year setting is accrual. |
| `DebitOrCreditType` | `Int32` | no |  | Specifies if the account year setting is of debit or credit type. |
| `VatType` | `Int32` | no |  | The vat type on the account year setting. |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) | The business key identifier of the vat rate. |
| `BlockedForManualCoding` | `Boolean` | no |  | Specifies if the account year setting is block for manual coding. |
| `IsFixedAssetAccount` | `Boolean` | no |  | Specifies if the account year setting is a fixed asset account. |
| `IncludeOrderNumberInCoding` | `Boolean` | no |  | Specifies if the account year setting should include ordernumber in coding. |
| `AccountId` | `Int64` | no | [Accounts](Accounting.md#Accounting.Account) | The business key identifier of the account. |
| `Account` | `Accounts` | no | [Accounts](Accounting.md#Accounting.Account) | The account of the account year setting. |
| `AccountCodingDimensions` | `AccountYearSettingCodingDimensionAvailabilities[]` | no | [AccountYearSettingCodingDimensionAvailabilities](Accounting.md#Accounting.AccountYearSettingCodingDimensionAvailability) | The account coding dimensions of the account year setting. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the accrual accounting ledger. |
| `Number` | `Int64` | no |  | The number of the accrual accounting ledger. |
| `ApprovedDate` | `DateTimeOffset?` | yes |  | When the accrual accounting ledger was approved. |

**Referenced by:** [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow)

<a id="Accounting.AccrualAccountingRow"></a>
### AccrualAccountingRows

Represents a accrual accounting row.

- **Endpoint:** `GET /api/v1/Accounting/AccrualAccountingRows`
- **Required permission:** Show accrual
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the accounting row. |
| `PeriodId` | `Int64` | no | [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod) | The business key identifier of the accrual accounting row's accounting year period. |
| `Period` | `AccountingYearPeriods` | no | [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod) | The accounting year period on the accrual accounting row. |
| `PeriodAmountInCompanyCurrency` | `Decimal` | no |  | Amount in company currency |
| `AccrualAccountingId` | `Int64` | no |  | The business key identifier of the accrual accounting. |
| `IsReleased` | `Boolean` | no |  | Specifies if the accrual accounting is released. |
| `LedgerId` | `Int64?` | yes | [AccrualAccountingLedgers](Accounting.md#Accounting.AccrualAccountingLedger) | The business key identifier of the accrual accounting row's ledger. |
| `Ledger` | `AccrualAccountingLedgers` | no | [AccrualAccountingLedgers](Accounting.md#Accounting.AccrualAccountingLedger) | The accrual accounting ledger. |
| `BookingId` | `Int64?` | yes |  | The business key identifier of the booking. |
| `RowIndex` | `Int32` | no |  | The row index of the accrual accounting. |
| `BookingRows` | `BookingRows[]` | no | [BookingRows](Accounting.md#Accounting.BookingRow) | Booking rows on the accrual accounting. |

**References out:** [AccountingYearPeriods](Accounting.md#Accounting.AccountingYearPeriod), [AccrualAccountingLedgers](Accounting.md#Accounting.AccrualAccountingLedger), [BookingRows](Accounting.md#Accounting.BookingRow)
**Referenced by:** [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting), [Vouchers](Accounting.md#Accounting.Voucher)

<a id="Accounting.AccrualAccounting"></a>
### AccrualAccountings

Represents a accrual accounting.

- **Endpoint:** `GET /api/v1/Accounting/AccrualAccountings`
- **Required permission:** Show accrual
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the accrual accounting. |
| `Number` | `String` | no |  | The human readable number on the accrual accounting. |
| `Text` | `String` | no |  | The human readable text on the accrual accounting. |
| `Type` | `Int32` | no |  | Type of accrual accounting. |
| `StartDate` | `DateTimeOffset?` | yes |  | Start date of the accrual accounting. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of the accounts payable. |
| `AccountsPayableBookingRowId` | `Int64?` | yes |  | The business key identifier of the accounts payable booking row. |
| `VoucherId` | `Int64?` | yes |  | The business key identifier of the voucher. |
| `VoucherRowId` | `Int64?` | yes |  | The business key identifier of the voucher row. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the accrual accounting comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment on the accrual accounting. |
| `CancelCommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the accrual accounting cancellation comment. |
| `CancelComment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The cancellation comment on the accrual accounting. |
| `IsCancelled` | `Boolean` | no |  | Specifies if the accrual accounting is cancelled. |
| `BookingId` | `Int64` | no |  | The business key identifier of the booking. |
| `Rows` | `AccrualAccountingRows[]` | no | [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow) | The accrual accounting rows. |
| `BookingRows` | `BookingRows[]` | no | [BookingRows](Accounting.md#Accounting.BookingRow) | The booking rows on the accrual accounting. |
| `AccountsPayableBookingRow` | `BookingRows` | no | [BookingRows](Accounting.md#Accounting.BookingRow) | The booking row of the accrual accounting's account payable. |

- `Type` — AccountsPayableBookingRow=1, VoucherRow=2, ReverseVoucher=3, FreeBooking=4, SalesAgreement=5, SupplierAgreement=6

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow), [BookingRows](Accounting.md#Accounting.BookingRow), [Comments](Common.md#Common.Comment)
**Referenced by:** [BookingRows](Accounting.md#Accounting.BookingRow), [VoucherRows](Accounting.md#Accounting.VoucherRow)

<a id="Accounting.AllocationKeyResultRow"></a>
### AllocationKeyResultRows

Represent an allocation key result row.

- **Endpoint:** `GET /api/v1/Accounting/AllocationKeyResultRows`
- **Required permission:** Show allocation keys
- **Introduced in:** 24.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the allocation key result row. |
| `AllocationKeyId` | `Int64` | no | [AllocationKeys](Accounting.md#Accounting.AllocationKey) | The business key identifier of the allocation key the result row belongs to. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry of the allocation key result row. |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The coding entry of the allocation key result row. |
| `Percentage` | `Decimal` | no |  | The percentage value of the allocation key result row. |
| `RowIndex` | `Int32` | no |  | The row index of the allocation key result row. |

**References out:** [AllocationKeys](Accounting.md#Accounting.AllocationKey), [CodingEntries](Accounting.md#Accounting.CodingEntry)
**Referenced by:** [AllocationKeys](Accounting.md#Accounting.AllocationKey)

<a id="Accounting.AllocationKey"></a>
### AllocationKeys

Represent an allocation key.

- **Endpoint:** `GET /api/v1/Accounting/AllocationKeys`
- **Required permission:** Show allocation keys
- **Introduced in:** 24.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the allocation key. |
| `Number` | `Int64` | no |  | The human readable identifier of the allocation key. |
| `Name` | `String` | no |  | The name of the allocation key. |
| `AllocationKeyResultRow` | `AllocationKeyResultRows[]` | no | [AllocationKeyResultRows](Accounting.md#Accounting.AllocationKeyResultRow) | The result rows of the allocation key. |

**References out:** [AllocationKeyResultRows](Accounting.md#Accounting.AllocationKeyResultRow)
**Referenced by:** [AllocationKeyResultRows](Accounting.md#Accounting.AllocationKeyResultRow), [AutoAllocations](Accounting.md#Accounting.AutoAllocation)

<a id="Accounting.AutoAllocation"></a>
### AutoAllocations

Represent an auto allocation.

- **Endpoint:** `GET /api/v1/Accounting/AutoAllocations`
- **Required permission:** Show automatic allocations
- **Introduced in:** 24.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the auto allocation. |
| `Number` | `String` | no |  | The human readable identifier of the auto allocation. |
| `Description` | `String` | no |  | The description of the auto allocation. |
| `Type` | `Int32` | no |  | The type of the auto allocation |
| `Active` | `Boolean` | no |  | Specifies whether the auto allocation is active or not. |
| `AllocationKeyId` | `Int64?` | yes | [AllocationKeys](Accounting.md#Accounting.AllocationKey) | The business key identifier of the allocation key linked to the auto allocation. |
| `AllocationKey` | `AllocationKeys` | no | [AllocationKeys](Accounting.md#Accounting.AllocationKey) | The allocation key linked to the auto allocation. |
| `AccountFrom` | `String` | no |  | The account number from which the auto allocation applies. |
| `AccountTo` | `String` | no |  | The account number to which the auto allocation applies. |

- `Type` — Direct=0, PeriodBalance=1, AccumulatedBalance=2

**References out:** [AllocationKeys](Accounting.md#Accounting.AllocationKey)

<a id="Accounting.BalanceRowDay"></a>
### BalanceRowDays

Represents a balance row day.

- **Endpoint:** `GET /api/v1/Accounting/BalanceRowDays`
- **Required permission:** Show balance information
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the balance row day. |
| `BalanceId` | `Int64` | no | [Balances](Accounting.md#Accounting.Balance) | The business key identifier of the balance the balance row day belongs to. |
| `Credit` | `Decimal` | no |  | The credit amount in the account's currency. |
| `CreditInCompanyCurrency` | `Decimal` | no |  | The credit amount in company currency. |
| `Date` | `DateTimeOffset` | no |  | The date of the balance row day. |
| `Debit` | `Decimal` | no |  | The debit amount in the account's currency. |
| `DebitInCompanyCurrency` | `Decimal` | no |  | The debit amount in company currency. |
| `PeriodNumber` | `Int32` | no |  | The period number for the balance row day's date. |
| `Quantity` | `Decimal` | no |  | The recorded quantity of the balance row day. |

**References out:** [Balances](Accounting.md#Accounting.Balance)

<a id="Accounting.Balance"></a>
### Balances

Represents a balance.

- **Endpoint:** `GET /api/v1/Accounting/Balances`
- **Required permission:** Show balance information
- **Introduced in:** 22.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the balance. |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) | The business key identifier of the accounting year the balance belongs to. |
| `Amount` | `Decimal` | no |  | The balance amount in the account's currency. |
| `AmountInCompanyCurrency` | `Decimal` | no |  | The balance amount in company currency. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry the balance belongs to. |
| `OpeningBalanceId` | `Int64?` | yes | [OpeningBalances](Accounting.md#Accounting.OpeningBalance) | The business key identifier of the opening balance for the balance. |
| `Quantity` | `Decimal` | no |  | The recorded quantity of the balance. |

**References out:** [AccountingYears](Accounting.md#Accounting.AccountingYear), [CodingEntries](Accounting.md#Accounting.CodingEntry), [OpeningBalances](Accounting.md#Accounting.OpeningBalance)
**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget), [BalanceRowDays](Accounting.md#Accounting.BalanceRowDay), [VoucherRows](Accounting.md#Accounting.VoucherRow)

<a id="Accounting.BankAccount"></a>
### BankAccounts

Represents a bank account.

- **Endpoint:** `GET /api/v1/Accounting/BankAccounts`
- **Required permission:** Show bank settings
- **Introduced in:** 24.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the bank account. |
| `Code` | `String` | no |  | The human readable identifier of the bank account. |
| `Description` | `String` | no |  | The translated description of the bank account. |
| `Type` | `Int32` | no |  | The bank account's type. |
| `Number` | `String` | no |  | The bank account's number. |
| `BgNumber` | `String` | no |  | The bank account's bankgiro number. |
| `PgNumber` | `String` | no |  | The bank account's plusgiro number. |
| `BankIdentifierCode` | `String` | no |  | The bank account's bank identifier code. |
| `CurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the bank account's currency. |
| `AccountingAccountId` | `Int64` | no | [Accounts](Accounting.md#Accounting.Account) | The business key identifier of the bank account's accounting account. |
| `BankAddressId` | `Int64` | no | [Addresses](Common.md#Common.Address) | The business key identifier of the bank account's bank address. |

- `Type` — Iban=1, Bban=2, Upic=3, Miscellaneous=4

**References out:** [Accounts](Accounting.md#Accounting.Account), [Addresses](Common.md#Common.Address), [Currencies](Common.md#Common.Currency)
**Referenced by:** [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment)

<a id="Accounting.BookingRow"></a>
### BookingRows

Represents a booking row.

- **Endpoint:** `GET /api/v1/Accounting/BookingRows`
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the booking row. |
| `Type` | `Int32` | no |  | The type of booking row. |
| `AuthorizedWhen` | `DateTimeOffset?` | yes |  | When the booking row was authorized. Property is obsolete, it gives last value from new list of row authorizations _(Now returns AuthorizedWhen from last row authorization)_ |
| `PurchaseOrderDeliveryRowId` | `Int64?` | yes | [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow) | The business key identifier of the booking rows purchase order delivery row. |
| `BookingId` | `Int64` | no | [Bookings](Accounting.md#Accounting.Booking) | The business key identifier of the booking. |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) | The business key identifier of the row's VAT rate. |
| `AccrualAccountingId` | `Int64?` | yes | [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting) | The business key identifier of the accrual accounting. |
| `OrderNumber` | `String` | no |  | The human readable identifier of the order number |
| `DebitInCompanyCurrency` | `Decimal` | no |  | Debit in the company currency. |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the debit in the company currency. |
| `CreditInCompanyCurrency` | `Decimal` | no |  | Credit in the company currency. |
| `CreditInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the credit in the company currency. |
| `Debit` | `Decimal` | no |  | Debit on the booking row. |
| `DebitCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the debit currency. |
| `Credit` | `Decimal` | no |  | Credit on the booking row. |
| `CreditCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the credit currency. |
| `Quantity` | `Decimal` | no |  | Quantity on the booking row. |
| `RowIndex` | `Int32` | no |  | Row index of the booking row. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry. |
| `NetAmountBookingRowId` | `Int64?` | yes | [BookingRows](Accounting.md#Accounting.BookingRow) | The business key identifier of the net amount row that the VAT row belongs to. |

- `Type` — NotInitialized=0, AccountsReceivable=1, OutputVat=2, AccountsPayable=3, PreliminaryAccountsPayable=4, PaymentIn=5, PaymentOut=6, Purchase=7, Sales=8, Miscellaneous=9, PurchaseWithoutOrder=10, InvoicingCharges=11, InsuranceCost=12, RoundOff=13, SetupPrice=14, Material=15, Inventory=16, PreliminaryAccount=17, InputVat=18, ExchangeRateAdjustment=19, InvoiceReminderFee=20, PriceDifference=21, PaymentInVat=22, PaymentOutVat=23, OtherPayment=24, InputVatNonDeductible=25, CurrencyDifference=26, WithholdingTax=27, ManualAccountsPayableFinalBookingFromG4=999

**References out:** [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting), [BookingRows](Accounting.md#Accounting.BookingRow), [Bookings](Accounting.md#Accounting.Booking), [CodingEntries](Accounting.md#Accounting.CodingEntry), [Currencies](Common.md#Common.Currency), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [VatRates](Common.md#Common.VatRate)
**Referenced by:** [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow), [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting), [BookingRows](Accounting.md#Accounting.BookingRow), [Bookings](Accounting.md#Accounting.Booking)

<a id="Accounting.Booking"></a>
### Bookings

Represents a booking.

- **Endpoint:** `GET /api/v1/Accounting/Bookings`
- **Introduced in:** 2.44

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the booking. |
| `ParentClass` | `Guid` | no |  | The GUID of the booking’s owner type. |
| `ParentId` | `Int64` | no |  | The business key identifier of the booking owner. |
| `Rows` | `BookingRows[]` | no | [BookingRows](Accounting.md#Accounting.BookingRow) | The rows that belong to the booking. |

**References out:** [BookingRows](Accounting.md#Accounting.BookingRow)
**Referenced by:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [BookingRows](Accounting.md#Accounting.BookingRow), [FixedAssetSales](Accounting.md#Accounting.FixedAssetSale), [IncomingPayments](Accounting.md#Accounting.IncomingPayment), [OutgoingPayments](Accounting.md#Accounting.OutgoingPayment)

<a id="Accounting.BudgetChart"></a>
### BudgetCharts

Represents a budget chart.

- **Endpoint:** `GET /api/v1/Accounting/BudgetCharts`
- **Required permission:** Show basic data for budget
- **Introduced in:** 23.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the budget chart. |
| `Code` | `String` | no |  | The human readable identifier of the budget chart. |
| `Description` | `String` | no |  | The translated description of the budget chart. |

**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget)

<a id="Accounting.CodingDimension"></a>
### CodingDimensions

Represents a Coding dimension.

- **Endpoint:** `GET /api/v1/Accounting/CodingDimensions`
- **Required permission:** Show dimensions/dimension codes
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the coding dimension. |
| `Number` | `Int32` | no |  | The number of the coding dimension. |
| `Description` | `String` | no |  | The description of the coding dimension. |
| `CodeDescription` | `String` | no |  | The description of the coding dimension code. |
| `ReferenceEntityType` | `Int32` | no |  | The coding dimension reference type of the coding dimension. |
| `CodingElements` | `CodingElements[]` | no | [CodingElements](Accounting.md#Accounting.CodingElement) | The coding elements of the coding dimension. |

- `ReferenceEntityType` — None=0, Project=1, ProductGroup=2, PartCode=3, Part=4, Department=5, WorkCenter=6, CustomerRootFromOrder=7, CustomerRootFromInvoice=8, SupplierRoot=9, Person=10, CustomerAccountGroupOnCustomer=11, CustomerDistrict=12, CustomerType=13, SupplierAccountGroupOnSupplier=14, SupplierDistrict=15, SupplierType=16

**References out:** [CodingElements](Accounting.md#Accounting.CodingElement)
**Referenced by:** [AccountYearSettingCodingDimensionAvailabilities](Accounting.md#Accounting.AccountYearSettingCodingDimensionAvailability), [CodingElements](Accounting.md#Accounting.CodingElement), [CodingEntryElements](Accounting.md#Accounting.CodingEntryElement)

<a id="Accounting.CodingElement"></a>
### CodingElements

Represents a Coding element.

- **Endpoint:** `GET /api/v1/Accounting/CodingElements`
- **Required permission:** Show dimensions/dimension codes
- **Introduced in:** 2.27

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the coding element. |
| `Code` | `String` | no |  | The human readable coding element code. |
| `Description` | `String` | no |  | The description of the coding element. |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](Accounting.md#Accounting.CodingDimension) | The business key identifier of the coding element. |
| `IsActive` | `Boolean` | no |  | Specifies if the coding element is active. |

**References out:** [CodingDimensions](Accounting.md#Accounting.CodingDimension)
**Referenced by:** [CodingDimensions](Accounting.md#Accounting.CodingDimension), [CodingEntryElements](Accounting.md#Accounting.CodingEntryElement)

<a id="Accounting.CodingEntry"></a>
### CodingEntries

Represents a coding entry.

- **Endpoint:** `GET /api/v1/Accounting/CodingEntries`
- **Required permission:** Show dimensions/dimension codes
- **Introduced in:** 2.30

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the coding entry. |
| `CodingEntryDescription` | `String` | no |  | The description of the coding entry. |
| `AccountId` | `Int64?` | yes | [Accounts](Accounting.md#Accounting.Account) | The business key identifier of the coding entry's account. |
| `Account` | `Accounts` | no | [Accounts](Accounting.md#Accounting.Account) | The account of the coding entry. |
| `CodingEntryElements` | `CodingEntryElements[]` | no | [CodingEntryElements](Accounting.md#Accounting.CodingEntryElement) | The coding entry elements of the coding entry. |

**References out:** [Accounts](Accounting.md#Accounting.Account), [CodingEntryElements](Accounting.md#Accounting.CodingEntryElement)
**Referenced by:** [AccountingBudgets](Accounting.md#Accounting.AccountingBudget), [AllocationKeyResultRows](Accounting.md#Accounting.AllocationKeyResultRow), [Balances](Accounting.md#Accounting.Balance), [BookingRows](Accounting.md#Accounting.BookingRow), [CodingEntryElements](Accounting.md#Accounting.CodingEntryElement), [CodingRows](Accounting.md#Accounting.CodingRow), [CustomerOrderPaymentPlanRows](Sales.md#Sales.CustomerOrderPaymentPlanRow), [OpeningBalances](Accounting.md#Accounting.OpeningBalance), [PaymentMethods](Common.md#Common.PaymentMethod), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [StandardAccounts](Accounting.md#Accounting.StandardAccount), [SupplierAccounts](Purchase.md#Purchase.SupplierAccount), [Suppliers](Purchase.md#Purchase.Supplier), [VoucherRows](Accounting.md#Accounting.VoucherRow), [WriteOffCodes](Common.md#Common.WriteOffCode)

<a id="Accounting.CodingEntryElement"></a>
### CodingEntryElements

Represents a coding entry element.

- **Endpoint:** `GET /api/v1/Accounting/CodingEntryElements`
- **Required permission:** Show dimensions/dimension codes
- **Introduced in:** 2.30

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the coding entry element. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry that the element belongs to. |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](Accounting.md#Accounting.CodingDimension) | The business key identifier of the element's coding dimension. |
| `CodingDimension` | `CodingDimensions` | no | [CodingDimensions](Accounting.md#Accounting.CodingDimension) | The coding dimension of the coding entry element. |
| `ReferencingEntityId` | `Int64?` | yes | [CodingElements](Accounting.md#Accounting.CodingElement) | The business key identifier of the referencing entity. References an entity of type according to the coding dimension's ReferenceEntityType, or CodingElements if None. |

**References out:** [CodingDimensions](Accounting.md#Accounting.CodingDimension), [CodingElements](Accounting.md#Accounting.CodingElement), [CodingEntries](Accounting.md#Accounting.CodingEntry)
**Referenced by:** [CodingEntries](Accounting.md#Accounting.CodingEntry)

<a id="Accounting.CodingRow"></a>
### CodingRows

Represents a coding row.

- **Endpoint:** `GET /api/v1/Accounting/CodingRows`
- **Introduced in:** 2.30

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the coding row. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding row's coding entry. |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The coding entry of the coding row. |
| `Type` | `Int32` | no |  | The type of the coding row. |

- `Type` — Standard=1, Setup=2, Material=3, Inventory=4, PriceDifference=5, Cost=6

**References out:** [CodingEntries](Accounting.md#Accounting.CodingEntry)
**Referenced by:** [Codings](Accounting.md#Accounting.Coding)

<a id="Accounting.Coding"></a>
### Codings

Represents a coding.

- **Endpoint:** `GET /api/v1/Accounting/Codings`
- **Introduced in:** 2.30

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the coding. |
| `CodingRows` | `CodingRows[]` | no | [CodingRows](Accounting.md#Accounting.CodingRow) | The coding rows belonging to the coding. |

**References out:** [CodingRows](Accounting.md#Accounting.CodingRow)
**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [InquiryRows](Purchase.md#Purchase.InquiryRow), [PurchaseOrderInvoiceRows](Purchase.md#Purchase.PurchaseOrderInvoiceRow), [PurchaseOrderRows](Purchase.md#Purchase.PurchaseOrderRow), [QuoteRows](Sales.md#Sales.QuoteRow), [SalesAgreementRows](Sales.md#Sales.SalesAgreementRow)

<a id="Accounting.FixedAssetDepreciation"></a>
### FixedAssetDepreciations

Represents a depreciation for a fixed assets object.

- **Endpoint:** `GET /api/v1/Accounting/FixedAssetDepreciations`
- **Required permission:** Show depreciation
- **Introduced in:** 23.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the depreciation. |
| `Amount` | `Decimal` | no |  | The amount of the depreciation. |
| `DepreciationDate` | `DateTimeOffset` | no |  | The depreciation date of the depreciation. |
| `VoucherDate` | `DateTimeOffset` | no |  | The voucher date of the depreciation. |
| `VoucherText` | `String` | no |  | The voucher date of the depreciation. |
| `ParentId` | `Int64` | no | [FixedAssets](Accounting.md#Accounting.FixedAsset) | The fixed assets object to which the depreciation belongs. |

**References out:** [FixedAssets](Accounting.md#Accounting.FixedAsset)

<a id="Accounting.FixedAssetGroup"></a>
### FixedAssetGroups

Represents a fixed assets group.

- **Endpoint:** `GET /api/v1/Accounting/FixedAssetGroups`
- **Required permission:** Show basic data for fixed assets register
- **Introduced in:** 23.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the fixed assets group. |
| `Code` | `String` | no |  | The human readable identifier of the fixed assets group. |

**Referenced by:** [FixedAssets](Accounting.md#Accounting.FixedAsset)

<a id="Accounting.FixedAsset"></a>
### FixedAssets

Represents a fixed assets object.

- **Endpoint:** `GET /api/v1/Accounting/FixedAssets`
- **Required permission:** Show fixed assets objects
- **Introduced in:** 23.5

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the fixed assets object. |
| `Code` | `String` | no |  | The human readable identifier of the fixed assets object. |
| `Description` | `String` | no |  | The translated description of the fixed assets object. |
| `GroupId` | `Int64` | no | [FixedAssetGroups](Accounting.md#Accounting.FixedAssetGroup) | The business key identifier of fixed assets group that the fixed assets object belongs to. |
| `Group` | `FixedAssetGroups` | no | [FixedAssetGroups](Accounting.md#Accounting.FixedAssetGroup) | The fixed assets group that the fixed assets object belongs to. |
| `AcquisitionDate` | `DateTimeOffset` | no |  | The acquisition date of the fixed assets object. |
| `AcquisitionValue` | `Decimal` | no |  | The acquisition value in company currency of the fixed assets object. |
| `Quantity` | `Decimal` | no |  | The quantity of the fixed assets object. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of the accounts payable connected to the fixed assets object. |
| `VoucherId` | `Int64?` | yes | [Vouchers](Accounting.md#Accounting.Voucher) | The business key identifier of the voucher connected to the fixed assets object. |
| `SupplierId` | `Int64?` | yes | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the supplier connected to the fixed assets object. |
| `CategoryString` | `String` | no |  | The category string of the fixed assets object. |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier of the work center of the fixed assets object. |
| `DepartmentId` | `Int64?` | yes | [Departments](Common.md#Common.Department) | The business key identifier of the department of the fixed assets object. |
| `SerialNumber` | `String` | no |  | The serial number of the fixed assets object. |
| `Location` | `String` | no |  | The location of the fixed assets object. |
| `PlannedDepreciationStartDate` | `DateTimeOffset` | no |  | The start date for the scheduled depreciation of the fixed assets object. |
| `PlannedDepreciationTimeInYears` | `Decimal` | no |  | The time (in years) for the scheduled depreciation of the fixed assets object. |
| `PlannedDepreciationPercentage` | `Decimal` | no |  | The percentage for the scheduled depreciation of the fixed assets object. |
| `CalculatedDepreciationStartDate` | `DateTimeOffset` | no |  | The start date for the calculated depreciation of the fixed assets object. |
| `CalculatedDepreciationPercentage` | `Decimal` | no |  | The depreciation percentage for the calculated depreciation of the fixed assets object. |
| `MinimumValue` | `Decimal` | no |  | The minimal value to depreciate the fixed assets object to. |
| `Sales` | `FixedAssetSales[]` | no | [FixedAssetSales](Accounting.md#Accounting.FixedAssetSale) | The registered sales/retirements of the fixed assets object. |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [Departments](Common.md#Common.Department), [FixedAssetGroups](Accounting.md#Accounting.FixedAssetGroup), [FixedAssetSales](Accounting.md#Accounting.FixedAssetSale), [Suppliers](Purchase.md#Purchase.Supplier), [Vouchers](Accounting.md#Accounting.Voucher), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [CustomerOrderRows](Sales.md#Sales.CustomerOrderRow), [FixedAssetDepreciations](Accounting.md#Accounting.FixedAssetDepreciation)

<a id="Accounting.FixedAssetSale"></a>
### FixedAssetSales

Represents a sale/retirement of a fixed assets object.

- **Endpoint:** `GET /api/v1/Accounting/FixedAssetSales`
- **Required permission:** Show fixed assets objects
- **Introduced in:** 23.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the fixed asset sale. |
| `SalesDate` | `DateTimeOffset` | no |  | The sales date of the fixed asset sale. |
| `Type` | `Int32` | no |  | The type of fixed asset sale. |
| `Quantity` | `Decimal` | no |  | The sold quantity of the fixed assets object. |
| `PartOfAcquisitionValue` | `Decimal` | no |  | The sold part of the fixed assets object's acquisition value. |
| `SalesValue` | `Decimal` | no |  | The sales value of the fixed asset sale. |
| `SalesProfit` | `Decimal?` | yes |  | The profit of the fixed asset sale. |
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) | The business key identifier of the accounts receivable linked to the fixed asset sale. |
| `CustomerId` | `Int64?` | yes | [Customers](Sales.md#Sales.Customer) | The business key identifier of the customer linked to the fixed asset sale. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the comment to the fixed asset sale. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment to the fixed asset sale. |
| `VoucherText` | `String` | no |  | The voucher text of the fixed asset sale. |
| `SalesTimestamp` | `DateTimeOffset` | no |  | The timestamp of the fixed asset sale. |
| `BookingId` | `Int64?` | yes | [Bookings](Accounting.md#Accounting.Booking) | The business key identifier of the booking of the fixed asset sale. |

- `Type` — Sale=0, Retirement=1

**References out:** [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [Bookings](Accounting.md#Accounting.Booking), [Comments](Common.md#Common.Comment), [Customers](Sales.md#Sales.Customer)
**Referenced by:** [FixedAssets](Accounting.md#Accounting.FixedAsset)

<a id="Accounting.IncomingPayment"></a>
### IncomingPayments

Represents an incoming payment.

- **Endpoint:** `GET /api/v1/Accounting/IncomingPayments`
- **Required permission:** Show accounts receivable
- **Introduced in:** 22.8

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the incoming payment. |
| `BankChargeAmount` | `Decimal?` | yes |  | The bank charge amount of the incoming payment. |
| `BankChargeAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the bank charge amount's currency. |
| `BookingId` | `Int64?` | yes | [Bookings](Accounting.md#Accounting.Booking) | The business key identifier of the incoming payment's booking. |
| `CancelDate` | `DateTimeOffset?` | yes |  | The date the payment was cancelled. _(Replaced by CancelTimeStamp)_ |
| `CancelTimeStamp` | `DateTimeOffset?` | yes |  | The timestamp when the payment was cancelled. |
| `CancelledByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the user that cancelled the payment. |
| `CancelPaymentDate` | `DateTimeOffset` | no |  | The date the cancellation is booked. |
| `CreationDate` | `DateTimeOffset` | no |  | The date the incoming payment was created. |
| `CurrencyExchangeRate` | `Decimal` | no |  | The exchange rate of the incoming payment. |
| `InterestType` | `Int32` | no |  | The interest type of the incoming payment. |
| `IsCancelled` | `Boolean` | no |  | Whether or not the payment is cancelled. |
| `PaidAmount` | `Decimal` | no |  | The paid amount. |
| `PaidAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the paid amount's currency. |
| `PaidAmountInCompanyCurrency` | `Decimal` | no |  | The paid amount in company currency. |
| `PaidAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the paid amount in company currency's currency. |
| `PaidVatAmount` | `Decimal?` | yes |  | The paid VAT amount. |
| `PaidVatAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the paid VAT amount's currency. |
| `ParentId` | `Int64` | no | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) | The business key identifier of the paid accounts receivable. |
| `PaymentDate` | `DateTimeOffset` | no |  | The payment date. |
| `PaymentMethodId` | `Int64?` | yes | [PaymentMethods](Common.md#Common.PaymentMethod) | The business key identifier of the payment method. |
| `VoucherText` | `String` | no |  | The voucher text of the incoming payment. |
| `WriteOffAmount` | `Decimal?` | yes |  | The amount written off for the incoming payment. |
| `WriteOffAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency of the amount written off. |
| `WriteOffAmountInCompanyCurrency` | `Decimal?` | yes |  | The amount written off in company currency for the incoming payment. |
| `WriteOffAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency of the amount written off in company currency for the incoming payment. |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](Common.md#Common.WriteOffCode) | The business key identifier of the incoming payment's write off code. |
| `InterestInvoicingStatus` | `Int32` | no |  | The interest invoicing status of the incoming payment. |
| `IsSetOffPayment` | `Boolean` | no |  | Specifies if the incoming payment is a set off payment. |
| `LedgerId` | `Int64?` | yes |  | The business key identifier of the incoming payment ledger. References IncomingPaymentLedger. |
| `ChequeNumber` | `String` | no |  | The cheque number of the incoming payment. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the opening balance. |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) | The business key identifier of the accounting year the opening balance belongs to. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry the opening balance belongs to. |
| `Credit` | `Decimal` | no |  | The credit amount of the opening balance. |
| `CreditCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency of the credit amount. |
| `CreditInCompanyCurrency` | `Decimal` | no |  | The credit amount in company currency of the opening balance. |
| `CreditInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency of the credit amount in company currency. |
| `Debit` | `Decimal` | no |  | The debit amount of the opening balance. |
| `DebitCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency of the debit amount. |
| `DebitInCompanyCurrency` | `Decimal` | no |  | The debit amount in company currency of the opening balance. |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the currency of the debit amount in company currency. |
| `ExchangeRate` | `Decimal` | no |  | The exchange rate on the opening balance. |
| `Quantity` | `Decimal` | no |  | The recorded quantity of the opening balance. |

**References out:** [AccountingYears](Accounting.md#Accounting.AccountingYear), [CodingEntries](Accounting.md#Accounting.CodingEntry), [Currencies](Common.md#Common.Currency)
**Referenced by:** [Balances](Accounting.md#Accounting.Balance)

<a id="Accounting.OutgoingPayment"></a>
### OutgoingPayments

Represents an outgoing payment.

- **Endpoint:** `GET /api/v1/Accounting/OutgoingPayments`
- **Required permission:** Show accounts payable
- **Introduced in:** 24.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the outgoing payment. |
| `AccountsPayableId` | `Int64` | no | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of the paid accounts payable. |
| `SupplierId` | `Int64` | no | [Suppliers](Purchase.md#Purchase.Supplier) | The business key identifier of the paid supplier. |
| `CreationDate` | `DateTimeOffset` | no |  | The creation date of the outgoing payment. |
| `PaymentDate` | `DateTimeOffset` | no |  | The payment date of the outgoing payment. |
| `PaymentMethodId` | `Int64` | no | [PaymentMethods](Common.md#Common.PaymentMethod) | The business key identifier of the payment's payment method. |
| `PaidAmount` | `Decimal` | no |  | The paid amount. |
| `PaidAmountCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the paid amount's currency. |
| `PaidAmountInCompanyCurrency` | `Decimal` | no |  | The paid amount in company currency. |
| `PaidAmountInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the paid amount in company currency's currency. |
| `PaidVatAmount` | `Decimal?` | yes |  | The paid VAT amount. |
| `PaidVatAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the paid VAT amount's currency. |
| `BankChargeAmount` | `Decimal?` | yes |  | The bank charge amount. |
| `BankChargeAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the bank charge amount's currency. |
| `IsOrdered` | `Boolean` | no |  | Specifies if the outgoing payment is ordered for payment. |
| `IsCancelled` | `Boolean` | no |  | Specifies if the outgoing payment is cancelled. |
| `CancelledByUserId` | `Int64?` | yes | [ApplicationUsers](Common.md#Common.ApplicationUser) | The business key identifier of the user that cancelled the payment. |
| `CancelDate` | `DateTimeOffset?` | yes |  | The date at which the payment was cancelled. _(Replaced by CancelTimeStamp)_ |
| `CancelTimeStamp` | `DateTimeOffset?` | yes |  | The timestamp when the payment was cancelled. |
| `ReceivingBankAccountId` | `Int64?` | yes | [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount) | The business key identifier of the receiving bank account. |
| `SendingBankAccountId` | `Int64?` | yes | [BankAccounts](Accounting.md#Accounting.BankAccount) | The business key identifier of the bank account the payment was sent from. |
| `SetOffIncomingPaymentId` | `Int64?` | yes | [IncomingPayments](Accounting.md#Accounting.IncomingPayment) | The business key identifier of the incoming payment the payment was set off against. |
| `BookingId` | `Int64?` | yes | [Bookings](Accounting.md#Accounting.Booking) | The business key identifier of the outgoing payment's booking. |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](Common.md#Common.WriteOffCode) | The business key identifier of the outgoing payment's write off code. |
| `WriteOffAmount` | `Decimal?` | yes |  | The write off amount. |
| `WriteOffAmountCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the write off amount's currency. |
| `WriteOffAmountInCompanyCurrency` | `Decimal?` | yes |  | The write off amount in company currency. |
| `WriteOffAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the write off amount in company currency's currency. |
| `BundleNumber` | `Int64` | no |  | The payment's bundle number. |
| `ChequeNumber` | `String` | no |  | The payment's cheque number. |
| `CurrencyExchangeRate` | `Decimal` | no |  | The payment's currency exchange rate. |
| `VoucherText` | `String` | no |  | The payment's voucher text. |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [ApplicationUsers](Common.md#Common.ApplicationUser), [BankAccounts](Accounting.md#Accounting.BankAccount), [Bookings](Accounting.md#Accounting.Booking), [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount), [Currencies](Common.md#Common.Currency), [IncomingPayments](Accounting.md#Accounting.IncomingPayment), [PaymentMethods](Common.md#Common.PaymentMethod), [Suppliers](Purchase.md#Purchase.Supplier), [WriteOffCodes](Common.md#Common.WriteOffCode)
**Referenced by:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable)

<a id="Accounting.StandardAccount"></a>
### StandardAccounts

Represents a standard account.

- **Endpoint:** `GET /api/v1/Accounting/StandardAccounts`
- **Required permission:** Show chart of accounts
- **Introduced in:** 22.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the standard account (mirrors AccountType). |
| `AccountType` | `Int32` | no |  | The business key identifier of the standard account. |
| `Version` | `Int32` | no |  | The version of the account. |
| `CodingEntryId` | `Int64?` | yes | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the account's coding entry. |
| `StandardAccountCategory` | `Int32` | no |  | The category of the account. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the voucher row. |
| `EntryIdentifier` | `String` | no |  | The unique coding identifier of the voucher row's coding entry. |
| `VoucherId` | `Int64` | no | [Vouchers](Accounting.md#Accounting.Voucher) | The business key identifier of the voucher that the voucher row belongs to. |
| `ParentVoucherDate` | `DateTimeOffset` | no |  | The voucher date of the parent voucher. |
| `ParentIsPreliminary` | `Boolean` | no |  | Specifies if the parent voucher is preliminary. |
| `ExchangeRate` | `Decimal` | no |  | The exchange rate of the voucher row. |
| `VatRateId` | `Int64?` | yes | [VatRates](Common.md#Common.VatRate) | The business key identifier of the row's VAT rate. |
| `BalanceId` | `Int64?` | yes | [Balances](Accounting.md#Accounting.Balance) | The business key identifier of the row's balance. |
| `CodingMethodId` | `Int64?` | yes |  | The business key identifier of the row's coding method. References CodingMethod. |
| `AccrualAccountingId` | `Int64?` | yes | [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting) | The business key identifier of the row's accrual accounting. |
| `OrderNumber` | `String` | no |  | The order number linked to the voucher row |
| `DebitInCompanyCurrency` | `Decimal` | no |  | Debit in the company currency. |
| `DebitInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the debit in the company currency. |
| `CreditInCompanyCurrency` | `Decimal` | no |  | Credit in the company currency. |
| `CreditInCompanyCurrencyCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the credit in the company currency. |
| `Debit` | `Decimal` | no |  | Debit on the voucher row. |
| `DebitCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the debit currency. |
| `Credit` | `Decimal` | no |  | Credit on the voucher row. |
| `CreditCurrencyId` | `Int64` | no | [Currencies](Common.md#Common.Currency) | The business key identifier of the credit currency. |
| `Quantity` | `Decimal` | no |  | The quantity set on the voucher row. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](Accounting.md#Accounting.CodingEntry) | The business key identifier of the coding entry. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of the accounts payable connected to the row. |
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) | The business key identifier of the accounts receivable connected to the row. |
| `NetAmountVoucherRowId` | `Int64?` | yes | [VoucherRows](Accounting.md#Accounting.VoucherRow) | The business key identifier of the net amount row that the VAT row belongs to. |

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [AccrualAccountings](Accounting.md#Accounting.AccrualAccounting), [Balances](Accounting.md#Accounting.Balance), [CodingEntries](Accounting.md#Accounting.CodingEntry), [Currencies](Common.md#Common.Currency), [VatRates](Common.md#Common.VatRate), [VoucherRows](Accounting.md#Accounting.VoucherRow), [Vouchers](Accounting.md#Accounting.Voucher)
**Referenced by:** [VoucherRows](Accounting.md#Accounting.VoucherRow), [Vouchers](Accounting.md#Accounting.Voucher)

<a id="Accounting.Voucher"></a>
### Vouchers

Represents a voucher.

- **Endpoint:** `GET /api/v1/Accounting/Vouchers`
- **Required permission:** Show voucher
- **Introduced in:** 2.30

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the voucher. |
| `Version` | `Int32` | no |  | The version of the voucher. |
| `SeriesId` | `Int64` | no | [VoucherSeries](Accounting.md#Accounting.VoucherSeries) | The business key identifier of the voucher series for the voucher. |
| `AccountingYearId` | `Int64` | no | [AccountingYears](Accounting.md#Accounting.AccountingYear) | The business key identifier of the accounting year for the voucher. |
| `Number` | `Int64` | no |  | The voucher number. |
| `Text` | `String` | no |  | The description of the voucher. |
| `VoucherDate` | `DateTimeOffset` | no |  | The date of the voucher. |
| `ConnectedVoucherId` | `Int64?` | yes | [Vouchers](Accounting.md#Accounting.Voucher) | The business key identifier of the voucher connected to the voucher. |
| `ConnectionType` | `Int32` | no |  | The connection type to the connected voucher. |
| `ReverseConnectionVoucherId` | `Int64?` | yes | [Vouchers](Accounting.md#Accounting.Voucher) | The business key identifier of rectification/copy connected to the voucher. |
| `ReverseConnectionType` | `Int32` | no |  | The connection type to the reverse connected voucher. |
| `IsPreliminary` | `Boolean` | no |  | Specifies if the voucher is preliminary. |
| `BundleNumber` | `Int64?` | yes |  | The bundle number of the voucher. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the voucher's comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the voucher. |
| `Rows` | `VoucherRows[]` | no | [VoucherRows](Accounting.md#Accounting.VoucherRow) | The rows belonging to the voucher. |
| `AccountsReceivableLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's accounts receivable ledger. References AccountsReceivableLedger. |
| `CancelledAccountsReceivableLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's cancelled accounts receivable ledger. References CancelledAccountsReceivableLedger. |
| `AccountsPayableLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's accounts payable ledger. References AccountsPayableLedger. |
| `CancelledAccountsPayableLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's cancelled accounts payable ledger. References CancelledAccountsPayableLedger. |
| `PreliminaryAccountsPayableLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's preliminary accounts payable ledger. References PreliminaryAccountsPayableLedger. |
| `CancelledPreliminaryAccountsPayableLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's cancelled preliminary accounts payable ledger. References CancelledPreliminaryAccountsPayableLedger. |
| `IncomingPaymentLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's incoming payment ledger. References IncomingPaymentLedger. |
| `AccrualAccountingLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's accrual accounting ledger. References AccrualAccountingLedger. |
| `OutgoingPaymentLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's outgoing payment ledger. References OutgoingPaymentLedger. |
| `FixedAssetLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's fixed asset payment ledger. References FixedAssetLedger. |
| `UnplannedStockBalanceChangeLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's unplanned stock balance change ledger. References UnplannedStockBalanceChangeLedger. |
| `StockTransactionLogLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's stock transaction log ledger. References StockTransactionLogLedger. |
| `ManufacturingOrderLogLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's manufacturing order log ledger. References ManufacturingOrderLogLedger. |
| `InvoiceLogLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's invoice log ledger. References InvoiceLogLedger. |
| `PriceChangeLogLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's price change log ledger. References PriceChangeLogLedger. |
| `CalculationDifferenceLedgerId` | `Int64?` | yes |  | The business key identifier of the voucher's calculation difference ledger. References CalculationDifferenceLedger. |
| `UnplannedStockBalanceChangeTransactionId` | `Int64?` | yes |  | The business key identifier for the unplanned stock balance change transaction of the voucher. References UnplannedStockBalanceChangeTransaction. |
| `AccountsReceivableId` | `Int64?` | yes |  | The business key identifier for the accounts receivable linked to the voucher. References AccountsReceivable. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier for the accounts payable linked to the voucher. |
| `AccountsPayable` | `AccountsPayables` | no | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The accounts payable linked to the voucher. |
| `AccrualAccountingRowId` | `Int64?` | yes | [AccrualAccountingRows](Accounting.md#Accounting.AccrualAccountingRow) | The business key identifier for the accrual accounting row linked to the voucher. |
| `VatBookingId` | `Int64?` | yes |  | The business key identifier for the voucher's VAT booking. References VatBooking. |
| `CorrectionBookingId` | `Int64?` | yes |  | The business key identifier for the voucher's correction booking. References Booking. |
| `CNSeries` | `String` | no |  | The CN series of the voucher. |
| `CNNumber` | `String` | no |  | The CN number of the voucher. |

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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the voucher series. |
| `Series` | `String` | no |  | The identifying code of the voucher series. |
| `IsActive` | `Boolean` | no |  | Defines if the voucher series is active. |

**Referenced by:** [ApplicationUsers](Common.md#Common.ApplicationUser), [Vouchers](Accounting.md#Accounting.Voucher)


## Payload types

<a id="Accounting.AccountingExportResponse"></a>
### AccountingExportResponse

The response object used by accounting exports.

- **Introduced in:** 23.9

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `CommandName` | `String` | no |  | The name of the command that was invoked. |
| `Name` | `String` | no |  | The name of the accounting exporter. |
| `Data` | `String` | no |  | The accounting export data represented as a Base64 string. |


<a id="Accounting.SetOffDestination"></a>
### SetOffDestination

The set-off invoice.

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable) | The business key identifier of accounts receivable. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](Accounting.md#Accounting.AccountsPayable) | The business key identifier of accounts payable. |
| `SetOffAmount` | `Decimal` | no |  | The amount to set-off. |
| `WriteOffCodeId` | `Int64?` | yes | [WriteOffCodes](Common.md#Common.WriteOffCode) | The business key identifier of the write off code of the set-off payment if paid amount deviates from the invoice. |
| `InterestType` | `Int32?` | yes |  | The interest type of the set-off invoice. |

- `InterestType` — InterestInvoice=0, NextRegularInvoice=1, None=2

**References out:** [AccountsPayables](Accounting.md#Accounting.AccountsPayable), [AccountsReceivables](Accounting.md#Accounting.AccountsReceivable), [WriteOffCodes](Common.md#Common.WriteOffCode)


## Depends on other modules

- [Common](Common.md): [Addresses](Common.md#Common.Address), [ApplicationUsers](Common.md#Common.ApplicationUser), [BusinessContactBankAccounts](Common.md#Common.BusinessContactBankAccount), [Comments](Common.md#Common.Comment), [Countries](Common.md#Common.Country), [Currencies](Common.md#Common.Currency), [CurrencyExchangeTypes](Common.md#Common.CurrencyExchangeType), [Departments](Common.md#Common.Department), [LanguageCodes](Common.md#Common.LanguageCode), [PaymentMethods](Common.md#Common.PaymentMethod), [PaymentTerms](Common.md#Common.PaymentTerm), [VatGroups](Common.md#Common.VatGroup), [VatRates](Common.md#Common.VatRate), [Warehouses](Common.md#Common.Warehouse), [WriteOffCodes](Common.md#Common.WriteOffCode)
- [Manufacturing](Manufacturing.md): [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
- [Purchase](Purchase.md): [PurchaseOrders](Purchase.md#Purchase.PurchaseOrder), [PurchaseOrderDeliveryRows](Purchase.md#Purchase.PurchaseOrderDeliveryRow), [Suppliers](Purchase.md#Purchase.Supplier), [SupplierAccountGroups](Purchase.md#Purchase.SupplierAccountGroup)
- [Sales](Sales.md): [Customers](Sales.md#Sales.Customer), [CustomerAccountGroups](Sales.md#Sales.CustomerAccountGroup)
