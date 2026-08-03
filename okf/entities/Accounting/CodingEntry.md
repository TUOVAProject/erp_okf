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

- **Module:** [Accounting](../../modules/Accounting.md)
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
| `AccountId` | `Int64?` | yes | [Accounts](Account.md) |  | The business key identifier of the coding entry's account. |
| `Account` | `Accounts` | no | [Accounts](Account.md) | expandable | The account of the coding entry. |
| `CodingEntryElements` | `CodingEntryElements[]` | no | [CodingEntryElements](CodingEntryElement.md) | expandable, collection | The coding entry elements of the coding entry. |

## Referenced by

**Accounting**

- [AccountingBudgets](AccountingBudget.md) — `CodingEntry` (expand)
- [AccountingBudgets](AccountingBudget.md) — `CodingEntryId` (FK)
- [AllocationKeyResultRows](AllocationKeyResultRow.md) — `CodingEntry` (expand)
- [AllocationKeyResultRows](AllocationKeyResultRow.md) — `CodingEntryId` (FK)
- [Balances](Balance.md) — `CodingEntryId` (FK)
- [BookingRows](BookingRow.md) — `CodingEntryId` (FK)
- [CodingEntryElements](CodingEntryElement.md) — `CodingEntryId` (FK)
- [CodingRows](CodingRow.md) — `CodingEntry` (expand)
- [CodingRows](CodingRow.md) — `CodingEntryId` (FK)
- [OpeningBalances](OpeningBalance.md) — `CodingEntryId` (FK)
- [StandardAccounts](StandardAccount.md) — `CodingEntryId` (FK)
- [VoucherRows](VoucherRow.md) — `CodingEntryId` (FK)

**Common**

- [PaymentMethods](../Common/PaymentMethod.md) — `BankingFeeAccountId` (FK)
- [PaymentMethods](../Common/PaymentMethod.md) — `BankingFeeCodingEntry` (expand)
- [PaymentMethods](../Common/PaymentMethod.md) — `BankingFeeCodingEntryId` (FK)
- [PaymentMethods](../Common/PaymentMethod.md) — `CodingAccountCodingEntry` (expand)
- [PaymentMethods](../Common/PaymentMethod.md) — `CodingAccountCodingEntryId` (FK)
- [PaymentMethods](../Common/PaymentMethod.md) — `CodingAccountId` (FK)
- [WriteOffCodes](../Common/WriteOffCode.md) — `IncomingPaymentCodingEntry` (expand)
- [WriteOffCodes](../Common/WriteOffCode.md) — `IncomingPaymentCodingEntryId` (FK)
- [WriteOffCodes](../Common/WriteOffCode.md) — `OutgoingPaymentCodingEntry` (expand)
- [WriteOffCodes](../Common/WriteOffCode.md) — `OutgoingPaymentCodingEntryId` (FK)

**Purchase**

- [PurchaseOrderInvoiceRows](../Purchase/PurchaseOrderInvoiceRow.md) — `CodingId` (FK)
- [SupplierAccounts](../Purchase/SupplierAccount.md) — `CodingEntryId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `AccrualAccountingReverseAccount` (expand)
- [Suppliers](../Purchase/Supplier.md) — `AccrualAccountingReverseAccountId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `OutgoingPaymentsAccount` (expand)
- [Suppliers](../Purchase/Supplier.md) — `OutgoingPaymentsAccountId` (FK)
- [Suppliers](../Purchase/Supplier.md) — `PurchaseAccount` (expand)
- [Suppliers](../Purchase/Supplier.md) — `PurchaseAccountId` (FK)

**Sales**

- [CustomerOrderPaymentPlanRows](../Sales/CustomerOrderPaymentPlanRow.md) — `CodingEntryId` (FK)


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
