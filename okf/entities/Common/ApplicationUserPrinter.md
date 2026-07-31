---
type: API Entity
title: ApplicationUserPrinters
description: Represents a printer that has been assigned to an application user.
resource: https://api.monitor.se/api/Monitor.API.Common.ApplicationUserPrinter.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ApplicationUserPrinter.html
  title: Monitor API — ApplicationUserPrinter
module: Common
api_class: ApplicationUserPrinter
doc_name: ApplicationUserPrinters
endpoint: GET /api/v1/Common/ApplicationUserPrinters
guid: F518CF01-8FB0-4134-B283-0178684F49F0
permission: Show user
introduced_in: '2.52'
property_count: 7
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/ServerPrinter.md
referenced_by:
- /entities/Common/ApplicationUser.md
---

# ApplicationUserPrinters

Represents a printer that has been assigned to an application user.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ApplicationUserPrinter`
- **Endpoint:** `GET /api/v1/Common/ApplicationUserPrinters`
- **Required permission:** Show user
- **GUID:** `F518CF01-8FB0-4134-B283-0178684F49F0`
- **Introduced in:** 2.52

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the application user printer. |
| `ApplicationUserId` | `Int64` | no | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the application user that the application user printer belongs to. |
| `PrinterName` | `String` | no |  | max length 300 | The name of the local printer that is assigned. |
| `NormalizedFormReportType` | `Int32?` | yes |  | enum | The type of form report that the printer assignment will be used for. |
| `FormReportType` | `Guid?` | yes |  |  | The type of form report that the printer assignment will be used for. |
| `ServerPrinterId` | `Int64?` | yes | [ServerPrinters](/entities/Common/ServerPrinter.md) |  | The server printer that is linked to the application user printer. |
| `FormDocumentType` | `Int32` | no |  | enum | The type of document that the printer assignment will be used for. |

## Enumerations

### NormalizedFormReportType

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `Quote` | 1 |
| `Acknowledgement` | 3 |
| `CustomerDeliveryNote` | 5 |
| `CustomerDeliveryNoteDelivered` | 6 |
| `Invoice` | 7 |
| `CustomerDeliveryNoteCollectionDelivered` | 8 |
| `SalesTransportLabelA4` | 16 |
| `ComprehensiveInvoice` | 17 |
| `PurchaseOrder` | 22 |
| `PurchaseOrderConfirmationReminder` | 23 |
| `PurchaseOrderConfirmationReminderCasualSupplier` | 24 |
| `PurchaseOrderDeliveryConfirmationReminder` | 25 |
| `PurchaseOrderDeliveryConfirmationReminderCasualSupplier` | 26 |
| `PurchaseTransportLabel` | 31 |
| `PickingList` | 100 |
| `InspectionReport` | 101 |
| `PurchaseTransportLabelForRejection` | 102 |
| `ProformaInvoice` | 103 |
| `ComprehensiveProformaInvoice` | 104 |
| `ManufacturingTransportLabelA4` | 105 |
| `ManufacturingTransportLabelA4ForRejection` | 106 |
| `ManufacturingTransportLabelA4InProgress` | 107 |
| `ManufacturingTransportLabelA4BeforeReporting` | 108 |
| `ManufacturingOrderOperation` | 109 |
| `ManufacturingOrderMaterial` | 110 |
| `ManufacturingOrderTraveler` | 111 |
| `PreCalculationSummary` | 112 |
| `SubcontractPurchaseOrder` | 113 |
| `SubcontractDeliveryNote` | 114 |
| `SubcontractTransportLabelA4` | 117 |
| `SubcontractTransportLabelA5` | 118 |
| `SubcontractTransportLabelSmall` | 119 |
| `LevelListWhereUsedList` | 120 |
| `LevelListConsistsOfList` | 122 |
| `PostCalculationSummary` | 123 |
| `PhysicalInventoryList` | 124 |
| `MaterialClearanceShortageList` | 125 |
| `AccountingOrder` | 126 |
| `GeneralLedgerDrilldown` | 127 |
| `JournalDrilldown` | 128 |
| `ManufacturingPickingList` | 129 |
| `ManufacturingPickingListGroupByOrder` | 130 |
| `ManufacturingPickingListGroupByMaterial` | 131 |
| `AccountingReportHeader` | 132 |
| `InternalInvoice` | 133 |
| `CashReceipt` | 134 |
| `AccountsReceivableLedger` | 135 |
| `AccountsReceivableLedgerReprint` | 136 |
| `IncomingPaymentLedger` | 137 |
| `IncomingPaymentLedgerReprint` | 138 |
| `AccountsPayableLedger` | 139 |
| `AccountsPayableLedgerReprint` | 140 |
| `PreliminaryAccountsPayableLedger` | 141 |
| `PreliminaryAccountsPayableLedgerReprint` | 142 |
| `CancelledAccountsPayableLedger` | 143 |
| `CancelledAccountsPayableLedgerReprint` | 144 |
| `CancelledPreliminaryAccountsPayableLedger` | 145 |
| `CancelledPreliminaryAccountsPayableLedgerReprint` | 146 |
| `PaymentReminder` | 147 |
| `PaymentReminderReprint` | 148 |
| `AccrualAccountingLedger` | 149 |
| `AccrualAccountingLedgerReprint` | 150 |
| `VatReport` | 151 |
| `VatReportAccounts` | 152 |
| `VatReportGeneralLedger` | 153 |
| `VatReportTransactions` | 154 |
| `VatReportCheck` | 155 |
| `VatReportDifferenceSearch` | 156 |
| `TransactionList` | 157 |
| `OutgoingPaymentLedger` | 158 |
| `OutgoingPaymentLedgerReprint` | 159 |
| `SalesTransportLabelA5` | 160 |
| `CustomerCaseConfirmation` | 161 |
| `AccountStatement` | 162 |
| `CustomerCaseAnswer` | 163 |
| `CustomerNonconformityReport` | 164 |
| `SupplierNonconformityReport` | 165 |
| `InternalNonconformityReport` | 166 |
| `SupplierClaimReport` | 167 |
| `CancelledAccountsReceivableLedger` | 168 |
| `CancelledAccountsReceivableLedgerReprint` | 169 |
| `ShipmentWayBill` | 170 |
| `ShipmentParcel` | 171 |
| `Inquiry` | 172 |
| `CustomerOrderPickingList` | 173 |
| `EimInvoiceInformation` | 174 |
| `InterestInvoice` | 175 |
| `FileLink` | 176 |
| `RecordingsAndSalaryTypeSummary` | 177 |
| `ProductRecordConsistsOf` | 178 |
| `ProductRecordIncludedIn` | 179 |
| `InternalProjectReport` | 180 |
| `ExternalProjectReport` | 181 |
| `TraceabilityProtocol` | 182 |
| `FixedAssetLedger` | 183 |
| `FixedAssetLedgerReprint` | 184 |
| `CustomReport` | 185 |
| `StockAcknowledgement` | 186 |
| `StockDeliveryNote` | 187 |
| `StockPurchaseOrder` | 188 |
| `StockDeliveryNoteDelivered` | 189 |
| `PurchaseOrderModified` | 190 |
| `TaxDepreciation` | 191 |
| `TaxDepreciationDrilldown` | 192 |
| `PartTransportLabelSmall` | 193 |
| `PartTransportLabelA5` | 194 |
| `PartTransportLabelA4` | 195 |
| `UnplannedStockBalanceChangeLedger` | 196 |
| `UnplannedStockBalanceChangeLedgerReprint` | 197 |
| `PIADetailed` | 198 |
| `StockTransactionLogLedger` | 199 |
| `ManufacturingOrderLogLedger` | 200 |
| `InvoiceLogLedger` | 201 |
| `PriceChangeLogLedger` | 202 |
| `CalculationDifferenceLedger` | 203 |
| `AccountStatementBalancePerCustomer` | 204 |
| `StockTransactionLogLedgerReprint` | 205 |
| `ManufacturingOrderLogLedgerReprint` | 206 |
| `PriceChangeLogLedgerReprint` | 207 |
| `CalculationDifferenceLedgerReprint` | 208 |
| `InvoiceLogLedgerReprint` | 209 |
| `PrintoutDemoCertificate` | 210 |
| `BlanketOrderPurchase` | 211 |
| `ArrivalNote` | 212 |
| `CorrectionInvoice` | 213 |
| `ModifiedOrderConfirmation` | 214 |
| `PurchaseDeliverySchedule` | 215 |
| `PackageList` | 216 |
| `PackageTransportLabel` | 217 |
| `AnnualVolumeList` | 218 |
| `BlanketOrderSales` | 219 |
| `TransportLabelDirectWithdrawalA4` | 220 |
| `TransportLabelDirectWithdrawalA5` | 221 |
| `TransportLabelDirectWithdrawalSmall` | 222 |
| `TransportLabelDirectArrivalA4` | 223 |
| `TransportLabelDirectArrivalA5` | 224 |
| `TransportLabelDirectArrivalSmall` | 225 |
| `TransportLabelMoveBetweenLocationsA4` | 226 |
| `TransportLabelMoveBetweenLocationsA5` | 227 |
| `TransportLabelMoveBetweenLocationsSmall` | 228 |
| `TransportLabelMoveBetweenWarehousesA4` | 229 |
| `TransportLabelMoveBetweenWarehousesA5` | 230 |
| `TransportLabelMoveBetweenWarehousesSmall` | 231 |
| `Standard8DNonconformityReport` | 232 |
| `PaymentLedger` | 233 |
| `PaymentLedgerReprint` | 234 |
| `PaymentVoucher` | 235 |
| `DebtorStatement` | 236 |
| `CreditorStatement` | 237 |
| `PrintVoucher` | 238 |
| `OfficialReceipt` | 239 |
| `PolishCashReceipt` | 240 |
| `PolishCashReport` | 241 |
| `Standard8DCustomerNonconformityReport` | 242 |
| `AutoCodingLedger` | 243 |
| `AutoCodingLedgerReprint` | 244 |
| `MeasuringProtocolManufacturing` | 245 |
| `MeasuringProtocolPurchase` | 246 |
| `VoucherList` | 247 |
| `RevenueCalculationLedger` | 248 |
| `RevenueCalculationLedgerReprint` | 249 |
| `GeneralActivityList` | 250 |
| `ReturnPurchaseOrderDeliveryNote` | 251 |
| `ReturnPurchaseOrderProforma` | 252 |
| `ReturnPurchaseOrderTransportLabelA4` | 253 |
| `ReturnPurchaseOrderTransportLabelA5` | 254 |
| `ReturnPurchaseOrderTransportLabelSmall` | 255 |
| `Waybill` | 256 |
| `ShipmentAdvice` | 257 |
| `PartTransportMultiLabel` | 258 |
| `StockTransportMultiLabel` | 259 |
| `SustainabilityCalculationDetailed` | 260 |
| `ShipmentReceipt` | 261 |
| `OrderRowDiscounts` | 262 |
| `BankAccountReconciliation` | 263 |
| `CollectiveCorrectionInvoice` | 264 |
| `ExternalCustomerNonconformityReport` | 265 |
| `ExternalSupplierNonconformityReport` | 266 |
| `ExternalInternalNonconformityReport` | 267 |
| `PartContentDeliveryReport` | 268 |
| `ProjectMaterialCalculationLedger` | 269 |
| `ProjectMaterialCalculationLedgerReprint` | 270 |
| `CausesForShortage` | 271 |
| `CustomerLevelListConsistsOfList` | 272 |
| `CustomerLevelListIncludedInList` | 273 |
| `SupplierLevelListConsistsOfList` | 274 |
| `SupplierLevelListIncludedInList` | 275 |
| `GPBForm` | 276 |
| `CurrencyWarehouse` | 277 |
| `ReturnPurchaseOrderPickingList` | 278 |
| `SubcontractProformaInvoice` | 279 |
| `LocationLabel` | 280 |
| `LocationMultiLabel` | 281 |
| `FilesExternal1` | 282 |
| `FilesExternal2` | 283 |
| `FilesExternal3` | 284 |
| `RemittanceAdvice` | 285 |
| `SupplierAgreement` | 286 |
| `ModifiedSupplierAgreement` | 287 |
| `SelfBilledInvoice` | 288 |
| `PurchaseTransportLabelA5` | 310 |
| `RefillPickingLocationStandard` | 500 |
| `PurchaseTransportLabelA5ForRejection` | 1020 |
| `ManufacturingTransportLabelA5` | 1050 |
| `ManufacturingTransportLabelA5ForRejection` | 1060 |
| `ManufacturingTransportLabelA5InProgress` | 1070 |
| `ManufacturingTransportLabelA5BeforeReporting` | 1080 |
| `SalesTransportLabelSmall` | 1600 |
| `Form` | 2401 |
| `ServiceReporting` | 2402 |
| `SalesAgreement` | 2501 |
| `ModifiedSalesAgreement` | 2502 |
| `AccountStatementPurchase` | 2503 |
| `ReturnPurchaseOrder` | 2504 |
| `PurchaseTransportLabelSmall` | 3100 |
| `PurchaseTransportLabelSmallForRejection` | 10200 |
| `ManufacturingTransportLabelSmall` | 10500 |
| `ManufacturingTransportLabelSmallForRejection` | 10600 |
| `ManufacturingTransportLabelSmallInProgress` | 10700 |
| `ManufacturingTransportLabelSmallBeforeReporting` | 10800 |
| `DebitNote` | 10801 |
| `ServiceTax` | 10802 |
| `EdiCustomerOrderConfirmation` | 20001 |
| `EdiCustomerOrderInvoice` | 20002 |
| `EdiCustomerOrderSimpleDispatchAdvice` | 20003 |
| `EdiCustomerOrderResponse` | 20004 |
| `EdiPurchaseOrder` | 20005 |
| `EdiCustomerOrderComplexDispatchAdvice` | 20006 |
| `EdiPurchaseDeliverySchedule` | 20007 |

### FormDocumentType

| Name | Value |
| --- | ---: |
| `Document` | 0 |
| `AdaptedReport` | 1 |


## Referenced by

**Common**

- [ApplicationUsers](/entities/Common/ApplicationUser.md) — `Printers` (expand)


## Example

```json
{
  "Id": 0,
  "ApplicationUserId": 0,
  "PrinterName": null,
  "NormalizedFormReportType": null,
  "FormReportType": null,
  "ServerPrinterId": null,
  "FormDocumentType": 0
}
```
