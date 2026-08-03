---
type: API Entity
title: PartTemplates
description: Represents a part template.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartTemplate.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartTemplate.html
  title: Monitor API — PartTemplate
module: Inventory
api_class: PartTemplate
doc_name: PartTemplates
endpoint: GET /api/v1/Inventory/PartTemplates
guid: 429950a6-1de2-4eb6-b509-77cd0c55c9e1
permission: Show basic data for part
introduced_in: '2.47'
property_count: 40
references_out:
- /entities/Common/Country.md
- /entities/Common/Person.md
- /entities/Common/ProductGroup.md
- /entities/Inventory/AbcCode.md
- /entities/Inventory/PartCode.md
- /entities/Inventory/ProfitMarkup.md
- /entities/Inventory/SalesOverheadMarkup.md
referenced_by:
- /entities/Inventory/Part.md
---

# PartTemplates

Represents a part template.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PartTemplate`
- **Endpoint:** `GET /api/v1/Inventory/PartTemplates`
- **Required permission:** Show basic data for part
- **GUID:** `429950a6-1de2-4eb6-b509-77cd0c55c9e1`
- **Introduced in:** 2.47

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part template. |
| `AbcCodeId` | `Int64?` | yes | [AbcCodes](AbcCode.md) |  | The business key identifier of the ABC code that the part template applies. |
| `AnnualVolume` | `Decimal?` | yes |  |  | The annual volume that the part template applies. |
| `AutomaticReportingMode` | `Int32?` | yes |  | enum | The automatic reporting mode that the part template applies. |
| `CategoryString` | `String` | no |  | max length 15 | The category string that the part template applies. |
| `Code` | `String` | no |  | unique, max length 20 | The human readable identifier of the part template. |
| `CountryOfOriginId` | `Int64?` | yes | [Countries](../Common/Country.md) |  | The business key identifier of the country of origin that the part template applies. |
| `DeductSalesForecast` | `Int32?` | yes |  | enum | The sales forecast deduction type that the part template applies. |
| `DeductionMethod` | `Int32?` | yes |  | enum | The sales deduction method that the part template applies if a deduct sales forecast type is defined. |
| `Description` | `String` | no |  |  | The description of the part template. |
| `Eoq` | `Decimal?` | yes |  |  | The EOQ that the part template applies. |
| `IsActive` | `Boolean` | no |  |  | Specifies whether or not the part template is active. |
| `IsDefault` | `Boolean` | no |  |  | Specifies whether or not the part template is the default part template. |
| `IsPreset` | `Boolean` | no |  |  | Specifies whether or not the part template is a preset. |
| `LotSizingRule` | `Int32?` | yes |  | enum | The lot sizing rule that the part template applies. |
| `ManageStockBalance` | `Boolean?` | yes |  |  | The stock balance management strategy that the part template applies. |
| `UseRandomLocationStorage` | `Boolean?` | yes |  |  | The random location storage strategy that the part template applies. |
| `AllowOrderCreationFromCustomerOrder` | `Boolean?` | yes |  |  | The customer order creation permission that the part template applies. |
| `RoundingBase` | `Decimal?` | yes |  |  | The rounding base that the part template applies. |
| `LeadTime` | `TimeSpan?` | yes |  |  | The lead time that the part template applies. |
| `ManufacturingLabelType` | `Int32?` | yes |  | enum | The manufacturing transport label type that the part template applies. |
| `SalesLabelType` | `Int32?` | yes |  | enum | The sales transport label type that the part template applies. |
| `PurchaseLabelType` | `Int32?` | yes |  | enum | The purchase transport label type that the part template applies. |
| `UseInCalculation` | `Boolean` | no |  |  | Whether or not the parts that derive from the part template should be used in calculations. |
| `PartCodeId` | `Int64?` | yes | [PartCodes](PartCode.md) |  | The business key identifier of the part code that the part template applies. |
| `PartType` | `Int32?` | yes |  | enum | The part template type that the part template applies. |
| `PreparerId` | `Int64?` | yes | [Persons](../Common/Person.md) |  | The business key identifier of the preparer that the part template applies. |
| `ProductGroupId` | `Int64?` | yes | [ProductGroups](../Common/ProductGroup.md) |  | The business key identifier of the product group that the part template applies. |
| `ReorderPoint` | `Decimal?` | yes |  |  | The reorder point that the part template applies. |
| `SafetyStock` | `Decimal?` | yes |  |  | The safety stock that the part template applies. |
| `SafetyTime` | `TimeSpan?` | yes |  |  | The safety time that the part template applies. |
| `SerialNumberGeneration` | `Int32?` | yes |  | enum | The serial number generation strategy that the part template applies. |
| `SerialNumberGenerationSource` | `Int32?` | yes |  | enum | The serial number generation source that the part template applies. |
| `TemplateType` | `Int32` | no |  | enum | The template type of the part template. |
| `TraceabilityMode` | `Int32?` | yes |  | enum | The traceability mode that the part template applies. |
| `ProfitMarkupId` | `Int64?` | yes | [ProfitMarkups](ProfitMarkup.md) |  | The business key identifier of the profit markup that the part template applies. |
| `SalesOverheadMarkupId` | `Int64?` | yes | [SalesOverheadMarkups](SalesOverheadMarkup.md) |  | The business key identifier of the sales overhead markup that the part template applies. |
| `PartActivityTemplateId` | `Int64?` | yes |  |  | The business key identifier of the part activity template that the part template applies. References PartActivityTemplate. |
| `PartStatus` | `Int32?` | yes |  | enum | The part status that the part template applies. |
| `LithuanianCountyOfOrigin` | `Int32?` | yes |  | enum, since 25.8 | The county of origin that the part template applies. Only used in the Lithuanian country package. |

## Enumerations

### AutomaticReportingMode

| Name | Value |
| --- | ---: |
| `PickingLocation` | 1 |
| `Cleared` | 2 |
| `BufferLocation` | 4 |
| `Project` | 8 |

### DeductSalesForecast

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `LeadTime` | 1 |
| `Now` | 2 |

### DeductionMethod

| Name | Value |
| --- | ---: |
| `Percent` | 0 |
| `TimeOrder` | 1 |
| `Closest` | 2 |
| `ClosestBefore` | 3 |
| `PeriodicIntervals` | 4 |

### LotSizingRule

| Name | Value |
| --- | ---: |
| `LotForLot` | 1 |
| `FixedQuantity` | 2 |
| `PeriodRequirement` | 3 |
| `Bucketpart` | 4 |
| `Linked` | 5 |

### ManufacturingLabelType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Transport` | 1 |
| `Label` | 2 |
| `SmallLabel` | 3 |
| `MultiLabel` | 4 |
| `SelectAtPrintout` | 5 |

