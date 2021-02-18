# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/properties/executors/properties/defaults
```

Specify default executor settings for all executors

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json*](../out/settings.schema.json "open original schema") |

## defaults Type

`object` ([Details](settings-properties-executors-properties-defaults.md))

# defaults Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                |
| :------------------------------ | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [pollinterval](#pollinterval)   | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-properties-executors-properties-defaults-properties-pollinterval.md "settings.schema.json#/properties/executors/properties/defaults/properties/pollinterval")   |
| [launcher](#launcher)           | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-properties-executors-properties-defaults-properties-launcher.md "settings.schema.json#/properties/executors/properties/defaults/properties/launcher")           |
| [max_pend_time](#max_pend_time) | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-properties-executors-properties-defaults-properties-max_pend_time.md "settings.schema.json#/properties/executors/properties/defaults/properties/max_pend_time") |
| [account](#account)             | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-properties-executors-properties-defaults-properties-account.md "settings.schema.json#/properties/executors/properties/defaults/properties/account")             |

## pollinterval

Specify poll interval in seconds after job submission, where buildtest will sleep and poll all jobs for job states. This field can be configured based on your preference. Excessive polling every few seconds can result in system degradation.

`pollinterval`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-properties-executors-properties-defaults-properties-pollinterval.md "settings.schema.json#/properties/executors/properties/defaults/properties/pollinterval")

### pollinterval Type

`integer`

### pollinterval Constraints

**maximum**: the value of this number must smaller than or equal to: `300`

**minimum**: the value of this number must greater than or equal to: `10`

### pollinterval Default Value

The default value is:

```json
30
```

## launcher

Specify batch launcher to use when submitting jobs, this is applicable for LSF and Slurm Executors.

`launcher`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-properties-executors-properties-defaults-properties-launcher.md "settings.schema.json#/properties/executors/properties/defaults/properties/launcher")

### launcher Type

`string`

### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"sbatch"` |             |
| `"bsub"`   |             |
| `"qsub"`   |             |

## max_pend_time

Cancel job if it is still pending in queue beyond max_pend_time

`max_pend_time`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-properties-executors-properties-defaults-properties-max_pend_time.md "settings.schema.json#/properties/executors/properties/defaults/properties/max_pend_time")

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

*   defined in: [buildtest configuration schema](settings-properties-executors-properties-defaults-properties-account.md "settings.schema.json#/properties/executors/properties/defaults/properties/account")

### account Type

`string`
