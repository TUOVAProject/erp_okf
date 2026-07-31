---
type: API Entity
title: Projects
description: Represents a project.
resource: https://api.monitor.se/api/Monitor.API.Common.Project.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Project.html
  title: Monitor API — Project
module: Common
api_class: Project
doc_name: Projects
endpoint: GET /api/v1/Common/Projects
guid: 1A7530E0-9336-488A-9C01-DD6240AC01A7
permission: Show projects
introduced_in: '2.31'
property_count: 33
references_out:
- /entities/Common/BusinessContactReference.md
- /entities/Common/Comment.md
- /entities/Common/ExtraField.md
- /entities/Common/Person.md
- /entities/Common/Project.md
- /entities/Common/ProjectAggregate.md
- /entities/Common/ProjectCostBudget.md
- /entities/Common/ProjectCostForecast.md
- /entities/Common/ProjectGroup.md
- /entities/Common/ProjectPhase.md
- /entities/Common/ProjectType.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
referenced_by:
- /entities/Common/Project.md
- /entities/Common/ProjectAggregate.md
- /entities/Common/ProjectCostBudget.md
- /entities/Common/ProjectCostForecast.md
- /entities/Common/ProjectPhase.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/Part.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Purchase/Inquiry.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/SalesAgreement.md
- /entities/TimeRecording/AdditionRecording.md
---

# Projects

Represents a project.

- **Module:** [Common](/modules/Common.md)
- **API class:** `Project`
- **Endpoint:** `GET /api/v1/Common/Projects`
- **Required permission:** Show projects
- **GUID:** `1A7530E0-9336-488A-9C01-DD6240AC01A7`
- **Introduced in:** 2.31

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the project. |
| `Code` | `String` | no |  |  | The human readable code of the project. |
| `Description` | `String` | no |  |  | The translated description of the project. |
| `Status` | `Int32` | no |  | enum | The status of the project. |
| `Priority` | `Int32` | no |  |  | The priority of the project. |
| `StartDate` | `DateTimeOffset` | no |  |  | The start date of the project. |
| `EndDate` | `DateTimeOffset` | no |  |  | The end date of the project. |
| `CustomerId` | `Int64?` | yes | [Customers](/entities/Sales/Customer.md) |  | The business key identifier of the customer that the project belongs to. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](/entities/Sales/CustomerOrder.md) | since 2.36 | The business key identifier of the project's customer order. |
| `CustomerOrder` | `CustomerOrders` | no | [CustomerOrders](/entities/Sales/CustomerOrder.md) | expandable, since 2.36 | The customer order of the project. |
| `CustomerOrderNumber` | `String` | no |  | since 2.36 | The customer's order number of the project. |
| `SellerId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) | since 2.36 | The business key identifier of the project's seller. |
| `Seller` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable, since 2.36 | The seller of the project. |
| `OurReferenceId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) | since 2.36 | The business key identifier of the project's our reference. |
| `OurReference` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable, since 2.36 | Our reference of the project. |
| `CustomerReferenceId` | `Int64?` | yes | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) | since 2.36 | The business key identifier of the project's customer reference. |
| `CustomerReference` | `BusinessContactReferences` | no | [BusinessContactReferences](/entities/Common/BusinessContactReference.md) | expandable, since 2.36 | The customer's reference of the project. |
| `InternalCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) | since 2.36 | The business key identifier of the project's internal comment. |
| `InternalComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable, since 2.36 | The internal comment of the project |
| `ExternalCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) | since 2.36 | The business key identifier of the project's external comment. |
| `ExternalComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable, since 2.36 | The external comment of the project. |
| `LongDescription` | `String` | no |  | max length 500, since 2.36 | The long description of the project. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](/entities/Common/ExtraField.md) | expandable, collection, since 2.36 | A collection of extra field values for the project. |
| `Phases` | `ProjectPhases[]` | no | [ProjectPhases](/entities/Common/ProjectPhase.md) | expandable, collection, since 2.36 | The phases of the project. |
| `ProjectTypeId` | `Int64` | no | [ProjectTypes](/entities/Common/ProjectType.md) | since 2.43 | The business key identifier of the project's type. |
| `ProjectType` | `ProjectTypes` | no | [ProjectTypes](/entities/Common/ProjectType.md) | expandable, since 2.43 | The project type. |
| `ProjectGroupId` | `Int64?` | yes | [ProjectGroups](/entities/Common/ProjectGroup.md) | since 2.43 | The business key identifier of the project's group. |
| `ProjectGroup` | `ProjectGroups` | no | [ProjectGroups](/entities/Common/ProjectGroup.md) | expandable, since 24.6 | The project group of the project. |
| `ProjectCostBudgets` | `ProjectCostBudgets[]` | no | [ProjectCostBudgets](/entities/Common/ProjectCostBudget.md) | expandable, collection, since 2.46 | The project cost budgets of the project. |
| `ProjectCostForecasts` | `ProjectCostForecasts[]` | no | [ProjectCostForecasts](/entities/Common/ProjectCostForecast.md) | expandable, collection, since 2.46 | The project cost forecasts of the project. |
| `ProjectAggregates` | `ProjectAggregates[]` | no | [ProjectAggregates](/entities/Common/ProjectAggregate.md) | expandable, collection, since 2.46 | The project aggregates of the project. |
| `ParentProjectId` | `Int64?` | yes | [Projects](/entities/Common/Project.md) | since 22.3 | The business key identifier of the parent project to the project. |
| `ProjectManagerId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) | since 23.4 | The business key identifier of the manager for the project. |

## Enumerations

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `InProgress` | 3 |
| `Finished` | 4 |
| `Standby` | 6 |
| `History` | 9 |


## Referenced by

**Common**

- [ProjectAggregates](/entities/Common/ProjectAggregate.md) — `ProjectId` (FK)
- [ProjectCostBudgets](/entities/Common/ProjectCostBudget.md) — `ProjectId` (FK)
- [ProjectCostForecasts](/entities/Common/ProjectCostForecast.md) — `ProjectId` (FK)
- [ProjectPhases](/entities/Common/ProjectPhase.md) — `ParentId` (FK)
- [Projects](/entities/Common/Project.md) — `ParentProjectId` (FK)

**Inventory**

- [CaseEntry](/entities/Inventory/CaseEntry.md) — `Project` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ProjectId` (FK)
- [Parts](/entities/Inventory/Part.md) — `ProjectId` (FK)

