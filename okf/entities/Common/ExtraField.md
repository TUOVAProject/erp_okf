---
type: API Entity
title: ExtraFields
description: Represents an extra field.
resource: https://api.monitor.se/api/Monitor.API.Common.ExtraField.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.ExtraField.html
  title: Monitor API — ExtraField
module: Common
api_class: ExtraField
doc_name: ExtraFields
endpoint: GET /api/v1/Common/ExtraFields
guid: 3726A06F-153C-404A-A625-17B3F47477AC
permission: Show extra fields
introduced_in: '2.18'
property_count: 16
references_out:
- /entities/Common/Comment.md
- /entities/Common/ExtraFieldOptionTemplate.md
referenced_by:
- /entities/Common/Person.md
- /entities/Common/Project.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/Part.md
- /entities/Inventory/ProductRecord.md
- /entities/Manufacturing/OperationRow.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
---

# ExtraFields

Represents an extra field.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `ExtraField`
- **Endpoint:** `GET /api/v1/Common/ExtraFields`
- **Required permission:** Show extra fields
- **GUID:** `3726A06F-153C-404A-A625-17B3F47477AC`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the extra field. |
| `ParentClass` | `Guid` | no |  |  | The GUID of the parent type. |
| `ParentId` | `Int64` | no |  |  | The business key identifier of the parent. |
| `Identifier` | `String` | no |  |  | The alphanumeric identifier of the extra field template. |
| `Type` | `Int32` | no |  |  | The extra field template type. |
| `StringValue` | `String` | no |  |  | The string value of the extra field. |
| `IntegerValue` | `Int32?` | yes |  |  | The integer value of the extra field. |
| `DecimalValue` | `Decimal?` | yes |  |  | The decimal value of the extra field. |
| `DateOnlyValue` | `DateTimeOffset?` | yes |  |  | The date-only value of the extra field. |
| `DateTimeValue` | `DateTimeOffset?` | yes |  |  | The date-time value of the extra field. |
| `SelectedOptionId` | `Int64?` | yes | [ExtraFieldOptionTemplates](ExtraFieldOptionTemplate.md) |  | The business key identifier of the selected option. References ExtraFieldOptionTemplates . |
| `SelectedOption` | `ExtraFieldOptionTemplates` | no | [ExtraFieldOptionTemplates](ExtraFieldOptionTemplate.md) | expandable | The selected option of the extra field. Only applicable to extra fields of type 6 (Options). |
| `SelectedOptionIds` | `String` | no | [ExtraFieldOptionTemplates](ExtraFieldOptionTemplate.md) |  | A comma separated value list of the selected options. References multiple ExtraFieldOptionTemplates . |
| `SelectedOptions` | `ExtraFieldOptionTemplates[]` | no | [ExtraFieldOptionTemplates](ExtraFieldOptionTemplate.md) | expandable, collection | The selected options of the extra field. Only applicable to extra fields of type 7 (Multiple options). |
| `CommentId` | `Int64?` | yes | [Comments](Comment.md) | since 2.36 | The business key identifier of the comment value of the extra field. |
| `Comment` | `Comments` | no | [Comments](Comment.md) | expandable, since 2.36 | The comment value of the extra field. |

## Referenced by

**Common**

- [Persons](Person.md) — `ExtraFields` (expand)
- [Projects](Project.md) — `ExtraFields` (expand)

**Inventory**

- [CaseEntry](../Inventory/CaseEntry.md) — `ExtraFields` (expand)
- [Parts](../Inventory/Part.md) — `ExtraFields` (expand)
- [ProductRecords](../Inventory/ProductRecord.md) — `ExtraFields` (expand)

**Manufacturing**

- [OperationRows](../Manufacturing/OperationRow.md) — `ExtraFields` (expand)

**Purchase**

- [Suppliers](../Purchase/Supplier.md) — `ExtraFields` (expand)

**Sales**

- [Customers](../Sales/Customer.md) — `ExtraFields` (expand)


## Example

```json
{
  "Id": 0,
  "ParentClass": "00000000-0000-0000-0000-000000000000",
  "ParentId": 0,
  "Identifier": null,
  "Type": 0,
  "StringValue": null,
  "IntegerValue": null,
  "DecimalValue": null,
  "DateOnlyValue": null,
  "DateTimeValue": null,
  "SelectedOptionId": null,
  "SelectedOption": null,
  "SelectedOptionIds": null,
  "SelectedOptions": null,
  "CommentId": null,
  "Comment": null
}
```
