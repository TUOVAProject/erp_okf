---
type: API Entity
title: ShipmentPackageInformationPackageNumbers
description: Represents a shipping agents real package number for a shipment package
  information.
resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentPackageInformationPackageNumber.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentPackageInformationPackageNumber.html
  title: Monitor API — ShipmentPackageInformationPackageNumber
module: Sales
api_class: ShipmentPackageInformationPackageNumber
doc_name: ShipmentPackageInformationPackageNumbers
endpoint: GET /api/v1/Sales/ShipmentPackageInformationPackageNumbers
guid: AD62F590-1E29-45AD-8AAC-297F71F8DEC7
permission: Show shipment
introduced_in: '24.3'
property_count: 3
references_out:
- /entities/Sales/ShipmentPackageInformation.md
referenced_by:
- /entities/Sales/ShipmentPackageInformation.md
---

# ShipmentPackageInformationPackageNumbers

Represents a shipping agents real package number for a shipment package information.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `ShipmentPackageInformationPackageNumber`
- **Endpoint:** `GET /api/v1/Sales/ShipmentPackageInformationPackageNumbers`
- **Required permission:** Show shipment
- **GUID:** `AD62F590-1E29-45AD-8AAC-297F71F8DEC7`
- **Introduced in:** 24.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the shipment package information package number. |
| `ParentId` | `Int64` | no | [ShipmentPackageInformations](ShipmentPackageInformation.md) | mandatory (Parent must always be set) | The business key identifier of the ShipmentPackageInformation it belongs to. |
| `ShippingAgentsPackageNumber` | `String` | no |  | max length 80 | The Real PackageNumber from shipper or edited manually of the package information. |

## Referenced by

**Sales**

- [ShipmentPackageInformations](ShipmentPackageInformation.md) — `ShippingAgentsPackageNumbers` (expand)


## Example

```json
{
  "Id": 0,
  "ParentId": 0,
  "ShippingAgentsPackageNumber": null
}
```
