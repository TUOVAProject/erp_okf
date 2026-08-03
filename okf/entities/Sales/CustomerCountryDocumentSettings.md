---
type: API Entity
title: CustomerCountryDocumentSettings
description: Represents a customer country document setting.
resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerCountryDocumentSettings.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.CustomerCountryDocumentSettings.html
  title: Monitor API — CustomerCountryDocumentSettings
module: Sales
api_class: CustomerCountryDocumentSettings
doc_name: CustomerCountryDocumentSettings
endpoint: GET /api/v1/Sales/CustomerCountryDocumentSettings
guid: 0eca2f98-1299-4c24-942c-859073e839a3
permission: Show customer
introduced_in: '26.3'
property_count: 17
references_out:
- /entities/Common/Country.md
- /entities/Sales/Customer.md
---

# CustomerCountryDocumentSettings

Represents a customer country document setting.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `CustomerCountryDocumentSettings`
- **Endpoint:** `GET /api/v1/Sales/CustomerCountryDocumentSettings`
- **Required permission:** Show customer
- **GUID:** `0eca2f98-1299-4c24-942c-859073e839a3`
- **Introduced in:** 26.3

## Notes

- Note if any setting is null or an entity for the customer, country and sales form is missing the corresponding entity in CountryDocumentSettings is used.

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the customer country document setting. |
| `RowIndex` | `Int32?` | yes |  |  | The row index of the document setting. |
| `CustomerId` | `Int64?` | yes | [Customers](Customer.md) |  | The business key identifier of the document setting's customer. |
| `CountryId` | `Int64` | no | [Countries](../Common/Country.md) |  | The business key identifier of the document setting's country. |
| `ShowInSalesForm` | `Int32` | no |  | bitmask, enum | Specifies the document type this setting applies to. |
| `ShowCountryOfOrigin` | `Boolean?` | yes |  |  | Specifies if this setting should show country of origin. |
| `ShowNetWeight` | `Boolean?` | yes |  |  | Specifies if this setting should show net weight. |
| `ShowTradeClassificationName` | `Boolean?` | yes |  |  | Specifies if this setting should show trade classification name. |
| `ShowCN` | `Boolean?` | yes |  |  | Specifies if this setting should show CN. |
| `ShowHS` | `Boolean?` | yes |  |  | Specifies if this setting should show HS. |
| `ShowTaric` | `Boolean?` | yes |  |  | Specifies if this setting should show taric. |
| `ShowHTS` | `Boolean?` | yes |  |  | Specifies if this setting should show HTS. |
| `ShowNCM` | `Boolean?` | yes |  |  | Specifies if this setting should show NCM. |
| `ShowECCN` | `Boolean?` | yes |  |  | Specifies if this setting should show ECCN. |
| `ShowSITC` | `Boolean?` | yes |  |  | Specifies if this setting should show SITC. |
| `AmountExcludedDiscount` | `Boolean?` | yes |  |  | Specifies if this setting should show amount excluded discount. |
| `TotalByCombCode` | `Int32?` | yes |  | enum, since 26.6 | Overrides the for this customer when set. Null means the country-level setting is used. Only meaningful when is . |

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
  "CustomerId": null,
  "CountryId": 0,
  "ShowInSalesForm": 0,
  "ShowCountryOfOrigin": null,
  "ShowNetWeight": null,
  "ShowTradeClassificationName": null,
  "ShowCN": null,
  "ShowHS": null,
  "ShowTaric": null,
  "ShowHTS": null,
  "ShowNCM": null,
  "ShowECCN": null,
  "ShowSITC": null,
  "AmountExcludedDiscount": null,
  "TotalByCombCode": null
}
```
