---
type: API Entity
title: DeliveryTerms
description: Represents a queryable delivery term.
resource: https://api.monitor.se/api/Monitor.API.Common.DeliveryTerm.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.DeliveryTerm.html
  title: Monitor API — DeliveryTerm
module: Common
api_class: DeliveryTerm
doc_name: DeliveryTerms
endpoint: GET /api/v1/Common/DeliveryTerms
guid: 67E4E9B6-C688-4175-B55A-2360D1520475
permission: Show terms
introduced_in: '2.18'
property_count: 10
referenced_by:
- /entities/Common/DeliveryAddressWarehouseInformation.md
- /entities/Purchase/Inquiry.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderInvoice.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/Quote.md
- /entities/Sales/SalesAgreement.md
- /entities/Sales/Shipment.md
---

# DeliveryTerms

Represents a queryable delivery term.

- **Module:** [Common](/modules/Common.md)
- **API class:** `DeliveryTerm`
- **Endpoint:** `GET /api/v1/Common/DeliveryTerms`
- **Required permission:** Show terms
- **GUID:** `67E4E9B6-C688-4175-B55A-2360D1520475`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the delivery term. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the delivery term is the default term. |
| `Description` | `String` | no |  |  | The translated description of the delivery term. |
| `Number` | `Int64` | no |  |  | The delivery term number. |
| `Destination` | `String` | no |  | max length 35 | The destination specified by the delivery term. |
| `TermLocation` | `String` | no |  | max length 35 | The location specified by the delivery term. |
| `TermCode` | `String` | no |  | max length 80 | The code specified by the delivery term. |
| `Payer` | `Int32` | no |  | enum | Specifies how payment is handled for the delivery term. |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |
| `ShipmentDefaultCode` | `String` | no |  | max length 5, since 24.8 | The shipment default code specified by the delivery term. |

## Enumerations

### Payer

| Name | Value |
| --- | ---: |
| `BuyerPays` | 1 |
| `SellerPays` | 2 |
| `OtherPayer` | 3 |
| `Incoterms` | 4 |


## Referenced by

**Common**

- [DeliveryAddressWarehouseInformations](/entities/Common/DeliveryAddressWarehouseInformation.md) — `DeliveryTermId` (FK)

**Purchase**

- [Inquiries](/entities/Purchase/Inquiry.md) — `DeliveryTermId` (FK)
- [PurchaseOrderInvoices](/entities/Purchase/PurchaseOrderInvoice.md) — `DeliveryTermId` (FK)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `DeliveryTerm` (expand)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `DeliveryTermId` (FK)

**Sales**

- [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) — `DeliveryTermId` (FK)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `DeliveryTermId` (FK)
- [Quotes](/entities/Sales/Quote.md) — `DeliveryTermId` (FK)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `DeliveryTermId` (FK)
- [Shipments](/entities/Sales/Shipment.md) — `DeliveryTermId` (FK)


## Example

```json
{
  "Id": 0,
  "IsDefault": false,
  "Description": null,
  "Number": 0,
  "Destination": null,
  "TermLocation": null,
  "TermCode": null,
  "Payer": 0,
  "CompanyIds": null,
  "ShipmentDefaultCode": null
}
```
