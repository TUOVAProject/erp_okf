---
type: API Entity
title: FixedAssetSales
description: Represents a sale/retirement of a fixed assets object.
resource: https://api.monitor.se/api/Monitor.API.Accounting.FixedAssetSale.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.FixedAssetSale.html
  title: Monitor API — FixedAssetSale
module: Accounting
api_class: FixedAssetSale
doc_name: FixedAssetSales
endpoint: GET /api/v1/Accounting/FixedAssetSales
guid: 0ff45db4-87c1-4c9f-9f00-60a22491f716
permission: Show fixed assets objects
introduced_in: '23.8'
property_count: 14
references_out:
- /entities/Accounting/AccountsReceivable.md
- /entities/Accounting/Booking.md
- /entities/Common/Comment.md
- /entities/Sales/Customer.md
referenced_by:
- /entities/Accounting/FixedAsset.md
---

# FixedAssetSales

Represents a sale/retirement of a fixed assets object.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `FixedAssetSale`
- **Endpoint:** `GET /api/v1/Accounting/FixedAssetSales`
- **Required permission:** Show fixed assets objects
- **GUID:** `0ff45db4-87c1-4c9f-9f00-60a22491f716`
- **Introduced in:** 23.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the fixed asset sale. |
| `SalesDate` | `DateTimeOffset` | no |  |  | The sales date of the fixed asset sale. |
| `Type` | `Int32` | no |  | enum | The type of fixed asset sale. |
| `Quantity` | `Decimal` | no |  |  | The sold quantity of the fixed assets object. |
| `PartOfAcquisitionValue` | `Decimal` | no |  |  | The sold part of the fixed assets object's acquisition value. |
| `SalesValue` | `Decimal` | no |  |  | The sales value of the fixed asset sale. |
| `SalesProfit` | `Decimal?` | yes |  |  | The profit of the fixed asset sale. |
| `AccountsReceivableId` | `Int64?` | yes | [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) |  | The business key identifier of the accounts receivable linked to the fixed asset sale. |
| `CustomerId` | `Int64?` | yes | [Customers](/entities/Sales/Customer.md) |  | The business key identifier of the customer linked to the fixed asset sale. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the comment to the fixed asset sale. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The comment to the fixed asset sale. |
| `VoucherText` | `String` | no |  | max length 100 | The voucher text of the fixed asset sale. |
| `SalesTimestamp` | `DateTimeOffset` | no |  |  | The timestamp of the fixed asset sale. |
| `BookingId` | `Int64?` | yes | [Bookings](/entities/Accounting/Booking.md) |  | The business key identifier of the booking of the fixed asset sale. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Sale` | 0 |
| `Retirement` | 1 |


## Referenced by

**Accounting**

- [FixedAssets](/entities/Accounting/FixedAsset.md) — `Sales` (expand)


## Example

```json
{
  "Id": 0,
  "SalesDate": "0001-01-01T00:00:00+00:00",
  "Type": 0,
  "Quantity": 0.0,
  "PartOfAcquisitionValue": 0.0,
  "SalesValue": 0.0,
  "SalesProfit": null,
  "AccountsReceivableId": null,
  "CustomerId": null,
  "CommentId": null,
  "Comment": null,
  "VoucherText": null,
  "SalesTimestamp": "0001-01-01T00:00:00+00:00",
  "BookingId": null
}
```
