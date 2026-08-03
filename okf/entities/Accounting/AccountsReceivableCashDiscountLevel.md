---
type: API Entity
title: AccountsReceivableCashDiscountLevels
description: Represents a cash discount level for an accounts receivable.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountsReceivableCashDiscountLevel.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountsReceivableCashDiscountLevel.html
  title: Monitor API — AccountsReceivableCashDiscountLevel
module: Accounting
api_class: AccountsReceivableCashDiscountLevel
doc_name: AccountsReceivableCashDiscountLevels
endpoint: GET /api/v1/Accounting/AccountsReceivableCashDiscountLevels
guid: 12EA47B2-0FAC-451F-BC95-A59F252094CA
permission: Show accounts receivable
introduced_in: '22.5'
property_count: 5
references_out:
- /entities/Accounting/AccountsReceivable.md
---

# AccountsReceivableCashDiscountLevels

Represents a cash discount level for an accounts receivable.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `AccountsReceivableCashDiscountLevel`
- **Endpoint:** `GET /api/v1/Accounting/AccountsReceivableCashDiscountLevels`
- **Required permission:** Show accounts receivable
- **GUID:** `12EA47B2-0FAC-451F-BC95-A59F252094CA`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the cash discount level. |
| `ParentId` | `Int64` | no | [AccountsReceivables](AccountsReceivable.md) |  | The business key identifier of the accounts receivable the cash discount level belongs to. |
| `Discount` | `Decimal?` | yes |  |  | The discount in percent for the cash discount level. |
| `DiscountDate` | `DateTimeOffset?` | yes |  |  | The date to which the discount applies. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the cash discount level. |

## Example

```json
{
  "Id": 0,
  "ParentId": 0,
  "Discount": null,
  "DiscountDate": null,
  "RowIndex": null
}
```
