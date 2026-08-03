---
type: API Entity
title: Calendars
description: Represents a queryable calendar.
resource: https://api.monitor.se/api/Monitor.API.Common.Calendar.html
tags:
- Common
- queryable
status: stable
generated:
  by: process:monitor-okf-build
  from: 677a27684767
sources:
- resource: https://api.monitor.se/api/Monitor.API.Common.Calendar.html
  title: Monitor API — Calendar
module: Common
api_class: Calendar
doc_name: Calendars
endpoint: GET /api/v1/Common/Calendars
guid: 6898DA90-2A68-4120-AC49-CE3839DE6AEC
permission: Show calendar
introduced_in: '2.18'
property_count: 5
referenced_by:
- /entities/Common/Warehouse.md
---

# Calendars

Represents a queryable calendar.

- **Module:** [Common](../../modules/Common.md)
- **API class:** `Calendar`
- **Endpoint:** `GET /api/v1/Common/Calendars`
- **Required permission:** Show calendar
- **GUID:** `6898DA90-2A68-4120-AC49-CE3839DE6AEC`
- **Introduced in:** 2.18

## Properties

| Property | Type | Null | References | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  |  | The business key identifier of the calendar. |
| `CalendarType` | `Int32` | no |  | enum | The type of the calendar. |
| `HolidayType` | `Int32` | no |  | bitmask, enum | The holiday type of the calendar. |
| `Description` | `String` | no |  |  | The translated description of the calendar. |
| `Code` | `String` | no |  | unique, max length 6 | The human readable code of the calendar. |

## Enumerations

### CalendarType

