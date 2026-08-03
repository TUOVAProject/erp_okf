---
type: API Entity
title: TransactionTypeIntrastats
description: Represents a transaction type intrastat.
resource: https://api.monitor.se/api/Monitor.API.Common.TransactionTypeIntrastat.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.TransactionTypeIntrastat.html
  title: Monitor API — TransactionTypeIntrastat
module: Common
api_class: TransactionTypeIntrastat
doc_name: TransactionTypeIntrastats
endpoint: GET /api/v1/Common/TransactionTypeIntrastats
guid: bfd9907d-c3f6-46bf-ae2e-aac533d3f217
permission: Show transaction types
introduced_in: '2.30'
property_count: 4
referenced_by:
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/CustomerOrderRow.md
---

# TransactionTypeIntrastats

Represents a transaction type intrastat.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `TransactionTypeIntrastat`
- **Endpoint:** `GET /api/v1/Common/TransactionTypeIntrastats`
- **Required permission:** Show transaction types
- **GUID:** `bfd9907d-c3f6-46bf-ae2e-aac533d3f217`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the transaction type. |
| `Number` | `Int64` | no |  | unique | The human readable identifier of the transaction type. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the transaction type is default. |
| `Description` | `String` | no |  |  | The translated description of the currency transaction type. |

## Referenced by

**Purchase**

- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `IntrastatTransactionType` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `IntrastatTransactionTypeId` (FK)

**Sales**

- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `IntrastatTransactionType` (expand)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `IntrastatTransactionTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "IsDefault": false,
  "Description": null
}
```
