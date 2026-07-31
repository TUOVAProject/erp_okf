---
type: API Entity
title: PersonTimeBanks
description: Represents a persons time bank.
resource: https://api.monitor.se/api/Monitor.API.TimeRecording.PersonTimeBank.html
tags:
- TimeRecording
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.TimeRecording.PersonTimeBank.html
  title: Monitor API — PersonTimeBank
module: TimeRecording
api_class: PersonTimeBank
doc_name: PersonTimeBanks
endpoint: GET /api/v1/TimeRecording/PersonTimeBanks
guid: 4F558C19-C90B-4F27-870C-EAEB1E7772D9
permission: Show recording items
introduced_in: '22.3'
property_count: 4
references_out:
- /entities/Common/Person.md
- /entities/TimeRecording/TimeBank.md
referenced_by:
- /entities/Common/Person.md
---

# PersonTimeBanks

Represents a persons time bank.

- **Module:** [TimeRecording](/modules/TimeRecording.md)
- **API class:** `PersonTimeBank`
- **Endpoint:** `GET /api/v1/TimeRecording/PersonTimeBanks`
- **Required permission:** Show recording items
- **GUID:** `4F558C19-C90B-4F27-870C-EAEB1E7772D9`
- **Introduced in:** 22.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the person time bank. |
| `PersonId` | `Int64` | no | [Persons](/entities/Common/Person.md) |  | The person identifier of the person time bank. |
| `TimeBankId` | `Int64` | no | [TimeBanks](/entities/TimeRecording/TimeBank.md) |  | The time bank identifier for the person time bank. |
| `Balance` | `TimeSpan` | no |  |  | The balance of the person time bank. |

## Referenced by

**Common**

- [Persons](/entities/Common/Person.md) — `TimeBanks` (expand)


## Example

```json
{
  "Id": 0,
  "PersonId": 0,
  "TimeBankId": 0,
  "Balance": "00:00:00"
}
```
