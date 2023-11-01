# Untitled string in script schema version Schema

```txt
script.schema.json#/properties/container/properties/platform
```

Specify a container platform to use when running test. This is used for running commands inside container.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                               |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [script.schema.json\*](../out/script.schema.json "open original schema") |

## platform Type

`string`

## platform Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"docker"`      |             |
| `"podman"`      |             |
| `"singularity"` |             |
