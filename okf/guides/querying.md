---
type: Guide
title: Querying the Monitor API
description: Endpoint shape, HTTP verbs and what the documentation does and does not
  cover.
generated:
  by: process:monitor-okf-build
  from: 677a27684767
tags:
- guide
---

# Querying the Monitor API

## Endpoint shape

Every documented endpoint follows one pattern:

```
GET  https://<host>/<language>/<company>/api/v1/<Module>/<Entity>
POST https://<host>/<language>/<company>/api/v1/<Module>/<Entity>/<Command>
```

The documentation renders the host as `localhost:8001` with language `sv` and
company `001.1` — these are placeholders for your own Monitor server, not a
public endpoint. The `/api/v1/<Module>/<Entity>` tail is the stable part, and it
is the `endpoint` value recorded on every entity page in this bundle.

## What is in this bundle

- **351 queryable entities** — `GET`, returning a collection.
- **4 commands** — `POST`, listed in
  [Modules](../modules/index.md). Their properties table is the **request body**,
  not a response shape.
- **25 payload types** — no endpoint of their own; they appear
  nested inside other responses or command bodies.

## What is deliberately not in this bundle

The API's 913 command pages (`POST` operations that create, update or remove data) are excluded by the crawler. They live under `Monitor.API.<Module>.Commands.*` upstream
and the crawler skips them by design, because the purpose of this bundle is to
describe the data model comprehensively rather than the write API.

The 4 commands that *are* here are the ones the upstream
documentation files outside that namespace; they are included for completeness,
not because command coverage is a goal.

If you need a write operation, go to https://api.monitor.se/api/ and look under the
module's `Commands` namespace.

## What the source documentation does not cover

The scraped pages contain **no** query-parameter reference: no documented
`$filter`, `$select`, `$orderby`, `$expand` or paging syntax, and no response
status codes. Only `GET` and `POST` appear anywhere in the corpus.

Two indirect signals are still recorded here, because they are the closest thing
the docs give to query semantics:

- Properties marked `expandable` (599
  of them) are navigation properties — the docs flag them as expandable, which
  implies an expand mechanism exists.
- One property summary
  ([FormReportConfigurations](../entities/Common/FormReportConfiguration.md) `Type`)
  notes that `$filter` and `$orderby` cannot be used with it, which confirms both
  options exist in some form.

Treat anything beyond that as unverified: it is not in the source documentation.

## Related

- [Naming conventions](naming-conventions.md)
- [Relationships](relationships.md)
- [Permissions](permissions.md)
