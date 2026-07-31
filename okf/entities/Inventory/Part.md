---
type: API Entity
title: Parts
description: Represents a part.
resource: https://api.monitor.se/api/Monitor.API.Inventory.Part.html
tags:
- Inventory
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Inventory.Part.html
  title: Monitor API — Part
module: Inventory
api_class: Part
doc_name: Parts
endpoint: GET /api/v1/Inventory/Parts
guid: 6B6B98DA-21A0-4CA4-9B88-21631C6EA572
permission: Show part
introduced_in: '2.18'
property_count: 138
references_out:
- /entities/Common/ApplicationUser.md
- /entities/Common/BusinessContactNoteHistory.md
- /entities/Common/Comment.md
- /entities/Common/Country.md
- /entities/Common/Currency.md
- /entities/Common/ExtraField.md
- /entities/Common/PartConfigurationTemplate.md
- /entities/Common/PartUnitUsage.md
- /entities/Common/Person.md
- /entities/Common/ProductGroup.md
- /entities/Common/Project.md
- /entities/Common/Revision.md
- /entities/Common/StatisticalGoodsCode.md
- /entities/Common/Unit.md
- /entities/Common/VatRate.md
- /entities/Common/Warehouse.md
- /entities/Inventory/Alloy.md
- /entities/Inventory/GoodsType.md
- /entities/Inventory/HyperLink.md
- /entities/Inventory/OrderQuantityTemplate.md
- /entities/Inventory/PackageType.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartActivity.md
- /entities/Inventory/PartCode.md
- /entities/Inventory/PartLocation.md
- /entities/Inventory/PartOtherIdentity.md
- /entities/Inventory/PartPlanningInformation.md
- /entities/Inventory/PartPurchaseControlDataRow.md
- /entities/Inventory/PartTemplate.md
- /entities/Inventory/ProfitMarkup.md
- /entities/Inventory/SalesOverheadMarkup.md
- /entities/Inventory/StorageOverheadMarkup.md
- /entities/Manufacturing/Drawing.md
- /entities/Manufacturing/Preparation.md
- /entities/Purchase/SupplierPartLink.md
- /entities/Sales/CustomerPartLink.md
referenced_by:
- /entities/Common/FormTemplateRow.md
- /entities/Common/PartConfigurationResult.md
- /entities/Common/PartConfigurationSelectionGroupResult.md
- /entities/Common/PartUnitUsage.md
- /entities/Common/PartialQuantity.md
- /entities/Common/PaymentPlanTemplateRow.md
- /entities/Common/Revision.md
- /entities/Common/StaggeredPrice.md
- /entities/Inventory/Alloy.md
- /entities/Inventory/AlloyQuantity.md
- /entities/Inventory/CaseEntry.md
- /entities/Inventory/CaseEntryAdditionalCost.md
- /entities/Inventory/CasePartLink.md
- /entities/Inventory/HyperLink.md
- /entities/Inventory/Location.md
- /entities/Inventory/Part.md
- /entities/Inventory/PartActivity.md
- /entities/Inventory/PartDefaultTransportLabel.md
- /entities/Inventory/PartImage.md
- /entities/Inventory/PartLocation.md
- /entities/Inventory/PartOtherIdentity.md
- /entities/Inventory/PartPurchaseControlDataRow.md
- /entities/Inventory/PhysicalInventoryRow.md
- /entities/Inventory/PriceChangeLog.md
- /entities/Inventory/ProductRecord.md
- /entities/Inventory/QuantityChange.md
- /entities/Inventory/SalesForecastRow.md
- /entities/Inventory/StockTransaction.md
- /entities/Manufacturing/Drawing.md
- /entities/Manufacturing/MaintenanceReportingRow.md
- /entities/Manufacturing/ManufacturingOrder.md
- /entities/Manufacturing/ManufacturingOrderMaterial.md
- /entities/Manufacturing/ManufacturingOrderNode.md
- /entities/Manufacturing/ManufacturingOrderOperation.md
- /entities/Purchase/BlanketOrderPurchaseRow.md
- /entities/Purchase/InquiryRow.md
- /entities/Purchase/PurchaseOrderRow.md
- /entities/Purchase/SupplierPartLink.md
- /entities/Sales/BlanketOrderSalesRow.md
- /entities/Sales/CustomerOrderPaymentPlanRow.md
- /entities/Sales/CustomerOrderRow.md
- /entities/Sales/CustomerOrderRowInflow.md
- /entities/Sales/CustomerOrderShippingInformationRow.md
- /entities/Sales/CustomerPartLink.md
- /entities/Sales/InvoiceLog.md
- /entities/Sales/PackageRow.md
- /entities/Sales/QuoteRow.md
- /entities/Sales/SalesAgreementBasisRow.md
- /entities/Sales/SalesAgreementRow.md
- /entities/Sales/SalesAgreementRowInflow.md
- /entities/Sales/SalesPickingListRowQuantity.md
- /entities/Sales/SalesPrice.md
---

