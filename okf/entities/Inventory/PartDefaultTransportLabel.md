---
type: API Entity
title: PartDefaultTransportLabels
description: Represents a part's default transport label.
resource: https://api.monitor.se/api/Monitor.API.Inventory.PartDefaultTransportLabel.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.PartDefaultTransportLabel.html
  title: Monitor API — PartDefaultTransportLabel
module: Inventory
api_class: PartDefaultTransportLabel
doc_name: PartDefaultTransportLabels
endpoint: GET /api/v1/Inventory/PartDefaultTransportLabels
guid: A41B7338-3805-4EBB-9FE9-80298B95542B
permission: Show part
introduced_in: '23.9'
property_count: 5
references_out:
- /entities/Common/FormReportConfiguration.md
- /entities/Inventory/Part.md
---

# PartDefaultTransportLabels

Represents a part's default transport label.

- **Module:** [Inventory](../../modules/Inventory.md)
- **API class:** `PartDefaultTransportLabel`
- **Endpoint:** `GET /api/v1/Inventory/PartDefaultTransportLabels`
- **Required permission:** Show part
- **GUID:** `A41B7338-3805-4EBB-9FE9-80298B95542B`
- **Introduced in:** 23.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the default transport label. |
| `PartId` | `Int64` | no | [Parts](Part.md) |  | The business key identifier of the part to which the transport label is set as default for. |
| `FormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](../Common/FormReportConfiguration.md) |  | The business key identifier of the transport label's form report configuration. |
| `Type` | `Int32` | no |  | enum | The transport label's type. |
| `FormReportTypeId` | `Guid` | no |  |  | The form report type id of the transport label. |

## Enumerations

### Type

| Name | Value |
| --- | ---: |
| `NodeToStock` | 0 |
| `Rejection` | 1 |
| `OperationInProgress` | 2 |
| `OperationBeforeReporting` | 3 |
| `Subcontract` | 4 |
| `SalesTransportLabel` | 5 |
| `PurchaseTransportLabel` | 6 |
| `PurchaseRejectionTransportLabel` | 7 |
| `PurchaseReturnOrderTransportLabel` | 8 |


## Example

```json
{
  "Id": 0,
  "PartId": 0,
  "FormReportConfigurationId": null,
  "Type": 0,
  "FormReportTypeId": "00000000-0000-0000-0000-000000000000"
}
```
