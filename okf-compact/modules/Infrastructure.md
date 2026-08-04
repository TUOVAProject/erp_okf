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

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Kind` | `Int32` | no |  | The validation kind of the result. |
| `Message` | `String` | no |  | The message returned by the validation. |

- `Kind` — Valid=0, Warning=1, Error=2

**Referenced by:** [ValidationCommandResponse](Infrastructure.md#Infrastructure.ValidationCommandResponse)

<a id="Infrastructure.BatchCommandEntity"></a>
### BatchCommandEntity

A batch command entity is used to create command batches, allowing transactional continuity across multiple commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Path` | `String` | no |  | The API-local URL to the command that should be invoked. For example /Common/Commands/CreateComment . |
| `Body` | `Object` | no |  | The JSON-encoded instance of the command that should be invoked. |
| `ForwardPropertyName` | `String` | no |  | The name of the property to forward from the response of the command to the next command in the batch. |
| `ReceivingPropertyName` | `String` | no |  | The name of the property that should receive the forwarded property from the previous command in the batch. |


<a id="Infrastructure.BatchResponse"></a>
### BatchResponse

The response object used by the batching system to return the complete result of an entire batch of commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `IsSuccessful` | `Boolean` | no |  | Specifies if the batch was successfully committed or not. |
| `Response` | `EntityCommandResponse[]` | no | [EntityCommandResponse](Infrastructure.md#Infrastructure.EntityCommandResponse) | The individual commmand responses in the batch. When the batch command includes commands that uses the /Many tag the responses are flattened out. You still get one result per individual command, but to be able to match the responses, the batch command also needs to be flattened out. |
| `FailingIndex` | `Int32?` | yes |  | The index of the failing command in the batch. |
| `ErrorMessage` | `String` | no |  | The error message of the failure that caused the batch to be rolled back. |

**References out:** [EntityCommandResponse](Infrastructure.md#Infrastructure.EntityCommandResponse)

<a id="Infrastructure.BooleanInput"></a>
### BooleanInput

Represents a nullable boolean input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `Boolean?` | yes |  | The nullable boolean value to update the property with. |


<a id="Infrastructure.DateTimeInput"></a>
### DateTimeInput

Represents a nullable date/time input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `DateTimeOffset?` | yes |  | The nullable date/time value to update the property with. |


<a id="Infrastructure.DecimalInput"></a>
### DecimalInput

Represents a nullable decimal input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `Decimal?` | yes |  | The nullable decimal value to update the property with. |


<a id="Infrastructure.EntityCommandResponse"></a>
### EntityCommandResponse

This is the response type of all state commands available in the system. As long as a command uses this return-type, it can be used with the command batching system.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `RootEntityId` | `Int64` | no |  | The business key identifier of the root entity in the context of the command. This is usually the parent entity of the parent that has been changed. |
| `EntityId` | `Int64` | no |  | The business key identifier of the main entity in the context of the command. This is always the entity that has been changed by the command. |
| `CommandName` | `String` | no |  | The name of the command that was invoked. |
| `Data` | `String` | no |  | Extended return-data of the command encoded as JSON. |

**Referenced by:** [BatchResponse](Infrastructure.md#Infrastructure.BatchResponse)

<a id="Infrastructure.ErrorCommandResponse"></a>
### ErrorCommandResponse

This is the response type returned if an error occurs when invoking a command.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `ErrorMessage` | `String` | no |  | The message of the error that caused the command to fail. |


<a id="Infrastructure.IntegerInput"></a>
### IntegerInput

Represents a nullable 32-bit integer input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `Int32?` | yes |  | The nullable 32-bit integer value to update the property with. |


<a id="Infrastructure.LongInput"></a>
### LongInput

Represents a nullable 64-bit integer input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `Int64?` | yes |  | The nullable 64-bit integer value to update the property with. |


<a id="Infrastructure.NotNullBooleanInput"></a>
### NotNullBooleanInput

Represents a boolean input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `Boolean` | no |  | The boolean value to update the property with. |


<a id="Infrastructure.NotNullDateTimeInput"></a>
### NotNullDateTimeInput

Represents a date/time value for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `DateTimeOffset` | no |  | The date/time value to update the property with. |


<a id="Infrastructure.NotNullDecimalInput"></a>
### NotNullDecimalInput

Represents a decimal input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `Decimal` | no |  | The decimal value to update the property with. |


<a id="Infrastructure.NotNullIntegerInput"></a>
### NotNullIntegerInput

Represents a 32-bit integer input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `Int32` | no |  | The 32-bit integer value to update the property with. |


<a id="Infrastructure.NotNullLongInput"></a>
### NotNullLongInput

Represents a 64-bit integer input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `Int64` | no |  | The 64-bit integer value to update the property with. |


<a id="Infrastructure.StringInput"></a>
### StringInput

Represents a string input for update commands.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `Value` | `String` | no |  | The string value to update the property with. |


<a id="Infrastructure.ValidationCommandResponse"></a>
### ValidationCommandResponse

This is the response type returned when adding /Validate after the command path.

- **Introduced in:** 2.18

| Property | Type | Nullable | References | Description |
| --- | --- | --- | --- | --- |
| `IsValid` | `Boolean` | no |  | Specifies if the command was validated or not. |
| `ErrorMessage` | `String` | no |  | The error message thrown by the command if any. |
| `Results` | `ApiValidationResult[]` | no | [ApiValidationResult](Infrastructure.md#Infrastructure.ApiValidationResult) | The validation results of the command. |

**References out:** [ApiValidationResult](Infrastructure.md#Infrastructure.ApiValidationResult)
