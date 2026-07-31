---
type: API Entity
title: ManufacturingPickingListMaterials
description: Represents a manufacturing picking list material.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingPickingListMaterial.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ManufacturingPickingListMaterial.html
  title: Monitor API — ManufacturingPickingListMaterial
module: Manufacturing
api_class: ManufacturingPickingListMaterial
doc_name: ManufacturingPickingListMaterials
endpoint: GET /api/v1/Manufacturing/ManufacturingPickingListMaterials
guid: 7CF7F984-02CB-4B72-B0DA-04DC58F31173
permission: Show manufacturing orders
introduced_in: '2.48'
property_count: 5
references_out:
- /entities/Inventory/QuantityChange.md
- /entities/Manufacturing/ManufacturingOrderMaterial.md
referenced_by:
- /entities/Manufacturing/ManufacturingPickingList.md
---

# ManufacturingPickingListMaterials

Represents a manufacturing picking list material.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `ManufacturingPickingListMaterial`
- **Endpoint:** `GET /api/v1/Manufacturing/ManufacturingPickingListMaterials`
- **Required permission:** Show manufacturing orders
- **GUID:** `7CF7F984-02CB-4B72-B0DA-04DC58F31173`
- **Introduced in:** 2.48

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the manufacturing picking list material. |
| `MaterialId` | `Int64` | no | [ManufacturingOrderMaterials](/entities/Manufacturing/ManufacturingOrderMaterial.md) |  | The business key identifier of the manufacturing order material. |
| `Material` | `ManufacturingOrderMaterials` | no | [ManufacturingOrderMaterials](/entities/Manufacturing/ManufacturingOrderMaterial.md) | expandable, since 24.9 | The manufacturing order material in the manufacturing picking list. |
| `QuantityChangeId` | `Int64` | no | [QuantityChanges](/entities/Inventory/QuantityChange.md) |  | The business key identifier of the manufacturing picking list materials quantity change. |
| `QuantityChange` | `QuantityChanges` | no | [QuantityChanges](/entities/Inventory/QuantityChange.md) | expandable | The suggested quantity for withdrawal when creating the picking list. |

## Referenced by

**Manufacturing**

- [ManufacturingPickingLists](/entities/Manufacturing/ManufacturingPickingList.md) — `Materials` (expand)


## Example

```json
{
  "Id": 0,
  "MaterialId": 0,
  "Material": null,
  "QuantityChangeId": 0,
  "QuantityChange": null
}
```
