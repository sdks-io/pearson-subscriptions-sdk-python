
# Add Product End Date

## Structure

`AddProductEndDate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end_date_condition` | [`EndDateConditionEnum`](../../doc/models/end-date-condition-enum.md) | Optional | enum values are "Subscription_End" "Fixed_Period" "Specific_End_Date" |
| `specific_end_date` | `str` | Optional | - |
| `up_to_periods` | `float` | Optional | - |
| `up_to_periods_type` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "endDateCondition": "Fixed_Period",
  "specificEndDate": "specificEndDate8",
  "upToPeriods": 47.48,
  "upToPeriodsType": "upToPeriodsType2"
}
```

