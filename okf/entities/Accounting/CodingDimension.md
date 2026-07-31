---
type: API Entity
title: CodingDimensions
description: Represents a Coding dimension.
resource: https://api.monitor.se/api/Monitor.API.Accounting.CodingDimension.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.CodingDimension.html
  title: Monitor API — CodingDimension
module: Accounting
api_class: CodingDimension
doc_name: CodingDimensions
endpoint: GET /api/v1/Accounting/CodingDimensions
guid: 254D2D51-C1BE-420D-8EC1-2718F669C45E
permission: Show dimensions/dimension codes
introduced_in: '2.27'
property_count: 6
references_out:
- /entities/Accounting/CodingElement.md
referenced_by:
- /entities/Accounting/AccountYearSettingCodingDimensionAvailability.md
- /entities/Accounting/CodingElement.md
- /entities/Accounting/CodingEntryElement.md
---

# CodingDimensions

Represents a Coding dimension.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `CodingDimension`
- **Endpoint:** `GET /api/v1/Accounting/CodingDimensions`
- **Required permission:** Show dimensions/dimension codes
- **GUID:** `254D2D51-C1BE-420D-8EC1-2718F669C45E`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the coding dimension. |
| `Number` | `Int32` | no |  |  | The number of the coding dimension. |
| `Description` | `String` | no |  |  | The description of the coding dimension. |
| `CodeDescription` | `String` | no |  |  | The description of the coding dimension code. |
| `ReferenceEntityType` | `Int32` | no |  | enum | The coding dimension reference type of the coding dimension. |
| `CodingElements` | `CodingElements[]` | no | [CodingElements](/entities/Accounting/CodingElement.md) | expandable, collection | The coding elements of the coding dimension. |

## Enumerations

### ReferenceEntityType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Project` | 1 |
| `ProductGroup` | 2 |
| `PartCode` | 3 |
| `Part` | 4 |
| `Department` | 5 |
| `WorkCenter` | 6 |
| `CustomerRootFromOrder` | 7 |
| `CustomerRootFromInvoice` | 8 |
| `SupplierRoot` | 9 |
| `Person` | 10 |
| `CustomerAccountGroupOnCustomer` | 11 |
| `CustomerDistrict` | 12 |
| `CustomerType` | 13 |
| `SupplierAccountGroupOnSupplier` | 14 |
| `SupplierDistrict` | 15 |
| `SupplierType` | 16 |


## Referenced by

**Accounting**

- [AccountYearSettingCodingDimensionAvailabilities](/entities/Accounting/AccountYearSettingCodingDimensionAvailability.md) — `CodingDimension` (expand)
- [AccountYearSettingCodingDimensionAvailabilities](/entities/Accounting/AccountYearSettingCodingDimensionAvailability.md) — `CodingDimensionId` (FK)
- [CodingElements](/entities/Accounting/CodingElement.md) — `CodingDimensionId` (FK)
- [CodingEntryElements](/entities/Accounting/CodingEntryElement.md) — `CodingDimension` (expand)
- [CodingEntryElements](/entities/Accounting/CodingEntryElement.md) — `CodingDimensionId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "CodeDescription": null,
  "ReferenceEntityType": 0,
  "CodingElements": null
}
```
