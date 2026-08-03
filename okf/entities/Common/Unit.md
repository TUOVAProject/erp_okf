---
type: API Entity
title: Units
description: Represents a quantity unit.
resource: https://api.monitor.se/api/Monitor.API.Common.Unit.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Unit.html
  title: Monitor API — Unit
module: Common
api_class: Unit
doc_name: Units
endpoint: GET /api/v1/Common/Units
guid: c666b903-0599-4082-b7f2-2cffa4d7ea82
permission: Show units
introduced_in: '2.18'
property_count: 4
referenced_by:
- /entities/Common/CompanyEmissionDetail.md
- /entities/Common/FormTemplateRow.md
- /entities/Common/PartUnitUsage.md
- /entities/Inventory/Alloy.md
- /entities/Inventory/Part.md
- /entities/Inventory/SalesForecastRow.md
- /entities/Manufacturing/MaintenanceReportingRow.md
- /entities/Purchase/BlanketOrderPurchaseRow.md
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/PurchaseOrderAdviceRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Purchase/SupplierPartLink.md
- /entities/Sales/BlanketOrderSalesRow.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/CustomerOrderRowInflow.md
- /entities/Sales/CustomerPartLink.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/SalesAgreementBasisRow.md
- /entities/Sales/SalesAgreementRow.md
- /entities/Sales/ShipmentCustomsRow.md
---

# Units

Represents a quantity unit.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `Unit`
- **Endpoint:** `GET /api/v1/Common/Units`
- **Required permission:** Show units
- **GUID:** `c666b903-0599-4082-b7f2-2cffa4d7ea82`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the unit. |
| `Code` | `String` | no |  |  | The translatable code of the unit. |
| `Description` | `String` | no |  |  | The translated description of the unit. |
| `Number` | `Int64` | no |  |  | The unit number. |

## Referenced by

**Common**

- [CompanyEmissionDetails](CompanyEmissionDetail.md) — `Unit` (expand)
- [FormTemplateRows](FormTemplateRow.md) — `UnitId` (FK)
- [PartUnitUsages](PartUnitUsage.md) — `UnitId` (FK)

**Inventory**

- [Alloys](../Inventory/Alloy.md) — `UnitId` (FK)
- [Parts](../Inventory/Part.md) — `StandardUnitId` (FK)
- [SalesForecastRows](../Inventory/SalesForecastRow.md) — `UnitId` (FK)

**Manufacturing**

- [MaintenanceReportingRows](../Manufacturing/MaintenanceReportingRow.md) — `UnitId` (FK)

**Purchase**

- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `Unit` (expand)
- [BlanketOrderPurchaseRows](../Purchase/BlanketOrderPurchaseRow.md) — `UnitId` (FK)
- [InquiryRows](../Purchase/InquiryRow.md) — `Unit` (expand)
- [InquiryRows](../Purchase/InquiryRow.md) — `UnitId` (FK)
- [PurchaseOrderAdviceRows](../Purchase/PurchaseOrderAdviceRow.md) — `UnitId` (FK)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `Unit` (expand)
- [PurchaseOrderRows](../Purchase/PurchaseOrderRow.md) — `UnitId` (FK)
- [SupplierPartLinks](../Purchase/SupplierPartLink.md) — `Unit` (expand)
- [SupplierPartLinks](../Purchase/SupplierPartLink.md) — `UnitId` (FK)

**Sales**

- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `Unit` (expand)
- [BlanketOrderSalesRows](../Sales/BlanketOrderSalesRow.md) — `UnitId` (FK)
- [CustomerOrderRowInflows](../Sales/CustomerOrderRowInflow.md) — `Unit` (expand)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `Unit` (expand)
- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `UnitId` (FK)
- [CustomerPartLinks](../Sales/CustomerPartLink.md) — `Unit` (expand)
- [CustomerPartLinks](../Sales/CustomerPartLink.md) — `UnitId` (FK)
- [QuoteRows](../Sales/QuoteRow.md) — `Unit` (expand)
- [QuoteRows](../Sales/QuoteRow.md) — `UnitId` (FK)
- [SalesAgreementBasisRows](../Sales/SalesAgreementBasisRow.md) — `Unit` (expand)
- [SalesAgreementBasisRows](../Sales/SalesAgreementBasisRow.md) — `UnitId` (FK)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `Unit` (expand)
- [SalesAgreementRows](../Sales/SalesAgreementRow.md) — `UnitId` (FK)
- [ShipmentCustomsRows](../Sales/ShipmentCustomsRow.md) — `OtherUnit` (expand)
- [ShipmentCustomsRows](../Sales/ShipmentCustomsRow.md) — `OtherUnitId` (FK)
- [ShipmentCustomsRows](../Sales/ShipmentCustomsRow.md) — `Unit` (expand)
- [ShipmentCustomsRows](../Sales/ShipmentCustomsRow.md) — `UnitId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "Number": 0
}
```
