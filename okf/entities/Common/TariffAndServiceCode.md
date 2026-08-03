---
type: API Entity
title: TariffAndServiceCodes
description: Represents a tariff and service code.
resource: https://api.monitor.se/api/Monitor.API.Common.TariffAndServiceCode.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.TariffAndServiceCode.html
  title: Monitor API — TariffAndServiceCode
module: Common
api_class: TariffAndServiceCode
doc_name: TariffAndServiceCodes
endpoint: GET /api/v1/Common/TariffAndServiceCodes
guid: F1C5176E-FF62-4D49-AA2F-D652DE05A6EF
permission: Show basic data for part
introduced_in: '2.30'
property_count: 5
referenced_by:
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/CustomerOrderRow.md
---

# TariffAndServiceCodes

Represents a tariff and service code.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `TariffAndServiceCode`
- **Endpoint:** `GET /api/v1/Common/TariffAndServiceCodes`
- **Required permission:** Show basic data for part
- **GUID:** `F1C5176E-FF62-4D49-AA2F-D652DE05A6EF`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the code. |
| `Code` | `String` | no |  | unique, max length 20 | The human readable identifier of the code. |
| `Name` | `String` | no |  |  | The translated name of the code. |
| `Type` | `Int32?` | yes |  | enum | The type of the code. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the code is active. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `Sales` | 1 |
| `Service` | 2 |
| `Purchase` | 3 |


## Referenced by

**Purchase**

- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `TariffAndServiceCode` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `TariffAndServiceCodeId` (FK)

**Sales**

- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `TariffAndServiceCode` (expand)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `TariffAndServiceCodeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Name": null,
  "Type": null,
  "IsActive": false
}
```
