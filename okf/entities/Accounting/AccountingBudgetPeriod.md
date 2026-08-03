---
type: API Entity
title: AccountingBudgetPeriods
description: Represents an accounting budget period.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingBudgetPeriod.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingBudgetPeriod.html
  title: Monitor API — AccountingBudgetPeriod
module: Accounting
api_class: AccountingBudgetPeriod
doc_name: AccountingBudgetPeriods
endpoint: GET /api/v1/Accounting/AccountingBudgetPeriods
guid: 61A641D7-0937-42A1-8B54-FECDB3630D4C
permission: Show budget
introduced_in: '23.3'
property_count: 5
references_out:
- /entities/Accounting/AccountingBudget.md
- /entities/Accounting/AccountingYearPeriod.md
referenced_by:
- /entities/Accounting/AccountingBudget.md
---

# AccountingBudgetPeriods

Represents an accounting budget period.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `AccountingBudgetPeriod`
- **Endpoint:** `GET /api/v1/Accounting/AccountingBudgetPeriods`
- **Required permission:** Show budget
- **GUID:** `61A641D7-0937-42A1-8B54-FECDB3630D4C`
- **Introduced in:** 23.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the accounting budget period. |
| `BudgetId` | `Int64` | no | [AccountingBudgets](AccountingBudget.md) |  | The business key identifier of the budget the accounting budget period belongs to. |
| `PeriodId` | `Int64` | no | [AccountingYearPeriods](AccountingYearPeriod.md) |  | The business key identifier of the period the accounting budget period belongs to. |
| `Amount` | `Decimal` | no |  |  | The amount of the accounting budget period. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the accounting budget period. |

## Referenced by

**Accounting**

- [AccountingBudgets](AccountingBudget.md) — `Periods` (expand)


## Example

```json
{
  "Id": 0,
  "BudgetId": 0,
  "PeriodId": 0,
  "Amount": 0.0,
  "Quantity": 0.0
}
```
