# Monitor ERP API (compact)

Compact, coding-agent-friendly view of the Monitor ERP API data model at
https://api.monitor.se/api/. The full bundle (`okf/`) documents the same
380 entities one file per entity; this bundle condenses every
module's entities into a single file so the whole API fits inside a small
agent context budget. Dropped versus `okf/`: JSON examples and full
per-member enum tables (kept as one compact line per enum property).

| | |
| --- | ---: |
| Modules | 8 |
| Documented pages | 380 |
| Queryable entities | 351 |
| Commands | 4 |
| Payload types | 25 |
| Properties | 5379 |
| Relationships | 1840 |

## Modules

- [Accounting](/modules/Accounting.md) — 41 queryable, 0 commands, 2 types
- [Common](/modules/Common.md) — 110 queryable, 0 commands, 3 types
- [Infrastructure](/modules/Infrastructure.md) — 0 queryable, 0 commands, 18 types
- [Inventory](/modules/Inventory.md) — 50 queryable, 0 commands, 0 types
- [Manufacturing](/modules/Manufacturing.md) — 30 queryable, 0 commands, 0 types
- [Purchase](/modules/Purchase.md) — 30 queryable, 0 commands, 0 types
- [Sales](/modules/Sales.md) — 70 queryable, 4 commands, 2 types
- [TimeRecording](/modules/TimeRecording.md) — 20 queryable, 0 commands, 0 types

## Most-referenced entities

- [Comments](/modules/Common.md#Common.Comment) — referenced by 214 properties
- [Currencies](/modules/Common.md#Common.Currency) — referenced by 198 properties
- [Persons](/modules/Common.md#Common.Person) — referenced by 72 properties
- [Parts](/modules/Inventory.md#Inventory.Part) — referenced by 70 properties
- [Addresses](/modules/Common.md#Common.Address) — referenced by 57 properties
- [ApplicationUsers](/modules/Common.md#Common.ApplicationUser) — referenced by 48 properties
- [Warehouses](/modules/Common.md#Common.Warehouse) — referenced by 44 properties
- [Units](/modules/Common.md#Common.Unit) — referenced by 33 properties
- [Customers](/modules/Sales.md#Sales.Customer) — referenced by 32 properties
- [CodingEntries](/modules/Accounting.md#Accounting.CodingEntry) — referenced by 31 properties
- [Suppliers](/modules/Purchase.md#Purchase.Supplier) — referenced by 28 properties
- [BusinessContactReferences](/modules/Common.md#Common.BusinessContactReference) — referenced by 27 properties
- [Revisions](/modules/Common.md#Common.Revision) — referenced by 26 properties
- [VatRates](/modules/Common.md#Common.VatRate) — referenced by 25 properties
- [PaymentTerms](/modules/Common.md#Common.PaymentTerm) — referenced by 24 properties
- [CurrencyExchangeTypes](/modules/Common.md#Common.CurrencyExchangeType) — referenced by 22 properties
- [CustomerOrders](/modules/Sales.md#Sales.CustomerOrder) — referenced by 22 properties
- [ProductRecords](/modules/Inventory.md#Inventory.ProductRecord) — referenced by 17 properties
- [CustomerAccountGroups](/modules/Sales.md#Sales.CustomerAccountGroup) — referenced by 15 properties
- [LanguageCodes](/modules/Common.md#Common.LanguageCode) — referenced by 15 properties

## Guides

- [Querying the Monitor API](/guides/querying.md)
- [Naming conventions](/guides/naming-conventions.md)
- [How entities relate](/guides/relationships.md)
- [Permissions](/guides/permissions.md)
- [Core entities](/guides/core-entities.md)
