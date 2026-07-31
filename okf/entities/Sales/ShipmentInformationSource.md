---
type: API Entity
title: ShipmentInformationSources
description: Represents a shipment information source.
resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentInformationSource.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.ShipmentInformationSource.html
  title: Monitor API — ShipmentInformationSource
module: Sales
api_class: ShipmentInformationSource
doc_name: ShipmentInformationSources
endpoint: GET /api/v1/Sales/ShipmentInformationSources
guid: 9CDD62AF-790E-41B2-B5A0-36A2E74FD5D9
permission: Show shipment
introduced_in: '23.1'
property_count: 9
references_out:
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
- /entities/Sales/CustomerOrder.md
- /entities/Sales/CustomerOrderInvoice.md
- /entities/Sales/SalesPickingList.md
- /entities/Sales/Shipment.md
referenced_by:
- /entities/Sales/ShipmentPackageInformation.md
---

# ShipmentInformationSources

Represents a shipment information source.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `ShipmentInformationSource`
- **Endpoint:** `GET /api/v1/Sales/ShipmentInformationSources`
- **Required permission:** Show shipment
- **GUID:** `9CDD62AF-790E-41B2-B5A0-36A2E74FD5D9`
- **Introduced in:** 23.1

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the shipment information source. |
| `ShipmentId` | `Int64?` | yes | [Shipments](/entities/Sales/Shipment.md) |  | The business key identifier of the shipment of the shipment information source. |
| `ShipmentInformationSourceType` | `Int32` | no |  | enum | The shipment information source type of the shipment information source. |
| `CustomerOrderId` | `Int64?` | yes | [CustomerOrders](/entities/Sales/CustomerOrder.md) |  | The business key identifier of the customer order of the shipment information source. |
| `PickingListId` | `Int64?` | yes | [SalesPickingLists](/entities/Sales/SalesPickingList.md) |  | The business key identifier of the picking list of the shipment information source. |
| `SupplierId` | `Int64?` | yes | [Suppliers](/entities/Purchase/Supplier.md) |  | The business key identifier of the supplier of the shipment information source. |
| `CustomerId` | `Int64?` | yes | [Customers](/entities/Sales/Customer.md) |  | The business key identifier of the customer of the shipment information source. |
| `CustomerOrderInvoiceId` | `Int64?` | yes | [CustomerOrderInvoices](/entities/Sales/CustomerOrderInvoice.md) |  | The business key identifier of the customer order shipment of the shipping information source. |
| `RowIndex` | `Int32` | no |  |  | The row index of the shipment information source. |

## Enumerations

### ShipmentInformationSourceType

| Name | Value |
| --- | ---: |
| `CustomerOrder` | 0 |
| `Supplier` | 1 |
| `PickingList` | 2 |
| `Customer` | 3 |
| `PickingListWithPackageStructure` | 4 |
| `Subcontract` | 5 |
| `ReturnOrder` | 6 |


## Referenced by

**Sales**

- [ShipmentPackageInformations](/entities/Sales/ShipmentPackageInformation.md) — `InformationSourceId` (FK)


## Example

```json
{
  "Id": 0,
  "ShipmentId": null,
  "ShipmentInformationSourceType": 0,
  "CustomerOrderId": null,
  "PickingListId": null,
  "SupplierId": null,
  "CustomerId": null,
  "CustomerOrderInvoiceId": null,
  "RowIndex": 0
}
```
