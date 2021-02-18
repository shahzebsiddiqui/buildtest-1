# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/properties/executors
```

The executor section is used for declaring your executors that are responsible for running jobs. The executor section can be `local`, `lsf`, `slurm`, `cobalt`. The executors are referenced in buildspec using `executor` field.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json*](../out/settings.schema.json "open original schema") |

## executors Type

`object` ([Details](settings-properties-executors.md))

# executors Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                              |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [defaults](#defaults) | `object` | Optional | cannot be null | [buildtest configuration schema](settings-properties-executors-properties-defaults.md "settings.schema.json#/properties/executors/properties/defaults") |
| [local](#local)       | `object` | Optional | cannot be null | [buildtest configuration schema](settings-properties-executors-properties-local.md "settings.schema.json#/properties/executors/properties/local")       |
| [lsf](#lsf)           | `object` | Optional | cannot be null | [buildtest configuration schema](settings-properties-executors-properties-lsf.md "settings.schema.json#/properties/executors/properties/lsf")           |
| [slurm](#slurm)       | `object` | Optional | cannot be null | [buildtest configuration schema](settings-properties-executors-properties-slurm.md "settings.schema.json#/properties/executors/properties/slurm")       |
| [cobalt](#cobalt)     | `object` | Optional | cannot be null | [buildtest configuration schema](settings-properties-executors-properties-cobalt.md "settings.schema.json#/properties/executors/properties/cobalt")     |

## defaults

Specify default executor settings for all executors

`defaults`

*   is optional

*   Type: `object` ([Details](settings-properties-executors-properties-defaults.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-properties-executors-properties-defaults.md "settings.schema.json#/properties/executors/properties/defaults")

### defaults Type

`object` ([Details](settings-properties-executors-properties-defaults.md))

## local

The `local` section is used for declaring local executors for running jobs on local machine

`local`

*   is optional

*   Type: `object` ([Details](settings-properties-executors-properties-local.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-properties-executors-properties-local.md "settings.schema.json#/properties/executors/properties/local")

### local Type

`object` ([Details](settings-properties-executors-properties-local.md))

## lsf

The `lsf` section is used for declaring LSF executors for running jobs using LSF scheduler

`lsf`

*   is optional

*   Type: `object` ([Details](settings-properties-executors-properties-lsf.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-properties-executors-properties-lsf.md "settings.schema.json#/properties/executors/properties/lsf")

### lsf Type

`object` ([Details](settings-properties-executors-properties-lsf.md))

## slurm

The `slurm` section is used for declaring Slurm executors for running jobs using Slurm scheduler

`slurm`

*   is optional

*   Type: `object` ([Details](settings-properties-executors-properties-slurm.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-properties-executors-properties-slurm.md "settings.schema.json#/properties/executors/properties/slurm")

### slurm Type

`object` ([Details](settings-properties-executors-properties-slurm.md))

## cobalt

The `cobalt` section is used for declaring Cobalt executors for running jobs using Cobalt scheduler

`cobalt`

*   is optional

*   Type: `object` ([Details](settings-properties-executors-properties-cobalt.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-properties-executors-properties-cobalt.md "settings.schema.json#/properties/executors/properties/cobalt")

### cobalt Type

`object` ([Details](settings-properties-executors-properties-cobalt.md))
