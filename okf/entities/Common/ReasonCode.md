---
type: API Entity
title: ReasonCodes
description: Represents a reason code.
resource: https://api.monitor.se/api/Monitor.API.Common.ReasonCode.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ReasonCode.html
  title: Monitor API — ReasonCode
module: Common
api_class: ReasonCode
doc_name: ReasonCodes
endpoint: GET /api/v1/Common/ReasonCodes
guid: 9C8F0C45-6C0E-47B0-8323-DAD0523DC224
permission: Show cause codes
introduced_in: '2.18'
property_count: 6
referenced_by:
- /entities/Purchase/PurchaseOrderRow.md
---

# ReasonCodes

Represents a reason code.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ReasonCode`
- **Endpoint:** `GET /api/v1/Common/ReasonCodes`
- **Required permission:** Show cause codes
- **GUID:** `9C8F0C45-6C0E-47B0-8323-DAD0523DC224`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the reason code. |
| `Type` | `Int32` | no |  | bitmask, enum | The usage type of the reason code. |
| `Code` | `String` | no |  | unique, max length 6 | The alphanumeric code of the reason code. |
| `Description` | `String` | no |  |  | The translated description of the reason code. |
| `CommentMandatory` | `Boolean` | no |  |  | Specifies if a comment is mandatory for the reason code. |
| `Active` | `Boolean` | no |  |  | Specifies if the reason code is active in the system. |

## Enumerations

### Type (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `All` | 0 |
| `PurchaseOrder` | 1 |
| `ManufacturingOrder` | 2 |


## Referenced by

**Purchase**

- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `DelayReason` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `DelayReasonId` (FK)


## Example

```json
{
  "Id": 0,
  "Type": 0,
  "Code": null,
  "Description": null,
  "CommentMandatory": false,
  "Active": false
}
```
