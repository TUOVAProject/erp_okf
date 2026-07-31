---
type: API Entity
title: BudgetCharts
description: Represents a budget chart.
resource: https://api.monitor.se/api/Monitor.API.Accounting.BudgetChart.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.BudgetChart.html
  title: Monitor API — BudgetChart
module: Accounting
api_class: BudgetChart
doc_name: BudgetCharts
endpoint: GET /api/v1/Accounting/BudgetCharts
guid: 01461CE9-0880-45A9-9771-CAFEC549B2F4
permission: Show basic data for budget
introduced_in: '23.3'
property_count: 3
referenced_by:
- /entities/Accounting/AccountingBudget.md
---

# BudgetCharts

Represents a budget chart.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `BudgetChart`
- **Endpoint:** `GET /api/v1/Accounting/BudgetCharts`
- **Required permission:** Show basic data for budget
- **GUID:** `01461CE9-0880-45A9-9771-CAFEC549B2F4`
- **Introduced in:** 23.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the budget chart. |
| `Code` | `String` | no |  | unique, max length 3 | The human readable identifier of the budget chart. |
| `Description` | `String` | no |  |  | The translated description of the budget chart. |

## Referenced by

**Accounting**

- [AccountingBudgets](/entities/Accounting/AccountingBudget.md) — `BudgetChartId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null
}
```