# Parts

Represents a part.

- **Module:** [Inventory](/modules/Inventory.md)
- **API class:** `Part`
- **Endpoint:** `GET /api/v1/Inventory/Parts`
- **Required permission:** Show part
- **GUID:** `6B6B98DA-21A0-4CA4-9B88-21631C6EA572`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the part. |
| `PartNumber` | `String` | no |  | unique, max length 20 | The human readable identifier of the part. |
| `Description` | `String` | no |  |  | The translated description of the part. |
| `ExtraDescription` | `String` | no |  |  | The translated extra description of the part. |
| `CompanyId` | `Int64` | no |  |  | The business key identifier of the company that the part is defined for. |
| `Length` | `Decimal?` | yes |  |  | The physical length of the part in metres. |
| `Width` | `Decimal?` | yes |  |  | The physical width of the part in metres. |
| `Height` | `Decimal?` | yes |  |  | The physical height of the part in metres. |
| `PackagingType` | `Int32` | no |  | enum | The packaging type that the part specifies. |
| `PackageVolumeConsistsOf` | `Int32` | no |  | enum | Specifies how package volume of the part has been specified. |
| `PackageTypeId` | `Int64?` | yes | [PackageTypes](/entities/Inventory/PackageType.md) |  | The business key identifier of the package type specified by the part. |
| `PackageType` | `PackageTypes` | no | [PackageTypes](/entities/Inventory/PackageType.md) | expandable | The package type specified by the part. |
| `PartPlanningInformations` | `PartPlanningInformation[]` | no | [PartPlanningInformation](/entities/Inventory/PartPlanningInformation.md) | expandable, collection | A collection of part planning information for the part. |
| `UseRandomLocationStorage` | `Boolean` | no |  |  | Specifies if the part employs random location storage. |
| `ShowFictiousStructureOnOrderRegistration` | `Boolean` | no |  |  | Specifies if the part should show its fictitious structure when registering orders. |
| `TraceabilityMode` | `Int32` | no |  | enum | The traceability mode that is employed by the part. |
| `UseBestBeforeDate` | `Boolean` | no |  | since 2.40 | Specifies whether or not best before date applies to the part. |
| `DaysToAddToBestBeforeDate` | `Int32?` | yes |  | since 2.40 | Days to use when best before date is active. |
| `SuggestBestBeforeDate` | `Int32` | no |  | enum, since 2.40 | Specifies whether or not a best before date should be suggested for the part. |
| `ManageStockBalance` | `Boolean` | no |  |  | Specifies if stock balance management is enabled for the part. |
| `StandardPrice` | `Decimal` | no |  |  | The standard price of the part. |
| `StandardPriceCurrencyId` | `Int64` | no | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency that the standard price is specified in. |
| `FutureStandardPrice` | `Decimal?` | yes |  |  | The future standard price of the part. |
| `FutureStandardPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency that the future standard price is specified in. |
| `PostCalculatedAveragePrice` | `Decimal?` | yes |  |  | The post calculated average price of the part. |
| `PostCalculatedAveragePriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency that the post calculated average price is specified in. |
| `Type` | `Int32` | no |  | enum | The part type. |
| `ProductGroupId` | `Int64` | no | [ProductGroups](/entities/Common/ProductGroup.md) |  | The business key identifier of the product group that the part belongs to. |
| `ProductGroup` | `ProductGroups` | no | [ProductGroups](/entities/Common/ProductGroup.md) | expandable | The product group that the part belongs to. |
| `WeightPerUnit` | `Decimal?` | yes |  |  | The weight of the part per unit in kilograms. |
| `StatisticalGoodsCodeId` | `Int64?` | yes | [StatisticalGoodsCodes](/entities/Common/StatisticalGoodsCode.md) |  | The business key identifier of the statistical goods code that the part is organized under. References a StatisticalGoodsCodes |
| `StatisticalGoodsCode` | `StatisticalGoodsCodes` | no | [StatisticalGoodsCodes](/entities/Common/StatisticalGoodsCode.md) | expandable | The statistical goods code that the part is organized under. |
| `StatisticalGoodsValue` | `Decimal?` | yes |  |  | The statistical goods value of the part. |
| `CountryOfOriginId` | `Int64?` | yes | [Countries](/entities/Common/Country.md) |  | The business key identifier of the part's country of origin. |
| `CountryOfOrigin` | `Countries` | no | [Countries](/entities/Common/Country.md) | expandable | The part's country of origin. |
| `PartCodeId` | `Int64?` | yes | [PartCodes](/entities/Inventory/PartCode.md) |  | The business key identifier of the part's part code. |
| `PartCode` | `PartCodes` | no | [PartCodes](/entities/Inventory/PartCode.md) | expandable | The part's part code. |
| `CategoryString` | `String` | no |  |  | The category of the part. |
| `StorageOverheadMarkupId` | `Int64` | no | [StorageOverheadMarkups](/entities/Inventory/StorageOverheadMarkup.md) |  | The business key identifier of the storage overhead markup of the part. |
| `StorageOverheadMarkup` | `StorageOverheadMarkups` | no | [StorageOverheadMarkups](/entities/Inventory/StorageOverheadMarkup.md) | expandable | The storage overhead markup of the part. |
| `SalesOverheadMarkupId` | `Int64` | no | [SalesOverheadMarkups](/entities/Inventory/SalesOverheadMarkup.md) |  | The business key identifier of the sales overhead markup of the part. |
| `SalesOverheadMarkup` | `SalesOverheadMarkups` | no | [SalesOverheadMarkups](/entities/Inventory/SalesOverheadMarkup.md) | expandable | The sales overhead markup of the part. |
| `ProfitMarkupId` | `Int64` | no | [ProfitMarkups](/entities/Inventory/ProfitMarkup.md) |  | The business key identifier of the part's profit markup. |
| `ProfitMarkup` | `ProfitMarkups` | no | [ProfitMarkups](/entities/Inventory/ProfitMarkup.md) | expandable | The part's profit markup. |
| `VolumePerUnit` | `Decimal?` | yes |  |  | The volume per unit of the part in cubic metres. |
| `AveragePrice` | `Decimal?` | yes |  |  | The average price of the part. |
| `AveragePriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency that the part's average price is specified in. |
| `LastPurchasePrice` | `Decimal?` | yes |  |  | The last purchase price of the part. |
| `LastPurchasePriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the part's last purchase price. |
| `AveragePriceTimestamp` | `DateTimeOffset?` | yes |  |  | The timestamp of the part's average price. |
| `PurchaseLabelType` | `Int32` | no |  | enum | The type of transport label that is used for the part when purchasing. |
| `CurrentAlloyId` | `Int64?` | yes | [Alloys](/entities/Inventory/Alloy.md) |  | The business key identifier of the current part alloy. |
| `CurrentAlloy` | `Alloys` | no | [Alloys](/entities/Inventory/Alloy.md) | expandable | The part's current alloy. |
| `PurchaseQuantityPerPackage` | `Decimal?` | yes |  |  | The quantity per package of the part when purchasing. |
| `IsPackaging` | `Boolean` | no |  |  | Specifies if the part is used for packaging. |
| `Status` | `Int32` | no |  | enum | The status of the part. |
| `PurchaseAndManufactureOnProject` | `Int32` | no |  | enum | Specifies if the part is purchased and manufactured on a project. |
| `ServiceType` | `Int32` | no |  | enum | The service type of the part. |
| `QuantityPerPackage` | `Decimal?` | yes |  |  | The quantity per package of the part. |
| `PackagingWeightPerPackage` | `Decimal?` | yes |  |  | The packaging weight per package. |
| `PackagingPartId` | `Int64?` | yes | [Parts](/entities/Inventory/Part.md) |  | The business key identifier of the packaging part used for this part. |
| `PackagingPart` | `Parts` | no | [Parts](/entities/Inventory/Part.md) | expandable | The packaging part used for this part. |
| `LoadingMetersPerUnit` | `Decimal?` | yes |  |  | The loading metres per unit. |
| `PackingReference` | `String` | no |  |  | The packing reference of the part. |
| `Gs1Code` | `String` | no |  | max length 35 | The GS1 code of the part. |
| `VatRateId` | `Int64?` | yes | [VatRates](/entities/Common/VatRate.md) |  | The business key identifier of the part's VAT rate. |
| `VatRate` | `VatRates` | no | [VatRates](/entities/Common/VatRate.md) |  | The part's VAT rate. |
| `LastSalesPrice` | `Decimal?` | yes |  |  | The last sales price of the part. |
| `LastSalesPriceCurrencyId` | `Int64?` | yes | [Currencies](/entities/Common/Currency.md) |  | The business key identifier of the currency that the last sales price was specified in. |
| `TransportCost` | `Decimal?` | yes |  |  | The transport cost of the part. |
| `SerialNumberGeneration` | `Int32` | no |  | enum | The serial number generation method of the part. |
| `SerialNumberGenerationSource` | `Int32` | no |  | enum | The serial number generation source of the part. |
| `GoodsType` | `String` | no |  | max length 35 | The goods type of the part. |
| `LeadTimeToCustomer` | `TimeSpan?` | yes |  |  | The lead time to the customer for the part. |
| `QuantityForLeadtimeToCustomer` | `Decimal?` | yes |  |  | The quantity for the lead time to the customer for the part. |
| `SalesLabelType` | `Int32` | no |  | enum | The type of transport label to use for the part when selling. |
| `DefaultCustomerOrderWarehouseId` | `Int64?` | yes | [Warehouses](/entities/Common/Warehouse.md) |  | The business key identifier of the default customer order warehouse to use for the part. |
| `ManufacturingLabelType` | `Int32` | no |  | enum | The type of transport label to use for the part when manufacturing. |
| `PreparerId` | `Int64?` | yes | [Persons](/entities/Common/Person.md) |  | The business key identifier of the person that prepares the part. |
| `Preparer` | `Persons` | no | [Persons](/entities/Common/Person.md) | expandable | The person that prepares the part. |
| `GoodsTypeId` | `Int64?` | yes | [GoodsTypes](/entities/Inventory/GoodsType.md) |  | The business key identifier of the goods type of the part. |
| `ExpGoodsType` | `GoodsTypes` | no | [GoodsTypes](/entities/Inventory/GoodsType.md) | expandable | The goods type of the part. |
| `CalculatedQuantity` | `Decimal` | no |  |  | The calculated quantity of the part. |
| `Alias` | `String` | no |  | max length 20 | The part alias. |
| `BlockedById` | `Int64?` | yes | [ApplicationUsers](/entities/Common/ApplicationUser.md) |  | The business key identifier of the application user that blocked the entity. |
| `BlockedBy` | `ApplicationUsers` | no | [ApplicationUsers](/entities/Common/ApplicationUser.md) | expandable | The application user that blocked the part. |
| `BlockedStatus` | `Int32` | no |  | enum | The block status of the entity. |
| `BlockedContextType` | `Int32` | no |  | bitmask, enum | Specifies which contexts the block applies for. |
| `BlockMessageId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The block message of the part. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |  | The date when the entity stops being blocked. |
| `ReceivingInspectionType` | `Int32` | no |  | enum | Specifies when reception inspection of the type occurs. |
| `StandardUnitId` | `Int64` | no | [Units](/entities/Common/Unit.md) |  | The business key identifier of the standard unit of the part. |
| `StandardPartUnitUsageId` | `Int64` | no | [PartUnitUsages](/entities/Common/PartUnitUsage.md) |  | The business key identifier of the standard part unit usage. |
| `StandardPartUnitUsage` | `PartUnitUsages` | no | [PartUnitUsages](/entities/Common/PartUnitUsage.md) | expandable | The standard part unit usage. |
| `PartUnitUsages` | `PartUnitUsages[]` | no | [PartUnitUsages](/entities/Common/PartUnitUsage.md) | expandable, collection, since 2.32 | A collection of part unit usages for the part. |
| `CommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the part comment. |
| `Comment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The part comment. |
| `ActiveRevisionId` | `Int64?` | yes | [Revisions](/entities/Common/Revision.md) |  | The business key identifier of the part's active revision. |
| `ActiveRevision` | `Revisions` | no | [Revisions](/entities/Common/Revision.md) | expandable | The active revision of the part. |
| `LatestCalculationId` | `Int64?` | yes |  |  | The business key identifier of the latest part calculation. |
| `ReceivingInstructionId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the receiving instruction of the part. |
| `ReceivingInstruction` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The receiving instruction of the part. |
| `PurchaseCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the part's purchase comment. |
| `PurchaseComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The purchase comment of the part. |
| `PickingInstructionId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the part's picking instruction. |
| `PickingInstruction` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The picking instruction of the part. |
| `SalesCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the part's sales comment. |
| `SalesComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The sales comment of the part. |
| `ManufacturingCommentId` | `Int64?` | yes | [Comments](/entities/Common/Comment.md) |  | The business key identifier of the part's manufacturing comment. |
| `ManufacturingComment` | `Comments` | no | [Comments](/entities/Common/Comment.md) | expandable | The manufacturing comment of the part. |
| `PreparationId` | `Int64?` | yes | [Preparations](/entities/Manufacturing/Preparation.md) |  | The business key identifier of the part's preparation. |
| `ExtraFields` | `ExtraFields[]` | no | [ExtraFields](/entities/Common/ExtraField.md) | expandable, collection | A collection of extra field values for the part. |
| `CustomerPartLinks` | `CustomerPartLinks[]` | no | [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) | expandable, collection | A collection of customer part links for the part. |
| `SupplierPartLinks` | `SupplierPartLinks[]` | no | [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) | expandable, collection | A collection of supplier part links for the part. |
| `Revisions` | `Revisions[]` | no | [Revisions](/entities/Common/Revision.md) | expandable, collection | A collection of revisions that belong to the part. |
| `Drawings` | `Drawings[]` | no | [Drawings](/entities/Manufacturing/Drawing.md) | expandable, collection | A collection of drawings that belong to the part. |
| `PartLocations` | `PartLocations[]` | no | [PartLocations](/entities/Inventory/PartLocation.md) | expandable, collection, since 2.28 | A collection of locations that belong to the part. |
| `HyperLinks` | `HyperLinks[]` | no | [HyperLinks](/entities/Inventory/HyperLink.md) | expandable, collection, since 2.55 | A collection of hyperlinks that belong to the part. |
| `PartActivities` | `PartActivities[]` | no | [PartActivities](/entities/Inventory/PartActivity.md) | expandable, collection, since 22.7 | A collection of activities that belong to the part. |
| `ConfigurationTemplateId` | `Int64?` | yes |  | since 2.33 | The business key identifier of the part configuration template that the part uses for part configuration. |
| `ConfigurationTemplate` | `PartConfigurationTemplates` | no | [PartConfigurationTemplates](/entities/Common/PartConfigurationTemplate.md) | expandable, since 22.3 | The part configuration template that the part uses for part configuration. |
| `OtherIdentities` | `PartOtherIdentities[]` | no | [PartOtherIdentities](/entities/Inventory/PartOtherIdentity.md) | expandable, collection, since 2.47 | The "other" identities of the part. |
| `Notes` | `BusinessContactNoteHistories[]` | no | [BusinessContactNoteHistories](/entities/Common/BusinessContactNoteHistory.md) | expandable, collection, since 2.55 | Rows of business contact notes. |
| `ConfigurationSelectionDescription` | `String` | no |  | since 2.55 | The selected configuration description of the part. |
| `OrderQuantityId` | `Int64?` | yes | [OrderQuantityTemplates](/entities/Inventory/OrderQuantityTemplate.md) | since 22.6 | The business key identifier of order quantity. |
| `OrderQuantity` | `OrderQuantityTemplates` | no | [OrderQuantityTemplates](/entities/Inventory/OrderQuantityTemplate.md) | expandable, since 22.6 | Order quantity template that holds the partial quantities, that acts as a default for the order equivalent order quantities. |
| `ProjectId` | `Int64?` | yes | [Projects](/entities/Common/Project.md) | since 22.7 | The business key identifier of the project that the part belongs to. |
| `PartTemplateId` | `Int64?` | yes | [PartTemplates](/entities/Inventory/PartTemplate.md) | since 23.1 | The business key identifier of the part template. |
| `PartTemplate` | `PartTemplates` | no | [PartTemplates](/entities/Inventory/PartTemplate.md) | expandable, since 23.1 | A part template information for the part. |
| `IsFixedWeight` | `Boolean` | no |  | since 23.2 | Information whether the part has a fixed weight. |
| `MaterialValidationSetting` | `Int32` | no |  | bitmask, enum, since 24.5 | The settings for serial number linked to which operation. |
| `AutomaticReportingMode` | `Int32` | no |  | bitmask, enum, since 24.6 | The automatic reporting mode that the part applies. |
| `EmissionFactorId` | `Int64?` | yes |  | since 25.7 | The business key identifier of the material type of the part. |
| `EmissionFactor` | `EmissionFactors` | no |  | expandable, since 25.7 | The emission factor for the part. |
| `Emissions` | `Decimal?` | yes |  | since 25.7 | The emission factor registered for the material type of the part. |
| `ControlDataRows` | `PartPurchaseControlDataRows[]` | no | [PartPurchaseControlDataRows](/entities/Inventory/PartPurchaseControlDataRow.md) | expandable, collection, since 26.6 | A collection of purchase control data rows for the part. |

## Enumerations

### PackagingType

| Name | Value |
| --- | ---: |
| `Unspecified` | 0 |
| `OuterPackaging` | 1 |
| `EurPallets` | 2 |
| `InnerPackaging` | 3 |
| `CoverPackaging` | 4 |

### PackageVolumeConsistsOf

| Name | Value |
| --- | ---: |
| `SurroundingPackagingVolume` | 0 |
| `PackagingVolumeAndPartVolume` | 1 |

### TraceabilityMode

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Batch` | 1 |
| `Individual` | 2 |
| `IndividualOnlyWithdrawal` | 4 |

