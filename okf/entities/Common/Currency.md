---
type: API Entity
title: Currencies
description: Represents a queryable currency.
resource: https://api.monitor.se/api/Monitor.API.Common.Currency.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Currency.html
  title: Monitor API — Currency
module: Common
api_class: Currency
doc_name: Currencies
endpoint: GET /api/v1/Common/Currencies
guid: 7FE7D8D5-FECB-4D7C-9300-E99DB95F0F9D
permission: Show currencies
introduced_in: '2.18'
property_count: 8
references_out:
- /entities/Common/CurrencyExchangeRate.md
- /entities/Common/CurrencyExchangeRateChangeLog.md
referenced_by:
- /entities/Accounting/AccountYearSetting.md
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/AccountsReceivable.md
- /entities/Accounting/BankAccount.md
- /entities/Accounting/BookingRow.md
- /entities/Accounting/IncomingPayment.md
- /entities/Accounting/OpeningBalance.md
- /entities/Accounting/OutgoingPayment.md
- /entities/Accounting/VoucherRow.md
- /entities/Common/BusinessContactBankAccount.md
- /entities/Common/Company.md
- /entities/Common/Country.md
- /entities/Common/CurrencyExchangeRateChangeLog.md
- /entities/Common/Money.md
- /entities/Common/PartConfigurationResult.md
- /entities/Common/PartConfigurationSelectionGroupResult.md
- /entities/Common/PriceList.md
- /entities/Inventory/Alloy.md
- /entities/Inventory/CaseEntryActivity.md
- /entities/Inventory/CaseEntryAdditionalCost.md
- /entities/Inventory/CaseManagementActivity.md
- /entities/Inventory/CaseManagementCost.md
- /entities/Inventory/CaseManagementTemplateCost.md
- /entities/Inventory/Part.md
- /entities/Inventory/PriceChangeLog.md
- /entities/Manufacturing/OperationRow.md
- /entities/Purchase/BlanketOrderPurchase.md
- /entities/Purchase/BlanketOrderPurchaseRow.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderInvoiceRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Purchase/Supplier.md
- /entities/Purchase/SupplierPartLink.md
- /entities/Sales/BlanketOrderSales.md
- /entities/Sales/BlanketOrderSalesRow.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/CustomerOrderInvoiceOrderRowDiscount.md
- /entities/Sales/CustomerOrderInvoiceRow.md
- /entities/Sales/CustomerOrderOrderRowDiscount.md
- /entities/Sales/CustomerOrderPaymentPlanRow.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/CustomerOrderRowInflow.md
- /entities/Sales/CustomerPartLink.md
- /entities/Sales/Quote.md
- /entities/Sales/QuoteOrderRowDiscount.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/SalesAgreementBasis.md
- /entities/Sales/SalesAgreementBasisRow.md
- /entities/Sales/SalesAgreementRow.md
- /entities/Sales/SalesAgreementRowInflow.md
- /entities/Sales/SalesPrice.md
- /entities/Sales/Shipment.md
- /entities/Sales/ShipmentCustoms.md
- /entities/TimeRecording/AdditionRecording.md
- /entities/TimeRecording/AttendanceAddition.md
---

# Currencies

Represents a queryable currency.

- **Module:** [Common](/modules/Common.md)
- **API class:** `Currency`
- **Endpoint:** `GET /api/v1/Common/Currencies`
- **Required permission:** Show currencies
- **GUID:** `7FE7D8D5-FECB-4D7C-9300-E99DB95F0F9D`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the currency. |
| `Code` | `String` | no |  | unique, max length 6 | The human readable identifier of the currency. |
| `Description` | `String` | no |  |  | The translated description of the currency. |
| `RateFactor` | `Int32` | no |  |  | The rate factor of the currency. |
| `DefaultSalesExchangeRate` | `Decimal` | no |  |  | The default sales exchange rate. |
| `DefaultPurchaseExchangeRate` | `Decimal` | no |  |  | The default purchase exchange rate. |
| `ExchangeRates` | `CurrencyExchangeRates[]` | no | [CurrencyExchangeRates](/entities/Common/CurrencyExchangeRate.md) | expandable, collection | All available exchange rates for the currency. |
| `ExchangeRatesChangeLog` | `CurrencyExchangeRateChangeLogs[]` | no | [CurrencyExchangeRateChangeLogs](/entities/Common/CurrencyExchangeRateChangeLog.md) | expandable, collection, since 2.26 | All previous exchange rates for the currency |

