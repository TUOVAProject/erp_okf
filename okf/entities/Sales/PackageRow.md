---
type: API Entity
title: PackageRows
description: Represents a package row.
resource: https://api.monitor.se/api/Monitor.API.Sales.PackageRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.PackageRow.html
  title: Monitor API — PackageRow
module: Sales
api_class: PackageRow
doc_name: PackageRows
endpoint: GET /api/v1/Sales/PackageRows
guid: 4CDC166D-5C02-4BF4-A440-D49E727AAFE9
permission: Show customer orders
introduced_in: '25.5'
property_count: 26
references_out:
- /entities/Common/Comment.md
- /entities/Inventory/Part.md
- /entities/Sales/CustomerOrderDeliveryRow.md
- /entities/Sales/PackageRow.md
- /entities/Sales/SalesPickingList.md
referenced_by:
- /entities/Sales/PackageRow.md
- /entities/Sales/PackageRowPartLocation.md
---

# PackageRows

Represents a package row.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `PackageRow`
- **Endpoint:** `GET /api/v1/Sales/PackageRows`
- **Required permission:** Show customer orders
- **GUID:** `4CDC166D-5C02-4BF4-A440-D49E727AAFE9`
- **Introduced in:** 25.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the package row. |
| `ParentId` | `Int64?` | yes | [SalesPickingLists](SalesPickingList.md) |  | The business key identifier of the row's picking list. |
| `ParentRowId` | `Int64?` | yes | [PackageRows](PackageRow.md) |  | The business key identifier of the row's parent row. |
| `CustomerOrderDeliveryRowId` | `Int64?` | yes | [CustomerOrderDeliveryRows](CustomerOrderDeliveryRow.md) |  | The business key identifier of the row's delivery row. |
| `PackagingPartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the packing part. |
| `Cleared` | `Boolean` | no |  |  | Specifies if the row is cleared. |
| `ContainerNumber` | `String` | no |  | max length 80 | The container number of the row. |
| `SealNumber` | `String` | no |  | max length 80 | The seal number of the row. |
| `PackageNumber` | `String` | no |  | max length 80 | The package number of the row. |
| `OtherPackageNumber` | `String` | no |  | max length 80 | The other package number of the row. |
| `OtherPackageNumberNumberSeriesType` | `Int32?` | yes |  | enum | The other package number series type of the row. |
| `ExternalPackageId` | `String` | no |  | max length 80 | The external package id of the row. |
| `Length` | `Decimal?` | yes |  |  | The length of the row's content. |
| `Width` | `Decimal?` | yes |  |  | The width of the row's content. |
| `Height` | `Decimal?` | yes |  |  | The height of the row's content. |
| `Volume` | `Decimal?` | yes |  |  | The volume of the row's content. |
| `VolumeCalculated` | `Decimal` | no |  |  | The calculated volume of the row's content. |
| `GrossWeight` | `Decimal?` | yes |  |  | The gross weight of the row's content. |
| `GrossWeightCalculated` | `Decimal` | no |  |  | The calculated gross weight of the row's content. |
| `ExternalCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the row's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The external comment of the row. |
| `InternalCommentId` | `Int64?` | yes | [Comments](../Common/Comment.md) |  | The business key identifier of the row's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](../Common/Comment.md) | expandable | The internal comment of the row. |
| `PackageComplete` | `Boolean` | no |  |  | Specifies if the package row is complete. |
| `BalanceChange` | `Decimal` | no |  |  | The balance change of the row. |
| `TemplateCode` | `String` | no |  |  | The template code of the row. |

## Enumerations

### OtherPackageNumberNumberSeriesType

