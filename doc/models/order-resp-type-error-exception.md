
# Order Resp Type Error Exception

## Structure

`OrderRespTypeErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_number` | `str` | Optional | Order Number. |
| `subscription_id` | `str` | Optional | Pearson subscription id. |
| `order_resp_error` | [`OrderRespError`](../../doc/models/order-resp-error.md) | Optional | - |

## Example (as JSON)

```json
{
  "orderNumber": "S12345",
  "subscriptionId": "S12345",
  "orderRespError": {
    "code": "E40",
    "message": "message6"
  }
}
```

