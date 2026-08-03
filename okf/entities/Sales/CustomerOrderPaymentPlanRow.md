---
type: API Entity
title: CustomerOrderPaymentPlanRows
description: Represents a customer order payment plan row.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderPaymentPlanRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerOrderPaymentPlanRow.html
  title: Monitor API — CustomerOrderPaymentPlanRow
module: Sales
api_class: CustomerOrderPaymentPlanRow
doc_name: CustomerOrderPaymentPlanRows
endpoint: GET /api/v1/Sales/CustomerOrderPaymentPlanRows
guid: E30E5D6E-3753-4F16-A5BC-605083F4816C
permission: Show customer orders
introduced_in: '22.7'
property_count: 18
references_out:
- /entities/Accounting/CodingEntry.md
- /entities/Common/Currency.md
- /entities/Common/PaymentTerm.md
- /entities/Common/VatRate.md
- /entities/Inventory/Part.md
- /entities/Sales/CustomerOrder.md
---

# CustomerOrderPaymentPlanRows

Represents a customer order payment plan row.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerOrderPaymentPlanRow`
- **Endpoint:** `GET /api/v1/Sales/CustomerOrderPaymentPlanRows`
- **Required permission:** Show customer orders
- **GUID:** `E30E5D6E-3753-4F16-A5BC-605083F4816C`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer order payment plan row. |
| `CustomerOrderId` | `Int64` | no | [CustomerOrders](CustomerOrder.md) |  | The business key identifier of the customer order this row belongs to. |
| `InvoicingPeriod` | `DateTimeOffset?` | yes |  |  | The invoicing period of the row. |
| `VatRateId` | `Int64?` | yes | [VatRates](../Common/VatRate.md) |  | The business key identifier of the VAT rate of the row. |
| `Amount` | `Decimal` | no |  |  | The amount of the row. |
| `AmountCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the currency for the rows amount. |
| `AmountInCompanyCurrency` | `Decimal` | no |  |  | The amount in company currency of the row. |
| `AmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the currency for the rows amount in company currency. |
| `ReducedAmountInCompanyCurrency` | `Decimal?` | yes |  |  | The reduced amount in company currency of the row. |
| `ReducedAmountInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the currency for the rows reduced amount in company currency. |
| `IsReset` | `Boolean` | no |  |  | Specifies if the row is reset. |
| `CodingEntryId` | `Int64?` | yes | [CodingEntries](../Accounting/CodingEntry.md) |  | The business key identifier of the coding entry for the row. |
| `PartialInvoiceType` | `Int32` | no |  | enum | The partial invoice type of the row. |
| `PartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the rows part. |
| `OverrideDescription` | `String` | no |  | max length 400 | The override description of the row. |
| `FractionOfTotal` | `Decimal` | no |  |  | The fraction of the total amount for the row. |
| `PaymentTermId` | `Int64?` | yes | [PaymentTerms](../Common/PaymentTerm.md) |  | The business key identifier of the payment term for the row. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the row. |

## Enumerations

### PartialInvoiceType

| Name | Value |
| --- | ---: |
| `NotInitialized` | 0 |
| `InAdvance` | 1 |
| `Delivery` | 2 |
| `InArrears` | 3 |
| `Text` | 4 |


## Example

```json
{
  "Id": 0,
  "CustomerOrderId": 0,
  "InvoicingPeriod": null,
  "VatRateId": null,
  "Amount": 0.0,
  "AmountCurrencyId": null,
  "AmountInCompanyCurrency": 0.0,
  "AmountInCompanyCurrencyCurrencyId": null,
  "ReducedAmountInCompanyCurrency": null,
  "ReducedAmountInCompanyCurrencyCurrencyId": null,
  "IsReset": false,
  "CodingEntryId": null,
  "PartialInvoiceType": 0,
  "PartId": null,
  "OverrideDescription": null,
  "FractionOfTotal": 0.0,
  "PaymentTermId": null,
  "RowIndex": null
}
```
