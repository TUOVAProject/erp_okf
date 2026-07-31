---
type: API Entity
title: ShipmentCustoms
description: Represents a shipments customs information.
resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentCustoms.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentCustoms.html
  title: Monitor API — ShipmentCustoms
module: Sales
api_class: ShipmentCustoms
doc_name: ShipmentCustoms
endpoint: GET /api/v1/Sales/ShipmentCustoms
guid: 628442CA-0EE8-4507-A749-96FE34D46B99
permission: Show shipment
introduced_in: '26.4'
property_count: 49
references_out:
- /entities/Common/Currency.md
- /entities/Common/CurrencyExchangeType.md
- /entities/Common/DeliveryMethod.md
- /entities/Common/Person.md
- /entities/Sales/Shipment.md
- /entities/Sales/ShipmentCustomsDocument.md
- /entities/Sales/ShipmentCustomsRow.md
referenced_by:
- /entities/Sales/Shipment.md
- /entities/Sales/ShipmentCustomsDocument.md
- /entities/Sales/ShipmentCustomsRow.md
---

# ShipmentCustoms

Represents a shipments customs information.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `ShipmentCustoms`
- **Endpoint:** `GET /api/v1/Sales/ShipmentCustoms`
- **Required permission:** Show shipment
- **GUID:** `628442CA-0EE8-4507-A749-96FE34D46B99`
- **Introduced in:** 26.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the shipments customs information. |
| `ParentId` | `Int64` | no | [Shipments](/entities/Sales/Shipment.md) |  | The business key identifier of the customs informations shipment. |
| `Dutiable` | `Boolean` | no |  |  | Indicates if the shipment is dutiable. |
| `InvoiceNumber` | `String` | no |  | max length 20 | The invoice number on the customs information. |
| `InvoiceDate` | `DateTimeOffset?` | yes |  |  | The invoice date on the customs information. |
| `CurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the customs informations currency. |
| `Currency` | `Currencies` | no | [Currencies](/entities/Common/Currency.md) | expandable | The customs informations currency. |
| `CurrencyExchangeTypeId` | `Int64` | no | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) |  | The business key identifier of the customs informations currency exchange type. |
| `CurrencyExchangeType` | `CurrencyExchangeTypes` | no | [CurrencyExchangeTypes](/entities/Common/CurrencyExchangeType.md) | expandable | The customs informations currency exchange type. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](/entities/Common/DeliveryMethod.md) |  | The business key identifier of the customs informations delivery method. |
| `DeliveryMethod` | `DeliveryMethods` | no | [DeliveryMethods](/entities/Common/DeliveryMethod.md) | expandable | The customs informations delivery method. |
| `ForeignDeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](/entities/Common/DeliveryMethod.md) |  | The business key identifier of the customs informations foreign delivery method. |
| `ForeignDeliveryMethod` | `DeliveryMethods` | no | [DeliveryMethods](/entities/Common/DeliveryMethod.md) | expandable | The customs informations foreign delivery method. |
| `DeclarantId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the customs informations declarant person. |
| `Declarant` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable | The customs informations declarant person. |
| `DeclarantName` | `String` | no |  | max length 71 | The customs informations declarant name. |
| `NumberOfPackages` | `Int32` | no |  |  | The number of packages on the customs information. |
| `Comment1` | `String` | no |  | max length 80 | The comment row 1 on the customs information. |
| `Comment2` | `String` | no |  | max length 80 | The comment row 2 on the customs information. |
| `Comment3` | `String` | no |  | max length 80 | The comment row 3 on the customs information. |
| `Comment4` | `String` | no |  | max length 80 | The comment row 4 on the customs information. |
| `TransactionType` | `String` | no |  | max length 50 | The customs informations transaction type. |
| `PointOfExport` | `String` | no |  | max length 50 | The customs informations point of export. |
| `City` | `String` | no |  | max length 50 | The customs informations city. |
| `Date` | `DateTimeOffset` | no |  |  | The customs informations date. |
| `DeclarantCorporationIdentificationNumber` | `String` | no |  | max length 30 | The customs informations declarant corporation identification number. |
| `ReferenceNumber` | `String` | no |  | max length 80 | The customs informations reference number. |
| `InvoiceType` | `Int32?` | yes |  | enum | The customs informations invoice type. |
| `ImportExportType` | `Int32?` | yes |  | enum | The customs informations import export type. |
| `ImportExportTypeName` | `String` | no |  | max length 80, since 26.5 | Free-text override of the import/export type. When set, it takes precedence over when the shipment is exported to forwarders (for example for forwarder-specific codes like "GIFT" or "sample"). |
| `ReasonForExport` | `String` | no |  | max length 70 | The customs informations reason for export. |
| `StatisticalGoodsCodeType` | `Int32` | no |  | enum | The customs informations statistical goods code type. |
| `EoriSeller` | `String` | no |  | max length 35 | The Economic Operator Registration and Identification number of the customs informations seller. |
| `VatNumberSeller` | `String` | no |  | max length 30 | The VAT number of the customs informations seller. |
| `CorporationIdentificationNumberSeller` | `String` | no |  | max length 30 | The corporation identification number of the customs informations seller. |
| `EoriPickup` | `String` | no |  | max length 35 | The customs informations Economic Operator Registration and Identification pickup number. |
| `EoriPurchaser` | `String` | no |  | max length 35 | The Economic Operator Registration and Identification number of the customs informations purchaser. |
| `VatNumberPurchaser` | `String` | no |  | max length 30 | The VAT number of the customs informations purchaser. |
| `CorporationIdentificationNumberPurchaser` | `String` | no |  | max length 30 | The corporation identification number of the customs informations purchaser. |
| `EoriDelivery` | `String` | no |  | max length 35 | The Economic Operator Registration and Identification number of the customs informations delivery. |
| `VatNumberDelivery` | `String` | no |  | max length 30 | The VAT number of the customs informations delivery. |
| `CorporationIdentificationNumberDelivery` | `String` | no |  | max length 30 | The corporation identification number of the customs informations delivery. |
| `CustomsPayingParty` | `Int32` | no |  | enum | Specifies who pay the cusoms fee. |
| `EoriCustomsPayer` | `String` | no |  | max length 35 | The Economic Operator Registration and Identification number of the customs payer. |
| `CorporationIdentificationNumberCustomsPayer` | `String` | no |  | max length 30 | The corporation identification number of the customs payer. |
| `VatNumberCustomsPayer` | `String` | no |  | max length 30 | The VAT number of the customs payer. |
| `CustomsPayer` | `String` | no |  | max length 50 | The customs informations customs payer. |
| `Rows` | `ShipmentCustomsRows[]` | no | [ShipmentCustomsRows](/entities/Sales/ShipmentCustomsRow.md) | expandable, collection | The rows of the customs information. |
| `Documents` | `ShipmentCustomsDocuments[]` | no | [ShipmentCustomsDocuments](/entities/Sales/ShipmentCustomsDocument.md) | expandable, collection | The documents of the customs information. |

## Enumerations

### InvoiceType

| Name | Value |
| --- | ---: |
| `Proforma` | 1 |
| `Commercial` | 2 |

### ImportExportType

| Name | Value |
| --- | ---: |
| `Permanent` | 1 |
| `Temporary` | 2 |
| `Reexport` | 3 |

### StatisticalGoodsCodeType

| Name | Value |
| --- | ---: |
| `CN` | 0 |
| `HS` | 1 |
| `Taric` | 2 |
| `HTS` | 3 |
| `NCM` | 4 |
| `ECCN` | 5 |
| `SITC` | 6 |

### CustomsPayingParty

| Name | Value |
| --- | ---: |
| `BuyerPays` | 1 |
| `SellerPays` | 2 |
| `OtherPayer` | 3 |
| `Incoterms` | 4 |


## Referenced by

**Sales**

- [ShipmentCustomsDocuments](/entities/Sales/ShipmentCustomsDocument.md) — `ParentId` (FK)
- [ShipmentCustomsRows](/entities/Sales/ShipmentCustomsRow.md) — `ParentId` (FK)
- [Shipments](/entities/Sales/Shipment.md) — `Customs` (expand)


## Example

```json
{
  "Id": 0,
  "ParentId": 0,
  "Dutiable": false,
  "InvoiceNumber": null,
  "InvoiceDate": null,
  "CurrencyId": 0,
  "Currency": null,
  "CurrencyExchangeTypeId": 0,
  "CurrencyExchangeType": null,
  "DeliveryMethodId": null,
  "DeliveryMethod": null,
  "ForeignDeliveryMethodId": null,
  "ForeignDeliveryMethod": null,
  "DeclarantId": null,
  "Declarant": null,
  "DeclarantName": null,
  "NumberOfPackages": 0,
  "Comment1": null,
  "Comment2": null,
  "Comment3": null,
  "Comment4": null,
  "TransactionType": null,
  "PointOfExport": null,
  "City": null,
  "Date": "0001-01-01T00:00:00+00:00",
  "DeclarantCorporationIdentificationNumber": null,
  "ReferenceNumber": null,
  "InvoiceType": null,
  "ImportExportType": null,
  "ImportExportTypeName": null,
  "ReasonForExport": null,
  "StatisticalGoodsCodeType": 0,
  "EoriSeller": null,
  "VatNumberSeller": null,
  "CorporationIdentificationNumberSeller": null,
  "EoriPickup": null,
  "EoriPurchaser": null,
  "VatNumberPurchaser": null,
  "CorporationIdentificationNumberPurchaser": null,
  "EoriDelivery": null,
  "VatNumberDelivery": null,
  "CorporationIdentificationNumberDelivery": null,
  "CustomsPayingParty": 0,
  "EoriCustomsPayer": null,
  "CorporationIdentificationNumberCustomsPayer": null,
  "VatNumberCustomsPayer": null,
  "CustomsPayer": null,
  "Rows": null,
  "Documents": null
}
```
