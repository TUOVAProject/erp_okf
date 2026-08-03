---
type: API Entity
title: AutoAllocations
description: Represent an auto allocation.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AutoAllocation.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AutoAllocation.html
  title: Monitor API — AutoAllocation
module: Accounting
api_class: AutoAllocation
doc_name: AutoAllocations
endpoint: GET /api/v1/Accounting/AutoAllocations
guid: 9CAA54CB-128C-42EC-B455-DD92B35AC76E
permission: Show automatic allocations
introduced_in: '24.8'
property_count: 9
references_out:
- /entities/Accounting/AllocationKey.md
---

# AutoAllocations

Represent an auto allocation.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `AutoAllocation`
- **Endpoint:** `GET /api/v1/Accounting/AutoAllocations`
- **Required permission:** Show automatic allocations
- **GUID:** `9CAA54CB-128C-42EC-B455-DD92B35AC76E`
- **Introduced in:** 24.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the auto allocation. |
| `Number` | `String` | no |  | unique, max length 35 | The human readable identifier of the auto allocation. |
| `Description` | `String` | no |  | max length 35 | The description of the auto allocation. |
| `Type` | `Int32` | no |  | enum | The type of the auto allocation |
| `Active` | `Boolean` | no |  |  | Specifies whether the auto allocation is active or not. |
| `AllocationKeyId` | `Int64?` | yes | [AllocationKeys](AllocationKey.md) | expandable | The business key identifier of the allocation key linked to the auto allocation. |
| `AllocationKey` | `AllocationKeys` | no | [AllocationKeys](AllocationKey.md) |  | The allocation key linked to the auto allocation. |
| `AccountFrom` | `String` | no |  | max length 10 | The account number from which the auto allocation applies. |
| `AccountTo` | `String` | no |  | max length 10 | The account number to which the auto allocation applies. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Direct` | 0 |
| `PeriodBalance` | 1 |
| `AccumulatedBalance` | 2 |


## Example

```json
{
  "Id": 0,
  "Number": null,
  "Description": null,
  "Type": 0,
  "Active": false,
  "AllocationKeyId": null,
  "AllocationKey": null,
  "AccountFrom": null,
  "AccountTo": null
}
```
