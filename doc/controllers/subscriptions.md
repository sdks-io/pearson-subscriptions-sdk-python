# Subscriptions

```python
subscriptions_controller = client.subscriptions
```

## Class Name

`SubscriptionsController`

## Methods

* [Aggregate Subscription](../../doc/controllers/subscriptions.md#aggregate-subscription)
* [Update Subscription](../../doc/controllers/subscriptions.md#update-subscription)
* [Cancel Subscription](../../doc/controllers/subscriptions.md#cancel-subscription)
* [Expire Subscriptions](../../doc/controllers/subscriptions.md#expire-subscriptions)


# Aggregate Subscription

```python
def aggregate_subscription(self,
                          x_user_id,
                          x_authorization,
                          body,
                          x_transaction_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_user_id` | `str` | Header, Required | UserId of an user who bought a subscription. This will be an IES userId |
| `x_authorization` | `str` | Header, Required | This will be an IES system token |
| `body` | [`OrderRequestType`](../../doc/models/order-request-type.md) | Body, Required | Data |
| `x_transaction_id` | `str` | Header, Optional | Unique ID for a transaction |

## Response Type

[`OrderRespType`](../../doc/models/order-resp-type.md)

## Example Usage

```python
x_user_id = 'X-UserId4'

x_authorization = 'X-Authorization6'

body = OrderRequestType(
    order_number='10034567',
    description='Sample description of the API',
    subscription_model_name='Mojo',
    store_code='US',
    swap_title=False,
    send_email=True,
    order_request_type_products=[
        OrderRequestTypeProduct(
            isbn='4280134085545',
            ppid='A101702992101'
        ),
        OrderRequestTypeProduct(
            isbn='4280134085546',
            ppid='A101702992102'
        )
    ],
    custom_fields=[
        CustomField(
            name='paymentMethod__c',
            value='CREDIT CARD'
        ),
        CustomField(
            name='paymentInfo__c',
            value='CREDIT CARD'
        ),
        CustomField(
            name='paymentToken__c',
            value='4111111111111111'
        ),
        CustomField(
            name='iesId__c',
            value='ea9mmnj1qe2tghnb3'
        ),
        CustomField(
            name='hybrisAccountNumber__c',
            value='456'
        ),
        CustomField(
            name='tepAccountNumber__c',
            value='c123'
        ),
        CustomField(
            name='institutionId__c',
            value='5678'
        ),
        CustomField(
            name='tepPartyId__c',
            value='GH6789'
        ),
        CustomField(
            name='campaignName__c',
            value='test val'
        ),
        CustomField(
            name='promoCode__c',
            value='PM10'
        ),
        CustomField(
            name='couponCode__c',
            value='BA10'
        ),
        CustomField(
            name='discountCodeStartDate__c',
            value='2021-09-21'
        ),
        CustomField(
            name='discountCodeEndDate__c',
            value='2021-11-21'
        ),
        CustomField(
            name='amountBeforeTax__c',
            value='9.99'
        ),
        CustomField(
            name='discountedAmountBeforeTax__c',
            value='9.99'
        ),
        CustomField(
            name='subscriptionSource__c',
            value='channel_partner'
        ),
        CustomField(
            name='upFrontPayment__c',
            value='true'
        ),
        CustomField(
            name='embeddedPromoCode__c',
            value='string'
        ),
        CustomField(
            name='discountCodeDescription__c',
            value='string'
        )
    ]
)

result = subscriptions_controller.aggregate_subscription(
    x_user_id,
    x_authorization,
    body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`InvalidReqTypeException`](../../doc/models/invalid-req-type-exception.md) |
| 401 | Unauthorized | [`AuthErrorTypeException`](../../doc/models/auth-error-type-exception.md) |
| 500 | Error | [`OrderRespTypeErrorException`](../../doc/models/order-resp-type-error-exception.md) |


# Update Subscription

```python
def update_subscription(self,
                       x_user_id,
                       x_authorization,
                       body,
                       x_transaction_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_user_id` | `str` | Header, Required | UserId of an user who bought a subscription. This will be an IES userId |
| `x_authorization` | `str` | Header, Required | This will be an IES system token |
| `body` | [`UpdateSubscription`](../../doc/models/update-subscription.md) | Body, Required | Data |
| `x_transaction_id` | `str` | Header, Optional | Unique ID for a transaction |

## Response Type

[`OrderRespType`](../../doc/models/order-resp-type.md)

## Example Usage

```python
x_user_id = 'X-UserId4'

x_authorization = 'X-Authorization6'

body = UpdateSubscription(
    order_type=OrderTypeEnum.UPGRADE,
    order_number='10034567',
    description='Sample description of the API',
    existing_account_number='A000000001',
    update_subscription_products=[
        Product(
            isbn='20045634128',
            ppid='A101702992101',
            end_date='2021-05-14T07:12:27.152-0500'
        ),
        Product(
            isbn='10045634128',
            ppid='A101702992102',
            end_date='2021-05-14T07:12:27.152-0500'
        )
    ],
    custom_fields=[
        CustomField(
            name='paymentMethod__c',
            value='CREDIT CARD'
        ),
        CustomField(
            name='paymentInfo__c',
            value='CREDIT CARD'
        ),
        CustomField(
            name='paymentToken__c',
            value='4111111111111111'
        ),
        CustomField(
            name='iesId__c',
            value='ea9mmnj1qe2tghnb3'
        ),
        CustomField(
            name='hybrisAccountNumber__c',
            value='456'
        ),
        CustomField(
            name='tepAccountNumber__c',
            value='c123'
        ),
        CustomField(
            name='institutionId__c',
            value='5678'
        ),
        CustomField(
            name='tepPartyId__c',
            value='GH6789'
        ),
        CustomField(
            name='campaignName__c',
            value='test val'
        ),
        CustomField(
            name='promoCode__c',
            value='PM10'
        ),
        CustomField(
            name='couponCode__c',
            value='BA10'
        ),
        CustomField(
            name='discountCodeStartDate__c',
            value='2021-09-21'
        ),
        CustomField(
            name='discountCodeEndDate__c',
            value='2021-11-21'
        ),
        CustomField(
            name='amountBeforeTax__c',
            value='9.99'
        ),
        CustomField(
            name='discountedAmountBeforeTax__c',
            value='9.99'
        ),
        CustomField(
            name='subscriptionSource__c',
            value='channel_partner'
        ),
        CustomField(
            name='upFrontPayment__c',
            value='true'
        ),
        CustomField(
            name='embeddedPromoCode__c',
            value='string'
        ),
        CustomField(
            name='discountCodeDescription__c',
            value='string'
        )
    ]
)

result = subscriptions_controller.update_subscription(
    x_user_id,
    x_authorization,
    body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`InvalidReqTypeException`](../../doc/models/invalid-req-type-exception.md) |
| 401 | Unauthorized | [`AuthErrorTypeException`](../../doc/models/auth-error-type-exception.md) |
| 500 | Error | [`OrderErrorTypeException`](../../doc/models/order-error-type-exception.md) |


# Cancel Subscription

Cancel subscription for a given subscription ID

```python
def cancel_subscription(self,
                       user_id,
                       x_authorization,
                       body,
                       x_transaction_id=None,
                       origin=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `str` | Header, Required | UserId of an user who bought a subscription. This will be an IES userId |
| `x_authorization` | `str` | Header, Required | This will be an IES system token |
| `body` | [`CancelReqType`](../../doc/models/cancel-req-type.md) | Body, Required | Data |
| `x_transaction_id` | `str` | Header, Optional | Unique ID for a transaction |
| `origin` | `str` | Header, Optional | Originating System |

## Response Type

[`CancelResType`](../../doc/models/cancel-res-type.md)

## Example Usage

```python
user_id = 'userId0'

x_authorization = 'X-Authorization6'

body = CancelReqType(
    subscription_id='urn:pearson:gps:subs:649e7109fc57341ba129e23',
    subscription_source=SubscriptionSourceEnum.INTERNAL,
    cancel_reason='No longer need service',
    cancel_date='2023-06-30'
)

result = subscriptions_controller.cancel_subscription(
    user_id,
    x_authorization,
    body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`InvalidReqTypeException`](../../doc/models/invalid-req-type-exception.md) |
| 401 | Unauthorized | [`AuthErrorTypeException`](../../doc/models/auth-error-type-exception.md) |
| 500 | Error | [`OrderErrorTypeException`](../../doc/models/order-error-type-exception.md) |


# Expire Subscriptions

Expire subscription for all past enddate internal and IA subscriptions

```python
def expire_subscriptions(self)
```

## Response Type

[`CancelResType`](../../doc/models/cancel-res-type.md)

## Example Usage

```python
result = subscriptions_controller.expire_subscriptions()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`InvalidReqTypeException`](../../doc/models/invalid-req-type-exception.md) |
| 401 | Unauthorized | [`AuthErrorTypeException`](../../doc/models/auth-error-type-exception.md) |
| 500 | Error | [`OrderErrorTypeException`](../../doc/models/order-error-type-exception.md) |

