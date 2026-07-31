---
type: API Entity
title: ShipmentCustomsDocuments
description: Represents a shipments customs information document.
resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentCustomsDocument.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentCustomsDocument.html
  title: Monitor API — ShipmentCustomsDocument
module: Sales
api_class: ShipmentCustomsDocument
doc_name: ShipmentCustomsDocuments
endpoint: GET /api/v1/Sales/ShipmentCustomsDocuments
guid: 0A9774AC-30EC-4AFC-B658-83A8C5FA18F5
permission: Show shipment
introduced_in: '26.4'
property_count: 5
references_out:
- /entities/Sales/ShipmentCustoms.md
referenced_by:
- /entities/Sales/ShipmentCustoms.md
---

# ShipmentCustomsDocuments

Represents a shipments customs information document.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `ShipmentCustomsDocument`
- **Endpoint:** `GET /api/v1/Sales/ShipmentCustomsDocuments`
- **Required permission:** Show shipment
- **GUID:** `0A9774AC-30EC-4AFC-B658-83A8C5FA18F5`
- **Introduced in:** 26.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the shipments customs information document. |
| `ParentId` | `Int64` | no | [ShipmentCustoms](/entities/Sales/ShipmentCustoms.md) |  | The business key identifier of the documents customs information. |
| `Code` | `String` | no |  | max length 35 | The documents code. |
| `Name` | `String` | no |  | max length 50 | The documents name. |
| `RowIndex` | `Int32?` | yes |  |  | The documents row index. |

## Referenced by

**Sales**

- [ShipmentCustoms](/entities/Sales/ShipmentCustoms.md) — `Documents` (expand)


## Example

```json
{
  "Id": 0,
  "ParentId": 0,
  "Code": null,
  "Name": null,
  "RowIndex": null
}
```
