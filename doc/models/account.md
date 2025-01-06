
# Account

The information of the new account to be created with the order. Note
that this actually specifies the invoice owner account of the
subscriptions included in this order. To create the new account,
either a **creditCard** structure or the
**hpmCreditCardPaymentMethodId** field (but not both) should be
provided. The one provided becomes the default payment method for this
account. If the credit card information is declined or can't be
verified, then the account is not created.

## Structure

`Account`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | **Constraints**: *Maximum Length*: `70` |
| `additional_email_addresses` | `str` | Optional | List of additional email addresses to receive emailed invoices. Values should be a comma-separated list of email addresses.<br>**Constraints**: *Maximum Length*: `1200` |
| `customer_service_rep_name` | `str` | Optional | Name of the account's customer service representative, if applicable.<br>**Constraints**: *Maximum Length*: `50` |
| `purchase_order_number` | `str` | Optional | The number of the purchase order associated with this account. Purchase order information generally comes from customers.<br>**Constraints**: *Maximum Length*: `100` |
| `sales_rep` | `str` | Optional | The name of the sales representative associated with this account, if applicable.<br>**Constraints**: *Maximum Length*: `50` |
| `sequence_set_id` | `str` | Optional | The ID of the billing document sequence set to assign to the customer account.<br><br>The billing documents to generate for this account will adopt the prefix and starting document number configured in the sequence set. |
| `allow_invoice_edit` | `bool` | Optional | Indicates if associated invoices can be edited.<br>Values are:<br><br>* `true`<br>* `false` (default)<br>**Default**: `False` |
| `name` | `str` | Optional | **Constraints**: *Maximum Length*: `255` |
| `currency` | `str` | Optional | 3 uppercase character currency code |
| `bill_cycle_day` | `int` | Optional | Day of the month that the account prefers billing periods to begin on. If set to 0, the bill cycle day will be set as "AutoSet".<br>**Constraints**: `>= 0`, `<= 31` |
| `invoice_delivery_prefs_print` | `bool` | Optional | Specifies whether to turn on the invoice delivery method 'Print' for the new account.<br>Values are:<br><br>* `true`. Turn on the invoice delivery method 'Print' for the new account.<br>* `false` (default). Turn off the invoice delivery method 'Print' for the new account.<br>**Default**: `False` |
| `invoice_delivery_prefs_email` | `bool` | Optional | Specifies whether to turn on the invoice delivery method 'Email' for the new account.<br>Values are:<br><br>* `true` (default). Turn on the invoice delivery method 'Email' for the new account.<br>* `false`. Turn off the invoice delivery method 'Email' for the new account.<br>**Default**: `False` |
| `auto_pay` | `bool` | Optional | Specifies whether future payments are to be automatically billed when they are due. Possible values are `true`, `false`.<br>**Default**: `True` |
| `payment_term` | `str` | Optional | - |
| `communication_profile_id` | `str` | Optional | aaa. |
| `batch` | `str` | Optional | Organizes your customer accounts into groups to optimize your billing and payment operations. |
| `invoice_template_id` | `str` | Optional | Invoice template ID, configured in Billing Settings. |
| `debit_memo_template_id` | `str` | Optional | The unique ID of the debit memo template, configured in Billing Settings. |
| `credit_memo_template_id` | `str` | Optional | The unique ID of the credit memo template, configured in Billing Settings. |
| `bill_to_contact` | [`BillToContactPostOrder`](../../doc/models/bill-to-contact-post-order.md) | Optional | - |
| `sold_to_contact` | [`BillToContactPostOrder`](../../doc/models/bill-to-contact-post-order.md) | Optional | - |

## Example (as JSON)

```json
{
  "accountNumber": "1234567890",
  "additionalEmailAddresses": "sample@email.com",
  "customerServiceRepName": "Alex Cutter",
  "purchaseOrderNumber": "q12345",
  "salesRep": "Alex Cutter",
  "sequenceSetId": "1",
  "allowInvoiceEdit": false,
  "name": "Demo test Account",
  "currency": "USD",
  "invoiceDeliveryPrefsPrint": false,
  "invoiceDeliveryPrefsEmail": false,
  "autoPay": true,
  "paymentTerm": "Due Upon Receipt",
  "communicationProfileId": "c123",
  "batch": "b1",
  "invoiceTemplateId": "in1",
  "debitMemoTemplateId": "dm1",
  "creditMemoTemplateId": "cm1"
}
```