**Manufacturing**

- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `Project` (expand)
- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `ProjectId` (FK)

**Purchase**

- [Inquiries](/entities/Purchase/Inquiry.md) — `ProjectId` (FK)

**Sales**

- [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) — `ProjectId` (FK)
- [SalesAgreements](/entities/Sales/SalesAgreement.md) — `ProjectId` (FK)

**TimeRecording**

- [AdditionRecordings](/entities/TimeRecording/AdditionRecording.md) — `ProjectId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "Status": 0,
  "Priority": 0,
  "StartDate": "0001-01-01T00:00:00+00:00",
  "EndDate": "0001-01-01T00:00:00+00:00",
  "CustomerId": null,
  "CustomerOrderId": null,
  "CustomerOrder": null,
  "CustomerOrderNumber": null,
  "SellerId": null,
  "Seller": null,
  "OurReferenceId": null,
  "OurReference": null,
  "CustomerReferenceId": null,
  "CustomerReference": null,
  "InternalCommentId": null,
  "InternalComment": null,
  "ExternalCommentId": null,
  "ExternalComment": null,
  "LongDescription": null,
  "ExtraFields": null,
  "Phases": null,
  "ProjectTypeId": 0,
  "ProjectType": null,
  "ProjectGroupId": null,
  "ProjectGroup": null,
  "ProjectCostBudgets": null,
  "ProjectCostForecasts": null,
  "ProjectAggregates": null,
  "ParentProjectId": null,
  "ProjectManagerId": null
}
```
