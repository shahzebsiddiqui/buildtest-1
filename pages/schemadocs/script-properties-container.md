# Untitled object in script schema version Schema

```txt
script.schema.json#/properties/container
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                               |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [script.schema.json\*](../out/script.schema.json "open original schema") |

## container Type

`object` ([Details](script-properties-container.md))

# container Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                 |
| :-------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| [platform](#platform) | `string` | Required | cannot be null | [script schema version](script-properties-container-properties-platform.md "script.schema.json#/properties/container/properties/platform") |
| [image](#image)       | `string` | Required | cannot be null | [script schema version](script-properties-container-properties-image.md "script.schema.json#/properties/container/properties/image")       |
| [mounts](#mounts)     | `string` | Optional | cannot be null | [script schema version](script-properties-container-properties-mounts.md "script.schema.json#/properties/container/properties/mounts")     |
| [options](#options)   | `string` | Optional | cannot be null | [script schema version](script-properties-container-properties-options.md "script.schema.json#/properties/container/properties/options")   |
| [command](#command)   | `string` | Optional | cannot be null | [script schema version](script-properties-container-properties-command.md "script.schema.json#/properties/container/properties/command")   |

## platform

Specify a container platform to use when running test. This is used for running commands inside container.

`platform`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [script schema version](script-properties-container-properties-platform.md "script.schema.json#/properties/container/properties/platform")

### platform Type

`string`

### platform Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"docker"`      |             |
| `"podman"`      |             |
| `"singularity"` |             |

## image

Specify a container image to use when running test. This is used for running commands inside container.

`image`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [script schema version](script-properties-container-properties-image.md "script.schema.json#/properties/container/properties/image")

### image Type

`string`

## mounts

Specify a list of directory paths to bind mount into the container

`mounts`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [script schema version](script-properties-container-properties-mounts.md "script.schema.json#/properties/container/properties/mounts")

### mounts Type

`string`

## options

Specify a list of options to pass to container runtime.

`options`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [script schema version](script-properties-container-properties-options.md "script.schema.json#/properties/container/properties/options")

### options Type

`string`

## command

Specify a list of commands to run inside container. This is used for running commands inside container.

`command`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [script schema version](script-properties-container-properties-command.md "script.schema.json#/properties/container/properties/command")

### command Type

`string`
