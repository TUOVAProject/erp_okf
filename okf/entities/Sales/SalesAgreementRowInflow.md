---
type: API Entity
title: SalesAgreementRowInflows
description: Represents a sales agreement inflow row.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreementRowInflow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreementRowInflow.html
  title: Monitor API — SalesAgreementRowInflow
module: Sales
api_class: SalesAgreementRowInflow
doc_name: SalesAgreementRowInflows
endpoint: GET /api/v1/Sales/SalesAgreementRowInflows
guid: 530d3209-85ab-498d-8b73-7d21ecb03f1d
permission: Show agreement
introduced_in: '26.4'
property_count: 43
references_out:
- /entities/Common/Currency.md
- /entities/Inventory/Part.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/SalesAgreementRow.md
---

# SalesAgreementRowInflows

Represents a sales agreement inflow row.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `SalesAgreementRowInflow`
- **Endpoint:** `GET /api/v1/Sales/SalesAgreementRowInflows`
- **Required permission:** Show agreement
- **GUID:** `530d3209-85ab-498d-8b73-7d21ecb03f1d`
- **Introduced in:** 26.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the inflow row. |
| `CreationTime` | `DateTimeOffset?` | yes |  |  | The creation time of the inflow row. |
| `LoggingTimeStamp` | `DateTimeOffset` | no |  |  | The logging timestamp of the inflow row. |
| `OrderRowType` | `Int32` | no |  | enum | The order row type of the inflow row. |
| `PartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the inflow rows part. |
| `AdditionalRowDescription` | `String` | no |  | max length 80 | The additional row description of the inflow row. |
| `SalesAgreementId` | `Int64?` | yes | [SalesAgreements](SalesAgreement.md) |  | The business key identifier of the inflow rows sales agreement. |
| `SalesAgreementRowId` | `Int64?` | yes | [SalesAgreementRows](SalesAgreementRow.md) |  | The business key identifier of the inflow rows sales agreement row. |
| `OrderedQuantityChange` | `Decimal?` | yes |  |  | The ordered quantity change of the inflow row. |
| `PriceChange` | `Decimal?` | yes |  |  | The price change of the inflow row. |
| `PriceChangeCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the price change currency. |
| `PriceChangeCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The price change currency. |
| `PriceChangeInCompanyCurrency` | `Decimal?` | yes |  |  | The price change in company currency of the inflow row. |
| `PriceChangeInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the price change in company currency. |
| `PriceChangeInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The price change in company currency. |
| `DiscountChange` | `Decimal?` | yes |  |  | The discount change of the inflow row. |
| `TotalValueChange` | `Decimal` | no |  |  | The total value change of the inflow row. |
| `TotalValueChangeCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the total value change currency. |
| `TotalValueChangeCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The total value change currency. |
| `TotalValueChangeInCompanyCurrency` | `Decimal` | no |  |  | The total value change in company currency of the inflow row. |
| `TotalValueChangeInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the total value change in company currency. |
| `TotalValueChangeInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The total value change in company currency. |
| `RowTotalValue` | `Decimal` | no |  |  | The row total value of the inflow row. |
| `RowTotalValueCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row total value currency. |
| `RowTotalValueCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The row total value currency. |
| `RowTotalValueInCompanyCurrency` | `Decimal` | no |  |  | The row total value in company currency of the inflow row. |
| `RowTotalValueInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the row total value in company currency. |
| `RowTotalValueInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The row total value in company currency. |
| `RowTotalQuantity` | `Decimal` | no |  |  | The row total quantity of the inflow row. |
| `IsOneTimeCost` | `Boolean` | no |  |  | Whether the inflow row is a one-time cost. |
| `SalesAgreementInvoicingInterval` | `Int32` | no |  | enum | The invoicing interval of the inflow row. |
| `TypeOfChange` | `Int32` | no |  | enum | The type of change of the inflow row. |
| `PriceDefinition` | `Int32` | no |  | enum | The price definition of the inflow row. |
| `PriceChangePerInterval` | `Decimal?` | yes |  |  | The price change per interval of the inflow row. |
| `PriceChangePerIntervalCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the price change per interval currency. |
| `PriceChangePerIntervalCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The price change per interval currency. |
| `PriceChangePerIntervalInCompanyCurrency` | `Decimal?` | yes |  |  | The price change per interval in company currency of the inflow row. |
| `PriceChangePerIntervalInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the price change per interval in company currency. |
| `PriceChangePerIntervalInCompanyCurrencyCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The price change per interval in company currency. |
| `TotalValueChangePerInterval` | `Decimal` | no |  |  | The total value change per interval of the inflow row. |
| `TotalValueChangePerIntervalInCompanyCurrency` | `Decimal` | no |  |  | The total value change per interval in company currency of the inflow row. |
| `RowTotalValuePerInterval` | `Decimal` | no |  |  | The row total value per interval of the inflow row. |
| `RowTotalValuePerIntervalInCompanyCurrency` | `Decimal` | no |  |  | The row total value per interval in company currency of the inflow row. |

## Enumerations

### OrderRowType

| Name | Value |
| --- | ---: |
| `Part` | 1 |
| `Additional` | 2 |
| `Sum` | 3 |
| `FreeText` | 4 |

### SalesAgreementInvoicingInterval

| Name | Value |
| --- | ---: |
| `Monthly` | 1 |
| `EveryOtherMonth` | 2 |
| `Quarterly` | 3 |
| `FourMonthly` | 4 |
| `SemiAnnually` | 5 |
| `Annually` | 6 |

### TypeOfChange

| Name | Value |
| --- | ---: |
| `NewRow` | 0 |
| `Upgrade` | 1 |
| `Downgrade` | 2 |
| `Churn` | 3 |
| `PriceChange` | 4 |

### PriceDefinition

| Name | Value |
| --- | ---: |
| `AccordingToInvoicingInterval` | 0 |
| `Day` | 1 |
| `Week` | 2 |
| `Month` | 3 |
| `TwoMonths` | 4 |
| `Quarter` | 5 |
| `FourMonths` | 6 |
| `SixMonths` | 7 |
| `Annual` | 8 |


## Example

```json
{
  "Id": 0,
  "CreationTime": null,
  "LoggingTimeStamp": "0001-01-01T00:00:00+00:00",
  "OrderRowType": 0,
  "PartId": null,
  "AdditionalRowDescription": null,
  "SalesAgreementId": null,
  "SalesAgreementRowId": null,
  "OrderedQuantityChange": null,
  "PriceChange": null,
  "PriceChangeCurrencyId": null,
  "PriceChangeCurrency": null,
  "PriceChangeInCompanyCurrency": null,
  "PriceChangeInCompanyCurrencyCurrencyId": null,
  "PriceChangeInCompanyCurrencyCurrency": null,
  "DiscountChange": null,
  "TotalValueChange": 0.0,
  "TotalValueChangeCurrencyId": null,
  "TotalValueChangeCurrency": null,
  "TotalValueChangeInCompanyCurrency": 0.0,
  "TotalValueChangeInCompanyCurrencyCurrencyId": null,
  "TotalValueChangeInCompanyCurrencyCurrency": null,
  "RowTotalValue": 0.0,
  "RowTotalValueCurrencyId": null,
  "RowTotalValueCurrency": null,
  "RowTotalValueInCompanyCurrency": 0.0,
  "RowTotalValueInCompanyCurrencyCurrencyId": null,
  "RowTotalValueInCompanyCurrencyCurrency": null,
  "RowTotalQuantity": 0.0,
  "IsOneTimeCost": false,
  "SalesAgreementInvoicingInterval": 0,
  "TypeOfChange": 0,
  "PriceDefinition": 0,
  "PriceChangePerInterval": null,
  "PriceChangePerIntervalCurrencyId": null,
  "PriceChangePerIntervalCurrency": null,
  "PriceChangePerIntervalInCompanyCurrency": null,
  "PriceChangePerIntervalInCompanyCurrencyCurrencyId": null,
  "PriceChangePerIntervalInCompanyCurrencyCurrency": null,
  "TotalValueChangePerInterval": 0.0,
  "TotalValueChangePerIntervalInCompanyCurrency": 0.0,
  "RowTotalValuePerInterval": 0.0,
  "RowTotalValuePerIntervalInCompanyCurrency": 0.0
}
```
