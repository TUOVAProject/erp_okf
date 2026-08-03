# TimeRecording

Monitor API module `TimeRecording`: 20 queryable entities, 0 commands, 0 payload types.

## Queryable entities

<a id="TimeRecording.AbsenceCode"></a>
### AbsenceCodes

Represents an absence code. Used in time recording to represent a period of absence.

- **Endpoint:** `GET /api/v1/TimeRecording/AbsenceCodes`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [AttendanceGroupSettings](/modules/TimeRecording.md#TimeRecording.AttendanceGroupSettings), [AttendanceIntervals](/modules/TimeRecording.md#TimeRecording.AttendanceInterval)

<a id="TimeRecording.AdditionRecording"></a>
### AdditionRecordings

Represents an additional recording

- **Endpoint:** `GET /api/v1/TimeRecording/AdditionRecordings`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AdditionType` | `Int32` | no |  |
| `AttendanceAdditionId` | `Int64` | no | [AttendanceAdditions](/modules/TimeRecording.md#TimeRecording.AttendanceAddition) |
| `AttendanceAddition` | `AttendanceAdditions` | no | [AttendanceAdditions](/modules/TimeRecording.md#TimeRecording.AttendanceAddition) |
| `TimeBankId` | `Int64?` | yes | [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank) |
| `TimeBank` | `TimeBanks` | no | [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank) |
| `TimeBankTransaction` | `Int32` | no |  |
| `MandatoryComment` | `Boolean` | no |  |
| `CommentId` | `Int64?` | yes |  |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |
| `Amount` | `Decimal` | no |  |
| `Cost` | `Decimal?` | yes |  |
| `CostCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `ProjectId` | `Int64?` | yes | [Projects](/modules/Common.md#Common.Project) |
| `IntervalStart` | `DateTimeOffset?` | yes |  |
| `IntervalEnd` | `DateTimeOffset?` | yes |  |

- `AdditionType` — Standard=0, SystemTimebankAdjustment=1
- `TimeBankTransaction` — Increase=0, Decrease=1

**References out:** [AttendanceAdditions](/modules/TimeRecording.md#TimeRecording.AttendanceAddition), [Comments](/modules/Common.md#Common.Comment), [Currencies](/modules/Common.md#Common.Currency), [Projects](/modules/Common.md#Common.Project), [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank)
**Referenced by:** [RecordingDays](/modules/TimeRecording.md#TimeRecording.RecordingDay)

<a id="TimeRecording.AttendanceAddition"></a>
### AttendanceAdditions

Represents an attendance addition

- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceAdditions`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 22.7

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `RowNumber` | `Int32` | no |  |
| `Description` | `String` | no |  |
| `AdditionType` | `Int32` | no |  |
| `IsActive` | `Boolean` | no |  |
| `EnterFromTo` | `Boolean` | no |  |
| `MandatoryComment` | `Boolean` | no |  |
| `LinkToProjectType` | `Int32` | no |  |
| `TimeBankId` | `Int64?` | yes | [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank) |
| `TimeBank` | `TimeBanks` | no | [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank) |
| `TimeBankTransaction` | `Int32` | no |  |
| `Cost` | `Decimal` | no |  |
| `CostCurrencyId` | `Int64?` | yes | [Currencies](/modules/Common.md#Common.Currency) |
| `SalaryTypes` | `SalaryTypes[]` | no | [SalaryTypes](/modules/TimeRecording.md#TimeRecording.SalaryType) |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](/modules/Common.md#Common.ProjectCostType) |
| `CostType` | `ProjectCostTypes` | no | [ProjectCostTypes](/modules/Common.md#Common.ProjectCostType) |
| `CostVisibility` | `Int32` | no |  |

- `AdditionType` — Standard=0, SystemTimebankAdjustment=1
- `LinkToProjectType` — None=0, Optional=1, Mandatory=2
- `TimeBankTransaction` — Increase=0, Decrease=1
- `CostVisibility` — No=0, Yes=1, Editable=2

**References out:** [Currencies](/modules/Common.md#Common.Currency), [ProjectCostTypes](/modules/Common.md#Common.ProjectCostType), [SalaryTypes](/modules/TimeRecording.md#TimeRecording.SalaryType), [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank)
**Referenced by:** [AdditionRecordings](/modules/TimeRecording.md#TimeRecording.AdditionRecording)

<a id="TimeRecording.AttendanceChart"></a>
### AttendanceChart

Represents an attendance chart.

- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceChart`
- **Required permission:** Show recording items
- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no | [RecordingDays](/modules/TimeRecording.md#TimeRecording.RecordingDay) |
| `RecordingDate` | `DateTime` | no |  |
| `EmployeeId` | `Int64` | no | [Persons](/modules/Common.md#Common.Person) |
| `EmployeeNumber` | `String` | no |  |
| `FirstName` | `String` | no |  |
| `LastName` | `String` | no |  |
| `InternalPhoneNumber` | `String` | no |  |
| `IsClosedInterval` | `Boolean` | no |  |
| `IntervalStart` | `DateTimeOffset` | no |  |
| `IntervalEnd` | `DateTimeOffset` | no |  |
| `AbsenceCodeId` | `Int64?` | yes |  |
| `AbsenceCode` | `String` | no |  |
| `AbsenceDescription` | `String` | no |  |
| `IsBreak` | `Boolean` | no |  |
| `ScheduleId` | `Int64?` | yes |  |
| `AbsenceKind` | `Int32` | no |  |
| `ScheduleType` | `Int32?` | yes |  |
| `IsNightSchedule` | `Boolean?` | yes |  |
| `ScheduleNumber` | `String` | no |  |
| `DepartmentId` | `Int64` | no |  |
| `DepartmentCode` | `String` | no |  |

**References out:** [Persons](/modules/Common.md#Common.Person), [RecordingDays](/modules/TimeRecording.md#TimeRecording.RecordingDay)

<a id="TimeRecording.AttendanceGroupSettings"></a>
### AttendanceGroupSettings

Represents an attendance group setting.

- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceGroupSettings`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 22.1

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `AllowAttendanceRecordingAdditionsInRecordingTerminal` | `Boolean` | no |  |
| `AllowAttendanceRecordingAdjustmentsInRecordingTerminal` | `Boolean` | no |  |
| `AllowShorterWorkingHours` | `Boolean` | no |  |
| `GenerateShorterWorkingHoursForHoliday` | `Boolean` | no |  |
| `Description` | `String` | no |  |
| `AbsenceCheck` | `Boolean` | no |  |
| `NonRegulatedWorkinghours` | `Boolean` | no |  |
| `AddRoundOffOvertimeToTimeBank` | `Int32` | no |  |
| `Name` | `String` | no |  |
| `AllowOvertime` | `Boolean` | no |  |
| `AllowAbsenceRecordingInNegativeFlexZones` | `Boolean` | no |  |
| `AutomaticOvertimeQuestionOutsideSchedule` | `Boolean` | no |  |
| `CalculationBase` | `Int32` | no |  |
| `CalculationFactor` | `TimeSpan` | no |  |
| `CalculateOvertime` | `Int32` | no |  |
| `FlexTime` | `Boolean` | no |  |
| `SalaryTypeForPositiveFlex` | `Int64?` | yes | [SalaryTypes](/modules/TimeRecording.md#TimeRecording.SalaryType) |
| `SalaryTypeForNegativeFlex` | `Int64?` | yes | [SalaryTypes](/modules/TimeRecording.md#TimeRecording.SalaryType) |
| `CalculateFlextime` | `Int32` | no |  |
| `SalaryTypeForScheduleLessRecording` | `Int64?` | yes | [SalaryTypes](/modules/TimeRecording.md#TimeRecording.SalaryType) |
| `MinTimePerDay` | `TimeSpan` | no |  |
| `NegativeFlexIncludedInDailyHours` | `Boolean` | no |  |
| `NumberOfDaysBackInTimeThatCanBeAdjusted` | `Int32` | no |  |
| `NumberOfDaysBackInTimeThatCanBeEdited` | `Int32` | no |  |
| `OvertimeInFlexZone` | `Boolean` | no |  |
| `OvertimeLimitAfter` | `TimeSpan` | no |  |
| `OvertimeLimitBefore` | `TimeSpan` | no |  |
| `PlanAbsenceViaRecordingTerminal` | `Boolean` | no |  |
| `RoundOffOvertime` | `Boolean` | no |  |
| `RoundOffOvertimeTimebankId` | `Int64?` | yes | [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank) |
| `RoundOffTo` | `TimeSpan` | no |  |
| `SalaryTypeAccordingToOvertime` | `Boolean` | no |  |
| `ShorterWorkingHoursTimeBankId` | `Int64?` | yes | [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank) |
| `TimeAfterScheduleEnd` | `TimeSpan` | no |  |
| `TimeBeforeScheduleStart` | `TimeSpan` | no |  |
| `UnavailableAbsenceCodes` | `AbsenceCodes[]` | no | [AbsenceCodes](/modules/TimeRecording.md#TimeRecording.AbsenceCode) |
| `OvertimeTypes` | `OvertimeTypes[]` | no | [OvertimeTypes](/modules/TimeRecording.md#TimeRecording.OvertimeType) |
| `IndirectWorkCodeId` | `Int64?` | yes | [IndirectWorkCodes](/modules/TimeRecording.md#TimeRecording.IndirectWorkCode) |

- `AddRoundOffOvertimeToTimeBank` — No=1, AllTime=2, TimeWithinFlexZone=3
- `CalculationBase` — Day=1, Hour=2, AccordingToSchedule=3
- `CalculateOvertime` — AllRecordedOvertime=0, AfterFulfilledDailyHours=1
- `CalculateFlextime` — AllRecordedFlex=0, AfterFulfilledDailyHours=1

**References out:** [AbsenceCodes](/modules/TimeRecording.md#TimeRecording.AbsenceCode), [IndirectWorkCodes](/modules/TimeRecording.md#TimeRecording.IndirectWorkCode), [OvertimeTypes](/modules/TimeRecording.md#TimeRecording.OvertimeType), [SalaryTypes](/modules/TimeRecording.md#TimeRecording.SalaryType), [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank)

<a id="TimeRecording.AttendanceInterval"></a>
### AttendanceIntervals

Represents an attendance recording interval on a recording day.

- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceIntervals`
- **Required permission:** Show recording items
- **Introduced in:** 2.25

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `IntervalStart` | `DateTimeOffset` | no |  |
| `IntervalEnd` | `DateTimeOffset` | no |  |
| `IsClosedInterval` | `Boolean` | no |  |
| `AbsenceCodeId` | `Int64?` | yes | [AbsenceCodes](/modules/TimeRecording.md#TimeRecording.AbsenceCode) |
| `DeductedIfDailyHoursNotFulfilledOverride` | `Boolean?` | yes |  |
| `OvertimeTypeBeforeId` | `Int64?` | yes | [OvertimeTypes](/modules/TimeRecording.md#TimeRecording.OvertimeType) |
| `OvertimeTypeAfterId` | `Int64?` | yes | [OvertimeTypes](/modules/TimeRecording.md#TimeRecording.OvertimeType) |
| `IsBreak` | `Boolean` | no |  |
| `IsAutomaticOut` | `Boolean` | no |  |
| `AbsenceKind` | `Int32` | no |  |
| `CalculatedTime` | `TimeSpan` | no |  |
| `CalculatedOvertimeBefore` | `TimeSpan` | no |  |
| `CalculatedOvertimeAfter` | `TimeSpan` | no |  |

- `AbsenceKind` — Default=0, Planned=1, Approved=2, TimeCard=3, NotContinue=4

**References out:** [AbsenceCodes](/modules/TimeRecording.md#TimeRecording.AbsenceCode), [OvertimeTypes](/modules/TimeRecording.md#TimeRecording.OvertimeType)
**Referenced by:** [RecordingDays](/modules/TimeRecording.md#TimeRecording.RecordingDay)

<a id="TimeRecording.IndirectWorkCode"></a>
### IndirectWorkCodes

Represents indirect work used for work recording.

- **Endpoint:** `GET /api/v1/TimeRecording/IndirectWorkCodes`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `CommentInputType` | `Int32` | no |  |
| `AffectsOrder` | `Int32` | no | [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `ColorCode` | `Int32?` | yes |  |
| `Active` | `Boolean` | no |  |

- `CommentInputType` — None=0, Optional=1, Mandatory=2
- `AffectsOrder` — No=0, UnitTime=1, SetupTime=2

**References out:** [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation)
**Referenced by:** [AttendanceGroupSettings](/modules/TimeRecording.md#TimeRecording.AttendanceGroupSettings), [StandbyWorks](/modules/TimeRecording.md#TimeRecording.StandbyWork), [WorkIntervals](/modules/TimeRecording.md#TimeRecording.WorkInterval)

<a id="TimeRecording.OvertimeType"></a>
### OvertimeTypes

Represents a overtime type.

- **Endpoint:** `GET /api/v1/TimeRecording/OvertimeTypes`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [AttendanceGroupSettings](/modules/TimeRecording.md#TimeRecording.AttendanceGroupSettings), [AttendanceIntervals](/modules/TimeRecording.md#TimeRecording.AttendanceInterval), [WorkshopScheduleSalaryTypes](/modules/TimeRecording.md#TimeRecording.WorkshopScheduleSalaryType)

<a id="TimeRecording.PersonTimeBank"></a>
### PersonTimeBanks

Represents a persons time bank.

- **Endpoint:** `GET /api/v1/TimeRecording/PersonTimeBanks`
- **Required permission:** Show recording items
- **Introduced in:** 22.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PersonId` | `Int64` | no | [Persons](/modules/Common.md#Common.Person) |
| `TimeBankId` | `Int64` | no | [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank) |
| `Balance` | `TimeSpan` | no |  |

**References out:** [Persons](/modules/Common.md#Common.Person), [TimeBanks](/modules/TimeRecording.md#TimeRecording.TimeBank)
**Referenced by:** [Persons](/modules/Common.md#Common.Person)

<a id="TimeRecording.PersonWorkCenter"></a>
### PersonWorkCenters

Represents a table that determines which work centers (and thereby which report numbers) the person should be allowed to select among in the priority plan and when starting work via report numbers.

- **Endpoint:** `GET /api/v1/TimeRecording/PersonWorkCenters`
- **Required permission:** Show person
- **Introduced in:** 24.3

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `WorkCenterId` | `Int64` | no | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |
| `PersonId` | `Int64` | no | [Persons](/modules/Common.md#Common.Person) |
| `Availability` | `Decimal?` | yes |  |
| `IsCapacityWorkCenter` | `Boolean` | no |  |
| `IsDefault` | `Boolean` | no |  |
| `ShowOnPriorityPlan` | `Boolean` | no |  |

**References out:** [Persons](/modules/Common.md#Common.Person), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [Persons](/modules/Common.md#Common.Person), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)

<a id="TimeRecording.PlannedAbsence"></a>
### PlannedAbsences

Represents a planned absence.

- **Endpoint:** `GET /api/v1/TimeRecording/PlannedAbsences`
- **Required permission:** Show person
- **Introduced in:** 2.47

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `PersonId` | `Int64` | no |  |
| `AbsenceFrom` | `DateTimeOffset` | no |  |
| `AbsenceTo` | `DateTimeOffset` | no |  |
| `AbsenceCodeId` | `Int64` | no |  |
| `PartOfDay` | `Boolean` | no |  |
| `Approved` | `Boolean` | no |  |
| `Status` | `Int32` | no |  |
| `AbsenceDuration` | `TimeSpan` | no |  |
| `AttendanceDuration` | `TimeSpan` | no |  |

- `Status` — AppliedFor=0, Approved=1, Denied=2

**Referenced by:** [Persons](/modules/Common.md#Common.Person)

<a id="TimeRecording.RecordingDay"></a>
### RecordingDays

Represents a Recording Day, which holds the attendance and work recordings which belongs to an employee for a specific date.

- **Endpoint:** `GET /api/v1/TimeRecording/RecordingDays`
- **Required permission:** Show recording items
- **Introduced in:** 2.25

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `RecordingDate` | `DateTime` | no |  |
| `PersonId` | `Int64` | no | [Persons](/modules/Common.md#Common.Person) |
| `ScheduleId` | `Int64?` | yes |  |
| `OvertimeScheduleId` | `Int64?` | yes |  |
| `CalculatedScheduleDiff` | `TimeSpan` | no |  |
| `CalculatedFlex` | `TimeSpan` | no |  |
| `CalculatedOvertime` | `TimeSpan` | no |  |
| `CalculatedAbsence` | `TimeSpan` | no |  |
| `CalculatedAttendance` | `TimeSpan` | no |  |
| `Exported` | `Boolean` | no |  |
| `Authorized` | `Boolean` | no |  |
| `AttendanceIntervals` | `AttendanceIntervals[]` | no | [AttendanceIntervals](/modules/TimeRecording.md#TimeRecording.AttendanceInterval) |
| `WorkIntervals` | `WorkIntervals[]` | no | [WorkIntervals](/modules/TimeRecording.md#TimeRecording.WorkInterval) |
| `Additions` | `AdditionRecordings[]` | no | [AdditionRecordings](/modules/TimeRecording.md#TimeRecording.AdditionRecording) |
| `Approved` | `Boolean` | no |  |
| `CommentText` | `String` | no |  |

**References out:** [AdditionRecordings](/modules/TimeRecording.md#TimeRecording.AdditionRecording), [AttendanceIntervals](/modules/TimeRecording.md#TimeRecording.AttendanceInterval), [Persons](/modules/Common.md#Common.Person), [WorkIntervals](/modules/TimeRecording.md#TimeRecording.WorkInterval)
**Referenced by:** [AttendanceChart](/modules/TimeRecording.md#TimeRecording.AttendanceChart)

<a id="TimeRecording.SalaryType"></a>
### SalaryTypes

Represents a salary type.

- **Endpoint:** `GET /api/v1/TimeRecording/SalaryTypes`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [AttendanceAdditions](/modules/TimeRecording.md#TimeRecording.AttendanceAddition), [AttendanceGroupSettings](/modules/TimeRecording.md#TimeRecording.AttendanceGroupSettings), [WorkshopScheduleSalaryTypes](/modules/TimeRecording.md#TimeRecording.WorkshopScheduleSalaryType)

<a id="TimeRecording.Schedule"></a>
### Schedules

Represents a schedule used for time recording.

- **Endpoint:** `GET /api/v1/TimeRecording/Schedules`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 22.2

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |
| `ScheduleLength` | `Int64` | no |  |
| `Start` | `Int64` | no |  |
| `End` | `Int64` | no |  |
| `OvertimeScheduleId` | `Int64?` | yes | [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule) |
| `FlexInStart` | `Int64?` | yes |  |
| `FlexInEnd` | `Int64?` | yes |  |
| `FlexOutStart` | `Int64?` | yes |  |
| `FlexOutEnd` | `Int64?` | yes |  |
| `IsNightSchedule` | `Boolean` | no |  |
| `Type` | `Int32` | no |  |
| `AmountSwh` | `Decimal?` | yes |  |
| `ScheduleNumberForExport` | `String` | no |  |
| `BlockedContextType` | `Int32` | no |  |
| `BlockedById` | `Int64?` | yes |  |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  |
| `BlockedToDate` | `DateTimeOffset?` | yes |  |
| `BlockedStatus` | `Int32` | no |  |
| `BlockMessageId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `BlockMessage` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

- `Type` (bitmask) — NotInitialized=0, Ordinary=1, Overtime=2
- `BlockedContextType` (bitmask) — None=0, RegisterScheduleCycle=1, CreateRecording=2
- `BlockedStatus` — None=0, Message=1, Blocked=2

**References out:** [Comments](/modules/Common.md#Common.Comment), [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule)
**Referenced by:** [Persons](/modules/Common.md#Common.Person), [ProductionCalendarExceptions](/modules/Manufacturing.md#Manufacturing.ProductionCalendarException), [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule), [WorkshopScheduleSalaryTypeRows](/modules/TimeRecording.md#TimeRecording.WorkshopScheduleSalaryTypeRow)

<a id="TimeRecording.Schedule_Obsolete"></a>
### Shedules _(deprecated)_

Represents a schedule used for time recording.

- **Endpoint:** `GET /api/v1/TimeRecording/Shedules`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |


<a id="TimeRecording.StandbyWork"></a>
### StandbyWorks

Represents a work put on standby.

- **Endpoint:** `GET /api/v1/TimeRecording/StandbyWorks`
- **Required permission:** Show recording items
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `EmployeeId` | `Int64` | no | [Persons](/modules/Common.md#Common.Person) |
| `BundleId` | `Guid` | no |  |
| `WorkRecordingType` | `Int32` | no |  |
| `IndirectWorkCodeId` | `Int64?` | yes | [IndirectWorkCodes](/modules/TimeRecording.md#TimeRecording.IndirectWorkCode) |
| `IndirectWorkCode` | `IndirectWorkCodes` | no | [IndirectWorkCodes](/modules/TimeRecording.md#TimeRecording.IndirectWorkCode) |
| `OperationId` | `Int64?` | yes | [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `Operation` | `ManufacturingOrderOperations` | no | [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `ActivityId` | `Int64?` | yes |  |

- `WorkRecordingType` — Indirect=0, OperationSetup=1, OperationUnit=2, ProjectActivity=3

**References out:** [IndirectWorkCodes](/modules/TimeRecording.md#TimeRecording.IndirectWorkCode), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [Persons](/modules/Common.md#Common.Person)

<a id="TimeRecording.TimeBank"></a>
### TimeBanks

Represents a time bank.

- **Endpoint:** `GET /api/v1/TimeRecording/TimeBanks`
- **Required permission:** Show recording items
- **Introduced in:** 2.26

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `Code` | `String` | no |  |
| `Description` | `String` | no |  |

**Referenced by:** [AdditionRecordings](/modules/TimeRecording.md#TimeRecording.AdditionRecording), [AttendanceAdditions](/modules/TimeRecording.md#TimeRecording.AttendanceAddition), [AttendanceGroupSettings](/modules/TimeRecording.md#TimeRecording.AttendanceGroupSettings), [PersonTimeBanks](/modules/TimeRecording.md#TimeRecording.PersonTimeBank)

<a id="TimeRecording.WorkInterval"></a>
### WorkIntervals

Represents a work interval.

- **Endpoint:** `GET /api/v1/TimeRecording/WorkIntervals`
- **Required permission:** Show recording items
- **Introduced in:** 2.25

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `IntervalStart` | `DateTimeOffset` | no |  |
| `IntervalEnd` | `DateTimeOffset` | no |  |
| `IsClosedInterval` | `Boolean` | no |  |
| `BundleId` | `Guid` | no |  |
| `WorkRecordingType` | `Int32` | no |  |
| `IndirectWorkCodeId` | `Int64?` | yes | [IndirectWorkCodes](/modules/TimeRecording.md#TimeRecording.IndirectWorkCode) |
| `OperationId` | `Int64?` | yes | [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation) |
| `TimeCalculationType` | `Int32` | no |  |
| `ReportingEmployeeId` | `Int64` | no | [Persons](/modules/Common.md#Common.Person) |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter) |
| `WorkedTime` | `TimeSpan` | no |  |
| `OfWichOvertime` | `TimeSpan` | no |  |
| `ReportedQuantity` | `Decimal` | no |  |
| `RejectedQuantity` | `Decimal` | no |  |
| `ActivityId` | `Int64?` | yes | [ProjectActivities](/modules/Common.md#Common.ProjectActivity) |
| `CommentId` | `Int64?` | yes | [Comments](/modules/Common.md#Common.Comment) |
| `Comment` | `Comments` | no | [Comments](/modules/Common.md#Common.Comment) |

- `WorkRecordingType` — Indirect=0, OperationSetup=1, OperationUnit=2, ProjectActivity=3
- `TimeCalculationType` — RecordedTime=0, PreCalculatedTime=1, BundleDistributedRecordedTime=2

**References out:** [Comments](/modules/Common.md#Common.Comment), [IndirectWorkCodes](/modules/TimeRecording.md#TimeRecording.IndirectWorkCode), [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [Persons](/modules/Common.md#Common.Person), [ProjectActivities](/modules/Common.md#Common.ProjectActivity), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [RecordingDays](/modules/TimeRecording.md#TimeRecording.RecordingDay)

<a id="TimeRecording.WorkshopScheduleSalaryTypeRow"></a>
### WorkshopScheduleSalaryTypeRows

Represent a workshop schedule salary type row.

- **Endpoint:** `GET /api/v1/TimeRecording/WorkshopScheduleSalaryTypeRows`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 24.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `ScheduleId` | `Int64` | no | [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule) |
| `Start` | `Int64?` | yes |  |
| `End` | `Int64?` | yes |  |
| `RowNumber` | `Int32?` | yes |  |

**References out:** [Schedules](/modules/TimeRecording.md#TimeRecording.Schedule)
**Referenced by:** [WorkshopScheduleSalaryTypes](/modules/TimeRecording.md#TimeRecording.WorkshopScheduleSalaryType)

<a id="TimeRecording.WorkshopScheduleSalaryType"></a>
### WorkshopScheduleSalaryTypes

Represent a workshop schedule salary type

- **Endpoint:** `GET /api/v1/TimeRecording/WorkshopScheduleSalaryTypes`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 24.4

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Id` | `Int64` | no |  |
| `WorkshopScheduleSalaryTypeRowId` | `Int64` | no | [WorkshopScheduleSalaryTypeRows](/modules/TimeRecording.md#TimeRecording.WorkshopScheduleSalaryTypeRow) |
| `OvertimeTypeId` | `Int64?` | yes | [OvertimeTypes](/modules/TimeRecording.md#TimeRecording.OvertimeType) |
| `Factor` | `Decimal?` | yes |  |
| `RowIndex` | `Int32?` | yes |  |
| `SalaryTypes` | `SalaryTypes[]` | no | [SalaryTypes](/modules/TimeRecording.md#TimeRecording.SalaryType) |

**References out:** [OvertimeTypes](/modules/TimeRecording.md#TimeRecording.OvertimeType), [SalaryTypes](/modules/TimeRecording.md#TimeRecording.SalaryType), [WorkshopScheduleSalaryTypeRows](/modules/TimeRecording.md#TimeRecording.WorkshopScheduleSalaryTypeRow)


## Depends on other modules

- [Common](/modules/Common.md): [Comments](/modules/Common.md#Common.Comment), [Currencies](/modules/Common.md#Common.Currency), [Persons](/modules/Common.md#Common.Person), [Projects](/modules/Common.md#Common.Project), [ProjectActivities](/modules/Common.md#Common.ProjectActivity), [ProjectCostTypes](/modules/Common.md#Common.ProjectCostType)
- [Manufacturing](/modules/Manufacturing.md): [ManufacturingOrderOperations](/modules/Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [WorkCenters](/modules/Manufacturing.md#Manufacturing.WorkCenter)
