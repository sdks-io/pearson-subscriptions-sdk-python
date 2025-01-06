
# Cancel Req Type

## Structure

`CancelReqType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Required | Subscription id |
| `subscription_source` | [`SubscriptionSourceEnum`](../../doc/models/subscription-source-enum.md) | Required | Internal or external |
| `cancel_reason` | `str` | Required | Reason for subscription cancel |
| `cancel_date` | `str` | Required | cancellation date |

## Example (as JSON)

```json
{
  "subscriptionId": "urn:pearson:gps:subs:649e7109fc57341ba129e23",
  "subscriptionSource": "Internal",
  "cancelReason": "No longer need service",
  "cancelDate": "2023-06-30"
}
```

