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

- **Module:** [Common](/modules/Common.md)
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
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the revision comment. References Comments . |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The revision comment. |
| `PartId` | `Int64` | no | [Part](/entities/Inventory/Part.md) |  | The business key identifier of the part that the revision belongs to. References . |

## Referenced by

**Inventory**

- [CaseEntry](/entities/Inventory/CaseEntry.md) — `PartRevision` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `PartRevisionId` (FK)
- [CaseEntryPartLinks](/entities/Inventory/CasePartLink.md) — `PartRevisionId` (FK)
- [PartLocations](/entities/Inventory/PartLocation.md) — `Revision` (expand)
- [PartLocations](/entities/Inventory/PartLocation.md) — `RevisionId` (FK)
- [Parts](/entities/Inventory/Part.md) — `ActiveRevision` (expand)
- [Parts](/entities/Inventory/Part.md) — `ActiveRevisionId` (FK)
- [Parts](/entities/Inventory/Part.md) — `Revisions` (expand)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `CustomerOrderPartRevisionId` (FK)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `PartRevisionId` (FK)

**Manufacturing**

- [ManufacturingOrderNodes](/entities/Manufacturing/ManufacturingOrderNode.md) — `Revision` (expand)
- [ManufacturingOrderNodes](/entities/Manufacturing/ManufacturingOrderNode.md) — `RevisionId` (FK)

**Purchase**

- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `Revision` (expand)
- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `RevisionId` (FK)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `Revision` (expand)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `RevisionId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `Revision` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `RevisionId` (FK)

**Sales**

- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `Revision` (expand)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `RevisionId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `Revision` (expand)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `RevisionId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `Revision` (expand)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `RevisionId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `Revision` (expand)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `RevisionId` (FK)


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
