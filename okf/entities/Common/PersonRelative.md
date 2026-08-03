---
type: API Entity
title: PersonRelatives
description: Represents the relative of a person.
resource: https://api.monitor.se/api/Monitor.API.Common.PersonRelative.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PersonRelative.html
  title: Monitor API — PersonRelative
module: Common
api_class: PersonRelative
doc_name: PersonRelatives
endpoint: GET /api/v1/Common/PersonRelatives
guid: C58DE800-60B3-4BE8-B7D0-1D3ADA6CCA8B
permission: Show person
introduced_in: '22.3'
property_count: 3
referenced_by:
- /entities/Common/Person.md
---

# PersonRelatives

Represents the relative of a person.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `PersonRelative`
- **Endpoint:** `GET /api/v1/Common/PersonRelatives`
- **Required permission:** Show person
- **GUID:** `C58DE800-60B3-4BE8-B7D0-1D3ADA6CCA8B`
- **Introduced in:** 22.3

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the relative. |
| `PersonId` | `Int64` | no |  |  | The business key identifier of the person that the relative is related to. |
| `Name` | `String` | no |  | max length 70 | The name of the relative. |

## Referenced by

**Common**

- [Persons](Person.md) — `Relatives` (expand)


## Example

```json
{
  "Id": 0,
  "PersonId": 0,
  "Name": null
}
```
