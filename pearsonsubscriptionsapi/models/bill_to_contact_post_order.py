# -*- coding: utf-8 -*-

"""
pearsonsubscriptionsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pearsonsubscriptionsapi.api_helper import APIHelper


class BillToContactPostOrder(object):

    """Implementation of the 'BillToContactPostOrder' model.

    Contact details associated with an account.

    Attributes:
        address_1 (str): First line of the contact's address. This is often a
            street address or a business name.
        address_2 (str): Second line of the contact's address.
        city (str): City of the contact's address.
        country (str): Country; must be a valid country name or abbreviation.
            If using Zuora Tax, you must specify a country in the bill-to
            contact to calculate tax.
        county (str): County of the contact's address.
        first_name (str): First name of the contact.
        last_name (str): Last name of the contact.
        mobile_phone (str): Mobile phone number of the contact.
        personal_email (str): Personal email address of the contact.
        postal_code (str): ZIP code or other postal code of the contact's
            address.
        state (str): State or province of the contact's address.
        work_email (str): Business email address of the contact.
        work_phone (str): Business phone number of the contact.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_1": 'address1',
        "address_2": 'address2',
        "city": 'city',
        "country": 'country',
        "county": 'county',
        "first_name": 'firstName',
        "last_name": 'lastName',
        "mobile_phone": 'mobilePhone',
        "personal_email": 'personalEmail',
        "postal_code": 'postalCode',
        "state": 'state',
        "work_email": 'workEmail',
        "work_phone": 'workPhone'
    }

    _optionals = [
        'address_1',
        'address_2',
        'city',
        'country',
        'county',
        'first_name',
        'last_name',
        'mobile_phone',
        'personal_email',
        'postal_code',
        'state',
        'work_email',
        'work_phone',
    ]

    def __init__(self,
                 address_1=APIHelper.SKIP,
                 address_2=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 county=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 mobile_phone=APIHelper.SKIP,
                 personal_email=APIHelper.SKIP,
                 postal_code=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 work_email=APIHelper.SKIP,
                 work_phone=APIHelper.SKIP):
        """Constructor for the BillToContactPostOrder class"""

        # Initialize members of the class
        if address_1 is not APIHelper.SKIP:
            self.address_1 = address_1 
        if address_2 is not APIHelper.SKIP:
            self.address_2 = address_2 
        if city is not APIHelper.SKIP:
            self.city = city 
        if country is not APIHelper.SKIP:
            self.country = country 
        if county is not APIHelper.SKIP:
            self.county = county 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if mobile_phone is not APIHelper.SKIP:
            self.mobile_phone = mobile_phone 
        if personal_email is not APIHelper.SKIP:
            self.personal_email = personal_email 
        if postal_code is not APIHelper.SKIP:
            self.postal_code = postal_code 
        if state is not APIHelper.SKIP:
            self.state = state 
        if work_email is not APIHelper.SKIP:
            self.work_email = work_email 
        if work_phone is not APIHelper.SKIP:
            self.work_phone = work_phone 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        address_1 = dictionary.get("address1") if dictionary.get("address1") else APIHelper.SKIP
        address_2 = dictionary.get("address2") if dictionary.get("address2") else APIHelper.SKIP
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        county = dictionary.get("county") if dictionary.get("county") else APIHelper.SKIP
        first_name = dictionary.get("firstName") if dictionary.get("firstName") else APIHelper.SKIP
        last_name = dictionary.get("lastName") if dictionary.get("lastName") else APIHelper.SKIP
        mobile_phone = dictionary.get("mobilePhone") if dictionary.get("mobilePhone") else APIHelper.SKIP
        personal_email = dictionary.get("personalEmail") if dictionary.get("personalEmail") else APIHelper.SKIP
        postal_code = dictionary.get("postalCode") if dictionary.get("postalCode") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        work_email = dictionary.get("workEmail") if dictionary.get("workEmail") else APIHelper.SKIP
        work_phone = dictionary.get("workPhone") if dictionary.get("workPhone") else APIHelper.SKIP
        # Return an object of this model
        return cls(address_1,
                   address_2,
                   city,
                   country,
                   county,
                   first_name,
                   last_name,
                   mobile_phone,
                   personal_email,
                   postal_code,
                   state,
                   work_email,
                   work_phone)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'address_1={self.address_1!r}, '
                f'address_2={self.address_2!r}, '
                f'city={self.city!r}, '
                f'country={self.country!r}, '
                f'county={self.county!r}, '
                f'first_name={self.first_name!r}, '
                f'last_name={self.last_name!r}, '
                f'mobile_phone={self.mobile_phone!r}, '
                f'personal_email={self.personal_email!r}, '
                f'postal_code={self.postal_code!r}, '
                f'state={self.state!r}, '
                f'work_email={self.work_email!r}, '
                f'work_phone={self.work_phone!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'address_1={self.address_1!s}, '
                f'address_2={self.address_2!s}, '
                f'city={self.city!s}, '
                f'country={self.country!s}, '
                f'county={self.county!s}, '
                f'first_name={self.first_name!s}, '
                f'last_name={self.last_name!s}, '
                f'mobile_phone={self.mobile_phone!s}, '
                f'personal_email={self.personal_email!s}, '
                f'postal_code={self.postal_code!s}, '
                f'state={self.state!s}, '
                f'work_email={self.work_email!s}, '
                f'work_phone={self.work_phone!s})')
