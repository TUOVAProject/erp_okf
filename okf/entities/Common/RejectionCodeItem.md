---
type: API Entity
title: RejectionCodeItems
description: Represents a rejection code.
resource: https://api.monitor.se/api/Monitor.API.Common.RejectionCodeItem.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.RejectionCodeItem.html
  title: Monitor API — RejectionCodeItem
module: Common
api_class: RejectionCodeItem
doc_name: RejectionCodeItems
endpoint: GET /api/v1/Common/RejectionCodeItems
guid: 19257A1A-F323-4672-B0E5-8F5D2F814F88
permission: Show rejection codes/cause codes
introduced_in: '2.18'
property_count: 6
referenced_by:
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CasePartLink.md
---

# RejectionCodeItems

Represents a rejection code.

- **Module:** [Common](/modules/Common.md)
- **API class:** `RejectionCodeItem`
- **Endpoint:** `GET /api/v1/Common/RejectionCodeItems`
- **Required permission:** Show rejection codes/cause codes
- **GUID:** `19257A1A-F323-4672-B0E5-8F5D2F814F88`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the rejection code. |
| `Code` | `String` | no |  | unique, max length 6 | The string identifier of the rejection code. |
| `Description` | `String` | no |  |  | The translated description of the rejection code. |
| `Active` | `Boolean` | no |  | since 2.22 | Specifies if the rejection code item is active. |
| `ForcedComment` | `Boolean` | no |  | since 2.22 | Specifies if the rejection code item requires a comment. |
| `Type` | `Int32` | no |  | bitmask, enum, since 2.22 | The rejection code item type. |

## Enumerations

### Type (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `ManufacturingReporting` | 1 |
| `ReceivingInspectionPurchase` | 2 |
| `CustomerNonConformity` | 4 |
| `SupplierNonConformity` | 8 |
| `InternalNonConformity` | 16 |
| `Standard8DNonConformity` | 32 |


## Referenced by

**Inventory**

- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ActualRejectionCode` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ActualRejectionCodeId` (FK)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ReasonRejectionCodeId` (FK)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `RejectionCodeItem` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `RejectionCodeItemId` (FK)
- [CaseEntryPartLinks](/entities/Inventory/CasePartLink.md) — `RejectionCodeItemId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "Active": false,
  "ForcedComment": false,
  "Type": 0
}
```
