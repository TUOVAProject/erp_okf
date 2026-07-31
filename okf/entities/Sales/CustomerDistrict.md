---
type: API Entity
title: CustomerDistricts
description: Represents a customer district.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerDistrict.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerDistrict.html
  title: Monitor API — CustomerDistrict
module: Sales
api_class: CustomerDistrict
doc_name: CustomerDistricts
endpoint: GET /api/v1/Sales/CustomerDistricts
guid: 44236786-CFCC-4730-81D9-9830C50F573B
permission: Show customer
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Common/Person.md
- /entities/Inventory/SalesForecast.md
- /entities/Sales/Customer.md
---

# CustomerDistricts

Represents a customer district.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `CustomerDistrict`
- **Endpoint:** `GET /api/v1/Sales/CustomerDistricts`
- **Required permission:** Show customer
- **GUID:** `44236786-CFCC-4730-81D9-9830C50F573B`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer district. |
| `Code` | `Int64` | no |  |  | The human readable identifier of the customer district. |
| `Description` | `String` | no |  | max length 400 | The translated description of the customer district. |
| `CompanyIds` | `Int64[]` | no |  | collection | The business key identifiers of the companies that this entity is available for. |

## Referenced by

**Common**

- [Persons](/entities/Common/Person.md) — `DistrictId` (FK)

**Inventory**

- [SalesForecasts](/entities/Inventory/SalesForecast.md) — `CustomerDistrictId` (FK)

**Sales**

- [Customers](/entities/Sales/Customer.md) — `District` (expand)
- [Customers](/entities/Sales/Customer.md) — `DistrictId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Description": null,
  "CompanyIds": null
}
```
