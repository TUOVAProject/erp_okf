---
type: API Entity
title: CompanyEmissionDetails
description: Represents a company emission type linked to sustainability reporting
  according to the GHG protocol.
resource: https://api.monitor.se/api/Monitor.API.Common.CompanyEmissionDetail.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.CompanyEmissionDetail.html
  title: Monitor API — CompanyEmissionDetail
module: Common
api_class: CompanyEmissionDetail
doc_name: CompanyEmissionDetails
endpoint: GET /api/v1/Common/CompanyEmissionDetails
guid: 57A8373B-5A6C-4D22-B057-A7094FBCC9C8
permission: Show pre-calculation
introduced_in: '25.9'
property_count: 11
references_out:
- /entities/Common/Unit.md
---

# CompanyEmissionDetails

Represents a company emission type linked to sustainability reporting according to the GHG protocol.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `CompanyEmissionDetail`
- **Endpoint:** `GET /api/v1/Common/CompanyEmissionDetails`
- **Required permission:** Show pre-calculation
- **GUID:** `57A8373B-5A6C-4D22-B057-A7094FBCC9C8`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the company emission type. |
| `Code` | `String` | no |  | max length 20 | The code of the company emission type. |
| `Description` | `String` | no |  | max length 400 | The description of the company emission type. |
| `EmissionType` | `Int32` | no |  |  | The emission type of the company emission type. |
| `Value` | `Decimal` | no |  |  | The value of the company emission type. |
| `Origin` | `String` | no |  |  | The origin of the company emission type. |
| `OriginDate` | `DateTimeOffset?` | yes |  |  | The origin date of the company emission type. |
| `ReliabilityIndex` | `Decimal` | no |  |  | The reliability index of the company emission type. |
| `ReportingMethod` | `Int32` | no |  |  | The reporting method of the company emission type. |
| `UnitId` | `Int64?` | yes |  |  | The business key identifier of the company emission type's unit. |
| `Unit` | `Units` | no | [Units](Unit.md) | expandable | The company emission type's unit. |

## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "EmissionType": 0,
  "Value": 0.0,
  "Origin": null,
  "OriginDate": null,
  "ReliabilityIndex": 0.0,
  "ReportingMethod": 0,
  "UnitId": null,
  "Unit": null
}
```
