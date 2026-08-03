---
type: API Entity
title: ShippingServices
description: Represents a shipping service.
resource: https://api.monitor.se/api/Monitor.API.Sales.ShippingService.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.ShippingService.html
  title: Monitor API — ShippingService
module: Sales
api_class: ShippingService
doc_name: ShippingServices
endpoint: GET /api/v1/Sales/ShippingServices
guid: 1C1F01DA-AE37-4721-AFA6-1F8F827A7E12
permission: Show shipment
introduced_in: '23.1'
property_count: 14
references_out:
- /entities/Purchase/Supplier.md
- /entities/Sales/ShippingTemplate.md
referenced_by:
- /entities/Sales/Shipment.md
---

# ShippingServices

Represents a shipping service.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `ShippingService`
- **Endpoint:** `GET /api/v1/Sales/ShippingServices`
- **Required permission:** Show shipment
- **GUID:** `1C1F01DA-AE37-4721-AFA6-1F8F827A7E12`
- **Introduced in:** 23.1

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the shipping service. |
| `Name` | `String` | no |  | max length 30 | The name of the shipping service. |
| `Code` | `String` | no |  | max length 35 | The human readable identifier of the shipping service. |
| `LogTradePrintQueue` | `String` | no |  | max length 25 | The Logtrade print queue of the shipping service. |
| `SchenkerOpalNumber` | `String` | no |  | max length 50 | The Schenker opal number of the shipping service. |
| `ConsolidatedShipment` | `Boolean` | no |  |  | Indicates if the shipping service is a consolidated shipment. |
| `StoredShipment` | `Boolean` | no |  |  | Indicates if the shipping service is a stored shipment. |
| `UseSellerAddress` | `Boolean` | no |  |  | Indicates if the shipping service use seller address. |
| `UsePurchaserAddress` | `Boolean` | no |  |  | Indicates if the shipping service use purchaser address. |
| `UseFrieghtPayerAddress` | `Boolean` | no |  |  | Indicates if the shipping service use frieght payer address. |
| `ShippingTemplateId` | `Int64?` | yes | [ShippingTemplates](ShippingTemplate.md) |  | The business key identifier of the shipping template of the shipping service. |
| `SenderQuickId` | `String` | no |  | max length 30 | The sender quick id of the shipping service. |
| `SupplierId` | `Int64?` | yes | [Suppliers](../Purchase/Supplier.md) |  | The business key identifier of the supplier of the shipping service. |
| `SellerQuickId` | `String` | no |  | max length 30 | The seller quick id of the shipping service. |

## Referenced by

**Sales**

- [Shipments](Shipment.md) — `ShippingService` (expand)
- [Shipments](Shipment.md) — `ShippingServiceId` (FK)


## Example

```json
{
  "Id": 0,
  "Name": null,
  "Code": null,
  "LogTradePrintQueue": null,
  "SchenkerOpalNumber": null,
  "ConsolidatedShipment": false,
  "StoredShipment": false,
  "UseSellerAddress": false,
  "UsePurchaserAddress": false,
  "UseFrieghtPayerAddress": false,
  "ShippingTemplateId": null,
  "SenderQuickId": null,
  "SupplierId": null,
  "SellerQuickId": null
}
```