### SuggestBestBeforeDate

| Name | Value |
| --- | ---: |
| `No` | 0 |
| `AddDays` | 1 |
| `ShortestFromReportedMaterial` | 2 |

### Type

| Name | Value |
| --- | ---: |
| `Purchased` | 0 |
| `Manufactured` | 1 |
| `Fictitious` | 2 |
| `Service` | 5 |
| `Subcontract` | 6 |

### PurchaseLabelType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Transport` | 1 |
| `Label` | 2 |
| `SmallLabel` | 3 |
| `MultiLabel` | 4 |
| `SelectAtPrintout` | 5 |

### Status

| Name | Value |
| --- | ---: |
| `Quote` | 1 |
| `Prototype` | 2 |
| `New` | 3 |
| `Normal` | 4 |
| `NewRevision` | 5 |
| `PhasingOut` | 6 |
| `Expired` | 9 |
| `Inactive` | 99 |

### PurchaseAndManufactureOnProject

| Name | Value |
| --- | ---: |
| `No` | 0 |
| `Yes` | 1 |
| `PickFromStockFirst` | 2 |

### ServiceType

| Name | Value |
| --- | ---: |
| `Unspecified` | 0 |
| `Freight` | 1 |
| `AlloyCost` | 2 |

### SerialNumberGeneration

