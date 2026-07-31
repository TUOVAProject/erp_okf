---
type: API Entity
title: EdiBehaviors
description: Represents an Edi Behavior
resource: https://api.monitor.se/api/Monitor.API.Common.EdiBehavior.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.EdiBehavior.html
  title: Monitor API — EdiBehavior
module: Common
api_class: EdiBehavior
doc_name: EdiBehaviors
endpoint: GET /api/v1/Common/EdiBehaviors
guid: 0DDB3AF5-69B4-4046-B916-D0E082D1F392
permission: Show EDI settings
introduced_in: '25.4'
property_count: 8
references_out:
- /entities/Common/EdiChannelConfiguration.md
- /entities/Common/Warehouse.md
- /entities/Sales/Customer.md
---

# EdiBehaviors

Represents an Edi Behavior

- **Module:** [Common](/modules/Common.md)
- **API class:** `EdiBehavior`
- **Endpoint:** `GET /api/v1/Common/EdiBehaviors`
- **Required permission:** Show EDI settings
- **GUID:** `0DDB3AF5-69B4-4046-B916-D0E082D1F392`
- **Introduced in:** 25.4

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the edi behaviour. |
| `Name` | `String` | no |  | unique, max length 80 | The name of the edi behaviour. |
| `Module` | `Int32` | no |  | enum | The module of the edi behaviour. |
| `EdiChannelConfigurations` | `EdiChannelConfigurations[]` | no | [EdiChannelConfigurations](/entities/Common/EdiChannelConfiguration.md) | expandable, collection | The edi channel configurations of edi behavior. |
| `Customers` | `Customers[]` | no | [Customers](/entities/Sales/Customer.md) | expandable, collection | The customer of edi behavior. |
| `InvoiceCustomers` | `Customers[]` | no | [Customers](/entities/Sales/Customer.md) | expandable, collection | The invoice customers of edi behavior. |
| `WarehouseId` | `Int64` | no | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the warehouse. |
| `Warehouse` | `Warehouses` | no | [Warehouses](/entities/Common/Warehouse.md) | expandable | The warehouse of the edi behavior. |

## Enumerations

### Module

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Sales` | 1 |
| `Purchase` | 2 |


## Example

```json
{
  "Id": 0,
  "Name": null,
  "Module": 0,
  "EdiChannelConfigurations": null,
  "Customers": null,
  "InvoiceCustomers": null,
  "WarehouseId": 0,
  "Warehouse": null
}
```
