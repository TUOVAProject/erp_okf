---
type: API Entity
title: EimDocuments
description: Represents an EimDocument.
resource: https://api.monitor.se/api/Monitor.API.Purchase.EimDocument.html
tags:
- Purchase
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Purchase.EimDocument.html
  title: Monitor API — EimDocument
module: Purchase
api_class: EimDocument
doc_name: EimDocuments
endpoint: GET /api/v1/Purchase/EimDocuments
guid: 41CE6B89-941B-4658-959C-8EB16CEB5217
permission: Show supplier invoice
introduced_in: '22.5'
property_count: 5
references_out:
- /entities/Accounting/AccountsPayable.md
- /entities/Common/BlobData.md
- /entities/Purchase/EimDocumentType.md
---

# EimDocuments

Represents an EimDocument.

- **Module:** [Purchase](../../modules/Purchase.md)
- **API class:** `EimDocument`
- **Endpoint:** `GET /api/v1/Purchase/EimDocuments`
- **Required permission:** Show supplier invoice
- **GUID:** `41CE6B89-941B-4658-959C-8EB16CEB5217`
- **Introduced in:** 22.5

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the document. |
| `BlobDataId` | `Int64` | no | [BlobData](../Common/BlobData.md) |  | The business key identifier of the blob data contained in the document. |
| `RotationAngle` | `Int32` | no |  |  | The amount of rotation in degrees to be applied to the document. |
| `AccountsPayableId` | `Int64` | no | [AccountsPayables](../Accounting/AccountsPayable.md) |  | The business key identifier of the accounts payable to which document belongs. |
| `DocumentTypeId` | `Int64` | no | [EimDocumentTypes](EimDocumentType.md) |  | The business key identifier of the document type of the document. |

## Example

```json
{
  "Id": 0,
  "BlobDataId": 0,
  "RotationAngle": 0,
  "AccountsPayableId": 0,
  "DocumentTypeId": 0
}
```
