---
type: API Entity
title: CentralBankCodes
description: Represents a central bank code.
resource: https://api.monitor.se/api/Monitor.API.Common.CentralBankCode.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.CentralBankCode.html
  title: Monitor API — CentralBankCode
module: Common
api_class: CentralBankCode
doc_name: CentralBankCodes
endpoint: GET /api/v1/Common/CentralBankCodes
guid: 7E13F0A1-0ADF-48D6-8E02-D3112C6D336F
permission: Show bank settings
introduced_in: '2.28'
property_count: 4
referenced_by:
- /entities/Common/BusinessContactBankAccount.md
---

# CentralBankCodes

Represents a central bank code.

- **Module:** [Common](/modules/Common.md)
- **API class:** `CentralBankCode`
- **Endpoint:** `GET /api/v1/Common/CentralBankCodes`
- **Required permission:** Show bank settings
- **GUID:** `7E13F0A1-0ADF-48D6-8E02-D3112C6D336F`
- **Introduced in:** 2.28

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the central bank code. |
| `Code` | `String` | no |  | max length 6 | The code of the central bank code. |
| `Description` | `String` | no |  |  | The description of the central bank code. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if the bank code is default. |

## Referenced by

**Common**

- [BusinessContactBankAccounts](/entities/Common/BusinessContactBankAccount.md) — `CentralBankCode` (expand)
- [BusinessContactBankAccounts](/entities/Common/BusinessContactBankAccount.md) — `CentralBankCodeId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "IsDefault": false
}
```
