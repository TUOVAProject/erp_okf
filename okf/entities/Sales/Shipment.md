---
type: API Entity
title: Shipments
description: Represents a shipment.
resource: https://api.monitor.se/api/Monitor.API.Sales.Shipment.html
tags:
- Sales
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Sales.Shipment.html
  title: Monitor API — Shipment
module: Sales
api_class: Shipment
doc_name: Shipments
endpoint: GET /api/v1/Sales/Shipments
guid: 4E8AEFBC-74B0-427C-A043-5AA7D91ED387
permission: Show shipment
introduced_in: '23.1'
property_count: 89
references_out:
- /entities/Common/Address.md
- /entities/Common/Currency.md
- /entities/Common/DeliveryAddress.md
- /entities/Common/DeliveryMethod.md
- /entities/Common/DeliveryTerm.md
- /entities/Common/Warehouse.md
- /entities/Purchase/Supplier.md
- /entities/Sales/Customer.md
- /entities/Sales/ShipmentCustoms.md
- /entities/Sales/ShippingService.md
- /entities/Sales/ShippingTemplate.md
referenced_by:
- /entities/Sales/ShipmentCustoms.md
- /entities/Sales/ShipmentInformationSource.md
- /entities/Sales/ShipmentPackageInformation.md
---

# Shipments

Represents a shipment.

