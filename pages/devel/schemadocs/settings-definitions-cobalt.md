# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/cobalt
```

An instance object of cobalt executor

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json*](../out/settings.schema.json "open original schema") |

## cobalt Type

`object` ([Details](settings-definitions-cobalt.md))

# cobalt Properties

| Property                        | Type          | Required | Nullable       | Defined by                                                                                                                                                    |
| :------------------------------ | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description)     | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-description.md "settings.schema.json#/definitions/cobalt/properties/description")     |
| [launcher](#launcher)           | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-launcher.md "settings.schema.json#/definitions/cobalt/properties/launcher")           |
| [options](#options)             | `array`       | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-options.md "settings.schema.json#/definitions/cobalt/properties/options")             |
| [queue](#queue)                 | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-queue.md "settings.schema.json#/definitions/cobalt/properties/queue")                 |
| [before_script](#before_script) | Not specified | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-before_script.md "settings.schema.json#/definitions/cobalt/properties/before_script") |
| [after_script](#after_script)   | Not specified | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-after_script.md "settings.schema.json#/definitions/cobalt/properties/after_script")   |
| [max_pend_time](#max_pend_time) | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-max_pend_time.md "settings.schema.json#/definitions/cobalt/properties/max_pend_time")                   |
| [account](#account)             | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-account.md "settings.schema.json#/definitions/cobalt/properties/account")                               |

## description

description field for documenting your executor

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-description.md "settings.schema.json#/definitions/cobalt/properties/description")

### description Type

`string`

## launcher

Specify the cobalt batch scheduler to use. This overrides the default `launcher` field. It must be `qsub`.

`launcher`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-launcher.md "settings.schema.json#/definitions/cobalt/properties/launcher")

### launcher Type

`string`

### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"qsub"` |             |

## options

Specify any options for `qsub` for this executor when running all jobs associated to this executor

`options`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-options.md "settings.schema.json#/definitions/cobalt/properties/options")

### options Type

`string[]`

## queue

Specify the lsf queue you want to use `-q <queue>`

`queue`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-queue.md "settings.schema.json#/definitions/cobalt/properties/queue")

### queue Type

`string`

## before_script

The `before_script` section can be used to specify commands before start of test. The script will be sourced in active shell.

`before_script`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-before_script.md "settings.schema.json#/definitions/cobalt/properties/before_script")

### before_script Type

unknown

## after_script

The `after_script` section can be used to specify commands at end of test. The script will be sourced in active shell.

`after_script`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-after_script.md "settings.schema.json#/definitions/cobalt/properties/after_script")

### after_script Type

unknown

## max_pend_time

Cancel job if it is still pending in queue beyond max_pend_time

`max_pend_time`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-max_pend_time.md "settings.schema.json#/definitions/cobalt/properties/max_pend_time")

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

*   defined in: [buildtest configuration schema](settings-definitions-account.md "settings.schema.json#/definitions/cobalt/properties/account")

### account Type

`string`
