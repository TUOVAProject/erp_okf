---
type: API Module
title: Infrastructure
description: Monitor ERP API module Infrastructure.
tags:
- Infrastructure
- module
generated:
  by: process:monitor-okf-build
  from: 677a27684767
entity_count: 18
queryable_count: 0
---

# Infrastructure

Monitor API module `Infrastructure`: 0 queryable entities, 0 commands, 18 payload types.

Full listing: [Infrastructure entities](/entities/Infrastructure/index.md)

## Queryable entities

| Entity | Endpoint | Description |
| --- | --- | --- |

## Payload types

| Type | Description |
| --- | --- |
| [ApiMultipartFormCommandAttribute](/entities/Infrastructure/ApiMultipartFormCommandAttribute.md) | Use this attribute to mark if command is using multipart/form body as request body. |
| [ApiValidationResult](/entities/Infrastructure/ApiValidationResult.md) | Specifies a command validation result. |
| [BatchCommandEntity](/entities/Infrastructure/BatchCommandEntity.md) | A batch command entity is used to create command batches, allowing transactional continuity across multiple commands. |
| [BatchResponse](/entities/Infrastructure/BatchResponse.md) | The response object used by the batching system to return the complete result of an entire batch of commands. |
| [BooleanInput](/entities/Infrastructure/BooleanInput.md) | Represents a nullable boolean input for update commands. |
| [DateTimeInput](/entities/Infrastructure/DateTimeInput.md) | Represents a nullable date/time input for update commands. |
| [DecimalInput](/entities/Infrastructure/DecimalInput.md) | Represents a nullable decimal input for update commands. |
| [EntityCommandResponse](/entities/Infrastructure/EntityCommandResponse.md) | This is the response type of all state commands available in the system. As long as a command uses this return-type, it can be used with the command batching system. |
| [ErrorCommandResponse](/entities/Infrastructure/ErrorCommandResponse.md) | This is the response type returned if an error occurs when invoking a command. |
| [IntegerInput](/entities/Infrastructure/IntegerInput.md) | Represents a nullable 32-bit integer input for update commands. |
| [LongInput](/entities/Infrastructure/LongInput.md) | Represents a nullable 64-bit integer input for update commands. |
| [NotNullBooleanInput](/entities/Infrastructure/NotNullBooleanInput.md) | Represents a boolean input for update commands. |
| [NotNullDateTimeInput](/entities/Infrastructure/NotNullDateTimeInput.md) | Represents a date/time value for update commands. |
| [NotNullDecimalInput](/entities/Infrastructure/NotNullDecimalInput.md) | Represents a decimal input for update commands. |
| [NotNullIntegerInput](/entities/Infrastructure/NotNullIntegerInput.md) | Represents a 32-bit integer input for update commands. |
| [NotNullLongInput](/entities/Infrastructure/NotNullLongInput.md) | Represents a 64-bit integer input for update commands. |
| [StringInput](/entities/Infrastructure/StringInput.md) | Represents a string input for update commands. |
| [ValidationCommandResponse](/entities/Infrastructure/ValidationCommandResponse.md) | This is the response type returned when adding /Validate after the command path. |
