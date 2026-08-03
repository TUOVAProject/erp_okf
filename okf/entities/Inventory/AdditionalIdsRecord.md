---
type: API Entity
title: AdditionalIDsRecords
description: Represents an addtional ids record.
resource: https://api.monitor.se/api/Monitor.API.Inventory.AdditionalIdsRecord.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.AdditionalIdsRecord.html
  title: Monitor API — AdditionalIdsRecord
module: Inventory
api_class: AdditionalIdsRecord
doc_name: AdditionalIDsRecords
endpoint: GET /api/v1/Inventory/AdditionalIDsRecords
guid: 420593B6-CEB9-4F4B-9820-EBABBFEA5EDF
permission: Show serial number
introduced_in: '25.9'
property_count: 9
references_out:
- /entities/Inventory/ProductRecord.md
---

# AdditionalIDsRecords

Represents an addtional ids record.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `AdditionalIdsRecord`
- **Endpoint:** `GET /api/v1/Inventory/AdditionalIDsRecords`
- **Required permission:** Show serial number
- **GUID:** `420593B6-CEB9-4F4B-9820-EBABBFEA5EDF`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the additional ids. |
| `ProductRecordId` | `Int64` | no | [ProductRecords](ProductRecord.md) |  | The business key identifier of the product record that the addtional ids belong to. |
| `Code` | `String` | no |  |  | Code value of the additional ids. |
| `Code2` | `String` | no |  |  | Code2 value of the additional ids. |
| `Code3` | `String` | no |  |  | Code3 value of the additional ids. |
| `Number` | `Int32?` | yes |  |  | Number value of the additional ids. |
| `Number2` | `Decimal?` | yes |  |  | Number2 value of the additional ids. |
| `Date` | `DateTimeOffset?` | yes |  |  | The date of the additional ids. |
| `Weight` | `Decimal?` | yes |  |  | The weight of the additional ids. |

## Example

```json
{
  "Id": 0,
  "ProductRecordId": 0,
  "Code": null,
  "Code2": null,
  "Code3": null,
  "Number": null,
  "Number2": null,
  "Date": null,
  "Weight": null
}
```
