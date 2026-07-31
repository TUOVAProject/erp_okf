---
type: API Entity
title: AccountsPayableCashDiscountLevels
description: Represents a cash discount level for an accounts payable.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountsPayableCashDiscountLevel.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountsPayableCashDiscountLevel.html
  title: Monitor API — AccountsPayableCashDiscountLevel
module: Accounting
api_class: AccountsPayableCashDiscountLevel
doc_name: AccountsPayableCashDiscountLevels
endpoint: GET /api/v1/Accounting/AccountsPayableCashDiscountLevels
guid: 402ef94a-1bfb-416e-89e5-8e5613c5ec02
permission: Show accounts payable
introduced_in: '22.5'
property_count: 5
references_out:
- /entities/Accounting/AccountsPayable.md
---

# AccountsPayableCashDiscountLevels

Represents a cash discount level for an accounts payable.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `AccountsPayableCashDiscountLevel`
- **Endpoint:** `GET /api/v1/Accounting/AccountsPayableCashDiscountLevels`
- **Required permission:** Show accounts payable
- **GUID:** `402ef94a-1bfb-416e-89e5-8e5613c5ec02`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the cash discount level. |
| `ParentId` | `Int64` | no | [AccountsPayables](/entities/Accounting/AccountsPayable.md) |  | The business key identifier of the accounts payable the cash discount level belongs to. |
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
