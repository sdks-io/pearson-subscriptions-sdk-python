
# Update or Add Product Charge Override

## Structure

`UpdateOrAddProductChargeOverride`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_rate_plan_charge_id` | `str` | Optional | This is unique rate plan charge id respective to rate plan id. It signifies the subscription type,entitlementLevel,maxEntitlements,numEntitlements etc.<br>**Constraints**: *Minimum Length*: `1` |
| `customer_facing_custom_fields` | [`CustomerFacingCustomFields`](../../doc/models/customer-facing-custom-fields.md) | Optional | - |
| `overrides_pricing` | [`OverridesPricing`](../../doc/models/overrides-pricing.md) | Optional | - |
| `add_product_end_date` | [`AddProductEndDate`](../../doc/models/add-product-end-date.md) | Optional | - |

## Example (as JSON)

```json
{
  "productRatePlanChargeId": "productRatePlanChargeId8",
  "customerFacingCustomFields": {
    "customerFacing__c": "customerFacing__c0"
  },
  "overridesPricing": {
    "discount": {
      "discountAmount": 252.52,
      "discountPercentage": 13.42
    }
  },
  "addProductEndDate": {
    "endDateCondition": "Specific_End_Date",
    "specificEndDate": "specificEndDate0",
    "upToPeriods": 155.16,
    "upToPeriodsType": "upToPeriodsType0"
  }
}
```

