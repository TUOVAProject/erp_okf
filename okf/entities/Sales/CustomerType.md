---
type: API Entity
title: CustomerTypes
description: Represents a customer type.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerType.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerType.html
  title: Monitor API — CustomerType
module: Sales
api_class: CustomerType
doc_name: CustomerTypes
endpoint: GET /api/v1/Sales/CustomerTypes
guid: 38834C07-1D87-4B1B-B7F7-49E69704080F
permission: Show customer
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Sales/Customer.md
---

# CustomerTypes

Represents a customer type.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `CustomerType`
- **Endpoint:** `GET /api/v1/Sales/CustomerTypes`
- **Required permission:** Show customer
- **GUID:** `38834C07-1D87-4B1B-B7F7-49E69704080F`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the type. |
| `Code` | `Int64` | no |  |  | The human readable identifier of the type. |
| `Description` | `String` | no |  | max length 400 | The translated description of the type. |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |

## Referenced by

**Sales**

- [Customers](/entities/Sales/Customer.md) — `Type` (expand)
- [Customers](/entities/Sales/Customer.md) — `TypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null,
  "CompanyIds": null
}
```