### SalesLabelType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Transport` | 1 |
| `Label` | 2 |
| `SmallLabel` | 3 |
| `MultiLabel` | 4 |
| `SelectAtPrintout` | 5 |

### PurchaseLabelType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Transport` | 1 |
| `Label` | 2 |
| `SmallLabel` | 3 |
| `MultiLabel` | 4 |
| `SelectAtPrintout` | 5 |

### PartType

| Name | Value |
| --- | ---: |
| `Purchased` | 0 |
| `Manufactured` | 1 |
| `Fictitious` | 2 |
| `Service` | 5 |
| `Subcontract` | 6 |

### SerialNumberGeneration

| Name | Value |
| --- | ---: |
| `Never` | 0 |
| `CustomerOrderRegistration` | 1 |
| `ManufacturingOrderRegistration` | 2 |
| `DeliveryReporting` | 3 |

### SerialNumberGenerationSource

| Name | Value |
| --- | ---: |
| `NumberSeries` | 0 |
| `Manual` | 1 |

### TemplateType

| Name | Value |
| --- | ---: |
| `Part` | 0 |
| `ConsumableEquipment` | 1 |
| `ReusableEquipment` | 2 |
| `EquipmentList` | 3 |

### TraceabilityMode

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Batch` | 1 |
| `Individual` | 2 |
| `IndividualOnlyWithdrawal` | 4 |

### PartStatus

| Name | Value |
| --- | ---: |
| `Quote` | 1 |
| `Prototype` | 2 |
| `New` | 3 |
| `Normal` | 4 |
| `NewRevision` | 5 |
| `PhasingOut` | 6 |
| `Expired` | 9 |
| `Inactive` | 99 |

### LithuanianCountyOfOrigin

| Name | Value |
| --- | ---: |
| `A` | 1 |
| `K` | 2 |
| `L` | 3 |
| `M` | 4 |
| `P` | 5 |
| `S` | 6 |
| `J` | 7 |
| `T` | 8 |
| `U` | 9 |
| `V` | 10 |


## Referenced by

**Inventory**

- [Parts](Part.md) — `PartTemplate` (expand)
- [Parts](Part.md) — `PartTemplateId` (FK)


## Example

```json
{
  "Id": 0,
  "AbcCodeId": null,
  "AnnualVolume": null,
  "AutomaticReportingMode": null,
  "CategoryString": null,
  "Code": null,
  "CountryOfOriginId": null,
  "DeductSalesForecast": null,
  "DeductionMethod": null,
  "Description": null,
  "Eoq": null,
  "IsActive": false,
  "IsDefault": false,
  "IsPreset": false,
  "LotSizingRule": null,
  "ManageStockBalance": null,
  "UseRandomLocationStorage": null,
  "AllowOrderCreationFromCustomerOrder": null,
  "RoundingBase": null,
  "LeadTime": null,
  "ManufacturingLabelType": null,
  "SalesLabelType": null,
  "PurchaseLabelType": null,
  "UseInCalculation": false,
  "PartCodeId": null,
  "PartType": null,
  "PreparerId": null,
  "ProductGroupId": null,
  "ReorderPoint": null,
  "SafetyStock": null,
  "SafetyTime": null,
  "SerialNumberGeneration": null,
  "SerialNumberGenerationSource": null,
  "TemplateType": 0,
  "TraceabilityMode": null,
  "ProfitMarkupId": null,
  "SalesOverheadMarkupId": null,
  "PartActivityTemplateId": null,
  "PartStatus": null,
  "LithuanianCountyOfOrigin": null
}
```
