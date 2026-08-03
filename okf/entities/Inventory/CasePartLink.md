---
type: API Entity
title: CaseEntryPartLinks
description: Represents a case part link.
resource: https://api.monitor.se/api/Monitor.API.Inventory.CasePartLink.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.CasePartLink.html
  title: Monitor API — CasePartLink
module: Inventory
api_class: CasePartLink
doc_name: CaseEntryPartLinks
endpoint: GET /api/v1/Inventory/CaseEntryPartLinks
guid: dd65ce0e-908f-47e0-94e0-2e958819fecd
permission: Show case
introduced_in: '24.5'
property_count: 14
references_out:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/AccountsReceivable.md
- /entities/Common/RejectionCodeItem.md
- /entities/Common/Revision.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/Part.md
- /entities/Inventory/ProductRecord.md
- /entities/Purchase/PurchaseOrder.md
- /entities/Sales/CustomerOrder.md
referenced_by:
- /entities/Inventory/CaseEntry.md
---

# CaseEntryPartLinks

Represents a case part link.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `CasePartLink`
- **Endpoint:** `GET /api/v1/Inventory/CaseEntryPartLinks`
- **Required permission:** Show case
- **GUID:** `dd65ce0e-908f-47e0-94e0-2e958819fecd`
- **Introduced in:** 24.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the case part link. |
| `CaseId` | `Int64` | no | [CaseEntry](CaseEntry.md) |  | The business key identifier of the case entry this case part link belongs to. |
| `PartId` | `Int64` | no | [Parts](Part.md) |  | The business key identifier of the referenced part. |
| `ProductRecordId` | `Int64?` | yes | [ProductRecords](ProductRecord.md) |  | The business key identifier of the referenced product record. |
| `IsDefault` | `Boolean` | no |  |  | Defines if the part is considered default part on this case. Can only be set on one part in a case. |
| `PartRevisionId` | `Int64?` | yes | [Revisions](../Common/Revision.md) |  | The business key identifier of the revision on part. |
| `RejectionCodeItemId` | `Int64` | no | [RejectionCodeItems](../Common/RejectionCodeItem.md) |  | The business key identifier of the rejection code for this case part link. |
| `RejectedQuantity` | `Decimal` | no |  |  | Quantity rejected for this case part link. |
| `RejectionDescription` | `String` | no |  | max length 400 | The rejection description for this case part link. |
| `ProductRecordBatchId` | `Int64?` | yes | [ProductRecords](ProductRecord.md) |  | The business key identifier of the referenced product record batch. |
| `CompensationCustomerOrderId` | `Int64?` | yes | [CustomerOrders](../Sales/CustomerOrder.md) |  | The business key identifier of compensation customer order for this part case link. |
| `CompensationAccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](../Accounting/AccountsReceivable.md) |  | The business key identifier of compensation accounts receivable for this part case link. |
| `CompensationPurchaseOrderId` | `Int64?` | yes | [PurchaseOrders](../Purchase/PurchaseOrder.md) |  | The business key identifier of compensation purchase order for this part case link. |
| `CompensationAccountsPayableId` | `Int64?` | yes | [AccountsPayables](../Accounting/AccountsPayable.md) |  | The business key identifier of compensation accounts payable for this part case link. |

## Referenced by

**Inventory**

- [CaseEntry](CaseEntry.md) — `CasePartLinks` (expand)


## Example

```json
{
  "Id": 0,
  "CaseId": 0,
  "PartId": 0,
  "ProductRecordId": null,
  "IsDefault": false,
  "PartRevisionId": null,
  "RejectionCodeItemId": 0,
  "RejectedQuantity": 0.0,
  "RejectionDescription": null,
  "ProductRecordBatchId": null,
  "CompensationCustomerOrderId": null,
  "CompensationAccountsReceivableId": null,
  "CompensationPurchaseOrderId": null,
  "CompensationAccountsPayableId": null
}
```
