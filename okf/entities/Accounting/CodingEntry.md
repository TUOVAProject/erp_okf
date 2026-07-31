---
type: API Entity
title: CodingEntries
description: Represents a coding entry.
resource: https://api.monitor.se/api/Monitor.API.Accounting.CodingEntry.html
tags:
- Accounting
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Accounting.CodingEntry.html
  title: Monitor API — CodingEntry
module: Accounting
api_class: CodingEntry
doc_name: CodingEntries
endpoint: GET /api/v1/Accounting/CodingEntries
guid: 57158A06-CC4E-4AB7-890D-D1760E2AF6E1
permission: Show dimensions/dimension codes
introduced_in: '2.30'
property_count: 5
references_out:
- /entities/Accounting/Account.md
- /entities/Accounting/CodingEntryElement.md
referenced_by:
- /entities/Accounting/AccountingBudget.md
- /entities/Accounting/AllocationKeyResultRow.md
- /entities/Accounting/Balance.md
- /entities/Accounting/BookingRow.md
- /entities/Accounting/CodingEntryElement.md
- /entities/Accounting/CodingRow.md
- /entities/Accounting/OpeningBalance.md
- /entities/Accounting/StandardAccount.md
- /entities/Accounting/VoucherRow.md
- /entities/Common/PaymentMethod.md
- /entities/Common/WriteOffCode.md
- /entities/Purchase/PurchaseOrderInvoiceRow.md
- /entities/Purchase/Supplier.md
- /entities/Purchase/SupplierAccount.md
- /entities/Sales/CustomerOrderPaymentPlanRow.md
---

# CodingEntries

Represents a coding entry.

- **Module:** [Accounting](/modules/Accounting.md)
- **API class:** `CodingEntry`
- **Endpoint:** `GET /api/v1/Accounting/CodingEntries`
- **Required permission:** Show dimensions/dimension codes
- **GUID:** `57158A06-CC4E-4AB7-890D-D1760E2AF6E1`
- **Introduced in:** 2.30

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the coding entry. |
| `CodingEntryDescription` | `String` | no |  | max length 50 | The description of the coding entry. |
| `AccountId` | `Int64?` | yes | [Accounts](/entities/Accounting/Account.md) |  | The business key identifier of the coding entry's account. |
| `Account` | `Accounts` | no | [Accounts](/entities/Accounting/Account.md) | expandable | The account of the coding entry. |
| `CodingEntryElements` | `CodingEntryElements[]` | no | [CodingEntryElements](/entities/Accounting/CodingEntryElement.md) | expandable, collection | The coding entry elements of the coding entry. |

## Referenced by

**Accounting**

- [AccountingBudgets](/entities/Accounting/AccountingBudget.md) — `CodingEntry` (expand)
- [AccountingBudgets](/entities/Accounting/AccountingBudget.md) — `CodingEntryId` (FK)
- [AllocationKeyResultRows](/entities/Accounting/AllocationKeyResultRow.md) — `CodingEntry` (expand)
- [AllocationKeyResultRows](/entities/Accounting/AllocationKeyResultRow.md) — `CodingEntryId` (FK)
- [Balances](/entities/Accounting/Balance.md) — `CodingEntryId` (FK)
- [BookingRows](/entities/Accounting/BookingRow.md) — `CodingEntryId` (FK)
- [CodingEntryElements](/entities/Accounting/CodingEntryElement.md) — `CodingEntryId` (FK)
- [CodingRows](/entities/Accounting/CodingRow.md) — `CodingEntry` (expand)
- [CodingRows](/entities/Accounting/CodingRow.md) — `CodingEntryId` (FK)
- [OpeningBalances](/entities/Accounting/OpeningBalance.md) — `CodingEntryId` (FK)
- [StandardAccounts](/entities/Accounting/StandardAccount.md) — `CodingEntryId` (FK)
- [VoucherRows](/entities/Accounting/VoucherRow.md) — `CodingEntryId` (FK)

**Common**

- [PaymentMethods](/entities/Common/PaymentMethod.md) — `BankingFeeAccountId` (FK)
- [PaymentMethods](/entities/Common/PaymentMethod.md) — `BankingFeeCodingEntry` (expand)
- [PaymentMethods](/entities/Common/PaymentMethod.md) — `BankingFeeCodingEntryId` (FK)
- [PaymentMethods](/entities/Common/PaymentMethod.md) — `CodingAccountCodingEntry` (expand)
- [PaymentMethods](/entities/Common/PaymentMethod.md) — `CodingAccountCodingEntryId` (FK)
- [PaymentMethods](/entities/Common/PaymentMethod.md) — `CodingAccountId` (FK)
- [WriteOffCodes](/entities/Common/WriteOffCode.md) — `IncomingPaymentCodingEntry` (expand)
- [WriteOffCodes](/entities/Common/WriteOffCode.md) — `IncomingPaymentCodingEntryId` (FK)
- [WriteOffCodes](/entities/Common/WriteOffCode.md) — `OutgoingPaymentCodingEntry` (expand)
- [WriteOffCodes](/entities/Common/WriteOffCode.md) — `OutgoingPaymentCodingEntryId` (FK)

**Purchase**

- [PurchaseOrderInvoiceRows](/entities/Purchase/PurchaseOrderInvoiceRow.md) — `CodingId` (FK)
- [SupplierAccounts](/entities/Purchase/SupplierAccount.md) — `CodingEntryId` (FK)
- [Suppliers](/entities/Purchase/Supplier.md) — `AccrualAccountingReverseAccount` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `AccrualAccountingReverseAccountId` (FK)
- [Suppliers](/entities/Purchase/Supplier.md) — `OutgoingPaymentsAccount` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `OutgoingPaymentsAccountId` (FK)
- [Suppliers](/entities/Purchase/Supplier.md) — `PurchaseAccount` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `PurchaseAccountId` (FK)

**Sales**

- [CustomerOrderPaymentPlanRows](/entities/Sales/CustomerOrderPaymentPlanRow.md) — `CodingEntryId` (FK)


## Example

```json
{
  "Id": 0,
  "CodingEntryDescription": null,
  "AccountId": null,
  "Account": null,
  "CodingEntryElements": null
}
```
