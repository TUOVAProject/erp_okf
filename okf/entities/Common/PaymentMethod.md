---
type: API Entity
title: PaymentMethods
description: Represents a queryable payment method.
resource: https://api.monitor.se/api/Monitor.API.Common.PaymentMethod.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.PaymentMethod.html
  title: Monitor API — PaymentMethod
module: Common
api_class: PaymentMethod
doc_name: PaymentMethods
endpoint: GET /api/v1/Common/PaymentMethods
guid: 0ebaa8b3-5f0c-4ffe-8806-7a21e3858d15
permission: Show terms
introduced_in: '2.18'
property_count: 18
references_out:
- /entities/Accounting/CodingEntry.md
- /entities/Common/FormReportConfiguration.md
referenced_by:
- /entities/Accounting/AccountsPayable.md
- /entities/Accounting/IncomingPayment.md
- /entities/Accounting/OutgoingPayment.md
- /entities/Common/PaymentTerm.md
- /entities/Purchase/Supplier.md
- /entities/Sales/CustomerOrder.md
---

# PaymentMethods

Represents a queryable payment method.

- **Module:** [Common](/modules/Common.md)
- **API class:** `PaymentMethod`
- **Endpoint:** `GET /api/v1/Common/PaymentMethods`
- **Required permission:** Show terms
- **GUID:** `0ebaa8b3-5f0c-4ffe-8806-7a21e3858d15`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the payment method. |
| `Code` | `String` | no |  | unique, max length 7 | Max length 7 |
| `Description` | `String` | no |  |  | The translated description of the payment method. |
| `PaymentType` | `Int32` | no |  | enum | The payment type of the payment method. |
| `BankWebpage` | `String` | no |  | max length 255 | The bank webpage URL of the payment method. |
| `CustomerIdAtBank` | `String` | no |  | max length 15 | The bank customer identifier of the payment method. |
| `SendPaymentFilePath` | `String` | no |  | max length 255 | The send payment file path of the payment method. |
| `SendPaymentDirectoryPath` | `String` | no |  | max length 255 | The send payment directory path of the payment method. |
| `CodingAccountId` | `Int64?` | yes | [CodingEntries](/entities/Accounting/CodingEntry.md) |  | The business key identifier of the payment method's coding account. This account is also found in the payment method's . References Account. |
| `IsActive` | `Boolean` | no |  |  | Specifies if the payment method is active and available in the MONITOR system. |
| `BankingFeeAccountId` | `Int64?` | yes | [CodingEntries](/entities/Accounting/CodingEntry.md) |  | The business key identifier of the payment method's banking fee account. This account is also found in the payment method's . References Account. |
| `TransactionListFormReportConfigurationId` | `Int64?` | yes | [FormReportConfigurations](/entities/Common/FormReportConfiguration.md) |  | The business key identifier of the payment method's translation list form report configuration. |
| `ReceivingBankAccountValidation` | `Int32` | no |  | enum | Specifies which type of validation will be performed for the payment method's receiving bank account. |
| `ReceivingGiroAccountValidation` | `Int32` | no |  | enum | Specifies which type of validation will be performed for the payment method's receiving giro account. |
| `CodingAccountCodingEntryId` | `Int64` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) | since 2.38 | The business key identifier of the payment method's coding account coding entry. References CodingEntries . |
| `CodingAccountCodingEntry` | `CodingEntries` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) | expandable, since 2.38 | The payment method's coding account coding entry. |
| `BankingFeeCodingEntryId` | `Int64` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) | since 2.38 | The business key identifier of the payment method's banking fee coding entry. References CodingEntries . |
| `BankingFeeCodingEntry` | `CodingEntries` | no | [CodingEntries](/entities/Accounting/CodingEntry.md) | expandable, since 2.38 | The payment method's banking fee coding entry. |

## Enumerations

### PaymentType

| Name | Value |
| --- | ---: |
| `ManualPayment` | 0 |
| `ElectronicPayment` | 1 |
| `ElectronicIncomingPayment` | 2 |
| `CashPayment` | 3 |
| `BankIntegration` | 4 |
| `Factoring` | 5 |

### ReceivingBankAccountValidation

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `WarnIfMissing` | 1 |
| `BlockIfMissing` | 2 |

### ReceivingGiroAccountValidation

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `WarnIfMissing` | 1 |
| `BlockIfMissing` | 2 |


## Referenced by

**Accounting**

- [AccountsPayables](/entities/Accounting/AccountsPayable.md) — `PaymentMethodId` (FK)
- [IncomingPayments](/entities/Accounting/IncomingPayment.md) — `PaymentMethodId` (FK)
- [OutgoingPayments](/entities/Accounting/OutgoingPayment.md) — `PaymentMethodId` (FK)

**Common**

- [PaymentTerms](/entities/Common/PaymentTerm.md) — `PaymentMethodId` (FK)

**Purchase**

- [Suppliers](/entities/Purchase/Supplier.md) — `PaymentMethod` (expand)
- [Suppliers](/entities/Purchase/Supplier.md) — `PaymentMethodId` (FK)

**Sales**

- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `PaymentMethod` (expand)
- [CustomerOrders](/entities/Sales/CustomerOrder.md) — `PaymentMethodId` (FK)


## Example

```json
{
  "Id": 0,
  "Code": null,
  "Description": null,
  "PaymentType": 0,
  "BankWebpage": null,
  "CustomerIdAtBank": null,
  "SendPaymentFilePath": null,
  "SendPaymentDirectoryPath": null,
  "CodingAccountId": null,
  "IsActive": false,
  "BankingFeeAccountId": null,
  "TransactionListFormReportConfigurationId": null,
  "ReceivingBankAccountValidation": 0,
  "ReceivingGiroAccountValidation": 0,
  "CodingAccountCodingEntryId": 0,
  "CodingAccountCodingEntry": null,
  "BankingFeeCodingEntryId": 0,
  "BankingFeeCodingEntry": null
}
```
