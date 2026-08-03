---
type: API Entity
title: AccountingBudgets
description: Represents an accounting budget.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingBudget.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingBudget.html
  title: Monitor API — AccountingBudget
module: Accounting
api_class: AccountingBudget
doc_name: AccountingBudgets
endpoint: GET /api/v1/Accounting/AccountingBudgets
guid: 646D760D-C81E-4B0A-90B1-6DD8C78F7B55
permission: Show budget
introduced_in: '23.3'
property_count: 9
references_out:
- /entities/Accounting/AccountYearSetting.md
- /entities/Accounting/AccountingBudgetPeriod.md
- /entities/Accounting/AccountingBudgetType.md
- /entities/Accounting/AccountingYear.md
- /entities/Accounting/Balance.md
- /entities/Accounting/BudgetChart.md
- /entities/Accounting/CodingEntry.md
referenced_by:
- /entities/Accounting/AccountingBudgetPeriod.md
---

# AccountingBudgets

Represents an accounting budget.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `AccountingBudget`
- **Endpoint:** `GET /api/v1/Accounting/AccountingBudgets`
- **Required permission:** Show budget
- **GUID:** `646D760D-C81E-4B0A-90B1-6DD8C78F7B55`
- **Introduced in:** 23.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the accounting budget. |
| `AccountYearSettingId` | `Int64` | no | [AccountYearSettings](AccountYearSetting.md) |  | The business key identifier of the account year setting the budget belongs to. |
| `AccountingYearId` | `Int64` | no | [AccountingYears](AccountingYear.md) |  | The business key identifier of the accounting year the budget belongs to. |
| `BalanceId` | `Int64` | no | [Balances](Balance.md) |  | The business key identifier of the budget's balance. |
| `BudgetChartId` | `Int64` | no | [BudgetCharts](BudgetChart.md) |  | The business key identifier of the budget's budget chart. |
| `BudgetTypeId` | `Int64` | no | [AccountingBudgetTypes](AccountingBudgetType.md) |  | The business key identifier of the budget type. |
| `CodingEntryId` | `Int64` | no | [CodingEntries](CodingEntry.md) |  | The business key identifier of the budget's coding entry. |
| `CodingEntry` | `CodingEntries` | no | [CodingEntries](CodingEntry.md) | expandable | The coding entry of the budget. |
| `Periods` | `AccountingBudgetPeriods[]` | no | [AccountingBudgetPeriods](AccountingBudgetPeriod.md) | expandable, collection | The periods of the accounting budget. |

## Referenced by

**Accounting**

- [AccountingBudgetPeriods](AccountingBudgetPeriod.md) — `BudgetId` (FK)


## Example

```json
{
  "Id": 0,
  "AccountYearSettingId": 0,
  "AccountingYearId": 0,
  "BalanceId": 0,
  "BudgetChartId": 0,
  "BudgetTypeId": 0,
  "CodingEntryId": 0,
  "CodingEntry": null,
  "Periods": null
}
```
