---
type: API Entity
title: ConnectionProfiles
description: Represents a connection profile.
resource: https://api.monitor.se/api/Monitor.API.Common.ConnectionProfile.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ConnectionProfile.html
  title: Monitor API — ConnectionProfile
module: Common
api_class: ConnectionProfile
doc_name: ConnectionProfiles
endpoint: GET /api/v1/Common/ConnectionProfiles
guid: 8C881937-8E3F-49C0-A55E-6B5E295C86DD
permission: Show connection
introduced_in: '23.2'
property_count: 11
referenced_by:
- /entities/Common/TransferProfile.md
---

# ConnectionProfiles

Represents a connection profile.

- **Module:** [Common](/modules/Common.md)
- **API class:** `ConnectionProfile`
- **Endpoint:** `GET /api/v1/Common/ConnectionProfiles`
- **Required permission:** Show connection
- **GUID:** `8C881937-8E3F-49C0-A55E-6B5E295C86DD`
- **Introduced in:** 23.2

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the profile. |
| `Number` | `Int64` | no |  | unique | The number of the profile. |
| `Description` | `String` | no |  |  | The description of the profile. |
| `TargetRole` | `Int32` | no |  | enum | The transfer role of the profile. |
| `RemoteCompanyId` | `Guid` | no |  |  | The remote company identifier of the profile. |
| `RemoteCompanyNumber` | `String` | no |  | max length 10 | The remote company number of the profile. |
| `RemoteCompanyName` | `String` | no |  | max length 80 | The remote company name of the profile. |
| `RemoteDnsName` | `String` | no |  | max length 253 | The remote dns name of the profile. |
| `RemotePort` | `Int32` | no |  |  | The remote TCP/IP port of the profile. |
| `LocalDnsName` | `String` | no |  | max length 253 | The local dns name of the profile. |
| `LocalPort` | `Int32` | no |  |  | The local TCP/IP port of the profile. |

## Enumerations

### TargetRole

| Name | Value |
| --- | ---: |
| `ManufacturingCompany` | 0 |
| `SalesCompany` | 1 |


## Referenced by

**Common**

- [TransferProfiles](/entities/Common/TransferProfile.md) — `ConnectionProfileId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "TargetRole": 0,
  "RemoteCompanyId": "00000000-0000-0000-0000-000000000000",
  "RemoteCompanyNumber": null,
  "RemoteCompanyName": null,
  "RemoteDnsName": null,
  "RemotePort": 0,
  "LocalDnsName": null,
  "LocalPort": 0
}
```
