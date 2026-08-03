---
type: API Entity
title: SupplierAccounts
description: Represents a supplier account.
resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierAccount.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.SupplierAccount.html
  title: Monitor API — SupplierAccount
module: Purchase
api_class: SupplierAccount
doc_name: SupplierAccounts
endpoint: GET /api/v1/Purchase/SupplierAccounts
guid: 4D41456F-A07A-4293-97E3-71D838A781BB
permission: Show supplier
introduced_in: '22.7'
property_count: 5
references_out:
- /entities/Accounting/CodingEntry.md
- /entities/Accounting/StandardAccount.md
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Purchase/Supplier.md
---

# SupplierAccounts

Represents a supplier account.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `SupplierAccount`
- **Endpoint:** `GET /api/v1/Purchase/SupplierAccounts`
- **Required permission:** Show supplier
- **GUID:** `4D41456F-A07A-4293-97E3-71D838A781BB`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the supplier account. |
| `SupplierId` | `Int64?` | yes | [Suppliers](Supplier.md) |  | The business key identifier of the accounts supplier. |
| `StandardAccountId` | `Int64?` | yes | [StandardAccounts](../Accounting/StandardAccount.md) |  | The business key identifier of the standard account for the account. |
| `StandardAccount` | `StandardAccounts` | no | [StandardAccounts](../Accounting/StandardAccount.md) | expandable | The standard account for the account. |
| `CodingEntryId` | `Int64?` | yes | [CodingEntries](../Accounting/CodingEntry.md) |  | The business key identifier of the coding entry for the account. |

## Referenced by

**Purchase**

- [Suppliers](Supplier.md) — `SupplierAccounts` (expand)


## Example

```json
{
  "Id": 0,
  "SupplierId": null,
  "StandardAccountId": null,
  "StandardAccount": null,
  "CodingEntryId": null
}
```
