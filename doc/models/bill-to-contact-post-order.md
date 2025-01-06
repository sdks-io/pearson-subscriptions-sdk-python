
# Bill to Contact Post Order

Contact details associated with an account.

## Structure

`BillToContactPostOrder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_1` | `str` | Optional | First line of the contact's address. This is often a street address or a business name.<br>**Constraints**: *Maximum Length*: `255` |
| `address_2` | `str` | Optional | Second line of the contact's address.<br>**Constraints**: *Maximum Length*: `255` |
| `city` | `str` | Optional | City of the contact's address.<br>**Constraints**: *Maximum Length*: `40` |
| `country` | `str` | Optional | Country; must be a valid country name or abbreviation. If using Zuora Tax, you must specify a country in the bill-to contact to calculate tax.<br>**Constraints**: *Maximum Length*: `64` |
| `county` | `str` | Optional | County of the contact's address.<br>**Constraints**: *Maximum Length*: `32` |
| `first_name` | `str` | Optional | First name of the contact.<br>**Constraints**: *Maximum Length*: `100` |
| `last_name` | `str` | Optional | Last name of the contact.<br>**Constraints**: *Maximum Length*: `100` |
| `mobile_phone` | `str` | Optional | Mobile phone number of the contact.<br>**Constraints**: *Maximum Length*: `40` |
| `personal_email` | `str` | Optional | Personal email address of the contact.<br>**Constraints**: *Maximum Length*: `80` |
| `postal_code` | `str` | Optional | ZIP code or other postal code of the contact's address.<br>**Constraints**: *Maximum Length*: `20` |
| `state` | `str` | Optional | State or province of the contact's address.<br>**Constraints**: *Maximum Length*: `40` |
| `work_email` | `str` | Optional | Business email address of the contact.<br>**Constraints**: *Maximum Length*: `80` |
| `work_phone` | `str` | Optional | Business phone number of the contact.<br>**Constraints**: *Maximum Length*: `40` |

## Example (as JSON)

```json
{
  "address1": "1051 E Hillsdale Blvd",
  "address2": "Santon street main",
  "city": "Durham",
  "country": "United States",
  "county": "Durham",
  "firstName": "Alex",
  "lastName": "Matthew",
  "mobilePhone": "1234567890",
  "personalEmail": "personal@email.com",
  "postalCode": "27703",
  "state": "NC",
  "workPhone": "1234567890"
}
```

