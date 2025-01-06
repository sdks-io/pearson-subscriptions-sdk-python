
# Order Request Type Product

## Structure

`OrderRequestTypeProduct`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `isbn` | `str` | Optional | product isbn value<br>**Constraints**: *Minimum Length*: `1` |
| `ppid` | `str` | Optional | product ppid value<br>**Constraints**: *Minimum Length*: `1` |
| `duration` | `float` | Optional | Duration of the entitlement in days for this product |
| `tax` | `float` | Optional | Cost of tax on the product |
| `price` | `float` | Optional | Cost of the product |

## Example (as JSON)

```json
{
  "isbn": "isbn2",
  "ppid": "ppid6",
  "duration": 32.56,
  "tax": 244.04,
  "price": 147.92
}
```

