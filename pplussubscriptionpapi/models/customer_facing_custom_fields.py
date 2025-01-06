# -*- coding: utf-8 -*-

"""
pplussubscriptionpapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pplussubscriptionpapi.api_helper import APIHelper


class CustomerFacingCustomFields(object):

    """Implementation of the 'CustomerFacingCustomFields' model.

    TODO: type model description here.

    Attributes:
        customer_facing__c (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_facing__c": 'customerFacing__c'
    }

    _optionals = [
        'customer_facing__c',
    ]

    def __init__(self,
                 customer_facing__c=APIHelper.SKIP):
        """Constructor for the CustomerFacingCustomFields class"""

        # Initialize members of the class
        if customer_facing__c is not APIHelper.SKIP:
            self.customer_facing__c = customer_facing__c 

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
        customer_facing__c = dictionary.get("customerFacing__c") if dictionary.get("customerFacing__c") else APIHelper.SKIP
        # Return an object of this model
        return cls(customer_facing__c)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'customer_facing__c={self.customer_facing__c!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'customer_facing__c={self.customer_facing__c!s})')
