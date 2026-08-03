---
type: API Entity
title: Codings
description: Represents a coding.
resource: https://api.monitor.se/api/Monitor.API.Accounting.Coding.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.Coding.html
  title: Monitor API — Coding
module: Accounting
api_class: Coding
doc_name: Codings
endpoint: GET /api/v1/Accounting/Codings
guid: BD4591A5-1FDC-46E3-89E5-6521DAE74C9B
introduced_in: '2.30'
property_count: 2
references_out:
- /entities/Accounting/CodingRow.md
referenced_by:
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/PurchaseOrderInvoiceRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/SalesAgreementRow.md
---

# Codings

Represents a coding.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `Coding`
- **Endpoint:** `GET /api/v1/Accounting/Codings`
- **GUID:** `BD4591A5-1FDC-46E3-89E5-6521DAE74C9B`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the coding. |
| `CodingRows` | `CodingRows[]` | no | [CodingRows](CodingRow.md) | expandable, collection | The coding rows belonging to the coding. |

## Referenced by

**Purchase**

- [InquiryRows](../Purchase/InquiryRow.md) — `Coding` (expand)
- [InquiryRows](../Purchase/InquiryRow.md) — `CodingId` (FK)
- [PurchaseOrderInvoiceRows](../Purchase/PurchaseOrderInvoiceRow.md) — `Coding` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `Coding` (expand)

**Sales**

- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `Coding` (expand)
- [QuoteRows](../Sales/QuoteRow.md) — `Coding` (expand)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `Coding` (expand)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `CodingId` (FK)


## Example

```json
{
  "Id": 0,
  "CodingRows": null
}
```
