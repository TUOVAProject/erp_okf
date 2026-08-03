# Infrastructure

Monitor API module `Infrastructure`: 0 queryable entities, 0 commands, 18 payload types.

## Payload types

<a id="Infrastructure.ApiMultipartFormCommandAttribute"></a>
### ApiMultipartFormCommandAttribute

Use this attribute to mark if command is using multipart/form body as request body.


<a id="Infrastructure.ApiValidationResult"></a>
### ApiValidationResult

Specifies a command validation result.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Kind` | `Int32` | no |  |
| `Message` | `String` | no |  |

- `Kind` — Valid=0, Warning=1, Error=2

**Referenced by:** [ValidationCommandResponse](/modules/Infrastructure.md#Infrastructure.ValidationCommandResponse)

<a id="Infrastructure.BatchCommandEntity"></a>
### BatchCommandEntity

A batch command entity is used to create command batches, allowing transactional continuity across multiple commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Path` | `String` | no |  |
| `Body` | `Object` | no |  |
| `ForwardPropertyName` | `String` | no |  |
| `ReceivingPropertyName` | `String` | no |  |


<a id="Infrastructure.BatchResponse"></a>
### BatchResponse

The response object used by the batching system to return the complete result of an entire batch of commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `IsSuccessful` | `Boolean` | no |  |
| `Response` | `EntityCommandResponse[]` | no | [EntityCommandResponse](/modules/Infrastructure.md#Infrastructure.EntityCommandResponse) |
| `FailingIndex` | `Int32?` | yes |  |
| `ErrorMessage` | `String` | no |  |

**References out:** [EntityCommandResponse](/modules/Infrastructure.md#Infrastructure.EntityCommandResponse)

<a id="Infrastructure.BooleanInput"></a>
### BooleanInput

Represents a nullable boolean input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `Boolean?` | yes |  |


<a id="Infrastructure.DateTimeInput"></a>
### DateTimeInput

Represents a nullable date/time input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `DateTimeOffset?` | yes |  |


<a id="Infrastructure.DecimalInput"></a>
### DecimalInput

Represents a nullable decimal input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `Decimal?` | yes |  |


<a id="Infrastructure.EntityCommandResponse"></a>
### EntityCommandResponse

This is the response type of all state commands available in the system. As long as a command uses this return-type, it can be used with the command batching system.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `RootEntityId` | `Int64` | no |  |
| `EntityId` | `Int64` | no |  |
| `CommandName` | `String` | no |  |
| `Data` | `String` | no |  |

**Referenced by:** [BatchResponse](/modules/Infrastructure.md#Infrastructure.BatchResponse)

<a id="Infrastructure.ErrorCommandResponse"></a>
### ErrorCommandResponse

This is the response type returned if an error occurs when invoking a command.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `ErrorMessage` | `String` | no |  |


<a id="Infrastructure.IntegerInput"></a>
### IntegerInput

Represents a nullable 32-bit integer input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `Int32?` | yes |  |


<a id="Infrastructure.LongInput"></a>
### LongInput

Represents a nullable 64-bit integer input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `Int64?` | yes |  |


<a id="Infrastructure.NotNullBooleanInput"></a>
### NotNullBooleanInput

Represents a boolean input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `Boolean` | no |  |


<a id="Infrastructure.NotNullDateTimeInput"></a>
### NotNullDateTimeInput

Represents a date/time value for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `DateTimeOffset` | no |  |


<a id="Infrastructure.NotNullDecimalInput"></a>
### NotNullDecimalInput

Represents a decimal input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `Decimal` | no |  |


<a id="Infrastructure.NotNullIntegerInput"></a>
### NotNullIntegerInput

Represents a 32-bit integer input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `Int32` | no |  |


<a id="Infrastructure.NotNullLongInput"></a>
### NotNullLongInput

Represents a 64-bit integer input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `Int64` | no |  |


<a id="Infrastructure.StringInput"></a>
### StringInput

Represents a string input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `Value` | `String` | no |  |


<a id="Infrastructure.ValidationCommandResponse"></a>
### ValidationCommandResponse

This is the response type returned when adding /Validate after the command path.

- **Introduced in:** 2.18

| Property | Type | Nullable | References |
| --- | --- | --- | --- |
| `IsValid` | `Boolean` | no |  |
| `ErrorMessage` | `String` | no |  |
| `Results` | `ApiValidationResult[]` | no | [ApiValidationResult](/modules/Infrastructure.md#Infrastructure.ApiValidationResult) |

**References out:** [ApiValidationResult](/modules/Infrastructure.md#Infrastructure.ApiValidationResult)
