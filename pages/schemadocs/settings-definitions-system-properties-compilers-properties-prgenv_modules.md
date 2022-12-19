# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## prgenv\_modules Type

`object` ([Details](settings-definitions-system-properties-compilers-properties-prgenv_modules.md))

# prgenv\_modules Properties

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                  |
| :-------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [gcc](#gcc)     | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-prgenv_modules-properties-gcc.md "settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules/properties/gcc")     |
| [intel](#intel) | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-prgenv_modules-properties-intel.md "settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules/properties/intel") |
| [cray](#cray)   | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-prgenv_modules-properties-cray.md "settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules/properties/cray")   |
| [nvhpc](#nvhpc) | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-prgenv_modules-properties-nvhpc.md "settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules/properties/nvhpc") |

## gcc

Specify name of Programming Environment module for gcc

`gcc`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-prgenv_modules-properties-gcc.md "settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules/properties/gcc")

### gcc Type

`string`

### gcc Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"PrgEnv-gnu"` |             |

## intel

Specify name of Programming Environment module for intel

`intel`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-prgenv_modules-properties-intel.md "settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules/properties/intel")

### intel Type

`string`

### intel Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"PrgEnv-intel"` |             |

## cray

Specify name of Programming Environment module for cray

`cray`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-prgenv_modules-properties-cray.md "settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules/properties/cray")

### cray Type

`string`

### cray Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"PrgEnv-cray"` |             |

## nvhpc

Specify name of Programming Environment module for nvhpc

`nvhpc`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers-properties-prgenv_modules-properties-nvhpc.md "settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules/properties/nvhpc")

### nvhpc Type

`string`

### nvhpc Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"PrgEnv-nvhpc"`  |             |
| `"PrgEnv-nvidia"` |             |