## Referenced by

**Accounting**

- [AccountYearSettings](/entities/Accounting/AccountYearSetting.md) — `CurrencyId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `CurrencyId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `InvoiceAmountCurrencyId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `InvoiceAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `OrderedRestAmountCurrencyId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `RestAmountCurrencyId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `RestAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `VatAmountCurrencyId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `VatAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `WithholdTaxAmountCurrencyId` (FK)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `WithholdTaxAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `CurrencyId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `InvoiceAmountCurrencyId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `InvoiceAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `OrderedRestAmountCurrencyId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `RestAmountCurrencyId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `RestAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `VatAmountCurrencyId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `VatAmountInCompanyCurrencyCurrencyId` (FK)
- [BankAccounts](/entities/Accounting/BankAccount.md) — `CurrencyId` (FK)
- [BookingRows](/entities/Accounting/BookingRow.md) — `CreditCurrencyId` (FK)
- [BookingRows](/entities/Accounting/BookingRow.md) — `CreditInCompanyCurrencyCurrencyId` (FK)
- [BookingRows](/entities/Accounting/BookingRow.md) — `DebitCurrencyId` (FK)
- [BookingRows](/entities/Accounting/BookingRow.md) — `DebitInCompanyCurrencyCurrencyId` (FK)
- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `BankChargeAmountCurrencyId` (FK)
- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `PaidAmountCurrencyId` (FK)
- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `PaidAmountInCompanyCurrencyCurrencyId` (FK)
- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `PaidVatAmountCurrencyId` (FK)
- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `WriteOffAmountCurrencyId` (FK)
- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `WriteOffAmountInCompanyCurrencyCurrencyId` (FK)
- [OpeningBalances](/entities/Accounting/OpeningBalance.md) — `CreditCurrencyId` (FK)
- [OpeningBalances](/entities/Accounting/OpeningBalance.md) — `CreditInCompanyCurrencyCurrencyId` (FK)
- [OpeningBalances](/entities/Accounting/OpeningBalance.md) — `DebitCurrencyId` (FK)
- [OpeningBalances](/entities/Accounting/OpeningBalance.md) — `DebitInCompanyCurrencyCurrencyId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `BankChargeAmountCurrencyId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `PaidAmountCurrencyId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `PaidAmountInCompanyCurrencyCurrencyId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `PaidVatAmountCurrencyId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `WriteOffAmountCurrencyId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `WriteOffAmountInCompanyCurrencyCurrencyId` (FK)
- [VoucherRows](/entities/Accounting/VoucherRow.md) — `CreditCurrencyId` (FK)
- [VoucherRows](/entities/Accounting/VoucherRow.md) — `CreditInCompanyCurrencyCurrencyId` (FK)
- [VoucherRows](/entities/Accounting/VoucherRow.md) — `DebitCurrencyId` (FK)
- [VoucherRows](/entities/Accounting/VoucherRow.md) — `DebitInCompanyCurrencyCurrencyId` (FK)

**Common**

- [BusinessContactBankAccounts](/entities/Common/BusinessContactBankAccount.md) — `Currency` (expand)
- [BusinessContactBankAccounts](/entities/Common/BusinessContactBankAccount.md) — `CurrencyId` (FK)
- [Companies](/entities/Common/Company.md) — `Currency` (expand)
- [Companies](/entities/Common/Company.md) — `CurrencyId` (FK)
- [Countries](/entities/Common/Country.md) — `CurrencyId` (FK)
- [CurrencyExchangeRateChangeLogs](/entities/Common/CurrencyExchangeRateChangeLog.md) — `CurrencyId` (FK)
- [Money](/entities/Common/Money.md) — `CurrencyId` (FK)
- [PartConfigurationResults](/entities/Common/PartConfigurationResult.md) — `StandardPriceCurrencyId` (FK)
- [PartConfigurationResults](/entities/Common/PartConfigurationResult.md) — `UnitPriceCurrencyId` (FK)
- [PartConfigurationResults](/entities/Common/PartConfigurationResult.md) — `UnitPriceInCompanyCurrencyCurrencyId` (FK)
- [PartConfigurationSelectionGroupResults](/entities/Common/PartConfigurationSelectionGroupResult.md) — `UnitPriceCurrencyId` (FK)
- [PartConfigurationSelectionGroupResults](/entities/Common/PartConfigurationSelectionGroupResult.md) — `UnitPriceInCompanyCurrencyCurrencyId` (FK)
- [PriceLists](/entities/Common/PriceList.md) — `CurrencyId` (FK)

**Inventory**

- [Alloys](/entities/Inventory/Alloy.md) — `PriceCurrencyId` (FK)
- [CaseEntryActivities](/entities/Inventory/CaseEntryActivity.md) — `CostPerHourCurrencyId` (FK)
- [CaseEntryAdditionalCost](/entities/Inventory/CaseEntryAdditionalCost.md) — `CostCurrencyId` (FK)
- [CaseManagementActivities](/entities/Inventory/CaseManagementActivity.md) — `CostPerHourCurrencyId` (FK)
- [CaseManagementCost](/entities/Inventory/CaseManagementCost.md) — `CostCurrencyId` (FK)
- [CaseManagementTemplateCosts](/entities/Inventory/CaseManagementTemplateCost.md) — `CostCurrencyId` (FK)
- [Parts](/entities/Inventory/Part.md) — `AveragePriceCurrencyId` (FK)
- [Parts](/entities/Inventory/Part.md) — `FutureStandardPriceCurrencyId` (FK)
- [Parts](/entities/Inventory/Part.md) — `LastPurchasePriceCurrencyId` (FK)
- [Parts](/entities/Inventory/Part.md) — `LastSalesPriceCurrencyId` (FK)
- [Parts](/entities/Inventory/Part.md) — `PostCalculatedAveragePriceCurrencyId` (FK)
- [Parts](/entities/Inventory/Part.md) — `StandardPriceCurrencyId` (FK)
- [PriceChangeLogs](/entities/Inventory/PriceChangeLog.md) — `NewPriceCurrencyId` (FK)
- [PriceChangeLogs](/entities/Inventory/PriceChangeLog.md) — `OldPriceCurrencyId` (FK)

**Manufacturing**

- [OperationRows](/entities/Manufacturing/OperationRow.md) — `SetupCostCurrencyId` (FK)
- [OperationRows](/entities/Manufacturing/OperationRow.md) — `UnitCostCurrencyId` (FK)

**Purchase**

- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `PriceCurrency` (expand)
- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `PriceCurrencyId` (FK)
- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `PriceInCompanyCurrencyCurrency` (expand)
- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `SetupPriceCurrency` (expand)
- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `SetupPriceCurrencyId` (FK)
- [BlanketOrderPurchases](/entities/Purchase/BlanketOrderPurchase.md) — `Currency` (expand)
- [BlanketOrderPurchases](/entities/Purchase/BlanketOrderPurchase.md) — `CurrencyId` (FK)
- [Inquiries](/entities/Purchase/Inquiry.md) — `CurrencyId` (FK)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `PriceCurrencyId` (FK)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `SetupPriceInCompanyCurrencyCurrencyId` (FK)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `StandardPriceCurrencyId` (FK)
- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `PriceCurrencyId` (FK)
- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `SetupPriceCurrencyId` (FK)
- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `SetupPriceInCompanyCurrencyCurrencyId` (FK)
- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `StandardPriceCurrencyId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `PriceCurrency` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `PriceCurrencyId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `SetupPriceCurrency` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `SetupPriceCurrencyId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `StandardPriceCurrency` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `StandardPriceCurrencyId` (FK)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `Currency` (expand)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `CurrencyId` (FK)
- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `PriceCurrency` (expand)
- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `PriceCurrencyId` (FK)
- [Suppliers](/entities/Purchase/Supplier.md) — `Currency` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `CurrencyId` (FK)

