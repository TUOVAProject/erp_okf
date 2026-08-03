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

- **Module:** [Common](../../modules/Common.md)
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
| `ExchangeRates` | `CurrencyExchangeRates[]` | no | [CurrencyExchangeRates](CurrencyExchangeRate.md) | expandable, collection | All available exchange rates for the currency. |
| `ExchangeRatesChangeLog` | `CurrencyExchangeRateChangeLogs[]` | no | [CurrencyExchangeRateChangeLogs](CurrencyExchangeRateChangeLog.md) | expandable, collection, since 2.26 | All previous exchange rates for the currency |

## Referenced by

**Accounting**

- [AccountYearSettings](../Accounting/AccountYearSetting.md) — `CurrencyId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `CurrencyId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `InvoiceAmountCurrencyId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `InvoiceAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `OrderedRestAmountCurrencyId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `RestAmountCurrencyId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `RestAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `VatAmountCurrencyId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `VatAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `WithholdTaxAmountCurrencyId` (FK)
- [AccountsPayables](../Accounting/AccountsPayable.md) — `WithholdTaxAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `CurrencyId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `InvoiceAmountCurrencyId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `InvoiceAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `OrderedRestAmountCurrencyId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `RestAmountCurrencyId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `RestAmountInCompanyCurrencyCurrencyId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `VatAmountCurrencyId` (FK)
- [AccountsReceivables](../Accounting/AccountsReceivable.md) — `VatAmountInCompanyCurrencyCurrencyId` (FK)
- [BankAccounts](../Accounting/BankAccount.md) — `CurrencyId` (FK)
- [BookingRows](../Accounting/BookingRow.md) — `CreditCurrencyId` (FK)
- [BookingRows](../Accounting/BookingRow.md) — `CreditInCompanyCurrencyCurrencyId` (FK)
- [BookingRows](../Accounting/BookingRow.md) — `DebitCurrencyId` (FK)
- [BookingRows](../Accounting/BookingRow.md) — `DebitInCompanyCurrencyCurrencyId` (FK)
- [IncomingPayments](../Accounting/IncomingPayment.md) — `BankChargeAmountCurrencyId` (FK)
- [IncomingPayments](../Accounting/IncomingPayment.md) — `PaidAmountCurrencyId` (FK)
- [IncomingPayments](../Accounting/IncomingPayment.md) — `PaidAmountInCompanyCurrencyCurrencyId` (FK)
- [IncomingPayments](../Accounting/IncomingPayment.md) — `PaidVatAmountCurrencyId` (FK)
- [IncomingPayments](../Accounting/IncomingPayment.md) — `WriteOffAmountCurrencyId` (FK)
- [IncomingPayments](../Accounting/IncomingPayment.md) — `WriteOffAmountInCompanyCurrencyCurrencyId` (FK)
- [OpeningBalances](../Accounting/OpeningBalance.md) — `CreditCurrencyId` (FK)
- [OpeningBalances](../Accounting/OpeningBalance.md) — `CreditInCompanyCurrencyCurrencyId` (FK)
- [OpeningBalances](../Accounting/OpeningBalance.md) — `DebitCurrencyId` (FK)
- [OpeningBalances](../Accounting/OpeningBalance.md) — `DebitInCompanyCurrencyCurrencyId` (FK)
- [OutgoingPayments](../Accounting/OutgoingPayment.md) — `BankChargeAmountCurrencyId` (FK)
- [OutgoingPayments](../Accounting/OutgoingPayment.md) — `PaidAmountCurrencyId` (FK)
- [OutgoingPayments](../Accounting/OutgoingPayment.md) — `PaidAmountInCompanyCurrencyCurrencyId` (FK)
- [OutgoingPayments](../Accounting/OutgoingPayment.md) — `PaidVatAmountCurrencyId` (FK)
- [OutgoingPayments](../Accounting/OutgoingPayment.md) — `WriteOffAmountCurrencyId` (FK)
- [OutgoingPayments](../Accounting/OutgoingPayment.md) — `WriteOffAmountInCompanyCurrencyCurrencyId` (FK)
- [VoucherRows](../Accounting/VoucherRow.md) — `CreditCurrencyId` (FK)
- [VoucherRows](../Accounting/VoucherRow.md) — `CreditInCompanyCurrencyCurrencyId` (FK)
- [VoucherRows](../Accounting/VoucherRow.md) — `DebitCurrencyId` (FK)
- [VoucherRows](../Accounting/VoucherRow.md) — `DebitInCompanyCurrencyCurrencyId` (FK)

**Common**

