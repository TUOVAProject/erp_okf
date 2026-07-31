---
type: API Entity
title: MaterialRowReferenceNumbers
description: Represents a reference number attached to a material row.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ReferenceNumber.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ReferenceNumber.html
  title: Monitor API — ReferenceNumber
module: Manufacturing
api_class: ReferenceNumber
doc_name: MaterialRowReferenceNumbers
endpoint: GET /api/v1/Manufacturing/MaterialRowReferenceNumbers
guid: CE74CF58-BE7E-4311-9701-48DFD5AEB73D
permission: Show part
introduced_in: '26.6'
property_count: 9
references_out:
- /entities/Manufacturing/MaterialRow.md
referenced_by:
- /entities/Manufacturing/MaterialRow.md
---

# MaterialRowReferenceNumbers

Represents a reference number attached to a material row.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `ReferenceNumber`
- **Endpoint:** `GET /api/v1/Manufacturing/MaterialRowReferenceNumbers`
- **Required permission:** Show part
- **GUID:** `CE74CF58-BE7E-4311-9701-48DFD5AEB73D`
- **Introduced in:** 26.6

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the reference number. |
| `MaterialRowId` | `Int64` | no | [MaterialRows](/entities/Manufacturing/MaterialRow.md) |  | The business key identifier of the material row that the reference number belongs to. |
| `Prefix` | `String` | no |  | max length 4 | The prefix part of the reference number. |
| `From` | `String` | no |  | max length 15 | The starting value of the reference number range. |
| `To` | `String` | no |  | max length 15 | The ending value of the reference number range. Only valid when is numeric; otherwise this value is not persisted and the quantity is one. |
| `Suffix` | `String` | no |  | max length 1 | The suffix part of the reference number. |
| `Remark` | `String` | no |  | max length 40 | A free-text remark associated with the reference number. |
| `Quantity` | `Decimal` | no |  |  | The quantity represented by the reference number range. This value is calculated from and and cannot be set directly. |
| `RowIndex` | `Int32?` | yes |  |  | The display order of the reference number within the material row. |

## Referenced by

**Manufacturing**

- [MaterialRows](/entities/Manufacturing/MaterialRow.md) — `ReferenceNumbers` (expand)


## Example

```json
{
  "Id": 0,
  "MaterialRowId": 0,
  "Prefix": null,
  "From": null,
  "To": null,
  "Suffix": null,
  "Remark": null,
  "Quantity": 0.0,
  "RowIndex": null
}
```