| Name | Value |
| --- | ---: |
| `Never` | 0 |
| `CustomerOrderRegistration` | 1 |
| `ManufacturingOrderRegistration` | 2 |
| `DeliveryReporting` | 3 |

### SerialNumberGenerationSource

| Name | Value |
| --- | ---: |
| `NumberSeries` | 0 |
| `Manual` | 1 |

### SalesLabelType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Transport` | 1 |
| `Label` | 2 |
| `SmallLabel` | 3 |
| `MultiLabel` | 4 |
| `SelectAtPrintout` | 5 |

### ManufacturingLabelType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Transport` | 1 |
| `Label` | 2 |
| `SmallLabel` | 3 |
| `MultiLabel` | 4 |
| `SelectAtPrintout` | 5 |

### BlockedStatus

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Message` | 1 |
| `Blocked` | 2 |

### BlockedContextType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `RegisterManufacturingOrder` | 1 |
| `RegisterPurchaseOrder` | 2 |
| `RegisterCustomerOrder` | 4 |
| `ReportManufacturingOrder` | 8 |
| `ReportPurchaseOrder` | 16 |
| `ReportCustomerOrder` | 32 |
| `WithdrawalManufacturingOrder` | 64 |
| `Preparation` | 128 |
| `ConfigurationSelection` | 256 |
| `RegisterAgreement` | 512 |
| `RegisterBlanketOrderPurchase` | 1024 |
| `RegisterBlanketOrderSales` | 2048 |
| `RegisterQuote` | 4096 |

### ReceivingInspectionType

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Always` | 1 |
| `VariableInspection` | 2 |