- **Module:** [Sales](../../modules/Sales.md)
- **API class:** `Shipment`
- **Endpoint:** `GET /api/v1/Sales/Shipments`
- **Required permission:** Show shipment
- **GUID:** `4E8AEFBC-74B0-427C-A043-5AA7D91ED387`
- **Introduced in:** 23.1

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the shipment. |
| `ShipmentNumber` | `String` | no |  | unique, max length 20 | The human readable identifier of the shipment. |
| `ConsignmentNo` | `String` | no |  | max length 35 | The real consignment/shipment number from the shipper. |
| `UnifaunOnlineFirstParcelNo` | `String` | no |  | max length 35 | The unifaun online first parcel number of the shipment. |
| `UnifaunOnlineFirstPrintLink` | `String` | no |  | max length 4000 | The unifaun online first print link of the shipment. |
| `LogTradeTrackingNo` | `String` | no |  | max length 400 | The log trade tracking number of the shipment. |
| `DeliveryMethodId` | `Int64?` | yes | [DeliveryMethods](../Common/DeliveryMethod.md) |  | The business key identifier of the shipments delivery method. |
| `DeliveryTermId` | `Int64?` | yes | [DeliveryTerms](../Common/DeliveryTerm.md) |  | The business key identifier of the shipments delivery term. |
| `DeliveryTermStandardCode` | `String` | no |  | max length 10 | The delivery term standard code of the shipment. |
| `DeliveryTermLocation` | `String` | no |  | max length 80 | The delivery term location of the shipment. |
| `ShippingAgentType` | `Int32` | no |  | enum | The shipping agent type of the shipment. |
| `ShipmentPayer` | `Int32` | no |  | enum | The shipment payer of the shipment. |
| `ShipmentPayerReference` | `String` | no |  | max length 80 | The shipment payer reference of the shipment. |
| `TransportDate` | `DateTimeOffset` | no |  |  | The transport date of the shipment. |
| `StoredShipment` | `Boolean` | no |  |  | Indicates if the shipment is stored. |
| `PickupDate` | `DateTimeOffset?` | yes |  |  | The pickup date of the shipment. |
| `PickupTimeFrom` | `DateTimeOffset?` | yes |  |  | The pickup time from of the shipment. |
| `PickupTimeTo` | `DateTimeOffset?` | yes |  |  | The pickup time to of the shipment. |
| `ExportDate` | `DateTimeOffset?` | yes |  |  | The export date of the shipment. |
| `DeliveryDate` | `DateTimeOffset?` | yes |  |  | The delivery date of the shipment. |
| `DeliveryTime` | `DateTimeOffset?` | yes |  |  | The delivery time of the shipment. |
| `PickupText1` | `String` | no |  | max length 50 | The first pickup text of the shipment. |
| `PickupMisc` | `String` | no |  | max length 50 | The pickup misc. text of the shipment. |
| `SchenkerOpalNumber` | `String` | no |  | max length 50 | The Schenker opal number of the shipment. |
| `IsConsolidated` | `Boolean` | no |  |  | Indicates if the shipment is consolidated. |
| `ConsolidateKey` | `String` | no |  | max length 80 | The consolidate key of the shipment. |
| `TotalEurPallets` | `Int32` | no |  |  | The total number of euro pallets on the shipment. |
| `CurrentInformationSourceType` | `Int32` | no |  | enum | The current shipment information source type of the shipment. |
| `Status` | `Int32` | no |  | enum | The status of the shipment. |
| `ShippingAgentId` | `Int64` | no | [Suppliers](../Purchase/Supplier.md) |  | The business key identifier of the shipping agent of the shipment. |
| `RecipientAdressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the recipient adress of the shipment. |
| `RecipientAdress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The recipient adress of the shipment. |
| `RecipientInvoiceAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the recipient invoice adress of the shipment. |
| `RecipientInvoiceAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The recipient invoice adress of the shipment. |
| `FreightPayerAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of the freight payer adress of the shipment. |
| `FreightPayerAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | The freight payer adress of the shipment. |
| `ConsignmentId` | `String` | no |  | max length 25 | The consignment id of the shipment. |
| `ConsignmentIdForReturn` | `String` | no |  | max length 25 | The consignment id for return of the shipment. |
| `OurReferenceName` | `String` | no |  | max length 80 | Our reference name of the shipment. |
| `OurReferencePhoneNumber` | `String` | no |  | max length 80 | Our reference phone number of the shipment. |
| `OurReferenceMobilePhoneNumber` | `String` | no |  | max length 80 | Our reference mobile phone number of the shipment. |
| `OurReferenceMail` | `String` | no |  | max length 80 | Our reference mail of the shipment. |
| `OurPickUpAddressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of our pick up address of the shipment. |
| `OurPickUpAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | Our pick up adress of the shipment. |
| `OurInvoiceAdressId` | `Int64?` | yes | [Addresses](../Common/Address.md) |  | The business key identifier of our invoce address of the shipment. |
| `OurInvoiceAddress` | `Addresses` | no | [Addresses](../Common/Address.md) | expandable | Our invoice adress of the shipment. |
| `PalletRegistrationNo` | `String` | no |  | max length 35 | The pallet registration number of the shipment. |
| `OurPalletRegistrationNo` | `String` | no |  | max length 35 | Our pallet registration number of the shipment. |
| `BusinessContactReferenceName` | `String` | no |  | max length 80 | The business contact reference name of the shipment. |
| `BusinessContactReferencePhoneNumber` | `String` | no |  | max length 80 | The business contact reference phone number of the shipment. |
| `BusinessContactReferenceMobilePhoneNumber` | `String` | no |  | max length 80 | The business contact reference mobile phone number of the shipment. |
| `BusinessContactReferenceMail` | `String` | no |  | max length 80 | The business contact reference mail of the shipment. |
| `ShippingTemplate` | `String` | no |  | max length 35 | The shipping template code of the shipment. |
| `ShippingTemplateId` | `Int64?` | yes | [ShippingTemplates](ShippingTemplate.md) |  | The business key identifier of the shipping template of the shipment. |
| `ShippingServiceId` | `Int64?` | yes | [ShippingServices](ShippingService.md) |  | The business key identifier of shipping service of the shipment. |
| `ShippingService` | `ShippingServices` | no | [ShippingServices](ShippingService.md) | expandable | The shipping service of the shipment. |
| `ShippingServiceCode` | `String` | no |  | max length 35 | The shipping service code of the shipment. |
| `SenderQuickId` | `String` | no |  | max length 30 | The sender quick id of the shipment. |
| `SellerQuickId` | `String` | no |  | max length 30 | The seller quick id of the shipment. |
| `ConsignorId` | `String` | no |  | max length 30 | The consignor id of the shipment. |
| `PickupId` | `String` | no |  | max length 30 | The pickup id of the shipment. |
| `LogTradePrintQueue` | `String` | no |  | max length 25 | The log trade print queue of the shipment. |
| `ShippingAgentCode` | `String` | no |  | max length 15 | The shipping agent code of the shipment. |
| `SenderReference` | `String` | no |  | max length 35 | The sender reference of the shipment. |
| `RecipientReference` | `String` | no |  | max length 35 | The recipient reference of the shipment. |
| `DeliveryInstruction` | `String` | no |  | max length 80 | The delivery instruction of the shipment. |
| `BookTransport` | `Boolean` | no |  |  | Indicates if the shipment has booked transport. |
| `ReturnLabel` | `Boolean` | no |  |  | Indicates if the shipment has return label. |
| `ShipmentPrintSetting` | `Int32` | no |  | enum | The print setting of the shipment. |
| `ActiveDeliveryAddressCustomerId` | `Int64?` | yes | [Customers](Customer.md) |  | The business key identifier of the active delivery address customer of the shipment. |
| `ActiveDeliveryAddressSupplierId` | `Int64?` | yes | [Suppliers](../Purchase/Supplier.md) |  | The business key identifier of the active delivery address supplier of the shipment. |
| `ActiveDeliveryAddressCompanyId` | `Int64?` | yes |  |  | The business key identifier of the active delivery address company of the shipment. |
| `ActiveDeliveryAddressDeliveryAddressId` | `Int64?` | yes | [DeliveryAddresses](../Common/DeliveryAddress.md) |  | The business key identifier of the active delivery address delivery address of the shipment. |
| `ActiveDeliveryAddressDeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](../Common/DeliveryAddress.md) | expandable | The active delivery address delivery address of the shipment. |
| `ActiveFallbackDeliveryAddressDeliveryAddressId` | `Int64?` | yes | [DeliveryAddresses](../Common/DeliveryAddress.md) |  | The business key identifier of the active fallback delivery address delivery address of the shipment. |
| `ActiveFallbackDeliveryAddressDeliveryAddress` | `DeliveryAddresses` | no | [DeliveryAddresses](../Common/DeliveryAddress.md) | expandable | The active fallback delivery address delivery address of the shipment. |
| `SourceOfAlternativeDeliveryAddresses` | `Int32` | no |  | enum | The source of alternative delivery addresses of the shipment. |
| `WarehouseShippingAgentCode` | `String` | no |  | max length 20 | The warehouse shipping agent code of the shipment. |
| `CustomerGoodsAddressNumber` | `String` | no |  | max length 80 | The customer goods address number of the shipment. |
| `CustomerShippingAgentCode` | `String` | no |  | max length 20 | The customer shipping agent code of the shipment. |
| `WarehouseId` | `Int64` | no | [Warehouses](../Common/Warehouse.md) |  | The business key identifier of the shipments warehouse. |
| `ShippingAgentAccountName` | `String` | no |  | max length 35 | The shipping agent account name of the shipment. |
| `CalculatedFreightPrice` | `Decimal?` | yes |  |  | The calculated freight price of the shipment. |
| `CalculatedFreightPriceCurrencyId` | `Int64?` | yes | [Currencies](../Common/Currency.md) |  | The business key identifier of the calculated freight price currency of the shipment. |
| `CalculatedFreightPriceCurrency` | `Currencies` | no | [Currencies](../Common/Currency.md) | expandable | The calculated freight price currency of the shipment. |
| `MobilePhoneNotificationNumber` | `String` | no |  | max length 35 | The mobile phone notification number for phone advice of the shipment. |
| `GoodsTrackingUrl` | `String` | no |  | max length 4000, since 24.7 | The goods tracking URL of the shipment. |
| `CustomsId` | `Int64?` | yes |  | since 26.4 | The business key identifier of the customs information of the shipment. |
| `Customs` | `ShipmentCustoms` | no | [ShipmentCustoms](ShipmentCustoms.md) | expandable, since 26.4 | The customs information of the shipment. |

## Enumerations

### ShippingAgentType

| Name | Value |
| --- | ---: |
| `Other` | 0 |
| `DHL` | 1 |
| `Schenker` | 2 |
| `PostNord` | 3 |
| `DSV` | 4 |

### ShipmentPayer

| Name | Value |
| --- | ---: |
| `BuyerPays` | 1 |
| `SellerPays` | 2 |
| `OtherPayer` | 3 |
| `Incoterms` | 4 |

### CurrentInformationSourceType

| Name | Value |
| --- | ---: |
| `CustomerOrder` | 0 |
| `Supplier` | 1 |
| `PickingList` | 2 |
| `Customer` | 3 |
| `PickingListWithPackageStructure` | 4 |
| `Subcontract` | 5 |
| `ReturnOrder` | 6 |

### Status

| Name | Value |
| --- | ---: |
| `Registered` | 1 |
| `ShipmentFailed` | 2 |
| `ShipmentInformationNotSufficient` | 3 |
| `Sent` | 4 |
| `Booked` | 5 |
| `Shipped` | 6 |
| `Cancelled` | 7 |

### ShipmentPrintSetting

| Name | Value |
| --- | ---: |
| `WaybillAndParcel` | 0 |
| `Waybill` | 1 |
| `Parcel` | 2 |

### SourceOfAlternativeDeliveryAddresses

| Name | Value |
| --- | ---: |
| `CurrentCustomer` | 0 |
| `Customer` | 1 |
| `Supplier` | 2 |
| `Company` | 3 |
| `CurrentSupplier` | 4 |


## Referenced by

**Sales**

- [ShipmentCustoms](ShipmentCustoms.md) — `ParentId` (FK)
- [ShipmentInformationSources](ShipmentInformationSource.md) — `ShipmentId` (FK)
- [ShipmentPackageInformations](ShipmentPackageInformation.md) — `ShipmentId` (FK)


## Example

```json
{
  "Id": 0,
  "ShipmentNumber": null,
  "ConsignmentNo": null,
  "UnifaunOnlineFirstParcelNo": null,
  "UnifaunOnlineFirstPrintLink": null,
  "LogTradeTrackingNo": null,
  "DeliveryMethodId": null,
  "DeliveryTermId": null,
  "DeliveryTermStandardCode": null,
  "DeliveryTermLocation": null,
  "ShippingAgentType": 0,
  "ShipmentPayer": 0,
  "ShipmentPayerReference": null,
  "TransportDate": "0001-01-01T00:00:00+00:00",
  "StoredShipment": false,
  "PickupDate": null,
  "PickupTimeFrom": null,
  "PickupTimeTo": null,
  "ExportDate": null,
  "DeliveryDate": null,
  "DeliveryTime": null,
  "PickupText1": null,
  "PickupMisc": null,
  "SchenkerOpalNumber": null,
  "IsConsolidated": false,
  "ConsolidateKey": null,
  "TotalEurPallets": 0,
  "CurrentInformationSourceType": 0,
  "Status": 0,
  "ShippingAgentId": 0,
  "RecipientAdressId": null,
  "RecipientAdress": null,
  "RecipientInvoiceAddressId": null,
  "RecipientInvoiceAddress": null,
  "FreightPayerAddressId": null,
  "FreightPayerAddress": null,
  "ConsignmentId": null,
  "ConsignmentIdForReturn": null,
  "OurReferenceName": null,
  "OurReferencePhoneNumber": null,
  "OurReferenceMobilePhoneNumber": null,
  "OurReferenceMail": null,
  "OurPickUpAddressId": null,
  "OurPickUpAddress": null,
  "OurInvoiceAdressId": null,
  "OurInvoiceAddress": null,
  "PalletRegistrationNo": null,
  "OurPalletRegistrationNo": null,
  "BusinessContactReferenceName": null,
  "BusinessContactReferencePhoneNumber": null,
  "BusinessContactReferenceMobilePhoneNumber": null,
  "BusinessContactReferenceMail": null,
  "ShippingTemplate": null,
  "ShippingTemplateId": null,
  "ShippingServiceId": null,
  "ShippingService": null,
  "ShippingServiceCode": null,
  "SenderQuickId": null,
  "SellerQuickId": null,
  "ConsignorId": null,
  "PickupId": null,
  "LogTradePrintQueue": null,
  "ShippingAgentCode": null,
  "SenderReference": null,
  "RecipientReference": null,
  "DeliveryInstruction": null,
  "BookTransport": false,
  "ReturnLabel": false,
  "ShipmentPrintSetting": 0,
  "ActiveDeliveryAddressCustomerId": null,
  "ActiveDeliveryAddressSupplierId": null,
  "ActiveDeliveryAddressCompanyId": null,
  "ActiveDeliveryAddressDeliveryAddressId": null,
  "ActiveDeliveryAddressDeliveryAddress": null,
  "ActiveFallbackDeliveryAddressDeliveryAddressId": null,
  "ActiveFallbackDeliveryAddressDeliveryAddress": null,
  "SourceOfAlternativeDeliveryAddresses": 0,
  "WarehouseShippingAgentCode": null,
  "CustomerGoodsAddressNumber": null,
  "CustomerShippingAgentCode": null,
  "WarehouseId": 0,
  "ShippingAgentAccountName": null,
  "CalculatedFreightPrice": null,
  "CalculatedFreightPriceCurrencyId": null,
  "CalculatedFreightPriceCurrency": null,
  "MobilePhoneNotificationNumber": null,
  "GoodsTrackingUrl": null,
  "CustomsId": null,
  "Customs": null
}
```
