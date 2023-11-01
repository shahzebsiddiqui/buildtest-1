# Untitled object in JSON Schema Definitions File.  Schema

```txt
definitions.schema.json#/definitions/status/properties/assert_range
```

Perform assertion based on lower and upper bound

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [definitions.schema.json\*](../out/definitions.schema.json "open original schema") |

## assert\_range Type

`object` ([Details](definitions-definitions-status-properties-assert_range.md))

# assert\_range Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                      |
| :-------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [mode](#mode)               | `string` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_range-properties-mode.md "definitions.schema.json#/definitions/status/properties/assert_range/properties/mode")               |
| [comparisons](#comparisons) | `array`  | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_range-properties-comparisons.md "definitions.schema.json#/definitions/status/properties/assert_range/properties/comparisons") |

## mode

Determine how the status check is resolved, for instance it can be logical AND or OR

`mode`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_range-properties-mode.md "definitions.schema.json#/definitions/status/properties/assert_range/properties/mode")

### mode Type

`string`

### mode Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"or"`  |             |
| `"and"` |             |
| `"OR"`  |             |
| `"AND"` |             |

## comparisons



`comparisons`

*   is required

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_range-properties-comparisons-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_range-properties-comparisons.md "definitions.schema.json#/definitions/status/properties/assert_range/properties/comparisons")

### comparisons Type

`object[]` ([Details](definitions-definitions-status-properties-assert_range-properties-comparisons-items.md))
