---
type: API Entity
title: PartPurchaseExpenseValues
description: Represents a part purchase expense values entity.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartPurchaseExpenseValues.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartPurchaseExpenseValues.html
  title: Monitor API — PartPurchaseExpenseValues
module: Inventory
api_class: PartPurchaseExpenseValues
doc_name: PartPurchaseExpenseValues
endpoint: GET /api/v1/Inventory/PartPurchaseExpenseValues
guid: 1e748c37-d10b-44e7-889b-da35ed77c464
permission: Show basic data for part
introduced_in: '2.48'
property_count: 44
referenced_by:
- /entities/Purchase/SupplierPartLink.md
---

# PartPurchaseExpenseValues

Represents a part purchase expense values entity.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `PartPurchaseExpenseValues`
- **Endpoint:** `GET /api/v1/Inventory/PartPurchaseExpenseValues`
- **Required permission:** Show basic data for part
- **GUID:** `1e748c37-d10b-44e7-889b-da35ed77c464`
- **Introduced in:** 2.48

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part purchase expense values. |
| `PartId` | `Int64` | no |  |  | The business key identifier of the part that part purchase expense values belongs to. |
| `Expense1PercentOfPriceValue` | `Decimal` | no |  |  | Expense1 (default name: Packaging) - percent of price. |
| `Expense1PerEachValue` | `Decimal` | no |  |  | Expense1 (default name: Packaging) - per each. |
| `Expense2PercentOfPriceValue` | `Decimal` | no |  |  | Expense2 (default name: Freight) - percent of price. |
| `Expense2PerEachValue` | `Decimal` | no |  |  | Expense2 (default name: Freight) - per each. |
| `Expense3PercentOfPriceValue` | `Decimal` | no |  |  | Expense3 (default name: Customs duty) - percent of price. |
| `Expense3PerEachValue` | `Decimal` | no |  |  | Expense3 (default name: Customs duty) - per each. |
| `CertificatePercentOfPriceValue` | `Decimal` | no |  |  | Certificate - percent of price. |
| `CertificatePerEachValue` | `Decimal` | no |  |  | Certificate - per each. |
| `CertificatePerKgValue` | `Decimal` | no |  |  | Certificate - per kg. |
| `CertificatePerPackageValue` | `Decimal` | no |  |  | Certificate - per package. |
| `CertificatePerOrderValue` | `Decimal` | no |  |  | Certificate - per order. |
| `CertificatePerQuantityValue` | `Decimal` | no |  |  | Certificate - per quantity. |
| `CertificateQuantityValue` | `Decimal` | no |  |  | Certificate - quantity. |
| `Expense1PerKgValue` | `Decimal` | no |  |  | Expense1 (default name: Packaging) - per kg. |
| `Expense1PerPackageValue` | `Decimal` | no |  |  | Expense1 (default name: Packaging) - per package. |
| `Expense1PerOrderValue` | `Decimal` | no |  |  | Expense1 (default name: Packaging) - per order. |
| `Expense1PerQuantityValue` | `Decimal` | no |  |  | Expense1 (default name: Packaging) - per quantity. |
| `Expense1QuantityValue` | `Decimal` | no |  |  | Expense1 (default name: Packaging) - quantity. |
| `Expense2PerKgValue` | `Decimal` | no |  |  | Expense2 (default name: Freight) - per kg. |
| `Expense2PerPackageValue` | `Decimal` | no |  |  | Expense2 (default name: Freight) - per package. |
| `Expense2PerOrderValue` | `Decimal` | no |  |  | Expense2 (default name: Freight) - per order. |
| `Expense2PerQuantityValue` | `Decimal` | no |  |  | Expense2 (default name: Freight) - per quantity. |
| `Expense2QuantityValue` | `Decimal` | no |  |  | Expense2 (default name: Freight) - quantity. |
| `Expense3PerKgValue` | `Decimal` | no |  |  | Expense3 (default name: Customs duty) - per kg. |
| `Expense3PerPackageValue` | `Decimal` | no |  |  | Expense3 (default name: Customs duty) - per package. |
| `Expense3PerOrderValue` | `Decimal` | no |  |  | Expense3 (default name: Customs duty) - per order. |
| `Expense3PerQuantityValue` | `Decimal` | no |  |  | Expense3 (default name: Customs duty) - per quantity. |
| `Expense3QuantityValue` | `Decimal` | no |  |  | Expense3 (default name: Customs duty) - quantity. |
| `Expense4PercentOfPriceValue` | `Decimal` | no |  |  | Expense4 (default name: Tooling) - percent of price. |
| `Expense4PerEachValue` | `Decimal` | no |  |  | Expense4 (default name: Tooling) - per each. |
| `Expense4PerKgValue` | `Decimal` | no |  |  | Expense4 (default name: Tooling) - per kg. |
| `Expense4PerPackageValue` | `Decimal` | no |  |  | Expense4 (default name: Tooling) - per package. |
| `Expense4PerOrderValue` | `Decimal` | no |  |  | Expense4 (default name: Tooling) - per order. |
| `Expense4PerQuantityValue` | `Decimal` | no |  |  | Expense4 (default name: Tooling) - per quantity. |
| `Expense4QuantityValue` | `Decimal` | no |  |  | Expense4 (default name: Tooling) - quantity. |
| `Expense5PercentOfPriceValue` | `Decimal` | no |  |  | Expense5 (default name: Other) - percent of price. |
| `Expense5PerEachValue` | `Decimal` | no |  |  | Expense5 (default name: Other) - per each. |
| `Expense5PerKgValue` | `Decimal` | no |  |  | Expense5 (default name: Other) - per kg. |
| `Expense5PerPackageValue` | `Decimal` | no |  |  | Expense5 (default name: Other) - per package. |
| `Expense5PerOrderValue` | `Decimal` | no |  |  | Expense5 (default name: Other) - per order. |
| `Expense5PerQuantityValue` | `Decimal` | no |  |  | Expense5 (default name: Other) - per quantity. |
| `Expense5QuantityValue` | `Decimal` | no |  |  | Expense5 (default name: Other) - quantity. |

