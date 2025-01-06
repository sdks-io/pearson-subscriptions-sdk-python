
# Rate Plan Pricing

## Structure

`RatePlanPricing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `discount` | [`Discount`](../../doc/models/discount.md) | Optional | - |
| `recurring_flat_fee` | [`RecurringFlatFee`](../../doc/models/recurring-flat-fee.md) | Optional | - |

## Example (as JSON)

```json
{
  "discount": {
    "discountAmount": 252.52,
    "discountPercentage": 13.42
  },
  "recurringFlatFee": {
    "listPrice": 233.52
  }
}
```
