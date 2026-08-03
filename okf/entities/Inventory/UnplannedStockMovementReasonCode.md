---
type: API Entity
title: UnplannedStockMovementReasonCodes
description: Represents a queryable unplanned stock movement reason code.
resource: https://api.monitor.se/api/Monitor.API.Inventory.UnplannedStockMovementReasonCode.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.UnplannedStockMovementReasonCode.html
  title: Monitor API — UnplannedStockMovementReasonCode
module: Inventory
api_class: UnplannedStockMovementReasonCode
doc_name: UnplannedStockMovementReasonCodes
endpoint: GET /api/v1/Inventory/UnplannedStockMovementReasonCodes
guid: 67D231B2-C23E-455A-970B-2D00E9DE1CB5
permission: Show cause codes
introduced_in: '2.18'
property_count: 5
---

# UnplannedStockMovementReasonCodes

Represents a queryable unplanned stock movement reason code.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `UnplannedStockMovementReasonCode`
- **Endpoint:** `GET /api/v1/Inventory/UnplannedStockMovementReasonCodes`
- **Required permission:** Show cause codes
- **GUID:** `67D231B2-C23E-455A-970B-2D00E9DE1CB5`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the unplanned stock movement reason code. |
| `Code` | `String` | no |  |  | The alphanumeric code of the reason code. |
| `Description` | `String` | no |  |  | The translated description of the reason code. |
| `CommentMandatory` | `Boolean` | no |  |  | Specifies if a comment is mandatory for the reason code. |
| `Active` | `Boolean` | no |  |  | Specifies if the reason code is active in the system. |

## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "CommentMandatory": false,
  "Active": false
}
```
