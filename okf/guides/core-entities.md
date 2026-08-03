---
type: Guide
title: Core entities
description: The most heavily referenced entities -- where to start reading.
generated:
  by: process:monitor-okf-build
  from: 677a27684767
tags:
- guide
---

# Core entities

380 pages is too many to read. These 20 are the
ones the rest of the model hangs off, ranked by how many properties across the
whole API point at them.

A high count means the entity is shared basic data that many resources join to,
so it is both the most likely thing you need and the most useful thing to
understand first.

| Entity | Module | Referenced by | Description |
| --- | --- | ---: | --- |
| [Comments](../entities/Common/Comment.md) | [Common](../modules/Common.md) | 214 | Represents a comment, containing both raw and HTML formatted text. |
| [Currencies](../entities/Common/Currency.md) | [Common](../modules/Common.md) | 198 | Represents a queryable currency. |
| [Persons](../entities/Common/Person.md) | [Common](../modules/Common.md) | 72 | Represents a person. |
| [Parts](../entities/Inventory/Part.md) | [Inventory](../modules/Inventory.md) | 70 | Represents a part. |
| [Addresses](../entities/Common/Address.md) | [Common](../modules/Common.md) | 57 | Represents a queryable address. |
| [ApplicationUsers](../entities/Common/ApplicationUser.md) | [Common](../modules/Common.md) | 48 | Represents a queryable MONITOR application user. |
| [Warehouses](../entities/Common/Warehouse.md) | [Common](../modules/Common.md) | 44 | Represents a warehouse. |
| [Units](../entities/Common/Unit.md) | [Common](../modules/Common.md) | 33 | Represents a quantity unit. |
| [Customers](../entities/Sales/Customer.md) | [Sales](../modules/Sales.md) | 32 | Represents a customer. |
| [CodingEntries](../entities/Accounting/CodingEntry.md) | [Accounting](../modules/Accounting.md) | 31 | Represents a coding entry. |
| [Suppliers](../entities/Purchase/Supplier.md) | [Purchase](../modules/Purchase.md) | 28 | Represents a supplier. |
| [BusinessContactReferences](../entities/Common/BusinessContactReference.md) | [Common](../modules/Common.md) | 27 | Represents a queryable business contact reference. |
| [Revisions](../entities/Common/Revision.md) | [Common](../modules/Common.md) | 26 | Represents a revision. |
| [VatRates](../entities/Common/VatRate.md) | [Common](../modules/Common.md) | 25 | Represents a VAT rate. |
| [PaymentTerms](../entities/Common/PaymentTerm.md) | [Common](../modules/Common.md) | 24 | Represents a queryable payment term. |
| [CurrencyExchangeTypes](../entities/Common/CurrencyExchangeType.md) | [Common](../modules/Common.md) | 22 | Represents a currency exchange type. |
| [CustomerOrders](../entities/Sales/CustomerOrder.md) | [Sales](../modules/Sales.md) | 22 | Represents a customer order. |
| [ProductRecords](../entities/Inventory/ProductRecord.md) | [Inventory](../modules/Inventory.md) | 17 | Represents a product record. |
| [CustomerAccountGroups](../entities/Sales/CustomerAccountGroup.md) | [Sales](../modules/Sales.md) | 15 | Represents a customer account group. |
| [LanguageCodes](../entities/Common/LanguageCode.md) | [Common](../modules/Common.md) | 15 | Represents a language code. Language codes are the language definitions in MONITOR. |

Each page's **Referenced by** section lists exactly which entities and
properties point at it, so you can go from "this is widely used" to "used by
these specific resources" in one hop.

## Related

- [How entities relate](relationships.md) — what the reference counts mean
- [Modules](../modules/index.md) — the same 380 pages grouped by area
