---
type: Knowledge Bundle
title: Monitor ERP API
description: 'Data model of the Monitor ERP REST API: 380 documented entities across
  8 modules, with 1840 resolved relationships.'
resource: https://api.monitor.se/api/
okf_version: '0.2'
tags:
- monitor
- erp
- api
- data-model
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/
  title: Monitor ERP API documentation
---

# Monitor ERP API

The data model of the Monitor ERP REST API, derived from the public documentation
at https://api.monitor.se/api/.

## Scope

This bundle describes **what data the API exposes and how it connects**: every
queryable resource, its properties, types, enumerations, required permission and
its relationships to other resources.

Two things are deliberately outside that scope, and you will not find them here:

- **Write operations.** The API's 913 command pages (`POST` operations that create, update or remove data) are excluded by the crawler. This bundle is the read model.
- **How to authenticate and how to shape a request.** The source documentation
  contains no authentication, `$filter`/`$expand`/paging or status-code
  reference, so neither does this bundle. See
  [Querying the Monitor API](/guides/querying.md) for exactly what the source
  does and does not say.

Use this to work out *which resource and which field* you need. You will need
Monitor's own operational documentation to make the call.

| | |
| --- | ---: |
| Modules | 8 |
| Documented pages | 380 |
| Queryable entities | 351 |
| Commands | 4 |
| Payload types | 25 |
| Properties | 5379 |
| Relationships | 1840 |

## If you read only two pages

1. [Core entities](/guides/core-entities.md) — the 20 entities
   the rest of the model hangs off, ranked by how much of the API points at them.
2. [How entities relate](/guides/relationships.md) — foreign keys vs. navigation
   properties, which is the one concept you need to traverse anything here.

## Start here

- [Guides](/guides/index.md) — how the API is shaped and how entities relate
- [Modules](/modules/index.md) — the 8 top-level modules
- [Entities](/entities/index.md) — every documented page

## Modules

- [Accounting](/modules/Accounting.md) — 41 queryable, 0 commands, 2 types
- [Common](/modules/Common.md) — 110 queryable, 0 commands, 3 types
- [Infrastructure](/modules/Infrastructure.md) — 0 queryable, 0 commands, 18 types
- [Inventory](/modules/Inventory.md) — 50 queryable, 0 commands, 0 types
- [Manufacturing](/modules/Manufacturing.md) — 30 queryable, 0 commands, 0 types
- [Purchase](/modules/Purchase.md) — 30 queryable, 0 commands, 0 types
- [Sales](/modules/Sales.md) — 70 queryable, 4 commands, 2 types
- [TimeRecording](/modules/TimeRecording.md) — 20 queryable, 0 commands, 0 types

## How to use this bundle

Each entity page carries its endpoint, required permission, full property table,
enumerations and JSON example. References in the property tables are links, and
each page lists what references it under **Referenced by** — so both directions
of the graph can be walked without loading anything else.

To answer a question about one entity, open its page. To answer a question about
how data connects, follow the links.
