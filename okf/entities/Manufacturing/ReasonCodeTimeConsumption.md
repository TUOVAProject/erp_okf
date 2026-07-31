---
type: API Entity
title: ReasonCodeTimeConsumptions
description: Represents a reason code time consumption.
resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ReasonCodeTimeConsumption.html
tags:
- Manufacturing
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Manufacturing.ReasonCodeTimeConsumption.html
  title: Monitor API — ReasonCodeTimeConsumption
module: Manufacturing
api_class: ReasonCodeTimeConsumption
doc_name: ReasonCodeTimeConsumptions
endpoint: GET /api/v1/Manufacturing/ReasonCodeTimeConsumptions
guid: 33EE3DE1-AE93-4D55-9F47-EF7831CCA3E9
permission: Show cause codes
introduced_in: '24.9'
property_count: 6
referenced_by:
- /entities/Manufacturing/ManufacturingOrderOperationReporting.md
---

# ReasonCodeTimeConsumptions

Represents a reason code time consumption.

- **Module:** [Manufacturing](/modules/Manufacturing.md)
- **API class:** `ReasonCodeTimeConsumption`
- **Endpoint:** `GET /api/v1/Manufacturing/ReasonCodeTimeConsumptions`
- **Required permission:** Show cause codes
- **GUID:** `33EE3DE1-AE93-4D55-9F47-EF7831CCA3E9`
- **Introduced in:** 24.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the reason code time consumption. |
| `Code` | `String` | no |  | unique, max length 6 | The alphanumeric code of the reason code time consumption. |
| `Description` | `String` | no |  |  | The translated description of the reason code time consumption. |
| `CommentMandatory` | `Boolean` | no |  |  | Specifies if a comment is mandatory for the reason code time consumption. |
| `Active` | `Boolean` | no |  |  | Specifies if the reason code time consumption is active in the system. |
| `TimeConsumptionType` | `Int32` | no |  | enum | The type of the reason code time consumption. |

## Enumerations

### TimeConsumptionType

| Name | Value |
| --- | ---: |
| `TimeLoss` | 0 |
| `TimeGain` | 1 |


## Referenced by

**Manufacturing**

- [ManufacturingOrderOperationReportings](/entities/Manufacturing/ManufacturingOrderOperationReporting.md) — `ReasonCodeTimeConsumption` (expand)
- [ManufacturingOrderOperationReportings](/entities/Manufacturing/ManufacturingOrderOperationReporting.md) — `ReasonCodeTimeConsumptionId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "CommentMandatory": false,
  "Active": false,
  "TimeConsumptionType": 0
}
```
