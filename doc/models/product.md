
# Product

## Structure

`Product`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `isbn` | `str` | Optional | product isbn number |
| `ppid` | `str` | Optional | product ppid number |
| `duration` | `float` | Optional | Duration of the entitlement in days for this product |
| `end_date` | `str` | Optional | end date for the entitlement. in yyyy-MM-dd'T'HH:mm:ss.SSSZ format. |
| `tax` | `float` | Optional | Cost of tax on the product |
| `price` | `float` | Optional | Cost of the product |

## Example (as JSON)

```json
{
  "isbn": "isbn8",
  "ppid": "ppid0",
  "duration": 117.0,
  "endDate": "endDate6",
  "tax": 72.48
}
```

