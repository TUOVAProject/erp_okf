---
type: API Entity
title: CustomerStatuses
description: Represents a customer status.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerStatus.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerStatus.html
  title: Monitor API — CustomerStatus
module: Sales
api_class: CustomerStatus
doc_name: CustomerStatuses
endpoint: GET /api/v1/Sales/CustomerStatuses
guid: 80966C87-EC9E-47B0-8E99-5034648C9F08
permission: Show customer
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Sales/Customer.md
---

# CustomerStatuses

Represents a customer status.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerStatus`
- **Endpoint:** `GET /api/v1/Sales/CustomerStatuses`
- **Required permission:** Show customer
- **GUID:** `80966C87-EC9E-47B0-8E99-5034648C9F08`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the status. |
| `Code` | `Int64` | no |  |  | The human readable identifier of the status. |
| `Description` | `String` | no |  | max length 400 | The translated description of the status. |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |

## Referenced by

**Sales**

- [Customers](Customer.md) — `Status` (expand)
- [Customers](Customer.md) — `StatusId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null,
  "CompanyIds": null
}
```
