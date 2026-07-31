---
type: API Entity
title: SalesAgreementTypes
description: Represents an agreement type.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreementType.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesAgreementType.html
  title: Monitor API — SalesAgreementType
module: Sales
api_class: SalesAgreementType
doc_name: SalesAgreementTypes
endpoint: GET /api/v1/Sales/SalesAgreementTypes
guid: 7E0ECC63-83B7-4604-893A-795B7B01112B
permission: Show agreement
introduced_in: '22.7'
property_count: 18
references_out:
- /entities/Common/PriceList.md
referenced_by:
- /entities/Sales/SalesAgreement.md
---

# SalesAgreementTypes

Represents an agreement type.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `SalesAgreementType`
- **Endpoint:** `GET /api/v1/Sales/SalesAgreementTypes`
- **Required permission:** Show agreement
- **GUID:** `7E0ECC63-83B7-4604-893A-795B7B01112B`
- **Introduced in:** 22.7

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the agreement type. |
| `PriceSetting` | `Int32` | no |  | enum | The price setting of the agreement type. |
| `PriceListId` | `Int64?` | yes | [PriceLists](/entities/Common/PriceList.md) |  | The business key identifier of the agreement types price list. |
| `Number` | `Int64` | no |  | unique | The number of the agreement type. |
| `Prefix` | `String` | no |  | max length 3 | The prefix of the agreement type. |
| `Description` | `String` | no |  |  | The translated description of the agreement type. |
| `Priority` | `Int32` | no |  |  | The priority of the agreement type. |
| `Visible` | `Boolean` | no |  |  | Indicates if the agreement type should be visible. |
| `IsPreset` | `Boolean` | no |  |  | Indicates if the agreement type is preset. |
| `CodingGroupId` | `Int64` | no |  |  | The business key identifier of the agreement types coding group. |
| `UpdateStatusAutomatically` | `Boolean` | no |  |  | Indicates if the status of the agreement should be updated automatically. |
| `InvoicingMethod` | `Int32` | no |  | enum | The invoicing method of the agreement type. |
| `PlannedInvoiceDateOffset` | `Int32` | no |  |  | The planned invoice date offset in days of the agreement type. |
| `ReleaseBasisAutomatically` | `Boolean` | no |  |  | Indicates if the agreement basis should be released automatically. |
| `UpwardAdjustmentTriggerType` | `Int32` | no |  | enum, since 25.8 | The trigger type for upward adjustments. |
| `UpwardAdjustmentTriggerValue` | `Int32` | no |  | since 25.8 | The trigger value for upward adjustments. |
| `AgreementValidFromSetting` | `Int32` | no |  | enum | The valid from setting of the agreement type. |
| `RateTypeSetting` | `Int32` | no |  | enum | The rate type setting of the agreement type. |

## Enumerations

### PriceSetting

| Name | Value |
| --- | ---: |
| `Customer` | 1 |
| `PriceList` | 2 |
| `StandardPrice` | 3 |

### InvoicingMethod

| Name | Value |
| --- | ---: |
| `InAdvance` | 1 |
| `InArrears` | 2 |

### UpwardAdjustmentTriggerType

| Name | Value |
| --- | ---: |
| `Always` | 1 |
| `Never` | 2 |
| `MinAmountForRow` | 3 |
| `MinAmountForAllRows` | 4 |
| `MinDaysToNextInvoice` | 5 |

### AgreementValidFromSetting

| Name | Value |
| --- | ---: |
| `Today` | 1 |
| `Empty` | 2 |

### RateTypeSetting

| Name | Value |
| --- | ---: |
| `Customer` | 1 |
| `OrderType` | 2 |


## Referenced by

**Sales**

- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `OrderTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "PriceSetting": 0,
  "PriceListId": null,
  "Number": 0,
  "Prefix": null,
  "Description": null,
  "Priority": 0,
  "Visible": false,
  "IsPreset": false,
  "CodingGroupId": 0,
  "UpdateStatusAutomatically": false,
  "InvoicingMethod": 0,
  "PlannedInvoiceDateOffset": 0,
  "ReleaseBasisAutomatically": false,
  "UpwardAdjustmentTriggerType": 0,
  "UpwardAdjustmentTriggerValue": 0,
  "AgreementValidFromSetting": 0,
  "RateTypeSetting": 0
}
```
