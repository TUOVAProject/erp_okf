---
type: Guide
title: How entities relate
description: Foreign keys vs. navigation properties, and how to traverse the model.
generated:
  by: process:monitor-okf-build
  from: 677a27684767
tags:
- guide
---

# How entities relate

The model contains **1840 relationships** between
380 entities. They come in two forms, and most related entities
are connected by both at once.

## Foreign key (1227 edges)

A scalar id property whose description says it references another entity:

```
| `PaymentTermId` | `Int64?` | yes | PaymentTerms | | ... References PaymentTerms |
```

Use these to join data yourself. They are almost always named `<Entity>Id` and
typed `Int64` / `Int64?`.

## Navigation property (613 edges)

A property whose **type** is another entity, usually flagged `expandable`:

```
| `PaymentTerm` | `PaymentTerms` | no | PaymentTerms | expandable | ... |
```

These are the related object itself rather than its id. A property typed
`SomeEntity[]` is a collection of them.

So `CustomerOrders` carries both `PaymentTermId` (the key) and `PaymentTerm`
(the object) pointing at the same target.

## Traversing this bundle

Every reference in a properties table is a markdown link to the target entity
page, and every entity page ends with a **Referenced by** section listing the
incoming edges grouped by module. Both directions are also in the frontmatter as
`references_out` and `referenced_by`, so a reverse lookup needs no index.

The most heavily referenced entities are the shared basic-data tables. Follow
**Referenced by** on any of these to see how widely they are used:

- [Comments](/entities/Common/Comment.md) — referenced by 214 properties
- [Currencies](/entities/Common/Currency.md) — referenced by 198 properties
- [Persons](/entities/Common/Person.md) — referenced by 72 properties
- [Parts](/entities/Inventory/Part.md) — referenced by 70 properties
- [Addresses](/entities/Common/Address.md) — referenced by 57 properties

## Module coupling

Each module page has a **Depends on other modules** section listing exactly
which entities it reaches into elsewhere — the fastest way to see how coupled
the modules are.