### MaterialValidationSetting (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `ActualOperation` | 0 |
| `AnyOperation` | 1 |

### AutomaticReportingMode (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `PickingLocation` | 1 |
| `Cleared` | 2 |
| `BufferLocation` | 4 |
| `Project` | 8 |


## Referenced by

**Common**

- [FormTemplateRows](/entities/Common/FormTemplateRow.md) — `MasterToolId` (FK)
- [PartConfigurationResults](/entities/Common/PartConfigurationResult.md) — `MainPartId` (FK)
- [PartConfigurationSelectionGroupResults](/entities/Common/PartConfigurationSelectionGroupResult.md) — `MainPartId` (FK)
- [PartConfigurationSelectionGroupResults](/entities/Common/PartConfigurationSelectionGroupResult.md) — `PartId` (FK)
- [PartUnitUsages](/entities/Common/PartUnitUsage.md) — `PartId` (FK)
- [PartialQuantities](/entities/Common/PartialQuantity.md) — `PackagePartId` (FK)
- [PaymentPlanTemplateRows](/entities/Common/PaymentPlanTemplateRow.md) — `Part` (expand)
- [PaymentPlanTemplateRows](/entities/Common/PaymentPlanTemplateRow.md) — `PartId` (FK)
- [Revisions](/entities/Common/Revision.md) — `PartId` (FK)
- [StaggeredPrices](/entities/Common/StaggeredPrice.md) — `PartId` (FK)

