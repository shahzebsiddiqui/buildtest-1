# Untitled object in compiler schema version 1.0 Schema

```txt
compiler-v1.0.schema.json#/definitions/compiler_declaration/properties/module
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                            |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [compiler-v1.0.schema.json*](../out/compiler-v1.0.schema.json "open original schema") |

## module Type

`object` ([Details](compiler-v1-definitions-compiler_declaration-properties-module.md))

# module Properties

| Property            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                             |
| :------------------ | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [purge](#purge)     | `boolean` | Optional | cannot be null | [compiler schema version 1.0](compiler-v1-definitions-compiler_declaration-properties-module-properties-purge.md "compiler-v1.0.schema.json#/definitions/compiler_declaration/properties/module/properties/purge")     |
| [load](#load)       | `array`   | Optional | cannot be null | [compiler schema version 1.0](definitions-definitions-list_of_strings.md "compiler-v1.0.schema.json#/definitions/compiler_declaration/properties/module/properties/load")                                              |
| [restore](#restore) | `string`  | Optional | cannot be null | [compiler schema version 1.0](compiler-v1-definitions-compiler_declaration-properties-module-properties-restore.md "compiler-v1.0.schema.json#/definitions/compiler_declaration/properties/module/properties/restore") |
| [swap](#swap)       | `array`   | Optional | cannot be null | [compiler schema version 1.0](compiler-v1-definitions-compiler_declaration-properties-module-properties-swap.md "compiler-v1.0.schema.json#/definitions/compiler_declaration/properties/module/properties/swap")       |

## purge

Run `module purge` if purge is set

`purge`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [compiler schema version 1.0](compiler-v1-definitions-compiler_declaration-properties-module-properties-purge.md "compiler-v1.0.schema.json#/definitions/compiler_declaration/properties/module/properties/purge")

### purge Type

`boolean`

## load

Load one or more modules via `module load`

`load`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [compiler schema version 1.0](definitions-definitions-list_of_strings.md "compiler-v1.0.schema.json#/definitions/compiler_declaration/properties/module/properties/load")

### load Type

`string[]`

### load Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## restore

Load a collection name via `module restore`

`restore`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [compiler schema version 1.0](compiler-v1-definitions-compiler_declaration-properties-module-properties-restore.md "compiler-v1.0.schema.json#/definitions/compiler_declaration/properties/module/properties/restore")

### restore Type

`string`

## swap

Swap modules using `module swap`. The swap property expects 2 unique modules.

`swap`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [compiler schema version 1.0](compiler-v1-definitions-compiler_declaration-properties-module-properties-swap.md "compiler-v1.0.schema.json#/definitions/compiler_declaration/properties/module/properties/swap")

### swap Type

`string[]`

### swap Constraints

**maximum number of items**: the maximum number of items for this array is: `2`

**minimum number of items**: the minimum number of items for this array is: `2`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
