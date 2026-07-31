---
type: API Entity
title: BusinessOpportunityReferences
description: Represents a business opportunity reference.
resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityReference.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.BusinessOpportunityReference.html
  title: Monitor API — BusinessOpportunityReference
module: Sales
api_class: BusinessOpportunityReference
doc_name: BusinessOpportunityReferences
endpoint: GET /api/v1/Sales/BusinessOpportunityReferences
guid: 26f6f166-6d9c-4c38-994b-2b7dcd66d784
permission: Show business opportunity
introduced_in: '25.9'
property_count: 12
references_out:
- /entities/Common/Comment.md
- /entities/Common/CommunicationAddress.md
- /entities/Sales/BusinessOpportunity.md
- /entities/Sales/Customer.md
---

# BusinessOpportunityReferences

Represents a business opportunity reference.

- **Module:** [Sales](/modules/Sales.md)
- **API class:** `BusinessOpportunityReference`
- **Endpoint:** `GET /api/v1/Sales/BusinessOpportunityReferences`
- **Required permission:** Show business opportunity
- **GUID:** `26f6f166-6d9c-4c38-994b-2b7dcd66d784`
- **Introduced in:** 25.9

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the business opportunity reference. |
| `Name` | `String` | no |  | max length 40 | The name of the reference. |
| `ParentId` | `Int64` | no | [BusinessOpportunities](/entities/Sales/BusinessOpportunity.md) |  | The business key identifier of the reference's business opportunity. |
| `ShouldFilterLogPosts` | `Boolean` | no |  |  | Specifies if the reference should filter log posts. |
| `IsDefault` | `Boolean` | no |  |  | Specifies if this is the default reference for the business opportunity. |
| `CustomerId` | `Int64?` | yes | [Customers](/entities/Sales/Customer.md) |  | The business key identifier of the customer the reference belongs to. |
| `ReferenceCode` | `String` | no |  | max length 40 | The code of the reference. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the reference's comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The reference's comment. |
| `Remark` | `String` | no |  | max length 80 | The remark of the reference. |
| `ReferenceCategory` | `String` | no |  | max length 20 | The reference category of the reference. |
| `CommunicationAddresses` | `CommunicationAddresses[]` | no | [CommunicationAddresses](/entities/Common/CommunicationAddress.md) | expandable, collection | The communication addresses of the reference. |

## Example

```json
{
  "Id": 0,
  "Name": null,
  "ParentId": 0,
  "ShouldFilterLogPosts": false,
  "IsDefault": false,
  "CustomerId": null,
  "ReferenceCode": null,
  "CommentId": null,
  "Comment": null,
  "Remark": null,
  "ReferenceCategory": null,
  "CommunicationAddresses": null
}
```
