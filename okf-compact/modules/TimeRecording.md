# TimeRecording

Monitor API module `TimeRecording`: 20 queryable entities, 0 commands, 0 payload types.

## Queryable entities

<a id="TimeRecording.AbsenceCode"></a>
### AbsenceCodes

Represents an absence code. Used in time recording to represent a period of absence.

- **Endpoint:** `GET /api/v1/TimeRecording/AbsenceCodes`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the absence code. |
| `Code` | `String` | no |  | The human readable identifier of the absence code. |
| `Description` | `String` | no |  | The translated description of the absence code. |

**Referenced by:** [AttendanceGroupSettings](TimeRecording.md#TimeRecording.AttendanceGroupSettings), [AttendanceIntervals](TimeRecording.md#TimeRecording.AttendanceInterval)

<a id="TimeRecording.AdditionRecording"></a>
### AdditionRecordings

Represents an additional recording

- **Endpoint:** `GET /api/v1/TimeRecording/AdditionRecordings`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 22.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the additional recording. |
| `AdditionType` | `Int32` | no |  | Type of attendance addition |
| `AttendanceAdditionId` | `Int64` | no | [AttendanceAdditions](TimeRecording.md#TimeRecording.AttendanceAddition) | The business key identifier of attendance addition id. |
| `AttendanceAddition` | `AttendanceAdditions` | no | [AttendanceAdditions](TimeRecording.md#TimeRecording.AttendanceAddition) | Attendance addition. |
| `TimeBankId` | `Int64?` | yes | [TimeBanks](TimeRecording.md#TimeRecording.TimeBank) | The business key identifier of time bank. |
| `TimeBank` | `TimeBanks` | no | [TimeBanks](TimeRecording.md#TimeRecording.TimeBank) | Time bank |
| `TimeBankTransaction` | `Int32` | no |  | Type of time bank transaction |
| `MandatoryComment` | `Boolean` | no |  | Specifies whether comment is mandatory or not. |
| `CommentId` | `Int64?` | yes |  | The comment id on the additional recording. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment on the additional recording. |
| `Amount` | `Decimal` | no |  | The amount of the additional recording. |
| `Cost` | `Decimal?` | yes |  | The cost of the additional recording. |
| `CostCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the additional recording cost currency. |
| `ProjectId` | `Int64?` | yes | [Projects](Common.md#Common.Project) | The business key identifier of the project this additional recording belongs to. |
| `IntervalStart` | `DateTimeOffset?` | yes |  | The start of the interval. |
| `IntervalEnd` | `DateTimeOffset?` | yes |  | The end of the interval. |

- `AdditionType` — Standard=0, SystemTimebankAdjustment=1
- `TimeBankTransaction` — Increase=0, Decrease=1

**References out:** [AttendanceAdditions](TimeRecording.md#TimeRecording.AttendanceAddition), [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [Projects](Common.md#Common.Project), [TimeBanks](TimeRecording.md#TimeRecording.TimeBank)
**Referenced by:** [RecordingDays](TimeRecording.md#TimeRecording.RecordingDay)

<a id="TimeRecording.AttendanceAddition"></a>
### AttendanceAdditions

Represents an attendance addition

- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceAdditions`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 22.7

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the attendance addition. |
| `RowNumber` | `Int32` | no |  | Row number of the attendance addition. |
| `Description` | `String` | no |  | The translated description of the attendance addition. |
| `AdditionType` | `Int32` | no |  | Type of attendance addition. |
| `IsActive` | `Boolean` | no |  | Specifies if attendance addition is active. |
| `EnterFromTo` | `Boolean` | no |  | Specifies whether Enter from/to is enabled. |
| `MandatoryComment` | `Boolean` | no |  | Specifies whether comment is mandatory or not. |
| `LinkToProjectType` | `Int32` | no |  | Type of link to project. |
| `TimeBankId` | `Int64?` | yes | [TimeBanks](TimeRecording.md#TimeRecording.TimeBank) | The business key identifier of time bank. |
| `TimeBank` | `TimeBanks` | no | [TimeBanks](TimeRecording.md#TimeRecording.TimeBank) | Time bank. |
| `TimeBankTransaction` | `Int32` | no |  | Type of time bank transaction. |
| `Cost` | `Decimal` | no |  | The cost of the attendance addition. |
| `CostCurrencyId` | `Int64?` | yes | [Currencies](Common.md#Common.Currency) | The business key identifier of the attendance addition cost currency. |
| `SalaryTypes` | `SalaryTypes[]` | no | [SalaryTypes](TimeRecording.md#TimeRecording.SalaryType) | The salary types of the attendance addition cost. |
| `CostTypeId` | `Int64?` | yes | [ProjectCostTypes](Common.md#Common.ProjectCostType) | The business key identifier of the project cost type of the attendance addition. |
| `CostType` | `ProjectCostTypes` | no | [ProjectCostTypes](Common.md#Common.ProjectCostType) | The project cost type of the attendance addition. |
| `CostVisibility` | `Int32` | no |  | The visibility or editability of the cost of the attendance addition. |

- `AdditionType` — Standard=0, SystemTimebankAdjustment=1
- `LinkToProjectType` — None=0, Optional=1, Mandatory=2
- `TimeBankTransaction` — Increase=0, Decrease=1
- `CostVisibility` — No=0, Yes=1, Editable=2

**References out:** [Currencies](Common.md#Common.Currency), [ProjectCostTypes](Common.md#Common.ProjectCostType), [SalaryTypes](TimeRecording.md#TimeRecording.SalaryType), [TimeBanks](TimeRecording.md#TimeRecording.TimeBank)
**Referenced by:** [AdditionRecordings](TimeRecording.md#TimeRecording.AdditionRecording)

<a id="TimeRecording.AttendanceChart"></a>
### AttendanceChart

Represents an attendance chart.

- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceChart`
- **Required permission:** Show recording items
- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no | [RecordingDays](TimeRecording.md#TimeRecording.RecordingDay) | The business key identifier of the latest recording day. |
| `RecordingDate` | `DateTime` | no |  | The date of the last recording. |
| `EmployeeId` | `Int64` | no | [Persons](Common.md#Common.Person) | The business key identifier of the employee that the recording belongs to. |
| `EmployeeNumber` | `String` | no |  | The employee number of the recording employee. |
| `FirstName` | `String` | no |  | The first name of the recording employee. |
| `LastName` | `String` | no |  | The last name of the recording employee. |
| `InternalPhoneNumber` | `String` | no |  | The internal phone number of the recording employee. |
| `IsClosedInterval` | `Boolean` | no |  | Specifies if the interval of the attendance period has been closed. |
| `IntervalStart` | `DateTimeOffset` | no |  | When the interval started. |
| `IntervalEnd` | `DateTimeOffset` | no |  | When the interval ended. |
| `AbsenceCodeId` | `Int64?` | yes |  | The business key identifier of the recording's absence code. |
| `AbsenceCode` | `String` | no |  | The human readable identifier of the recording's absence code. |
| `AbsenceDescription` | `String` | no |  | The absence code description. |
| `IsBreak` | `Boolean` | no |  | Specifies if the interval is considered break time. |
| `ScheduleId` | `Int64?` | yes |  | The business key identifier of the schedule that the recording is based upon. |
| `AbsenceKind` | `Int32` | no |  | The absence kind of the recording. |
| `ScheduleType` | `Int32?` | yes |  | The schedule type of the recording. Represents Monitor.StrawberryFields.Shared.Workshop.WorkshopScheduleType 1 - Ordinary 2 - Overtime |
| `IsNightSchedule` | `Boolean?` | yes |  | Specifies if the recording falls under night schedule. |
| `ScheduleNumber` | `String` | no |  | The schedule number of the recording. |
| `DepartmentId` | `Int64` | no |  | The business key identifier of the department linked to the recording. |
| `DepartmentCode` | `String` | no |  | The department code of the recording. |

**References out:** [Persons](Common.md#Common.Person), [RecordingDays](TimeRecording.md#TimeRecording.RecordingDay)

<a id="TimeRecording.AttendanceGroupSettings"></a>
### AttendanceGroupSettings

Represents an attendance group setting.

- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceGroupSettings`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 22.1

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the attendance group setting. |
| `AllowAttendanceRecordingAdditionsInRecordingTerminal` | `Boolean` | no |  | Indicates if attendance recording additions is allowed in the recording terminal. |
| `AllowAttendanceRecordingAdjustmentsInRecordingTerminal` | `Boolean` | no |  | Indicates if attendance recording adjustments are allowed in the recording terminal. |
| `AllowShorterWorkingHours` | `Boolean` | no |  | Indicates if shorter working hours are allowed. |
| `GenerateShorterWorkingHoursForHoliday` | `Boolean` | no |  | Indicates if shorter working hours for holidays should be generated. |
| `Description` | `String` | no |  | The translated description of the attendance group setting. |
| `AbsenceCheck` | `Boolean` | no |  | Indicates if absences should be checked. |
| `NonRegulatedWorkinghours` | `Boolean` | no |  | Indicates if non regulated working hours are allowed. |
| `AddRoundOffOvertimeToTimeBank` | `Int32` | no |  | The round off for overtime to the time bank. |
| `Name` | `String` | no |  | The name of the attendance group setting. |
| `AllowOvertime` | `Boolean` | no |  | Indicates if overtime is allowed. |
| `AllowAbsenceRecordingInNegativeFlexZones` | `Boolean` | no |  | Indicates if absence recording is allowed within negative flex zones. |
| `AutomaticOvertimeQuestionOutsideSchedule` | `Boolean` | no |  | Indicates if there should be a dialog for overtime outside of the schedule. |
| `CalculationBase` | `Int32` | no |  | The calculation base type for shorter working hours. |
| `CalculationFactor` | `TimeSpan` | no |  | The calculation factor. |
| `CalculateOvertime` | `Int32` | no |  | Indicates how overtime is calculated. |
| `FlexTime` | `Boolean` | no |  | Indicates if flex time is allowed. |
| `SalaryTypeForPositiveFlex` | `Int64?` | yes | [SalaryTypes](TimeRecording.md#TimeRecording.SalaryType) | The salary type for positive flex. |
| `SalaryTypeForNegativeFlex` | `Int64?` | yes | [SalaryTypes](TimeRecording.md#TimeRecording.SalaryType) | The salary type for negative flex. |
| `CalculateFlextime` | `Int32` | no |  | Indicates how flex is calculated. |
| `SalaryTypeForScheduleLessRecording` | `Int64?` | yes | [SalaryTypes](TimeRecording.md#TimeRecording.SalaryType) | The salary type for schedule less recordings. |
| `MinTimePerDay` | `TimeSpan` | no |  | The minimum time the employee has to work for shorter working hours to apply when using per day calculation. |
| `NegativeFlexIncludedInDailyHours` | `Boolean` | no |  | Indicates if negative flex should be included in daily hours. |
| `NumberOfDaysBackInTimeThatCanBeAdjusted` | `Int32` | no |  | Determains how many days are adjustable back in time. |
| `NumberOfDaysBackInTimeThatCanBeEdited` | `Int32` | no |  | Determains how many days are editable back in time. |
| `OvertimeInFlexZone` | `Boolean` | no |  | Indicates if overtime is allowed within flex zone. |
| `OvertimeLimitAfter` | `TimeSpan` | no |  | The overtime limit after the end of the schedule. |
| `OvertimeLimitBefore` | `TimeSpan` | no |  | The overtime limit before the start of the schedule. |
| `PlanAbsenceViaRecordingTerminal` | `Boolean` | no |  | Indicates if planned absence is allowed from the recording terminal. |
| `RoundOffOvertime` | `Boolean` | no |  | Indicates if round off overtime should be used. |
| `RoundOffOvertimeTimebankId` | `Int64?` | yes | [TimeBanks](TimeRecording.md#TimeRecording.TimeBank) | The timebank to use for round off overtime. |
| `RoundOffTo` | `TimeSpan` | no |  | The time to round off overtime to. |
| `SalaryTypeAccordingToOvertime` | `Boolean` | no |  | Indicates if salary type should be calculated from the start of the overtime schedule, not from where it was recorded. |
| `ShorterWorkingHoursTimeBankId` | `Int64?` | yes | [TimeBanks](TimeRecording.md#TimeRecording.TimeBank) | The time bank to use for shorter working hours. |
| `TimeAfterScheduleEnd` | `TimeSpan` | no |  | Threshold for automatic overtime question after schedule end in recording terminal. |
| `TimeBeforeScheduleStart` | `TimeSpan` | no |  | Threshold for automatic overtime question before schedule start in recording terminal. |
| `UnavailableAbsenceCodes` | `AbsenceCodes[]` | no | [AbsenceCodes](TimeRecording.md#TimeRecording.AbsenceCode) | Unavailable absence codes for the attendance group setting. |
| `OvertimeTypes` | `OvertimeTypes[]` | no | [OvertimeTypes](TimeRecording.md#TimeRecording.OvertimeType) | The overtime types for the attendance group setting. |
| `IndirectWorkCodeId` | `Int64?` | yes | [IndirectWorkCodes](TimeRecording.md#TimeRecording.IndirectWorkCode) | The business key identifier of the indirect work. |

- `AddRoundOffOvertimeToTimeBank` — No=1, AllTime=2, TimeWithinFlexZone=3
- `CalculationBase` — Day=1, Hour=2, AccordingToSchedule=3
- `CalculateOvertime` — AllRecordedOvertime=0, AfterFulfilledDailyHours=1
- `CalculateFlextime` — AllRecordedFlex=0, AfterFulfilledDailyHours=1

**References out:** [AbsenceCodes](TimeRecording.md#TimeRecording.AbsenceCode), [IndirectWorkCodes](TimeRecording.md#TimeRecording.IndirectWorkCode), [OvertimeTypes](TimeRecording.md#TimeRecording.OvertimeType), [SalaryTypes](TimeRecording.md#TimeRecording.SalaryType), [TimeBanks](TimeRecording.md#TimeRecording.TimeBank)

<a id="TimeRecording.AttendanceInterval"></a>
### AttendanceIntervals

Represents an attendance recording interval on a recording day.

- **Endpoint:** `GET /api/v1/TimeRecording/AttendanceIntervals`
- **Required permission:** Show recording items
- **Introduced in:** 2.25

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of an attendance interval. |
| `IntervalStart` | `DateTimeOffset` | no |  | The start of the interval. |
| `IntervalEnd` | `DateTimeOffset` | no |  | The end of the interval. |
| `IsClosedInterval` | `Boolean` | no |  | Indicatates if the interval was ended. If false the interval is considered the active interval on the day which the next attendance recording is supposed to end. |
| `AbsenceCodeId` | `Int64?` | yes | [AbsenceCodes](TimeRecording.md#TimeRecording.AbsenceCode) | The business key identifier of an absence code. If defined this interval is an absence recording. References a AbsenceCodes |
| `DeductedIfDailyHoursNotFulfilledOverride` | `Boolean?` | yes |  | Used to per recording be able to override the setting from an absence code if it should affect deduction of overtime. |
| `OvertimeTypeBeforeId` | `Int64?` | yes | [OvertimeTypes](TimeRecording.md#TimeRecording.OvertimeType) | The business key identifier of an overtime type selected at the start of the interval. References a OvertimeTypes |
| `OvertimeTypeAfterId` | `Int64?` | yes | [OvertimeTypes](TimeRecording.md#TimeRecording.OvertimeType) | The business key identifier of an overtime type selected at the end of the interval. References a OvertimeTypes |
| `IsBreak` | `Boolean` | no |  | Indicates if this is a break recording. |
| `IsAutomaticOut` | `Boolean` | no |  | Indicates if this was an automatic clock-out recording due to forgotten clock-out the previous day. |
| `AbsenceKind` | `Int32` | no |  | Specifies the absence kind recorded for this interval. |
| `CalculatedTime` | `TimeSpan` | no |  | The recorded time for this interval after schedule and settings has been taken into account. |
| `CalculatedOvertimeBefore` | `TimeSpan` | no |  | The amount of overtime before schedule start. |
| `CalculatedOvertimeAfter` | `TimeSpan` | no |  | The amount of overtime after schedule end. |

- `AbsenceKind` — Default=0, Planned=1, Approved=2, TimeCard=3, NotContinue=4

**References out:** [AbsenceCodes](TimeRecording.md#TimeRecording.AbsenceCode), [OvertimeTypes](TimeRecording.md#TimeRecording.OvertimeType)
**Referenced by:** [RecordingDays](TimeRecording.md#TimeRecording.RecordingDay)

<a id="TimeRecording.IndirectWorkCode"></a>
### IndirectWorkCodes

Represents indirect work used for work recording.

- **Endpoint:** `GET /api/v1/TimeRecording/IndirectWorkCodes`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the indirect work. |
| `Code` | `String` | no |  | The human readable identifier of the indirect work. |
| `Description` | `String` | no |  | The translated description of the indirect work. |
| `CommentInputType` | `Int32` | no |  | Describes if a comment may or must be supplied when recording. |
| `AffectsOrder` | `Int32` | no | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) | Describes how this indirect work is reported when linked to a ManufacturingOrderOperations in recording. |
| `ColorCode` | `Int32?` | yes |  | Color code encoded as an ARGB. |
| `Active` | `Boolean` | no |  | Indicates whether the indirect work code is active and may be used to start new indirect work. |

- `CommentInputType` — None=0, Optional=1, Mandatory=2
- `AffectsOrder` — No=0, UnitTime=1, SetupTime=2

**References out:** [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation)
**Referenced by:** [AttendanceGroupSettings](TimeRecording.md#TimeRecording.AttendanceGroupSettings), [StandbyWorks](TimeRecording.md#TimeRecording.StandbyWork), [WorkIntervals](TimeRecording.md#TimeRecording.WorkInterval)

<a id="TimeRecording.OvertimeType"></a>
### OvertimeTypes

Represents a overtime type.

- **Endpoint:** `GET /api/v1/TimeRecording/OvertimeTypes`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the overtime type. |
| `Code` | `String` | no |  | The human readable identifier of the overtime type. |
| `Description` | `String` | no |  | The translated description of the overtime type. |

**Referenced by:** [AttendanceGroupSettings](TimeRecording.md#TimeRecording.AttendanceGroupSettings), [AttendanceIntervals](TimeRecording.md#TimeRecording.AttendanceInterval), [WorkshopScheduleSalaryTypes](TimeRecording.md#TimeRecording.WorkshopScheduleSalaryType)

<a id="TimeRecording.PersonTimeBank"></a>
### PersonTimeBanks

Represents a persons time bank.

- **Endpoint:** `GET /api/v1/TimeRecording/PersonTimeBanks`
- **Required permission:** Show recording items
- **Introduced in:** 22.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the person time bank. |
| `PersonId` | `Int64` | no | [Persons](Common.md#Common.Person) | The person identifier of the person time bank. |
| `TimeBankId` | `Int64` | no | [TimeBanks](TimeRecording.md#TimeRecording.TimeBank) | The time bank identifier for the person time bank. |
| `Balance` | `TimeSpan` | no |  | The balance of the person time bank. |

**References out:** [Persons](Common.md#Common.Person), [TimeBanks](TimeRecording.md#TimeRecording.TimeBank)
**Referenced by:** [Persons](Common.md#Common.Person)

<a id="TimeRecording.PersonWorkCenter"></a>
### PersonWorkCenters

Represents a table that determines which work centers (and thereby which report numbers) the person should be allowed to select among in the priority plan and when starting work via report numbers.

- **Endpoint:** `GET /api/v1/TimeRecording/PersonWorkCenters`
- **Required permission:** Show person
- **Introduced in:** 24.3

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the person work center. |
| `WorkCenterId` | `Int64` | no | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier of the work center that is linked to the person. |
| `PersonId` | `Int64` | no | [Persons](Common.md#Common.Person) | The business key identifier of the employee that is linked to the work center. |
| `Availability` | `Decimal?` | yes |  | Availability in percent |
| `IsCapacityWorkCenter` | `Boolean` | no |  | Determines if the Work Center has the employee linked as capacity. |
| `IsDefault` | `Boolean` | no |  | Determines if the work center should be selected by default when starting direct work. |
| `ShowOnPriorityPlan` | `Boolean` | no |  | Determine if the work center should be available to select in the work center field in order for priority plan to be shown in the recording terminal during start of direct work. |

**References out:** [Persons](Common.md#Common.Person), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [Persons](Common.md#Common.Person), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)

<a id="TimeRecording.PlannedAbsence"></a>
### PlannedAbsences

Represents a planned absence.

- **Endpoint:** `GET /api/v1/TimeRecording/PlannedAbsences`
- **Required permission:** Show person
- **Introduced in:** 2.47

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the planned absence. |
| `PersonId` | `Int64` | no |  | The business key identifier of the person. References(Person) |
| `AbsenceFrom` | `DateTimeOffset` | no |  | The start of the absence period. |
| `AbsenceTo` | `DateTimeOffset` | no |  | The end of the absence period. |
| `AbsenceCodeId` | `Int64` | no |  | The business key identifier of the absence code. References(AbsenceCode) |
| `PartOfDay` | `Boolean` | no |  | Specifies if the absence is part of a day. |
| `Approved` | `Boolean` | no |  | Specifies if the absence is approved. _(Use status instead. (Returns true if status is approved else returns false))_ |
| `Status` | `Int32` | no |  | Specifies the absence status. |
| `AbsenceDuration` | `TimeSpan` | no |  | The absence duration of the planned absence. |
| `AttendanceDuration` | `TimeSpan` | no |  | The attendance duration of the planned absence. |

- `Status` — AppliedFor=0, Approved=1, Denied=2

**Referenced by:** [Persons](Common.md#Common.Person)

<a id="TimeRecording.RecordingDay"></a>
### RecordingDays

Represents a Recording Day, which holds the attendance and work recordings which belongs to an employee for a specific date.

- **Endpoint:** `GET /api/v1/TimeRecording/RecordingDays`
- **Required permission:** Show recording items
- **Introduced in:** 2.25

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the recording day. |
| `RecordingDate` | `DateTime` | no |  | The date this recording day belongs to. |
| `PersonId` | `Int64` | no | [Persons](Common.md#Common.Person) | The business key identifier of the Employee that this recording day belongs to. |
| `ScheduleId` | `Int64?` | yes |  | The business key identifier of the workshop schedule assigned to this day. Null if recording without schedule. |
| `OvertimeScheduleId` | `Int64?` | yes |  | The business key identifier of the workshop overtime schedule assigned to this day. Null if recording without overtime schedule. |
| `CalculatedScheduleDiff` | `TimeSpan` | no |  | The calculated difference between the schedule length and the sum of recorded attendance and absence on the day. |
| `CalculatedFlex` | `TimeSpan` | no |  | The days calculated total flex-time. |
| `CalculatedOvertime` | `TimeSpan` | no |  | The days calculated total overtime. |
| `CalculatedAbsence` | `TimeSpan` | no |  | The days calculated total absence. |
| `CalculatedAttendance` | `TimeSpan` | no |  | The days calculated total attendance. |
| `Exported` | `Boolean` | no |  | Indicatates if the day has been exported by the salary export system. When true the creation of new or modification of existing attendance recordings is not allowed. |
| `Authorized` | `Boolean` | no |  | Indicatates if the day has been authorized. |
| `AttendanceIntervals` | `AttendanceIntervals[]` | no | [AttendanceIntervals](TimeRecording.md#TimeRecording.AttendanceInterval) | The recorded attendance intervals belonging to this day. |
| `WorkIntervals` | `WorkIntervals[]` | no | [WorkIntervals](TimeRecording.md#TimeRecording.WorkInterval) | The recorded work intervals belonging to this day. |
| `Additions` | `AdditionRecordings[]` | no | [AdditionRecordings](TimeRecording.md#TimeRecording.AdditionRecording) | Additional recordings belonging to this day. |
| `Approved` | `Boolean` | no |  | Indicates that the employee is finished with the adding or adjustments. |
| `CommentText` | `String` | no |  | Recording comment |

**References out:** [AdditionRecordings](TimeRecording.md#TimeRecording.AdditionRecording), [AttendanceIntervals](TimeRecording.md#TimeRecording.AttendanceInterval), [Persons](Common.md#Common.Person), [WorkIntervals](TimeRecording.md#TimeRecording.WorkInterval)
**Referenced by:** [AttendanceChart](TimeRecording.md#TimeRecording.AttendanceChart)

<a id="TimeRecording.SalaryType"></a>
### SalaryTypes

Represents a salary type.

- **Endpoint:** `GET /api/v1/TimeRecording/SalaryTypes`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the salary type. |
| `Code` | `String` | no |  | The human readable identifier of the salary type. |
| `Description` | `String` | no |  | The translated description of the salary type. |

**Referenced by:** [AttendanceAdditions](TimeRecording.md#TimeRecording.AttendanceAddition), [AttendanceGroupSettings](TimeRecording.md#TimeRecording.AttendanceGroupSettings), [WorkshopScheduleSalaryTypes](TimeRecording.md#TimeRecording.WorkshopScheduleSalaryType)

<a id="TimeRecording.Schedule"></a>
### Schedules

Represents a schedule used for time recording.

- **Endpoint:** `GET /api/v1/TimeRecording/Schedules`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 22.2

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the schedule. |
| `Code` | `String` | no |  | The human readable identifier of the schedule. |
| `Description` | `String` | no |  | The translated description of the schedule. |
| `ScheduleLength` | `Int64` | no |  | The length of the schedule. |
| `Start` | `Int64` | no |  | Information about the start of the schedule. |
| `End` | `Int64` | no |  | Information about the end of the schedule. |
| `OvertimeScheduleId` | `Int64?` | yes | [Schedules](TimeRecording.md#TimeRecording.Schedule) | The business key identifier of the Overtime schedule. |
| `FlexInStart` | `Int64?` | yes |  | The flex in start of the schedule. |
| `FlexInEnd` | `Int64?` | yes |  | The flex in end of the schedule. |
| `FlexOutStart` | `Int64?` | yes |  | The flex out start of the schedule. |
| `FlexOutEnd` | `Int64?` | yes |  | The flex out end of the schedule. |
| `IsNightSchedule` | `Boolean` | no |  | The boolean value for the night schedule. |
| `Type` | `Int32` | no |  | A type of schedule. |
| `AmountSwh` | `Decimal?` | yes |  | The amount of shorter work hours (SWH) |
| `ScheduleNumberForExport` | `String` | no |  | The schedule number for export |
| `BlockedContextType` | `Int32` | no |  | The context type of block |
| `BlockedById` | `Int64?` | yes |  | The business key identifier of the application user that blocked the entity. |
| `BlockedFromDate` | `DateTimeOffset?` | yes |  | The date when the entity starts being blocked. |
| `BlockedToDate` | `DateTimeOffset?` | yes |  | The date when the entity stops being blocked. |
| `BlockedStatus` | `Int32` | no |  | The block status of the entity. |
| `BlockMessageId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the entity block message comment. References Comments . |
| `BlockMessage` | `Comments` | no | [Comments](Common.md#Common.Comment) | The entity block message comment |

- `Type` (bitmask) — NotInitialized=0, Ordinary=1, Overtime=2
- `BlockedContextType` (bitmask) — None=0, RegisterScheduleCycle=1, CreateRecording=2
- `BlockedStatus` — None=0, Message=1, Blocked=2

**References out:** [Comments](Common.md#Common.Comment), [Schedules](TimeRecording.md#TimeRecording.Schedule)
**Referenced by:** [Persons](Common.md#Common.Person), [ProductionCalendarExceptions](Manufacturing.md#Manufacturing.ProductionCalendarException), [Schedules](TimeRecording.md#TimeRecording.Schedule), [WorkshopScheduleSalaryTypeRows](TimeRecording.md#TimeRecording.WorkshopScheduleSalaryTypeRow)

<a id="TimeRecording.Schedule_Obsolete"></a>
### Shedules _(deprecated)_

Represents a schedule used for time recording.

- **Endpoint:** `GET /api/v1/TimeRecording/Shedules`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the shedule. |
| `Code` | `String` | no |  | The human readable identifier of the shedule. |
| `Description` | `String` | no |  | The translated description of the shedule. |


<a id="TimeRecording.StandbyWork"></a>
### StandbyWorks

Represents a work put on standby.

- **Endpoint:** `GET /api/v1/TimeRecording/StandbyWorks`
- **Required permission:** Show recording items
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the standby work. |
| `EmployeeId` | `Int64` | no | [Persons](Common.md#Common.Person) | The business key identifier of the employee who has this work on standby. |
| `BundleId` | `Guid` | no |  | The bundle id of the work. Used to identify if work should be started as a bundle when restarting. |
| `WorkRecordingType` | `Int32` | no |  | What type of work this represents. |
| `IndirectWorkCodeId` | `Int64?` | yes | [IndirectWorkCodes](TimeRecording.md#TimeRecording.IndirectWorkCode) | The business key identifier of the indirect work code, defined when WorkRecordingType is Indirect. |
| `IndirectWorkCode` | `IndirectWorkCodes` | no | [IndirectWorkCodes](TimeRecording.md#TimeRecording.IndirectWorkCode) | The indirect work code, available when WorkRecordingType is Indirect. |
| `OperationId` | `Int64?` | yes | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) | The business key identifier of the operation, defined when WorkRecordingType is OperationSetup or OperationUnit. |
| `Operation` | `ManufacturingOrderOperations` | no | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) | The operation for this work, available when WorkRecordingType is OperationSetup or OperationUnit. |
| `ActivityId` | `Int64?` | yes |  | The business key identifier of the activity, defined when WorkRecordingType is Activity. References a project activity. |

- `WorkRecordingType` — Indirect=0, OperationSetup=1, OperationUnit=2, ProjectActivity=3

**References out:** [IndirectWorkCodes](TimeRecording.md#TimeRecording.IndirectWorkCode), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [Persons](Common.md#Common.Person)

<a id="TimeRecording.TimeBank"></a>
### TimeBanks

Represents a time bank.

- **Endpoint:** `GET /api/v1/TimeRecording/TimeBanks`
- **Required permission:** Show recording items
- **Introduced in:** 2.26

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the time bank. |
| `Code` | `String` | no |  | The human readable identifier of the time bank. |
| `Description` | `String` | no |  | The translated description of the time bank. |

**Referenced by:** [AdditionRecordings](TimeRecording.md#TimeRecording.AdditionRecording), [AttendanceAdditions](TimeRecording.md#TimeRecording.AttendanceAddition), [AttendanceGroupSettings](TimeRecording.md#TimeRecording.AttendanceGroupSettings), [PersonTimeBanks](TimeRecording.md#TimeRecording.PersonTimeBank)

<a id="TimeRecording.WorkInterval"></a>
### WorkIntervals

Represents a work interval.

- **Endpoint:** `GET /api/v1/TimeRecording/WorkIntervals`
- **Required permission:** Show recording items
- **Introduced in:** 2.25

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of a work interval. |
| `IntervalStart` | `DateTimeOffset` | no |  | The start of the interval. |
| `IntervalEnd` | `DateTimeOffset` | no |  | The end of the interval. |
| `IsClosedInterval` | `Boolean` | no |  | Indicatates if the interval was ended. If false the interval is considered an active interval on the day which a future work recording is supposed to end. |
| `BundleId` | `Guid` | no |  | Identifier to detect what work was recorded in the same bundle. |
| `WorkRecordingType` | `Int32` | no |  | What type of work this recording represents. Indicates which id is relevant on the interval. |
| `IndirectWorkCodeId` | `Int64?` | yes | [IndirectWorkCodes](TimeRecording.md#TimeRecording.IndirectWorkCode) | The business key identifier to an indirect work code. Defined if is indirect work. |
| `OperationId` | `Int64?` | yes | [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation) | The business key identifier to a manufacturing order operation. Defined if it is an operation unit or a setup recording. |
| `TimeCalculationType` | `Int32` | no |  | The time calculation type for this interval. |
| `ReportingEmployeeId` | `Int64` | no | [Persons](Common.md#Common.Person) | The business key identifier to the employee making the recording. When machine recording this key will represent the operator if defined. Otherwise this will be the same as the person owning the recording day. |
| `WorkCenterId` | `Int64?` | yes | [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter) | The business key identifier to the workcenter associated with the recording. |
| `WorkedTime` | `TimeSpan` | no |  | The calculated work time for this interval. |
| `OfWichOvertime` | `TimeSpan` | no |  | How much of the worked time that was considered overtime. |
| `ReportedQuantity` | `Decimal` | no |  | The reported quantity for this recording. |
| `RejectedQuantity` | `Decimal` | no |  | The rejected quantity for this recording. |
| `ActivityId` | `Int64?` | yes | [ProjectActivities](Common.md#Common.ProjectActivity) | The business key identifier to a project activity. Defined if it is a project activity. |
| `CommentId` | `Int64?` | yes | [Comments](Common.md#Common.Comment) | The business key identifier of the work interval comment. |
| `Comment` | `Comments` | no | [Comments](Common.md#Common.Comment) | The comment of the work interval. |

- `WorkRecordingType` — Indirect=0, OperationSetup=1, OperationUnit=2, ProjectActivity=3
- `TimeCalculationType` — RecordedTime=0, PreCalculatedTime=1, BundleDistributedRecordedTime=2

**References out:** [Comments](Common.md#Common.Comment), [IndirectWorkCodes](TimeRecording.md#TimeRecording.IndirectWorkCode), [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [Persons](Common.md#Common.Person), [ProjectActivities](Common.md#Common.ProjectActivity), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
**Referenced by:** [RecordingDays](TimeRecording.md#TimeRecording.RecordingDay)

<a id="TimeRecording.WorkshopScheduleSalaryTypeRow"></a>
### WorkshopScheduleSalaryTypeRows

Represent a workshop schedule salary type row.

- **Endpoint:** `GET /api/v1/TimeRecording/WorkshopScheduleSalaryTypeRows`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 24.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of the row |
| `ScheduleId` | `Int64` | no | [Schedules](TimeRecording.md#TimeRecording.Schedule) | The business key identifier of schedule |
| `Start` | `Int64?` | yes |  | Information about the start of the salary type row |
| `End` | `Int64?` | yes |  | Information about the end of the salary type row |
| `RowNumber` | `Int32?` | yes |  | The row number of the workshop salary type row. |

**References out:** [Schedules](TimeRecording.md#TimeRecording.Schedule)
**Referenced by:** [WorkshopScheduleSalaryTypes](TimeRecording.md#TimeRecording.WorkshopScheduleSalaryType)

<a id="TimeRecording.WorkshopScheduleSalaryType"></a>
### WorkshopScheduleSalaryTypes

Represent a workshop schedule salary type

- **Endpoint:** `GET /api/v1/TimeRecording/WorkshopScheduleSalaryTypes`
- **Required permission:** Show basic data for attendance
- **Introduced in:** 24.4

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Id` | `Int64` | no |  | The business key identifier of workshop schedule salary type |
| `WorkshopScheduleSalaryTypeRowId` | `Int64` | no | [WorkshopScheduleSalaryTypeRows](TimeRecording.md#TimeRecording.WorkshopScheduleSalaryTypeRow) | The business key identifier of workshop schedule salary type row |
| `OvertimeTypeId` | `Int64?` | yes | [OvertimeTypes](TimeRecording.md#TimeRecording.OvertimeType) | The business key identifier of overtime type |
| `Factor` | `Decimal?` | yes |  | The factor of workshop schedule salary type |
| `RowIndex` | `Int32?` | yes |  | The row index of workshop schedule salary type |
| `SalaryTypes` | `SalaryTypes[]` | no | [SalaryTypes](TimeRecording.md#TimeRecording.SalaryType) | List of salary type |

**References out:** [OvertimeTypes](TimeRecording.md#TimeRecording.OvertimeType), [SalaryTypes](TimeRecording.md#TimeRecording.SalaryType), [WorkshopScheduleSalaryTypeRows](TimeRecording.md#TimeRecording.WorkshopScheduleSalaryTypeRow)


## Depends on other modules

- [Common](Common.md): [Comments](Common.md#Common.Comment), [Currencies](Common.md#Common.Currency), [Persons](Common.md#Common.Person), [Projects](Common.md#Common.Project), [ProjectActivities](Common.md#Common.ProjectActivity), [ProjectCostTypes](Common.md#Common.ProjectCostType)
- [Manufacturing](Manufacturing.md): [ManufacturingOrderOperations](Manufacturing.md#Manufacturing.ManufacturingOrderOperation), [WorkCenters](Manufacturing.md#Manufacturing.WorkCenter)
