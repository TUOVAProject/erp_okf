---
type: API Entity
title: Countries
description: Represents a queryable country.
resource: https://api.monitor.se/api/Monitor.API.Common.Country.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Country.html
  title: Monitor API — Country
module: Common
api_class: Country
doc_name: Countries
endpoint: GET /api/v1/Common/Countries
guid: 2815F623-7A7B-4546-B4ED-947A17E02D85
permission: Show countries
introduced_in: '2.18'
property_count: 17
references_out:
- /entities/Common/Currency.md
- /entities/Common/LanguageCode.md
- /entities/Common/VatGroup.md
- /entities/Sales/CustomerAccountGroup.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Common/Address.md
- /entities/Common/BusinessContactBankAccount.md
- /entities/Common/DeliveryAddress.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartTemplate.md
- /entities/Sales/CountryDocumentSettings.md
- /entities/Sales/CustomerCountryDocumentSettings.md
- /entities/Sales/ShipmentCustomsRow.md
---

# Countries

Represents a queryable country.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `Country`
- **Endpoint:** `GET /api/v1/Common/Countries`
- **Required permission:** Show countries
- **GUID:** `2815F623-7A7B-4546-B4ED-947A17E02D85`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the country. |
| `Code` | `String` | no |  | max length 3 | The human readable code of the country. |
| `Description` | `String` | no |  |  | The translated description of the country. |
| `IsEuMember` | `Boolean` | no |  |  | Specifies if the country is a member of the European Union. |
| `LanguageId` | `Int64` | no | [LanguageCodes](LanguageCode.md) |  | References LanguageCodes . |
| `CurrencyId` | `Int64?` | yes | [Currencies](Currency.md) |  | References Currencies . |
| `AddressFormatType` | `Int32` | no |  |  | The format type of the address. |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](../Sales/CustomerAccountGroup.md) |  | References CustomerAccountGroups . |
| `IsActive` | `Boolean` | no |  |  | Specifies if the country is active and available in MONITOR or not. |
| `SupplierAccountGroupId` | `Int64?` | yes |  |  | References SupplierAccountGroup. |
| `VatGroupId` | `Int64?` | yes | [VatGroups](VatGroup.md) | **deprecated since 2.39** | References VatGroups . _(Replaced by CustomerVatGroupId/SupplierVatGroupId)_ |
| `SupplierVatGroupId` | `Int64?` | yes | [VatGroups](VatGroup.md) |  | References VatGroups . |
| `CustomerVatGroupId` | `Int64?` | yes | [VatGroups](VatGroup.md) |  | References VatGroups . |
| `VatRegistrationNumberPrefixException` | `String` | no |  | max length 3 | The VAT registration number prefix exception of the country. |
| `CountryRegion` | `Int32` | no |  | default: 0, since 2.47 | Region code in integer format according to ISO-3166 |
| `CountrySubRegion` | `Int32` | no |  | default: 0, since 2.47 | Sub region code in integer format according to ISO-3166 |
| `CountryIntermediateRegion` | `Int32` | no |  | default: 0, since 2.47 | Intermediate region code in integer format according to ISO-3166 |

## Referenced by

**Accounting**

- [AccountsPayables](../Accounting/AccountsPayable.md) — `CountryId` (FK)

**Common**

- [Addresses](Address.md) — `CountryId` (FK)
- [BusinessContactBankAccounts](BusinessContactBankAccount.md) — `Country` (expand)
- [BusinessContactBankAccounts](BusinessContactBankAccount.md) — `CountryId` (FK)
- [DeliveryAddresses](DeliveryAddress.md) — `CountryId` (FK)
- [Warehouses](Warehouse.md) — `CountryId` (FK)

**Inventory**

- [PartTemplates](../Inventory/PartTemplate.md) — `CountryOfOriginId` (FK)
- [Parts](../Inventory/Part.md) — `CountryOfOrigin` (expand)
- [Parts](../Inventory/Part.md) — `CountryOfOriginId` (FK)

**Sales**

- [CountryDocumentSettings](../Sales/CountryDocumentSettings.md) — `CountryId` (FK)
- [CustomerCountryDocumentSettings](../Sales/CustomerCountryDocumentSettings.md) — `CountryId` (FK)
- [ShipmentCustomsRows](../Sales/ShipmentCustomsRow.md) — `CountryOfOrigin` (expand)
- [ShipmentCustomsRows](../Sales/ShipmentCustomsRow.md) — `CountryOfOriginId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "IsEuMember": false,
  "LanguageId": 0,
  "CurrencyId": null,
  "AddressFormatType": 0,
  "CustomerAccountGroupId": null,
  "IsActive": false,
  "SupplierAccountGroupId": null,
  "VatGroupId": null,
  "SupplierVatGroupId": null,
  "CustomerVatGroupId": null,
  "VatRegistrationNumberPrefixException": null,
  "CountryRegion": 0,
  "CountrySubRegion": 0,
  "CountryIntermediateRegion": 0
}
```