- [BusinessContactBankAccounts](BusinessContactBankAccount.md) — `Currency` (expand)
- [BusinessContactBankAccounts](BusinessContactBankAccount.md) — `CurrencyId` (FK)
- [Companies](Company.md) — `Currency` (expand)
- [Companies](Company.md) — `CurrencyId` (FK)
- [Countries](Country.md) — `CurrencyId` (FK)
- [CurrencyExchangeRateChangeLogs](CurrencyExchangeRateChangeLog.md) — `CurrencyId` (FK)
- [Money](Money.md) — `CurrencyId` (FK)
- [PartConfigurationResults](PartConfigurationResult.md) — `StandardPriceCurrencyId` (FK)
- [PartConfigurationResults](PartConfigurationResult.md) — `UnitPriceCurrencyId` (FK)
- [PartConfigurationResults](PartConfigurationResult.md) — `UnitPriceInCompanyCurrencyCurrencyId` (FK)
- [PartConfigurationSelectionGroupResults](PartConfigurationSelectionGroupResult.md) — `UnitPriceCurrencyId` (FK)
- [PartConfigurationSelectionGroupResults](PartConfigurationSelectionGroupResult.md) — `UnitPriceInCompanyCurrencyCurrencyId` (FK)
- [PriceLists](PriceList.md) — `CurrencyId` (FK)

**Inventory**

- [Alloys](../Inventory/Alloy.md) — `PriceCurrencyId` (FK)
- [CaseEntryActivities](../Inventory/CaseEntryActivity.md) — `CostPerHourCurrencyId` (FK)
- [CaseEntryAdditionalCost](../Inventory/CaseEntryAdditionalCost.md) — `CostCurrencyId` (FK)
- [CaseManagementActivities](../Inventory/CaseManagementActivity.md) — `CostPerHourCurrencyId` (FK)
- [CaseManagementCost](../Inventory/CaseManagementCost.md) — `CostCurrencyId` (FK)
- [CaseManagementTemplateCosts](../Inventory/CaseManagementTemplateCost.md) — `CostCurrencyId` (FK)
- [Parts](../Inventory/Part.md) — `AveragePriceCurrencyId` (FK)
- [Parts](../Inventory/Part.md) — `FutureStandardPriceCurrencyId` (FK)
- [Parts](../Inventory/Part.md) — `LastPurchasePriceCurrencyId` (FK)
- [Parts](../Inventory/Part.md) — `LastSalesPriceCurrencyId` (FK)
- [Parts](../Inventory/Part.md) — `PostCalculatedAveragePriceCurrencyId` (FK)
- [Parts](../Inventory/Part.md) — `StandardPriceCurrencyId` (FK)
- [PriceChangeLogs](../Inventory/PriceChangeLog.md) — `NewPriceCurrencyId` (FK)
- [PriceChangeLogs](../Inventory/PriceChangeLog.md) — `OldPriceCurrencyId` (FK)

**Manufacturing**

- [OperationRows](../Manufacturing/OperationRow.md) — `SetupCostCurrencyId` (FK)
- [OperationRows](../Manufacturing/OperationRow.md) — `UnitCostCurrencyId` (FK)

**Purchase**

- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `PriceCurrency` (expand)
- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `PriceCurrencyId` (FK)
- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `PriceInCompanyCurrencyCurrency` (expand)
- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `SetupPriceCurrency` (expand)
- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `SetupPriceCurrencyId` (FK)
- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `Currency` (expand)
- [BlanketOrderPurchases](../Purchase/BlanketOrderPurchase.md) — `CurrencyId` (FK)
- [Inquiries](../Purchase/Inquiry.md) — `CurrencyId` (FK)
- [InquiryRows](../Purchase/InquiryRow.md) — `PriceCurrencyId` (FK)
- [InquiryRows](../Purchase/InquiryRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [InquiryRows](../Purchase/InquiryRow.md) — `SetupPriceInCompanyCurrencyCurrencyId` (FK)
- [InquiryRows](../Purchase/InquiryRow.md) — `StandardPriceCurrencyId` (FK)
- [PurchaseOrderInvoiceRows](../Purchase/PurchaseOrderInvoiceRow.md) — `PriceCurrencyId` (FK)
- [PurchaseOrderInvoiceRows](../Purchase/PurchaseOrderInvoiceRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [PurchaseOrderInvoiceRows](../Purchase/PurchaseOrderInvoiceRow.md) — `SetupPriceCurrencyId` (FK)
- [PurchaseOrderInvoiceRows](../Purchase/PurchaseOrderInvoiceRow.md) — `SetupPriceInCompanyCurrencyCurrencyId` (FK)
- [PurchaseOrderInvoiceRows](../Purchase/PurchaseOrderInvoiceRow.md) — `StandardPriceCurrencyId` (FK)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `PriceCurrency` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `PriceCurrencyId` (FK)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `SetupPriceCurrency` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `SetupPriceCurrencyId` (FK)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `StandardPriceCurrency` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `StandardPriceCurrencyId` (FK)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `Currency` (expand)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `CurrencyId` (FK)
- [SupplierPartLinks](../Purchase/SupplierPartLink.md) — `PriceCurrency` (expand)
- [SupplierPartLinks](../Purchase/SupplierPartLink.md) — `PriceCurrencyId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `Currency` (expand)
- [Suppliers](../Purchase/Supplier.md) — `CurrencyId` (FK)

**Sales**

- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `Currency` (expand)
- [BlanketOrderSales](../Sales/BlanketOrderSales.md) — `CurrencyId` (FK)
- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `PriceCurrency` (expand)
- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `PriceCurrencyId` (FK)
- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `PriceInCompanyCurrencyCurrency` (expand)
- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `SetupPriceCurrency` (expand)
- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `SetupPriceCurrencyId` (FK)
- [CustomerOrderInvoiceOrderRowDiscounts](../Sales/CustomerOrderInvoiceOrderRowDiscount.md) — `AsAmountCurrencyId` (FK)
- [CustomerOrderInvoiceOrderRowDiscounts](../Sales/CustomerOrderInvoiceOrderRowDiscount.md) — `GrossPriceCurrencyId` (FK)
- [CustomerOrderInvoiceOrderRowDiscounts](../Sales/CustomerOrderInvoiceOrderRowDiscount.md) — `NetPriceCurrencyId` (FK)
- [CustomerOrderInvoiceRows](../Sales/CustomerOrderInvoiceRow.md) — `PriceCurrencyId` (FK)
- [CustomerOrderInvoiceRows](../Sales/CustomerOrderInvoiceRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [CustomerOrderInvoiceRows](../Sales/CustomerOrderInvoiceRow.md) — `SetupPriceInCompanyCurrencyCurrencyId` (FK)
- [CustomerOrderInvoiceRows](../Sales/CustomerOrderInvoiceRow.md) — `StandardPriceCurrencyId` (FK)
- [CustomerOrderInvoices](../Sales/CustomerOrderInvoice.md) — `EditedOrderAmountExcludingVatCurrencyId` (FK)
- [CustomerOrderOrderRowDiscounts](../Sales/CustomerOrderOrderRowDiscount.md) — `AsAmountCurrencyId` (FK)
- [CustomerOrderOrderRowDiscounts](../Sales/CustomerOrderOrderRowDiscount.md) — `GrossPriceCurrencyId` (FK)
- [CustomerOrderOrderRowDiscounts](../Sales/CustomerOrderOrderRowDiscount.md) — `NetPriceCurrencyId` (FK)
- [CustomerOrderPaymentPlanRows](../Sales/CustomerOrderPaymentPlanRow.md) — `AmountCurrencyId` (FK)
- [CustomerOrderPaymentPlanRows](../Sales/CustomerOrderPaymentPlanRow.md) — `AmountInCompanyCurrencyCurrencyId` (FK)
- [CustomerOrderPaymentPlanRows](../Sales/CustomerOrderPaymentPlanRow.md) — `ReducedAmountInCompanyCurrencyCurrencyId` (FK)
- [CustomerOrderRowInflows](../Sales/CustomerOrderRowInflow.md) — `PriceChangeCurrency` (expand)
- [CustomerOrderRowInflows](../Sales/CustomerOrderRowInflow.md) — `PriceChangeCurrencyId` (FK)
- [CustomerOrderRowInflows](../Sales/CustomerOrderRowInflow.md) — `SetupPriceChangeCurrency` (expand)
- [CustomerOrderRowInflows](../Sales/CustomerOrderRowInflow.md) — `SetupPriceChangeCurrencyId` (FK)
- [CustomerOrderRowInflows](../Sales/CustomerOrderRowInflow.md) — `TotalValueChangeCurrency` (expand)
- [CustomerOrderRowInflows](../Sales/CustomerOrderRowInflow.md) — `TotalValueChangeCurrencyId` (FK)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `ComparativePriceCurrencyId` (FK)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `PriceCurrencyId` (FK)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `SetupPriceCurrencyId` (FK)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `StandardPriceCurrencyId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `CurrencyId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `EditedOrderAmountExcludingVatCurrencyId` (FK)
- [CustomerOrders](../Sales/CustomerOrder.md) — `ResetPaymentPlanDifferenceAmountCurrency` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `ResetPaymentPlanDifferenceAmountCurrencyId` (FK)
- [CustomerPartLinks](../Sales/CustomerPartLink.md) — `PriceCurrency` (expand)
- [CustomerPartLinks](../Sales/CustomerPartLink.md) — `PriceCurrencyId` (FK)
- [Customers](../Sales/Customer.md) — `Currency` (expand)
- [Customers](../Sales/Customer.md) — `CurrencyId` (FK)
- [QuoteOrderRowDiscounts](../Sales/QuoteOrderRowDiscount.md) — `AsAmountCurrencyId` (FK)
- [QuoteOrderRowDiscounts](../Sales/QuoteOrderRowDiscount.md) — `GrossPriceCurrencyId` (FK)
- [QuoteOrderRowDiscounts](../Sales/QuoteOrderRowDiscount.md) — `NetPriceCurrencyId` (FK)
- [QuoteRows](../Sales/QuoteRow.md) — `PriceCurrencyId` (FK)
- [QuoteRows](../Sales/QuoteRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [QuoteRows](../Sales/QuoteRow.md) — `SetupPriceInCompanyCurrencyCurrencyId` (FK)
- [QuoteRows](../Sales/QuoteRow.md) — `StandardPriceCurrencyId` (FK)
- [Quotes](../Sales/Quote.md) — `CurrencyId` (FK)
- [Quotes](../Sales/Quote.md) — `EditedOrderAmountExcludingVatCurrencyId` (FK)
- [SalesAgreementBases](../Sales/SalesAgreementBasis.md) — `Currency` (expand)
- [SalesAgreementBases](../Sales/SalesAgreementBasis.md) — `CurrencyId` (FK)
- [SalesAgreementBasisRows](../Sales/SalesAgreementBasisRow.md) — `PriceCurrency` (expand)
- [SalesAgreementBasisRows](../Sales/SalesAgreementBasisRow.md) — `PriceCurrencyId` (FK)
- [SalesAgreementBasisRows](../Sales/SalesAgreementBasisRow.md) — `PriceInCompanyCurrencyCurrency` (expand)
- [SalesAgreementBasisRows](../Sales/SalesAgreementBasisRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementBasisRows](../Sales/SalesAgreementBasisRow.md) — `StandardPriceCurrency` (expand)
- [SalesAgreementBasisRows](../Sales/SalesAgreementBasisRow.md) — `StandardPriceCurrencyId` (FK)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `PriceChangeCurrency` (expand)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `PriceChangeCurrencyId` (FK)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `PriceChangeInCompanyCurrencyCurrency` (expand)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `PriceChangeInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `PriceChangePerIntervalCurrency` (expand)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `PriceChangePerIntervalCurrencyId` (FK)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `PriceChangePerIntervalInCompanyCurrencyCurrency` (expand)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `PriceChangePerIntervalInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `RowTotalValueCurrency` (expand)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `RowTotalValueCurrencyId` (FK)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `RowTotalValueInCompanyCurrencyCurrency` (expand)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `RowTotalValueInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `TotalValueChangeCurrency` (expand)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `TotalValueChangeCurrencyId` (FK)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `TotalValueChangeInCompanyCurrencyCurrency` (expand)
- [SalesAgreementRowInflows](../Sales/SalesAgreementRowInflow.md) — `TotalValueChangeInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `PriceCurrencyId` (FK)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `PriceInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `SetupPriceCurrencyId` (FK)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `SetupPriceInCompanyCurrencyCurrencyId` (FK)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `StandardPriceCurrencyId` (FK)
- [SalesAgreements](../Sales/SalesAgreement.md) — `CurrencyId` (FK)
- [SalesPrices](../Sales/SalesPrice.md) — `FuturePriceCurrency` (expand)
- [SalesPrices](../Sales/SalesPrice.md) — `FuturePriceCurrencyId` (FK)
- [SalesPrices](../Sales/SalesPrice.md) — `FutureSetupPriceCurrency` (expand)
- [SalesPrices](../Sales/SalesPrice.md) — `FutureSetupPriceCurrencyId` (FK)
- [SalesPrices](../Sales/SalesPrice.md) — `PriceCurrency` (expand)
- [SalesPrices](../Sales/SalesPrice.md) — `PriceCurrencyId` (FK)
- [SalesPrices](../Sales/SalesPrice.md) — `SetupPriceCurrency` (expand)
- [SalesPrices](../Sales/SalesPrice.md) — `SetupPriceCurrencyId` (FK)
- [ShipmentCustoms](../Sales/ShipmentCustoms.md) — `Currency` (expand)
- [ShipmentCustoms](../Sales/ShipmentCustoms.md) — `CurrencyId` (FK)
- [Shipments](../Sales/Shipment.md) — `CalculatedFreightPriceCurrency` (expand)
- [Shipments](../Sales/Shipment.md) — `CalculatedFreightPriceCurrencyId` (FK)

**TimeRecording**

- [AdditionRecordings](../TimeRecording/AdditionRecording.md) — `CostCurrencyId` (FK)
- [AttendanceAdditions](../TimeRecording/AttendanceAddition.md) — `CostCurrencyId` (FK)


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