## Referenced by

**Purchase**

- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `PartPurchaseExpenseValues` (expand)
- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `PartPurchaseExpenseValuesId` (FK)


## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "Expense1PercentOfPriceValue": 0.0,
  "Expense1PerEachValue": 0.0,
  "Expense2PercentOfPriceValue": 0.0,
  "Expense2PerEachValue": 0.0,
  "Expense3PercentOfPriceValue": 0.0,
  "Expense3PerEachValue": 0.0,
  "CertificatePercentOfPriceValue": 0.0,
  "CertificatePerEachValue": 0.0,
  "CertificatePerKgValue": 0.0,
  "CertificatePerPackageValue": 0.0,
  "CertificatePerOrderValue": 0.0,
  "CertificatePerQuantityValue": 0.0,
  "CertificateQuantityValue": 0.0,
  "Expense1PerKgValue": 0.0,
  "Expense1PerPackageValue": 0.0,
  "Expense1PerOrderValue": 0.0,
  "Expense1PerQuantityValue": 0.0,
  "Expense1QuantityValue": 0.0,
  "Expense2PerKgValue": 0.0,
  "Expense2PerPackageValue": 0.0,
  "Expense2PerOrderValue": 0.0,
  "Expense2PerQuantityValue": 0.0,
  "Expense2QuantityValue": 0.0,
  "Expense3PerKgValue": 0.0,
  "Expense3PerPackageValue": 0.0,
  "Expense3PerOrderValue": 0.0,
  "Expense3PerQuantityValue": 0.0,
  "Expense3QuantityValue": 0.0,
  "Expense4PercentOfPriceValue": 0.0,
  "Expense4PerEachValue": 0.0,
  "Expense4PerKgValue": 0.0,
  "Expense4PerPackageValue": 0.0,
  "Expense4PerOrderValue": 0.0,
  "Expense4PerQuantityValue": 0.0,
  "Expense4QuantityValue": 0.0,
  "Expense5PercentOfPriceValue": 0.0,
  "Expense5PerEachValue": 0.0,
  "Expense5PerKgValue": 0.0,
  "Expense5PerPackageValue": 0.0,
  "Expense5PerOrderValue": 0.0,
  "Expense5PerQuantityValue": 0.0,
  "Expense5QuantityValue": 0.0
}
```
