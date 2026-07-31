---
type: API Entity
title: SalesAgreementRows
description: Represents an agreement row.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreementRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreementRow.html
  title: Monitor API — SalesAgreementRow
module: Sales
api_class: SalesAgreementRow
doc_name: SalesAgreementRows
endpoint: GET /api/v1/Sales/SalesAgreementRows
guid: 9EEE0EA1-560D-4530-809D-1B42FEAF6CB7
permission: Show agreement
introduced_in: '22.7'
property_count: 59
references_out:
- /entities/Accounting/Coding.md
- /entities/Common/Currency.md
- /entities/Common/Revision.md
- /entities/Common/Unit.md
- /entities/Common/VatRate.md
- /entities/Inventory/Part.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/SalesAgreementRow.md
referenced_by:
- /entities/Sales/SalesAgreement.md
- /entities/Sales/SalesAgreementBasisRow.md
- /entities/Sales/SalesAgreementRow.md
- /entities/Sales/SalesAgreementRowInflow.md
---

# SalesAgreementRows

Represents an agreement row.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `SalesAgreementRow`
- **Endpoint:** `GET /api/v1/Sales/SalesAgreementRows`
- **Required permission:** Show agreement
- **GUID:** `9EEE0EA1-560D-4530-809D-1B42FEAF6CB7`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the row. |
| `ParentRowId` | `Int64?` | yes | [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) |  | The business key identifier of the rows parent row. |
| `ParentOrderId` | `Int64` | no | [SalesAgreements](/entities/Sales/SalesAgreement.md) |  | The business key identifier of the rows parent agreement. |
| `Position` | `Int64?` | yes |  |  | The position of the row. |
| `OrderRowType` | `Int32` | no |  | enum | The order row type of the row. |
| `PartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the rows part. |
| `AdditionalRowDescription` | `String` | no |  |  | The additional row description of the row. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the row. |
| `FutureQuantity` | `Decimal?` | yes |  |  | The future quantity of the row. |
| `PreviousQuantity` | `Decimal?` | yes |  |  | The previous quantity of the row. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor of the row. |
| `UnitId` | `Int64?` | yes | [Units](/entities/Common/Unit.md) |  | The business key identifier of the rows unit. |
| `Unit` | `Units` | no | [Units](/entities/Common/Unit.md) | expandable | The unit of the row. |
| `Price` | `Decimal?` | yes |  |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the rows price currency. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The rows price in the company currency. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the company currency. |
| `FuturePriceAmount` | `Decimal?` | yes |  |  | The future price amount of the row. |
| `PreviousPriceAmount` | `Decimal?` | yes |  |  | The previous price amount of the row. |
| `Discount` | `Decimal` | no |  |  | The discount of the row. |
| `VatRateId` | `Int64` | no | [VatRates](/entities/Common/VatRate.md) |  | The business key identifier of the rows VAT rate. |
| `FutureValidFrom` | `DateTimeOffset?` | yes |  |  | The future valid from of the row. |
| `PreviousValidThrough` | `DateTimeOffset?` | yes |  |  | The previous valid through of the row. |
| `CustomerPartNumber` | `String` | no |  | max length 20 | The customer part number of the row. |
| `PartRowType` | `Int32` | no |  | enum | The part row type of the row. |
| `SetupPrice` | `Decimal?` | yes |  | **deprecated since 22.7** | The setup price of the row. _(Setup price has never been used in sales agreements. One time cost rows are used instead.)_ |
| `SetupPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) | **deprecated since 22.7** | The business key identifier of the rows setup price currency. _(Setup price has never been used in sales agreements. One time cost rows are used instead.)_ |
| `SetupPriceInCompanyCurrency` | `Decimal?` | yes |  | **deprecated since 22.7** | The setup price in company currency of the row. _(Setup price has never been used in sales agreements. One time cost rows are used instead.)_ |
| `SetupPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) | **deprecated since 22.7** | The business key identifier of the company currency. _(Setup price has never been used in sales agreements. One time cost rows are used instead.)_ |
| `ShowFreeTextIn` | `Int32` | no |  | bitmask, enum | Specifies which documents the free text data of the row should be projected on. |
| `RevisionId` | `Int64?` | yes | [Revisions](/entities/Common/Revision.md) |  | The business key identifier of the revision of the rows part. |
| `Revision` | `Revisions` | no | [Revisions](/entities/Common/Revision.md) | expandable | The revision of the row's part. |
| `FreeTextHtml` | `String` | no |  |  | The free text formatted as rich text HTML of the row. |
| `FreeText` | `String` | no |  |  | The free text as raw text of the row. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the row. |
| `QuantityRatio` | `Decimal?` | yes |  |  | The quantity ratio of the row. |
| `CodingId` | `Int64?` | yes | [Codings](/entities/Accounting/Coding.md) |  | The business key identifier of the rows coding. |
| `Coding` | `Codings` | no | [Codings](/entities/Accounting/Coding.md) | expandable | The coding of the row. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |  | The delivery date of the row. |
| `CompensatedRowId` | `Int64?` | yes | [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) |  | The business key identifier of the row compensated for this row. |
| `OneTimeCostType` | `Int32` | no |  | enum | The one time cost type of the row. |
| `PeriodStart` | `DateTimeOffset?` | yes |  |  | The period start of the row. |
| `PeriodEnd` | `DateTimeOffset?` | yes |  |  | The period end of the row. |
| `PlannedInvoiceDate` | `DateTimeOffset?` | yes |  |  | The planned invoice date of the row. |
| `StandardPrice` | `Decimal?` | yes |  |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the rows standard price currency. |
| `FutureDiscount` | `Decimal?` | yes |  |  | The future discount of the row. |
| `PreviousDiscount` | `Decimal?` | yes |  |  | The previous discount of the row. |
| `IsAccrual` | `Boolean` | no |  |  | Indicates if the row is accrual. |
| `ValidFrom` | `DateTimeOffset?` | yes |  |  | The valid from date of the row. |
| `ValidTo` | `DateTimeOffset?` | yes |  |  | The valid to date of the row. |
| `FuturePriceInCompanyCurrencyAmount` | `Decimal?` | yes |  |  | The future price in company currency amount of the row. |
| `PreviousPriceInCompanyCurrencyAmount` | `Decimal?` | yes |  |  | The previous price in company currency amount of the row. |
| `EntityIdentityString` | `String` | no |  | max length 20 | The entity identity string of the row. |
| `ExtraFieldBool` | `Boolean` | no |  | since 23.8 | An extra field of type bool. |
| `ExtraFieldInteger` | `Int32?` | yes |  | since 23.8 | An extra field of type integer. |
| `ExtraFieldDecimal` | `Decimal?` | yes |  | since 23.8 | An extra field of type decimal. |
| `ExtraFieldDate` | `DateTimeOffset?` | yes |  | since 23.8 | An extra field of type date. |
| `ExtraFieldText` | `String` | no |  | max length 80, since 23.8 | An extra field of type text. |

## Enumerations

### OrderRowType

| Name | Value |
| --- | ---: |
| `Part` | 1 |
| `Additional` | 2 |
| `Sum` | 3 |
| `FreeText` | 4 |

### PartRowType

| Name | Value |
| --- | ---: |
| `NotPartRow` | 0 |
| `RegularRow` | 1 |
| `SubPartRow` | 2 |
| `SetupPriceRow` | 3 |
| `AlloyCostRow` | 4 |
| `PaymentPlanRow` | 5 |
| `PackagingRow` | 6 |

### ShowFreeTextIn (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Quote` | 1 |
| `Acknowledgement` | 2 |
| `DeliveryNote` | 4 |
| `Invoice` | 8 |
| `ProFormaInvoice` | 16 |

