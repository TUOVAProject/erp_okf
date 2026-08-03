---
type: API Entity
title: OtherCustomerNumbers
description: Represents an alternative customer code mainly used for EDI.
resource: https://api.monitor.se/api/Monitor.API.Sales.OtherCustomerNumber.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.OtherCustomerNumber.html
  title: Monitor API — OtherCustomerNumber
module: Sales
api_class: OtherCustomerNumber
doc_name: OtherCustomerNumbers
endpoint: GET /api/v1/Sales/OtherCustomerNumbers
guid: 5C82F478-6089-4004-A032-965C50A8AC94
permission: Show customer
introduced_in: '2.32'
property_count: 5
references_out:
- /entities/Sales/Customer.md
referenced_by:
- /entities/Sales/Customer.md
---

# OtherCustomerNumbers

Represents an alternative customer code mainly used for EDI.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `OtherCustomerNumber`
- **Endpoint:** `GET /api/v1/Sales/OtherCustomerNumbers`
- **Required permission:** Show customer
- **GUID:** `5C82F478-6089-4004-A032-965C50A8AC94`
- **Introduced in:** 2.32

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the other customer number. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if this is the default/active other customer number. |
| `Number` | `String` | no |  | max length 25 | The human readable identifier of the other customer number. |
| `CustomerId` | `Int64` | no | [Customers](Customer.md) |  | The business key identifier of the owning customer. |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |

## Referenced by

**Sales**

- [Customers](Customer.md) — `OtherCustomerNumbers` (expand)


## Example

```json
{
  "Id": 0,
  "IsDefault": false,
  "Number": null,
  "CustomerId": 0,
  "CompanyIds": null
}
```
