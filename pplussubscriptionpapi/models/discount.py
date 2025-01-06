# -*- coding: utf-8 -*-

"""
pplussubscriptionpapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pplussubscriptionpapi.api_helper import APIHelper


class Discount(object):

    """Implementation of the 'Discount' model.

    TODO: type model description here.

    Attributes:
        discount_amount (float): Only applicable if the discount charge is a
            fixed-amount discount.
        discount_percentage (float): Only applicable if the discount charge is
            a percentage discount

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "discount_amount": 'discountAmount',
        "discount_percentage": 'discountPercentage'
    }

    _optionals = [
        'discount_amount',
        'discount_percentage',
    ]

    def __init__(self,
                 discount_amount=APIHelper.SKIP,
                 discount_percentage=APIHelper.SKIP):
        """Constructor for the Discount class"""

        # Initialize members of the class
        if discount_amount is not APIHelper.SKIP:
            self.discount_amount = discount_amount 
        if discount_percentage is not APIHelper.SKIP:
            self.discount_percentage = discount_percentage 

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
        discount_amount = dictionary.get("discountAmount") if dictionary.get("discountAmount") else APIHelper.SKIP
        discount_percentage = dictionary.get("discountPercentage") if dictionary.get("discountPercentage") else APIHelper.SKIP
        # Return an object of this model
        return cls(discount_amount,
                   discount_percentage)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'discount_amount={self.discount_amount!r}, '
                f'discount_percentage={self.discount_percentage!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'discount_amount={self.discount_amount!s}, '
                f'discount_percentage={self.discount_percentage!s})')