**Inventory**

- [AlloyQuantities](/entities/Inventory/AlloyQuantity.md) — `PartId` (FK)
- [Alloys](/entities/Inventory/Alloy.md) — `PartId` (FK)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `Part` (expand)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `PartId` (FK)
- [CaseEntry](/entities/Inventory/CaseEntry.md) — `ReasonPartId` (FK)
- [CaseEntryAdditionalCost](/entities/Inventory/CaseEntryAdditionalCost.md) — `Part` (expand)
- [CaseEntryAdditionalCost](/entities/Inventory/CaseEntryAdditionalCost.md) — `PartId` (FK)
- [CaseEntryPartLinks](/entities/Inventory/CasePartLink.md) — `PartId` (FK)
- [HyperLinks](/entities/Inventory/HyperLink.md) — `PartId` (FK)
- [Locations](/entities/Inventory/Location.md) — `PackagingPart` (expand)
- [Locations](/entities/Inventory/Location.md) — `PackagingPartId` (FK)
- [PartActivities](/entities/Inventory/PartActivity.md) — `PartId` (FK)
- [PartDefaultTransportLabels](/entities/Inventory/PartDefaultTransportLabel.md) — `PartId` (FK)
- [PartImages](/entities/Inventory/PartImage.md) — `PartId` (FK)
- [PartLocations](/entities/Inventory/PartLocation.md) — `PartId` (FK)
- [PartOtherIdentities](/entities/Inventory/PartOtherIdentity.md) — `PartId` (FK)
- [PartPurchaseControlDataRows](/entities/Inventory/PartPurchaseControlDataRow.md) — `PartId` (FK)
- [Parts](/entities/Inventory/Part.md) — `PackagingPart` (expand)
- [Parts](/entities/Inventory/Part.md) — `PackagingPartId` (FK)
- [PhysicalInventoryRows](/entities/Inventory/PhysicalInventoryRow.md) — `PartId` (FK)
- [PriceChangeLogs](/entities/Inventory/PriceChangeLog.md) — `PartId` (FK)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `Part` (expand)
- [ProductRecords](/entities/Inventory/ProductRecord.md) — `PartId` (FK)
- [QuantityChanges](/entities/Inventory/QuantityChange.md) — `PartId` (FK)
- [SalesForecastRows](/entities/Inventory/SalesForecastRow.md) — `PartId` (FK)
- [StockTransactions](/entities/Inventory/StockTransaction.md) — `PartId` (FK)

