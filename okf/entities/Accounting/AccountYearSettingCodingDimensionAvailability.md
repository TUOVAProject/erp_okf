---
type: API Entity
title: AccountYearSettingCodingDimensionAvailabilities
description: Represents a coding dimension available on a account for a specific year
  setting.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountYearSettingCodingDimensionAvailability.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountYearSettingCodingDimensionAvailability.html
  title: Monitor API — AccountYearSettingCodingDimensionAvailability
module: Accounting
api_class: AccountYearSettingCodingDimensionAvailability
doc_name: AccountYearSettingCodingDimensionAvailabilities
endpoint: GET /api/v1/Accounting/AccountYearSettingCodingDimensionAvailabilities
guid: 636F00AC-949D-400B-8AA2-4107A8FBA01E
permission: Show accounting year
introduced_in: '2.27'
property_count: 5
references_out:
- /entities/Accounting/AccountYearSetting.md
- /entities/Accounting/CodingDimension.md
referenced_by:
- /entities/Accounting/AccountYearSetting.md
---

# AccountYearSettingCodingDimensionAvailabilities

Represents a coding dimension available on a account for a specific year setting.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `AccountYearSettingCodingDimensionAvailability`
- **Endpoint:** `GET /api/v1/Accounting/AccountYearSettingCodingDimensionAvailabilities`
- **Required permission:** Show accounting year
- **GUID:** `636F00AC-949D-400B-8AA2-4107A8FBA01E`
- **Introduced in:** 2.27

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the Account year setting coding dimension availability. |
| `CodingDimensionId` | `Int64` | no | [CodingDimensions](/entities/Accounting/CodingDimension.md) |  | The business key identifier of the coding dimension. |
| `CodingDimension` | `CodingDimensions` | no | [CodingDimensions](/entities/Accounting/CodingDimension.md) | expandable | The coding dimension. |
| `CodingDimensionAvailability` | `Int32` | no |  | enum | The coding dimension availability state. |
| `AccountYearSettingId` | `Int64` | no | [AccountYearSettings](/entities/Accounting/AccountYearSetting.md) |  | The business key identifier of the account year setting. |

## Enumerations

### CodingDimensionAvailability

| Name | Value |
| --- | ---: |
| `NotAllowed` | 0 |
| `Allowed` | 1 |
| `Mandatory` | 2 |


## Referenced by

**Accounting**

- [AccountYearSettings](/entities/Accounting/AccountYearSetting.md) — `AccountCodingDimensions` (expand)


## Example

```json
{
  "Id": 0,
  "CodingDimensionId": 0,
  "CodingDimension": null,
  "CodingDimensionAvailability": 0,
  "AccountYearSettingId": 0
}
```
