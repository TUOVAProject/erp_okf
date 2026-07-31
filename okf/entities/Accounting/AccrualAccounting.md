---
type: API Entity
title: AccrualAccountings
description: Represents a accrual accounting.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccrualAccounting.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccrualAccounting.html
  title: Monitor API — AccrualAccounting
module: Accounting
api_class: AccrualAccounting
doc_name: AccrualAccountings
endpoint: GET /api/v1/Accounting/AccrualAccountings
guid: 39C3A08C-F566-4259-90FF-6C58EDD97781
permission: Show accrual
introduced_in: '2.27'
property_count: 18
references_out:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/AccrualAccountingRow.md
- /entities/Accounting/BookingRow.md
- /entities/Common/Comment.md
referenced_by:
- /entities/Accounting/BookingRow.md
- /entities/Accounting/VoucherRow.md
---

# AccrualAccountings

Represents a accrual accounting.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `AccrualAccounting`
- **Endpoint:** `GET /api/v1/Accounting/AccrualAccountings`
- **Required permission:** Show accrual
- **GUID:** `39C3A08C-F566-4259-90FF-6C58EDD97781`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the accrual accounting. |
| `Number` | `String` | no |  | max length 20 | The human readable number on the accrual accounting. |
| `Text` | `String` | no |  | max length 100 | The human readable text on the accrual accounting. |
| `Type` | `Int32` | no |  | enum | Type of accrual accounting. |
| `StartDate` | `DateTimeOffset?` | yes |  |  | Start date of the accrual accounting. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](/entities/Accounting/AccountsPayable.md) |  | The business key identifier of the accounts payable. |
| `AccountsPayableBookingRowId` | `Int64?` | yes |  |  | The business key identifier of the accounts payable booking row. |
| `VoucherId` | `Int64?` | yes |  |  | The business key identifier of the voucher. |
| `VoucherRowId` | `Int64?` | yes |  |  | The business key identifier of the voucher row. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the accrual accounting comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment on the accrual accounting. |
| `CancelCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the accrual accounting cancellation comment. |
| `CancelComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The cancellation comment on the accrual accounting. |
| `IsCancelled` | `Boolean` | no |  |  | Specifies if the accrual accounting is cancelled. |
| `BookingId` | `Int64` | no |  |  | The business key identifier of the booking. |
| `Rows` | `AccrualAccountingRows[]` | no | [AccrualAccountingRows](/entities/Accounting/AccrualAccountingRow.md) | expandable, collection | The accrual accounting rows. |
| `BookingRows` | `BookingRows[]` | no | [BookingRows](/entities/Accounting/BookingRow.md) | expandable, collection | The booking rows on the accrual accounting. |
| `AccountsPayableBookingRow` | `BookingRows` | no | [BookingRows](/entities/Accounting/BookingRow.md) | expandable | The booking row of the accrual accounting's account payable. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `AccountsPayableBookingRow` | 1 |
| `VoucherRow` | 2 |
| `ReverseVoucher` | 3 |
| `FreeBooking` | 4 |
| `SalesAgreement` | 5 |
| `SupplierAgreement` | 6 |


## Referenced by

**Accounting**

- [BookingRows](/entities/Accounting/BookingRow.md) — `AccrualAccountingId` (FK)
- [VoucherRows](/entities/Accounting/VoucherRow.md) — `AccrualAccountingId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": null,
  "Text": null,
  "Type": 0,
  "StartDate": null,
  "AccountsPayableId": null,
  "AccountsPayableBookingRowId": null,
  "VoucherId": null,
  "VoucherRowId": null,
  "CommentId": null,
  "Comment": null,
  "CancelCommentId": null,
  "CancelComment": null,
  "IsCancelled": false,
  "BookingId": 0,
  "Rows": null,
  "BookingRows": null,
  "AccountsPayableBookingRow": null
}
```
