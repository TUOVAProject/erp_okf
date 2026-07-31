---
type: API Entity
title: SupplierAccountGroups
description: Represents a supplier account group.
resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierAccountGroup.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierAccountGroup.html
  title: Monitor API — SupplierAccountGroup
module: Purchase
api_class: SupplierAccountGroup
doc_name: SupplierAccountGroups
endpoint: GET /api/v1/Purchase/SupplierAccountGroups
guid: AA52F99D-01A4-47FE-9601-DCD759E455DC
permission: Show chart of accounts
introduced_in: '2.27'
property_count: 5
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Purchase/PurchaseOrderInvoice.md
- /entities/Purchase/Supplier.md
---

# SupplierAccountGroups

Represents a supplier account group.

- **Module:** [Purchase](/modules/Purchase.md)
- **API class:** `SupplierAccountGroup`
- **Endpoint:** `GET /api/v1/Purchase/SupplierAccountGroups`
- **Required permission:** Show chart of accounts
- **GUID:** `AA52F99D-01A4-47FE-9601-DCD759E455DC`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the group. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the group is the default group. |
| `Number` | `Int64` | no |  |  | The human readable identifier of the group. |
| `Description` | `String` | no |  |  | The translated description of the group. |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |

## Referenced by

**Accounting**

- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `SupplierAccountGroupId` (FK)

**Purchase**

- [PurchaseOrderInvoices](/entities/Purchase/PurchaseOrderInvoice.md) — `AccountGroupId` (FK)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `AccountGroup` (expand)
- [PurchaseOrders](/entities/Purchase/PurchaseOrder.md) — `AccountGroupId` (FK)
- [Suppliers](/entities/Purchase/Supplier.md) — `SupplierAccountGroupId` (FK)


## Example

```json
{
  "Id": 0,
  "IsDefault": false,
  "Number": 0,
  "Description": null,
  "CompanyIds": null
}
```
