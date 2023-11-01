# Untitled object in spack schema version Schema

```txt
spack.schema.json#/definitions/load
```

load spack packages using `spack load` command

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [spack.schema.json\*](../out/spack.schema.json "open original schema") |

## load Type

`object` ([Details](spack-definitions-load.md))

# load Properties

| Property            | Type     | Required | Nullable       | Defined by                                                                                                                    |
| :------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| [options](#options) | `string` | Optional | cannot be null | [spack schema version](spack-definitions-load-properties-options.md "spack.schema.json#/definitions/load/properties/options") |
| [specs](#specs)     | `array`  | Optional | cannot be null | [spack schema version](definitions-definitions-list_of_strings.md "spack.schema.json#/definitions/load/properties/specs")     |

## options

Pass options to `spack load` command

`options`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [spack schema version](spack-definitions-load-properties-options.md "spack.schema.json#/definitions/load/properties/options")

### options Type

`string`

## specs

List of specs to install using `spack load` command

`specs`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [spack schema version](definitions-definitions-list_of_strings.md "spack.schema.json#/definitions/load/properties/specs")

### specs Type

`string[]`

### specs Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
