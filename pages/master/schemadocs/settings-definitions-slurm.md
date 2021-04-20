# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/slurm
```

An instance object of slurm executor

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json*](../out/settings.schema.json "open original schema") |

## slurm Type

`object` ([Details](settings-definitions-slurm.md))

# slurm Properties

| Property                        | Type          | Required | Nullable       | Defined by                                                                                                                                                  |
| :------------------------------ | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description)     | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-description.md "settings.schema.json#/definitions/slurm/properties/description")     |
| [launcher](#launcher)           | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-launcher.md "settings.schema.json#/definitions/slurm/properties/launcher")           |
| [options](#options)             | `array`       | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-options.md "settings.schema.json#/definitions/slurm/properties/options")             |
| [cluster](#cluster)             | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-cluster.md "settings.schema.json#/definitions/slurm/properties/cluster")             |
| [partition](#partition)         | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-partition.md "settings.schema.json#/definitions/slurm/properties/partition")         |
| [qos](#qos)                     | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-qos.md "settings.schema.json#/definitions/slurm/properties/qos")                     |
| [before_script](#before_script) | Not specified | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-before_script.md "settings.schema.json#/definitions/slurm/properties/before_script") |
| [after_script](#after_script)   | Not specified | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-after_script.md "settings.schema.json#/definitions/slurm/properties/after_script")   |
| [max_pend_time](#max_pend_time) | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-max_pend_time.md "settings.schema.json#/definitions/slurm/properties/max_pend_time")                  |
| [account](#account)             | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-account.md "settings.schema.json#/definitions/slurm/properties/account")                              |

## description

description field for documenting your executor

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-description.md "settings.schema.json#/definitions/slurm/properties/description")

### description Type

`string`

## launcher

Specify the slurm batch scheduler to use. This overrides the default `launcher` field. This must be `sbatch`.

`launcher`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-launcher.md "settings.schema.json#/definitions/slurm/properties/launcher")

### launcher Type

`string`

### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"sbatch"` |             |

## options

Specify any other options for `sbatch` used by this executor for running all jobs.

`options`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-options.md "settings.schema.json#/definitions/slurm/properties/options")

### options Type

`string[]`

## cluster

Specify the slurm cluster you want to use `-M <cluster>`

`cluster`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-cluster.md "settings.schema.json#/definitions/slurm/properties/cluster")

### cluster Type

`string`

## partition

Specify the slurm partition you want to use `-p <partition>`

`partition`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-partition.md "settings.schema.json#/definitions/slurm/properties/partition")

### partition Type

`string`

## qos

Specify the slurm qos you want to use `-q <qos>`

`qos`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-qos.md "settings.schema.json#/definitions/slurm/properties/qos")

### qos Type

`string`

## before_script

The `before_script` section can be used to specify commands before start of test. The script will be sourced in active shell.

`before_script`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-before_script.md "settings.schema.json#/definitions/slurm/properties/before_script")

### before_script Type

unknown

## after_script

The `after_script` section can be used to specify commands at end of test. The script will be sourced in active shell.

`after_script`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-after_script.md "settings.schema.json#/definitions/slurm/properties/after_script")

### after_script Type

unknown

## max_pend_time

Cancel job if it is still pending in queue beyond max_pend_time

`max_pend_time`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-max_pend_time.md "settings.schema.json#/definitions/slurm/properties/max_pend_time")

### max_pend_time Type

`integer`

### max_pend_time Constraints

**minimum**: the value of this number must greater than or equal to: `10`

### max_pend_time Default Value

The default value is:

```json
90
```

## account

Specify Job Account for charging resources

`account`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-account.md "settings.schema.json#/definitions/slurm/properties/account")

### account Type

`string`
