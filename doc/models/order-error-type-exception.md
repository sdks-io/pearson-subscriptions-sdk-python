
# Order Error Type Exception

## Structure

`OrderErrorTypeException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_number` | `str` | Optional | Order Number. |
| `order_error` | [`OrderError`](../../doc/models/order-error.md) | Optional | - |

## Example (as JSON)

```json
{
  "orderNumber": "S12345",
  "orderError": {
    "code": "code4",
    "message": "message6"
  }
}
```

