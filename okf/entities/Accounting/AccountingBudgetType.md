---
type: API Entity
title: AccountingBudgetTypes
description: Represents an accounting budget type.
resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingBudgetType.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.AccountingBudgetType.html
  title: Monitor API — AccountingBudgetType
module: Accounting
api_class: AccountingBudgetType
doc_name: AccountingBudgetTypes
endpoint: GET /api/v1/Accounting/AccountingBudgetTypes
guid: 59F1175E-CE81-4EC0-954D-C6745B141E00
permission: Show basic data for budget
introduced_in: '23.3'
property_count: 4
referenced_by:
- /entities/Accounting/AccountingBudget.md
---

# AccountingBudgetTypes

Represents an accounting budget type.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `AccountingBudgetType`
- **Endpoint:** `GET /api/v1/Accounting/AccountingBudgetTypes`
- **Required permission:** Show basic data for budget
- **GUID:** `59F1175E-CE81-4EC0-954D-C6745B141E00`
- **Introduced in:** 23.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the accounting budget type. |
| `Number` | `Int64` | no |  | unique | The human readable identifier of the accounting budget type. |
| `Description` | `String` | no |  |  | The translated description of the accounting budget type. |
| `IsActive` | `Boolean` | no |  |  | Whether or not the accounting budget type is active. |

## Referenced by

**Accounting**

- [AccountingBudgets](AccountingBudget.md) — `BudgetTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "IsActive": false
}
```
