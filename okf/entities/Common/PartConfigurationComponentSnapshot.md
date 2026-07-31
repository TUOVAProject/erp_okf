---
type: API Entity
title: PartConfigurationComponentSnapshots
description: Represents a part configuration component snapshot.
resource: https://api.monitor.se/api/Monitor.API.Common.PartConfigurationComponentSnapshot.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PartConfigurationComponentSnapshot.html
  title: Monitor API — PartConfigurationComponentSnapshot
module: Common
api_class: PartConfigurationComponentSnapshot
doc_name: PartConfigurationComponentSnapshots
endpoint: GET /api/v1/Common/PartConfigurationComponentSnapshots
guid: 405B6AA4-3E0E-4F72-A759-B0551BEBB747
permission: Show part
introduced_in: '26.3'
property_count: 32
references_out:
- /entities/Common/PartConfigurationComponentSnapshot.md
referenced_by:
- /entities/Common/PartConfigurationComponentSnapshot.md
- /entities/Common/PartConfigurationSelectionGroupResult.md
---

# PartConfigurationComponentSnapshots

Represents a part configuration component snapshot.

- **Module:** [Common](/modules/Common.md)
- **API class:** `PartConfigurationComponentSnapshot`
- **Endpoint:** `GET /api/v1/Common/PartConfigurationComponentSnapshots`
- **Required permission:** Show part
- **GUID:** `405B6AA4-3E0E-4F72-A759-B0551BEBB747`
- **Introduced in:** 26.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the component snapshot. |
| `ComponentType` | `Int32` | no |  | enum | The component type discriminator. |
| `ParentId` | `Int64` | no |  |  | The business key identifier of the template snapshot this component belongs to. |
| `OriginComponentId` | `Int64?` | yes |  |  | The business key identifier of the origin configuration component. |
| `ParentRowId` | `Int64?` | yes | [PartConfigurationComponentSnapshots](/entities/Common/PartConfigurationComponentSnapshot.md) |  | The business key identifier of the parent component within the same template (self-referencing hierarchy). For example, a variable nested under a section. |
| `RowIndex` | `Int32?` | yes |  |  | The row index for ordering. |
| `ShowOnDocument` | `Int32?` | yes |  |  | Document types to show the section on. Only applicable for Section components. |
| `ShowOnFooter` | `Int32?` | yes |  |  | Document types to show the section footer on. Only applicable for Section components. |
| `Visible` | `Boolean?` | yes |  |  | Whether the section is visible. Only applicable for Section components. |
| `ExternalVisible` | `Boolean?` | yes |  |  | Whether the section is externally visible. Only applicable for Section components. |
| `Name` | `String` | no |  |  | The variable name. Only applicable for Variable components. |
| `VariableType` | `Int32?` | yes |  |  | The variable type. Only applicable for Variable components. |
| `Formula` | `String` | no |  |  | The variable formula. Only applicable for Variable components. |
| `Mandatory` | `Boolean?` | yes |  |  | Whether the variable is mandatory. Only applicable for Variable components. |
| `Min` | `Decimal?` | yes |  |  | The minimum value. Only applicable for Variable components. |
| `Max` | `Decimal?` | yes |  |  | The maximum value. Only applicable for Variable components. |
| `NumberOfDecimals` | `Int32?` | yes |  |  | The number of decimals. Only applicable for Variable components. |
| `RoundingBase` | `Decimal?` | yes |  |  | The rounding base. Only applicable for Variable components. |
| `UnitId` | `Int64?` | yes |  |  | The business key identifier of the unit. Only applicable for Variable components. |
| `ExtraFieldTemplateId` | `Int64?` | yes |  |  | The business key identifier of the extra field template. Only applicable for Variable components. |
| `VariableId` | `Int64?` | yes |  |  | The business key identifier of the variable. Only applicable for Variable components. |
| `DocumentDisplaySettings` | `Int32?` | yes |  |  | The document display settings. Only applicable for Variable components. |
| `BindPropertyType` | `Int32?` | yes |  |  | The bind property type. Only applicable for Variable components. |
| `Code` | `String` | no |  |  | The selection group code. Only applicable for SelectionGroup components. |
| `AutomaticSelectionAlternative` | `Int32?` | yes |  | enum | The automatic selection alternative. Only applicable for SelectionGroup components. |
| `MaximumSelectedRows` | `Int32?` | yes |  |  | The maximum number of selected rows. Only applicable for SelectionGroup components. |
| `MinimumSelectedRows` | `Int32?` | yes |  |  | The minimum number of selected rows. Only applicable for SelectionGroup components. |
| `MinimumSelectedQuantity` | `Decimal?` | yes |  |  | The minimum selected quantity. Only applicable for SelectionGroup components. |
| `MaximumSelectedQuantity` | `Decimal?` | yes |  |  | The maximum selected quantity. Only applicable for SelectionGroup components. |
| `ManagedOptionsType` | `Int32?` | yes |  | enum | The managed options type. Only applicable for SelectionGroup components. |
| `ManagedOptionsIdentifier` | `String` | no |  |  | The managed options identifier. Only applicable for SelectionGroup components. |
| `SourceVersion` | `Int32?` | yes |  |  | The source version. Only applicable for SelectionGroup components. |

## Enumerations

### ComponentType

| Name | Value |
| --- | ---: |
| `Section` | 0 |
| `Variable` | 1 |
| `SelectionGroup` | 2 |

### AutomaticSelectionAlternative

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `YesFirst` | 1 |
| `YesAll` | 2 |

### ManagedOptionsType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Selection` | 1 |
| `SelectionAndQuantity` | 2 |


## Referenced by

**Common**

- [PartConfigurationComponentSnapshots](/entities/Common/PartConfigurationComponentSnapshot.md) — `ParentRowId` (FK)
- [PartConfigurationSelectionGroupResults](/entities/Common/PartConfigurationSelectionGroupResult.md) — `SelectionGroupTemplateId` (FK)


## Example

```json
{
  "Id": 0,
  "ComponentType": 0,
  "ParentId": 0,
  "OriginComponentId": null,
  "ParentRowId": null,
  "RowIndex": null,
  "ShowOnDocument": null,
  "ShowOnFooter": null,
  "Visible": null,
  "ExternalVisible": null,
  "Name": null,
  "VariableType": null,
  "Formula": null,
  "Mandatory": null,
  "Min": null,
  "Max": null,
  "NumberOfDecimals": null,
  "RoundingBase": null,
  "UnitId": null,
  "ExtraFieldTemplateId": null,
  "VariableId": null,
  "DocumentDisplaySettings": null,
  "BindPropertyType": null,
  "Code": null,
  "AutomaticSelectionAlternative": null,
  "MaximumSelectedRows": null,
  "MinimumSelectedRows": null,
  "MinimumSelectedQuantity": null,
  "MaximumSelectedQuantity": null,
  "ManagedOptionsType": null,
  "ManagedOptionsIdentifier": null,
  "SourceVersion": null
}
```
