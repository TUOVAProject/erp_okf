---
type: API Entity
title: SalesAgreementBases
description: Represents a sales agreement basis.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreementBasis.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreementBasis.html
  title: Monitor API — SalesAgreementBasis
module: Sales
api_class: SalesAgreementBasis
doc_name: SalesAgreementBases
endpoint: GET /api/v1/Sales/SalesAgreementBases
guid: 61d4a4e1-492b-4caf-a3d3-8afec951c340
permission: Show agreement
introduced_in: '26.4'
property_count: 19
references_out:
- /entities/Accounting/Account.md
- /entities/Common/Currency.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/SalesAgreementBasisRow.md
referenced_by:
- /entities/Sales/SalesAgreement.md
- /entities/Sales/SalesAgreementBasisRow.md
---

# SalesAgreementBases

Represents a sales agreement basis.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `SalesAgreementBasis`
- **Endpoint:** `GET /api/v1/Sales/SalesAgreementBases`
- **Required permission:** Show agreement
- **GUID:** `61d4a4e1-492b-4caf-a3d3-8afec951c340`
- **Introduced in:** 26.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the agreement basis. |
| `SalesAgreementId` | `Int64` | no | [SalesAgreements](/entities/Sales/SalesAgreement.md) |  | The business key identifier of the parent agreement. |
| `CustomerOrderId` | `Int64` | no | [CustomerOrders](/entities/Sales/CustomerOrder.md) |  | The business key identifier of the customer order generated from this agreement basis. |
| `InvoiceId` | `Int64?` | yes | [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) |  | The business key identifier of the invoice for this agreement basis. |
| `AccrualAccountId` | `Int64?` | yes | [Accounts](/entities/Accounting/Account.md) |  | The business key identifier of the accrual account for this agreement basis. |
| `IsAccrual` | `Boolean` | no |  |  | Indicates if this agreement basis uses accrual accounting. |
| `IsOneTimeCost` | `Boolean` | no |  |  | Indicates if this agreement basis is a one-time cost. |
| `IsRemoved` | `Boolean` | no |  |  | Indicates if the agreement basis and the linked customer order has been set as removed. |
| `IsPaused` | `Boolean` | no |  |  | Indicates if the agreement basis is paused. |
| `InvoicingMethod` | `Int32` | no |  | enum | The invoicing method of the agreement basis. |
| `PeriodStart` | `DateTimeOffset` | no |  |  | The period start date of the agreement basis. |
| `PeriodEnd` | `DateTimeOffset` | no |  |  | The period end date of the agreement basis. |
| `PlannedInvoiceDate` | `DateTimeOffset` | no |  |  | The planned invoice date of the agreement basis. |
| `PeriodStartOnAgreementWhenCreated` | `DateTimeOffset?` | yes |  |  | The period start on the agreement when this basis was created. |
| `ExchangeRate` | `Decimal` | no |  |  | The exchange rate of the agreement basis. |
| `CurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency of the agreement basis. |
| `Currency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The currency of the agreement basis. |
| `UseForwardRate` | `Boolean` | no |  |  | Indicates if the agreement basis uses forward rate. |
| `Rows` | `SalesAgreementBasisRows[]` | no | [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) | expandable, collection | The rows of the agreement basis. |

## Enumerations

### InvoicingMethod

| Name | Value |
| --- | ---: |
| `InAdvance` | 1 |
| `InArrears` | 2 |


## Referenced by

**Sales**

- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `ParentAgreementBasisId` (FK)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `Bases` (expand)


## Example

```json
{
  "Id": 0,
  "SalesAgreementId": 0,
  "CustomerOrderId": 0,
  "InvoiceId": null,
  "AccrualAccountId": null,
  "IsAccrual": false,
  "IsOneTimeCost": false,
  "IsRemoved": false,
  "IsPaused": false,
  "InvoicingMethod": 0,
  "PeriodStart": "0001-01-01T00:00:00+00:00",
  "PeriodEnd": "0001-01-01T00:00:00+00:00",
  "PlannedInvoiceDate": "0001-01-01T00:00:00+00:00",
  "PeriodStartOnAgreementWhenCreated": null,
  "ExchangeRate": 0.0,
  "CurrencyId": 0,
  "Currency": null,
  "UseForwardRate": false,
  "Rows": null
}
```
