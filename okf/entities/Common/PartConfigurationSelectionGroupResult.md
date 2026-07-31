---
type: API Entity
title: PartConfigurationSelectionGroupResults
description: Represents a part configuration selection group result
resource: https://api.monitor.se/api/Monitor.API.Common.PartConfigurationSelectionGroupResult.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PartConfigurationSelectionGroupResult.html
  title: Monitor API — PartConfigurationSelectionGroupResult
module: Common
api_class: PartConfigurationSelectionGroupResult
doc_name: PartConfigurationSelectionGroupResults
endpoint: GET /api/v1/Common/PartConfigurationSelectionGroupResults
guid: 309ca79d-4a6b-4e70-9354-204f167449fe
permission: Show part
introduced_in: '25.7'
property_count: 22
references_out:
- /entities/Common/Currency.md
- /entities/Common/PartConfigurationComponentSnapshot.md
- /entities/Common/PartConfigurationResult.md
- /entities/Inventory/Part.md
referenced_by:
- /entities/Common/PartConfigurationResult.md
---

# PartConfigurationSelectionGroupResults

Represents a part configuration selection group result

- **Module:** [Common](/modules/Common.md)
- **API class:** `PartConfigurationSelectionGroupResult`
- **Endpoint:** `GET /api/v1/Common/PartConfigurationSelectionGroupResults`
- **Required permission:** Show part
- **GUID:** `309ca79d-4a6b-4e70-9354-204f167449fe`
- **Introduced in:** 25.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part configuration selection group result. |
| `PartId` | `Int64` | no | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the part. |
| `SelectionGroupTemplateRowId` | `Int64` | no |  |  | The business key identifier of the selection group row snapshot. |
| `RowIndex` | `Int32` | no |  |  | The row of the result. |
| `SelectionGroupTemplateId` | `Int64` | no | [PartConfigurationComponentSnapshots](/entities/Common/PartConfigurationComponentSnapshot.md) |  | The business key identifier of the selection group snapshot. |
| `PartConfigurationResultId` | `Int64` | no | [PartConfigurationResults](/entities/Common/PartConfigurationResult.md) |  | The business key identifier of the part configuration result. |
| `Quantity` | `Decimal` | no |  | since 25.9 | The quantity of the result row. |
| `SetupQuantity` | `Decimal` | no |  | since 26.3 | The setup quantity of the result row. |
| `UnitPrice` | `Decimal?` | yes |  | since 26.3 | The unit price amount. |
| `UnitPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) | since 26.3 | The business key identifier of the currency for the unit price. |
| `UnitPriceInCompanyCurrency` | `Decimal?` | yes |  | since 26.3 | The unit price amount in company currency. |
| `UnitPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) | since 26.3 | The business key identifier of the currency for the unit price in company currency. |
| `DiscountPercentage` | `Decimal` | no |  | since 26.3 | The discount percentage. |
| `PriceFormulaFactor` | `Decimal` | no |  | since 26.3 | The price formula factor. |
| `LockedUnitPrice` | `Boolean` | no |  | since 26.3 | Whether the unit price is locked. |
| `LockedDiscount` | `Boolean` | no |  | since 26.3 | Whether the discount is locked. |
| `SelectedByType` | `Int32` | no |  | enum, since 26.3 | The type indicating how the row was selected. |
| `SelectedByName` | `String` | no |  | since 26.3 | The name indicating who or what selected the row. |
| `SelectionType` | `Int32` | no |  | enum, since 26.3 | The selection type. |
| `ToOperation` | `Int32?` | yes |  | since 26.3 | The target operation number. |
| `MainPartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) | since 26.3 | The business key identifier of the main part. |
| `Position` | `String` | no |  | since 26.3 | The position string. |

## Enumerations

### SelectedByType

| Name | Value |
| --- | ---: |
| `User` | 0 |
| `Preset` | 1 |

### SelectionType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Initialization` | 5 |
| `RuleUnselect` | 10 |
| `Manual` | 20 |
| `GroupRule` | 30 |
| `SelectionRuleSelect` | 40 |
| `Locked` | 50 |
| `TemporaryLockedByManualSelection` | 60 |


## Referenced by

**Common**

- [PartConfigurationResults](/entities/Common/PartConfigurationResult.md) — `PartConfigurationSelectionGroupResults` (expand)


## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "SelectionGroupTemplateRowId": 0,
  "RowIndex": 0,
  "SelectionGroupTemplateId": 0,
  "PartConfigurationResultId": 0,
  "Quantity": 0.0,
  "SetupQuantity": 0.0,
  "UnitPrice": null,
  "UnitPriceCurrencyId": null,
  "UnitPriceInCompanyCurrency": null,
  "UnitPriceInCompanyCurrencyCurrencyId": null,
  "DiscountPercentage": 0.0,
  "PriceFormulaFactor": 0.0,
  "LockedUnitPrice": false,
  "LockedDiscount": false,
  "SelectedByType": 0,
  "SelectedByName": null,
  "SelectionType": 0,
  "ToOperation": null,
  "MainPartId": null,
  "Position": null
}
```
