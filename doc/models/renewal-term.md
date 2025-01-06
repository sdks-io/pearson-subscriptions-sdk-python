
# Renewal Term

## Structure

`RenewalTerm`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `period` | `int` | Optional | Duration of the renewal term in months, years, days, or weeks, depending on the value of the `periodType` field. |
| `period_type` | [`PeriodTypeEnum`](../../doc/models/period-type-enum.md) | Optional | Unit of time that the renewal term is measured in. |

## Example (as JSON)

```json
{
  "period": 102,
  "periodType": "Day"
}
```
