---
type: API Entity
title: FixedAssets
description: Represents a fixed assets object.
resource: https://api.monitor.se/api/Monitor.API.Accounting.FixedAsset.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.FixedAsset.html
  title: Monitor API — FixedAsset
module: Accounting
api_class: FixedAsset
doc_name: FixedAssets
endpoint: GET /api/v1/Accounting/FixedAssets
guid: 74cf08b4-ffd9-46eb-aef6-f4a6a10f692d
permission: Show fixed assets objects
introduced_in: '23.5'
property_count: 23
references_out:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/FixedAssetGroup.md
- /entities/Accounting/FixedAssetSale.md
- /entities/Accounting/Voucher.md
- /entities/Common/Department.md
- /entities/Manufacturing/WorkCenter.md
- /entities/Purchase/Supplier.md
referenced_by:
- /entities/Accounting/FixedAssetDepreciation.md
- /entities/Sales/CustomerOrderRow.md
---

# FixedAssets

Represents a fixed assets object.

- **Module:** [Accounting](../../modules/Accounting.md)
- **API class:** `FixedAsset`
- **Endpoint:** `GET /api/v1/Accounting/FixedAssets`
- **Required permission:** Show fixed assets objects
- **GUID:** `74cf08b4-ffd9-46eb-aef6-f4a6a10f692d`
- **Introduced in:** 23.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the fixed assets object. |
| `Code` | `String` | no |  | unique, max length 16 | The human readable identifier of the fixed assets object. |
| `Description` | `String` | no |  | max length 400 | The translated description of the fixed assets object. |
| `GroupId` | `Int64` | no | [FixedAssetGroups](FixedAssetGroup.md) |  | The business key identifier of fixed assets group that the fixed assets object belongs to. |
| `Group` | `FixedAssetGroups` | no | [FixedAssetGroups](FixedAssetGroup.md) | expandable | The fixed assets group that the fixed assets object belongs to. |
| `AcquisitionDate` | `DateTimeOffset` | no |  |  | The acquisition date of the fixed assets object. |
| `AcquisitionValue` | `Decimal` | no |  |  | The acquisition value in company currency of the fixed assets object. |
| `Quantity` | `Decimal` | no |  |  | The quantity of the fixed assets object. |
| `AccountsPayableId` | `Int64?` | yes | [AccountsPayables](AccountsPayable.md) |  | The business key identifier of the accounts payable connected to the fixed assets object. |
| `VoucherId` | `Int64?` | yes | [Vouchers](Voucher.md) |  | The business key identifier of the voucher connected to the fixed assets object. |
| `SupplierId` | `Int64?` | yes | [Suppliers](../Purchase/Supplier.md) |  | The business key identifier of the supplier connected to the fixed assets object. |
| `CategoryString` | `String` | no |  | max length 20 | The category string of the fixed assets object. |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](../Manufacturing/WorkCenter.md) |  | The business key identifier of the work center of the fixed assets object. |
| `DepartmentId` | `Int64?` | yes | [Departments](../Common/Department.md) |  | The business key identifier of the department of the fixed assets object. |
| `SerialNumber` | `String` | no |  | max length 26 | The serial number of the fixed assets object. |
| `Location` | `String` | no |  | max length 255 | The location of the fixed assets object. |
| `PlannedDepreciationStartDate` | `DateTimeOffset` | no |  |  | The start date for the scheduled depreciation of the fixed assets object. |
| `PlannedDepreciationTimeInYears` | `Decimal` | no |  |  | The time (in years) for the scheduled depreciation of the fixed assets object. |
| `PlannedDepreciationPercentage` | `Decimal` | no |  |  | The percentage for the scheduled depreciation of the fixed assets object. |
| `CalculatedDepreciationStartDate` | `DateTimeOffset` | no |  |  | The start date for the calculated depreciation of the fixed assets object. |
| `CalculatedDepreciationPercentage` | `Decimal` | no |  |  | The depreciation percentage for the calculated depreciation of the fixed assets object. |
| `MinimumValue` | `Decimal` | no |  |  | The minimal value to depreciate the fixed assets object to. |
| `Sales` | `FixedAssetSales[]` | no | [FixedAssetSales](FixedAssetSale.md) | expandable, collection, since 23.8 | The registered sales/retirements of the fixed assets object. |

## Referenced by

**Accounting**

- [FixedAssetDepreciations](FixedAssetDepreciation.md) — `ParentId` (FK)

**Sales**

- [CustomerOrderRows](../Sales/CustomerOrderRow.md) — `FixedAssetId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "GroupId": 0,
  "Group": null,
  "AcquisitionDate": "0001-01-01T00:00:00+00:00",
  "AcquisitionValue": 0.0,
  "Quantity": 0.0,
  "AccountsPayableId": null,
  "VoucherId": null,
  "SupplierId": null,
  "CategoryString": null,
  "WorkCenterId": null,
  "DepartmentId": null,
  "SerialNumber": null,
  "Location": null,
  "PlannedDepreciationStartDate": "0001-01-01T00:00:00+00:00",
  "PlannedDepreciationTimeInYears": 0.0,
  "PlannedDepreciationPercentage": 0.0,
  "CalculatedDepreciationStartDate": "0001-01-01T00:00:00+00:00",
  "CalculatedDepreciationPercentage": 0.0,
  "MinimumValue": 0.0,
  "Sales": null
}
```
