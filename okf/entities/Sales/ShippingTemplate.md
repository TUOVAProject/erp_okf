---
type: API Entity
title: ShippingTemplates
description: Represents a shipping service.
resource: https://api.monitor.se/api/Monitor.API.Sales.ShippingTemplate.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.ShippingTemplate.html
  title: Monitor API — ShippingTemplate
module: Sales
api_class: ShippingTemplate
doc_name: ShippingTemplates
endpoint: GET /api/v1/Sales/ShippingTemplates
guid: 41B5651B-9391-426B-A17C-E52E02DB1EA0
permission: Show shipment
introduced_in: '23.1'
property_count: 8
references_out:
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Sales/Shipment.md
- /entities/Sales/ShippingService.md
---

# ShippingTemplates

Represents a shipping service.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `ShippingTemplate`
- **Endpoint:** `GET /api/v1/Sales/ShippingTemplates`
- **Required permission:** Show shipment
- **GUID:** `41B5651B-9391-426B-A17C-E52E02DB1EA0`
- **Introduced in:** 23.1

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the shipping template. |
| `ShippingTemplateName` | `String` | no |  | max length 30 | The name of the shipping template. |
| `ShippingTemplateCode` | `String` | no |  | max length 35 | The human readable identifier of the shipping template. |
| `ExportPickupAddress` | `Boolean` | no |  |  | Indicates if the shipping template export pickup address. |
| `ExportDeliveryAddress` | `Boolean` | no |  |  | Indicates if the shipping template export delivery address. |
| `ConsignorId` | `String` | no |  | max length 30 | The consignor id of the shipping template. |
| `PickupId` | `String` | no |  | max length 30 | The pickup id of the shipping template. |
| `SupplierId` | `Int64?` | yes | [Suppliers](../Purchase/Supplier.md) |  | The business key identifier of the shipping templates supplier. |

## Referenced by

**Sales**

- [Shipments](Shipment.md) — `ShippingTemplateId` (FK)
- [ShippingServices](ShippingService.md) — `ShippingTemplateId` (FK)


## Example

```json
{
  "Id": 0,
  "ShippingTemplateName": null,
  "ShippingTemplateCode": null,
  "ExportPickupAddress": false,
  "ExportDeliveryAddress": false,
  "ConsignorId": null,
  "PickupId": null,
  "SupplierId": null
}
```
