
# Rate Plan End Date

## Structure

`RatePlanEndDate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end_date_condition` | [`EndDateConditionEnum`](../../doc/models/end-date-condition-enum.md) | Optional | enum values are "Subscription_End" "Fixed_Period" "Specific_End_Date" |
| `specific_end_date` | `date` | Optional | - |
| `up_to_periods` | `float` | Optional | Duration of the charge in billing periods, days, weeks, months, or years, depending on the value of the upToPeriodsType field. Only applicable if the value of the endDateCondition field is Fixed_Period. |
| `up_to_periods_type` | [`UpToPeriodsTypeEnum`](../../doc/models/up-to-periods-type-enum.md) | Optional | Unit of time that the charge duration is measured in. Only applicable if the value of the endDateCondition field is Fixed_Period. |

## Example (as JSON)

```json
{
  "endDateCondition": "Fixed_Period",
  "specificEndDate": "2016-03-13",
  "upToPeriods": 77.86,
  "upToPeriodsType": "Billing_Periods"
}
```

