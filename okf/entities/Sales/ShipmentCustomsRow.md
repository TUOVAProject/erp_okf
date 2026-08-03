---
type: API Entity
title: ShipmentCustomsRows
description: Represents a shipments customs information row.
resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentCustomsRow.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentCustomsRow.html
  title: Monitor API — ShipmentCustomsRow
module: Sales
api_class: ShipmentCustomsRow
doc_name: ShipmentCustomsRows
endpoint: GET /api/v1/Sales/ShipmentCustomsRows
guid: B32F90BF-08A8-4376-BC30-7BE139646611
permission: Show shipment
introduced_in: '26.4'
property_count: 22
references_out:
- /entities/Common/Country.md
- /entities/Common/StatisticalGoodsCode.md
- /entities/Common/Unit.md
- /entities/Sales/ShipmentCustoms.md
referenced_by:
- /entities/Sales/ShipmentCustoms.md
---

# ShipmentCustomsRows

Represents a shipments customs information row.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `ShipmentCustomsRow`
- **Endpoint:** `GET /api/v1/Sales/ShipmentCustomsRows`
- **Required permission:** Show shipment
- **GUID:** `B32F90BF-08A8-4376-BC30-7BE139646611`
- **Introduced in:** 26.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the shipments customs information row. |
| `ParentId` | `Int64` | no | [ShipmentCustoms](ShipmentCustoms.md) |  | The business key identifier of the rows customs information. |
| `RowIndex` | `Int32?` | yes |  |  | The rows index number. |
| `CountryOfOriginId` | `Int64?` | yes | [Countries](../Common/Country.md) |  | The business key identifier of the rows country of origin. |
| `CountryOfOrigin` | `Countries` | no | [Countries](../Common/Country.md) | expandable | The rows country of origin. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](../Common/StatisticalGoodsCode.md) |  | The business key identifier of the rows statistical goods code. |
| `StatisticalGoodsCode` | `StatisticalGoodsCodes` | no | [StatisticalGoodsCodes](../Common/StatisticalGoodsCode.md) | expandable | The rows statistical goods code. |
| `UnitId` | `Int64?` | yes | [Units](../Common/Unit.md) |  | The business key identifier of the rows unit. |
| `Unit` | `Units` | no | [Units](../Common/Unit.md) | expandable | The rows unit. |
| `AdditionalCode` | `String` | no |  | max length 50 | The rows additional code. |
| `Amount` | `Decimal` | no |  |  | The rows amount. |
| `AmountInCompanyCurrency` | `Decimal` | no |  |  | The rows amount in company currency. |
| `Content` | `String` | no |  | max length 80 | The rows content. |
| `GrossWeight` | `Decimal?` | yes |  |  | The rows gross weight. |
| `NetWeight` | `Decimal?` | yes |  |  | The rows net weight. |
| `GoodsLabel` | `String` | no |  | max length 50 | The rows goods label. |
| `OtherQuantity` | `Decimal?` | yes |  |  | The rows other quantity. |
| `OtherUnitId` | `Int64?` | yes | [Units](../Common/Unit.md) |  | The business key identifier of the rows other unit. |
| `OtherUnit` | `Units` | no | [Units](../Common/Unit.md) | expandable | The rows other unit. |
| `OtherUnitCode` | `String` | no |  | max length 10 | The rows other unit code. |
| `Procedure` | `String` | no |  | max length 80 | The rows procedure. |
| `Quantity` | `Int32` | no |  |  | The rows quantity. |

## Referenced by

**Sales**

- [ShipmentCustoms](ShipmentCustoms.md) — `Rows` (expand)


## Example

```json
{
  "Id": 0,
  "ParentId": 0,
  "RowIndex": null,
  "CountryOfOriginId": null,
  "CountryOfOrigin": null,
  "StatisticalGoodsCodeId": null,
  "StatisticalGoodsCode": null,
  "UnitId": null,
  "Unit": null,
  "AdditionalCode": null,
  "Amount": 0.0,
  "AmountInCompanyCurrency": 0.0,
  "Content": null,
  "GrossWeight": null,
  "NetWeight": null,
  "GoodsLabel": null,
  "OtherQuantity": null,
  "OtherUnitId": null,
  "OtherUnit": null,
  "OtherUnitCode": null,
  "Procedure": null,
  "Quantity": 0
}
```
