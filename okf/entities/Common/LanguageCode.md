---
type: API Entity
title: LanguageCodes
description: Represents a language code. Language codes are the language definitions
  in MONITOR.
resource: https://api.monitor.se/api/Monitor.API.Common.LanguageCode.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.LanguageCode.html
  title: Monitor API — LanguageCode
module: Common
api_class: LanguageCode
doc_name: LanguageCodes
endpoint: GET /api/v1/Common/LanguageCodes
guid: 08A89350-7A92-4B22-8B8F-7F17FCAAF867
permission: Show languages
introduced_in: '2.18'
property_count: 3
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Common/Address.md
- /entities/Common/ApplicationUser.md
- /entities/Common/Company.md
- /entities/Common/Country.md
- /entities/Common/DeliveryAddress.md
- /entities/Common/MonitoringTaskRecipient.md
- /entities/Common/Person.md
- /entities/Common/Warehouse.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
---

# LanguageCodes

Represents a language code. Language codes are the language definitions in MONITOR.

- **Module:** [Common](/modules/Common.md)
- **API class:** `LanguageCode`
- **Endpoint:** `GET /api/v1/Common/LanguageCodes`
- **Required permission:** Show languages
- **GUID:** `08A89350-7A92-4B22-8B8F-7F17FCAAF867`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the language code. |
| `Code` | `String` | no |  | unique, max length 3 | The human readable code of the language. |
| `Phrase` | `String` | no |  |  | The translated description of the language code. |

## Referenced by

**Accounting**

- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `Language` (expand)
- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `LanguageId` (FK)

**Common**

- [Addresses](/entities/Common/Address.md) — `LanguageId` (FK)
- [ApplicationUsers](/entities/Common/ApplicationUser.md) — `LanguageId` (FK)
- [Companies](/entities/Common/Company.md) — `Language` (expand)
- [Companies](/entities/Common/Company.md) — `LanguageId` (FK)
- [Countries](/entities/Common/Country.md) — `LanguageId` (FK)
- [DeliveryAddresses](/entities/Common/DeliveryAddress.md) — `LanguageId` (FK)
- [MonitoringTaskRecipients](/entities/Common/MonitoringTaskRecipient.md) — `LanguageCodeId` (FK)
- [Persons](/entities/Common/Person.md) — `LanguageId` (FK)
- [Warehouses](/entities/Common/Warehouse.md) — `LanguageId` (FK)

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `Language` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `LanguageId` (FK)

**Sales**

- [Customers](/entities/Sales/Customer.md) — `Language` (expand)
- [Customers](/entities/Sales/Customer.md) — `LanguageId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Phrase": null
}
```