**Sales**

- [BlanketOrderSales](/entities/Sales/BlanketOrderSales.md) — `Currency` (expand)
- [BlanketOrderSales](/entities/Sales/BlanketOrderSales.md) — `CurrencyId` (FK)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `PriceCurrency` (expand)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `PriceCurrencyId` (FK)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `PriceInCompanyCurrencyCurrency` (expand)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `SetupPriceCurrency` (expand)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `SetupPriceCurrencyId` (FK)
- [CustomerOrderInvoiceOrderRowDiscounts](/entities/Sales/CustomerOrderInvoiceOrderRowDiscount.md) — `AsAmountCurrencyId` (FK)
- [CustomerOrderInvoiceOrderRowDiscounts](/entities/Sales/CustomerOrderInvoiceOrderRowDiscount.md) — `GrossPriceCurrencyId` (FK)
- [CustomerOrderInvoiceOrderRowDiscounts](/entities/Sales/CustomerOrderInvoiceOrderRowDiscount.md) — `NetPriceCurrencyId` (FK)
- [CustomerOrderInvoiceRows](/entities/Sales/CustomerOrderInvoiceRow.md) — `PriceCurrencyId` (FK)
- [CustomerOrderInvoiceRows](/entities/Sales/CustomerOrderInvoiceRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [CustomerOrderInvoiceRows](/entities/Sales/CustomerOrderInvoiceRow.md) — `SetupPriceInCompanyCurrencyCurrencyId` (FK)
- [CustomerOrderInvoiceRows](/entities/Sales/CustomerOrderInvoiceRow.md) — `StandardPriceCurrencyId` (FK)
- [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) — `EditedOrderAmountExcludingVatCurrencyId` (FK)
- [CustomerOrderOrderRowDiscounts](/entities/Sales/CustomerOrderOrderRowDiscount.md) — `AsAmountCurrencyId` (FK)
- [CustomerOrderOrderRowDiscounts](/entities/Sales/CustomerOrderOrderRowDiscount.md) — `GrossPriceCurrencyId` (FK)
- [CustomerOrderOrderRowDiscounts](/entities/Sales/CustomerOrderOrderRowDiscount.md) — `NetPriceCurrencyId` (FK)
- [CustomerOrderPaymentPlanRows](/entities/Sales/CustomerOrderPaymentPlanRow.md) — `AmountCurrencyId` (FK)
- [CustomerOrderPaymentPlanRows](/entities/Sales/CustomerOrderPaymentPlanRow.md) — `AmountInCompanyCurrencyCurrencyId` (FK)
- [CustomerOrderPaymentPlanRows](/entities/Sales/CustomerOrderPaymentPlanRow.md) — `ReducedAmountInCompanyCurrencyCurrencyId` (FK)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `PriceChangeCurrency` (expand)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `PriceChangeCurrencyId` (FK)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `SetupPriceChangeCurrency` (expand)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `SetupPriceChangeCurrencyId` (FK)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `TotalValueChangeCurrency` (expand)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `TotalValueChangeCurrencyId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `ComparativePriceCurrencyId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `PriceCurrencyId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `SetupPriceCurrencyId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `StandardPriceCurrencyId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `CurrencyId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `EditedOrderAmountExcludingVatCurrencyId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `ResetPaymentPlanDifferenceAmountCurrency` (expand)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `ResetPaymentPlanDifferenceAmountCurrencyId` (FK)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `PriceCurrency` (expand)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `PriceCurrencyId` (FK)
- [Customers](/entities/Sales/Customer.md) — `Currency` (expand)
- [Customers](/entities/Sales/Customer.md) — `CurrencyId` (FK)
- [QuoteOrderRowDiscounts](/entities/Sales/QuoteOrderRowDiscount.md) — `AsAmountCurrencyId` (FK)
- [QuoteOrderRowDiscounts](/entities/Sales/QuoteOrderRowDiscount.md) — `GrossPriceCurrencyId` (FK)
- [QuoteOrderRowDiscounts](/entities/Sales/QuoteOrderRowDiscount.md) — `NetPriceCurrencyId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `PriceCurrencyId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `SetupPriceInCompanyCurrencyCurrencyId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `StandardPriceCurrencyId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `CurrencyId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `EditedOrderAmountExcludingVatCurrencyId` (FK)
- [SalesAgreementBases](/entities/Sales/SalesAgreementBasis.md) — `Currency` (expand)
- [SalesAgreementBases](/entities/Sales/SalesAgreementBasis.md) — `CurrencyId` (FK)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `PriceCurrency` (expand)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `PriceCurrencyId` (FK)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `PriceInCompanyCurrencyCurrency` (expand)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `StandardPriceCurrency` (expand)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `StandardPriceCurrencyId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `PriceChangeCurrency` (expand)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `PriceChangeCurrencyId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `PriceChangeInCompanyCurrencyCurrency` (expand)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `PriceChangeInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `PriceChangePerIntervalCurrency` (expand)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `PriceChangePerIntervalCurrencyId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `PriceChangePerIntervalInCompanyCurrencyCurrency` (expand)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `PriceChangePerIntervalInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `RowTotalValueCurrency` (expand)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `RowTotalValueCurrencyId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `RowTotalValueInCompanyCurrencyCurrency` (expand)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `RowTotalValueInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `TotalValueChangeCurrency` (expand)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `TotalValueChangeCurrencyId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `TotalValueChangeInCompanyCurrencyCurrency` (expand)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `TotalValueChangeInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `PriceCurrencyId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `SetupPriceCurrencyId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `SetupPriceInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `StandardPriceCurrencyId` (FK)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `CurrencyId` (FK)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `FuturePriceCurrency` (expand)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `FuturePriceCurrencyId` (FK)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `FutureSetupPriceCurrency` (expand)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `FutureSetupPriceCurrencyId` (FK)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `PriceCurrency` (expand)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `PriceCurrencyId` (FK)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `SetupPriceCurrency` (expand)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `SetupPriceCurrencyId` (FK)
- [ShipmentCustoms](/entities/Sales/ShipmentCustoms.md) — `Currency` (expand)
- [ShipmentCustoms](/entities/Sales/ShipmentCustoms.md) — `CurrencyId` (FK)
- [Shipments](/entities/Sales/Shipment.md) — `CalculatedFreightPriceCurrency` (expand)
- [Shipments](/entities/Sales/Shipment.md) — `CalculatedFreightPriceCurrencyId` (FK)

**TimeRecording**

- [AdditionRecordings](/entities/TimeRecording/AdditionRecording.md) — `CostCurrencyId` (FK)
- [AttendanceAdditions](/entities/TimeRecording/AttendanceAddition.md) — `CostCurrencyId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "RateFactor": 0,
  "DefaultSalesExchangeRate": 0.0,
  "DefaultPurchaseExchangeRate": 0.0,
  "ExchangeRates": null,
  "ExchangeRatesChangeLog": null
}
```
