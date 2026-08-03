---
type: API Entity
title: EimDocumentTypes
description: Represents an EIM document type.
resource: https://api.monitor.se/api/Monitor.API.Purchase.EimDocumentType.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.EimDocumentType.html
  title: Monitor API — EimDocumentType
module: Purchase
api_class: EimDocumentType
doc_name: EimDocumentTypes
endpoint: GET /api/v1/Purchase/EimDocumentTypes
guid: A5EC82C0-BD86-44D1-A6AF-DB103D802E3D
permission: Show attachment types
introduced_in: '22.5'
property_count: 6
referenced_by:
- /entities/Purchase/EimDocument.md
---

# EimDocumentTypes

Represents an EIM document type.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `EimDocumentType`
- **Endpoint:** `GET /api/v1/Purchase/EimDocumentTypes`
- **Required permission:** Show attachment types
- **GUID:** `A5EC82C0-BD86-44D1-A6AF-DB103D802E3D`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the document type. |
| `Number` | `Int64` | no |  | unique | The human readable identifier of the document type. |
| `Description` | `String` | no |  | max length 400, since 25.9 | The name of the document type. |
| `IsDefaultImportType` | `Boolean` | no |  | since 25.9 | Specifies if the type is the default type for E-invoice imports. |
| `IsDefaultMonitorExpenseType` | `Boolean` | no |  | since 25.9 | Specifies if the type is the default type for imports from Monitor Expense. |
| `IsDefaultBankIntegrationType` | `Boolean` | no |  | since 25.9 | Specifies if the type is the default type for imports via bank integration. |

## Referenced by

**Purchase**

- [EimDocuments](EimDocument.md) — `DocumentTypeId` (FK)


## Example

```json
{
  "Id": 0,
  "Number": 0,
  "Description": null,
  "IsDefaultImportType": false,
  "IsDefaultMonitorExpenseType": false,
  "IsDefaultBankIntegrationType": false
}
```
