---
type: API Entity
title: Bookings
description: Represents a booking.
resource: https://api.monitor.se/api/Monitor.API.Accounting.Booking.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.Booking.html
  title: Monitor API — Booking
module: Accounting
api_class: Booking
doc_name: Bookings
endpoint: GET /api/v1/Accounting/Bookings
guid: 9c0f59b7-6d48-4099-8e4b-c95ced9cd87d
introduced_in: '2.44'
property_count: 4
references_out:
- /entities/Accounting/BookingRow.md
referenced_by:
- /entities/Accounting/AccountsReceivable.md
- /entities/Accounting/BookingRow.md
- /entities/Accounting/FixedAssetSale.md
- /entities/Accounting/IncomingPayment.md
- /entities/Accounting/OutgoingPayment.md
---

# Bookings

Represents a booking.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `Booking`
- **Endpoint:** `GET /api/v1/Accounting/Bookings`
- **GUID:** `9c0f59b7-6d48-4099-8e4b-c95ced9cd87d`
- **Introduced in:** 2.44

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the booking. |
| `ParentClass` | `Guid` | no |  |  | The GUID of the booking’s owner type. |
| `ParentId` | `Int64` | no |  |  | The business key identifier of the booking owner. |
| `Rows` | `BookingRows[]` | no | [BookingRows](/entities/Accounting/BookingRow.md) | expandable, collection | The rows that belong to the booking. |

## Referenced by

**Accounting**

- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `Booking` (expand)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `BookingId` (FK)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `CancelBooking` (expand)
- [AccountsReceivables](/entities/Accounting/AccountsReceivable.md) — `CancelBookingId` (FK)
- [BookingRows](/entities/Accounting/BookingRow.md) — `BookingId` (FK)
- [FixedAssetSales](/entities/Accounting/FixedAssetSale.md) — `BookingId` (FK)
- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `BookingId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `BookingId` (FK)


## Example

```json
{
  "Id": 0,
  "ParentClass": "00000000-0000-0000-0000-000000000000",
  "ParentId": 0,
  "Rows": null
}
```