**Manufacturing**

- [Drawings](/entities/Manufacturing/Drawing.md) — `PartId` (FK)
- [MaintenanceReportingRows](/entities/Manufacturing/MaintenanceReportingRow.md) — `MasterToolId` (FK)
- [ManufacturingOrderMaterials](/entities/Manufacturing/ManufacturingOrderMaterial.md) — `Part` (expand)
- [ManufacturingOrderMaterials](/entities/Manufacturing/ManufacturingOrderMaterial.md) — `PartId` (FK)
- [ManufacturingOrderNodes](/entities/Manufacturing/ManufacturingOrderNode.md) — `PartId` (FK)
- [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) — `Part` (expand)
- [ManufacturingOrderOperations](/entities/Manufacturing/ManufacturingOrderOperation.md) — `PartId` (FK)
- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `Part` (expand)
- [ManufacturingOrders](/entities/Manufacturing/ManufacturingOrder.md) — `PartId` (FK)

**Purchase**

- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `Part` (expand)
- [BlanketOrderPurchaseRows](/entities/Purchase/BlanketOrderPurchaseRow.md) — `PartId` (FK)
- [InquiryRows](/entities/Purchase/InquiryRow.md) — `PartId` (FK)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `Part` (expand)
- [PurchaseOrderRows](/entities/Purchase/PurchaseOrderRow.md) — `PartId` (FK)
- [SupplierPartLinks](/entities/Purchase/SupplierPartLink.md) — `PartId` (FK)

**Sales**

- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `Part` (expand)
- [BlanketOrderSalesRows](/entities/Sales/BlanketOrderSalesRow.md) — `PartId` (FK)
- [CustomerOrderPaymentPlanRows](/entities/Sales/CustomerOrderPaymentPlanRow.md) — `PartId` (FK)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `Part` (expand)
- [CustomerOrderRowInflows](/entities/Sales/CustomerOrderRowInflow.md) — `PartId` (FK)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `Part` (expand)
- [CustomerOrderRows](/entities/Sales/CustomerOrderRow.md) — `PartId` (FK)
- [CustomerOrderShippingInformationRows](/entities/Sales/CustomerOrderShippingInformationRow.md) — `PackagingPart` (expand)
- [CustomerOrderShippingInformationRows](/entities/Sales/CustomerOrderShippingInformationRow.md) — `PackagingPartId` (FK)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `PackagingPartId` (FK)
- [CustomerPartLinks](/entities/Sales/CustomerPartLink.md) — `PartId` (FK)
- [InvoiceLogs](/entities/Sales/InvoiceLog.md) — `PartId` (FK)
- [PackageRows](/entities/Sales/PackageRow.md) — `PackagingPartId` (FK)
- [QuoteRows](/entities/Sales/QuoteRow.md) — `PartId` (FK)
- [SalesAgreementBasisRows](/entities/Sales/SalesAgreementBasisRow.md) — `PartId` (FK)
- [SalesAgreementRowInflows](/entities/Sales/SalesAgreementRowInflow.md) — `PartId` (FK)
- [SalesAgreementRows](/entities/Sales/SalesAgreementRow.md) — `PartId` (FK)
- [SalesPickingListRowQuantities](/entities/Sales/SalesPickingListRowQuantity.md) — `PartId` (FK)
- [SalesPrices](/entities/Sales/SalesPrice.md) — `PartId` (FK)


## Example

