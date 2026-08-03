---
type: API Entity
title: InquiryTypes
description: Represents an inquiry type.
resource: https://api.monitor.se/api/Monitor.API.Purchase.InquiryType.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.InquiryType.html
  title: Monitor API — InquiryType
module: Purchase
api_class: InquiryType
doc_name: InquiryTypes
endpoint: GET /api/v1/Purchase/InquiryTypes
guid: D20073E0-51CA-4310-A4CD-DC5A536B3517
permission: Show order types
introduced_in: '2.31'
property_count: 11
references_out:
- /entities/Common/CurrencyExchangeType.md
referenced_by:
- /entities/Purchase/Inquiry.md
---

# InquiryTypes

Represents an inquiry type.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `InquiryType`
- **Endpoint:** `GET /api/v1/Purchase/InquiryTypes`
- **Required permission:** Show order types
- **GUID:** `D20073E0-51CA-4310-A4CD-DC5A536B3517`
- **Introduced in:** 2.31

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the type. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the type. |
| `Prefix` | `String` | no |  | max length 3 | The prefix to apply on inquiry numbers spawned from this type. |
| `Description` | `String` | no |  | max length 400 | The translated description of the type. |
| `Priority` | `Int32` | no |  |  | The priority of the type. |
| `Visible` | `Boolean` | no |  |  | Specifies if the type is visible. |
| `IsPreset` | `Boolean` | no |  |  | Specifies if the type is a preset type. |
| `BaseType` | `Int32` | no |  | enum | The base type of inquiries created from this type. |
| `CodingGroupId` | `Int64` | no |  |  | The business key identifier of the type's coding group. |
| `RateTypeSetting` | `Int32` | no |  | enum, since 22.9 | The rate type setting of the inquiry type. |
| `CurrencyExchangeTypeId` | `Int64?` | yes | [CurrencyExchangeTypes](../Common/CurrencyExchangeType.md) | since 22.9 | The business key identifier of the inquiry type's currency exchange type. |

## Enumerations

### BaseType

| Name | Value |
| --- | ---: |
| `Inquiry` | 0 |

### RateTypeSetting

| Name | Value |
| --- | ---: |
| `Supplier` | 1 |
| `OrderType` | 2 |


## Referenced by

**Purchase**

- [Inquiries](Inquiry.md) — `OrderType` (expand)
- [Inquiries](Inquiry.md) — `OrderTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Prefix": null,
  "Description": null,
  "Priority": 0,
  "Visible": false,
  "IsPreset": false,
  "BaseType": 0,
  "CodingGroupId": 0,
  "RateTypeSetting": 0,
  "CurrencyExchangeTypeId": null
}
```
