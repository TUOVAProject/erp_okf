---
type: API Entity
title: StatisticalGoodsCodes
description: Represents a queryable statistical goods code.
resource: https://api.monitor.se/api/Monitor.API.Common.StatisticalGoodsCode.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.StatisticalGoodsCode.html
  title: Monitor API — StatisticalGoodsCode
module: Common
api_class: StatisticalGoodsCode
doc_name: StatisticalGoodsCodes
endpoint: GET /api/v1/Common/StatisticalGoodsCodes
guid: ABCEBA49-7308-44B5-AB33-BBB395210994
permission: Show CN codes
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Inventory/Part.md
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/ShipmentCustomsRow.md
---

# StatisticalGoodsCodes

Represents a queryable statistical goods code.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `StatisticalGoodsCode`
- **Endpoint:** `GET /api/v1/Common/StatisticalGoodsCodes`
- **Required permission:** Show CN codes
- **GUID:** `ABCEBA49-7308-44B5-AB33-BBB395210994`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the statistical goods code. |
| `Code` | `String` | no |  | unique, max length 14 | The human readable identifier of the statistical goods code. |
| `Description` | `String` | no |  |  | The translated description of the statistical goods code. |
| `DeclarationType` | `Int32` | no |  | enum | The declaration type of the statistical goods code. |

## Enumerations

### DeclarationType

| Name | Value |
| --- | ---: |
| `Weight` | 1 |
| `OtherQuantity` | 2 |
| `WeightAndOtherQuantity` | 3 |
| `ExcludeFromDeclaration` | 4 |


## Referenced by

**Inventory**

- [Parts](../Inventory/Part.md) — `StatisticalGoodsCode` (expand)
- [Parts](../Inventory/Part.md) — `StatisticalGoodsCodeId` (FK)

**Purchase**

- [InquiryRows](../Purchase/InquiryRow.md) — `StatisticalGoodsCodeId` (FK)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `StatisticalGoodsCode` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `StatisticalGoodsCodeId` (FK)

**Sales**

- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `StatisticalGoodsCodeId` (FK)
- [QuoteRows](../Sales/QuoteRow.md) — `StatisticalGoodsCodeId` (FK)
- [ShipmentCustomsRows](../Sales/ShipmentCustomsRow.md) — `StatisticalGoodsCode` (expand)
- [ShipmentCustomsRows](../Sales/ShipmentCustomsRow.md) — `StatisticalGoodsCodeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "DeclarationType": 0
}
```
