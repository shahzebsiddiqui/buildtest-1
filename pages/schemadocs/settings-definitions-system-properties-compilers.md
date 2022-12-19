# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/system/properties/compilers
```

Declare compiler section for defining system compilers that can be referenced in buildspec.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## compilers Type

`object` ([Details](settings-definitions-system-properties-compilers.md))

# compilers Properties

| Property                           | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                |
| :--------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [enable\_prgenv](#enable_prgenv)   | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-enable_prgenv.md "settings.schema.json#/definitions/system/properties/compilers/properties/enable_prgenv")   |
| [modulepath](#modulepath)          | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/system/properties/compilers/properties/modulepath")                                        |
| [purge](#purge)                    | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-purge.md "settings.schema.json#/definitions/system/properties/compilers/properties/purge")                   |
| [prgenv\_modules](#prgenv_modules) | `object`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-prgenv_modules.md "settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules") |
| [find](#find)                      | `object`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-find.md "settings.schema.json#/definitions/system/properties/compilers/properties/find")                     |
| [compiler](#compiler)              | `object`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-compiler.md "settings.schema.json#/definitions/system/properties/compilers/properties/compiler")             |

## enable\_prgenv

Enable support for Programming Environment

`enable_prgenv`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-enable_prgenv.md "settings.schema.json#/definitions/system/properties/compilers/properties/enable_prgenv")

### enable\_prgenv Type

`boolean`

## modulepath



`modulepath`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/system/properties/compilers/properties/modulepath")

### modulepath Type

`string[]`

### modulepath Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## purge

A boolean to determine whether to purge modules via `module purge` when generating compiler declaration

`purge`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-purge.md "settings.schema.json#/definitions/system/properties/compilers/properties/purge")

### purge Type

`boolean`

## prgenv\_modules



`prgenv_modules`

*   is optional

*   Type: `object` ([Details](settings-definitions-system-properties-compilers-properties-prgenv_modules.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-prgenv_modules.md "settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules")

### prgenv\_modules Type

`object` ([Details](settings-definitions-system-properties-compilers-properties-prgenv_modules.md))

## find

Find compilers by specifying regular expression that is applied to modulefile names

`find`

*   is optional

*   Type: `object` ([Details](settings-definitions-system-properties-compilers-properties-find.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-find.md "settings.schema.json#/definitions/system/properties/compilers/properties/find")

### find Type

`object` ([Details](settings-definitions-system-properties-compilers-properties-find.md))

## compiler

Start of compiler declaration

`compiler`

*   is optional

*   Type: `object` ([Details](settings-definitions-system-properties-compilers-properties-compiler.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-compiler.md "settings.schema.json#/definitions/system/properties/compilers/properties/compiler")

### compiler Type

`object` ([Details](settings-definitions-system-properties-compilers-properties-compiler.md))