| Name | Value |
| --- | ---: |
| `NotInitalized` | 0 |
| `CustomerOrderNumber` | 2 |
| `PurchaseOrderNumber` | 3 |
| `AccountsReceivableNumber` | 4 |
| `SupplierCode` | 5 |
| `CustomerCode` | 6 |
| `AccountsPayableNumber` | 7 |
| `InventoryLogPriceId` | 13 |
| `PickingListNumber` | 14 |
| `AccountsReceivableLedgerNumber` | 15 |
| `RejectionLogId` | 16 |
| `ReportNumberForMaterial` | 17 |
| `ReportNumberForOperation` | 18 |
| `ManufacturingOrderNumber` | 19 |
| `AccountsReceivableNumberCashReceipt` | 20 |
| `AccountsReceivableNumberInterest` | 21 |
| `AccountsReceivableNumberInternal` | 22 |
| `AccountsReceivableNumberCredit` | 23 |
| `ProformaInvoiceNumber` | 24 |
| `DeliveryNoteNumber` | 25 |
| `PhysicalInventoryList` | 27 |
| `VoucherNumber` | 28 |
| `AutoCoding` | 29 |
| `AutoAllocation` | 30 |
| `ManufacturingPickingListNumber` | 31 |
| `AccountsReceivableNumberOnAccount` | 32 |
| `IncomingPaymentsBundleNumber` | 33 |
| `AccrualAccountingNumber` | 34 |
| `ShipmentNumber` | 35 |
| `AccountsPayableNumberOnAccount` | 36 |
| `OutgoingPaymentsBundleNumber` | 37 |
| `CaseNumber` | 38 |
| `TransactionList` | 39 |
| `Quote` | 40 |
| `Inquiry` | 41 |
| `Project` | 43 |
| `ProjectCostReportingEntry` | 44 |
| `FixedAsset` | 45 |
| `EdiFileTransaction` | 46 |
| `ServerPrinterNumber` | 47 |
| `AgentTaskNumber` | 48 |
| `MonitoringTaskNumber` | 49 |
| `DeliverySchedule` | 50 |
| `AccountsReceivableNumberDebitNote` | 51 |
| `AccountsReceivableNumberServiceTax` | 52 |
| `CodingMethod` | 53 |
| `TransferTask` | 54 |
| `BlanketOrderPurchase` | 55 |
| `ArrivalNote` | 56 |
| `GS1Code` | 57 |
| `AccountsReceivableNumberCorrectionInvoice` | 58 |
| `PackageNumber` | 59 |
| `MaintenanceReportingServiceNumber` | 60 |
| `BlanketOrderSales` | 61 |
| `AccountingReport` | 62 |
| `VatReport` | 63 |
| `PaymentBundleNumber` | 64 |
| `PackagingTemplateNumber` | 65 |
| `AllocationKeyNumber` | 66 |
| `PurchaseDeliverySchedule` | 67 |
| `SalesAgreement` | 68 |
| `AccountsReceivableNumberAdvance` | 69 |
| `SsccPackage` | 70 |
| `SalesForecast` | 71 |
| `BankAccountReconciliationReport` | 72 |
| `AccountsReceivableNumberCollectiveCorrectionInvoice` | 73 |
| `OscarPackage` | 74 |
| `DunsPackage` | 75 |
| `JipdecPackage` | 76 |
| `AccountsPayableNumberCorrectionInvoice` | 77 |
| `BusinessOpportunity` | 78 |
| `DeliveryNoteSubcontract` | 79 |
| `SupplierAgreement` | 80 |


## Referenced by

**Sales**

- [PackageRowPartLocations](PackageRowPartLocation.md) — `ParentPackageRowId` (FK)
- [PackageRows](PackageRow.md) — `ParentRowId` (FK)


## Example

```json
{
  "Id": 0,
  "ParentId": null,
  "ParentRowId": null,
  "CustomerOrderDeliveryRowId": null,
  "PackagingPartId": null,
  "Cleared": false,
  "ContainerNumber": null,
  "SealNumber": null,
  "PackageNumber": null,
  "OtherPackageNumber": null,
  "OtherPackageNumberNumberSeriesType": null,
  "ExternalPackageId": null,
  "Length": null,
  "Width": null,
  "Height": null,
  "Volume": null,
  "VolumeCalculated": 0.0,
  "GrossWeight": null,
  "GrossWeightCalculated": 0.0,
  "ExternalCommentId": null,
  "ExternalComment": null,
  "InternalCommentId": null,
  "InternalComment": null,
  "PackageComplete": false,
  "BalanceChange": 0.0,
  "TemplateCode": null
}
```
