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

- **Module:** [Common](/modules/Common.md)
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

- [CompanyEmissionDetails](/entities/Common/CompanyEmissionDetail.md) — `Unit` (expand)
- [FormTemplateRows](/entities/Common/FormTemplateRow.md) — `UnitId` (FK)
- [PartUnitUsages](/entities/Common/PartUnitUsage.md) — `UnitId` (FK)

**Inventory**

- [Alloys](/entities/Inventory/Alloy.md) — `UnitId` (FK)
- [Parts](/entities/Inventory/Part.md) — `StandardUnitId` (FK)
- [SalesForecastRows](/entities/Inventory/SalesForecastRow.md) — `UnitId` (FK)

**Manufacturing**

- [MaintenanceReportingRows](/entities/Manufacturing/MaintenanceReportingRow.md) — `UnitId` (FK)

**Purchase**

- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `Unit` (expand)
- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `UnitId` (FK)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `Unit` (expand)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `UnitId` (FK)
- [PurchaseOrderAdviceRows](/entities/Purchase/PurchaseOrderAdviceRow.md) — `UnitId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `Unit` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `UnitId` (FK)
- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `Unit` (expand)
- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `UnitId` (FK)

**Sales**

- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `Unit` (expand)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `UnitId` (FK)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `Unit` (expand)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `Unit` (expand)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `UnitId` (FK)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `Unit` (expand)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `UnitId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `Unit` (expand)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `UnitId` (FK)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `Unit` (expand)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `UnitId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `Unit` (expand)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `UnitId` (FK)
- [ShipmentCustomsRows](/entities/Sales/ShipmentCustomsRow.md) — `OtherUnit` (expand)
- [ShipmentCustomsRows](/entities/Sales/ShipmentCustomsRow.md) — `OtherUnitId` (FK)
- [ShipmentCustomsRows](/entities/Sales/ShipmentCustomsRow.md) — `Unit` (expand)
- [ShipmentCustomsRows](/entities/Sales/ShipmentCustomsRow.md) — `UnitId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "Number": 0
}
```
