# Naming conventions

## Plural name vs. class name

Each entity has two names, and they differ:

| | Example | Where it appears |
| --- | --- | --- |
| Documentation / API name | `CustomerOrders` | the URL path, the page title, `title` in this bundle |
| API class name | `CustomerOrder` | the documentation page filename, `api_class` in this bundle |

The API name is usually the plural of the class name, but the mapping is
irregular often enough that it must never be computed. `Addresses`,
`BlanketOrderSales` and `SalesAgreementBases` all break a naive
"strip the trailing s" rule.

**In this bundle the relationship is never guessed.** Every cross-reference is
resolved from the actual hyperlink in the source documentation, so
`api_class` and the link target are always exact.

File naming here follows the class name (`/entities/Sales/CustomerOrder.md`)
because it is unique per module; the plural API name is in `title`.

## Commands

The 4 command pages are all titled with a bare verb in the
source documentation — `Create`, `Remove`, `GetWithdrawalInformation` — which is
ambiguous across pages. This bundle titles them by their unique class name
(for example `CreateSalesPickingList`) and keeps the original verb in
`doc_name`.

## Deprecated pages

An entity whose class name ends in `_Obsolete` is marked `status: deprecated` in
its frontmatter. Individual properties carry their own deprecation:
**58 properties** are marked deprecated, most with an
explicit replacement in the description.
