---
type: API Entity
title: WriteOffCodes
description: Represents a write off code.
resource: https://api.monitor.se/api/Monitor.API.Common.WriteOffCode.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.WriteOffCode.html
  title: Monitor API — WriteOffCode
module: Common
api_class: WriteOffCode
doc_name: WriteOffCodes
endpoint: GET /api/v1/Common/WriteOffCodes
guid: 63A4D27E-040B-4A14-A782-0BFA901228BC
permission: Show bank settings
introduced_in: '22.8'
property_count: 7
references_out:
- /entities/Accounting/CodingEntry.md
referenced_by:
- /entities/Accounting/IncomingPayment.md
- /entities/Accounting/OutgoingPayment.md
- /entities/Accounting/SetOffDestination.md
---

# WriteOffCodes

Represents a write off code.

- **Module:** [Common](/modules/Common.md)
- **API class:** `WriteOffCode`
- **Endpoint:** `GET /api/v1/Common/WriteOffCodes`
- **Required permission:** Show bank settings
- **GUID:** `63A4D27E-040B-4A14-A782-0BFA901228BC`
- **Introduced in:** 22.8

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the write off code. |
| `Code` | `String` | no |  | unique, max length 5 | The human readable identifier of the write off code. |
| `Description` | `String` | no |  |  | The translated description of the write off code. |
| `IncomingPaymentCodingEntryId` | `Int64` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) |  | The business key identifier of the write off code's coding entry for incoming payments. |
| `IncomingPaymentCodingEntry` | `CodingEntries` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) | expandable | The write off code's coding entry for incoming payments. |
| `OutgoingPaymentCodingEntryId` | `Int64` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) |  | The business key identifier of the write off code's coding entry for outgoing payments. |
| `OutgoingPaymentCodingEntry` | `CodingEntries` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) | expandable | The write off code's coding entry for outgoing payments. |

## Referenced by

**Accounting**

- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `WriteOffCodeId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `WriteOffCodeId` (FK)
- [SetOffDestination](/entities/Accounting/SetOffDestination.md) — `WriteOffCodeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "IncomingPaymentCodingEntryId": 0,
  "IncomingPaymentCodingEntry": null,
  "OutgoingPaymentCodingEntryId": 0,
  "OutgoingPaymentCodingEntry": null
}
```
