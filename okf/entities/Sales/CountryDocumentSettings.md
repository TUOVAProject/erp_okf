---
type: API Entity
title: CountryDocumentSettings
description: Represents a country document setting.
resource: https://api.monitor.se/api/Monitor.API.Sales.CountryDocumentSettings.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CountryDocumentSettings.html
  title: Monitor API — CountryDocumentSettings
module: Sales
api_class: CountryDocumentSettings
doc_name: CountryDocumentSettings
endpoint: GET /api/v1/Sales/CountryDocumentSettings
guid: 4a2c8077-1f23-4cd8-8c5a-4f70af4348fa
permission: Modify settings for file viewer
introduced_in: '26.3'
property_count: 16
references_out:
- /entities/Common/Country.md
---

# CountryDocumentSettings

Represents a country document setting.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CountryDocumentSettings`
- **Endpoint:** `GET /api/v1/Sales/CountryDocumentSettings`
- **Required permission:** Modify settings for file viewer
- **GUID:** `4a2c8077-1f23-4cd8-8c5a-4f70af4348fa`
- **Introduced in:** 26.3

## Notes

- Note the values in this entity can be overridden on each customer by CustomerCountryDocumentSettings .

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the country document setting. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the document setting. |
| `CountryId` | `Int64` | no | [Countries](../Common/Country.md) |  | The business key identifier of the document setting's country. |
| `ShowInSalesForm` | `Int32` | no |  | bitmask, enum | Specifies the document type this setting applies to. |
| `ShowCountryOfOrigin` | `Boolean` | no |  |  | Specifies if this setting should show country of origin. |
| `ShowNetWeight` | `Boolean` | no |  |  | Specifies if this setting should show net weight. |
| `ShowTradeClassificationName` | `Boolean` | no |  |  | Specifies if this setting should show trade classification name. |
| `ShowCN` | `Boolean` | no |  |  | Specifies if this setting should show CN. |
| `ShowHS` | `Boolean` | no |  |  | Specifies if this setting should show HS. |
| `ShowTaric` | `Boolean` | no |  |  | Specifies if this setting should show taric. |
| `ShowHTS` | `Boolean` | no |  |  | Specifies if this setting should show HTS. |
| `ShowNCM` | `Boolean` | no |  |  | Specifies if this setting should show NCM. |
| `ShowECCN` | `Boolean` | no |  |  | Specifies if this setting should show ECCN. |
| `ShowSITC` | `Boolean` | no |  |  | Specifies if this setting should show SITC. |
| `AmountExcludedDiscount` | `Boolean` | no |  |  | Specifies if this setting should show amount excluded discount. |
| `TotalByCombCode` | `Int32` | no |  | enum, since 26.6 | Specifies which classification code system drives the "Total by Comb. n. code" summary section on Pro forma and Comprehensive proforma invoices. Only meaningful when is . |

## Enumerations

### ShowInSalesForm (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Quote` | 1 |
| `Acknowledgement` | 2 |
| `DeliveryNote` | 4 |
| `Invoice` | 8 |
| `ProFormaInvoice` | 16 |

### TotalByCombCode

| Name | Value |
| --- | ---: |
| `CN` | 0 |
| `HS` | 1 |
| `Taric` | 2 |
| `HTS` | 3 |
| `NCM` | 4 |
| `ECCN` | 5 |
| `SITC` | 6 |


## Example

```json
{
  "Id": 0,
  "RowIndex": null,
  "CountryId": 0,
  "ShowInSalesForm": 0,
  "ShowCountryOfOrigin": false,
  "ShowNetWeight": false,
  "ShowTradeClassificationName": false,
  "ShowCN": false,
  "ShowHS": false,
  "ShowTaric": false,
  "ShowHTS": false,
  "ShowNCM": false,
  "ShowECCN": false,
  "ShowSITC": false,
  "AmountExcludedDiscount": false,
  "TotalByCombCode": 0
}
```
