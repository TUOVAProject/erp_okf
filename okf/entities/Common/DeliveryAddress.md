---
type: API Entity
title: DeliveryAddresses
description: Represents a delivery address.
resource: https://api.monitor.se/api/Monitor.API.Common.DeliveryAddress.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.DeliveryAddress.html
  title: Monitor API — DeliveryAddress
module: Common
api_class: DeliveryAddress
doc_name: DeliveryAddresses
endpoint: GET /api/v1/Common/DeliveryAddresses
guid: CE99DAB8-D95F-4DD5-9747-AEA02084F5B7
introduced_in: '2.18'
property_count: 28
references_out:
- /entities/Common/Address.md
- /entities/Common/BusinessContactReference.md
- /entities/Common/Country.md
- /entities/Common/DeliveryAddressWarehouseInformation.md
- /entities/Common/LanguageCode.md
- /entities/Common/VatGroup.md
- /entities/Common/VatRate.md
- /entities/Sales/CustomerAccountGroup.md
referenced_by:
- /entities/Common/DeliveryAddressWarehouseInformation.md
- /entities/Common/Warehouse.md
- /entities/Inventory/ProductRecord.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
- /entities/Sales/Shipment.md
---

# DeliveryAddresses

Represents a delivery address.

- **Module:** [Common](/modules/Common.md)
- **API class:** `DeliveryAddress`
- **Endpoint:** `GET /api/v1/Common/DeliveryAddresses`
- **GUID:** `CE99DAB8-D95F-4DD5-9747-AEA02084F5B7`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the address. |
| `Addressee` | `String` | no |  | max length 100 | The addressee of the address. |
| `Field1` | `String` | no |  | max length 50 | The first field of the address. |
| `Field2` | `String` | no |  | max length 50 | The second field of the address. |
| `Field3` | `String` | no |  | max length 50 | The third field of the address. |
| `Field4` | `String` | no |  | max length 50 | The fourth field of the address. |
| `Field5` | `String` | no |  | max length 50 | The fifth field of the address. |
| `Locality` | `String` | no |  | max length 50 | The locality of the address. |
| `Region` | `String` | no |  | max length 50 | The region of the address. |
| `PostalCode` | `String` | no |  | max length 10 | The postal code of the address. |
| `AddressFormatType` | `Int32` | no |  |  | The format type of the address. |
| `CountryId` | `Int64` | no | [Countries](/entities/Common/Country.md) |  | References Countries . |
| `LanguageId` | `Int64` | no | [LanguageCodes](/entities/Common/LanguageCode.md) |  | The business key identifier of the language code. References LanguageCodes . |
| `FormReportTranslationGroupId` | `Int64` | no |  |  | The business key identifier of the form report translation group. References FormReportTranslationGroup. |
| `PostalCodeId` | `Int64?` | yes |  | **deprecated since 2.44** | The business key identifier of the postal code. References PostalCode. _(Unavailable)_ |
| `IsDefault` | `Boolean` | no |  |  | Specifies if this is the default delivery address. |
| `AddressId` | `Int64` | no | [Addresses](/entities/Common/Address.md) |  | References Addresses . |
| `ConsigneeReferenceId` | `Int64?` | yes | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) |  | References BusinessContactReferences . |
| `ConsigneeReferenceName` | `String` | no |  | max length 80 | The consignee reference name of the delivery address. |
| `Destination` | `String` | no |  | max length 35 | The destination of the delivery address. |
| `DeliveryWeekdays` | `Int32` | no |  | bitmask, enum, **deprecated since 2.18** | Specifies which days delivery can be made to the delivery address. _(Can be found under Warehouses)_ |
| `DeliveryInstruction` | `String` | no |  | max length 80 | The instruction of delivery for the delivery address. |
| `VatRateId` | `Int64?` | yes | [VatRates](/entities/Common/VatRate.md) |  | The business key identifier of the VatRate of the delivery address. References VatRates . |
| `CustomerAccountGroupId` | `Int64?` | yes | [CustomerAccountGroups](/entities/Sales/CustomerAccountGroup.md) |  | The business key identifier of the customer account group of the delivery address. References CustomerAccountGroups . |
| `SupplierAccountGroupId` | `Int64?` | yes |  |  | The business key identifier of the supplier account group of the delivery address. References SupplierAccountGroup. |
| `VatGroupId` | `Int64?` | yes | [VatGroups](/entities/Common/VatGroup.md) |  | The business key identifier of the VAT group that the delivery address belongs to. References VatGroups . |
| `VatNumber` | `String` | no |  | max length 30, since 24.9 | Vat registration number to be set on delivery address |
| `Warehouses` | `DeliveryAddressWarehouseInformations[]` | no | [DeliveryAddressWarehouseInformations](/entities/Common/DeliveryAddressWarehouseInformation.md) | expandable, collection, since 2.43 | The warehouse information that belongs to the delivery address. |

## Enumerations

### DeliveryWeekdays (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Monday` | 1 |
| `Tuesday` | 2 |
| `Wednesday` | 4 |
| `Thursday` | 8 |
| `Friday` | 16 |
| `Saturday` | 32 |
| `Sunday` | 64 |


## Referenced by

**Common**

- [DeliveryAddressWarehouseInformations](/entities/Common/DeliveryAddressWarehouseInformation.md) — `ParentId` (FK)
- [Warehouses](/entities/Common/Warehouse.md) — `DeliveryAddresses` (expand)

**Inventory**

- [ProductRecords](/entities/Inventory/ProductRecord.md) — `DeliveryAddressId` (FK)

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `DeliveryAddress` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `DeliveryAddressId` (FK)
- [Suppliers](/entities/Purchase/Supplier.md) — `DeliveryAddresses` (expand)

**Sales**

- [Customers](/entities/Sales/Customer.md) — `ActiveDeliveryAddress` (expand)
- [Customers](/entities/Sales/Customer.md) — `ActiveDeliveryAddressId` (FK)
- [Customers](/entities/Sales/Customer.md) — `DeliveryAddresses` (expand)
- [Shipments](/entities/Sales/Shipment.md) — `ActiveDeliveryAddressDeliveryAddress` (expand)
- [Shipments](/entities/Sales/Shipment.md) — `ActiveDeliveryAddressDeliveryAddressId` (FK)
- [Shipments](/entities/Sales/Shipment.md) — `ActiveFallbackDeliveryAddressDeliveryAddress` (expand)
- [Shipments](/entities/Sales/Shipment.md) — `ActiveFallbackDeliveryAddressDeliveryAddressId` (FK)


## Example

```json
{
  "Id": 0,
  "Addressee": null,
  "Field1": null,
  "Field2": null,
  "Field3": null,
  "Field4": null,
  "Field5": null,
  "Locality": null,
  "Region": null,
  "PostalCode": null,
  "AddressFormatType": 0,
  "CountryId": 0,
  "LanguageId": 0,
  "FormReportTranslationGroupId": 0,
  "PostalCodeId": null,
  "IsDefault": false,
  "AddressId": 0,
  "ConsigneeReferenceId": null,
  "ConsigneeReferenceName": null,
  "Destination": null,
  "DeliveryWeekdays": 0,
  "DeliveryInstruction": null,
  "VatRateId": null,
  "CustomerAccountGroupId": null,
  "SupplierAccountGroupId": null,
  "VatGroupId": null,
  "VatNumber": null,
  "Warehouses": null
}
```