```json
{
  "Id": 0,
  "PartNumber": null,
  "Description": null,
  "ExtraDescription": null,
  "CompanyId": 0,
  "Length": null,
  "Width": null,
  "Height": null,
  "PackagingType": 0,
  "PackageVolumeConsistsOf": 0,
  "PackageTypeId": null,
  "PackageType": null,
  "PartPlanningInformations": null,
  "UseRandomLocationStorage": false,
  "ShowFictiousStructureOnOrderRegistration": false,
  "TraceabilityMode": 0,
  "UseBestBeforeDate": false,
  "DaysToAddToBestBeforeDate": null,
  "SuggestBestBeforeDate": 0,
  "ManageStockBalance": false,
  "StandardPrice": 0.0,
  "StandardPriceCurrencyId": 0,
  "FutureStandardPrice": null,
  "FutureStandardPriceCurrencyId": null,
  "PostCalculatedAveragePrice": null,
  "PostCalculatedAveragePriceCurrencyId": null,
  "Type": 0,
  "ProductGroupId": 0,
  "ProductGroup": null,
  "WeightPerUnit": null,
  "StatisticalGoodsCodeId": null,
  "StatisticalGoodsCode": null,
  "StatisticalGoodsValue": null,
  "CountryOfOriginId": null,
  "CountryOfOrigin": null,
  "PartCodeId": null,
  "PartCode": null,
  "CategoryString": null,
  "StorageOverheadMarkupId": 0,
  "StorageOverheadMarkup": null,
  "SalesOverheadMarkupId": 0,
  "SalesOverheadMarkup": null,
  "ProfitMarkupId": 0,
  "ProfitMarkup": null,
  "VolumePerUnit": null,
  "AveragePrice": null,
  "AveragePriceCurrencyId": null,
  "LastPurchasePrice": null,
  "LastPurchasePriceCurrencyId": null,
  "AveragePriceTimestamp": null,
  "PurchaseLabelType": 0,
  "CurrentAlloyId": null,
  "CurrentAlloy": null,
  "PurchaseQuantityPerPackage": null,
  "IsPackaging": false,
  "Status": 0,
  "PurchaseAndManufactureOnProject": 0,
  "ServiceType": 0,
  "QuantityPerPackage": null,
  "PackagingWeightPerPackage": null,
  "PackagingPartId": null,
  "PackagingPart": null,
  "LoadingMetersPerUnit": null,
  "PackingReference": null,
  "Gs1Code": null,
  "VatRateId": null,
  "VatRate": null,
  "LastSalesPrice": null,
  "LastSalesPriceCurrencyId": null,
  "TransportCost": null,
  "SerialNumberGeneration": 0,
  "SerialNumberGenerationSource": 0,
  "GoodsType": null,
  "LeadTimeToCustomer": null,
  "QuantityForLeadtimeToCustomer": null,
  "SalesLabelType": 0,
  "DefaultCustomerOrderWarehouseId": null,
  "ManufacturingLabelType": 0,
  "PreparerId": null,
  "Preparer": null,
  "GoodsTypeId": null,
  "ExpGoodsType": null,
  "CalculatedQuantity": 0.0,
  "Alias": null,
  "BlockedById": null,
  "BlockedBy": null,
  "BlockedStatus": 0,
  "BlockedContextType": 0,
  "BlockMessageId": null,
  "BlockMessage": null,
  "BlockedFromDate": null,
  "BlockedToDate": null,
  "ReceivingInspectionType": 0,
  "StandardUnitId": 0,
  "StandardPartUnitUsageId": 0,
  "StandardPartUnitUsage": null,
  "PartUnitUsages": null,
  "CommentId": null,
  "Comment": null,
  "ActiveRevisionId": null,
  "ActiveRevision": null,
  "LatestCalculationId": null,
  "ReceivingInstructionId": null,
  "ReceivingInstruction": null,
  "PurchaseCommentId": null,
  "PurchaseComment": null,
  "PickingInstructionId": null,
  "PickingInstruction": null,
  "SalesCommentId": null,
  "SalesComment": null,
  "ManufacturingCommentId": null,
  "ManufacturingComment": null,
  "PreparationId": null,
  "ExtraFields": null,
  "CustomerPartLinks": null,
  "SupplierPartLinks": null,
  "Revisions": null,
  "Drawings": null,
  "PartLocations": null,
  "HyperLinks": null,
  "PartActivities": null,
  "ConfigurationTemplateId": null,
  "ConfigurationTemplate": null,
  "OtherIdentities": null,
  "Notes": null,
  "ConfigurationSelectionDescription": null,
  "OrderQuantityId": null,
  "OrderQuantity": null,
  "ProjectId": null,
  "PartTemplateId": null,
  "PartTemplate": null,
  "IsFixedWeight": false,
  "MaterialValidationSetting": 0,
  "AutomaticReportingMode": 0,
  "EmissionFactorId": null,
  "EmissionFactor": null,
  "Emissions": null,
  "ControlDataRows": null
}
```
