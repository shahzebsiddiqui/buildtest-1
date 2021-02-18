# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/properties/executors/properties/slurm
```

The `slurm` section is used for declaring Slurm executors for running jobs using Slurm scheduler

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [settings.schema.json*](../out/settings.schema.json "open original schema") |

## slurm Type

`object` ([Details](settings-properties-executors-properties-slurm.md))

# slurm Properties

| Property | Type     | Required | Nullable       | Defined by                                                                                                                                           |
| :------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| `^.*$`   | `object` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm.md "settings.schema.json#/properties/executors/properties/slurm/patternProperties/^.*$") |

## Pattern: `^.*$`

An instance object of slurm executor

`^.*$`

*   is optional

*   Type: `object` ([Details](settings-definitions-slurm.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm.md "settings.schema.json#/properties/executors/properties/slurm/patternProperties/^.\*$")

### ^.\*$ Type

`object` ([Details](settings-definitions-slurm.md))
