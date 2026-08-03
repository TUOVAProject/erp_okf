# Core entities

380 pages is too many to read. These 20 are the
ones the rest of the model hangs off, ranked by how many properties across the
whole API point at them.

A high count means the entity is shared basic data that many resources join to,
so it is both the most likely thing you need and the most useful thing to
understand first.

| Entity | Module | Referenced by | Description |
| --- | --- | ---: | --- |
| [Comments](../modules/Common.md#Common.Comment) | [Common](../modules/Common.md) | 214 | Represents a comment, containing both raw and HTML formatted text. |
| [Currencies](../modules/Common.md#Common.Currency) | [Common](../modules/Common.md) | 198 | Represents a queryable currency. |
| [Persons](../modules/Common.md#Common.Person) | [Common](../modules/Common.md) | 72 | Represents a person. |
| [Parts](../modules/Inventory.md#Inventory.Part) | [Inventory](../modules/Inventory.md) | 70 | Represents a part. |
| [Addresses](../modules/Common.md#Common.Address) | [Common](../modules/Common.md) | 57 | Represents a queryable address. |
| [ApplicationUsers](../modules/Common.md#Common.ApplicationUser) | [Common](../modules/Common.md) | 48 | Represents a queryable MONITOR application user. |
| [Warehouses](../modules/Common.md#Common.Warehouse) | [Common](../modules/Common.md) | 44 | Represents a warehouse. |
| [Units](../modules/Common.md#Common.Unit) | [Common](../modules/Common.md) | 33 | Represents a quantity unit. |
| [Customers](../modules/Sales.md#Sales.Customer) | [Sales](../modules/Sales.md) | 32 | Represents a customer. |
| [CodingEntries](../modules/Accounting.md#Accounting.CodingEntry) | [Accounting](../modules/Accounting.md) | 31 | Represents a coding entry. |
| [Suppliers](../modules/Purchase.md#Purchase.Supplier) | [Purchase](../modules/Purchase.md) | 28 | Represents a supplier. |
| [BusinessContactReferences](../modules/Common.md#Common.BusinessContactReference) | [Common](../modules/Common.md) | 27 | Represents a queryable business contact reference. |
| [Revisions](../modules/Common.md#Common.Revision) | [Common](../modules/Common.md) | 26 | Represents a revision. |
| [VatRates](../modules/Common.md#Common.VatRate) | [Common](../modules/Common.md) | 25 | Represents a VAT rate. |
| [PaymentTerms](../modules/Common.md#Common.PaymentTerm) | [Common](../modules/Common.md) | 24 | Represents a queryable payment term. |
| [CurrencyExchangeTypes](../modules/Common.md#Common.CurrencyExchangeType) | [Common](../modules/Common.md) | 22 | Represents a currency exchange type. |
| [CustomerOrders](../modules/Sales.md#Sales.CustomerOrder) | [Sales](../modules/Sales.md) | 22 | Represents a customer order. |
| [ProductRecords](../modules/Inventory.md#Inventory.ProductRecord) | [Inventory](../modules/Inventory.md) | 17 | Represents a product record. |
| [CustomerAccountGroups](../modules/Sales.md#Sales.CustomerAccountGroup) | [Sales](../modules/Sales.md) | 15 | Represents a customer account group. |
| [LanguageCodes](../modules/Common.md#Common.LanguageCode) | [Common](../modules/Common.md) | 15 | Represents a language code. Language codes are the language definitions in MONITOR. |

Each page's **Referenced by** section lists exactly which entities and
properties point at it, so you can go from "this is widely used" to "used by
these specific resources" in one hop.

## Related

- [How entities relate](relationships.md) — what the reference counts mean
- [Modules](../index.md) — the same 380 pages grouped by area