| Name | Value |
| --- | ---: |
| `NoHoliday` | 0 |
| `Weekend` | 1 |
| `OnlySundayWeekend` | 2 |
| `Swedish` | 10 |
| `Norwegian` | 11 |
| `Estonian` | 12 |
| `Finnish` | 13 |
| `German` | 14 |
| `Hungarian` | 15 |
| `Latvian` | 16 |
| `Polish` | 17 |
| `Russian` | 18 |
| `Lithuanian` | 19 |
| `Usa` | 20 |
| `Danish` | 21 |
| `Andorra` | 22 |
| `UnitedArabEmirates` | 23 |
| `Afghanistan` | 24 |
| `AntiguaBarbuda` | 25 |
| `Albania` | 26 |
| `Armenia` | 27 |
| `Angola` | 28 |
| `Argentina` | 29 |
| `AmericanSamoa` | 30 |
| `Austria` | 31 |
| `Australia` | 32 |
| `Aruba` | 33 |
| `Azerbaijan` | 34 |
| `BosniaHerzegovina` | 35 |
| `Barbados` | 36 |
| `Bangladesh` | 37 |
| `Belgium` | 38 |
| `BurkinaFaso` | 39 |
| `Bulgaria` | 40 |
| `Bahrain` | 41 |
| `Burundi` | 42 |
| `Brunei` | 43 |
| `Bolivia` | 44 |
| `Brazil` | 45 |
| `Bahamas` | 46 |
| `Botswana` | 47 |
| `Belarus` | 48 |
| `Belize` | 49 |
| `Canada` | 50 |
| `CongoBrazzaville` | 51 |
| `Switzerland` | 52 |
| `CotedIvoire` | 53 |
| `Chile` | 54 |
| `Cameroon` | 55 |
| `China` | 56 |
| `Colombia` | 57 |
| `CostaRica` | 58 |
| `Cuba` | 59 |
| `Curacao` | 60 |
| `Cyprus` | 61 |
| `CzechRepublic` | 62 |
| `Djibouti` | 63 |
| `Dominica` | 64 |
| `DominicanRepublic` | 65 |
| `Algeria` | 66 |
| `Ecuador` | 67 |
| `Egypt` | 68 |
| `Spain` | 69 |
| `Ethiopia` | 70 |
| `Fiji` | 71 |
| `France` | 72 |
| `Gabon` | 73 |
| `UnitedKingdom` | 74 |
| `Georgia` | 75 |
| `Guernsey` | 76 |
| `Ghana` | 77 |
| `Greenland` | 78 |
| `Guinea` | 79 |
| `Greece` | 80 |
| `Guatemala` | 81 |
| `Guam` | 82 |
| `HongKong` | 83 |
| `Honduras` | 84 |
| `Croatia` | 85 |
| `Haiti` | 86 |
| `Indonesia` | 87 |
| `Ireland` | 88 |
| `Israel` | 89 |
| `IsleofMan` | 90 |
| `India` | 91 |
| `Iran` | 92 |
| `Iceland` | 93 |
| `Italy` | 94 |
| `Jersey` | 95 |
| `Jamaica` | 96 |
| `Jordan` | 97 |
| `Japan` | 98 |
| `Kenya` | 99 |
| `Kyrgyzstan` | 100 |
| `Cambodia` | 101 |
| `SaintKittsNevis` | 102 |
| `SouthKorea` | 103 |
| `Kuwait` | 104 |
| `Kazakhstan` | 105 |
| `Laos` | 106 |
| `SaintLucia` | 107 |
| `Liechtenstein` | 108 |
| `SriLanka` | 109 |
| `Lesotho` | 110 |
| `Luxembourg` | 111 |
| `Morocco` | 112 |
| `Monaco` | 113 |
| `Moldova` | 114 |
| `Montenegro` | 115 |
| `Madagascar` | 116 |
| `MarshallIslands` | 117 |
| `NorthMacedonia` | 118 |
| `Macau` | 119 |
| `NorthernMarianaIslands` | 120 |
| `Mauritania` | 121 |
| `Malta` | 122 |
| `Maldives` | 123 |
| `Malawi` | 124 |
| `Mexico` | 125 |
| `Malaysia` | 126 |
| `Mozambique` | 127 |
| `Namibia` | 128 |
| `Nigeria` | 129 |
| `Nicaragua` | 130 |
| `Netherlands` | 131 |
| `NewZealand` | 132 |
| `Oman` | 133 |
| `Panama` | 134 |
| `Peru` | 135 |
| `PapuaNewGuinea` | 136 |
| `Philippines` | 137 |
| `Pakistan` | 138 |
| `PuertoRico` | 139 |
| `Portugal` | 140 |
| `Palau` | 141 |
| `Paraguay` | 142 |
| `Qatar` | 143 |
| `Romania` | 144 |
| `Serbia` | 145 |
| `SaudiArabia` | 146 |
| `Seychelles` | 147 |
| `Singapore` | 148 |
| `Slovenia` | 149 |
| `Slovakia` | 150 |
| `SierraLeone` | 151 |
| `SanMarino` | 152 |
| `Surinam` | 153 |
| `SaoTomePrincipe` | 154 |
| `ElSalvador` | 155 |
| `Eswatini` | 156 |
| `Chad` | 157 |
| `FrenchSouthernTerritories` | 158 |
| `Thailand` | 159 |
| `EastTimor` | 160 |
| `Tunisia` | 161 |
| `Tonga` | 162 |
| `Turkiye` | 163 |
| `TrinidadTobago` | 164 |
| `Tuvalu` | 165 |
| `Taiwan` | 166 |
| `Tanzania` | 167 |
| `Ukraine` | 168 |
| `UnitedStatesMinorOutlyingIslands` | 169 |
| `Uruguay` | 170 |
| `Uzbekistan` | 171 |
| `VaticanCity` | 172 |
| `Venezuela` | 173 |
| `UnitedStatesVirginIslands` | 174 |
| `Vietnam` | 175 |
| `Vanuatu` | 176 |
| `Samoa` | 177 |
| `SouthAfrica` | 178 |
| `Zambia` | 179 |
| `Zimbabwe` | 180 |

### HolidayType (bitmask — values combine)

| Name | Value |
| --- | ---: |
| `None` | 0 |
| `Weekend` | 1 |
| `Holiday` | 2 |
| `All` | 3 |


## Referenced by

**Common**

- [Warehouses](Warehouse.md) — `Calendar` (expand)
- [Warehouses](Warehouse.md) — `CalendarId` (FK)


## Example

```json
{
  "Id": 0,
  "CalendarType": 0,
  "HolidayType": 0,
  "Description": null,
  "Code": null
}
```
