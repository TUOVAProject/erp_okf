---
type: API Entity
title: SalesPickingLists
description: Represents a sales picking list.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesPickingList.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesPickingList.html
  title: Monitor API — SalesPickingList
module: Sales
api_class: SalesPickingList
doc_name: SalesPickingLists
endpoint: GET /api/v1/Sales/SalesPickingLists
guid: 388FA65F-A574-4AEA-B11B-68D824FC8F35
permission: Show customer orders
introduced_in: '2.53'
property_count: 10
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/Person.md
- /entities/Common/Warehouse.md
- /entities/Sales/CustomerOrderInvoice.md
referenced_by:
- /entities/Sales/GetWithdrawalInformation.md
- /entities/Sales/PackageRow.md
- /entities/Sales/RemoveSalesPickingList.md
- /entities/Sales/ShipmentInformationSource.md
- /entities/Sales/WithdrawalInformationRow.md
---

# SalesPickingLists

Represents a sales picking list.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `SalesPickingList`
- **Endpoint:** `GET /api/v1/Sales/SalesPickingLists`
- **Required permission:** Show customer orders
- **GUID:** `388FA65F-A574-4AEA-B11B-68D824FC8F35`
- **Introduced in:** 2.53

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the picking list. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the picking list. |
| `PrintedByApplicationUserId` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the application user that printed the picking list. |
| `PrintedByPersonId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the person that printed the picking list. |
| `PrintedTimestamp` | `DateTimeOffset?` | yes |  |  | The date the picking list was printed. |
| `State` | `Int32` | no |  | enum | The state for the picking list. |
| `Status` | `Int32` | no |  | enum | The state for the picking list. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse for the picking list. |
| `CustomerOrderInvoices` | `CustomerOrderInvoices[]` | no | [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) | expandable, collection | The customer order invoices of the picking list. |
| `LifeCycleState` | `Int32` | no |  | enum | The life cycle state of the picking list. |

## Enumerations

### State

| Name | Value |
| --- | ---: |
| `Registered` | 0 |
| `ReadyForInvoicing` | 1 |

### Status

| Name | Value |
| --- | ---: |
| `ReadyForDelivery` | 1 |
| `ReadyForDeliveryCreditLimitExceeded` | 2 |
| `ReadyForDeliveryUnpaidAdvance` | 3 |
| `Pending` | 4 |
| `Shortage` | 5 |
| `UnConfirmed` | 6 |
| `Preliminary` | 7 |
| `PreliminaryCreditLimitExceeded` | 8 |
| `PreliminaryUnpaidAdvance` | 9 |

### LifeCycleState

| Name | Value |
| --- | ---: |
| `Transient` | 1 |
| `Persistent` | 10 |
| `History` | 20 |
| `RemovableCandidate` | 99 |


## Referenced by

**Sales**

- [GetWithdrawalInformation](/entities/Sales/GetWithdrawalInformation.md) — `PickingListId` (FK)
- [PackageRows](/entities/Sales/PackageRow.md) — `ParentId` (FK)
- [RemoveSalesPickingList](/entities/Sales/RemoveSalesPickingList.md) — `PickingListId` (FK)
- [ShipmentInformationSources](/entities/Sales/ShipmentInformationSource.md) — `PickingListId` (FK)
- [WithdrawalInformationRow](/entities/Sales/WithdrawalInformationRow.md) — `PickingListId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "PrintedByApplicationUserId": null,
  "PrintedByPersonId": null,
  "PrintedTimestamp": null,
  "State": 0,
  "Status": 0,
  "WarehouseId": 0,
  "CustomerOrderInvoices": null,
  "LifeCycleState": 0
}
```
