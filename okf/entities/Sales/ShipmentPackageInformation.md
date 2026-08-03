---
type: API Entity
title: ShipmentPackageInformations
description: Represents a shipment package information.
resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentPackageInformation.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentPackageInformation.html
  title: Monitor API — ShipmentPackageInformation
module: Sales
api_class: ShipmentPackageInformation
doc_name: ShipmentPackageInformations
endpoint: GET /api/v1/Sales/ShipmentPackageInformations
guid: DDF592AF-F818-4EA7-BD4E-69F660E14F7A
permission: Show shipment
introduced_in: '23.1'
property_count: 20
references_out:
- /entities/Inventory/GoodsType.md
- /entities/Inventory/PackageType.md
- /entities/Sales/Shipment.md
- /entities/Sales/ShipmentInformationSource.md
- /entities/Sales/ShipmentPackageInformationPackageNumber.md
referenced_by:
- /entities/Sales/ShipmentPackageInformationPackageNumber.md
---

# ShipmentPackageInformations

Represents a shipment package information.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `ShipmentPackageInformation`
- **Endpoint:** `GET /api/v1/Sales/ShipmentPackageInformations`
- **Required permission:** Show shipment
- **GUID:** `DDF592AF-F818-4EA7-BD4E-69F660E14F7A`
- **Introduced in:** 23.1

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the shipment package information. |
| `InformationSourceId` | `Int64?` | yes | [ShipmentInformationSources](ShipmentInformationSource.md) |  | The business key identifier of the information source of the package information. |
| `Count` | `Int32` | no |  |  | The number of packages of the package information. |
| `PackageTypeName` | `String` | no |  | max length 80 | The package type name of the package information. |
| `PackageType` | `Int64?` | yes | [PackageTypes](../Inventory/PackageType.md) |  | The business key identifier of the package type of the package information. |
| `GoodsTypeName` | `String` | no |  | max length 80 | The goods type name of the package information. |
| `GoodsType` | `Int64?` | yes | [GoodsTypes](../Inventory/GoodsType.md) |  | The business key identifier of the goods type of the package information. |
| `PackageIdentification` | `String` | no |  | max length 20 | The package identification of the package information. |
| `PackageTypeCode` | `String` | no |  | max length 16 | The package type code of the package information. |
| `Volume` | `Decimal` | no |  |  | The volume of the package information. |
| `GrossWeight` | `Decimal` | no |  |  | The gross weight of the package information. |
| `LoadingMeters` | `Decimal` | no |  |  | The loading meters of the package information. |
| `Length` | `Decimal` | no |  |  | The length of the package information. |
| `Width` | `Decimal` | no |  |  | The width of the package information. |
| `Height` | `Decimal` | no |  |  | The height of the package information. |
| `GoodsLabel` | `String` | no |  | max length 50 | The GoodsLabel of the package information. |
| `PackageNumber` | `String` | no |  | max length 80, since 24.3 | The PackageNumber to identify a package with a Shipping Partner of the package information. |
| `ShippingAgentsPackageNumbers` | `ShipmentPackageInformationPackageNumbers[]` | no | [ShipmentPackageInformationPackageNumbers](ShipmentPackageInformationPackageNumber.md) | expandable, collection, since 24.3 | The Real PackageNumbers from shipping agent or edited manually of the package information. |
| `ShipmentId` | `Int64?` | yes | [Shipments](Shipment.md) |  | The business key identifier of the shipment of the package information. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the package information. |

## Referenced by

**Sales**

- [ShipmentPackageInformationPackageNumbers](ShipmentPackageInformationPackageNumber.md) — `ParentId` (FK)


## Example

```json
{
  "Id": 0,
  "InformationSourceId": null,
  "Count": 0,
  "PackageTypeName": null,
  "PackageType": null,
  "GoodsTypeName": null,
  "GoodsType": null,
  "PackageIdentification": null,
  "PackageTypeCode": null,
  "Volume": 0.0,
  "GrossWeight": 0.0,
  "LoadingMeters": 0.0,
  "Length": 0.0,
  "Width": 0.0,
  "Height": 0.0,
  "GoodsLabel": null,
  "PackageNumber": null,
  "ShippingAgentsPackageNumbers": null,
  "ShipmentId": null,
  "RowIndex": null
}
```