### LifeCycleState

| Name | Value |
| --- | ---: |
| `Transient` | 1 |
| `Persistent` | 10 |
| `History` | 20 |
| `RemovableCandidate` | 99 |

### OneTimeCostType

| Name | Value |
| --- | ---: |
| `No` | 0 |
| `AddToExistingAgreementBasis` | 1 |
| `CreateNewAgreementBasis` | 2 |


## Referenced by

**Sales**

- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `AgreementRowId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `SalesAgreementRowId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `CompensatedRowId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `ParentRowId` (FK)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `Rows` (expand)


## Example

```json
{
  "Id": 0,
  "ParentRowId": null,
  "ParentOrderId": 0,
  "Position": null,
  "OrderRowType": 0,
  "PartId": null,
  "AdditionalRowDescription": null,
  "Quantity": 0.0,
  "FutureQuantity": null,
  "PreviousQuantity": null,
  "ConversionFactor": 0.0,
  "UnitId": null,
  "Unit": null,
  "Price": null,
  "PriceCurrencyId": null,
  "PriceInCompanyCurrency": null,
  "PriceInCompanyCurrencyCurrencyId": null,
  "FuturePriceAmount": null,
  "PreviousPriceAmount": null,
  "Discount": 0.0,
  "VatRateId": 0,
  "FutureValidFrom": null,
  "PreviousValidThrough": null,
  "CustomerPartNumber": null,
  "PartRowType": 0,
  "SetupPrice": null,
  "SetupPriceCurrencyId": null,
  "SetupPriceInCompanyCurrency": null,
  "SetupPriceInCompanyCurrencyCurrencyId": null,
  "ShowFreeTextIn": 0,
  "RevisionId": null,
  "Revision": null,
  "FreeTextHtml": null,
  "FreeText": null,
  "LifeCycleState": 0,
  "QuantityRatio": null,
  "CodingId": null,
  "Coding": null,
  "DeliveryDate": null,
  "CompensatedRowId": null,
  "OneTimeCostType": 0,
  "PeriodStart": null,
  "PeriodEnd": null,
  "PlannedInvoiceDate": null,
  "StandardPrice": null,
  "StandardPriceCurrencyId": null,
  "FutureDiscount": null,
  "PreviousDiscount": null,
  "IsAccrual": false,
  "ValidFrom": null,
  "ValidTo": null,
  "FuturePriceInCompanyCurrencyAmount": null,
  "PreviousPriceInCompanyCurrencyAmount": null,
  "EntityIdentityString": null,
  "ExtraFieldBool": false,
  "ExtraFieldInteger": null,
  "ExtraFieldDecimal": null,
  "ExtraFieldDate": null,
  "ExtraFieldText": null
}
```
