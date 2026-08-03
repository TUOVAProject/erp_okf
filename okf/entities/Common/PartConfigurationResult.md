---
type: API Entity
title: PartConfigurationResults
description: Represents a part configuration result.
resource: https://api.monitor.se/api/Monitor.API.Common.PartConfigurationResult.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PartConfigurationResult.html
  title: Monitor API — PartConfigurationResult
module: Common
api_class: PartConfigurationResult
doc_name: PartConfigurationResults
endpoint: GET /api/v1/Common/PartConfigurationResults
guid: E1BE03D8-6DBC-437E-89CF-D947C3299218
permission: Show part
introduced_in: '2.55'
property_count: 21
references_out:
- /entities/Common/Currency.md
- /entities/Common/PartConfiguration.md
- /entities/Common/PartConfigurationSelectionGroupResult.md
- /entities/Common/PartConfigurationTemplate.md
- /entities/Inventory/Part.md
referenced_by:
- /entities/Common/PartConfiguration.md
- /entities/Common/PartConfigurationSelectionGroupResult.md
---

# PartConfigurationResults

Represents a part configuration result.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `PartConfigurationResult`
- **Endpoint:** `GET /api/v1/Common/PartConfigurationResults`
- **Required permission:** Show part
- **GUID:** `E1BE03D8-6DBC-437E-89CF-D947C3299218`
- **Introduced in:** 2.55

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part configuration result. |
| `TemplateId` | `Int64` | no | [PartConfigurationTemplates](PartConfigurationTemplate.md) |  | The business key identifier of the result's template. |
| `MainPartId` | `Int64?` | yes | [Parts](../Inventory/Part.md) |  | The business key identifier of the part to configure. |
| `Quantity` | `Decimal` | no |  |  | The quantity to produce from this configuration. |
| `UnitPrice` | `Decimal?` | yes |  |  | The unit price of the configured part. |
| `UnitPriceCurrencyId` | `Int64?` | yes | [Currencies](Currency.md) |  | The business key identifier of the currency for the configured part's unit price. |
| `StandardPrice` | `Decimal?` | yes |  |  | The standard price of the configured part. |
| `StandardPriceCurrencyId` | `Int64?` | yes | [Currencies](Currency.md) |  | The business key identifier of the currency for the configured part's standard price. |
| `UnitPriceInCompanyCurrency` | `Decimal?` | yes |  |  | The unit price of the configured part int the company's currency. |
| `UnitPriceInCompanyCurrencyCurrencyId` | `Int64?` | yes | [Currencies](Currency.md) |  | The business key identifier of the currency for the configured part's price in company currency. |
| `DiscountPercentage` | `Decimal` | no |  |  | The discount percentage for the configured part. |
| `LockedUnitPrice` | `Boolean` | no |  |  | If the unit price is locked on the configured part. |
| `LockedDiscount` | `Boolean` | no |  |  | If the discount percentage is locked on the configured part. |
| `AlternativePreparationCode` | `String` | no |  | max length 200 | The alternative preparation code on the configured part. |
| `WeightPerUnit` | `Decimal?` | yes |  |  | The weight per unit on the configured part. |
| `IsValid` | `Boolean` | no |  |  | If the configuration is valid. |
| `PriceFormulaFactor` | `Decimal` | no |  |  | The price formula factor for the configured part. |
| `SnapshotId` | `Int64?` | yes |  |  | The business key identifier of the result's snapshot. |
| `PartConfigurationId` | `Int64?` | yes | [PartConfigurations](PartConfiguration.md) |  | The business key identifier of the result's configuration. |
| `PartCalculationId` | `Int64?` | yes |  |  | The business key identifier of the result's calculation. |
| `PartConfigurationSelectionGroupResults` | `PartConfigurationSelectionGroupResults[]` | no | [PartConfigurationSelectionGroupResults](PartConfigurationSelectionGroupResult.md) | collection, since 25.7 | The list of Part configuration selection group result. |

## Referenced by

**Common**

- [PartConfigurationSelectionGroupResults](PartConfigurationSelectionGroupResult.md) — `PartConfigurationResultId` (FK)
- [PartConfigurations](PartConfiguration.md) — `ResultId` (FK)


## Example

```json
{
  "Id": 0,
  "TemplateId": 0,
  "MainPartId": null,
  "Quantity": 0.0,
  "UnitPrice": null,
  "UnitPriceCurrencyId": null,
  "StandardPrice": null,
  "StandardPriceCurrencyId": null,
  "UnitPriceInCompanyCurrency": null,
  "UnitPriceInCompanyCurrencyCurrencyId": null,
  "DiscountPercentage": 0.0,
  "LockedUnitPrice": false,
  "LockedDiscount": false,
  "AlternativePreparationCode": null,
  "WeightPerUnit": null,
  "IsValid": false,
  "PriceFormulaFactor": 0.0,
  "SnapshotId": null,
  "PartConfigurationId": null,
  "PartCalculationId": null,
  "PartConfigurationSelectionGroupResults": null
}
```
