---
type: API Entity
title: CompanyOverheadTypes
description: Represents an overhead type used in company emission and sustainability
  calculations.
resource: https://api.monitor.se/api/Monitor.API.Common.CompanyOverheadType.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.CompanyOverheadType.html
  title: Monitor API — CompanyOverheadType
module: Common
api_class: CompanyOverheadType
doc_name: CompanyOverheadTypes
endpoint: GET /api/v1/Common/CompanyOverheadTypes
guid: 25DC4043-EA63-4E39-A3FA-B1F64046334C
permission: Show pre-calculation
introduced_in: '25.9'
property_count: 4
---

# CompanyOverheadTypes

Represents an overhead type used in company emission and sustainability calculations.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `CompanyOverheadType`
- **Endpoint:** `GET /api/v1/Common/CompanyOverheadTypes`
- **Required permission:** Show pre-calculation
- **GUID:** `25DC4043-EA63-4E39-A3FA-B1F64046334C`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the overhead type. |
| `Description` | `String` | no |  | max length 400 | The description of the overhead type. |
| `Code` | `String` | no |  | max length 20 | The code of the overhead type. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the overhead type is default. |

## Example

```json
{
  "Id": 0,
  "Description": null,
  "Code": null,
  "IsDefault": false
}
```
