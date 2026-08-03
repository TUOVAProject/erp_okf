---
type: API Entity
title: Revisions
description: Represents a revision.
resource: https://api.monitor.se/api/Monitor.API.Common.Revision.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Revision.html
  title: Monitor API — Revision
module: Common
api_class: Revision
doc_name: Revisions
endpoint: GET /api/v1/Common/Revisions
guid: ACB084C7-B5A6-41B5-B94A-D68B992E9A87
permission: Show part
introduced_in: '2.18'
property_count: 6
references_out:
- /entities/Common/Comment.md
- /entities/Inventory/Part.md
referenced_by:
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CasePartLink.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartLocation.md
- /entities/Inventory/ProductRecord.md
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Purchase/BlanketOrderPurchaseRow.md
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/BlanketOrderSalesRow.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/SalesAgreementRow.md
---

# Revisions

Represents a revision.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `Revision`
- **Endpoint:** `GET /api/v1/Common/Revisions`
- **Required permission:** Show part
- **GUID:** `ACB084C7-B5A6-41B5-B94A-D68B992E9A87`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the revision. |
| `Number` | `String` | no |  | unique (per per Part), max length 25 | The revision number. Max length 25 Nullable No Unique Yes (per Part) |
| `ValidFrom` | `DateTimeOffset?` | yes |  |  | The valid from date of the revision. |
| `CommentId` | `Int64?` | yes | [Comments](Comment.md) |  | The business key identifier of the revision comment. References Comments . |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable | The revision comment. |
| `PartId` | `Int64` | no | [Part](../Inventory/Part.md) |  | The business key identifier of the part that the revision belongs to. References . |

## Referenced by

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `PartRevision` (expand)
- [CaseEntry](../Inventory/CaseEntry.md) — `PartRevisionId` (FK)
- [CaseEntryPartLinks](../Inventory/CasePartLink.md) — `PartRevisionId` (FK)
- [PartLocations](../Inventory/PartLocation.md) — `Revision` (expand)
- [PartLocations](../Inventory/PartLocation.md) — `RevisionId` (FK)
- [Parts](../Inventory/Part.md) — `ActiveRevision` (expand)
- [Parts](../Inventory/Part.md) — `ActiveRevisionId` (FK)
- [Parts](../Inventory/Part.md) — `Revisions` (expand)
- [ProductRecords](../Inventory/ProductRecord.md) — `CustomerOrderPartRevisionId` (FK)
- [ProductRecords](../Inventory/ProductRecord.md) — `PartRevisionId` (FK)

**Manufacturing**

- [ManufacturingOrderNodes](../Manufacturing/ManufacturingOrderNode.md) — `Revision` (expand)
- [ManufacturingOrderNodes](../Manufacturing/ManufacturingOrderNode.md) — `RevisionId` (FK)

**Purchase**

- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `Revision` (expand)
- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `RevisionId` (FK)
- [InquiryRows](../Purchase/InquiryRow.md) — `Revision` (expand)
- [InquiryRows](../Purchase/InquiryRow.md) — `RevisionId` (FK)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `Revision` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `RevisionId` (FK)

**Sales**

- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `Revision` (expand)
- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `RevisionId` (FK)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `Revision` (expand)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `RevisionId` (FK)
- [QuoteRows](../Sales/QuoteRow.md) — `Revision` (expand)
- [QuoteRows](../Sales/QuoteRow.md) — `RevisionId` (FK)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `Revision` (expand)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `RevisionId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": null,
  "ValidFrom": null,
  "CommentId": null,
  "Comment": null,
  "PartId": 0
}
```
