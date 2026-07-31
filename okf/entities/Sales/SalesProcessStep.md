---
type: API Entity
title: SalesProcessSteps
description: Represents a sales process step.
resource: https://api.monitor.se/api/Monitor.API.Sales.SalesProcessStep.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.SalesProcessStep.html
  title: Monitor API — SalesProcessStep
module: Sales
api_class: SalesProcessStep
doc_name: SalesProcessSteps
endpoint: GET /api/v1/Sales/SalesProcessSteps
guid: 25130296-198e-49d9-91bb-74541450a8af
permission: Show business opportunity
introduced_in: '25.9'
property_count: 5
referenced_by:
- /entities/Sales/SalesProcessTemplateRow.md
---

# SalesProcessSteps

Represents a sales process step.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `SalesProcessStep`
- **Endpoint:** `GET /api/v1/Sales/SalesProcessSteps`
- **Required permission:** Show business opportunity
- **GUID:** `25130296-198e-49d9-91bb-74541450a8af`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the sales process step. |
| `Code` | `Int64` | no |  | unique | The human readable identifier of the sales process step. |
| `Step` | `String` | no |  | max length 10 | The name of the sales process step. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the sales process step is active. |
| `Description` | `String` | no |  | max length 400 | The translated description of the sales process step. |

## Referenced by

**Sales**

- [SalesProcessTemplateRows](/entities/Sales/SalesProcessTemplateRow.md) — `SalesProcessStep` (expand)
- [SalesProcessTemplateRows](/entities/Sales/SalesProcessTemplateRow.md) — `SalesProcessStepId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": 0,
  "Step": null,
  "IsActive": false,
  "Description": null
}
```
