---
type: API Entity
title: CommunicationAddresses
description: Represents a queryable communication address. A communication address
  is used to store either phone, cellphone, email or fax information in MONITOR.
resource: https://api.monitor.se/api/Monitor.API.Common.CommunicationAddress.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.CommunicationAddress.html
  title: Monitor API — CommunicationAddress
module: Common
api_class: CommunicationAddress
doc_name: CommunicationAddresses
endpoint: GET /api/v1/Common/CommunicationAddresses
guid: 65BC336B-BD64-46B5-947C-894031B8CE33
introduced_in: '2.18'
property_count: 6
referenced_by:
- /entities/Purchase/Inquiry.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/Supplier.md
- /entities/Sales/BusinessOpportunityReference.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/Quote.md
---

# CommunicationAddresses

Represents a queryable communication address. A communication address is used to store either phone, cellphone, email or fax information in MONITOR.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `CommunicationAddress`
- **Endpoint:** `GET /api/v1/Common/CommunicationAddresses`
- **GUID:** `65BC336B-BD64-46B5-947C-894031B8CE33`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the communication address. |
| `Type` | `Int32` | no |  | enum | The type of information stored within this particular communication address instance. |
| `CommunicationAddressValue` | `String` | no |  | max length 80 | The value of the communication address. |
| `Remarks` | `String` | no |  | max length 80 | Any remarks regarding the communication address. |
| `RecipientOf` | `Int32` | no |  | bitmask, enum | Specifies what types of communication the address should be recipient of. |
| `ContactName` | `String` | no |  | max length 80, since 2.45.1 | The contact name of the communication address. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Phone` | 0 |
| `Fax` | 1 |
| `Email` | 2 |
| `CellPhone` | 3 |

### RecipientOf (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Invoice` | 1 |
| `Reminder` | 2 |
| `OrderConfirmation` | 4 |
| `DispatchAdvice` | 8 |
| `ShippingAgentAdvice` | 16 |
| `OrderConfirmationReminder` | 32 |
| `DeliveryReminder` | 64 |
| `DeliverySchedule` | 128 |
| `PurchaseOrder` | 256 |
| `Quote` | 512 |
| `ShippingAgentSmsAdvice` | 1024 |
| `SubcontractDeliveryNote` | 2048 |
| `Inquiry` | 4096 |
| `CaseClaimReport` | 8192 |
| `CaseConfirmation` | 16384 |
| `CaseResponse` | 32768 |
| `NonconformityReport` | 65536 |
| `Proforma` | 131072 |
| `ProjectReportExternal` | 262144 |
| `ProjectReportInternal` | 524288 |
| `CustomerDeliveryNote` | 1048576 |
| `TraceabilityProtocol` | 2097152 |
| `BlanketOrderPurchase` | 4194304 |
| `BlanketOrderSales` | 8388608 |
| `PurchaseDeliverySchedule` | 16777216 |
| `SalesAgreement` | 33554432 |
| `AccountStatement` | 67108864 |
| `EInvoiceInvitation` | 134217728 |
| `ReturnOrder` | 268435456 |
| `SubcontractProformaInvoice` | 536870912 |
| `SupplierAgreement` | 1073741824 |


## Referenced by

**Purchase**

- [Inquiries](../Purchase/Inquiry.md) — `CommunicationAddresses` (expand)
- [PurchaseOrders](../Purchase/PurchaseOrder.md) — `CommunicationAddresses` (expand)
- [Suppliers](../Purchase/Supplier.md) — `CommunicationAddresses` (expand)

**Sales**

- [BusinessOpportunityReferences](../Sales/BusinessOpportunityReference.md) — `CommunicationAddresses` (expand)
- [CustomerOrders](../Sales/CustomerOrder.md) — `CommunicationAddresses` (expand)
- [Customers](../Sales/Customer.md) — `CommunicationAddresses` (expand)
- [Quotes](../Sales/Quote.md) — `CommunicationAddresses` (expand)


## Example

```json
{
  "Id": 0,
  "Type": 0,
  "CommunicationAddressValue": null,
  "Remarks": null,
  "RecipientOf": 0,
  "ContactName": null
}
```
