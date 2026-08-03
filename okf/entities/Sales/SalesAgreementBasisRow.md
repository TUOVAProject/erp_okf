---
type: API Entity
title: SalesAgreementBasisRows
description: Represents a sales agreement basis row.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreementBasisRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreementBasisRow.html
  title: Monitor API — SalesAgreementBasisRow
module: Sales
api_class: SalesAgreementBasisRow
doc_name: SalesAgreementBasisRows
endpoint: GET /api/v1/Sales/SalesAgreementBasisRows
guid: 1e49a395-9918-4583-9a00-ffe5d1be4efd
permission: Show agreement
introduced_in: '26.4'
property_count: 32
references_out:
- /entities/Common/Currency.md
- /entities/Common/Unit.md
- /entities/Common/VatRate.md
- /entities/Inventory/Part.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/SalesAgreementBasis.md
- /entities/Sales/SalesAgreementBasisRow.md
- /entities/Sales/SalesAgreementRow.md
referenced_by:
- /entities/Sales/SalesAgreementBasis.md
- /entities/Sales/SalesAgreementBasisRow.md
---

# SalesAgreementBasisRows

Represents a sales agreement basis row.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `SalesAgreementBasisRow`
- **Endpoint:** `GET /api/v1/Sales/SalesAgreementBasisRows`
- **Required permission:** Show agreement
- **GUID:** `1e49a395-9918-4583-9a00-ffe5d1be4efd`
- **Introduced in:** 26.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the agreement basis row. |
| `ParentRowId` | `Int64?` | yes | [SalesAgreementBasisRows](SalesAgreementBasisRow.md) |  | The business key identifier of the parent row. |
| `ParentAgreementBasisId` | `Int64` | no | [SalesAgreementBases](SalesAgreementBasis.md) |  | The business key identifier of the parent agreement basis. |
| `AgreementRowId` | `Int64` | no | [SalesAgreementRows](SalesAgreementRow.md) |  | The business key identifier of the source agreement row. |
| `CustomerOrderRowId` | `Int64` | no | [CustomerOrderRows](CustomerOrderRow.md) |  | The business key identifier of the generated customer order row. |
| `OrderRowType` | `Int32` | no |  | enum | The order row type of the row. |
| `PartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the row's part. |
| `EntityIdentityString` | `String` | no |  | max length 20 | The entity identity string of the row. |
| `AdditionalRowDescription` | `String` | no |  |  | The additional row description of the row. |
| `FreeTextHtml` | `String` | no |  |  | The free text formatted as rich text HTML of the row. |
| `FreeText` | `String` | no |  |  | The free text as raw text of the row. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the row. |
| `ConversionFactor` | `Decimal` | no |  |  | The conversion factor of the row. |
| `UnitId` | `Int64?` | yes | [Units](../Common/Unit.md) |  | The business key identifier of the row's unit. |
| `Unit` | `Units` | no | [Units](../Common/Unit.md) | expandable | The unit of the row. |
| `MileageHours` | `Decimal` | no |  |  | The mileage hours of the row. |
| `Price` | `Decimal?` | yes |  |  | The price of the row. |
| `PriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's price currency. |
| `PriceCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The price currency of the row. |
| `PriceInCompanyCurrency` | `Decimal?` | yes |  |  | The price in company currency of the row. |
| `PriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the company currency. |
| `PriceInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The company currency of the row's price. |
| `Discount` | `Decimal` | no |  |  | The discount of the row. |
| `StandardPrice` | `Decimal?` | yes |  |  | The standard price of the row. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row's standard price currency. |
| `StandardPriceCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The standard price currency of the row. |
| `Amount` | `Decimal` | no |  |  | The total amount of the row. |
| `AmountInCompanyCurrency` | `Decimal` | no |  |  | The total amount in company currency of the row. |
| `VatRateId` | `Int64` | no | [VatRates](../Common/VatRate.md) |  | The business key identifier of the row's VAT rate. |
| `IsOneTimeCost` | `Boolean` | no |  |  | Indicates if the row is a one-time cost. |
| `PeriodStart` | `DateTimeOffset?` | yes |  |  | The period start date of the row. |
| `PeriodEnd` | `DateTimeOffset?` | yes |  |  | The period end date of the row. |

## Enumerations

### OrderRowType

| Name | Value |
| --- | ---: |
| `Part` | 1 |
| `Additional` | 2 |
| `Sum` | 3 |
| `FreeText` | 4 |


## Referenced by

**Sales**

- [SalesAgreementBases](SalesAgreementBasis.md) — `Rows` (expand)
- [SalesAgreementBasisRows](SalesAgreementBasisRow.md) — `ParentRowId` (FK)


## Example

```json
{
  "Id": 0,
  "ParentRowId": null,
  "ParentAgreementBasisId": 0,
  "AgreementRowId": 0,
  "CustomerOrderRowId": 0,
  "OrderRowType": 0,
  "PartId": null,
  "EntityIdentityString": null,
  "AdditionalRowDescription": null,
  "FreeTextHtml": null,
  "FreeText": null,
  "Quantity": 0.0,
  "ConversionFactor": 0.0,
  "UnitId": null,
  "Unit": null,
  "MileageHours": 0.0,
  "Price": null,
  "PriceCurrencyId": null,
  "PriceCurrency": null,
  "PriceInCompanyCurrency": null,
  "PriceInCompanyCurrencyCurrencyId": null,
  "PriceInCompanyCurrencyCurrency": null,
  "Discount": 0.0,
  "StandardPrice": null,
  "StandardPriceCurrencyId": null,
  "StandardPriceCurrency": null,
  "Amount": 0.0,
  "AmountInCompanyCurrency": 0.0,
  "VatRateId": 0,
  "IsOneTimeCost": false,
  "PeriodStart": null,
  "PeriodEnd": null
}
```
