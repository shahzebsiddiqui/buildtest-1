# Untitled string in JSON Schema Definitions File.  Schema

```txt
definitions.schema.json#/definitions/status/properties/slurm_job_state
```

This field can be used for checking Slurm Job State, if there is a match buildtest will report as `PASS`

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [definitions.schema.json*](../out/definitions.schema.json "open original schema") |

## slurm_job_state Type

`string`

## slurm_job_state Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"COMPLETED"`     |             |
| `"FAILED"`        |             |
| `"OUT_OF_MEMORY"` |             |
| `"TIMEOUT"`       |             |
