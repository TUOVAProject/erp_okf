---
type: API Entity
title: Companies
description: Represents a company in the MONITOR system.
resource: https://api.monitor.se/api/Monitor.API.Common.Company.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Company.html
  title: Monitor API — Company
module: Common
api_class: Company
doc_name: Companies
endpoint: GET /api/v1/Common/Companies
guid: 8C9373B7-7F59-4F91-A8D3-15852B2CADFB
permission: Show company information
introduced_in: '24.3'
property_count: 11
references_out:
- /entities/Common/BlobData.md
- /entities/Common/Currency.md
- /entities/Common/LanguageCode.md
- /entities/Common/Warehouse.md
referenced_by:
- /entities/Common/Warehouse.md
---

# Companies

Represents a company in the MONITOR system.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `Company`
- **Endpoint:** `GET /api/v1/Common/Companies`
- **Required permission:** Show company information
- **GUID:** `8C9373B7-7F59-4F91-A8D3-15852B2CADFB`
- **Introduced in:** 24.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the company. |
| `Name` | `String` | no |  |  | The name of the company. |
| `ImageId` | `Int64?` | yes |  |  | The business key identifier for the image of the company. |
| `Image` | `BlobData` | no | [BlobData](BlobData.md) | expandable | The image blob of the company. |
| `CurrencyId` | `Int64` | no | [Currencies](Currency.md) |  | The business key identifier for the currency of the company. |
| `Currency` | `Currencies` | no | [Currencies](Currency.md) | expandable | The company currency. |
| `LanguageId` | `Int64` | no | [LanguageCodes](LanguageCode.md) |  | The business key identifier of the language. |
| `Language` | `LanguageCodes` | no | [LanguageCodes](LanguageCode.md) | expandable | The language of the company. |
| `Warehouses` | `Warehouses[]` | no | [Warehouses](Warehouse.md) | expandable, collection | The warehouses that belong to the company. |
| `TimeZone` | `String` | no |  | since 25.2 | The time zone of the company. Specified as a time zone identifier. Identifier depends on underlying database engine, and could be in either IANA or Windows style. |
| `CorporationIdentificationNumber` | `String` | no |  | max length 25, since 25.4 | The corporation identification number of the company. |

## Referenced by

**Common**

- [Warehouses](Warehouse.md) — `TimeZoneId` (FK)


## Example

```json
{
  "Id": 0,
  "Name": null,
  "ImageId": null,
  "Image": null,
  "CurrencyId": 0,
  "Currency": null,
  "LanguageId": 0,
  "Language": null,
  "Warehouses": null,
  "TimeZone": null,
  "CorporationIdentificationNumber": null
}
```
