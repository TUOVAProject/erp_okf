---
type: Bundle Overview
title: About this bundle
description: 'Data model of the Monitor ERP REST API: 380 documented entities across
  8 modules, with 1840 resolved relationships.'
resource: https://api.monitor.se/api/
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

# About this bundle

The data model of the Monitor ERP REST API, derived from the public documentation
at https://api.monitor.se/api/.

## Scope

This bundle describes **what data the API exposes and how it connects**: every
queryable resource, its properties, types, enumerations, required permission and
its relationships to other resources.

Two things are deliberately outside that scope:

- **Write operations.** The API's 913 command pages (`POST` operations that create, update or remove data) are excluded by the crawler. This bundle is the read model.
- **Monitor's Developer Guide.** Only the API Reference pages are scraped. How to
  authenticate, the URL format, query options and worked examples are in
  Monitor's Developer Guide: https://api.monitor.se/articles/v1/index.html

See [Querying the Monitor API](guides/querying.md) for the endpoint shape.

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

1. [Core entities](guides/core-entities.md) — the 20 entities
   the rest of the model hangs off, ranked by how much of the API points at them.
2. [How entities relate](guides/relationships.md) — foreign keys vs. navigation
   properties, which is the one concept you need to traverse anything here.

## How to use this bundle

Each entity page carries its endpoint, required permission, full property table,
enumerations and JSON example. References in the property tables are links, and
each page lists what references it under **Referenced by** — so both directions
of the graph can be walked without loading anything else.

To answer a question about one entity, open its page. To answer a question about
how data connects, follow the links.
